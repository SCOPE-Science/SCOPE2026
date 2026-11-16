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

The integer determinant certificate has been replayed in exact modular arithmetic using the displayed finite prime \(1000003\). A second, combinatorially independent enumeration verifies the ranks modulo \(1000033\). Both programs use the Python standard library and the `CERTIFICATE.json` included here.

Run from the extracted directory:

```sh
python3 verify_insertions.py
python3 verify_splits.py
```

Observed output:

```text
PASS: 105 distinct trees; degree-one rank 31; degree-two rank 105.
PASS: modular determinants 243 582830 and explicit mixture separation.
PASS: 105 compatible full split systems; rank 31 and rank 105 modulo 1000033
```

The first method inserts leaves at edges and tests path disjointness. The second constructs maximal compatible split systems and tests separation by a split. Neither calls the other. The verified incidence-array SHA-256 is `77b2724baaf35916196e7a8a2ec528d9b5b11de538573cb959c638629d7f8cd4`; it denotes the row-major binary incidence array sorted lexicographically by its rows. Both computations agree on all \(105\) rows and \(45\) queries.

This is a finite exhaustive certificate, not an inference from sampled cases. No calculations for larger leaf counts, numerical conditioning analysis, or external independent audit are supplied.
