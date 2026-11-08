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

The theorem covers all smooth plane cubics over \(\mathbb F_5\), not just a sample. The C++ enumerator normalizes the first nonzero of ten coefficients and systematically traverses the remaining base-five digits; this proves the total count \((5^{10}-1)/4=2{,}441{,}406\). It checks all \(31\) rational plane points and exact gradients and tangent-line masks. It derives the precise maximum \(29\) in a superset of geometrically smooth equations, enumerates all maximum forms, and computes both projective orbits using four linear-change generators.

Run `c++ -O3 -std=c++17 verify_cubic_tangents_f5.cpp -o check_cubics && ./check_cubics`; it returns `CUBIC_F5_TANGENT_EXTREMAL_PASS 2441406 1895000 29 186000 93000 93000` and the complete histogram. The separate NumPy/SymPy implementation `python3 verify_independent_f5.py` returns `VECTOR_CUBIC_F5_CENSUS_PASS 2441406 1895000 29 186000 93000 93000` and `REP_SMOOTH_AND_COVER_PASS` for both models. The Python code verifies the unit ideal of the full Jacobian system in each projective affine chart; this is an algebraic-closure smoothness certificate, not just a count of nonsingular rational points.

The two elliptic Weil numerators follow from the verified rational point counts and the genus-one Hasse–Weil formula. The finite enumeration covers every coefficient tuple at the claimed field and degree but makes no claim about other fields or degrees. No independent audit or independent historical-priority certification has been performed.
