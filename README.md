# turtlebot-simple-distance-beep
Simple ROS package to warn how close the turtlebot is to an obstacle

## Installation

Initialize a ROS workspace, then copy the files in `src` in your workspace's `src` folder, then remake and re-source the project:

```
$ mkdir -p <your-ws>/src
$ cd <your-ws>/src
$ catkin_make # eventually use python 3 with -DPYTHON_EXECUTABLE=/usr/bin/python3 for example
$ cp ../turtlebot-simple-distance-beep/src .
$ cd ..
$ catkin_make
$ source devel/setup.bash
```

## Run

This works with 3 scripts (though it could've been made in one, this has been done so because it was initially a class assignment):
* `collision_detection.py` gathers info from the bumper and publishes a sound if it got hit
* `min_dist_detection.py` gathers the information from the `astra` laser sensor on the turtlebot and publishes it on `/min_dist`
* `sound_min_dist_feedback` subscribes to `/min_dist`, examines the distance, and beeps (= publishes on `/mobile_base/commands/sound`) faster or slower depending on how close of an obstacle it is.

There is a fourth very simple script, `collision_prevention.py`, that takes every class and instantiates them all at once.

### Start everything at once

```
$ rosrun collision collision_prevention.py
```

### Start scripts separately

In different terminals:

```
$ rosrun collision collision_warning.py
```

```
$ rosrun collision min_dist_detection.py
```

```
$ rosrun collision sound_min_dist_feedback.py 
```