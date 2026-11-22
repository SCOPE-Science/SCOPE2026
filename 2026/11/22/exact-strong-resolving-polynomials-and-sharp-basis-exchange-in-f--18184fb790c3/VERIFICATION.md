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
# Verification

The infinite-family theorem is established by the geometric proof in `RESULT.md`. The standalone programs perform independent finite crosschecks, not an exhaustive search of all finite generalized quadrangles.

Run `python3 verify.py` with Python 3.8 or later. It constructs the symplectic \(W(3,2)\) from nonzero vectors of \(\mathbb F_2^4\) and a quadrangle of order \((2,4)\) from 27 cubic-surface curve labels, then tests incidence axioms, all-pairs distances and mutual maximality, independent-set omission counts on each shore, the direct strong-resolving criterion for all 225 bases of \(W(3,2)\), all 593,775 six-vertex omission candidates, and basis-exchange components.

Compile and run `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_duads.cpp -o verify_duads && ./verify_duads`. This independently constructs \(W(3,2)\) from 15 duads and 15 synthemes of \(K_6\), and verifies the MMD graph, all six-omission candidates, exchange edges, connectivity and diameter.

Actual tested output (Python):

```text
W(3,2) exchange k= 1 components [(1, 225)] edges 0
W(3,2) exchange k= 2 components [(225, 1)] edges 1350
W(3,2) verified points 15 lines 15 MMD edges 120 strong dim 24 bases 225 point omit counts {0: 1, 1: 15, 2: 45, 3: 15} line omit counts {0: 1, 1: 15, 2: 45, 3: 15}
GQ(2,4) exchange k= 1 components [(1, 1215)] edges 0
GQ(2,4) exchange k= 2 components [(45, 27)] edges 7290
GQ(2,4) exchange k= 3 components [(45, 27)] edges 26730
GQ(2,4) exchange k= 4 components [(1215, 1)] edges 32805
GQ(2,4) verified points 27 lines 45 MMD edges 936 strong dim 64 bases 1215 point omit counts {0: 1, 1: 27, 2: 135, 3: 45} line omit counts {0: 1, 1: 45, 2: 270, 3: 270, 4: 135, 5: 27}
ALL CHECKS PASS
```

Actual tested output (C++17):

```text
W(3,2) independent duad-syntheme construction: points 15, lines 15, MMD edges 120, six-vertex omitted independent sets 225, swap edges 1350, diameter 4. ALL CHECKS PASS
```

All checks use exact combinatorial or integer arithmetic. They do not test every order \((s,t)\), establish existence for arbitrary parameters, or provide independent external validation. Originality is assessed against inspected sources and may be revisited if earlier priority evidence appears.
