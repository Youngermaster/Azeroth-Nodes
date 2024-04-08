import threading
import time
from name_node import NameNode
from data_node import DataNode
from client import DFSClient


def start_name_node():
    global name_node
    name_node = NameNode()
    print("NameNode started.")


def start_data_node():
    global data_node
    data_node = DataNode(storage_location="/tmp/azeroth_nodes")
    print("DataNode started at /tmp/azeroth_nodes.")


def simulate_client_operations():
    client = DFSClient(name_node_address="http://localhost:5000")

    # Example file operations
    file_name = "example.txt"
    file_content = "Hello, Azeroth Nodes! This is a test file."

    print("Writing file...")
    client.write_file(file_name, file_content)

    print("Reading file...")
    retrieved_content = client.read_file(file_name)
    print("Retrieved content:", retrieved_content)

    print("Deleting file...")
    client.delete_file(file_name)
    print("File deleted.")


if __name__ == "__main__":
    print("Welcome to Azeroth Nodes!")

    # Start NameNode and DataNode in separate threads
    name_node_thread = threading.Thread(target=start_name_node)
    data_node_thread = threading.Thread(target=start_data_node)

    name_node_thread.start()
    data_node_thread.start()

    # Ensure servers are up before starting client operations
    time.sleep(1)

    # Simulate client operations
    simulate_client_operations()
