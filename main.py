import random
import time

class AgenticDevOpsAgent:
    def __init__(self):
        # Simulates the current state of the code, affecting build/test outcomes
        self.code_state = "stable" 
        self.build_attempts = 0

    def simulate_code_change(self):
        # Simulate a developer pushing code, sometimes introducing issues
        issues = ["stable", "dependency_issue", "syntax_error", "test_failure"]
        self.code_state = random.choice(issues)
        print(f"\n--- Developer pushed code. Current code state: '{self.code_state}' ---")
        self.build_attempts = 0 # Reset attempts for new code

    def run_build(self):
        self.build_attempts += 1
        print(f"  [CI/CD] Attempting build (attempt {self.build_attempts})...")
        time.sleep(0.5) # Simulate build time

        if self.code_state == "dependency_issue":
            print("  [BUILD FAILED] Missing dependencies detected.")
            return False
        elif self.code_state == "syntax_error":
            print("  [BUILD FAILED] Syntax error detected.")
            return False
        else:
            print("  [BUILD SUCCESS] Project compiled successfully.")
            return True

    def run_tests(self):
        print("  [CI/CD] Running tests...")
        time.sleep(0.5) # Simulate test time

        if self.code_state == "test_failure":
            print("  [TEST FAILED] Critical tests failed.")
            return False
        else:
            print("  [TEST SUCCESS] All tests passed.")
            return True

    def agent_analyze_and_act(self, stage, success):
        # This is where the 'agentic' intelligence comes in.
        # Instead of just failing, it tries to understand and act proactively.
        if stage == "build":
            if not success:
                print("  [AGENT] Build failed. Analyzing...")
                if self.code_state == "dependency_issue":
                    # Agent identifies a common, fixable issue
                    print("  [AGENT] Identified missing dependency issue. Attempting auto-resolution...")
                    time.sleep(1)
                    self.code_state = "stable" # Agent 'fixed' it
                    print("  [AGENT] Dependency resolved. Retrying build...")
                    return "retry_build" # Signal to retry
                elif self.code_state == "syntax_error":
                    # Agent identifies an issue requiring human intervention, provides context
                    print("  [AGENT] Identified syntax error. Suggesting specific code review for 'main.py' line 42.")
                    print("  [AGENT] Notifying developer for immediate fix. Build paused.")
                    return "pause" # Agent decided to pause and wait for human fix
            else:
                print("  [AGENT] Build successful. Proceeding to tests.")
                return "continue"
        elif stage == "test":
            if not success:
                print("  [AGENT] Tests failed. Analyzing...")
                if self.code_state == "test_failure":
                    # Agent identifies a critical issue and suggests a proactive mitigation
                    print("  [AGENT] Detected critical regression pattern. Suggesting automated rollback to previous stable version.")
                    print("  [AGENT] Initiating rollback procedure (simulated).")
                    return "rollback" # Agent decided to rollback
            else:
                print("  [AGENT] Tests successful. Ready for deployment.")
                return "deploy"
        return "unknown"

    def run_agentic_pipeline(self):
        print("\n=== Starting Agentic DevOps Pipeline ===")

        self.simulate_code_change()

        # --- Build Stage ---
        build_successful = False
        while not build_successful and self.build_attempts < 3: # Agent might retry a few times
            build_successful = self.run_build()
            action = self.agent_analyze_and_act("build", build_successful)

            if action == "retry_build":
                continue # Loop to retry build
            elif action == "pause":
                print("  [PIPELINE PAUSED] Waiting for developer intervention due to syntax error.")
                return # Stop the pipeline for now
            elif action == "continue":
                break # Build successful, exit loop

        if not build_successful:
            print("  [PIPELINE FAILED] Build could not be resolved by agent after multiple attempts.")
            return

        # --- Test Stage ---
        test_successful = self.run_tests()
        action = self.agent_analyze_and_act("test", test_successful)

        if action == "rollback":
            print("  [PIPELINE ACTION] Rollback initiated and completed.")
            print("  [PIPELINE END] Agentic pipeline finished with rollback.")
        elif action == "deploy":
            print("  [PIPELINE ACTION] Deployment initiated (simulated).")
            print("  [PIPELINE END] Agentic pipeline finished with successful deployment.")
        else:
            print("  [PIPELINE END] Agentic pipeline finished with unknown state.")


if __name__ == "__main__":
    agent = AgenticDevOpsAgent()
    # Run the pipeline multiple times to see different agent behaviors
    for i in range(3):
        agent.run_agentic_pipeline()
        print("\n" + "="*50 + "\n")
        time.sleep(2) # Pause between runs for clarity
