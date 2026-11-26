---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

On each pure-adherence face, the disease-free equilibrium is the only possible sink below the infection threshold; at equality it has a zero eigenvalue, and above it only the unique endemic equilibrium can be a sink. At a mixed disease-free equilibrium the infectious direction separates triangularly and the behavioral eigenvalue is 2 epsilon kappa x(1-x)>0; kappa=0 gives no such root. The same behavioral argument excludes mixed sinks if a=0. Otherwise the endemic branch is an interval since b is nonincreasing. Substituting the endemic prevalence into the payoff cancels the 1-e x factor in the reciprocal term and gives G''=-2 P a^2/[rho(1-a x)^3]<0. The epidemic block A is invertible with positive determinant. Differentiating its equilibrium conditions with respect to x identifies the Schur complement as epsilon x(1-x)G'; hence det J has the sign of G', and the Hurwitz condition in dimension three requires G'<0. Strict concavity admits at most one such zero, including at tangency where det J vanishes. For the rational vector an independently differentiated exact calculation obtains precisely the six listed feasible roots, the two quoted mixed characteristic polynomials and exactly three sinks. At the lower mixed root C3<0 gives a positive real eigenvalue and C3 differs from C1 C2, excluding imaginary-axis roots. At the upper mixed root the exact Hurwitz gap is 2224280063/28224000000. The two other unstable roots have explicit positive real directions within invariant physical faces. The face and mixed sinks persist by their strict inequalities and branch feasibility under sufficiently small admissible perturbation.

## originality

PASS

Kumata–Ito–Yamamichi supply the exact same model, endemic reduction, boundary stability conditions, determinant identity, necessary slope sign and cubic tests, and report coexistence via parameter maps. That is substantial prior coverage. Credit here is restricted to the analytic global three-sink ceiling (in particular the one-mixed-sink bound from concavity) and the exact rational certificate of attainment and persistence. The inspected main text and supplement do not state that sharp uniform theorem. A separate exact calculation confirms that triple coexistence also occurs in the parameter slice they plotted in Fig. S3; no priority is assigned for the qualitative phenomenon or numerical detection of it.

## value

PASS

The same-model literature gives stability conditions for a candidate equilibrium and outcome maps. A sharp uniform ceiling answers a different useful question: no admissible parameter choices can give two Hurwitz mixed outcomes or more than three concurrent sinks, even though a phase diagram at fixed settings can miss regions of three-way coexistence. The rational witness demonstrates attainment with strict margins and open persistence, distinguishing a capacity theorem from a numerical pattern or a routine isolated root check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
