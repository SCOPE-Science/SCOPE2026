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
# Reproducibility and limits

Execute `python3 verify_direct.py` and `python3 verify_slots.py` with Python 3.10 or later; only the standard library is required. Each must exit with status zero and reproduce the corresponding embedded `.out` file. The direct program constructs \(L(K_n)\) by explicit edge incidence, tests each candidate vertex subset for domination and a perfect matching, then checks all legal one-selected-vertex slides for \(n=4,7\). The slot program generates the complete space reached from one centered-triple configuration for \(m=1,2,3\), checking counts and regularity.

Direct output:
```
n=4: optimal_size=2, states=12, degree=4, edges=24, triangles=8, components=1: PASS
n=7: optimal_size=4, states=630, degree=8, edges=2520, triangles=840, components=1: PASS
```
Slot output:
```
m=1: states=12, degree=4, edges=24, eccentricity=3, layers=[(0, 1), (1, 4), (2, 6), (3, 1)]: PASS
m=2: states=630, degree=8, edges=2520, eccentricity=6, layers=[(0, 1), (1, 8), (2, 32), (3, 86), (4, 176), (5, 261), (6, 66)]: PASS
m=3: states=75600, degree=12, edges=453600, eccentricity=10, layers=[(0, 1), (1, 12), (2, 78), (3, 383), (4, 1576), (5, 5331), (6, 13770), (7, 24664), (8, 23409), (9, 6144), (10, 232)]: PASS
```
The finite traversal checks are not substitutes for the proof valid for all integers \(m\ge1\). Eccentricities in output are finite observations, not a claimed general diameter formula. The independently audited status above remains unperformed.
