## Problem Definition
In this assignment, we are trying to:

- Understand computer vision.
- Design and implement algorithms that recognize at least 3 hand shapes or gestures.
- Create a graphical display that responds to the recognition of the hand shapes or gestures.
- We believe the program and the results are useful because:

## Method and Implementation
- To achieve our goals, we use several computer vision techniques.
- To detect static hand shapes, the major technique we use is template matching. We first get clear pictures of certain hand shapes (highFive and fist) as our templates, and use matchTemplate() method in opencv to see if the hand shape in the frame matches any of our templates. If a matching is detected, a corresponding emoji will show in our window.
- To detect a dynamic hand gesture, we use techniques including skin-color detection, frame-to-frame differencing, motion energy templates, and size of "movement blobs".

Functionss we use in our program:
- mySkinDetect: This function detects whether a pixel belongs to the skin based on RGB values.
- myTemplateMatching: This function detects if the gesture in the frame is matched with any template; if yes then draw an emoji corresponding to that gesture.
- myFrameDifferencing: This function does frame differencing between the current frame and the previous frame.
- myMotionEnergy: This function accumulates the frame differences for a certain number of pairs of frames.

## Experiments
Our experiments include:
- No hand in the camera
- Hand gestures that do not match any template
- Static hand gesture that matches our template: fighting
- Static hand gesture that matches our template: high five
- Dynamic hand gesture: waving
Evaluation metrics:
- Detection rates
- Overall accuracy

## Results


Experiment 1: No hand in the camera




Experiment 2: Hand gestures that do not match any template





Experiment 3: Static hand gesture that matches our template: fighting





Experiment 4: Static hand gesture that matches our template: high five





Experiment 5: Dynamic hand gesture: waving





Confusion Matrix of "high five" detection

Actual
Predicted		True	False
True	13	6
False	2	9
Detection rate: 86.67%

Overall accuracy: 73.33%

Confusion Matrix of "fighting" detection

Actual
Predicted		True	False
True	10	1
False	5	14
Detection rate: 66.67%

Overall accuracy: 80.00%

Confusion Matrix of "waving" detection

Actual
Predicted		True	False
True	15	5
False	0	10
Detection rate: 100%

Overall accuracy: 83.33%

## Discussion and conclusion
The strengths and weaknesses of our method:
- Strength: Our template matching method can be used for detecting other gestures by adding a picture in the folder and adjusting few lines of code. And our detection rate of waving hand is very high because we combine skin color detection with frame-to-frame differencing method, which makes the program sensitive to small moves of hand.
- Weakness: There are limitations of template matching method that the hand gesture in the frame has to be very similar to the template to be detected, and some other gestures that are similar to the template which are not supposed to be detected sometimes are wrongly detected by our program. Also, although waving is sensitively detected for most of times, some other moving parts of body (e.g. a face) will also be wrongly detected sometimes.
Potential future works:
- Improve template matching method to let the program be able to detect desired hand gestures even if they are not that similar to the template, and ignore other objects even if they are somehow similar to our template.
- Try other methods, for example, background detection, to better recognize a hand in a frame.
- Apply the improvement to the recognization of a waving hand so that a moving head or similar body parts will not be detected as a moving hand anymore.


## Credits and Bibliography
Boston University Department of Computer Science, CS440, Professor Betke
This project is contributed by Jiatong Hao and Xianhui Li

