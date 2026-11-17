---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Lagrange/Sylow subgroup classification yields trivial subgroup, normal rotation C_p, p order-two reflection subgroups and whole group. Their distinct cosets are respectively 2p singleton sets, two partition halves, p² cross-half pairs, and whole group; all p² cross pairs are realized as reflection cosets. Every pair is shattered using a 2-point coset or half plus distinct singletons. Same-half triples fail to realize a two-positive trace; mixed triples realize all 8 traces via global, half, cross, singleton and outside singleton. Four supports with 3 in one half contain an unshattered triple; 2+2 supports cannot realize a 3-positive cross-half trace except via whole group, which selects all four. Thus sharp cubic polynomial. Independent trace enumerations using exactly the concept families (not original verifier) for p=3,5,7 yield [1,6,15,18,0], [1,10,45,100,0], [1,14,91,294,0].

## originality

PASS

PASS best of knowledge: exact prior cyclic all-coset formula and group translate regularity statements do not entail nonabelian prime-dihedral reflection coset trace classification; no earlier exact mixed-triple census found in performed searches. Elementary deductions could exist unindexed, so no assertion of historical certainty.

## value

PASS

The full shattered-support polynomial of all single subgroup cosets in the smallest natural nonabelian family is a precise reusable combinatorial benchmark: cross-rotation/reflection pairs create unexpected VC dimension 3 versus a different cyclic coset system, and an exact triple-orbit characterization identifies every feasible support. Although the subgroup algebra is elementary, the all-size classification is a motivated complete invariant rather than an arbitrary tiny-case calculation or simple renaming of a published table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
