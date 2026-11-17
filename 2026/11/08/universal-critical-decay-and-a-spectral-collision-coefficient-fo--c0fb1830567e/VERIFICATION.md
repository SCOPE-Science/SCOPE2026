---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Positive primitive L=(1-delta)I+beta A has Lv=v. The exact product-union bound F(x)=Lx-H(x), H>=0, gives monotonically decreasing Perron mass a=v^T x. Nonzero limiting mass contradicts uniform positivity propagation and strictly positive H. Stable spectral modes are O(a²) and z/a->0. Expanding independent-neighbor product yields collision quadratic H_2 projected to K=delta[1-delta(1+1/rho)/2]sum v_i³; then 1/a increments ->K and t a->1/K. Own independent n=2 edge and n=3 path numerical nonaligned states at t=30000 agree to 0.03%; cannot prove infinite n. Original checker.py and pinned proof inspected.

## originality

PASS

Existing literature establishes same model and threshold but not this equality-case global decay coefficient in inspected accessible results. Collision correction is model-specific, not implied by NIMFA critical formula.

## value

PASS

A model-specific exact critical relaxation coefficient for every finite connected graph identifies epidemic clearance speed at marginal threshold, a meaningful quantity not provided by a binary epidemic threshold or a generic parabolic existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
