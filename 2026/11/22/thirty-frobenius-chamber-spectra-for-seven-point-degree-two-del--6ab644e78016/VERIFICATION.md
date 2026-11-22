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

# Verification

The proof establishes the geometry and rational descent first; the finite computation concerns the complete 56-curve configuration, not a random sample. In one directory with `CHAMBER_SPECTRA.json`, execute:

```sh
python3 verify_chamber_cycles.py
python3 verify_orbit_blocks.py
```

The first enumerates exactly 33,645 pairwise-disjoint supports and the complete 30-case Frobenius permutation. The second independently enumerates compatible full curve-orbit blocks and uses exact Möbius inversion on all powers, never constructing the list of 33,645 geometric supports. For each of the 15 integer partitions of 7 and both quadratic-twist choices, the exact computed spectrum, fixed support count and total cycle weight are checked against `CHAMBER_SPECTRA.json`. Expected final markers are `DIRECT_33645_SUPPORT_PERMUTATION_30_CASES_OK` and `INDEPENDENT_ORBIT_BLOCK_AND_MOBIUS_30_CASES_OK`.

These calculations do not prove that all 15 seven-point partition types exist over every small field, do not classify other Weyl actions, and do not independently establish historical priority. The 56-curve classification, chamber-support equivalence and rational-descent proof are essential mathematical inputs. Independent review is not yet performed.
