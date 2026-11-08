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

# Verification method and limits

Run `python3 split_threshold_verify.py`; no third-party packages or input files are needed. The checker enumerates all split graph presentations for each order zero through seven using every possible clique/independent-set split and every cross-edge bit matrix. It applies the same refinement colour dictionary to all presentations at each round and tests full colour-preserving graph isomorphisms within each resulting colour-histogram group. The exact observed table is:

| Vertices | Labelled-partition presentations | Distinct refinement groups | Nonisomorphic pair within a group |
|---|---:|---:|---|
| 0 | 1 | 1 | no |
| 1 | 2 | 1 | no |
| 2 | 4 | 2 | no |
| 3 | 10 | 4 | no |
| 4 | 34 | 9 | no |
| 5 | 162 | 21 | no |
| 6 | 1090 | 56 | no |
| 7 | 10370 | 164 | no |

The computed isomorphism-class counts for positive sizes match Royle, Table 1 (2000). The witness constructor confirms a shared two-class refinement histogram but rejects every colour-preserving bijection at order eight. The checker also tests connected universal-join witnesses through order twelve. A terminal `result: PASS` was observed on the actual package source.

The published structural lemma connecting counting two-variable logic to colour refinement is used to pass from equal logical theories to equal colour histograms. The *finite* cutoff is checked exhaustively. The claimed extension to every higher order comes from the proof of equitable partition preservation under a universal join, not from the four finite extension checks. There is no independent audit.
