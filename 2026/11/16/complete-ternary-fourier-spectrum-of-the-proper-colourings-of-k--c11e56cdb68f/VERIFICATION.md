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

# Reproduction and verification

Run `python3 verify.py` from the package directory. This standalone checker uses only Python 3 standard libraries, sums all proper three-colourings as exact counts of the three character phases, compares the direct values with the theorem, and checks complete signed eigenvalue multiplicity distributions for lengths one through six. The original execution produced:

`TERNARY_BICLIQUE_FOURIER_EXACT_PASS exhaustive_frequencies=9828 random_tests=320`

The same file also checks reproducible selected frequencies at lengths seven and eight, and all predicted multiplicity totals and zero counts at lengths twelve and eighteen. The nonbalanced frequencies are set to zero by the proved colour-translation symmetry; the checker directly enumerates every balanced frequency for lengths one through six. The general formula is proved by three-colour character orthogonality and direct counting, not inferred from bounded tests. The full Babson–Beck source was inaccessible, so no global novelty certification is claimed. Independent mathematical assessment has not been performed.
