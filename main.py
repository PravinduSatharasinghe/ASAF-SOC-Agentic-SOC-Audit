#!/usr/bin/env python3
import sys
from src.config import Config
from src.agents.supervisor import SOCSupervisor

def main():
    # Allow custom target subnet scope input from CLI argument
    scope = sys.argv[1] if len(sys.argv) > 1 else Config.DEFAULT_SCOPE
    
    # Initialize and execute pipeline
    supervisor = SOCSupervisor()
    supervisor.execute_audit(scope)

if __name__ == "__main__":
    main()
