all_sensor_status = {
                      'soc': 'ON',
                      'current': 'ON'
                     }

def get_sensor_status(param_name):
    return all_sensor_status[param_name]
    
def set_sensor_status(param_name, sensor_status):
     all_sensor_status[param_name] = sensor_status
    