import cv2

def draw_overlay(frame, status, temporal, anomaly):

    cv2.putText(frame, f"Status: {status}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    cv2.putText(frame, f"Temporal: {temporal:.1f}",
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2)

    cv2.putText(frame, f"Anomaly: {anomaly:.1f}",
                (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,0,255),
                2)

    return frame