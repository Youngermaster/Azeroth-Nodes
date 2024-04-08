class DataNode:
    def __init__(self, storage_location):
        self.storage = storage_location

    def store_block(self, block_id, block_data):
        with open(f"{self.storage}/{block_id}", "w") as file:
            file.write(block_data)

    def retrieve_block(self, block_id):
        with open(f"{self.storage}/{block_id}", "r") as file:
            return file.read()
