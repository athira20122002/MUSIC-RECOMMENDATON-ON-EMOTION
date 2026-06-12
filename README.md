# 🎵 Music Recommendation Based on Emotion Recognition

An intelligent music recommendation system that utilizes real-time facial emotion recognition to detect a user's emotional state and recommend music accordingly. By combining Computer Vision and Deep Learning techniques, the application delivers a personalized and interactive music listening experience.

## 📖 Overview

This project captures live video from a webcam, detects facial expressions, and identifies the user's dominant emotion using DeepFace and OpenCV. Based on the detected emotion, the system recommends music that aligns with the user's mood, enhancing personalization and user engagement.

## ✨ Features

* 🎥 Real-Time Face Detection using OpenCV and Haar Cascade Classifier
* 🧠 Emotion Recognition powered by DeepFace pre-trained deep learning models
* 🎵 Emotion-Based Music Recommendation
* 🖥️ Live Webcam Analysis and Emotion Display
* 📊 Emotion Confidence Score Evaluation
* 🔄 Continuous Real-Time Monitoring
* ⚡ Interactive and User-Friendly Experience
* ⌨️ Simple Keyboard Controls

## 🛠️ Technologies Used

* 🐍 Python
* 👁️ OpenCV
* 🤖 DeepFace
* 📐 Haar Cascade Classifier
* 🎵 Music Recommendation Logic
* 📊 NumPy
* 🖥️ Computer Vision
* 🧠 Deep Learning

## 🎭 Supported Emotion Categories

| Emotion     | Recommendation Type              |
| ----------- | -------------------------------- |
| 😊 Happy    | Energetic and cheerful music     |
| 😢 Sad      | Calming and uplifting songs      |
| 😠 Angry    | Relaxing and stress-relief music |
| 😲 Surprise | Exciting and dynamic tracks      |
| 😨 Fear     | Soothing and comforting music    |
| 🤢 Disgust  | Mood-enhancing recommendations   |
| 😐 Neutral  | Popular and balanced playlists   |

## ⚙️ How It Works

### 📹 Video Acquisition

The webcam continuously captures live video frames.

### 🔍 Face Detection

OpenCV's Haar Cascade Classifier identifies and locates faces within each frame.

### 🧠 Emotion Analysis

Detected facial regions are processed using DeepFace, which:

* Extracts facial features
* Evaluates emotion probabilities
* Identifies the dominant emotion
* Generates confidence scores for each emotion category

### 🎵 Music Recommendation

The detected emotion is mapped to a predefined music category, and relevant songs are recommended to match the user's mood.

### 🖥️ Real-Time Visualization

The application displays:

* Face bounding boxes
* Detected emotion labels
* Emotion confidence levels
* Recommended music category

## 📊 System Workflow

1. Capture video from webcam
2. Detect face regions
3. Extract facial features
4. Perform emotion classification
5. Identify dominant emotion
6. Generate music recommendations
7. Display results in real time

## 🎯 Applications

* Personalized Music Recommendation Systems
* Smart Entertainment Platforms
* Emotion-Aware Applications
* Human-Computer Interaction Research
* Mental Wellness and Mood Tracking Solutions
* AI-Based Recommendation Systems
* Educational and Research Demonstrations

## 💡 Learning Outcomes

* Computer Vision Fundamentals
* Facial Emotion Recognition
* Deep Learning Model Integration
* Real-Time Video Processing
* Human-Centered AI Applications
* Recommendation System Design
* Python-Based AI Development

## 👩‍💻 Author

**Athira Mohan**

GitHub: https://github.com/athira20122002

## 📄 License

This project is licensed under the MIT License.

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

