import sys
from pathlib import Path

from environment import Environment
from simulation import SimulationEngine, SimulationInitializer


def main():
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "config.json"
    
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"Error: Config file not found: {config_path}")
        print(f"Usage: python -m mas_market_laboratory.mas_market_labratory [config_path]")
        sys.exit(1)
    
    print("=" * 60)
    print("MAS Market Laboratory - Multi-Agent Simulation")
    print("=" * 60)
    print(f"Config: {config_file.absolute()}")
    print()
    
    print("Initializing configurations...")
    SimulationInitializer.INITIALIZE_CONFIGS(str(config_file.absolute()))
    print(" ✔️Configurations loaded")
    print()
    
    print("Creating environment...")
    env = Environment()
    print("✔️ Environment created")
    print()    

    print("Creating simulation engine...")
    engine = SimulationEngine(env)
    print("✔️ Simulation engine ready")
    print()
    
    print("=" * 60)
    print("Starting Simulation")
    print("=" * 60)
    engine.run()
    
    print()
    print("=" * 60)
    print("Simulation Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
