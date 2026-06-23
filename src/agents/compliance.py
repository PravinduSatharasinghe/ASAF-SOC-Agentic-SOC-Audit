import time
from typing import Dict, Any, List
from src.config import log_agent, Colors

class ComplianceAgent:
    def __init__(self):
        self.name = "Compliance-Auditor"

    def run(self, vulnerabilities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        log_agent(self.name, "Mapping identified vulnerabilities to compliance frameworks (NIST, CIS, GDPR)...", Colors.YELLOW)
        time.sleep(1.0)

        compliance_gaps = []
        for vuln in vulnerabilities:
            # Determine mapped controls
            cis_control = "CIS Control 7 (Continuous Vulnerability Management)"
            nist_control = "NIST SP 800-53 Rev. 5 (RA-5: Vulnerability Monitoring and Scanning)"
            gdpr_article = "Article 32 (Security of Processing - Technical Measures)"

            compliance_gaps.append({
                "vulnerability": vuln["cve"],
                "target_host": vuln["hostname"],
                "ip": vuln["ip"],
                "impacted_frameworks": {
                    "CIS": cis_control,
                    "NIST": nist_control,
                    "GDPR": gdpr_article
                },
                "audit_recommendation": f"Enforce automated patch validation and software inventory integrity. Fix: {vuln['fix']}"
            })

        log_agent(self.name, f"Successfully mapped {len(compliance_gaps)} findings to compliance framework guidelines.", Colors.YELLOW)
        return compliance_gaps
