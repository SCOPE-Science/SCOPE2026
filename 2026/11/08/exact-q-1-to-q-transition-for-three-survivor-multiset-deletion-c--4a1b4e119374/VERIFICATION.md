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

# Reproduction and scope
Run `python3 checker.py` with Python 3 and only its standard library. The checker validates explicit construction families, their pairwise intersection constraints, lower-endpoint witnesses and independent three-symbol output disjointness for bounded parameters. It also exhausts pairs of bounded-multiplicity vectors for small alphabets. All checks have fixed deterministic bounds and require no internet connection or external data.

The all-alphabet upper bounds are proved symbolically: any two words with a coordinate of multiplicity at least three must choose distinct such coordinates; two different words with every multiplicity at most two necessarily overlap in at least \(2n-2q\) elements. The output-disjointness criterion follows directly from inclusion of a size-three common submultiset. No finite computation is offered as a proof for unbounded \(q\) or \(n\).

The result does not address \(n\le q+1\) beyond the displayed sharp-boundary construction, and does not cover four or more surviving elements. Independent mathematical validation has not been performed.
