# ARG RL Instructions

## Where to download RL model
```
ARG NAS/ arg-projectfile-download/robotx-2022/acme_model/vrx-v2.zip
```

## On GitHub
```
ARG-NCTU/robotx-2022/docs/Dynamic_Positioning/04-drl-inference.md
```

## How to run inference
```bash
~ cd robotx-2022/
~ source ipc_run.sh
＃ cd catkin_ws/
＃ catkin build -c
＃ source environment.sh
＃ roslaunch vrx_gazebo base_wamv_demo.launch # open gazebo
# in another tab
＃ source ipc_join.sh
＃ source environment.sh
＃ roslaunch vrx_gazebo usv_joydrive estop.launch veh:=wamv2
