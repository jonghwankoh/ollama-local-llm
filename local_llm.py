import argparse
import os
import subprocess
import yaml
import sys

def load_profile(profile_path):
    with open(profile_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def run_ollama(config):
    model_name = config.get('model_name')
    modelfile = config.get('modelfile')
    
    print(f"[*] Initializing Ollama model: {model_name}")
    try:
        # Create model from Modelfile
        subprocess.run(["ollama", "create", model_name, "-f", modelfile], check=True)
        print(f"[*] Starting model: {model_name}")
        # Run model
        subprocess.run(["ollama", "run", model_name])
    except subprocess.CalledProcessError as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("[!] Error: 'ollama' command not found. Please install Ollama.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Local LLM Extensible Launcher")
    parser.add_argument("action", choices=["run", "list"], help="Action to perform")
    parser.add_argument("--profile", "-p", help="Profile name (filename in profiles/ without .yaml)")
    
    args = parser.parse_args()
    
    if args.action == "list":
        profiles = os.listdir("profiles")
        print("Available Profiles:")
        for p in profiles:
            if p.endswith(".yaml"):
                print(f"  - {p[:-5]}")
        return

    if args.action == "run":
        if not args.profile:
            print("[!] Please specify a profile with --profile or -p")
            return
        
        profile_path = os.path.join("profiles", f"{args.profile}.yaml")
        if not os.path.exists(profile_path):
            print(f"[!] Profile not found: {profile_path}")
            return
        
        config = load_profile(profile_path)
        engine = config.get('engine', 'ollama')
        
        if engine == "ollama":
            run_ollama(config)
        else:
            print(f"[!] Engine '{engine}' is not yet implemented.")

if __name__ == "__main__":
    main()
