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

# Reproduction notes

The accompanying `CHECK.py` uses only the standard Python library. Execute `python3 CHECK.py`; it recomputes the first three coefficients of the exact leverage kernel's analytic \(q=d^2\) series using rational power-series arithmetic at eight distinct rational evaluation points. It also checks an exact polynomial quotient identity, rational brackets on the unique positive transition root, and 96 independently solved three-dimensional real Gram systems at a range of positive frequency gaps and evaluation sites.

The exact rational tests are finite cross-checks of the symbolic coefficient computation. They do **not** establish the universal coefficient polynomials at every real point, the absence of all other roots, or uniqueness of the emerging local maximum; these are established analytically in `RESULT.md` through series algebra, elementary real inequalities, and an implicit-function argument. No global frequency optimization, formal proof assistant, or independent mathematical validation is asserted.
