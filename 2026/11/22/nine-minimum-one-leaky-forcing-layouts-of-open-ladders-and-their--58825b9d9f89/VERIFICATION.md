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

# Reproducible scientific checks
Compile the standalone finite checker in `verify.cpp` with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify`, then run `./verify`.

For every length 2 through 16, the checker builds the labelled ladder directly from graph edges and tests every possible nonforcing leaked vertex. It enumerates all candidate initial sets at successive cardinalities through four. For lengths five through sixteen it compares the successful minimum sets with the explicit nine-family classification, and computes the 12 legal one-token exchanges and absence of optimum-preserving adjacent token slides. The observed final line is `VERIFY_OK`.

The proof of the unbounded family is supplied in RESULT.md. Finite enumeration does not establish claims for lengths beyond sixteen, and this verification has not been independently audited.
