---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The explicit 11-vertex standard Mycielskian C5 has 20 edges. Direct component-size enumeration across all 2^11 masks gives 102 nonempty Ind1 faces and 312 nonempty Ind2 faces. The fetched certificate proof/relative_collapse.json contains 105 lower/upper face pairs, and proof/verify_groetzsch.py checks each lower face has exactly one remaining strict coface (the upper), with one more vertex, until precisely Ind1 remains. The fetched 50-edge acyclic matching on Ind1 has one critical 0-cell and one critical 2-cell; the general Mycielskian suspension and Ind(C5)≃S1 independently support Ind1≃S2. The independent verifier for the broader n=3..6 result also reconstructed 105 genuine pairs at n=5. This proves a finite simple-homotopy result, not an all-n theorem.

## originality

FAIL

The assigned same-commit record 2026/11/01/a-sharp-inclusion-collapse-boundary-in-mycielski-cycle-higher-in--ce8cb3bb3a1b states the same canonical collapse for n=5 with exactly 105 elementary pairs and deduces Ind2(μ(C5))≃S2, as one case of a strictly stronger theorem covering n=3,4,5 and n=6 relative homology. The entire mathematical claim of this record is already logically implied by that full statement; distinct certificate encodings do not restore novelty. This is decisive within the frozen assignment, independently of bibliographic uncertainty.

## value

PASS

Stability of the ordinary independence complex under the first higher-independence cutoff is a motivated topological invariant and an explicit inclusion-level simple-homotopy witness. Its value as a mathematical fact survives the originality failure, but separate publication is redundant with the encompassing companion result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
