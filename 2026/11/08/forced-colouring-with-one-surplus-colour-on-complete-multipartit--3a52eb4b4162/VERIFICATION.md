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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 standard library. It separately implements Farr's local unique-missing-colour forcing rule on explicitly generated labelled complete multipartite graphs and the proposed coefficient formula. The program exhaustively enumerates every partial colouring (including blanks) for fourteen part-size profiles and compares the exact entire coefficient vectors. The test set contains three, four and five partite sets, all-singleton profiles, mixed part sizes, and small equal and unequal nonsingleton classes.

The final line of the successful replay is `ALL_PROFILES_OK 14`. In particular, the four-colour polynomial for \(K_{2,2,2}\) has coefficient vector \((288,432,288,96)\) in degrees \(3,4,5,6\). The separately implemented definition-based enumeration and symbolic coefficient calculation agree on the checked finite cases.

The finite enumeration is not a proof for arbitrarily large graphs and it is not independent mathematical certification. The unrestricted polynomial and minimum-domain formulas depend on the proof's capacity dichotomy, seeded-part necessity and sufficiency, and disjoint counting arguments in `RESULT.md`. No independent audit has been performed.
