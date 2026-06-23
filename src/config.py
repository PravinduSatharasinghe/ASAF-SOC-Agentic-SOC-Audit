import os
import sys

# Standard log coloring setup
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

class Config:
    DEFAULT_SCOPE = "10.0.4.0/24 (Production Server Subnet)"
    REPORT_OUTPUT_PATH = "mock_audit_report.md"
    PLAYBOOK_OUTPUT_PATH = "remediate_vulnerabilities.yml"

def log_agent(agent_name: str, message: str, color: str = Colors.BLUE):
    print(f"{color}{Colors.BOLD}[{agent_name}]{Colors.ENDC} {message}")
