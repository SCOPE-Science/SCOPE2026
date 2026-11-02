---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed the exact system xdot=a-(b+1)x+x²y, ydot=bx-x²y for a,b>0. S=x+y obeys Sdot=a-x. Invariance applied to all smooth antiderivatives H(S) yields E[x|S]=a and Cov(x,S)=0. Consequently Cov(x,y)=-Var(x), Var(y)=Var(S)+Var(x), Var(x)=E[Sdot²]. Antiderivative tests K(x) yield E[y|x]=F(x)=((b+1)x-a)/x². The pointwise residual y-F=xdot/x² and conditional orthogonality yield Var(y)-Var(F)=E[(xdot/x²)²]. Compact positive support guarantees bounded x^{-1} and positive y_min, so F>=y_min on the x-support and x>a/(b+1). Zero Var(x) or Var(S) together with invariance forces x=a and y=b/a, giving all strict non-equilibrium cases. Independent SymPy symbolic cancellation checks for Sdot, nullcline residual and equilibrium passed. The Git tree SHA reconstructed exactly from the eight observed Git blob identities; packaged VERIFY_OK was not taken as a proof of analytic steps.

## originality

FAIL

Direct prior mathematical coverage by the October 4 exact Brusselator stationary slice-calibration theorem, not merely the same title or analogous parameters. It proves the entire total-concentration law, autocovariance law, variance/speed identity and rigidity; the extra x-fiber regression, speed residual and x-support threshold are elementary consequences of the standard generator invariance equation for this already-published polynomial flow. The submitted final headline therefore lacks a surviving original mathematical assertion. This is a scientific implication judgment; VPN failure for a separate 1978 source is not treated as evidence of nonnovelty.

## value

FAIL

The Brusselator and its total concentration and nullcline are natural mathematical objects, and the original formulas are correct. But the most meaningful purported invariant—universal negative covariance and strict variance ordering for all stationary states—already appears, with the full conditional and speed identity, in the published October 4 same mathematical model theorem. The remaining x-fiber calibration is directly E[x-dot|x]=0 and its square-integrable residual is the standard law of total variance. The x lower barrier is immediate from positivity of that regression (and from elementary vector-field crossing). No independently unknown or mathematically motivated invariant/classification remains after removing covered or routine deductions. Value is not denied merely because the proof is short; it is denied because the precise finished mathematical content is already covered plus routine consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
