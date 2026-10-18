---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For q=3, n=5, one deletion and SET-valued shadows, independently enumerated all 3^4=81 targets and 3^5=243 candidate centers. The ten alphabet-permutation/reversal orbits give 81 targets of aggregate nonnegative integer dual weight 468. Every center has distinct-descendant weight at most 23 (attained by 126 centers). Hence any cover size is >=ceil(468/23)=21. Expanding seven published prototypes by three common alphabet translates yields exactly 21 distinct centers and partitions all 81 targets once. Reconstructed covering/duality inequalities; complete finite exhaustive proof, not a sampling argument.

## originality

FAIL

FAIL: the published October 4 Resultary RESULT.md already gives EXACTLY K_D^3(5,1)=21 with the IDENTICAL seven prototypes, ten orbit representatives, integer numerators summing 468, shadow bound 23 and corresponding construction. Its full proof directly implies the submitted assertion that all 81 shadows partition: the same 21 centers produce the same distinct deletion descendants. Both the numerical claim and its finite certificate are covered before the pinned October 13 package.

## value

FAIL

FAIL independent value: the natural exact finite covering number is mathematically motivated, but this submission only restates a previously publicly established sharp fact, including the same certificate and codebook. The word "partition" does not produce a new extremizer theorem; it is a property of that identical published construction. Correctness and repeatability cannot recover independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
