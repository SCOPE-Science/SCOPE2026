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

# Exact verification

Run `python3 verify.py` from the directory holding the eight files. The verifier rebuilds all three canonical source languages (`aabb`, `aabc`, `abcd`) and each full received-word set, then reconstructs all conflict edges from intersections; it does not read the precomputed incidence certificate as input. It checks the local independence polynomials by two logically separate procedures: integer recursion on the conflict graph using closed-neighborhood deletion, and direct enumeration of each candidate subset, including all size-six subsets for the 24-vertex case. It checks the three optimal codebooks, local output dual weights, uniform exact fractional values for all-distinct permutations, the all-alphabet formulas, and direct global constructions for alphabet sizes 2 through 8. Expected final output line: `VERIFY_OK`.

`local_certificate.json` preserves the full finite canonical instance, explicit output balls and adjacency lists, computed polynomial coefficients, witness codebooks and rational nonzero weights. It is a redundant data certificate, not an appeal to a computational log. A finite enumeration proves the arbitrary-alphabet theorem only because the full mathematically proved multiset decomposition reduces every alphabet to these same three finite graphs; direct alphabet tests alone would not do so. No independent mathematical audit has been performed.
