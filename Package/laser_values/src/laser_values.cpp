#include "ros/ros.h"
#include"sensor_msgs/LaserScan.h"
void laser_callback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
    printf("The number of data is %d \n", msg->ranges.size());
};
int main(int argc,char** argv)
{
    ros::init(argc, argv, "laser_value");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("/scan", 10, laser_callback);
    ros::spin();
    return 0;
}