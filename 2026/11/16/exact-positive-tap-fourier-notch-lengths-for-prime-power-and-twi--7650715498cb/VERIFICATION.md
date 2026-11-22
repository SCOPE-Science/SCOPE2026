---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The all-primitive-root zero set is precisely Φ_N divisibility. Splitting F(X) by exponent modulo q=p^(k-1), or q=2^(s-1)p^(k-1), and comparing last residue q-1 forces degree ≥pq−1 or ≥(2p−1)q−1. In the mixed case a strictly positive Φ_(2p) multiple below degree 2p−2 is impossible: reduce modulo Y^p+1 and compare the same-sign consecutive top coefficients b_(p−2), b_(p−1) with the alternating signs of Φ_(2p). H_p=(1+Y^p)Σ_(0..p−2)Y^j+(1/2)Y^(p−1)Φ_(2p) fills every coefficient positively; substitution X^q, residue filling and convolution with 1+X+...+X^m give all longer degrees and integral coefficients after scaling. Independently inspected verify.py and reproduced exact SymPy witness checks for sample N; these are corroboration only. N=2 and p=3 boundary obey formulas.

## originality

PASS

Best-of-knowledge: substantive comparison of the exact claim and implications with closest published scientific results, including generalizations and potential near-equivalences; residual priority risks explicitly retained.

## value

PASS

Strictly positive consecutive impulse responses are a natural finite Fourier design constraint not captured by sparse nonnegative cyclotomic multiples. The exact minimal hardware length, for two infinite arithmetic period families, is a nontrivial constructive threshold with potentially reusable residue-divisibility obstruction; this is more than relabeling a known minimal support degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
