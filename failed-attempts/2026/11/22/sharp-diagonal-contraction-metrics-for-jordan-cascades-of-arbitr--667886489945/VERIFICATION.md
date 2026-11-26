---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For x_i=√(p_i/p_{i+1}) the Hermitian part is −aI+(c/2)T(x) on a positive weighted path. Its product ∏x_i=√(p_1/p_n) is ≥K^(−1/2) without any monotonicity assumption on P. In the Rayleigh quotient for u=(1,√2,…,√2,1) the denominator is 2(n−1) and the product of u_i u_{i+1} is 2^(n−2). AM–GM proves the asserted bound and forces all x_i u_i u_{i+1} equal if sharp; saturation also forces p_n/p_1=K. The forced edges are √2q at the ends and q in the interior. Indeed the path has Tu=2qu, certifying sharpness by positivity. Normalizing p_1=1 recovers the proposed entries; the two end ratios are (2q²)^−1 and internal ratios q^−2. If q>1/√2 the first ratio alone makes p_2<1 with p_n=K, violating the budget. Compactness after normalizing min p_i=1 makes nonattainment of the universal lower bound strictly nonsharp below 2^(n−3). The boundary example and exact least budget follow from the equivalence of μ_P(G)≤0 and all-time weighted semigroup contractivity (differentiate squared energy at zero or along the flow). Independently checked 12 rational LDL certificates for the candidate and feasibility on both sides of onset: python3 /workspace/reproductions/check_frozen_math.py 4. No uploaded checker executed; these diagnostics supplement the arbitrary-n proof.

## originality

FAIL

The central all-length lower bound, sharp high-budget value and attaining profile are direct consequences of the classical Berger power-norm inequality and the explicit Crabb extremizing shifts. Applied to the last nonzero power of the diagonally scaled shift, they give exactly the claimed constant and the candidate. Recovering the metric and testing the two end ratios gives the claimed feasible branch and the contractivity budget by elementary translation. The frozen proof correctly adds an elementary direct equality-rigidity argument; the available modern passage does not verify the historically complete classification of equality cases, so the assessment does not assert that every detail is stated verbatim in Crabb. The verified implication, not inaccessible older text or the dimensional four-stage overlap, is the failure reason.

## value

FAIL

The sharp conditioning of a nonnormal cascade is a natural question, and the frozen text is a useful self-contained exposition of the high-budget answer. But the exact invariant advanced here is mechanically inherited from the classical power bound and its explicit sharp shift, with only the metric ratios and an elementary sharpness/rigidity test left to check. The record does not solve the lower-budget problem or present a nonroutine independent consequence. The original claim therefore fails the value bar for a narrow exact finding, not because conditioned contractivity is unmotivated or the proof is wrong.

The dated certificate retains the supplied scientific assessment, sources and limitations.
