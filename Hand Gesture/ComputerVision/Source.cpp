/*	CS440_Programming_Assignment_2 - Computer_Vision
*	Author: Xianhui Li, Jiatong Hao
*	April 2, 2018
*
*	--------------
*	This gesture recognition program can recognize:
*		a) an open hand/high five gesture
*		b) a fist
*		c) hand waving
*       (Please make sure there is a black background :)
*	--------------
*   How the program respond to recognized gestures:
*       a) if you show an open hand, an emoji will be printed on the screen to do a high five with you
*       b) if you show a fist, an emoji will be printed on the screen to fight back
*       c) if you are waving, an emoji will wave to you as well, and it's curious on whether you are saying hello or goodbye to it
*   --------------
*   Interesting aspects of the graphical display:
*       a) we use emojis instead of mere words :)
*       b) the emojis are not only description of your gesture; it "interacts" with you
*   --------------
*/


//opencv libraries
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
//C++ standard libraries
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;

//function declarations

/**
Function that returns the maximum of 3 integers
@param a first integer
@param b second integer
@param c third integer
*/
int myMax(int a, int b, int c);

/**
Function that returns the minimum of 3 integers
@param a first integer
@param b second integer
@param c third integer
*/
int myMin(int a, int b, int c);

/**
Function that detects whether a pixel belongs to the skin based on RGB values
@param src The source color image
@param dst The destination grayscale image where skin pixels are colored white and the rest are colored black
*/
void mySkinDetect(Mat& src, Mat& dst);

/**
Function that does frame differencing between the current frame and the previous frame
@param src The current color image
@param prev The previous color image
@param dst The destination grayscale image where pixels are colored white if the corresponding pixel intensities in the current
and previous image are not the same
*/
void myFrameDifferencing(Mat& prev, Mat& curr, Mat& skinPrev, Mat& skinCurr, Mat& dst);

/**
Function that accumulates the frame differences for a certain number of pairs of frames
@param mh Vector of frame difference images
@param dst The destination grayscale image to store the accumulation of the frame difference images
@param img_display The image to display the result
@param wavingHand The emoji to display when a waving is recognized
*/
void myMotionEnergy(vector<Mat> mh, Mat& dst, Mat& img_display, Mat& wavingHand);

/**
Function that detect if a high five gesture template is in the frame; if yes then draw a emoji
@param src The current color image
@param dst The destination grayscale image
@param imgTemplate The template we want to find in the frame
@param img_display The image to display the result
@param result The emoji to display when an open hand is recognized
*/
void myTemplateMatching(Mat& src, Mat& dst, Mat& imgTemplate, Mat& img_display, Mat& result);


int main()
{

	//----------------
	//a) Reading a stream of images from a webcamera, and displaying the video
	//----------------

	VideoCapture cap(0);

	// if not successful, exit program
	if (!cap.isOpened())
	{
		cout << "Cannot open the video cam" << endl;
		return -1;
	}

	//create a window called "MyVideoFrame0"
	namedWindow("MyVideo0", WINDOW_AUTOSIZE);
	Mat frame0;

	// read a new frame from video
	bool bSuccess0 = cap.read(frame0);
	if (!bSuccess0)
	{
		cout << "Cannot read a frame from video stream" << endl;
	}

	//show the frame in "MyVideo" window
	imshow("MyVideo0", frame0);


	//create windows for high five gesture recognition, waving recognization
	//windows for frame differencing, and motion energy
	namedWindow("HighFiveOrHaveAFight", WINDOW_AUTOSIZE);
	namedWindow("Waving", WINDOW_AUTOSIZE);
	namedWindow("FrameDifference", WINDOW_AUTOSIZE);

	//load template for high five gesture recognition
	Mat openTemplate = imread("openHand.jpg", IMREAD_COLOR);
	Mat fistTemplate = imread("fist.jpg", IMREAD_COLOR);

	//load the emoji displayed when a gesture is found
	Mat highFiveEmoji = imread("highFive.jpg", IMREAD_COLOR);
	Mat fistEmoji = imread("fist_emoji.jpg", IMREAD_COLOR);
	Mat wavingHandEmoji = imread("waving-hand.png", IMREAD_COLOR);

	//set up for motion history
	vector<Mat> myMotionHistory;
	Mat fMH1, fMH2, fMH3;
	fMH1 = Mat::zeros(frame0.rows, frame0.cols, CV_8UC1);
	fMH2 = fMH1.clone();
	fMH3 = fMH1.clone();
	myMotionHistory.push_back(fMH1);
	myMotionHistory.push_back(fMH2);
	myMotionHistory.push_back(fMH3);

	while (1)
	{
		// read a new frame from video
		Mat frame;
		bool bSuccess = cap.read(frame);
		//if not successful, break loop
		if (!bSuccess)
		{
			cout << "Cannot read a frame from video stream" << endl;
			break;
		}

		//----------------
		// a) Read a stream of images from a web camera, and displaying the video
		//----------------
		imshow("MyVideo0", frame);

		//----------------
		//	b) High five or fist recognition
		//----------------

		// destination frame and result display frame
		Mat frameDest; Mat img_display;
		img_display = frame.clone();

		// call myTemplateMatching function
		myTemplateMatching(frame, frameDest, openTemplate, img_display, highFiveEmoji);
		myTemplateMatching(frame, frameDest, fistTemplate, img_display, fistEmoji);
		imshow("HighFiveOrHaveAFight", img_display);


		//----------------
		//	c) Frame-to-frame differencing
		//----------------

		// destination frame
		Mat frameDest0; Mat frameDest1;
		frameDest0 = Mat::zeros(frame.rows, frame.cols, CV_8UC1); //Returns a zero array of same size as src mat, and of type CV_8UC1
		frameDest1 = Mat::zeros(frame.rows, frame.cols, CV_8UC1); //Returns a zero array of same size as src mat, and of type CV_8UC1

		
		//imshow("Skin", frameDest);

		//call myFrameDifferencing function
		myFrameDifferencing(frame0, frame, frameDest0, frameDest1, frameDest);
		imshow("FrameDifference", frameDest);

		//----------------
		//  d) Recognize hand waving by motion history
		//----------------

		myMotionHistory.erase(myMotionHistory.begin());
		myMotionHistory.push_back(frameDest);
		Mat myMH = Mat::zeros(frame0.rows, frame0.cols, CV_8UC1);

		Mat img_display1 = frame.clone();

		//call myMotionEnergy function
		myMotionEnergy(myMotionHistory, myMH, img_display1, wavingHandEmoji);
		//imshow("MotionEnergy", myMH); 
		imshow("Waving", img_display1);

		frame0 = frame;

		//wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
		if (waitKey(30) == 27)
		{
			cout << "esc key is pressed by user" << endl;
			break;
		}

	}
	cap.release();
	return 0;
}

//Function that returns the maximum of 3 integers
int myMax(int a, int b, int c) {
	int m = a;
	(void)((m < b) && (m = b));
	(void)((m < c) && (m = c));
	return m;
}

//Function that returns the minimum of 3 integers
int myMin(int a, int b, int c) {
	int m = a;
	(void)((m > b) && (m = b));
	(void)((m > c) && (m = c));
	return m;
}

//Function that detects whether a pixel belongs to the skin based on RGB values
void mySkinDetect(Mat& src, Mat& dst) {
	//Surveys of skin color modeling and detection techniques:
	//Vezhnevets, Vladimir, Vassili Sazonov, and Alla Andreeva. "A survey on pixel-based skin color detection techniques." Proc. Graphicon. Vol. 3. 2003.
	//Kakumanu, Praveen, Sokratis Makrogiannis, and Nikolaos Bourbakis. "A survey of skin-color modeling and detection methods." Pattern recognition 40.3 (2007): 1106-1122.
	for (int i = 0; i < src.rows; i++){
		for (int j = 0; j < src.cols; j++){
			//For each pixel, compute the average intensity of the 3 color channels
			Vec3b intensity = src.at<Vec3b>(i, j); //Vec3b is a vector of 3 uchar (unsigned character)
			int B = intensity[0]; int G = intensity[1]; int R = intensity[2];
			if ((R > 95 && G > 40 && B > 20) && (myMax(R, G, B) - myMin(R, G, B) > 15) && (abs(R - G) > 15) && (R > G) && (R > B)){
				dst.at<uchar>(i, j) = 255;
			}
		}
	}
}

// Function that detect if a high five gesture template is in the frame; if yes then draw a emoji
void myTemplateMatching(Mat& src, Mat& dst, Mat& imgTemplate, Mat& img_display, Mat& result){

	// set the size of the matching grid
	int dst_cols = src.cols - imgTemplate.cols + 1;
	int dst_rows = src.rows - imgTemplate.rows + 1;
	dst.create(dst_rows, dst_cols, CV_32FC1);

	//template matching function
	matchTemplate(src, imgTemplate, dst, CV_TM_CCOEFF_NORMED);

	//since we are using normalized correlation coeffcient, we want the position with the highest r
	double minVal; double maxVal; Point minLoc; Point maxLoc;
	Point matchLoc;
	minMaxLoc(dst, &minVal, &maxVal, &minLoc, &maxLoc, Mat());
	matchLoc = maxLoc;

	// set a threshold
	double threshold = 0.6;
	if (maxVal > threshold){
		result.copyTo(img_display.rowRange(50, 170).colRange(50, 170));
	}
}

//Function that does frame differencing between the current frame and the previous frame
void myFrameDifferencing(Mat& prev, Mat& curr, Mat& skinPrev, Mat& skinCurr, Mat& dst) {
	//For more information on operation with arrays: http://docs.opencv.org/modules/core/doc/operations_on_arrays.html
	mySkinDetect(prev, skinPrev);
	mySkinDetect(curr, skinCurr);
	absdiff(skinPrev, skinCurr, dst);
	Mat cp = dst.clone();
	//cvtColor(dst, cp, CV_BGR2GRAY);
	dst = cp > 50;
}

//Function that accumulates the frame differences for a certain number of pairs of frames
void myMotionEnergy(vector<Mat> mh, Mat& dst, Mat& img_display, Mat& wavingHand) {
	Mat mh0 = mh[0];
	Mat mh1 = mh[1];
	Mat mh2 = mh[2];
	
	//counter for the number of pixels that have changing
	int count = 0;

	for (int i = 0; i < dst.rows; i++){
		for (int j = 0; j < dst.cols; j++){
			if (mh0.at<uchar>(i, j) == 255 || mh1.at<uchar>(i, j) == 255 || mh2.at<uchar>(i, j) == 255){
				dst.at<uchar>(i, j) = 255;
				count += 1;
			}
		}
	}
	
	if (count >= dst.rows * dst.cols * 0.1){
		wavingHand.copyTo(img_display.rowRange(70, 198).colRange(70, 198));
		putText(img_display, "Are you saying hello or goodbye?", Point2i(70, 50), FONT_HERSHEY_SIMPLEX, 0.5, CV_RGB(255, 255, 255), 1, 0);
	}

}
