### driver
```
https://www.wemos.cc/en/latest/ch340_driver.html
```
### mcu https://micropython.org/download/?mcu=esp32s3

### virtial environment set-up
```
python -m venv iot-env
```
```
iot-env/Script/activate
```
### installing necessary tools
```
pip install esptool
```
### Check the com port and erase flash(here my chip is esp32s3)
```
esptool --chip esp32s3 --port COM3 erase_flash
```
### Write MicroPython to esp32s3
```
esptool --chip esp32s3 --port COM3 write_flash -z 0 ESP32_GENERIC_S3-20241025-v1.24.0.bin
```

