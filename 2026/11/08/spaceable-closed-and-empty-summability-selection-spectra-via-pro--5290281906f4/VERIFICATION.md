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
# Verification notes

The result is analytical. The following checks were performed on the displayed statements and on the relevant source theorems, not on an unrelated test file.

1. **Domain and quantifiers.** The two real Lorentz weights are positive decreasing, equal to one at the first coordinate, tend to zero, and have divergent first powers. In the first family the boundary exponent \(r>1\) is included. In the second no finite positive exponent is included. Separate ambient duals are constructed as allowed in the claim.
2. **Norms and closure.** Projective simple tensors satisfy \(\|a\otimes v\|_\pi=\|a\|_Z\|v\|_Z\). Hence the map from the full Banach space \(Z\) into the sup-norm Banach sequence space is a linear isometry; its image is necessarily norm-closed. For each nonzero image sequence, the normalized coordinate span is linearly isometric to \(Z\), so no collapse of basicness or symmetry is possible.
3. **All-point estimate.** For \(q\in A_w\), apply Hölder in the Lorentz norm, then adjoint duality as in [1, (3.8)]: \(\|(f(e_n))\|_q\le\|f\|\|w\|_q\). Every predual test vector is a bounded bilinear form whose second slice has dual norm at most \(\|B\|\|v\|_Z\).
4. **Nonstandard obstruction.** The tensor fiber \(X_v=\{a\otimes v:a\in Z\}\) is closed in \(V\) and hereditarily \(\ell_1\). For its canonical image inside \(V^{**}\), the restriction \(V^*\twoheadrightarrow X_v^*\) is surjective and open. Thus dense summability in the larger predual would induce dense summability in \(X_v^*\), contradicting [1, Lemma 2.4]. Relative weak-star convergence is weak convergence inside the fiber by Hahn–Banach extension. Both exact hypotheses of [1, Theorem 3.1] are therefore satisfied; its exclusion is for **every normalized sequence in the fiber**, not just the coordinate basis.
5. **Elementary exponents.** For the threshold weight \(w_n^r=(\log2)^2/[n(\log(n+1))^2]\); the series converges. For \(q<r\), the power exponent \(q/r<1\) dominates the logarithmic correction and the series diverges. For the empty-spectrum weight, every fixed logarithmic power is asymptotically larger than \(n^{-1/2}\), giving divergence for each finite \(q\).
6. **Scope and prior implication.** [1, Corollary 3.5] proves existence of one model and [1, Theorem 3.10] proves spaceability of open thresholds; these statements are not substituted for the closed/empty spaceability claim. Full-text results and §8 were read and compared.

No standalone numerical certificate is needed. No finite computation can certify the universal conclusions, and independent audit has not been performed.
