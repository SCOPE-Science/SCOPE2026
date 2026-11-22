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

# Reproducibility and proof checks

1. **Model normalization.** For \(t=e^{-s}\), the Cayley conjugate of the disk composition map is \(w\mapsto(w+1-t)/t\). Its Hardy-space weight is \(1/t\); after inverse Laplace transform, composition acts as \(g(x)\mapsto e^{-(1-t)x}g(tx)\). Multiplication by \(\sqrt t\) and the logarithmic unitary yield the stated unit-norm-dominated \(\Sigma_s\).
2. **Bounds.** Verify the continuous contraction-semigroup dilation theorem is invoked for the *common* semigroup, so all matrix-integrated entries share one spectral measure. Weakly null packets of width \(n\), placed in \([-2n,-n]\), have translation error at most \(\sqrt{2S/n}\) for \(s\le S\), damping error at most \(e^{-n+S}\), and measure-tail error at most twice the total variation beyond \(S\).
3. **Matrix-level equality.** For each finite matrix of Fourier transforms and every fixed frequency, select a Euclidean unit singular vector. Tensor with the packet to obtain the essential lower bound, then take the frequency supremum.
4. **Exact example.** For \(|z|=1\), \(|1+z-z^2|^2=3-z^2-z^{-2}=3-2\cos(2\arg z)\), so its maximum is exactly \(5\). Every \(0<a<1\) gives the full circle of phases through \(z=e^{-i\xi(-\log a)}\).

These are analytic checks; no finite numerical test is asserted to certify the infinite-dimensional claim. Independent audit has not been performed. Historical priority is qualified by inaccessible older full text.
