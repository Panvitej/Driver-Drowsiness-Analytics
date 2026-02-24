Driver Drowsiness Analytics System
https://img.shields.io/badge/Python-3.7+-blue.svg
https://img.shields.io/badge/OpenCV-4.5+-green.svg
https://img.shields.io/badge/MediaPipe-0.8+-orange.svg
https://img.shields.io/badge/License-MIT-yellow.svg

A vision-based driver drowsiness detection and analytics system that monitors driver behaviour in real-time using computer vision techniques. The system tracks multiple behavioural cues including eye closure, yawning, hand-to-face proximity, and head motion to compute a drowsiness index and generate comprehensive analytics.

📋 Table of Contents
Overview

Features

System Architecture

Installation

Usage

Technical Details

Outputs

Results

Future Work

Contributing

Acknowledgments

Citation

Contact

🔍 Overview
Driver fatigue, inattention, and micro-sleep are among the leading causes of road accidents worldwide. This system provides a non-intrusive, real-time solution for monitoring driver drowsiness using only a standard camera. By analysing facial landmarks and hand movements, it detects early signs of fatigue and alerts the driver before a potential incident.

The system produces two main outputs:

Real-time annotated video with on-screen status indicators

Post-processing analytics dashboard with temporal behaviour analysis

✨ Features
Real-time Monitoring
Eye Closure Detection - Using Eye Aspect Ratio (EAR) to detect closed eyes and micro-sleeps

Yawning Detection - Measuring mouth opening normalized by face width

Hand-to-Face Proximity - Detecting face-touching behaviours (eye rubbing, face touching)

Head Motion Analysis - Tracking vertical head movements to detect nodding

Advanced Analytics
Temporal Behaviour Windows - Sliding window analysis of driver behaviour

Asymmetric Exponential Smoothing - Scores rise quickly but decay slowly for stable predictions

Dual Scoring System - Temporal drowsiness score + facial anomaly score

Behavioural Classification - Alert, Behavioural Fatigue, Critical Anomalous Behaviour states

Output & Visualization
Annotated Video Output - Real-time overlays with scores and status

Comprehensive Dashboard - Time-series plots, status distributions, behaviour history

CSV Export - Frame-level data for further analysis

🏗 System Architecture
text
Video Input → MediaPipe Processing → Feature Extraction → Temporal Analysis → Visualization
     ↓                ↓                      ↓                    ↓                 ↓
  OpenCV        Face Mesh + Hands       EAR, Yawn Ratio,       Sliding Window    Annotated Video
               Face Detection          Hand Distance,         + Smoothing      + Analytics Dashboard
                                        Head Motion
Key Components:
Feature Extraction - MediaPipe landmarks for facial and hand features

Temporal Modelling - Behaviour histories over sliding windows

Score Computation - Weighted combination of behavioural metrics

Asymmetric Smoothing - Stabilized score curves

Visualization - Real-time overlays and post-analysis dashboard

💻 Installation
Prerequisites
Python 3.7+

Webcam or video input source

Setup
bash
# Clone the repository
git clone https://github.com/yourusername/driver-drowsiness-analytics.git
cd driver-drowsiness-analytics

# Install required packages
pip install opencv-python mediapipe numpy pandas matplotlib

# Verify installation
python -c "import cv2; import mediapipe; print('Setup successful!')"
Dependencies
OpenCV - Video processing and visualization

MediaPipe - Facial and hand landmark detection

NumPy - Mathematical operations

Pandas - Data management and export

Matplotlib - Dashboard visualization

🚀 Usage
Basic Usage
python
# Run on video file
python drowsiness_detector.py --input path/to/video.mp4 --output results/

# Run with webcam
python drowsiness_detector.py --camera 0 --output results/

# Custom parameters
python drowsiness_detector.py --input video.mp4 --window 10 --threshold 0.23
Command Line Arguments
Argument	Description	Default
--input	Input video file path	None
--camera	Camera device ID	None
--output	Output directory	./output
--window	Temporal window (seconds)	10
--ear_thresh	EAR threshold for eye closure	0.23
--yawn_thresh	Yawn ratio threshold	0.22
--hand_thresh	Hand proximity threshold	0.9
🔧 Technical Details
Feature Extraction
Eye Aspect Ratio (EAR)
text
EAR = (||p2-p6|| + ||p3-p5||) / (2 * ||p1-p4||)
Higher values = eyes open

Lower values (< threshold) = eyes closed

Yawn-Chin Ratio
text
R_yawn = d_chin-lip / d_face
Measures mouth opening normalized by face width

Hand-to-Face Proximity
text
d_hand-face = √[(hx - fx)² + (hy - fy)²]
Normalized by face size for scale invariance

Scoring System
Temporal Drowsiness Score:

text
S_temp = 60r_eye + 25r_yawn + 10r_hand + 20r_mod
Combined Score:

text
S_combined = 0.7S_temp + 0.3S_anom
Status Classification
Score Range	Status	Action
< 30	Alert	Normal driving
30 - 60	Behavioural Fatigue	Consider break
≥ 60	Critical Anomalous	Immediate rest recommended
📊 Outputs
1. Annotated Video
Each frame displays:

Current EAR and yawn ratio

Binary flags (eyes closed, yawning, hand near face)

Windowed percentages

Current status with colour coding

Smoothed score bars

2. Analytics Dashboard
Time-series plots of drowsiness and anomaly scores

Event ratio trends over time

Status distribution pie chart

Behaviour history timeline

3. CSV Export
Frame-level data including:

Timestamps

Raw and smoothed scores

Event flags

Status labels

📈 Results
The system effectively detects:

Micro-sleep episodes through sustained low EAR values

Fatigue indicators through combined behavioural patterns

Anomalous behaviour like frequent face touching

Head nodding patterns

Sample analytics output includes:

Percentage of time in each alert state

Most frequent drowsiness indicators

Temporal patterns of behaviour changes

🔮 Future Work
Integrate head pose estimation (pitch, yaw, roll)

Implement deep learning models for improved accuracy

Evaluate on larger datasets with ground truth labels

Deploy on embedded hardware (Raspberry Pi, Jetson Nano)

Add multi-camera support for different viewing angles

Develop mobile application version

Real-time alert system with audio warnings

