---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For equal separately normalized boundary-circle Hardy masses, Laurent basis e_n=z^n/sqrt(1+R^(2n)) is orthonormal. Compression gives the bilateral k-shift weights w_n=(A+B R^(2n+k))/sqrt((1+R^(2n))(1+R^(2n+2k))). For k>0 the selfcommutator diagonal entries are f(q²s)-f(s), with f(t)=(a+2ct+bt²)/(1+(q+q^-1)t+t²). Independent exact symbolic algebra verified the stated factorization as a positive prefactor times a linear polynomial in s. Since s ranges a two-sided geometric tail to zero and infinity, positivity iff da>=2c>=db. Cauchy--Schwarz makes da>=2c redundant whenever 2c>=db, yielding the disk |B-A/d|<=|A|/d; adjoint reverses roles for k<0. Two-sided geometric tail decay proves C in every S_p>0, and telescoping proves tr C=k(a-b). Both tail coefficients zero imply only A=B=0 is normal. No finite diagnostic stands in for these infinite claims.

## originality

PASS

This is an exact phase-dependent complex disk classification for a single angular mode with independent two-boundary amplitudes, not only analytic Laurent monomial multipliers. Accessible Adhikari--Das and Adhikari--Das--Jain--Sarkar primary texts characterize algebraic Toeplitz and compact perturbation behavior without this disk statement. The Resultary coordinate multiplier selfcommutator is a one-dimensional constrained subfamily B=R^k A and cannot imply the full disk.

## value

PASS

Sharp complete scalar classification of hyponormality with explicitly nonnormal nonanalytic examples, full Schatten regularity, and exact trace on a natural annular Hardy Toeplitz family; an independently useful operator-theoretic boundary rather than a routine fixed-example check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
