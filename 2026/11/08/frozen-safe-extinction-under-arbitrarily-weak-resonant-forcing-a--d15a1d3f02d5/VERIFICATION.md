---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The assumptions define a stable-focus coexistence equilibrium J=[[-alpha,-a n],[a b p,0]] with discriminant alpha^2<4d and n=m/(ab), p=(r/a)(1-n/K), d=rm(1-n/K). Exponential stability plus variation-of-constants establishes uniformly in time an O(epsilon^2) remainder for all bounded forcing inputs. For each frozen eta the first-order prey step response is epsilon s c exp(-alpha t/2) sin(qt)/q; |sin qt|<=qt bounds its maximum by 2 epsilon s c/(e alpha). Predator L1 convolution bound is epsilon s kappa coth(pi alpha/(4q)); strict u,v inequalities keep all frozen trajectories safely in coexistence for small epsilon. Periodic sine forcing at sqrt(d) has asymptotic prey amplitude epsilon s c/alpha, strictly exceeding the moving prey-barrier u epsilon, while its predator remains above the moving predator barrier. Crossing f1 into N<Na with P>Pa has an admissible Filippov f2 continuation with negative prey drift; subsequent prey extinction and eventually predator decay follow by differential inequalities. Exact step amplitude tends to ratio 2/e as q/alpha tends to 0, establishing sharpness of the universal sufficient comparison (not the full nonlinear tipping threshold).

## originality

PASS

PASS qualified: Gao–Poloni–Wang–Lewis analyze the same threshold predator–prey model and frequency-induced tipping at fixed thresholds/amplitudes, and contemporaneous published findings calculate first-harmonic resonance or joint-threshold accessibility, but none inspected proves the co-moving O(epsilon) barrier with *all frozen rates safe* and *every sufficiently weak resonant periodic amplitude admitting extinction* nor the sharp universal 2/e step/sinusoid gap. Related works are credited; no absolute priority is asserted.

## value

PASS

PASS: a model-specific counterexample to frozen-parameter safety inference is conceptually meaningful, especially the explicit nonempty universal corridor and rigorous Filippov extinction despite asymptotically vanishing periodic forcing. The result separates oscillatory resonance from every constant-rate response using a sharp universal coefficient; it does not exaggerate into a full tipping phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
