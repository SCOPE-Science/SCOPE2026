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

Execute `python3 verify_certificate.py` and `python3 verify_metric.py` from this directory. Both use only the Python standard library. The former checks the complete 90-word domain, all nine orbit generators, 72 distinct weighted cliques, all 90 weighted vertex coverages, and the explicit 18-word code. The latter checks independently that all 8,100 ordered metric distances agree between the breadth-first and inversion-count constructions.

## Observed results

`verify_certificate.py`: 90 words, 18 codewords, clique orbit sizes 12/6/12/6/6/6/12/6/6, clique-weight sum 360, minimum coverage numerator 19, exact size bound 18; certificate passed.

`verify_metric.py`: all 8,100 shortest-path distances agreed with the independently computed inversion-count metric; 18-word witness has minimum distance three.

The two finite programs test all instances relevant to the particular theorem, while the incidence-counting inequality in `RESULT.md` supplies the deduction from those exhaustively checked facts. No claim is made for arbitrary lengths or compositions. Independent audit remains unperformed.
