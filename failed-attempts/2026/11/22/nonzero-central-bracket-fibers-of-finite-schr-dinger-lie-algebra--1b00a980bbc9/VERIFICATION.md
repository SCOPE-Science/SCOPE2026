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

In odd characteristic the trace-zero centralizer of any nonzero X in sl₂ is its span: X is nonscalar and its full matrix centralizer is spanned by I and X. Thus a nonzero commuting pair is (αT,βT) in a unique projective direction. The determinant-one change (u,v)↦(t,w) in the proof preserves ω and reduces the vector condition to Tw=0. Each w≠0 gives q^(2n−1) choices of t for any scalar c, whereas w=0 contributes only at c=0. Exactly q+1 projective lines are nilpotent, each with q^n kernel vectors, and each has q²−1 coefficient pairs. Including the purely symplectic case X=Y=0 and the q² free center coordinates gives the stated N_c. The extra zero fiber consists of q^(2n+2) choices per commuting sl₂ pair, and the number of such pairs is q³+(q³−1)q. This checks ordered pairs, all nonzero c and all odd prime powers. Independent replay `python /workspace/branches/independent_math.py bracket` used ranks of adjoint matrices with and without their center row rather than the supplied pair loop. It reproduced the three recorded prime-field checks and found (N_0,N_c)=(52494561,4723920) for q=9,n=1; these are examples, not the general proof.

## originality

FAIL

The centralizer record ending f15d2ef997cd does not print N_c, but its six-type table and proof mechanically imply it. The proof already gives the projected centralizer equations and exactly when the residual linear functional vanishes or has one-dimensional image. For any prescribed c≠0 the nonvanishing cases have the same solution counts as c=0, while vanishing cases give none. The exact formula, its nilpotent split and the zero excess are recoverable from these statements. This is scientific coverage, not an inference of priority or ordering from the common date; the scalar commuting probability alone would not have sufficed.

## value

FAIL

Counting pure central representations is naturally motivated, and the determinant-one proof is a clear alternate derivation. But the exact invariant and its nilpotent grouping are mechanical consequences of the six-type census and its explicit image calculation. Repackaging the same counts without a distinct quantitative or structural increment does not meet the bar for a stand-alone exact invariant; no valuable unaddressed remainder of this specific Finding was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
