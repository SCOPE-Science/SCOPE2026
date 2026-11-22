# Uniform marginal crossover for a one-dimensional power-law Ising droplet barrier

## Finding

For the infinite one-dimensional ferromagnetic Ising chain with couplings \(J_r=Jr^{-(1+\sigma)}\), the exact maximum *contiguous-droplet energy* has a uniform two-parameter weak-field asymptotic that resolves the marginal interaction exponent \(\sigma=1\) to bounded additive accuracy.

Fix \(J>0\), put \(R=2J/h\), \(\ell=\log R\), and let \(\lambda\) range in any fixed compact subset of \(\mathbb R\). For \(h\downarrow0\), set \(\sigma=1+\lambda/\ell\). Define \(\Phi(\lambda)=(1-e^{-\lambda})/\lambda\) for \(\lambda\ne0\) and \(\Phi(0)=1\). Let \(B(h,\sigma)\) be the maximal energy excess among contiguous finite plus-spin intervals relative to the all-minus background. Then

\[
\frac{B(h,1+\lambda/\ell)}{4J}
=\ell\Phi(\lambda)+\gamma-\lambda e^{-\lambda}+O_K(\ell^{-1}),
\]

uniformly for \(\lambda\in K\), for every compact \(K\subset\mathbb R\). Here \(\gamma\) is the Euler--Mascheroni constant. If \(n_c\) is any maximizing interval length, then, uniformly on the same compact sets,

\[
n_c=\left(\frac{R}{\sigma}\right)^{1/\sigma}+O_K(1),\qquad
\frac{n_c}{R}=e^{-\lambda}\bigl(1+O_K(\ell^{-1})\bigr).
\]

Consequently, the leading crossover function is positive and strictly decreasing, and its bounded-order correction is explicit. The result applies to the *contiguous-interval energy landscape*, not automatically to stochastic transition times, finite-volume saddles, or diffuse continuum critical droplets.

## Assumptions and scope

Consider spins \(s_i\in\{-1,+1\}\) indexed by \(\mathbb Z\), coupling \(J_r=J/r^{1+\sigma}\), with \(J>0\), \(\sigma>0\), and positive field \(h\). Only finite deviations from the all-minus state are considered, so their energy differences are well defined without assigning an infinite absolute Hamiltonian. For \(n\ge1\), change exactly the spins \(1,\ldots,n\) to plus, and denote the finite excitation energy by \(E_h(n)\); set \(E_h(0)=0\). Define \(B(h,\sigma)=\max_{n\in\mathbb Z_{\ge0}} E_h(n)\). The maximum exists for every positive field because \(E_h(n)\to-\infty\) as \(n\to\infty\) when \(h>0\), since the interaction energy grows sublinearly for each \(\sigma>0\).

The claim concerns the joint limit \(\ell=\log(2J/h)\to\infty\) with \(\lambda=(\sigma-1)\ell\) fixed in a compact set. It does not claim uniformity over unbounded \(\lambda\), over vanishing \(J\), or over a finite chain whose length competes with \(n_c\).

## Proof

**1. Exact energy and strictly decreasing increments.** A bond of length \(r\) crosses the boundary of the plus interval in exactly \(2\min(r,n)\) positions, and each antiparallel bond adds \(2Jr^{-(1+\sigma)}\) to the background energy. Therefore

\[
E_h(n)=4J\left(\sum_{r=1}^{n}r^{-\sigma}
+n\sum_{r=n+1}^{\infty}r^{-(1+\sigma)}\right)-2hn.
\]

For \(n\ge0\), direct subtraction gives

\[
E_h(n+1)-E_h(n)=4J\sum_{r=n+1}^{\infty}r^{-(1+\sigma)}-2h.
\]

This difference is strictly decreasing in \(n\). Thus the maximizer is unique except at a single exact tie of consecutive lengths, which does not affect the asymptotics.

**2. Uniform localization of the discrete maximum.** For \(\sigma\in[1/2,3/2]\), integral comparison or Euler--Maclaurin gives, uniformly as \(n\to\infty\),

\[
\sum_{r=n+1}^{\infty}r^{-(1+\sigma)}
=\frac{n^{-\sigma}}{\sigma}-\frac{n^{-(1+\sigma)}}2
+O(n^{-(2+\sigma)}).
\]

Set \(x_*=(R/\sigma)^{1/\sigma}\). Since \(h/(2J)=1/R\), the increment changes sign within \(O(1)\) integers of \(x_*\). Hence \(n_c=x_*+O(1)\), uniformly as \(\lambda\) runs over any fixed compact set, because \(\sigma=1+\lambda/\ell\) lies in the above interval for large \(\ell\). This estimate also covers two adjacent maximizing lengths at a tie.

**3. Energy expansion without spurious singularities.** Euler--Maclaurin yields

\[
\sum_{r=1}^{n}r^{-\sigma}+n\sum_{r=n+1}^{\infty}r^{-(1+\sigma)}
=\zeta(\sigma)-\frac{n^{1-\sigma}}{\sigma(\sigma-1)}
+O(n^{-(1+\sigma)}),
\]

uniformly for \(\sigma\in[1/2,3/2]\), \(\sigma\ne1\). The symbol \(\zeta\) on \(\sigma<1\) denotes the analytic continuation, not an ordinary convergent sum; the displayed combination remains finite. The cancellation of the \(n^{-\sigma}\) terms follows by expanding the finite harmonic sum and the tail separately. The continuous leading expression has derivative \(n^{-\sigma}/\sigma-1/R\) and second derivative \(-n^{-(1+\sigma)}\). Replacing \(n_c\) by \(x_*\) therefore costs only \(O(x_*^{-(1+\sigma)})\). At the stationary point, \(x_*/R=x_*^{1-\sigma}/\sigma\). Consequently,

\[
\frac{B(h,\sigma)}{4J}
=\zeta(\sigma)-\frac{x_*^{1-\sigma}}{\sigma-1}
+O(x_*^{-(1+\sigma)}).
\]

At \(\sigma=1\) the right side is interpreted by continuity as \(\gamma+\log x_*\), with the same negligible error; alternatively, apply the direct harmonic-number formula.

**4. Marginal expansion.** Write \(\varepsilon=\lambda/\ell\). Directly from \(x_*=(R/(1+\varepsilon))^{1/(1+\varepsilon)}\),

\[
\log x_*=\ell-\lambda+O_K(\ell^{-1}),\qquad
\varepsilon\log x_*=\lambda-\frac{\lambda^2}{\ell}+O_K(\ell^{-2}).
\]

The Laurent expansion \(\zeta(1+\varepsilon)=\varepsilon^{-1}+\gamma+O(\varepsilon)\) and the exponential expansion give

\[
\zeta(1+\varepsilon)-\frac{x_*^{-\varepsilon}}{\varepsilon}
=\ell\frac{1-e^{-\lambda}}{\lambda}+\gamma-\lambda e^{-\lambda}
+O_K(\ell^{-1}).
\]

The apparent singularity at \(\lambda=0\) is removable: write \((1-e^{-\varepsilon\log x_*})/\varepsilon=\log x_*\int_0^1 e^{-t\varepsilon\log x_*}\,dt\) to see that the remainder bounds are uniform through zero. Since \(x_*\asymp_K R\), the discretization remainder is exponentially smaller than \(\ell^{-1}\). Moreover \(\log x_* =\ell-\lambda+O_K(\ell^{-1})\), so \(n_c/R=e^{-\lambda}(1+O_K(\ell^{-1}))\). Finally \(\Phi(\lambda)=\int_0^1 e^{-\lambda t}\,dt\) implies \(\Phi>0\) and \(\Phi'(\lambda)=-\int_0^1 t e^{-\lambda t}\,dt<0\).

## Verification

The independently executable `check.py` evaluates finite droplet energies through the Hurwitz zeta function and compares them with their original finite-sum definitions; it also tests strict discrete concavity, maximizer localization, the Euler--Maclaurin cancellation coefficient, and the two-sided joint-limit behavior at fixed \(\lambda\). Command: `python check.py`. Tested with Python 3 and `mpmath` at 60 decimal digits; 159 deterministic assertions passed. Such checks are diagnostic, not substitutes for the uniform analytical proof above.

## Relationship to prior work

Lazarides and Pizzi (2025) analyzed apparent bistability and the weak-long-range critical-droplet scale under power-law couplings, including the regime approaching the marginal decay exponent. Van Enter, Kimura, Ruszel and Spitoni (2019) characterized critical lengths and metastable states for finite long-range Ising chains. Batini, Pagni and Defenu (2026) gave the exact two-wall lattice droplet-energy formula and separate fixed-exponent barrier regimes. Those object-level formulas and fixed-exponent laws are prior results, not claimed here. The finding is instead a **uniform joint-exponent/weak-field expansion of the optimized infinite-chain contiguous-droplet energy, including its order-one finite part**. The result is derived from the exact lattice interaction, not asserted for the continuum field-theory saddle or stochastic nucleation rate. A broader implicit formulation in classical asymptotic droplet analysis remains a publication-priority risk.

## Limitations

The chain is infinite, the droplet is a single finite contiguous interval, and only its energy maximum is classified. No theorem on full finite-volume transition-path barriers, finite-temperature kinetics or entropic rate prefactors follows merely from these calculations. The compact-\(\lambda\) uniformity does not justify extrapolation to fixed \(\sigma\ne1\) as \(h\to0\). The use of analytic continuation in the proof is a finite-sum identity, not a claim of a physically convergent infinite harmonic series for \(\sigma\le1\).

## References

1. A. Lazarides and A. Pizzi, *Apparent bistability from weak long-range interactions*, arXiv:2506.10068 (first submitted 11 June 2025), https://arxiv.org/abs/2506.10068.
2. A. C. D. van Enter, B. Kimura, W. Ruszel and C. Spitoni, *Nucleation for One-Dimensional Long-Range Ising Models*, Journal of Statistical Physics 174 (2019), https://doi.org/10.1007/s10955-019-02238-y.
3. L. Batini, V. Pagni and N. Defenu, *Critical droplets and metastability in long-range chains*, arXiv:2611.25764 (first submitted 19 November 2026), https://arxiv.org/abs/2611.25764.
