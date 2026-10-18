---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: With a_i=si+t and gcd(s,t)=1, a_i^k≡t^k mod s. Set h0=r+s−1. Every representation with residue h0 t^k must have number of distinct summands h≡h0 (mod s); h0−s=r−1<r, so at least h0 terms. Positivity and strict growth make M_k=sum_{i=n}^{n+h0−1}a_i^k the smallest such sum, hence M_k−s is bad if positive, yielding N(k)≥M_k−s+1. If M_k−s≤0 the bound is vacuous. Fuller–Nichols Theorem 8 gives N(1)=M_1−s+1 and a_i^k≥a_i; thus endpoint inequality whenever N(k) exists. The argument also works for s=1, t=0 (unit residue ring trivial), and an independent checker validated 9072 parameter tuples; proof is modular, not based on those tests.

## originality

FAIL

FAIL: Fuller–Nichols 2015 Theorem 8 and its proof already use the exact same fixed-residue summand-count obstruction h0=r+s−1 to obtain M_1−s+1. The proposed k-th-power lower bound is the immediate reuse of that argument with a_i replaced by a_i^k while preserving a_i^k≡t^k and monotonicity. No new obstruction, classification or unrelated phenomenon is added. The authors ask stronger adjacent-exponent monotonicity, which this does not approach beyond trivial comparison to k=1. It is a direct routine prior-method implication even if the formula is not printed for all k.

## value

FAIL

FAIL: The natural anti-Waring monotonicity question is meaningful, but this endpoint is a one-paragraph consequence of prior Theorem 8 residue counting and positivity of powers of positive integers. It does not provide the nontrivial k→k+1 step, new threshold existence, or a substantive invariant; its marginal additional inequality has no independent mathematical depth under the shared bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
