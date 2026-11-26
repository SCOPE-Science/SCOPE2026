---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On a unit Zak cell the transform of the window is e^(-lambda x) times the finite geometric series in r exp(-2 pi i xi), nonzero and bounded away from zero on the cell. Multiplication on the image of the Fourier monomial basis gives a Riesz basis and makes the squared essential extrema the optimal bounds; the time factor contributes r^2 to the lower bound and 1 to the upper. The triangle inequality maximizes the geometric series at aligned phases. For the minimum, at a given Chebyshev value the leftmost preimage strictly maximizes the positive denominator. On that first arc set x=-cos u; T'_L equals L times 1+2 sum_{j=1}^{(L-1)/2} cos(2ju), whose derivative in u is strictly negative for 0<u<pi/L. This proves strict increase of E and rules out competing interior or exterior minima, including at the threshold. The left endpoint factor vanishes exactly when cosh(L lambda/2)/cosh(lambda/2)=L, a strictly increasing ratio from 1 to infinity. Expanding T'_L in u gives T''_L(-1)=-L^2(L^2-1)/3; the implicit root has slope -E_r/E_x>0, so the angular squared slope is c_L=-2E_r/E_x with remainder as stated. Independently expanding the direct geometric series using moments of (-r)^j at L=5 gives c_5=2.927050983124842 at r=(3-sqrt(5))/2, in agreement with the exact formula. Finally y=L lambda_L/2 lies between arcosh L and log(2L)/(1-1/L); inserting this O(log L) estimate in cosh(y/L) and inverting gives the displayed O(log^2(L)/L^3) damping error.

## originality

PASS

Best of current knowledge, the global finite-damping minimizer classification for every odd L>=5, the general onset coefficient and the large-length threshold are new relative to the inspected near matches. The Zak reduction, small lengths, even lengths and previously known weak-damping coefficients are not credited as new.

## value

PASS

An all-odd classification locates the global worst Zak frequency at any damping, thereby giving optimal frame constants without a global numerical optimization. The explicit local splitting and large-length threshold characterize a genuine change of minimizers rather than just producing another instance of a known frame-bound formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
