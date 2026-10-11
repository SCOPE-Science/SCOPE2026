---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Mori's Lemma 3.5 makes both \(L_\phi(u)=\sum_j u([\gamma_j])\) and \(Q_\phi(u)=\sum_j u([\gamma_j])^2\) factorization invariants. For the reference Calabi-Yau factorization both equal its length \(m\). Hence for any competing positive factorization, with integer \(x_j=u([\gamma'_j])\), one has \(\sum x_j=\sum x_j^2=m\). Therefore \(\sum x_j(x_j-1)=0\); every integer summand is nonnegative and vanishes only for 0 or 1, proving the zero-one law and exactly \(m\) ones. Mori's rank and Euler-characteristic formulas then give the asserted allowable-filling defect identities.

## originality

FAIL

The zero-one conclusion is an immediate integer identity from the two invariants already published in Mori's Lemma 3.5. Once \(\sum x_j=\sum x_j^2=m\) is known, the entire local defect law follows by the elementary nonnegativity of \(x(x-1)\) on integers; the length and filling excess then use Mori's published formulas. This is therefore covered by direct implication even though Mori states only the minimal-length consequence explicitly.

## value

FAIL

The local interpretation of the excess is tidy, but after Mori's two exact invariants it is a one-line nonnegative-integer observation. It does not isolate an independent mathematical gap: every asserted defect count is mechanically forced by the already published formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
