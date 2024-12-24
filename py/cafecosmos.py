from ape import Contract, networks, accounts, chain
import os
import json
from pathlib import Path
import yaml


abi_root_dir = "../packages/cafecosmos-contracts/abi"

def load_abis() -> dict:
    """
    Load all ABI files from the given directory structure.
    Returns a dictionary with contract names as keys and their ABIs as values.
    """
    abis = {}
    root_path = Path(abi_root_dir)
    
    # Walk through all subdirectories
    for contract_dir in root_path.iterdir():
        if contract_dir.is_dir():
            # Look for the .abi.json file in each contract directory
            abi_file = next(contract_dir.glob("*.abi.json"), None)
            if abi_file:
                try:
                    with open(abi_file, 'r') as f:
                        contract_name = contract_dir.name.replace(".sol", "")
                        abis[contract_name] = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"Error loading {abi_file}: {e}")
                except Exception as e:
                    print(f"Error processing {abi_file}: {e}")
    
    return abis

def get_config() -> dict:
    with open("../config.yaml", 'r') as f:
        return yaml.safe_load(f)


class CafeCosmos:

    
    def __init__(self, network, world_address=None):

        contract_abis = load_abis()
        config = get_config()

        if(world_address is None):
            world_address = config["worlds"][network]

        self.world_address = world_address
        self.rpc = config["networks"][network][0]["rpc"]

        # print("hey")
        print("Connecting to network: ", self.rpc)
        print(help(networks))
        # networks.provider.network.connect(self.rpc)
        # networks.network_manager
        # networks.network_manager.

        # self.world = Contract(world_address, abi=contract_abis["IWorld"])
        # chain.chain_manager
        
        # self.landTransform = Contract(world_address, abi=contract_abis["LandTransform"])
        # self.landNFTs = Contract(world_address, abi=contract_abis["LandNFTs"])
        # self.landQuestTaskProgressUpdate = Contract(world_address, abi=contract_abis["LandQuestTaskProgressUpdate"])
        # self.perlinItemConfig = Contract(world_address, abi=contract_abis["PerlinItemConfig"])
        # self.vesting = Contract(world_address, abi=contract_abis["Vesting"])
        # self.redistributor = Contract(world_address, abi=contract_abis["Redistributor"])



if __name__ == "__main__":

    # worlds = load_worlds()

    network = "redstone-testnet"
    # world_address = worlds[network]

    cafe = CafeCosmos(network=network)
    # print(cafe.world÷)

