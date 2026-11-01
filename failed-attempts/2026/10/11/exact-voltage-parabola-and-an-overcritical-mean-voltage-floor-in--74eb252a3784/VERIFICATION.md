---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For compact invariant mu, stationarity of every C1 voltage antiderivative G(v) gives E[G'(v)(I-sin(phi)-gamma*v)]=0 and therefore E[sin(phi)|v]=I-gamma*v. Since the conditional sine mean is in [-1,1], the asserted voltage strip follows. Stationarity of cos(phi) gives E[v sin(phi)]=0, so gamma E[v^2]=I m, and subtracting m^2 gives the exact voltage-variance parabola. With acceleration A=I-sin(phi)-gamma*v, E[A|v]=0 and E[A]=0; thus the L2-orthogonal decomposition sin(phi)=I-gamma*v-A proves covariance and variance-defect formulas and the correlation expression. If m=0, power identity forces v=0 almost surely, whence full invariant support is equilibria. If E[A^2]=0, every orbit on invariant support has v constant; a nonzero constant v would traverse all phases while sin(phi) remains fixed, impossible. For any non-equilibrium invariant state, Var(v)>0 and E[A^2]>0, hence 0<m<I/gamma and -1<Corr(v,sin(phi))<0. For I>1 no equilibria: strict acceleration variance and the sine variance bound imply gamma*I*m>I^2-1, yielding the strict mean floor. Independently, the same floor is obtained from the elementary nonnegative strip product E[(v-a)(b-v)] with a=(I-1)/gamma,b=(I+1)/gamma and E[v^2]=I*m/gamma; equality is excluded by invariant-support rigidity at strip endpoints. All statements include nonergodic probability mixtures and I=1 boundary, and compactness justifies bounded generator tests. The packaged verify.py checks only a few rational algebra instances, not stationarity or universal quantifiers; the independent checker similarly offers bounded corroboration.

## originality

FAIL

A direct 2005 same-equation source predates this record: Coullet, Gilli, Monticelli and Vandenberghe, American Journal of Physics 73 (2005), Eq. (2) theta''+beta theta'+sin(theta)=gamma and Eq. (8) beta integral_0^T(theta'_p)^2 dt=2*pi*gamma for each periodic running orbit. Renaming their beta to damping gamma and their gamma to bias I and dividing by T gives exactly gamma E[v^2]=I E[v]; the stated voltage-variance parabola is its one-line variance rewrite. Their work explicitly recognizes this as the Josephson same-object model. The conditional regression for arbitrary compact invariant measures is the standard generator stationarity identity E[G'(v) dot v]=0 for every voltage test, which needs no system-specific new theorem. Its support strip follows at once from |sin|<=1; the residual variance/covariance formulas are one-step conditional-expectation Pythagoras. The overcritical mean floor is the elementary variance upper bound for a variable restricted to the derived strip, and strictness follows from noninvariance of the two endpoint level sets. Consequently the combined result is a collation of the already published exact power balance with generic invariant-measure calculus and elementary bounded-variable inequalities; no new nonstandard identity or scientifically independent exact invariant survives. Coullet does not itself state the all-invariant-measures conditional regression; this conclusion is an explicit implication using standard measure invariance, not a claim of verbatim publication. Resultary search shows a copy of the assigned record and related different-system analogues but no independent stronger Resultary entry; the decisive source is the 2005 primary paper.

## value

FAIL

Mean junction voltage is a natural and physically important observable, but this particular package does not determine a formerly unknown exact invariant requiring independent mathematical work. The advertised voltage-variance parabola is merely the 2005 known dissipative power balance rewritten as Var(v)=E[v²]−m². The conditional force law is a routine application of stationarity to antiderivatives of arbitrary functions of velocity; sine-current covariance/variance and strict correlation follow by elementary orthogonal-projection algebra. The overcritical lower floor, though a useful consistency inequality, is the standard bound E[(v-a)(b-v)]≥0 for a bounded variable with a,b obtained directly from the conditional sine range and the preexisting moment law; strictness from the simple impossibility of invariant support at its endpoints. No new structural lemma, sharp new parameter constant, complete classification, motivated counterexample to prior theory, or distinct unknown invariant remains after the published result and these standard deductions. Therefore clear exposition and diagnostic convenience do not by themselves establish an independent research-value contribution, despite mathematical correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
