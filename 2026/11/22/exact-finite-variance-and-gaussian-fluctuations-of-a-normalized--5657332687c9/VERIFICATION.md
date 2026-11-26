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

Assesses /workspace/repairs/4/RESULT.md. The finite moments and Gaussian limit are unchanged; the repaired claim credits as its contribution the exact finite self-normalized moments and treats the limit as a broader-theorem consequence. In the proper-complex convention S=Σ|g_j|² is Gamma(n,1), independent of the uniform sphere direction and hence independent of Y=T/S². At two frequency points Wick contractions with k=0,1,2 cross-pairs in each direction have counts [4,16,4] and give E[|P(t)|⁴|P(s)|⁴]=4n⁴+16n²|D_n(t−s)|²+4|D_n(t−s)|⁴. Normalized Haar yields ∫|D_n|²=n and ∫|D_n|⁴=Σ_{|k|<n}(n−|k|)²=(2n³+n)/3. Therefore ET=2n² and ET²=4n⁴+(56n³+4n)/3. Divide respectively by ES²=n(n+1) and ES⁴=n(n+1)(n+2)(n+3) before subtracting the mean squared: the displayed rational variance follows, with n Var(Y_n)→8/3. Independent boundary checks: n=1 is identically one; n=2 has Y_2=1+2U(1−U) for U uniform on [0,1], giving mean 4/3 and variance 1/45. For the limit, U_n=(S−n)/n is O_P(n^−1/2), and Y_n−2=(H_n−2U_n²)/(1+U_n)². The fourth Wick polynomial has mean zero, no quadratic chaos, and covariance 4|r_n|⁴. Its n-scaled integrated variance tends to 8/3. In each connected q-vertex Wick cumulant the factors off a spanning tree have moduli ≤1; successively integrating leaves bounds the remainder by ||r_n||_1^(q−1). The sine bound gives ||r_n||_1≤(1+log n)/n, so the cumulants of √n H_n of orders q≥3 vanish. Moments, Gaussian determinacy and Slutsky establish the limit with either centering. The added proof of its coverage by the Gaussian-array theorem is also correct: averaging the quartic Wick integrand over M=2n nodes is exact, the standardized real two-vector has component correlations bounded by 1/d at cyclic distance d, and off-diagonal fourth powers satisfy both uniform row summability and the ordinary-index averaged tail test (wrap pairs at distance d number 2d, contributing an O(1/M) bound). The rank-four polynomial is fixed, and the √M-scaled variance tends to 16/3. Finite package checks were inspected but not rerun; they are not the proof of the CLT.

## originality

PASS

The distinct supported contribution after repair is the finite-n rational variance of the Haar-integrated squared periodogram divided by its squared sample power, for proper-complex Gaussian consecutive analytic coefficients. The CLT is not credited as a separate original result: it follows from Bardet–Surgailis Theorem 1(ii) by exact oversampling, covariance summability and cancellation of the quadratic component. No compared theorem supplied the finite-n variance of this ratio.

## value

PASS

The fourth power of the Nikolskii factor is a natural, rotation-invariant shape statistic for a standard random analytic polynomial; equivalently it measures spectral concentration after removing sample power. Its exact variance for every n supplies a quantitative benchmark on the complex sphere, including finite-size differences from fixed-amplitude phases that a shared leading coefficient cannot distinguish. The precision is independently useful for finite degrees and is not furnished by an array CLT or coarse expectation bounds. No claim of a new general Gaussian limit principle is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
