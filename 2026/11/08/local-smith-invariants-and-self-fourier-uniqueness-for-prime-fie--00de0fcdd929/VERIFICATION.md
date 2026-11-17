---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For every odd prime p, the conic x²+y²=1 is the cyclic norm-one group of order N=p-(-1/p)=2m (split or nonsplit). Dot-product restricted Fourier entries equal a group convolution kernel in real part (h+h^-1)/2. Since p does not divide N, unramified multiplicative character diagonalization is integral and preserves Smith exponents. Expanding zeta_p^a=(1+pi)^a shows for character r the first unit coefficient occurs exactly at k=min(r,N-r); earlier terms are p-divisible and acquire pi-order at least p-1+j>k, preventing cancellation. Hence exponents are 0,1,1,...,m-1,m-1,m and v_pi determinant=m², all nonzero (self-sampling uniqueness). Independent exact truncated-ring block ranks tested p=3,5,7 and every allowable precision. Finite primes do not prove arbitrary p; proof does.

## originality

PASS

The finite-field Bessel transform and norm-one convolution are classical, and are not claimed original. Khekalo 2001 concerns finite-field Bessel functions, but only catalogue details/abstract-level access was available, leaving a real priority risk. Garcia–Karaali–Katz concern symmetry-compressed Fourier minors/uncertainty, not full local cyclotomic Smith invariant lists of this conic self-restriction. The other fully inspected local Smith theorem is for a *parabola* and has different index set and invariant factors. On inspected evidence, the complete conic p-adic Smith valuation sequence and invertibility statement survive as qualified originality.

## value

PASS

An explicit all-prime complete local Smith profile of a natural Fourier self-restriction operator determines precise local invertibility and optimal cyclotomic precision loss. Both split and nonsplit norm-one tori have the same uniform pattern. This is an independently useful arithmetic invariant, not merely a determinant nonvanishing experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
