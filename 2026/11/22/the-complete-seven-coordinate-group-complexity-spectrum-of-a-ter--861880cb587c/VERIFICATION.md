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

## Reproduction
Run `python3 verification/verify.py` from the extraction directory with Python 3.10 or later. Only the standard library is used. The expected output is bundled as `verification/output.txt`.

## Checks actually completed
The code reconstructed the nine seven-letter factors from three aligned substitution-block pairs; directly enumerated all 63 unordered proper coordinate bipartitions; generated five transitive subgroup representatives of orders 7, 14, 21, 42 and 168; generated their full conjugacy families of sizes 120, 120, 120, 120 and 30; and evaluated complete group-orbit equivalence on the nine factors. It also checked the Parikh classes and explicit witnesses for all attainable values. The executed code asserted the complete histograms and ended with `PASS`.

## Independent mathematical inputs and limitations
The exhaustive seven-type list of transitive subgroups of the symmetric group on seven letters is a published finite-group classification, not an output inferred from a bounded random search. The script independently tests the stated representatives and every conjugate but does not reprove the classification. The result concerns only factor length seven. No external independent audit was conducted.
