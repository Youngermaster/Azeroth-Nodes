import os


class DataNode:
    def __init__(self, storage_location: str):
        self.storage = storage_location
        os.makedirs(storage_location, exist_ok=True)  # Ensures directory exists

    def store_block(self, block_id: str, block_data: str) -> None:
        block_path = os.path.join(self.storage, block_id)
        with open(block_path, "w") as file:
            file.write(block_data)

    def retrieve_block(self, block_id: str) -> str:
        block_path = os.path.join(self.storage, block_id)
        if os.path.exists(block_path):
            with open(block_path, "r") as file:
                return file.read()
        return ""  # Returns an empty string if block not found
