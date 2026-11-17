---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For y²+y=x⁹+omega over F4 (omega²+omega+1=0), odd sole pole of degree 9 gives genus (9−1)/2=4, affine derivative in y=1 and one rational infinity point. For all x in F64, x⁹ lies in F8, so absolute trace F64/F2 of x⁹=0, while trace of omega=1 (three-fold F4/F2 trace). Therefore no affine F64 points, N3=1, and same trace over F4 gives N1=1; B3=(N3−N1)/3=0. The universal assertion uses Weil N_r >=4^r+1−8*2^r, and all proper divisors d<=r/2 with N_d bounded by 2^r+1+8*2^(r/2), at most r/2 such d. This is <=49r/32 *2^r for r>=4. Since 2^r−8>49r/32 for every r>=4 by induction, N_r exceeds sum proper N_d and thus r B_r>0. Weil equality at r=3 forces all Frobenius eigenvalues cubed equal 8; N1 fixes multiplicities 4,2,2 among 2,2zeta,2zeta², yielding P(T)=(1−2T)^4(1+2T+4T²)^2 and B1=1,B2=4,B3=0,B4=54. Independently recomputed all shown counts; finite tests are not an all-r proof.

## originality

PASS

Best-of-knowledge PASS with specific priority risk: Aubry–Herbaut–Monaldi classify exact closed-point thresholds through genus three and give general estimates, but no explicit genus-four F4 missing-degree-three curve in inspected primary. Lario public genus-four F64/F4 table already lists the matching Weil-polynomial candidate; the polynomial is NOT new. A candidate polynomial alone does not prove the existence of a geometrically integral genus-four curve realizing it, whereas the explicit Artin–Schreier equation plus trace does. No independently identified earlier actual realization of this candidate; an inaccessible thesis or database entry could eliminate historical priority.

## value

PASS

PASS: exact universal closed-point threshold rho(q,g) is the precise natural invariant motivating the Aubry–Herbaut–Monaldi program. The sharp g=4, q=4 bound requires an actual smooth curve with B3=0, not only Weil-admissible coefficients. The theorem supplies an explicit witness and a uniform theorem for every larger degree, with no claim of genus/field-wide classification beyond this parameter pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
