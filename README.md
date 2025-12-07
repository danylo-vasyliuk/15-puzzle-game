# 15 Puzzle Game

A clean, maintainable, and testable implementation of the classic **15 Puzzle Game**  
designed for terminal play, built with **Python 3.13**.

The project follows clean separation of responsibilities:

- **Game logic** (pure model, no I/O)
- **Board generation** (ensures solvable puzzles)
- **Presentation layer** (terminal rendering)
- **Input handling** (isolated)
- **App coordination** (game loop)

---

## 🧩 Features

- Fully solvable random board generation (random walk algorithm)
- Terminal-based UI  
- Clean modular architecture  
- Unit tests included  

---

## 🚀 Installation & Setup

### **1. Install dependencies (Poetry)**

If you want to run locally:

```bash
poetry install
poetry env activate
python fifteen/run.py
```

Running with Docker:

```bash
docker compose build
```

```bash
docker compose run --rm puzzle
```
