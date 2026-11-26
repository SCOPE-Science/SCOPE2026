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

Deleting horizontal steps gives Catalan multiplicities depending only on profile weight, so weights index the entire spectrum. The half-line adjacency A counts the signed walks via factors A+I and A-I, which commute. Pairing opposite signs gives B=A^2-I, entrywise nonnegative including at height zero, and W_n(r) is the (0,0) entry of (A+I)^(n-2r)B^r. The difference W_n(r)-W_n(r+1)=2W_(n-1)(r) in the lower-half range is nonnegative by the same representation. B on even heights, with heights divided by two, forbids only the ground-level loop, so the central moment is R_floor(n/2); the extra factor A in odd length contributes zero by height parity. Every allowed profile has weight congruent to n modulo 2, proving complement sign reflection. R_0=1, R_1=0, and an up step, internal level steps and down step give R_m>0 for m>=2. The weight lists at n=0,1,2,3 are (1), (1,-1), (2,0,2), (4,0,0,-4), which give the claimed ranks and nullities by binomial multiplicity. At n=10 the Catalan count is 2188 and at m=5 the Riordan count is 6 (one internal three-level-step path and five paths with two up steps). Walsh orthogonality and comparison with the total mass give the signs, inverse norm and condition number in counting normalization. Inspected but did not run verify.py; python3 verify.py replays the reported finite checks, not the all-size proof.

## originality

PASS

The supported distinct content is the monotone lower-half Walsh spectrum with a sharp central Riordan gap, the exact singular-length classification and counting recovery on ordinary Motzkin horizontal profiles for all lengths. Classical counts and a diagonal restriction at one length are credited. The strongest compared local findings either treat only length ten on a larger group, change the underlying path class, or change the statistic and the spectrum. This is a best-of-knowledge assessment.

## value

PASS

Recoverability from natural count profiles is not settled by parity of the total count. The theorem identifies every exceptional length and gives the sharp noise amplification in the invertible cases, not merely a finite list of computed spectra. The link between a central Walsh mode and a different classical excursion class explains the entire spectral minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
