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

This works with two scripts (though it could've been made in one, this has been done so because it was initially a class assignment):
* `min_dist_detection.py` gathers the information from the `astra` laser sensor on the turtlebot and publishes it on `/my_dist`
* `sound_min_dist_feedback` subscribes to `/my_dist`, examines the distance, and beeps (= publishes on `/mobile_base/commands/sound`) faster or slower depending on how close of an obstacle it is.

In two terminals:

```
$ rosrun collision min_dist_detection.py
```

```
$ rosrun collision sound_min_dist_feedback.py 
```