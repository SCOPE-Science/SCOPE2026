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

A root secant is 1/(r_i+r_j); subtracting two adjacent secants and dividing by t_k-t_i=(r_k-r_i)(r_k+r_i) gives the negative reciprocal of the three pair sums. In the ratio the r_2+r_3 factor cancels. The derivative of the logarithm of a pair sum is -1/(2r_i r_j), so log H has derivative (1/r_1-1/r_4)(1/r_2+1/r_3)/2>0. Both limits follow by taking r_1 to zero at the finite boundary and rescaling all roots by sqrt(-tau) at the other; neither endpoint is allowed. For admissible ratio, prescribed D_123 recovers S>0 and simultaneously matches D_234. The first secant fixes K and the first observation fixes B. Those two observables plus the two curvature coordinates determine the entire data tuple by successive substitution, proving sufficiency including exactly K>0 (or the additional B constraint if imposed). With three observations one can instead vary tau and solve for the other three coefficients continuously, staying in the strict positive region near any interior point. A subset of those observations cannot remove the ambiguity. Independently, the difference between two fits with distinct clocks has second derivative equal to a difference of two inverse powers 3/2 with distinct shifts; their ratio is strictly monotone, so at most one second-derivative zero is possible, contradicting two required by Rolle from four distinct intersections. Finally expanding log pair sums to first order cancels t_2 and t_3 and gives (t_4-t_1)/(2(-tau)); this is structural ill-conditioning, not a noisy-estimation claim. The included script is supplementary; the proof check covers arbitrary real spacings and boundary exclusions.

## originality

PASS

Pass for the sharp admissibility range, exact positive-coefficient inverse and minimality package for the double-offset Philip model at arbitrary known times. Not a claim to novelty of the Philip law, four-parameter fitting, the divided-difference method or general identifiability theory. Strong methodological overlap with a different Green–Ampt observation operator is explicitly credited.

## value

PASS

Clock and baseline calibration are real ambiguities for cumulative readings. Four arbitrary-time observations and a computable exact infeasibility test are more informative than parameter counting or a generic rank test; the positivity check avoids admitting mathematically shaped but physically out-of-scope fits. The remote-onset degeneracy flags an identifiability versus precision distinction. No extrapolation to noisy field data or higher-order infiltration laws is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
