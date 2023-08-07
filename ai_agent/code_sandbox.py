import os
from environment_setup import setup_environment

class CodeSandbox:
    def __init__(self, communication_details):
        self.communication_details = communication_details
        self.environment = setup_environment("code_sandbox")

    def run_blocker_page(self):
        from blocker_page import BlockerPage
        self.blocker_page = BlockerPage(self.environment)
        self.blocker_page.run()

    def generate_art(self):
        from art_generator import ArtGenerator
        self.art_generator = ArtGenerator(self.environment)
        self.art_generator.generate()

    def generate_narrative(self):
        from narrative_generator import NarrativeGenerator
        self.narrative_generator = NarrativeGenerator(self.environment)
        self.narrative_generator.generate()

    def communicate(self):
        from email_communication import EmailCommunication
        from telephone_communication import TelephoneCommunication
        self.email_communication = EmailCommunication(self.communication_details)
        self.telephone_communication = TelephoneCommunication(self.communication_details)
        self.email_communication.send()
        self.telephone_communication.call()

    def operate_autonomously(self):
        from autonomous_operation import AutonomousOperation
        self.autonomous_operation = AutonomousOperation(self.environment)
        self.autonomous_operation.operate(self)

if __name__ == "__main__":
    communication_details = {"email": "ai_agent@example.com", "telephone": "+1234567890"}
    code_sandbox = CodeSandbox(communication_details)
    code_sandbox.run_blocker_page()
    code_sandbox.generate_art()
    code_sandbox.generate_narrative()
    code_sandbox.communicate()
    code_sandbox.operate_autonomously()