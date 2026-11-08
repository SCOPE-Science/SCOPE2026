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

# Reproducible verification

The standalone Python 3 verifier requires no third-party packages. Run:

```sh
python3 verify_six_cubic.py CERTIFICATE.json
```

It enumerates all \(262144\) arc subsets of the bidirected prism and checks two independent face conditions: a successor-map no-cycle test and an independent disjoint-set-union acyclicity test. They agree on \(687\) faces, with simplex vector \((18,108,260,240,60)\). The same checks enumerate the previously known bidirected \(K_{3,3}\) comparator without treating it as a new result.

Two deterministic arc-toggle Morse matchings, with ascending and descending arc order, each give \(323\) pairs and leave \(9\), \(26\), \(6\) cells in degrees two, three, four. Each acyclicity test visits all \(687\) faces and all \(2274\) Hasse incidences. Integral cancellations use only signed unit pivots. The surviving degree-three matrix is \(9\times26\) of rank four, with determinant \(-1\) on the maximal-rank minor indexed by zero-based rows \(0,1,4,5\) and columns \(4,9,10,13\); the degree-four matrix is zero. The exact signed matrices for both orders are saved in `CERTIFICATE.json`, and the verifier checks this file against freshly reconstructed data. Direct original-complex mod-two and mod-three boundary calculations also return dimensions \((5,22,6)\) in degrees two, three and four.

`VERIFY_OUTPUT.txt` contains the exact expected successful execution text. The last line is `SIX_VERTEX_CUBIC_MULTIPATH_INTEGRAL_HOMOLOGY_VERIFIED`.

Limitations: these checks concern the precisely specified finite prism only. Integral homology does not by itself establish a homotopy equivalence to a wedge of spheres. The checks do not constitute an independent external audit.
