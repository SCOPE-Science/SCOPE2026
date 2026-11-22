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

# Verification of the characteristic-three projective-plane wave

Two executable Python programs accompany the proof. They are ordinary arithmetic checkers, not an independent audit and not a substitute for the universal derivation.

## Exact homogeneous-coordinate checker

From the package directory, run:

```
python3 verify_planes.py
```

This program requires Python 3 and NumPy. It independently constructs the homogeneous-coordinate projective planes of orders \(2,3,4,5,7\) (including explicit field arithmetic over \(\mathbb F_4\)); verifies line cardinalities and \(BB^{\mathsf T}=sI+J\); constructs the whole matrix \(T\) over \(\mathbb F_3\); and uses modular Gaussian elimination on \(T^t-I\) for each divisor of the expected global clock. It also verifies \(T^L=I\) for the listed order \(L\). Recorded actual results:

| Plane order | Incidence rank | Divisor times | Actual fixed-space dimensions | Global clock |
|---|---:|---|---|---:|
| 2 | 6 | 1,2,4,8 | 0,0,4,28 | 8 |
| 3 | 7 | 1,2,3,4,6,12 | 1,2,2,26,4,52 | 12 |
| 4 | 21 | 1,2,3,6,9,18 | 20,40,41,82,42,84 | 18 |
| 5 | 30 | 1,2,4,8 | 0,0,4,124 | 8 |
| 7 | 57 | 1,2,3,6,9,18 | 56,112,113,226,114,228 | 18 |

## Independently implemented affine-coordinate checker

Run:

```
python3 verify_affine.py
```

This program uses only the Python standard library. It constructs incidences from affine points, lines of each slope, vertical lines, and infinity points; iterates every basis vector under the full two-level neighbor update; and computes nullities by a separately written integer-only elimination. It verifies all divisor-time dimensions for orders \(2,3,5\), agreeing with the first checker.

## Limits

No full-state enumeration is made of the exponentially many labelled configurations. The programs test only the specified Desarguesian examples. The theorem for all finite planes, every finite extension of characteristic three, and every positive time is established in RESULT.md from the plane identities and exact Jordan-block computation. The checkers do not establish historical priority or supply independent peer review.
