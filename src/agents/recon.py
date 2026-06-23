import time
from typing import Dict, Any, List
from src.config import log_agent, Colors

class ReconAgent:
    def __init__(self):
        self.name = "Reconnaissance-Agent"

    def run(self, state: Dict[str, Any]) -> List[Dict[str, Any]]:
        log_agent(self.name, f"Initiating network asset discovery for scope: {state['target_scope']}", Colors.CYAN)
        time.sleep(1)

        # Simulate network and application discovery
        discovered_assets = [
            {
                "id": "asset-01",
                "hostname": "web-prod-srv01.local",
                "ip": "10.0.4.12",
                "os": "Ubuntu 20.04 LTS",
                "criticality": "High",
                "services": [
                    {"port": 80, "service": "http", "version": "Apache httpd 2.4.41"},
                    {"port": 443, "service": "https", "version": "Apache httpd 2.4.41 (OpenSSL 1.1.1f)"},
                    {"port": 22, "service": "ssh", "version": "OpenSSH 8.2p1"}
                ]
            },
            {
                "id": "asset-02",
                "hostname": "db-prod-srv01.local",
                "ip": "10.0.4.15",
                "os": "RedHat Enterprise Linux 8",
                "criticality": "Critical",
                "services": [
                    {"port": 5432, "service": "postgresql", "version": "PostgreSQL 12.2"},
                    {"port": 22, "service": "ssh", "version": "OpenSSH 8.0"}
                ]
            }
        ]

        log_agent(self.name, f"Completed asset mapping. Found {len(discovered_assets)} active hosts.", Colors.CYAN)
        for asset in discovered_assets:
            log_agent(self.name, f"  -> Asset: {asset['hostname']} ({asset['ip']}) | OS: {asset['os']}", Colors.CYAN)

        return discovered_assets
