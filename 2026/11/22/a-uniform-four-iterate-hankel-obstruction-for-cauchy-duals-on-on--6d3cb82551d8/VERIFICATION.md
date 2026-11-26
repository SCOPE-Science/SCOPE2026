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

On the normalized point basis the squared Cauchy-dual weight for an edge z→w is μ(w)/(μ(z)h(z)^2), with h(z)=μ(φ⁻¹{z})/μ(z). The first and second inverse-image masses of v_r are a_r+s and a_r+2s, also across the branching vertex; on a ray both equal c_i. This checks 2-isometry, boundedness and invertibility of C*C (h≥1). A descendant at a fixed depth has a unique ancestral path, so squared amplitudes add, also for countably many rays since their total mass is finite. With A=x+κ, D=A−1, B=A−2, the penultimate step has squared weight B/D and the next splits into xD/A² on the cycle and κD/A² on rays. The cycle continuation contributes factors 1, x/(x+1), x/(x+2) in γ₂,γ₃,γ₄. For κ=2 the last factor is still correct: the second post-return iterate uses the total squared weights at the branch, (x+1)/(x+2), not just its cycle edge. All later ray weights are one. Independent symbolic Schur-complement reproduction (/workspace/review-evidence/replay.py 4, output 4.txt) gives exactly the displayed factorization and the two positive earlier determinants. In particular the only potentially vanishing factor in the stated domain is κ−2. Negative determinant excludes a positive measure of squared radii for this vector and thus excludes subnormality for κ≥3. The order-four sharpness is for this vector's leading/shifted Hankel PSD tests, not all possible operator probes or other moment tests. Vanishing at κ=2 by itself establishes no classification.

## originality

PASS

The weight model and qualitative subnormality machinery are known. The surviving distinct claim is the exact negative penultimate-vector Hankel determinant, with a uniform order-four cutoff and positivity of the two lower-order tests. The closest inspected general criterion is a moment-fit test with κ-dependent range and a prescribed measure, not a sign determination for this fixed low-order matrix. Finding a mismatch with that particular measure does not determine low-order Hankel positivity.

## value

PASS

An explicit scalar obstruction with five directly computable norms avoids a length-dependent full-cycle comparison or constructing a candidate measure. It works even for arbitrarily long circuits and different ray-mass splits, is sharp in moment order for the specified Hankel tests, and distinguishes the two-cycle boundary. The finite cutoff and exact defect are useful independently of the already known qualitative criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
