import socket
import threading
import pickle

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
server_socket.bind(server_address)
server_socket.listen(5)

# List to store connected clients and their game state
clients = []

# Function to handle each client
def handle_client(client_socket, player_id):
    # Initialize player's game state
    player_lane = 1  # Start in the center lane
    speed = 2
    score = 0

    while True:
        try:
            # Receive player input
            data = client_socket.recv(1024)
            if not data:
                break

            input_data = pickle.loads(data)

            # Update player's game state
            player_lane = input_data['player_lane']

            # Send updated game state to all clients
            game_state = {'player_lane': player_lane, 'speed': speed, 'score': score}
            for client in clients:
                client[0].send(pickle.dumps(game_state))

        except Exception as e:
            print(f"Error handling client {player_id}: {e}")
            break

    # Remove the client from the list upon disconnection
    clients.remove((client_socket, player_id))
    client_socket.close()

# Accept and handle clients in separate threads
player_id = 1
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    
    # Add the new client to the list
    clients.append((client_socket, player_id))

    # Start a new thread for the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, player_id))
    client_handler.start()

    # Increment player_id for the next client
    player_id += 1
