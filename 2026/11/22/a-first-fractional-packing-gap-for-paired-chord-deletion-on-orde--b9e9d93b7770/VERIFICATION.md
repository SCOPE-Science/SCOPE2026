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

The standalone `verify.py` program re-generates the full finite matching families, recomputes each deletion outcome in two independent ways, checks the subset-dynamic-program and clique-enumeration optima, and validates the explicit integral half-unit primal and dual certificates in `CERTIFICATES.json`.

Run `python3 verify.py` beside `CERTIFICATES.json`; successful execution ends in `VERIFY_OK` and reports all four cases. No random testing, floating-point tolerance or assumption about a larger matching order enters the finite proof. The four-pair input consists of all 105 matchings and 15 possible received types. Independent external validation has not been performed; historical novelty remains subject to the inaccessible full text described in the scientific review.
