# 🎯 Genetic Algorithm: Find Numbers with Target Product

This is a simple Python project that uses a **Genetic Algorithm** to evolve a list of numbers whose product equals a target value `T`.

It’s a beginner-friendly project designed like a first-year computer science student would write. No external libraries are required — just basic Python!

---

## 📌 Problem Statement

> Given a **target number `T`** and a **list length `k`**, find a list of `k` integers (from 1 to 9) such that:
> 
> ```
> num[0] * num[1] * ... * num[k-1] == T
> ```

✅ Example:

---

## 🧬 How It Works

This project uses a basic **Genetic Algorithm (GA)** approach:
1. Create a random population of number lists.
2. Evaluate how close each list's product is to the target.
3. Select the best lists and mix them (crossover).
4. Randomly change some numbers (mutation).
5. Repeat until a list is found that exactly matches the target product.

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Save the code to a file, like `main.py`.
3. Open terminal or command prompt and run:

```bash
python main.py
```
📁 genetic-algorithm-product
├── main.py        ← main program code
└── README.md      ← this file

🙋‍♂️ Author
Shahriyar Sumon
👨‍🎓 CSE Student | Loves AI, Algorithms & Creative Ideas
