import requests


class DFSClient:
    def __init__(self, name_node_address):
        self.name_node = name_node_address

    def write_file(self, file_name, file_data):
        data_blocks = []
        for block_id, block_data in enumerate(file_data):
            data_blocks.append(block_id)
            requests.post(
                f"{self.name_node}/store_block",
                json={"block_id": block_id, "block_data": block_data},
            )
        requests.post(
            f"{self.name_node}/store_file_metadata",
            json={"file_name": file_name, "data_blocks": data_blocks},
        )

    def read_file(self, file_name):
        data_blocks = requests.get(
            f"{self.name_node}/retrieve_file_metadata", json={"file_name": file_name}
        ).json()
        file_data = []
        for block_id in data_blocks:
            file_data.append(
                requests.get(
                    f"{self.name_node}/retrieve_block", json={"block_id": block_id}
                ).json()
            )
        return file_data
