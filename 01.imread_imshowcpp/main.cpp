#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main(){
    cv::Mat img = cv::imread("lena.jpeg", cv::IMREAD_GRAYSCALE);
    cv::imshow("Window", img);

    cv::waitKey(0);

    return 0;

}

