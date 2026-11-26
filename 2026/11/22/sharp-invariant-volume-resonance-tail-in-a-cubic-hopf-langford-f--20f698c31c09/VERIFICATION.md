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

In polar variables q=u²+v², the reduced motion is canonical for H/2 with z'=A−q, q'=(2z−1)q and θ'=β. H is conserved and divergence vanishes in physical coordinates. Each positive regular level inside Ω is a compact oval times the angle circle; the only critical level there is the central circle at H=1/16. This gives both-time invariance and the winding classification, with the rational tori a countable union of null surfaces. The two z branches give P=2∫dz/√(A²−h); factoring around z=1/2 gives 4 K(m)/√(1/4+√h), with strict decrease and limit 2π√2 at the center. DLMF §19.12.1 in modulus convention gives K(m)=log(4/√(1−m))+o(1) in the record's parameter convention; 1−m∼8√h and the prefactor is 8+O(√h), so P=2 log(4/h)+o(1), with the correct additive constant. The physical Jacobian after angle integration is π dq dz and V(0)=π/3. Independently, layer-cake integration of A−√((A²−h)_+) shows V(0)−V(h)=(π/2)∫_0^h P(s)ds, without differentiating a moving endpoint. Thus the normalized lost volume is 3h(log(4/h)+1)+o(h). Inverting the monotone period gives h_R=4e^(−πR/β)(1+o(1)), establishing the displayed tail constant 12π/β. Replay: RESULT.md §§Proof, lines 33–80; check.py was inspected only and finite checks do not establish the tail.

## originality

PASS

The supported distinct result is the sharp pushforward of ordinary 3D physical volume on the specified bounded invariant lobe, not its first integral, closed invariant tori, period quadrature or resonance geometry in isolation. A very close generalized-flow paper remains a material full-text access risk; the checked statements and distinct exact pushforwards do not demonstrate coverage of this volume law.

## value

PASS

Uniform Euclidean volume is a distinguished invariant sampling law because the original flow is divergence-free on a finite invariant region. The exact critical rate and coefficient quantify how rare long reduced periods are in that measure, where uniformly sampling h would give a different prefactor. This is a useful specific volume-statistical invariant, not a purported positive-volume set of resonant tori or novelty of integrability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
