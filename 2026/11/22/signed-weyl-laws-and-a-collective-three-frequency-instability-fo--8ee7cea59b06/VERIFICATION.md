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

For row n and column n+j far from zero, T* T uses the common output level n+ℓ+j and TT* uses the two output levels n and n+j. Their denominators yield the difference −(2ℓ+j)n^{-3}+O(n^{-4}); its coefficient agrees with the (−j)-th Fourier coefficient of −2 Re(conj(B) zB′). With D_nn=(n+1)^{-3/2}, the finite-band remainder after subtracting D T(σ) D has tail norm O(N^{-4}) and deletion costs rank ≤2N, hence s_j=O(j^{-4}) for the remainder. To verify the weighted counting step put ρ=t^{-1/3}. Compression below ερ costs at most ερ+O(1) eigenvalues per sign; compression beyond Rρ has norm less than t once R³>||σ||∞. The couplings across cuts cost only bounded rank for each fixed partition. In blocks between ερ and Rρ, freezing D gives operator norm error ≤t times O(η) for fixed ε and mesh η. Normalized traces of powers of each long Toeplitz section converge to symbol moments because only boundedly many boundary rows disagree. Apply this to continuous upper and lower ramps for the signed count threshold; for fixed ramps the block averages converge by a Riemann sum as η tends to zero. Removing the ramps is justified by the null planar threshold set ±x^{-3}σ=1, even for constant σ. The limit in x integrates to (±σ)_+^{1/3}. Min–max absorbs the remainder at any fixed relative threshold because its count is O(t^{-1/4}). The negative angular mean gives a strictly positive negative-side coefficient. The combined count inverts to the stated singular-value law, Schatten cutoff and harmonic-sum limit. A strictly negative σ gives a negative tail quadratic form since the D-conjugated tail error is O(N^{-1}); a positive arc gives infinite positive inertia. For the witness the diagonal contribution to Re(conj(B)C) is 644/100, and the off-diagonal contributions at π/3 are 135/100, −275√3/100, and −198√3/100. The resulting (779−473√3)/100 is strictly negative by squaring. Every pair has strictly positive lower bound (v−u)(mv−ℓu) for that radial expression. Thus the example is not at a critical endpoint. The packaged checker was inspected, not run; neither the analytical count nor the sign test relies on reported finite spectra.

## originality

PASS

The supported distinction is the signed law for the adjoint self-commutator of every fixed polynomial Hardy Volterra operator, with its explicit third-order tail symbol, and the strict three-frequency witness. Credit older Volterra and Toeplitz methods, two-term Bergman inertia and the closely related cubic Hardy law for ordinary commutators. Similar third-order decay and identical Schatten exponents do not equate the operators or their signed counts.

## value

PASS

Exact sign-resolved eigenvalue counts go beyond order estimates or ideal membership, and yield a computable logarithmic spectral residue. The explicit strict witness shows that checking every pair of frequencies fails to detect infinite positive inertia for a natural fixed-polynomial family. This is a structural obstruction, not an isolated numerical threshold search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
