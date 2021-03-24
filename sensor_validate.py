from math import isnan
from sensorController import call_controller

def track_param_jumping_limit(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_param_reading(values, param_name, param_jump_threshold):
  last_but_one_reading = get_relevant_length(values)
  for i in range(last_but_one_reading):
    if(not track_param_jumping_limit(values[i], values[i + 1], param_jump_threshold)):    
      return False
  return checkInputIsEmpty(values, param_name)

def get_relevant_length(values):
    total_values = len(values)
    if total_values != 0:
        return total_values - 1
    else:
        return total_values

def checkInputIsEmpty(values, param_name):
    input_length = len(values)
    if input_length == 0:
        return call_controller(param_name)
    else:
        return checkInputHasNanValue(values)

def checkInputHasNanValue(values):
    for value in values:
        value_is_nan = is_value_nan(value)
        if value_is_nan != False:
            return value_is_nan
    return True

def is_value_nan(value):
    if isnan(value):
        return 'NULL_VALUE'
    else:
        return False

