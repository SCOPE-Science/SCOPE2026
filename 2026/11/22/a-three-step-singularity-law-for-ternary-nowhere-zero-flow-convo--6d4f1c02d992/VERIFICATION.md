---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the whole ambient group, each Fourier character is one eigenvector of counting convolution. The ternary zero-sum filter gives the average of three products with local factors 2 at a frequency-symbol match and -1 otherwise, i.e. (-1)^n times the sum of three signed powers (-2)^(c_j) divided by 3. This is integer-valued because each power is 1 modulo 3; negation symmetry also gives real eigenvalues, whose moduli are the singular values. Divide a putative vanishing sum by the smallest signed power. A unique minimum leaves an odd integer; three minima leave 3; two minima force the remaining exponent to exceed the minimum by one. For n>=2 this gives exactly (m,m,m+1) up to permutation with m>=1 and n=3m+1. Counting ambient words gives the factor of three and the stated multinomial nullity. The normalized probability for one ordered count triple differs from the central equal-count probability at length 3m by (3m+1)/(3(m+1)); Stirling then gives the claimed constant and relative O(1/n) along the singular progression only. A separate phase-count check on dual coset representatives at n=2 through 7 gave nonzero ambient nullities only at 4 and 7, namely 36 and 630. RESULT.md lines 35–61 give the all-length replay; check.py was inspected, not executed.

## originality

PASS

The supported distinct result is the full-length exact cancellation and ambient-rank law for the full-weight part of the ternary single-check code, including its multiplicities and asymptotic nullity density. Character diagonalization and modular flow counts are established. The closest inspected graph spectra use different generators or supports and do not give the claimed cancellation criterion. This comparison does not certify historical priority.

## value

PASS

The dipole is a canonical nowhere-zero flow family, and ambient counting convolution asks a natural recoverability question not answered by counting its flows. The exact singular progression, description of every invisible mode, and quantitative rate of loss give a usable rank classification across all lengths. The value is the cancellation and rank law, not the standard character filter; no claim is made about stable inversion away from zero or arbitrary graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
