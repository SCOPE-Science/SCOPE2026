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

# Exact reproducibility
Run `python CHECK.py` with Python 3 and `sympy` as stated in `requirements.txt`. The checker uses symbolic exact integers and rational polynomial algebra, not floating-point sampling. It checks the 9-by-10 even-sector matrix rank 9, the listed 9-by-9 determinant 110592, injectivity on the six nontrivial parity sectors, direct harmonicity, all twelve edge restrictions, and a Gröbner basis for the edge-line ideal. The manuscript supplies the proof that these finite checks exhaust every polynomial through total degree six.

Independent mathematical validation has not been performed. No statement concerning all polynomial degrees or entire harmonic functions is certified.
