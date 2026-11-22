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

# Reproduction and limits

Run `python3 verify_double_star.py` and `python3 check_facets.py` using Python 3 with its standard library; compare outputs with the embedded `verify_double_star_output.txt` and `check_facets_output.txt`. The first script generates all proper three-colourings, all vertex subsets, target functions, and exact Boolean trace families for the five indicated double stars. The second enumerates all subsets for 25 double stars and checks every possible facet intersection. Both programs terminate with assertions on any disagreement. They do not extrapolate a finite result to the universal theorem.

The all-parameter scientific proof rests instead on: a four-path obstruction for any proper three-colouring query choice; a fixed target assignment in each of the three hub-selection regimes; a disjoint generating-function partition; and the nerve lemma applied to four simplices with all pairwise and triple intersections nonempty but empty fourfold intersection.

An independent audit has not been performed.
