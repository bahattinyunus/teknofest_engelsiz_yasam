import logging
from barrierfree_architect.perception import PerceptionLayer
from barrierfree_architect.core import BrainProcessor
from barrierfree_architect.interface import OutputHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Architect-Main")

def run_system():
    logger.info("Starting BarrierFree-Architect System...")
    
    # 1. Initialize Layers
    perception = PerceptionLayer()
    brain = BrainProcessor()
    output = OutputHandler()
    
    # 2. Main Loop (Simulated)
    logger.info("System operational. Listening for sensory input...")
    try:
        raw_data = perception.get_sensory_input()
        processed_data = brain.analyze(raw_data)
        output.send_to_user(processed_data)
        logger.info("Cycle completed successfully.")
    except Exception as e:
        logger.error(f"System Failure: {e}")

if __name__ == "__main__":
    run_system()
