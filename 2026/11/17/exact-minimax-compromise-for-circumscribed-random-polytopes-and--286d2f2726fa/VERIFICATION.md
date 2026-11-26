---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the corrected finding, reconstructed the curvature-risk normalization from Böröczky–Reitzner and the Hölder lower bound with equality at rho proportional to (lambda f^p+(1-lambda)g^p)^(1/p). Strict concavity for unequal laws gives an interior stationary multiplier and equalizes the actual two risks, establishing a matching upper bound within the admissible positive continuous densities. For the oval, r=h+h''=1+t cos(2 theta), dS=r dtheta and curvature=1/r; p=3. Independently set x=t cos(2 theta), U=<r^(2/3)>^(-3), V=<r^(1/3)>^(-3), and factor the half-weight denominator S=(U+V)/2 times (1+Ux/(U+V)). U/(U+V)=1/2+O(t^4). The angular factor (1+x)^(1/3)(1+x/2)^(-2/3)=1-x²/12+x³/12+O(x^4). U-V=-t^4/72+O(t^6), so the slope coefficient is ((3/8)/12-1/72)/3=5/864, with the second derivative -t²/9+O(t^4) from <x²>=t²/2. Even analytic dependence and the simple zero of H'/t² yield the shift 5t²/96+O(t^4). Taylor expansion gives gain 25t^6/165888+O(t^8) in H; cubing multiplies the leading coefficient by three. No finite checker proves the expansion. Replay is the exact calculation in the repair; inspected the frozen verifier and its verification notes without running the script. The claim applies to fixed-density leading errors and sufficiently small nonzero t, not finite N or general shape perturbations.

## originality

PASS

The repaired claim is specifically the sharp sixth-order oval separation, not the two-law radius theorem. It is not supplied by the known separate curvature risks, Hölder/power-mean center identities, or the prior half-weight inequality. The coefficient requires evaluating the particular normalized curvature perturbation beyond its quadratic behavior.

## value

PASS

The published lower bound is expressly not known to be exact from its derivation. The oval perturbation proves a concrete strict failure arbitrarily close to a disk and identifies the first order at which the average benchmark underestimates the optimum. The small size is mathematically informative: quadratic or quartic near-disk comparisons cannot detect it. This justifies the exact positive coefficient and the narrower finding, apart from the known minimax reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
