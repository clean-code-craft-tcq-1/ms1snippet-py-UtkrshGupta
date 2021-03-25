import sensorActions as sa

def call_controller(param_name):
    if sa.get_sensor_status(param_name) == 'OFF':
        sa.set_sensor_status(param_name, 'ON')
        print('{} sensor was off, controller made the sensor running again'.format(param_name.upper()))
        return "SENSOR_UP_AGAIN"
    else: 
        print('{} sensor is not working'.format(param_name.upper()))
        return None
