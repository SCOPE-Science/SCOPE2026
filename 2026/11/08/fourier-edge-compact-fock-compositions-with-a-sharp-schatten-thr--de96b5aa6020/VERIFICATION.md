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

# Analytic verification and reproducibility

The result can be checked without external computation. Start with \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\) and \(e_n(z)=z^n/\sqrt{n!}\). Verify the exact cancellation
\[
|e^{\beta z^2/2}|^2e^{-\beta|z|^2}=e^{-2\beta(\operatorname{Im}z)^2}.
\]
For boundedness use the variable substitution \(w=\lambda z\) with Jacobian \(\lambda^2\), and for compactness truncate the output to disks and use \(\sup_{|z|>R}|g_a(z)|e^{-\beta(\operatorname{Im}z)^2}\to0\).

For the Schatten criterion, inspect Du (2011), Theorem 2.3; it applies because the weighted composition operator is already bounded and its source/target is the standard Gaussian Fock Hilbert space. The remaining scalar integral \(\int |g_a(x+iy)|^p e^{-p\beta y^2}dxdy\) is finite exactly when \(p(1-a)>1\). One may verify the endpoint asymptotic by splitting the Fourier integral at \(t=|x|^{-1}\), integrating the remainder by parts, and using the classical oscillatory Mellin integral; the global bound permits dominated convergence in \(y\). No finite sample is claimed to prove an infinite statement.

For the exact Hilbert--Schmidt norm, sum the Fock basis first and use the Plancherel convention \(\int_{\mathbb R}|\hat h(x)|^2dx=2\pi\int_{\mathbb R}|h(t)|^2dt\). Complete the square in the Gaussian integral. The endpoint windows integrate \(|x|^{-1}\) or \(|x|^{2a-2}\) on the two tails. All constants in the result follow from these steps. Horizontal truncation is not the same as a singular-value partial sum.

No independent audit, machine formalization, or external certification has been performed.
