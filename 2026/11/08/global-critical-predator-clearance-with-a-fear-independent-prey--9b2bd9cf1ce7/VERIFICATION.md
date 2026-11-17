---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the exact three-compartment Mondal–Sarkar–Sk ODE with X(0)>0, S(0)+I(0)>0, strictly positive fear K, d4>d3 and c1 f(L)=d3, summing predator equations cancels transmission, treatment and recovery: Pdot=[c1 f(X)-d3]S-(d4-d3)I. Logistic prey comparison makes the positive part of the predator growth integrable, so P has a finite limit; if positive, positive fear bounds prey strictly below L, forcing P to decay exponentially, a contradiction. Hence P->0, X->L. The infected fraction I/P decays exponentially, and stable prey-mode slaving yields (X-L)/P->-B/(r-d1), where B=rLK+f(L). Thus tS->(r-d1)/[c1 fprime(L) B] and t(L-X)->1/[c1 fprime(L)], independent of K. Independent exact rational coefficients for K=1/2 and 1/4 yield tS=1/2 and 3/5, respectively, but both prey deficits 3/2. The full global result rests on the comparison and damping proof, not the finite checks.

## originality

PASS

The primary Scientific Reports paper introduces the same fear/refuge infected-predator ODE and strict predator-free stability inequalities, but its equilibrium and epidemiological R0 analysis do not supply nonlinear global equality-case clearance rates. Similar Resultary two-compartment fear/refuge results have different differential equations and no infected fraction with treatment cancellation. The related two-path infection paper is a genuine incomplete historical access risk.

## value

PASS

The actual predator invasion equality is an ecologically natural nonhyperbolic regime not decided by strict local stability. The exact globally attracting fate, explicit 1/t predator amplitude and cancellation of fear from prey deficit are structural predictions for the full infection/treatment system; they are not a routine substitution from a simpler two-dimensional predator model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
