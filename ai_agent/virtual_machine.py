```python
import os
import subprocess
from ai_agent import environment_setup

class VirtualMachine:
    def __init__(self, vm_name):
        self.vm_name = vm_name
        self.vm_path = os.path.join(environment_setup.VM_DIRECTORY, vm_name)

    def start_vm(self):
        subprocess.run(["VBoxManage", "startvm", self.vm_name])

    def stop_vm(self):
        subprocess.run(["VBoxManage", "controlvm", self.vm_name, "poweroff"])

    def reset_vm(self):
        subprocess.run(["VBoxManage", "controlvm", self.vm_name, "reset"])

    def snapshot_vm(self, snapshot_name):
        subprocess.run(["VBoxManage", "snapshot", self.vm_name, "take", snapshot_name])

    def restore_vm(self, snapshot_name):
        subprocess.run(["VBoxManage", "snapshot", self.vm_name, "restore", snapshot_name])

    def run_script_in_vm(self, script_path):
        script_name = os.path.basename(script_path)
        subprocess.run(["VBoxManage", "guestcontrol", self.vm_name, "run", script_name, "--username", environment_setup.VM_USERNAME, "--password", environment_setup.VM_PASSWORD])

if __name__ == "__main__":
    vm = VirtualMachine(environment_setup.VM_NAME)
    vm.start_vm()
```