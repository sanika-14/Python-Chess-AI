Here’s the updated README to reflect the option of playing either against another player or the AI:

---

# Python-Chess-AI

Welcome to **Python-Chess-AI**, a project aimed at developing a chess-playing platform using Python. You can either play against another player or challenge a powerful AI powered by the **Stockfish** engine.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Project Overview
This project offers two modes: **Player vs Player** and **Player vs AI**. In AI mode, the game uses **Stockfish**, one of the strongest open-source chess engines, to provide a competitive and intelligent chess-playing experience. You can also enjoy classic two-player chess locally.

## Features
- **Player vs Player**: Play chess with another person locally on the same machine.
- **Player vs AI**: Play against the Stockfish-powered AI that evaluates the board and makes intelligent moves.
- Standard two-player chess rules are fully implemented.
- Graphical user interface (GUI) for easy gameplay.
- Ability to switch between game modes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sanika-14/Python-Chess-AI.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Python-Chess-AI
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download and install Stockfish:
    - For Windows: Download [Stockfish](https://stockfishchess.org/download/) and follow the installation instructions.
    - For Linux: You can install Stockfish using your package manager.
        ```bash
        sudo apt install stockfish
        ```

5. Run the chess game:
    ```bash
    python chess-game-ai.py
    ```

## Usage
1. After starting the game, a graphical chessboard will appear.
2. You will be prompted to select the game mode:
   - **Player vs Player**: Both players take turns using the same interface.
   - **Player vs AI**: The AI will make moves using Stockfish after each player's turn.
3. Make your moves by clicking on the pieces and selecting the destination squares.

## Technologies Used
- **Python**: The core programming language for this project.
- **Pygame**: For implementing the graphical user interface (GUI).
- **Stockfish**: The chess engine used for AI move generation and board evaluation.



---

