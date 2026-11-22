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

# Reproducibility

Use a standard Python 3 installation and a C++17 compiler. In a directory containing `verify_python.py`, `verify_cpp.cpp`, and the original `orbit_table.csv`, run:

```sh
python3 verify_python.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cpp.cpp -o paley27_check
./paley27_check
```

The Python program recreates the orbit CSV and checks the face coefficients, the absence of four-point off-support shattering, the entire orbit census, the 351 maximal triples, their pair multiplicities, and mod-two boundary ranks. The C++ program uses a different irreducible field polynomial and quadratic-residue test and independently checks all support counts and ranks. The correct output ends with `PYTHON_EXHAUSTIVE_OK` and `CPP_INDEPENDENT_EXHAUSTIVE_OK`; recorded runs are supplied in `python_output.txt` and `cpp_output.txt`. Recompute the CSV rather than trusting the stored version. The supporting files are ordinary finite enumerations: no numerical approximation or infeasibility inference from timeout occurs.

The resulting invariants are exact for the stated finite field only. Mod-two homology does not establish integral homology or a homotopy equivalence. No independent mathematical audit has been performed.
