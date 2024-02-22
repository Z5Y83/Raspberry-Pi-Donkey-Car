# Raspberry-Pi-Donkey-Car  

This project is for learning raspberry pi and opencv.  
This project use raspberry pi 3B+ to make a donkey car, combined with opencv classifier to detect object. When donkey car detects an object, it will automatically move to that object.   

# Setup  
  `1. pip install opencv-python`
# some problems or error you may see  
1. error: externally-managed-environment  
   Ans: 1. open terminal  
        2. run `sudo nano /etc/pip.conf`  
        3. add `break-system-packages = true`  
        4. Ctrl+X then Y -> enter  
        5. pip install opencv-python  
   reference: https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3  
3. raspberry pi install GPIO  
   `sudo apt-get install rpi.gpio`  
   reference: https://www.cnblogs.com/ollie-lin/p/10336271.html

# Reference  
raspberry pi donkey car code: https://github.com/piepie-tw/pi-follower-car  
opencv(classifiers for detecting objects): https://github.com/opencv/opencv/tree/4.x/data  
cars.xml: https://github.com/andrewssobral/vehicle_detection_haarcascades/tree/master  
Draw bounding box and tutorial: https://steam.oxxostudio.tw/category/python/ai/ai-cars-dectection.html  
