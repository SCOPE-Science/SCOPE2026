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

Let b_z=z(1−z), A_z=(X−λz)z^X, and φ_z=z exp(λ(z−1)). The pgf gives E A_z=0 and Cov(A_z,X)=λφ_z. The centered fitted influence ψ_z=A_z−φ_z(X−λ) subtracts the mean-score projection. Factorial moments at zw give E A_z A_w=λzw exp(λ(zw−1))[1+λ(1−z)(1−w)]; subtract λφ_zφ_w to get the asserted covariance and leading 2λ²b_z b_w. The diagonal is positive: A_z decays at large counts whereas its proposed cancellation by the nonconstant linear function φ_z(X−λ) cannot hold everywhere. The exact product remainder in nD_n is −n(mean(X)−λ)(mean(z^(X+1))−φ_z), with expected absolute value O_z(λ) by Cauchy–Schwarz; its contribution to H_n is O_z(n^(−1/2)) in L¹. The bias is −Cov(X,z^(X+1))/n and the pgf gives the displayed sign and value. Independently, with q_2=P(X=2), the centered difference ψ_z+2b_z(1_{X=2}−q_2) has second moment O_z(λ³): use the expansions on cells 0,1,2 and the polynomially weighted O(λ³) Poisson tail above two. Thus jointly for fixed weights H_n(z)=√2(nq_2−N_2)/(√n λ)+o_P(1), since σ_z∼√2 λ b_z and the binomial variance controls the coefficient substitution. That common binomial coordinate has a Gaussian limit when nq_2→∞, the stated centered signed Poisson limit at positive finite τ, and tends to zero in probability when nq_2→0 (no doubleton with high probability and the normalized deterministic term vanishes). A bounded subsequence of nλ² would force a further nonnormal subsequential limit, giving necessity. At τ=.3 the zero-doubleton value is .3873 and the one-doubleton value is about −2.1947; all larger counts remain outside the two-sided cutoff, with no atom on it. Hence rejection tends to 1−exp(−.15). Relative consistency of the sample mean since nλ→∞ ensures the same limit after plugging it into σ; no plug-in claim at zero intensity. Read checker.py and VERIFICATION.md: the reported finite covariance, bias and simulations are supplementary, not a plug-in proof or proof of any limit. No uploaded code was executed.

## originality

PASS

Credit the existing difference-form test, fixed-mean multiweight theory and exponential weight family. The supported distinct package is the unconditional shrinking-null calibration: a common rare-doubleton coordinate at all rates, its joint Gaussian/Poisson/degenerate regimes and the resultant critical null rejection probability. The covariance specialization and bias are checked as identities, not credited as separately novel against all fixed-parameter theory.

## value

PASS

This answers when the existing normal calibration is valid after mean fitting at low intensity: the governing sample information is the expected number of doubletons, not the expected number of positive counts. The common coordinate shows that combining a fixed collection of standardized weights does not yield multiple independent null signals at leading order. The jump from 5% nominal to about 14% actual asymptotic rejection gives a concrete consequence for a standard testing practice, independent of a claim about growing-weight or inverse-covariance procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
