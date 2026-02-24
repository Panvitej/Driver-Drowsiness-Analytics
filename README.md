# Driver Drowsiness Analytics  
*A vision-based behavioural analytics system for detecting driver fatigue and anomalous behaviour from video.*

---

## Project Overview

This project presents a complete **driver drowsiness analytics pipeline** that analyses a driver’s face and hand behaviour from video streams and produces:

1. a **real-time annotated output video**, and  
2. a **post-run analytics dashboard** summarising driver behaviour and risk trends.

The system is developed as an academic project at **:contentReference[oaicite:0]{index=0}** and focuses on interpretable, landmark-based computer vision rather than black-box deep learning.

---

## Key Idea

Instead of classifying a driver as simply *alert* or *drowsy*, the system continuously measures multiple behavioural cues, aggregates them over time, and produces:

- a **temporal drowsiness score**, and  
- a **facial anomaly score**,  

which are further stabilised using **asymmetric exponential smoothing** to avoid sudden and unstable predictions.

---

## Features

The system analyses the following behavioural signals:

- **Eye closure** using Eye Aspect Ratio (EAR)  
- **Yawning** using a normalised mouth–chin distance  
- **Hand-to-face proximity** to detect face touching or occlusion  
- **Head vertical motion** to capture nodding behaviour  

These are combined over a sliding time window to generate meaningful risk trends instead of frame-by-frame decisions.

---

## System Outputs

### 1. Annotated Video Output
Each frame contains:
- EAR and yawn ratio values  
- flags for eyes closed, yawning, and hand near face  
- windowed behaviour percentages  
- smoothed temporal and anomaly scores  
- driver status and advisory message

### 2. Analytics Dashboard
A post-processing dashboard is generated from stored frame-level metrics and includes:

- time-series plots of temporal drowsiness score  
- time-series plots of anomaly score  
- behaviour frequency curves (eye closure, yawning, hand near face)  
- distribution of driver states over the entire video

---

## Architecture

The processing pipeline consists of three major stages:

1. **Landmark extraction**
2. **Temporal modelling and scoring**
3. **Visualisation and analytics**

Each video frame is processed to extract facial and hand landmarks, compute behavioural features, update temporal histories, calculate risk scores, and finally generate visual overlays and analytics data.

---

## Feature Extraction

### Eye Aspect Ratio (EAR)
EAR is computed from six eye landmarks.  
A lower EAR indicates eye closure.  
Both eyes are averaged and thresholded to detect closed-eye frames.

### Yawn–Chin Ratio
The vertical distance between the upper lip and chin is normalised by face width.  
Large values indicate yawning behaviour.

### Hand-to-Face Proximity
The distance between fingertip landmarks and the face centre is normalised by face size.  
A small ratio indicates the hand is near the face.

### Head Motion
Vertical movement of the nose landmark is tracked inside a temporal window to detect nodding.

---

## Temporal Modelling

Binary histories are maintained for:

- eyes closed  
- yawning  
- hand near face  
- combined eye-closure + yawning events  

From a sliding window of frames, behaviour ratios are computed and used to generate a **raw temporal drowsiness score**:


Stemp,raw = 60·reye + 25·ryawn + 10·rhand + 20·rmoderate


The score is clipped to the range [0, 100].

---

## Anomaly Modelling

An independent anomaly score is generated using:

- standard deviation of EAR  
- frequent yawning in the window  
- head nodding amplitude  
- hand-near-face frequency  

Textual behavioural notes are also generated (for example, *frequent yawning* or *irregular eye closure pattern*).

---

## Asymmetric Exponential Smoothing

To avoid unstable behaviour, both the temporal score and anomaly score are smoothed using an asymmetric rule:

- scores **increase quickly** when risk rises  
- scores **decrease slowly** when risk reduces  

This creates a stable and interpretable risk curve suitable for analytics and decision support.

---

## Driver State and Advice Logic

A combined score is computed as:


Scombined = 0.7 · Stemp,smooth + 0.3 · Sanom,smooth


Driver states are defined as:

- **Alert**: Scombined < 30  
- **Behavioural Fatigue**: 30 ≤ Scombined < 60  
- **Critical Anomalous Behaviour**: Scombined ≥ 60  

Special states:

- **Driver Not Visible** – when the face is not detected  
- **Face Occluded** – when the hand is very close to the face while risk is otherwise low  

Each state is associated with short advisory messages such as rest or break suggestions.

---

## Implementation

The system is implemented in Python using:

- **:contentReference[oaicite:1]{index=1}** for video processing, overlays and I/O  
- **MediaPipe by :contentReference[oaicite:2]{index=2}** for face mesh, face detection and hand landmark estimation  
- NumPy for numerical computations  
- Pandas and Matplotlib for analytics and dashboard generation  

The main processing loop:

1. reads a video frame  
2. extracts facial and hand landmarks  
3. computes behavioural features  
4. updates sliding window histories  
5. computes raw and smoothed scores  
6. determines driver status and advice  
7. draws overlays and stores analytics data  

At the end of processing, all per-frame metrics are exported to a CSV file and used to generate the dashboard plots.

---

## Example Use-Cases

- driver behaviour analysis for research studies  
- offline evaluation of fatigue detection algorithms  
- educational projects in computer vision and human behaviour analytics  
- early-stage driver assistance systems

---

## Results

The system provides:

- interpretable behavioural analytics instead of only binary labels  
- stable temporal trends through asymmetric smoothing  
- detailed post-run dashboards that show *when*, *how long*, and *why* the driver exhibited fatigue-related behaviour

---

## Limitations

- performance depends on face visibility and lighting conditions  
- landmark-based thresholds may require tuning for different users  
- no ground-truth physiological validation is used

---

## Future Work

- explicit head pose estimation (pitch, yaw, roll)  
- hybrid models combining landmarks with deep learning  
- evaluation on larger annotated datasets  
- deployment on embedded in-vehicle hardware

---
