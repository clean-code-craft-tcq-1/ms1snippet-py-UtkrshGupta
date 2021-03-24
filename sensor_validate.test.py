import unittest
from sensor_validate import validate_param_reading
from sensorActions import set_sensor_status

soc_jump_threshold = 0.05
current_jump_threshold = 0.1

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    self.assertFalse(

      validate_param_reading([0.0, 0.01, 0.5, 0.51], 'soc', soc_jump_threshold)
    )
    self.assertTrue(

      validate_param_reading([0.1], 'soc', soc_jump_threshold)
    )   
    
    set_sensor_status('soc', False)
    self.assertEqual(
        validate_param_reading([], 'soc', soc_jump_threshold), 'SENSOR_UP_AGAIN', 'Sensor was off, suitable actions are handled by controller'
    )

    self.assertIsNone(
        validate_param_reading([], 'soc', soc_jump_threshold), 'Sensor is not working'
    )
    
    self.assertEqual(
        validate_param_reading([0.01, 0.02, float('nan')], 'soc', soc_jump_threshold) , 'NULL_VALUE'
    )
    
  def test_reports_error_when_current_jumps(self):
    self.assertFalse(
      validate_param_reading([0.03, 0.03, 0.03, 0.33], 'current', current_jump_threshold)
    ) 
    
    self.assertTrue(
      # sensor_validate.validate_current_reading([0.03, 0.03, 0.03, 0.33])
      validate_param_reading([0.1], 'current', current_jump_threshold)
    )   
    
    self.assertIsNone(
      validate_param_reading([], 'current', current_jump_threshold), 'Sensor is not working'
    )
    
    self.assertEqual(
      validate_param_reading([0.01, 0.02, float('nan')], 'current', current_jump_threshold) , 'NULL_VALUE'
    )
  
if __name__ == "__main__":
  unittest.main()
