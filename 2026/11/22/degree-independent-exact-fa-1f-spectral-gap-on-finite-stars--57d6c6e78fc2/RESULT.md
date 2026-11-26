# Exact slow eigenspace of the FA-1f chain on a finite star

## Finding

Let \(K_{1,n}\) have \(n\ge2\) leaves, let \(q\in(0,1)\) be the vacancy probability, and write \(p=1-q\). For the unit-rate FA-1f heat-bath chain on the nonempty-vacancy component, put \(\lambda_*=1-\sqrt p\), the known star relaxation gap. The *entire* eigenspace of \(-\mathcal L\) at \(\lambda_*\) is as follows. If \(h\) is the hub occupation and \(\xi=(\eta_1,\ldots,\eta_n)\) the leaf occupations, then
\[
g(\xi)=\sum_{i=1}^n a_i(\eta_i-p),\quad \sum_{i=1}^n a_i=0,\qquad
 f(0,\xi)=g(\xi),\qquad f(1,\xi)=\frac{q}{q-\lambda_*}g(\xi)
\]
on the allowed states. In particular the multiplicity is exactly \(n-1\), not merely at least \(n-1\). A centered observable invariant under all leaf permutations has no component in this eigenspace, so on each finite star its stationary autocovariance has no term proportional to \(e^{-t\lambda_*}\).

## Assumptions and scope

Each site attempts independently at rate one to refresh its occupation from Bernoulli\((p)\); the refresh is allowed only if a neighbor is vacant. Occupation \(0\) denotes a vacancy. The fully occupied state is isolated and removed. From any allowed state with occupied hub, the hub can become vacant, and from a vacant hub all leaf configurations are accessible. The chain is therefore irreducible on its allowed states, with reversible measure given by Bernoulli\((p)\) product measure conditioned on the allowed states. The heat-bath clock convention matters. For the exceptional one-leaf star, the gap is \(q\); there is no positive-dimensional leaf-contrast space in that case.

## Proof

Write \(\xi_\star=(1,\ldots,1)\), and let \(H_{\rm leaf}\) be the negative generator of the unconstrained independent rate-one leaf refreshes on the full leaf cube, equipped with its Bernoulli\((p)\) product law. Its spectrum is \(0,1,\ldots,n\): products of distinct centered occupations diagonalize it, with eigenvalue the number of factors. Let \(P_\star\) multiply by the indicator of \(\xi_\star\).

Write \((g,b)\) for the two hub components of an eigenfunction of \(-\mathcal L\) at \(\lambda<q\). The component \(b\) is only defined for \(\xi\ne\xi_\star\). From an occupied hub only the hub can flip, at rate \(q\); hence \(b=qg/(q-\lambda)\) there. From a vacant hub, all leaves may refresh, and the hub may fill at rate \(p\) except when \(\xi=\xi_\star\). Substitution gives the equivalent equation on the full leaf cube
\[
\left[H_{\rm leaf}-\mu(\lambda)I+(\mu(\lambda)-\lambda)P_\star\right]g=0,
\qquad \mu(\lambda)=\frac{\lambda(1-\lambda)}{q-\lambda}.
\]

In particular \(0<\lambda_*<q\) and \(\mu(\lambda_*)=1\). Pair the equation at \(\lambda_*\) with \(w(\xi)=\sum_i(\eta_i-p)\) in the unconditioned leaf product space. The contribution of \(H_{\rm leaf}-I\) is zero by self-adjointness and \(H_{\rm leaf}w=w\), whereas the rank-one term equals \((1-\lambda_*)p^n(nq)g(\xi_\star)\). Its prefactor is nonzero, forcing \(g(\xi_\star)=0\). Thus \(H_{\rm leaf}g=g\), and the only possibilities are the linear combinations in the statement: their evaluation at \(\xi_\star\) equals \(q\sum_i a_i\). Conversely every such combination solves the leaf equation and reconstructs an eigenfunction. The stated dimension follows. Averaging over permutations of the leaves annihilates each of these combinations, proving orthogonality to permutation-invariant observables. Reversible spectral expansion then proves the autocovariance assertion.

For completeness, the same scalar elimination verifies the gap normalization. On \(0<\lambda<\lambda_*\), \(0<\lambda<\mu(\lambda)<1\). The inequality \(\mu>\lambda\) follows from \(p>0\), and \(\mu\) increases strictly up to \(1\) since \(\mu'(\lambda)=1+pq/(q-\lambda)^2\). The rank-one term is nonnegative, so min–max makes the second eigenvalue of the eliminated operator at least \(1-\mu>0\). Its constant-vector Rayleigh quotient is \(-\mu(1-p^n)-\lambda p^n<0\). It is therefore nonsingular on this interval. For \(n=1\), the two states with exactly one vacancy each jump to the doubly vacant state at rate \(q\), with reverse rates \(p\). The antisymmetric eigenvalue is \(q\), and the two eigenvalues in the symmetric block are \(0\) and \(q+2p=2-q\).

## Verification

The accompanying `verify.py` checks detailed balance and the contrast eigenfunctions with exact fractions, and optionally diagonalizes selected finite symmetrized generators to check the gap normalization. These are finite consistency checks, not a certificate of the absence of further modes at \(\lambda_*\). The pairing with \(w\) in the proof establishes that absence for every \(n\ge2\) and \(0<q<1\). Run `python3 verify.py` (NumPy and SciPy are used for the optional spectra).

## Relationship to prior work and limitations

*Size-independent nonradial relaxation modes of facilitated spins on bicliques* states the exact star gap and proves a contrast construction for bicliques: the contrast construction also supplies at least \(n-1\) modes on a star. Neither the gap formula nor that lower bound on dimension is claimed as new here. The additional statement is the exhaustion of the gap eigenspace, including the absence of a permutation-invariant mode at that rate. The comparison does not establish historical priority. The general FA-1f bounds of Cancrini, Martinelli, Roberto and Toninelli and of Shapira do not identify this eigenspace. No full spectrum, uniform separation for permutation-invariant modes as \(n\to\infty\), mixing-time estimate, or Metropolis analogue is asserted.

## References

1. *Size-independent nonradial relaxation modes of facilitated spins on bicliques*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-size-independent-nonradial-relaxation-modes-of-facilitated-spins--5b75bead5e92, Finding, Proof and Relationship to prior work.
2. N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Facilitated spin models: recent and new results*, arXiv:0712.1934, §6.
3. A. Shapira, *A Note on the Spectral Gap of the Fredrickson–Andersen One Spin Facilitated Model*, J. Stat. Phys. 181 (2020), 2346–2352, DOI 10.1007/s10955-020-02666-1.
