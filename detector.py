import cv2
import mediapipe as mp
import numpy as np

class DriverDetector:

    def __init__(self, config):
        self.cfg = config
        self.mp_face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_hands = mp.solutions.hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def extract_features(self, frame):

        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_results = self.mp_face_mesh.process(rgb)
        hand_results = self.mp_hands.process(rgb)

        if not face_results.multi_face_landmarks:
            return {"face_present": False}

        lm = face_results.multi_face_landmarks[0].landmark

        avg_ear = self._compute_ear(lm, w, h)
        yawn_ratio = self._compute_yawn_ratio(lm, w, h)

        features = {
            "face_present": True,
            "avg_ear": avg_ear,
            "eyes_closed": avg_ear < self.cfg.EAR_THRESHOLD,
            "yawn_ratio": yawn_ratio,
            "is_yawning": yawn_ratio > self.cfg.YAWN_RATIO_THRESHOLD
        }

        return features