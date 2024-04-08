class NameNode:
    def __init__(self) -> None:
        self.metadata = {}  # maps file names to lists of (block_id, data_node) tuples
        self.data_nodes = []  # stores DataNode addresses

    def register_data_node(self, data_node_address: str) -> None:
        if data_node_address not in self.data_nodes:
            self.data_nodes.append(data_node_address)

    def store_file_metadata(self, file_name: str, data_blocks: list) -> None:
        self.metadata[file_name] = data_blocks

    def get_file_metadata(self, file_name: str) -> list:
        return self.metadata.get(file_name, [])
