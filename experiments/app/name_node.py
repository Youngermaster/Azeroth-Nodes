class NameNode:
    def __init__(self) -> None:
        self.metadata = {}
        self.data_nodes = []

    def register_data_node(self, data_node_address: str) -> None:
        self.data_nodes.append(data_node_address)

    def store_file_metadata(self, file_name: str, data_blocks) -> None:
        self.metadata[file_name] = data_blocks
