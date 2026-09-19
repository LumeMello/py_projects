# ⚡ RSA-CHRONO // CIPHER TERMINAL

> *"Neon signs buzz against the rain. The message must pass undetected."*

A lightweight implementation of asymmetric RSA encryption and custom alphanumeric stream encoding in Python.

---

### 📼 SYSTEM OVERVIEW

The pipeline splits the encryption pipeline into two distinct components:
* **Character Mapping (`TextToNumber.py`)**: Converts lowercase alphanumeric text and spaces into a normalized integer stream[span_0](start_span)[span_0](end_span).
* **Modular Arithmetic Engine (`RSA.py`)**: Executes textbook RSA modular exponentiation over discrete vectors using public and private key pairs[span_1](start_span)[span_1](end_span).

---

### 📂 PROJECT STRUCTURE

```bash
├── TextToNumber.py    # String ↔ Number vector encoding/decoding
└── RSA.py             # Modular exponentiation cipher engine
```

---

### ⚙️ PROTOCOL SPECIFICATIONS

#### 1. Character Encoding Protocol (`TextToNumber.py`)
* **Spaces (`' '`)** $\rightarrow$ `99`[span_2](start_span)[span_2](end_span)
* **Alphabet (`a-z`)** $\rightarrow$ `10` through `35` (calculated as `ord(char) - 97 + 10`)[span_3](start_span)[span_3](end_span)

#### 2. Key Parameters (`RSA.py`)
* **Modulus ($n$)**: `851`[span_4](start_span)[span_4](end_span)
* **Public Exponent ($e$)**: `5`[span_5](start_span)[span_5](end_span)
* **Private Exponent ($d$)**: `317`[span_6](start_span)[span_6](end_span)

---

### 🕹️ EXECUTION & USAGE

**Encoding and Decoding Text:**
```bash
python3 TextToNumber.py
```
* **Sample Text**: `"Hello World"`[span_7](start_span)[span_7](end_span)
* **Function**: Maps characters to values via `text_to_numbers()` and reverses them using `numbers_to_text()`[span_8](start_span)[span_8](end_span).

**Encrypting & Decrypting Data:**
```bash
python3 RSA.py
```
* **Encryption**: Computes $(b^e) \pmod{n}$ via `cript(b, n, e)`[span_9](start_span)[span_9](end_span).
* **Decryption**: Computes $(a^d) \pmod{n}$ via `decript(a, n, d)`[span_10](start_span)[span_10](end_span).
* **Target Vector**: `[18, 22, 99, 28, 14, 23, 25, 10, 18]`[span_11](start_span)[span_11](end_span).

---

### ⚠️ SECURITY NOTICE

* **Educational Implementation**: Uses textbook RSA arithmetic with a small composite modulus ($n = 851$)[span_12](start_span)[span_12](end_span).
* **Production Standards**: Production cryptographic workloads require 2048+ bit primes and randomized padding schemes (such as OAEP).
