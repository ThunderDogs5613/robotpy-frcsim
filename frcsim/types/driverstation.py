
import functools

from ..msgs.driver_station_pb2 import DriverStation
from ..msgs.joystick_pb2 import Joystick

import hal
from hal_impl.data import hal_data
from hal_impl import mode_helpers

class DriverStationControl:

    def __init__(self, controller):

        controller.subscribe('ds/state',
                             'gazebo.msgs.DriverStation',
                             self.on_state)

        for i in range(6):
            controller.subscribe('ds/joysticks/%s' % i,
                                 'gazebo.msgs.Joystick',
                                 functools.partial(self.on_joystick, i))

        self.state = None
        self.enabled = None
        hal_data["control"]['has_source'] = True

    def on_joystick(self, idx, msg):
        
        js = hal_data['joysticks'][idx]
        buttons = js['buttons']
        axes = js['axes']
        js['has_source'] = True
        
        msg = Joystick.FromString(msg)
        
        # super inefficient, but could be worse..
        # -> probably will be bit by race conditions here 
        for i, (a, _) in enumerate(zip(msg.axes, axes)):
            axes[i] = a
            
        for i, (b, _) in enumerate(zip(msg.buttons, buttons)):
            buttons[i] = b

        mode_helpers.notify_new_ds_data()

    def on_state(self, msg):
        state = DriverStation.FromString(msg)
        
        if self.state != state.state or self.enabled != state.enabled:
            
            if state.state == DriverStation.TEST:
                mode_helpers.set_test_mode(state.enabled)
            elif state.state == DriverStation.AUTO:
                mode_helpers.set_autonomous(state.enabled)
            elif state.state == DriverStation.TELEOP:
                mode_helpers.set_teleop_mode(state.enabled)
            
            self.state = state.state
            self.enabled = state.enabled
    