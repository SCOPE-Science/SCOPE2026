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

Write A=D⊕J with J²=0 and G=(k×)^V⋉(1+J). Dual coordinates are vertex values α and arrow values w. For support S={a:w_a≠0}, unipotent conjugation translates α by the incidence image L_S, rank r(S)=n−c(S) over every finite field (forest leaf-elimination proof, loops zero). The diagonal torus scales nonzero arrows by endpoint ratios, with orbit cardinality (q−1)^r(S) and (q−1)^(|S|−r(S)) torus orbits at each support. The α-coset space has q^(n−r(S)) classes; hence each combined coadjoint orbit has cardinality [q(q−1)]^r(S), and number q^(n−r(S))(q−1)^(|S|−r(S)). Summing supports gives q^c z^(n−c) T(1+q/z,q), and weighted mass equals q^(n+|E|). Independently checked small multigraph rank/mass, including loops, parallel, disconnected and q=4.

## originality

PASS

The 2026/10/12 algebra-element inner-conjugacy class theorem already proves the scalar total q^c T(q+1,q) for primal adjoint action. That scalar equality also follows from Burnside (equal dimensions of fixed spaces for a linear action and its dual); it is NOT new. Earlier 2026/10/26 unit-group conjugacy-spectrum theorem treats orbits on G itself, not dual A*. The new surviving claim is the full coadjoint orbit-size histogram; it is mathematically different from primal sizes: on the two-vertex single-arrow quiver over q=3, primal algebra conjugacy sizes are 1,2,3 while coadjoint sizes include 6. Full rank support weights are not inferable from the scalar total, despite matching Tutte evaluations. Strong qualified pass only for entire spectrum.

## value

PASS

This exact orbit-size spectrum is a natural full classification of a torus-by-radical action, making orientation-independent matroid structure visible at every orbit size (rather than just total orbit number). Loops, parallel arrows, and all characteristics are uniformly included; this is a meaningful global structural invariant, even though scalar total is prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
