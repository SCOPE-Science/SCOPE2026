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

The programs `verify_tournament_enumeration.cpp` and `verify_tournament_scc.cpp` implement mathematically distinct complete integer calculations; `verify_all.py` compiles and replays them in a temporary local directory. It compares all 32,768 coefficients, verifies the 156-row symmetry orbit certificate and the integer endpoint-kernel sum. The certificate `walsh_coefficients.txt` is a single signed integer for each frequency mask in increasing numerical order. The certificate `tournament_support_orbits.tsv` has one record for each support-graph isomorphism class.

Expected: 22,320 strong tournaments; 8,416 nonzero coefficients; 24,352 zeros; 124 zero graph orbits, of which exactly two are not explained by the stated group actions; exception orbit representatives 958 and 1883 of size 360 each; smallest nonzero Fourier magnitude 16; projection kernel integer absolute sum 1,399,040. Exact Parseval identity: \(\sum_s W(s)^2=32,768\cdot22,320\).

These checks prove the finite claims by executable exhaustive integer enumeration conditional on the displayed short programs and basic elementary recurrence. They do not constitute third-party independent review, generalization to more vertices, or a guarantee that no older result with different terminology exists.
