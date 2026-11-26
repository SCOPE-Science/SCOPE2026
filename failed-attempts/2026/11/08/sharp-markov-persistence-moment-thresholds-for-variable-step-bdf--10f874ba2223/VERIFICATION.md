---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The zero-right-hand-side BDF2 formula gives Δ_n = R_n² Δ_(n−1)/(1+2R_n), so Z is a positive sum of products of the multipliers a,b. Their product is r/[(1+2r)(r+2)]<1. Equal limiting state frequencies (including deterministic alternation) give log-product rate log(ab)/2<0 and almost-sure absolute summability. Write A=a^s, B=b^s and M=diag(A,B)P for the two-state transition matrix P. Expected s-powers of products are components of iterates of M; exponential decay when ρ(M)<1 gives a finite moment by Minkowski for s≥1 and subadditivity for 0<s<1. Conversely finite conditional moments obey m>Mm from the strictly positive additive term 1, whence a positive left Perron vector gives ρ(M)<1 even for the irreducible two-cycle at p=0. The determinant at 1 is 1−AB−p(A+B−2AB). The other eigenvalue is <1: M is diagonally similar to a symmetric matrix whose smaller eigenvalue is at most pB<1. For a≤1, all row sums are ≤1, one strictly smaller; irreducibility gives ρ<1. For a>1, the determinant decreases from 1−AB>0 to (1−A)(1−B)<0 and hence gives precisely the displayed cutoff and divergence at equality. Substitution gives 24/31 and 171/283 at r=3, bracketing 7/10. At p=0 the two phase sums are (1+a)/(1−ab) and (1+b)/(1−ab). The degenerate r=1 uses two labels for the same physical ratio; the deterministic Z=3/2 is independent of p. This is an infinite-iteration startup-amplification statement, not a finite-horizon mesh-stability result. The frozen check script was inspected, not run; it samples the algebra and is not needed for the proof.

## originality

FAIL

The all-real-moment frontier, including the critical case, is mechanically implied by the known BDF2 parasitic multiplier and the classical iid perpetuity moment theorem applied to iid pairs of consecutive high/low runs. No separate stochastic effect or nontrivial new lemma is needed for this specialization. This is demonstrated prior implication, not a claim that an earlier paper printed the identical rational formula.

## value

FAIL

The contrast between pathwise and moment behavior is a useful example for interpreting correlated steps. As a new mathematical finding, however, the exact frontier and numerical witness are routine geometric-sum substitutions in the established positive-perpetuity criterion for the standard scalar BDF2 mode. The frozen statement gives no distinct BDF2 mechanism or stability conclusion beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
