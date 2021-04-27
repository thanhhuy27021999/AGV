#include "ros/ros.h"
#include "tf/transform_listener.h"
#include <iostream>
#include "geometry_msgs/PoseWithCovarianceStamped.h"

void PoseCallback(const geometry_msgs::PoseWithCovarianceStamped::ConstPtr& msg)
{
    ROS_INFO("The pose is: x= %f y = %f z = %f ",msg->pose.pose.position.x,msg->pose.pose.position.y,
    msg->pose.pose.position.z);
    ROS_INFO("orientation is x=%f y= %f z= %f w=%f ",msg->pose.pose.orientation.x, msg->pose.pose.orientation.y
    ,msg->pose.pose.orientation.z, msg->pose.pose.orientation.w);
    ros::param::set("/pose_x",msg->pose.pose.position.x);
    ros::param::set("/pose_y",msg->pose.pose.position.y);
    ros::param::set("/pose_z",msg->pose.pose.position.z);

    ros::param::set("/orie_x",msg->pose.pose.orientation.x);
    ros::param::set("/orie_y",msg->pose.pose.orientation.y);
    ros::param::set("/orie_z",msg->pose.pose.orientation.z);
    ros::param::set("/orie_w",msg->pose.pose.orientation.w);
    double x;
    ros::param::get("/pose_x",x);
    ROS_INFO("----- %f ",x);
};
int main(int argc,char** argv)
{
    ros::init(argc, argv, "take_position");
    ros::NodeHandle n;
    ros::Subscriber SubPose = n.subscribe("/amcl_pose",10,PoseCallback);
    ros::spin();
    return 0;
}