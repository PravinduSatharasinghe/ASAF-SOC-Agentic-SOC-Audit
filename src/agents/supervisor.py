from typing import Dict, Any
from src.config import log_agent, Colors
from src.agents.recon import ReconAgent
from src.agents.vulnerability import VulnerabilityAgent
from src.agents.compliance import ComplianceAgent
from src.agents.remediation import RemediationAgent

class SOCSupervisor:
    def __init__(self):
        self.name = "SOC-Supervisor"

    def execute_audit(self, scope: str) -> None:
        print("="*80)
        print(f"{Colors.BLUE}{Colors.BOLD}ASAF-SOC: Agentic Security Audit Framework for SOC{Colors.ENDC}")
        print(f"Target Scope: {Colors.YELLOW}{scope}{Colors.ENDC}")
        print("="*80)

        # Initialize State
        state: Dict[str, Any] = {
            "target_scope": scope,
            "assets": [],
            "vulnerabilities": [],
            "compliance_gaps": []
        }

        log_agent(self.name, "Initializing security audit pipeline state. Spawning agents...", Colors.BLUE)
        print("-" * 60)

        # Step 1: Recon & Asset Discovery
        recon = ReconAgent()
        state["assets"] = recon.run(state)
        print("-" * 60)

        # Step 2: Vulnerability Analysis
        vuln_analyst = VulnerabilityAgent()
        state["vulnerabilities"] = vuln_analyst.run(state["assets"])
        print("-" * 60)

        # Step 3: Compliance Mapping
        compliance_auditor = ComplianceAgent()
        state["compliance_gaps"] = compliance_auditor.run(state["vulnerabilities"])
        print("-" * 60)

        # Step 4: Remediation Scripting & Reporting
        reporter = RemediationAgent()
        reporter.run(state)
        print("="*80)
        print(f"{Colors.GREEN}{Colors.BOLD}Security Audit Pipeline Complete!{Colors.ENDC}")
        print("="*80)
