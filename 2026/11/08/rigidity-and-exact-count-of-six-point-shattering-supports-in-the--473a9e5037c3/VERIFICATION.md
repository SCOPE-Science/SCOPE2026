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

For six shattered KG(13,3) support triples, singleton hit traces force six distinct private coordinates; the empty trace requires three unused coordinates; hence the residual two-element edges span ≤4 coordinates. With ≤3 residual coordinates, a four-hit trace avoiding two residual edges cannot be realized by a three-point center. With exactly four, any two residual edges must intersect or a four-hit trace is impossible. A pairwise-intersecting 2-edge multigraph spanning four vertices is a common-center star, with arm multiplicities m1+m2+m3=6. Omitting one support from each of two arms forces each remaining arm multiplicity ≥2, giving (2,2,2). Conversely each hit trace uses at most one coordinate per arm and pads with three unused, proving shattering. Orbit-stabilizer gives 13!/288=21,621,600 unordered six-supports and unique orbit. Independently enumerated all 286 three-point centers for canonical support to verify all 64 traces; also recomputed count 13*C(12,3)*C(9,6)*90.

## originality

PASS

The October 25 rank-three Kneser theorem proves the exact VC dimension and minimal ground order n=13 and constructs one doubled-spoke witness. It does not classify all shattered six-sets or count their complete orbit. Exact uniqueness and coefficient 21,621,600 are additional finite structural conclusions, not consequences of dimension six alone.

## value

PASS

The top coefficient and orbit count of the natural VC-shattering polynomial at the first possible ambient order quantify witness rigidity rather than mere existence. An exact symmetry-class classification is a motivated finite invariant, potentially useful for checking extremal constructions and density computations, not an arbitrary list of tiny graph examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
