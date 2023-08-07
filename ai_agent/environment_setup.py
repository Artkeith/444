```python
import os

class EnvironmentSetup:
    def __init__(self):
        self.communication_details = {
            "telephone_number": os.getenv("TELEPHONE_NUMBER"),
            "email_address": os.getenv("EMAIL_ADDRESS")
        }
        self.environment = os.getenv("ENVIRONMENT", "code_sandbox")
        self.blocker_page_id = os.getenv("BLOCKER_PAGE_ID")
        self.art_generator_function = os.getenv("ART_GENERATOR_FUNCTION")
        self.narrative_generator_function = os.getenv("NARRATIVE_GENERATOR_FUNCTION")
        self.email_communication_message = os.getenv("EMAIL_COMMUNICATION_MESSAGE")
        self.telephone_communication_message = os.getenv("TELEPHONE_COMMUNICATION_MESSAGE")

    def get_environment_details(self):
        return {
            "communication_details": self.communication_details,
            "environment": self.environment,
            "blocker_page_id": self.blocker_page_id,
            "art_generator_function": self.art_generator_function,
            "narrative_generator_function": self.narrative_generator_function,
            "email_communication_message": self.email_communication_message,
            "telephone_communication_message": self.telephone_communication_message
        }
```