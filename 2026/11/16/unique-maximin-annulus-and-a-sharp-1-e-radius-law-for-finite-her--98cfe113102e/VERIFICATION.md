---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For normalized Gaussian STFT, angular orthogonality diagonalizes every radial annulus on Hermite modes: lambda_j(a,s)=1/j!∫_a^(a+s)e^-u u^j du. Integration by parts gives lambda_(j+1)-lambda_j=p_(j+1)(a)-p_(j+1)(a+s), whose sign switches at most once from + to -, so the minimum on 0..K is min(lambda_0,lambda_K), with strict interior gap at their positive crossing for K>=2. The ratio lambda_K/lambda_0 grows strictly from below 1 to infinity, so unique a_K(s)>0 satisfies ∫_0^s e^-t(a+t)^K dt=K!(1-e^-s). At crossing lambda'_K=lambda_(K-1)-lambda_K>0, and lambda_K increases until crossing; lambda_0 decreases afterwards, establishing global unique maximin and bottom eigenspace span{h0,hK}. For fixed s, a/K->1/e from Stirling; uniform bounded-t limit gives J_s=∫_0^s e^((e-1)t)dt and log corrections as claimed. Independently checked numerical crossing and intermediate-mode inequalities at K=2,3,8,40, with no extrapolation of finite checks to large K; K100 naive incomplete-gamma evaluation underflows, so excluded as evidence.

## originality

PASS

Best-of-knowledge statement-level comparison of aliases, stronger coverage and tables does not show domination of precise claim. The current problem optimizes the LEAST eigenvalue in a fixed finite Hermite subspace (indices 0..K). The primary 2025 result optimizes the SECOND LARGEST eigenvalue of the infinite Fock Toeplitz spectrum and agrees with endpoint balancing only in excluded K=1-like special case. The published staircase maximizes the LARGEST eigenvalue for each preselected annulus, the opposite spectral edge. Unimodality in the previously published mode staircase is useful for the min-at-endpoints reduction, but finding and globally optimizing the crossing and deriving its sharp bandwidth expansion requires additional analysis. No prior implication to full claim identified; claims about K=1 overlap are expressly excluded.

## value

PASS

Unique maximin annulus is an exact worst-case observability design for a natural finite-dimensional Hermite subspace. It gives the unique geometry, precise two-dimensional worst-signal space and a sharp 1/e asymptotic with logarithmic correction for growing bandwidth; useful as a robust time-frequency sensing benchmark, not merely textbook diagonalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
