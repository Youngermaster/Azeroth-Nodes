import requests


class DFSClient:
    def __init__(self, name_node_address: str):
        self.name_node = name_node_address

    def write_file(self, file_name: str, file_data: str) -> None:
        block_size = 1024 * 1024  # 1MB per block
        blocks = [
            file_data[i : i + block_size] for i in range(0, len(file_data), block_size)
        ]
        data_blocks = []
        for block_id, block_data in enumerate(blocks):
            data_node = self.name_node
            response = requests.post(
                f"{data_node}/store_block",
                json={"block_id": str(block_id), "block_data": block_data},
            )
            if response.ok:
                data_blocks.append((block_id, data_node))
        requests.post(
            f"{self.name_node}/store_file_metadata",
            json={"file_name": file_name, "data_blocks": data_blocks},
        )

    def read_file(self, file_name: str) -> str:
        response = requests.get(
            f"{self.name_node}/retrieve_file_metadata", json={"file_name": file_name}
        )
        if response.ok:
            data_blocks = response.json()
            file_data = []
            for block_id, data_node in data_blocks:
                block_response = requests.get(
                    f"{data_node}/retrieve_block", json={"block_id": str(block_id)}
                )
                if block_response.ok:
                    file_data.append(block_response.text)
            return "".join(file_data)
        return ""

    def delete_file(self, file_name: str) -> None:
        data_blocks = requests.post(
            f"{self.name_node}/delete_file_metadata", json={"file_name": file_name}
        )
        if data_blocks.ok:
            for block_id, data_node in data_blocks.json():
                requests.post(
                    f"{data_node}/delete_block", json={"block_id": str(block_id)}
                )
