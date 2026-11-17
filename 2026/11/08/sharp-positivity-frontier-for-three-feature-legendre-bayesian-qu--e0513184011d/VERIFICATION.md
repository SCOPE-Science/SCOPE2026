---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: for centrally symmetric n-point multiset and positive a0,a1,a2,eta, the even feature z_i=P2(x_i) is orthogonal to odd x. Two Sherman-Morrison inversions show every weight sign is eta-a2 d_i, d_i=z_i sum z_j-sum z_j². For each paired noncentral feature s, s(t-s)=t²/4-(s-t/2)²<=t²/4; the reflected partner contributes zero, and odd n has one central z=-1/2. The resulting maximum is C_n=(n-2)/4 even and max((n-1)/16,(n-6)/4) odd, with explicit realizations incl n=2. PSD matrix order yields Q_eta(1)<=a0 n/(eta+a0 n); C_n/n->1/4 implies universal unmodified bias lower bound a2/(4a0+a2). Independent rational finite grid across n=2..10 confirmed sharp maxima, not substituted for all-n proof.

## originality

PASS

PASS best-of-knowledge: Zhu-Li operator-adapted three-feature quadrature and Karvonen-Kanagawa-Sarkka kernel-weight positivity provide model/background, but not a worst-case all-symmetric-design sharp nugget with parity and quantitative mass-bias obstruction. Hayakawa imposes a positive-simplex constraint rather than the unmodified ridge posterior mean. Motivating 2026 Zhu-Li full text could not be accessed (abstract only); its presence alone is not decisive prior coverage. Record historical risk.

## value

PASS

PASS: deciding the exact ridge regularization required to prevent negative quadrature weights for every symmetric sampling design is a natural stability/fidelity tradeoff. The parity switch and unavoidable constant-integrand bias quantify a genuine obstruction; a complete family classification, not merely a two-node exercise or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
