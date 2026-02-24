from collections import deque
import numpy as np

class ScoreEngine:

    def __init__(self, config, fps):
        self.cfg = config
        self.window = int(config.WINDOW_SECONDS * fps)

        self.eye_hist = deque(maxlen=self.window)
        self.yawn_hist = deque(maxlen=self.window)
        self.ear_hist = deque(maxlen=self.window)

        self.prev_temporal = None
        self.prev_anomaly = None

    def update(self, features):

        if not features["face_present"]:
            return 0.0, 0.0

        self.eye_hist.append(int(features["eyes_closed"]))
        self.yawn_hist.append(int(features["is_yawning"]))
        self.ear_hist.append(features["avg_ear"])

        temporal_raw = self._compute_temporal()
        anomaly_raw = self._compute_anomaly()

        temporal = self._smooth(
            self.prev_temporal,
            temporal_raw,
            self.cfg.TEMP_UP_ALPHA,
            self.cfg.TEMP_DOWN_ALPHA
        )

        anomaly = self._smooth(
            self.prev_anomaly,
            anomaly_raw,
            self.cfg.ANOM_UP_ALPHA,
            self.cfg.ANOM_DOWN_ALPHA
        )

        self.prev_temporal = temporal
        self.prev_anomaly = anomaly

        return temporal, anomaly