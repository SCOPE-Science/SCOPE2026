---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

This PASS is for repairs/4/RESULT.md. The frozen formula under pairwise distinctness is correct, but the frozen scope line 29 explicitly and falsely says the determinant vanishes otherwise. For C_4 with d=1 and (b_0,b_1,b_2)=(0,1,0), B is the projection onto the paired modes: its sensor rows are (1,0,−1,0)/2 and (0,1,0,−1)/2, giving determinant 1/4 after the first two rows e_0^T,e_1^T. The repair gives the exact condition without an injectivity assumption and removes conflation with eventual observability. For each Fourier pair, the antisymmetric combination of sensor multipliers is ζ^(−kd)−ζ^(kd), with the normalization N^−M supplied by all columns. By multilinearity the two paired eigenvectors can be replaced by one time vector in each sensor block after extracting that scalar, even in the zero case. Only the two opposite assignments of the singleton columns survive the block expansion; the products of Vandermondes agree and the block-assignment signs are opposite, resulting in |(−1)^d−1|. Even offsets or a nontrivial gcd(d,M) then give zero; at coprime offsets multiplication by d permutes the residues and the paired product is M by the root-of-unity product. Both Vandermondes contain every pair of indices except {0,M}, proving precisely the stated collision exception. The row count rules out fewer samples. For adjacency at d=1, before time t the seen coordinates are the consecutive interval [1−t,t]; the two walk-count rows add −t and 1+t with unit coefficients and no wraparound collision because the final interval has length N. This gives integer unit triangularity, and the universal determinant transfers |det|=1 to all coprime d. CHECK.py and VERIFICATION.md were inspected, not executed; their recorded exact integer cases only test adjacency and affine evolutions, and neither the general formula nor the collision correction relies on them.

## originality

PASS

The repaired exact full-state determinant and adjacency unimodularity remain distinct from the closest checked sources to the best of current knowledge. Coprimality at the minimal horizon is not claimed as the contribution: same-day exact-rank results give rank there and at one longer horizon. Determinant magnitude is additional to rank. The collision exception follows from the corrected exact formula and is not claimed as a separate originality result.

## value

PASS

The exact full-state square determinant at the minimal conceivable number of samples is a useful invariant beyond observability. It identifies equal volume across every successful placement and reveals unit lattice index for adjacency, so exact integral reconstruction needs no denominators. This provides a genuine additional conclusion, not a stability claim or merely the endpoint-collision counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
