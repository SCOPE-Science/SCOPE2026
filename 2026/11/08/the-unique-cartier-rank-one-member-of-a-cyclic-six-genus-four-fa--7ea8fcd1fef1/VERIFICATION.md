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

The two accompanying Python 3 programs use only the standard library:

```bash
python3 verify_symbolic.py
python3 verify_finite.py
```

The symbolic checker performs multivariate polynomial arithmetic in characteristic \(11\), recomputes the five Cartier coefficient entries from \(Q(t)^5\), and checks the linear elimination identity and both cleared-denominator identities by exact polynomial comparison. It checks the exceptional discriminant and Cartier entry as well as the excluded singular parameter. A successful run prints `VERIFY_SYMBOLIC_OK`.

The finite checker independently expands the full degree-ten branch polynomial to the fifth power for all \(121\) pairs over \(\mathbb F_{11}\), discards singular models by the cubic discriminant criterion, and row-reduces every resulting four-by-four matrix modulo \(11\). It verifies the \(101\) smooth pairs and their \(83,17,1\) rank-derived \(a\)-number counts. A successful run prints `VERIFY_FINITE_OK`.

The full algebraically-closed classification rests on the stated polynomial vanishing and elimination proof, not the finite-field enumeration. No independent external audit or computation on every algebraic-closure point has been performed.
