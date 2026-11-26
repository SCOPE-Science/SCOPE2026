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

The substitution y=e^t−1 and Stirling expansion are formally coefficientwise finite and give integral coefficients. Modulo 2^r, terms of factorial index at least 2r vanish, and for n≥r all even bases of the fixed finite inclusion–exclusion sum vanish. The modulo-32 cycle 31,17,31,1 repeats on n≥5 via the eighth powers of the odd bases; independently multiplying the truncated exponential series in integer derivative coordinates reproduced this cycle and passed 459 half-shift tests. For odd j, writing j²=1+8u gives ν₂(binomial(2^{s−1},k)·8^k)≥s−1−ν₂(k)+3k≥s+4 for k≥2 when the binomial is nonzero. This proves j^{2^s}−1≡2^{s−1}(j²−1) modulo 2^{s+4}, including s=1. Applied to the fixed odd bases, this lifts the base defect for every n≥r and r=s+4. Parity is preserved by the half-shift, so applying it twice gives a period; its half fails on all sufficiently large even n. The least eventual period divides any period by Euclidean differences. Reduction of the base cycle gives the parity alternation modulo 4, 8 and 16 and the constant tail modulo 2.

## originality

FAIL

Distinct prior Resultary records already cover the complete least-period law and both branches of the half-period defect, including the same onset n≥r. This is affirmative coverage, not an inference from an unsuccessful search.

## value

FAIL

The sharp period and parity defect are natural arithmetic invariants, but both are already recorded with the same quantifiers. No additional unknown invariant, stronger onset, or independently useful structural result is asserted; the proof and checks recompute the covered theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
