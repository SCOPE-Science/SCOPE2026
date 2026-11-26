---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For each row whiten the two-dimensional centered normal with covariance [[κ²,κρ],[κρ,1]] after scaling the shorter column to unit norm and removing the common sketch variance. The indefinite quadratic form has trace κ²−1, determinant −κ²(1−ρ²), and eigenvalues (κ²−1±Δ)/2. The d-row difference is therefore the difference of independent, positively scaled chi-squares in the full-rank case; the ratio against their sum gives Beta(d/2,d/2) and the strict risk I_z. Parallel columns give a zero risk and no almost-sure tie since the longer sketch is a strictly larger multiple of a nonzero Gaussian sketch of the shorter. For fixed lengths, Δ and z decrease strictly with |ρ|, while the Gram eigenvalue gap grows, increasing the square root of the eigenvalue ratio. The beta integral at fixed 0<z<1/2 is asymptotic to [z(1−z)]^a/(a(1−2z)) for a=d/2, by the endpoint derivative of log[t(1−t)]. Stirling gives the asserted normalization. This is the first two-column pivot only, with the asymptotic not uniform over changing κ or ρ. Replay: RESULT.md lines 29–61 and the Fraction examples at lines 63–65. Inspected VERIFICATION.md and verify.py, not executed; their finite rational and Monte Carlo checks cannot prove either continuum or asymptotic statement.

## originality

FAIL

The central exact law is already a direct specialization of Gaunt's Corollary 2.12, not merely a parallel use of standard probability tools. The extremal angle statement comes from monotonicity of that law; juxtaposing it with a two-by-two condition number does not produce an independent exact risk theorem. The other QR and catalogue comparisons do not override the exact older coverage.

## value

FAIL

The first-pivot error is a natural practical statistic and the conditioning warning is useful exposition. But in this frozen two-column problem the exact probability is already known through the sign theorem; the extrema, condition-number comparison and sharp equivalent follow by a scalar substitution, Gram diagonalization and standard beta endpoint asymptotics. No independently substantive unknown classification or downstream numerical result survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
