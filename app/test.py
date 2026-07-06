from models.sensor import Sensor

sensor_fc = Sensor("ESF00000000fc2f4839", "8700", "4840", name="fc2f4839")
sensor_56 = Sensor("SES00000000567f49fa", "8700", "4840", name="567f49fa")

print(sensor_fc.get_link())
print(sensor_56.get_link())