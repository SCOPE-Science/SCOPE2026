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
# Verification record

Two independently written exhaustive programs were executed against the exact source files in this package before release. Running `g++ -O3 -std=c++17 verify.cpp -o verify_cpp && ./verify_cpp` printed `TERNARY_HAMMING_MIS_CPP_PASS`. Running `python3 verify.py` printed `TERNARY_HAMMING_MIS_SHATTER_PASS`. Each asserts 11776 independent subsets, 390 inclusion-maximal independent sets (54/324/12 by sizes 5/7/9), the coefficients (1,27,270,1278,2862,2322) and facet multiplicities (36 of size three, 2322 of size five). The Python program also verifies all small facets are coordinate transversals and all five-facet orbits have sizes 54,324,648,648,648.

The finite search is exhaustive, with an explicit increasing-order independent-set enumeration and exact Boolean trace enumeration. No timeouts, random sampling, unverified external dataset or probabilistic inference is used. It certifies the stated finite case only, and it does not constitute independent peer review or historical uniqueness certification.
