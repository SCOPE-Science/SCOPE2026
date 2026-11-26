---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independent azimuth integration gives the whole law. Fold azimuth by prism symmetry into φ in [0,π/6]; the vertical component of an upper-hemisphere uniform normal is uniform on [0,1]. Set g(c)=c/sqrt(c²+t²). Conditionally, the triangular case has probability 1−g(cos φ). A pentagon occurs precisely when the unscaled threshold lies between cos(π/3+φ) and cos(π/3−φ), so its conditional probability is g(cos(π/3−φ))−g(cos(π/3+φ)). Integrating using sin φ as the variable gives the stated p3 and p5, with p4 the remainder; the generic sign patterns give no other types. The stationary factor decreases strictly from 1 to 3/2−sqrt(3), proving the unique maximum. A bounded independent bisection reproduced t=0.53146955106361, 2t/sqrt(3)=0.61368817674533 and p5=0.38515580567418. Replay: python3 /workspace/review-evidence/5/check_prism.py. The analytic proof, not any grid or Monte Carlo check, covers all t>0. Frozen checker and verification notes were inspected, not executed.

## originality

FAIL

Two distinct indexed results state the same full Haar centroid-fixed law and exactly the same unique positive optimizer. This is established catalogue coverage, not a finding that either November-labelled entry predates the frozen result or establishes historical priority. The different affine Crofton model is not grounds for rejection.

## value

PASS

The mathematical question is worthwhile: the exact family law resolves which generic polygon types occur for every aspect ratio and the derivative establishes a unique design optimum under a precisely specified natural measure. Such a law can also distinguish orientation-Haar from affine stereological sampling. This assessment of the mathematical content does not confer distinct credit for equivalent catalogue coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
