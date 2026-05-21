# TinyTrack AI

TinyTrack AI is a small learning project for understanding visual machine learning and reinforcement learning.

The goal is to build a simple 2D car environment first, then later train an AI agent to drive inside it.

## Current Stage

Right now the project is in the basic Pygame stage:

- open a game window
- draw a simple car rectangle
- move the car with arrow keys
- keep the car inside the screen
- draw a simple rectangular track
- learn how the game loop works

AI training will be added after the environment is easy to understand.

## Tech Stack

- Python
- Pygame
- Gymnasium
- Stable-Baselines3
- PyTorch

## Run

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the current environment:

```bash
python tinytrack_env.py
```

## Learning Goal

This project is for learning:

- how game loops work
- how keyboard input works
- how screen coordinates work
- how boundary clamping works
- how visual simulations are built
- what an AI environment is
- how observations, actions, rewards, and episodes work
- how reinforcement learning can train an agent through trial and error

## Final Goal

The final version should show a small car learning to drive around a 2D track using reinforcement learning.
