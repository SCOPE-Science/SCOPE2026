---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite reproducibility and proof boundaries

Run `python3 verify.py` using the standard Python 3 library only. It constructs every clique of the inclusive Hamming-distance-two graph, forms simplicial boundaries and obtains exact ranks **over the field with two elements**. It tests all prefixes of each supplied distance-four code, with final reduced third Betti ranks \(0,1,29,129\) for \(n=3,4,5,6\) respectively, and tests the local cubical pivot combinatorics for every deleted codeword and coordinate triple.

The executed output is recorded as `verification_output.txt`. These finite checks are consistency checks. They do not establish integral torsion-freeness, acyclic matchings for all dimensions, or priority; the written integral proof establishes the universal mathematical claim. No independent expert audit has been performed.
