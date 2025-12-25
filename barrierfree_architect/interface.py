class OutputHandler:
    """
    Handles communication with the user via Accessibility Interfaces
    such as Screen Readers, Haptic Feedback, or Smart Devices.
    """
    def __init__(self):
        self.device = "Default Speaker/Vibration"

    def send_to_user(self, info):
        # Implementation for voice conversion or haptic output
        print(f"[ACCESSIBILITY OUTPUT]: {info}")
