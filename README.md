# Turbo-Drive
Technology : Python, Network Programming
This is a simple multiplayer car game implemented using a client-server architecture. Players control a car and navigate through lanes, avoiding collisions with other vehicles.
# Features
Client-Server Architecture: The game follows a client-server model, allowing multiple players to connect and play together.

Player Authentication: Players need to log in with a username and password before starting the game.

Game Controls: Players can control their cars using the left and right arrow keys. The objective is to navigate through lanes, avoid collisions, and score points.

Scoring System: Players earn points for successfully navigating through lanes. The game speed increases as the player's score goes up.

Game Over Screen: When a collision occurs, the game enters a "Game Over" state. Players can choose to play again or exit.

Multiplayer Interaction: Player movements are sent to the server, which updates the game state and broadcasts it to all connected clients.

# Getting Started
**Prerequisites**
Python 3.x
Pygame library (for the client-side)

# Technologies Used
Python: The core programming language used for both client and server implementations.

Pygame: A cross-platform set of Python modules designed for writing video games. Used on the client-side for handling game graphics and user input.

Socket Programming: Python's built-in socket library is used for communication between the client and server.

Threading: Threading is employed for handling multiple client connections simultaneously.

Pickle: The pickle module is used for serializing and deserializing Python objects to facilitate data exchange between the client and server.

Tkinter: Used for creating the graphical user interface (GUI) on the client side, providing a login window for user authentication.
