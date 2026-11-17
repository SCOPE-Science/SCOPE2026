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

# Verification and reproducibility

Run `python3 verify_transfer.py` with Python 3, NetworkX and SymPy available. It generates all 15,625 three-column words, exactly tests the local eight-incidence rule, constructs a 625-state spatial graph, extracts its unique 283-vertex cyclic component, checks the full characteristic-polynomial factorization, tests the integer Perron certificate in `spectral_certificate.json`, and computes first counts from Newton power sums. Standard output is in `verify_transfer.out`. The certificate vector and multiplication comparisons are integer-only once the transfer is built.

Run `g++ -std=c++17 -O3 direct_enumeration.cpp -o direct_enumeration && ./direct_enumeration`. It applies the original four-state update to every one of \(4^{2n}\) initial configurations at each \(n=3,4,5,6\), without referring to the five-history transfer states. Its recorded output is `direct_enumeration.out`, and agrees exactly.

The all-width theorem relies on the explicit finite transfer equivalence and factorization; the bounded direct enumeration is only an independent check. The entropy inequality comes from a positive integer Collatz witness on the primitive SCC, not numerical spectral fitting. The calculation does not check broader cylinders, higher temporal periods, or historical priority.
