---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Use u=(1-cos theta)/2 and normalized spin Wigner densities 3(1-u)^2, 6u(1-u),3u², each integrating to 1. Integrate over u in [0,p]∪[1-q,1]; orthogonal azimuthal orders diagonalize the restriction. For p>=q write d=p-q in [0,h]. Lambda_-1-lambda_+1=3d(1-h)>=0; lambda_0=h²(3-h)/2+3(1-h)d²/2 is strictly increasing for d>0, while lambda_+1 strictly decreases on [0,h]. Their difference equals (3/4)(1-h)(3d²+2d+h²-2h), negative at d0, positive at dh and with one root d*. This gives exact unique (up to reflection) global maximin, multiplicity two and strict improvement. Taylor d*=h-2h²+O(h³) yields q*=h²+O(h³) and 2:1 asymptotics. Independently evaluated h=.1,.5,.9 polynomial eigenvalues and equality at d*, and inspected symbolic/numerical checker; finite tests not needed for global proof.

## originality

PASS

Spin Slepian cap operators and Wigner densities are classical; a sharp fixed-total-area two-opposite-cap maximin allocation with universal strict asymmetry is not implied by the original primary cap theorem or the distinct published pure scalar higher-degree transitions.

## value

PASS

The fixed observation-area budget and smallest concentration eigenvalue are intrinsic to worst-case spin harmonic observability; an exact unique asymmetric optimizer, doubly degenerate bottleneck and factor-two small-area advantage form a motivated geometric design theorem rather than an arbitrary small matrix exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
