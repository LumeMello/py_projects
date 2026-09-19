# ⚡ RSA-CHRONO // CIPHER TERMINAL

> *"Neon signs buzz against the rain. The message must pass undetected."*

A lightweight implementation of asymmetric RSA encryption and custom alphanumeric stream encoding in Python.

---

### 📂 PROJECT STRUCTURE

```bash
├── TextToNumber.py    # String ↔ Number vector encoding/decoding
└── RSA.py             # Modular exponentiation cipher engine
```

---

### ⚠️ SECURITY NOTICE

* **Educational Implementation**: Uses textbook RSA arithmetic with a small composite modulus ($n = 851$).
* **Production Standards**: Production cryptographic workloads require 2048+ bit primes and randomized padding schemes (such as OAEP).
