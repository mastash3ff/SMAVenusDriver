class BatteryChargerState(object):
    """Battery Charger Finite State Machine that represents all states:  Bulk, Absorption, Float.
    """

    def __init__(self, bv, mc, av):
        self.new_state(BulkBatteryChargerState)
        self.battery_voltage = bv
        self.max_current = mc
        self.absorption_voltage = av

    def new_state(self, new_state):
        self.__class__ = new_state

    def action(self, a):
        raise NotImplementedError()


class BulkBatteryChargerState(BatteryChargerState):
    """
    Charge at the max current set until a voltage threshold (called absorption voltage) is hit. Transition to Absorption state.
    """

    def action(self, a):
        # TODO
        raise NotImplementedError()
        self.new_state(AbsorptionBatteryChargerState)


class AbsorptionBatteryChargerState(BatteryChargerState):
    """
    Maintain the absorption voltage level by reducing or increasing charge current as required to drive the battery
    up or down to the  absorption voltage threshold. Do this for a pre-set amount of time, then transition to float
    state.
    """

    def action(self, a):
        # TODO
        raise NotImplementedError()
        self.new_state(FloatBatteryChargerState)


class FloatBatteryChargerState(BatteryChargerState):
    """
    Same as  Absorption state but with a different (lower) voltage threshold.  Do this indefinitely.
    """

    def action(self, a):
        # TODO
        raise NotImplementedError()
