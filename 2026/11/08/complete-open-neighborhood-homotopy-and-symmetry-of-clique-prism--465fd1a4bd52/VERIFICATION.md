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
# Reproducibility

Run `python3 verify_clique_prism.py` with the Python 3 standard library. The script regenerates every open-neighborhood simplex as a subset of a stated facet; it independently computes mod-two boundary ranks and face vectors and checks the precise intersection with the crown graph for each \(n=4,5,6,7,8\). It also checks that both side complexes have the claimed boundary-plus-private-cone face sets.

For \(n=5,6\), it enumerates every \(S_n\times C_2\) automorphism, computes the signed simplicial Lefschetz number directly, and verifies agreement with the characters proved using integral Mayer–Vietoris. The generated output is preserved in `verification_output.txt` and terminates with `ALL_CHECKS_PASS`.

The executable finite range is not a proof for all integers. The proof for every \(n\ge4\) is the explicit cover, crown intersection, null maps and homotopy-pushout argument in RESULT.md. Its integral module assertion is separately justified by naturality of Mayer–Vietoris, including the exchange sign. No independent external audit has been performed.
