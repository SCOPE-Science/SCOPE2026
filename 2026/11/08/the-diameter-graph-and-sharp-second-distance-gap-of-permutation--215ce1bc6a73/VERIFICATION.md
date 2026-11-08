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

# Verification of the diameter graph and sharp finite-image second-distance gap

The complete proof, including the unrestricted quantifiers, is in `RESULT.md`. The following computation supplies standalone exact-integer sanity checks; it is **not** an exhaustive proof over infinitely many dimensions or over uncountably many points of the convex image.

Run `python3 verify.py` using Python 3 and its standard library, without installation or external datasets. The actual executed result was:

```
PASS: 694526 exact-integer assertions; complete projected-X-ray pair checks for k=2,...,7, projection-profile checks through k=8, and constructed exact witnesses through k=100.
```

For every \(2\le k\le7\), the program generates **every permutation**, deduplicates their X-ray vectors, compares every distinct vector pair, checks the exact maximum and diameter-pair set, and verifies the runner-up distance when it exists. At \(k=8\) it checks imagewise norm and occupancy inequalities without exhausting every image pair. It also checks the exact witnesses through \(k=100\) and deterministic pseudorandom pairs through \(k=15\). The code deliberately uses integers only, so no floating-point tolerances or unstated numerical certificates enter these checks.

Two critical assertions have direct theoretical certificates independent of the program: (i) a noncentral permutation X-ray has each coordinate at most \(k-1\), with near-maximal occupancy forcing one of two exact vectors; (ii) strict convexity of squared Euclidean distance prohibits additional diametral pairs in the convex hull. Those arguments, plus the explicit runner-up permutation and concentration inequality, prove all claimed values for unrestricted integer \(k\ge2\).

The runner-up assertion concerns only the finite set of distinct permutation X-rays. It is **not** a claimed missing interval of pairwise distances within the full convex polytope. Independent audit of the mathematics has not been performed.
