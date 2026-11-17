---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Correct for all integer N>=2 and gamma>0, with unmodified first-order Korobov full-lattice weights against mu(t)=pi|sin(2pi t)|/2. The minimum-norm periodic H1 interpolant has cellwise bubble -4pi^2 gamma ubar b_N; integrating gives w_j=H_j-[4pi^2 gamma B_N/(N(1+pi^2 gamma/(3N^2)))]. The Fourier coefficients of mu and the nonnegative hat Fourier multipliers give H_j>=H_0; direct sine/cotangent integration gives H_0 and B_N. B_N>1/(12N^2), H_0<=1/N establish a positive unique gamma threshold, equal-zero and negative above; Taylor expansion yields Gamma_N=N+pi^2/3+O(N^-1). Independently compared formulas with prior identical theorem; finite direct-solve source verifier was inspected, not mistaken for the infinite proof.

## originality

FAIL

FAIL: full mathematical implication by the already published November 2 Korobov threshold result. Same kernel, density, nodes, gamma convention and exact boundary. Its P_N equals this H_N and its bubble H_N(old)=2 B_N(here), so the earlier minimum weight and threshold are exactly identical for EVERY N and gamma. A second older published theorem evaluates the same positivity frontier and adds the separate constant-function sign transition.

## value

FAIL

FAIL: after exact all-parameter prior coverage, no independent unknown exact invariant, substantial new classification, or motivated additional boundary remains. Correctness, cleaner spline derivation and finite verification do not create scientific value for a fully published formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
