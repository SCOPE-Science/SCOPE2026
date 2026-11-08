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

# Reproduction and verification

Use the supplied `verify.py` and `crosscheck.cpp`. The first constructs the \(q^2\)-vertex directed graph and computes its exact in-arborescence minors using Bareiss elimination for every integer \(2\le q\le6\), then enumerates Euler tours with a fixed first edge for \(q=2,3\). The second independently enumerates ordered outgoing-edge schedules for \(q=2,3\), retaining schedules that form a single complete circuit.

```sh
python3 verify.py
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck
```

The Python computation reports `VERIFY_OK`. The C++ computation reports `CROSSCHECK_OK`. Both tests use exact integer operations. The case \(q=6\) is checked by a \(35\times35\) integer determinant, not a floating-point approximation. The proof in `RESULT.md` is symbolic for all \(q\ge2\); no computation of finitely many cases could establish the infinite statement. No independent scientific or historical-priority audit has been performed.
