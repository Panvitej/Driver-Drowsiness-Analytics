class AdviceEngine:

    def evaluate(self, temporal_score, anomaly_score, features):

        combined = 0.7 * temporal_score + 0.3 * anomaly_score

        if not features["face_present"]:
            return "Driver Not Visible"

        if combined < 30:
            return "Alert"

        if combined < 60:
            return "Behavioural Fatigue"

        return "Critical Behaviour"