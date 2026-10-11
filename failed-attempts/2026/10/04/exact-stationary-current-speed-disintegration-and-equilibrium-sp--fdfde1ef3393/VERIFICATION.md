---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Testing arbitrary antiderivatives of functions of \(y\) and \(z\) gives the two conditional laws exactly. If \(\mathbb E[x^2]=0\), invariance forces \(x=z=0\) and bounded completeness of the remaining scalar equation yields the equilibrium \((0,\alpha/\kappa,0)\). For nontrivial measures, stationarity of \(x^2/2\) and \(z^2/2\) gives the weighted mean formula, while the conditional \(z\)-law gives \(D=\mathbb E[(x-\lambda z)^2]=X_2-\lambda^2\mathbb E[z^2]\). Upper equality forces \(x=\lambda z\), hence constant \(z,x\), and bounded completeness reduces the support to the known equilibrium set. The symbolic verifier reproduces the algebra.

## originality

FAIL

The two headline conditional laws are immediate specializations of the standard stationary-coordinate identity: testing functions of \(y\) gives \(\mathbb E[\dot y\mid y]=0\), and testing functions of \(z\) gives \(\mathbb E[\dot z\mid z]=0\). The weighted-speed defect then follows from stationarity of \(x^2/2\) and \(z^2/2\) plus algebra, while equality rigidity is a short invariant-support calculation. No difficult model-specific lemma is introduced. Exact-database non-detection therefore does not overcome direct coverage by the general generator principle.

## value

FAIL

Although the weighted formulation is physically suggestive, the mathematical content is a sequence of standard one-coordinate stationarity tests and elementary moment substitutions followed by equilibrium algebra. It does not add a nonstandard structural lemma, boundary phenomenon or difficult exact invariant beyond what a specialist can derive mechanically from the published vector field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
