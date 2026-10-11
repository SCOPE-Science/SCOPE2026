---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Zuo's norm-comparison inequality gives \(C_P(X)\le d_{\mathrm{BM}}(X,\ell_2^2)^2\), and Zuo's Example 2.10 gives \(C_P(X)=1+1/\sqrt5\). For \(|(x,y)|_*^2=5x^2+y^2\), the squared quotient is \((5+2t+t^2)/(4(5+t^2))\) with \(t=|y|/|x|\). Its derivative has the sign of \(5-t^2\), so its minimum is \(1/4\) at the axis limits and its maximum is \((5+\sqrt5)/20\) at \(t=\sqrt5\). This gives \(d_{\mathrm{BM}}^2\le1+1/\sqrt5\), hence equality.

## originality

FAIL

A separate published SCOPE result already proves the exact same Banach--Mazur distance \(d_{\mathrm{BM}}(\mathrm{ces}_2^{(2)},\ell_2^2)=\sqrt{1+1/\sqrt5}\) and supplies an optimal Euclidean ellipsoid. Zuo's 2012 primary article already proves \(C_P(\mathrm{ces}_2^{(2)})=1+1/\sqrt5\). The assigned equality \(C_P=d_{\mathrm{BM}}^2\) is therefore the direct conjunction of two already-published exact values.

## value

FAIL

The equality is elegant, but after the exact Banach--Mazur distance and exact Ptolemy constant have both been published for the same plane, the final statement is a one-line corollary rather than an independent gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
