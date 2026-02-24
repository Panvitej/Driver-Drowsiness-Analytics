import cv2
from config import Config
from detector import DriverDetector
from scoring import ScoreEngine
from advisor import AdviceEngine
from visualization import draw_overlay


def main(video_path):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Cannot open video")

    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0

    detector = DriverDetector(Config)
    scorer = ScoreEngine(Config, fps)
    advisor = AdviceEngine()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        features = detector.extract_features(frame)
        temporal, anomaly = scorer.update(features)
        status = advisor.evaluate(temporal, anomaly, features)

        frame = draw_overlay(frame, status, temporal, anomaly)

        cv2.imshow("Driver Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main("input.mp4")