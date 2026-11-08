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

# Verification and boundaries

The proof in RESULT.md is deductive and holds for all stated integer parameters. Its crucial checkpoints are: the three-layer domination inequality; the total window-excess bound of at most two; the exclusion of full occupied layers at equality; the characterization of empty/monochromatic runs; the cyclic composition count; and the chromatic-polynomial factor.

Run `python3 scripts/verify.py` with Python 3 and no non-standard packages. The checker builds the direct-product graph from its adjacency definition, then tests **every vertex subset of size at most the claimed minimum** in the following cases:

- \((n,q)=(6,3),(7,3),(8,3),(9,3),(6,4),(7,4),(6,5)\).

The total number of distinct subsets inspected in those seven cases is \(786909\). The number of independent dominating sets below the candidate minimum is zero in each case. The enumerated numbers at the candidate minimum are, in order, \(18,42,72,18,36,84,60\), matching the closed formula. A separate loop evaluates the formula for \(162\) other integer pairs, which is an arithmetic consistency check, not another independent mathematical verification.

Expected terminal line starts `VERIFY_OK raw_graph_profiles` and ends `literal_independent_dominating_test=PASS minimum_multiplicities=PASS`.

Finite enumeration is not a proof for arbitrary parameter size. Only the proof's Steps 1–5 establish the unrestricted theorem. The verifier does not assess originality, scientific importance, or publication priority. Independent mathematical audit has not been performed.
