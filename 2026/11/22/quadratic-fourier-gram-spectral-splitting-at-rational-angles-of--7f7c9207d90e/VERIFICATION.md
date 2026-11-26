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

For fixed p<1 and finite N the observation rows admit a norm-convergent Taylor series (the geometric weight also controls the rows on a sufficiently small complex strip). At resonance interpolation at L distinct roots gives rank L and kernel polynomials (z^L−1)R. The coefficient norm on these is twice the squared norm of R, as the two blocks are disjoint. Let E be the kernel. Min–max restricted to E puts all K small eigenvalues at O(ε²), and the other L stay bounded below. With respect to E and its orthogonal complement, Schur complementation of the invertible hard block subtracts the squared projection of the first variation onto the unperturbed range. The resulting soft block is ε²T+O(|ε|³), T the Gram of the projected first variation on E. Taking the Schur complement at a small eigenvalue parameter instead of zero changes it by O(ε⁴) uniformly for |λ|=O(ε²); inertia of the shifted Hermitian blocks and the norm error sandwich the ordered eigenvalues even at repeated coefficients. The first derivative is iLsR(ζ^r); projecting off the range subtracts its conditional mean given r=s mod L. Since (s−r)/L has geometric parameter p^L, its variance is p^L/(1−p^L)^2. In the isometric kernel coordinates this gives T=L⁴p^L H_K/[2(1−p^L)^2]; the moment form is strictly positive by interpolation. For K=L the Fourier matrix diagonalizes H_L with masses LW_r, while the repeated blocks give hard eigenvalues 2LW_r. Dividing the hard maximum by the soft minimum and taking a square root gives exactly the displayed coefficient of |ε|^−1. The result is local, not uniform at extreme p or changing L. Fresh direct SVDs of 384 weighted observation rows for 2≤L≤7, p=.46,.83, all admissible coprime angles and redundancies tested 360 signed perturbations. Maximum relative coefficient errors were 5.28e−5 for the soft branches and 4.17e−8 for the condition coefficient. These are finite corroboration; the omitted row tail has norm at most sqrt(N p^384).

## originality

PASS

Credit the identical geometric measure, moments, resonant finite support, and norm/determinant data to Zhedanov, and the framework of finite Vandermonde cluster scales to the cited authors. The checked sources do not give the individual angular-splitting coefficients of the infinite weighted orbit or the paired hard/soft constants at doubled bandwidth.

## value

PASS

The first redundant band of a fixed geometric sampling orbit is a natural rank-loss boundary. Its complete positive coefficient spectrum distinguishes weak directions that determinant order or a bound on the weakest direction cannot separate. The sharp doubled-band condition coefficient quantifies actual reconstruction sensitivity at this boundary, not only rank loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
