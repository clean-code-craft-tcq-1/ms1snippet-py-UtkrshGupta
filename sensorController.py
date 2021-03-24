import sensorActions as sa

def call_controller(param_name):
    if sa.get_sensor_status(param_name) == False:
        sa.set_sensor_status(param_name, True)
        print('{} sensor was off, controller made the sensor running again'.format(param_name.upper()))
        return "SENSOR_UP_AGAIN"
    else: 
        print('Sensor is not working')
        return None
