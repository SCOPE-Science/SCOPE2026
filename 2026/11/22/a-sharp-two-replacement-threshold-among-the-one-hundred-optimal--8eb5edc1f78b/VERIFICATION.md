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

# Executable finite verification

The two standalone sources `verify_gp.cpp` and `verify_incidence.py` were run with ordinary command-line tools and require no external input file or specialized mathematical package:

```sh
c++ -O2 -std=c++17 -Wall -Wextra verify_gp.cpp -o verify_gp
./verify_gp
python3 verify_incidence.py
```

They produced:

```
GP(10,3): ordinary_6=130 semitotal_6=100 one_jump_edges=0 two_jump_edges=570 diameter=4 degree_hist=8:30,12:10,13:60 VERIFY_OK
Incidence H(5,2): ordinary_6=130 semitotal_6=100 one_jump_edges=0 two_jump_edges=570 diameter=4 orbits=10,30,60 VERIFY_OK
```

Both independently construct the graph and evaluate the complete semitotal predicate on all six-sets. The Petersen implementation visits all \(2^{20}\) bit masks before retaining size-six candidates; the subset-incidence implementation visits exactly \(\binom{20}{6}=38{,}760\) six-sets. Both also independently rule out all dominating five-subsets, thereby excluding every smaller semitotal configuration without external premises. The second source additionally checks a 20-vertex isomorphism between these two representations. Both independently test every unordered pair of the 100 optima, verify no one-replacement neighbors, and calculate all 100 distance vectors in the two-replacement graph. The first additionally checks the complete orbit-specific distance-shell possibilities. The second independently constructs all 240 symmetry actions and obtains exactly three orbits of sizes 10, 30 and 60.

The external semitotal degree inequality is cited in `RESULT.md`; these finite programs do not purport to prove that separate published theorem. The checked finite census establishes the exact result on the specified graph, not an unknown general theorem or research priority. No independent external audit was carried out.
