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

The prior norm convergence has the same amplitudes hθ_j and normalization 2h, for the coefficient-side product CC*. In its limiting matrix every (n,m) degree block is the outer product of the indicated multinomial vectors times the signed binomial entry. Normalizing one vector per degree and flipping degree signs gives DHD and a zero block. The moment formula gives H ≥ 0; independently the binomial series gives each row sum exactly 2, so the symmetric Schur bound is 2 without needing the Laguerre computation. After removing the common Fourier phase, the collision integral has one torus maximum. The Hessian in its log is −2Σ with det Σ=∏θ_j>0; the real even log has quartic error, giving a relative O(n^-1) Gaussian error by rescaling and an exponentially small exterior tail. Stirling then gives B_nn of order n^-r/2 and, for r=2, coefficient 1/(2π√(u(1−u))) times 1/n with summable error. Positive diagonal trace gives the exact trace claims; c_n→0 gives multiprime compactness. In the one-prime case the weakly null normalized block indicators have a uniformly positive quadratic form by the order N^-1/2 binomial estimate on order N^1/2 near-diagonal entries per row. For two primes the dyadic pieces of B^1/2 have bounded Hilbert–Schmidt norm and operator norm O(2^-j/4); the S_(2p) estimates are summable for p>1 and their sum is B^1/2. For p≤1 the S_1 obstruction suffices. An independent finite sum at n=25,50,100,200 checked the two- and three-weight constants (recorded in /workspace/branches/d1e44778-1767-4906-90da-b133a3544109/ordinal2_findings.md); at u=1/2 Vandermonde gives c_n²=H_nn, so B_nn~1/(πn), confirming the normalization exactly at the symmetric test weight. The uploaded numerical script was inspected, not run; it prints the two traces rather than asserting their agreement. Neither numerical check is needed for the infinite proof.

## originality

PASS

The exact critical limit, its weighted binomial matrix, the multinomial Fourier integral and qualitative multiprime compactness are covered by the closest preprint. What survives the comparison is the sharp two-prime ideal threshold and exact cutoff-trace residue together with nuclearity at three or more active primes. This is a bounded assessment, not historical priority certification.

## value

PASS

Active-prime count is an intrinsic parameter of the critical family. Distinguishing mere compactness, compactness with a sharp norm-ideal endpoint, and nuclearity answers a natural quantitative question left by the known limit. The explicit residue in the canonical degree cutoff measures the two-prime obstruction and retains dependence on the weights, not just support count. The useful result is this quantitative operator boundary, not a new central limit theorem or a gain at an arbitrary single exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
