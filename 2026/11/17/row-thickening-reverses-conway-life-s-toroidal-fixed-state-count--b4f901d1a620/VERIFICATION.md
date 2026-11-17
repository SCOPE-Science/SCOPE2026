---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run from a directory containing the enclosed files:

```bash
python3 check_life4_transfer.py > actual_transfer.txt
cmp actual_transfer.txt transfer_output.txt
g++ -O2 -std=c++17 check_life4_direct.cpp -o check_life4_direct
./check_life4_direct > actual_direct.txt
cmp actual_direct.txt direct_output.txt
```

Python 3 and SymPy are required for the exact polynomial factorization; a C++17 compiler is required for the independent direct-update enumeration.

The Python program independently constructs every legal triple-column transition, verifies the strong component decomposition, produces an exact degree-127 characteristic polynomial and trace values, constructs the height-three resonance component, tests the exact rational Perron certificate, and verifies the all-circumference inequality using a spectral bound plus finitely many exact traces. Its saved output is `transfer_output.txt`.

The C++ program directly applies the eight-neighbor Moore B3/S23 rule to every binary configuration on heights four, circumferences three through six. Its saved output is `direct_output.txt`.

**Scientific limit:** The finite brute-force enumeration by itself proves only these four cases; the theorem for all circumferences follows from the transfer identity, spectral inequalities and exact finite remainder. No independent external mathematical audit has been performed.
