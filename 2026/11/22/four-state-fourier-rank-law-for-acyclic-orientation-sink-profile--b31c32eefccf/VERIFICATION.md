---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The signed sum weights orientations, including repetitions of the same sink set. With rightward edge bit 1, the terminal signs indeed use left bit 0 and right bit 1, and an interior sink has bit pair (1,0). This gives the displayed transfer, including the empty interior product at n=2. A zero interior letter gives J=ee^T, and zero endpoints give e or e^T. Factorization at these zeros and B^4=-4I then give the run restrictions; the full selection instead uses exponent n−2 with both signed terminal vectors and vanishes at n=0 mod 4. Empty selection has sum 2^(n−1). The four projective transitions and terminal survival counts are correct; the live states form a strongly connected graph with a self-loop. Independent symbolic calculation confirmed the characteristic polynomial, generating function and positive root 1.85356027758. Primitivity and the nonnegative nonzero initial and terminal vectors give a positive leading coefficient and exponential decay of the surviving fraction. Independent orientation enumeration and integer FWHT agreed frequency by frequency for n=2 through 14 and reproduced rank 3878 at n=14. The recurrence yields 157406 at n=20.

## originality

PASS

The distinct claims are the exact positional support test and resulting all-order rank law. Multivariate orientation polynomials provide substantially the same sink data, and a closely matching Fourier study provides a path singularity obstruction; neither inspected result classifies the full nonzero support on paths.

## value

PASS

For a natural inhomogeneous Boolean observation operator, a singularity witness alone leaves both recoverable coordinates and information dimension open. This theorem identifies every recoverable character and quantifies rank and its decay for all path orders. The endpoint and full-run exceptions are needed to apply the criterion, not redundant numerical checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
