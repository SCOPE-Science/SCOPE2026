---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the spectral-component theorem

This is an analytic proof, with no computational or finite-exhaustion prerequisites.

1. Coefficients: the function \(h(w)=w(1-w)^{-1/4}\sin(\log(1-w))\) has \(h_0=h_1=0\) and \(h_2=-1\), so the rank-one operator is nonzero and square-zero. The \(H^2\) bound is deduced from an integrable exponent \(1/2<1\) on the boundary squared modulus.
2. Spectral identity: the scalar \(K_c(zI-S)^{-1}e_0\) equals \(c h(1/z)e_0\). Fredholm index \(-1\) retains the open disk, and the essential spectrum retains the circle.
3. Exact real-root localization: \(\partial_t\log H_c(t)=e^{-t}/(1-e^{-t})+1/4+\cot t\), and its derivative is strictly negative on each negative-sine interval; maxima grow exponentially. Exactly two real roots occur for every sufficiently large lobe.
4. Count: two roots per logarithmic width \(2\pi\) gives \(N_c(\delta)=(1/\pi)\log(1/\delta)+O_c(1)\), with a bounded partial-interval correction.

The statement for every \(c>0\) is proved directly; no extrapolation from finite tests is used. The proof does not establish where nonreal outliers lie, except that their only possible accumulation on the original circle is at \(1\). The exact older literature coverage remains subject to external confirmation.
