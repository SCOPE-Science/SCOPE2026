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

# Reproducing the finite theorem

Dependencies: Python 3.10+ and the `networkx` version range declared in `requirements.txt`. From the directory containing all extracted package files:

```
python -m pip install -r requirements.txt
python verify_katz.py
python verify_trees.py
```

The first script builds exact matching polynomials, exact walk-count centrality numerators and integer coefficient-sign certificates for every edge of all unlabelled trees with \(2\le n\le8\). It checks each chosen rational bound by evaluating the integer determinant polynomial. All nonzero comparison polynomials except two have a fixed sign throughout a rational interval containing the entire admissible Katz range. Both exceptions are verified by exact rational score evaluations with opposite signs, using independently computed integer fourth-walk bounds to certify their attenuation values are admissible. The expected output ends with `EXACT_CERTIFICATE_OK`.

The second script independently enumerates every labelled Prüfer sequence for the same sizes and compares unrooted canonical tree codes. In particular, it checks all \(8^6=262144\) labelled Prüfer sequences against the 23 unlabelled representatives used in the first script. Exhaustiveness depends on the standard Prüfer bijection and the recursive center-based characterization of tree isomorphism, not numerical sampling.

Limitations: These files verify exact finite minimality only up to order eight and the two displayed rational witnesses. They do not establish claims about all higher orders, non-trees, unweighted/directed variants or historical priority. External independent scientific audit has not occurred.
