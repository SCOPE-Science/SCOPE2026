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
# Verification record

The general result is proved from preservation of the quandle operation, binary linear-map rank counts, quotient-coset occupancy counts, and idempotent projection-kernel decompositions in `RESULT.md`. The checker is supplementary: run `python3 checker.py` from the directory containing these files (standard Python 3, no third-party packages). It directly checks every map of a four-element quandle and all uniquely parametrized homomorphisms for ranks one and two, including direct evaluation of every quandle product and the compositional idempotence condition. The output includes the image-size histograms and retraction spectra and checks their equality with the formulas. The checker also evaluates symbolic totals for rank three. It does not enumerate maps at unbounded rank or establish historical novelty; those scientific judgments rest on the written proof and documented source comparisons. Independent audit has not been performed.
