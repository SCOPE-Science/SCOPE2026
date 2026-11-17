# A two-degree spectral crossover for annular Hardy cross-commutators

## Finding

Let \(H_r\) be the equal-boundary-weight Hardy space on the annulus \(\{r<|z|<1\}\), and let \(S_j=M_{z^j}\). The compact, generally nonnormal cross-commutator
\[
K_{m,n}(r)=[S_m^*,S_n]=S_m^*S_n-S_nS_m^*,\qquad m,n\in\mathbb N,
\]
has an exactly sampled, strictly log-concave singular-value profile. The substantive two-degree assertion concerns \(m\ne n\); the equal-degree specialization is included to calibrate the formulas against known self-commutators.

Put \(h=-2\log r>0\), \(a=mh\), \(b=nh\), and define, for real \(t\),
\[
F_{a,b}(t)=\frac{(1-e^{-a})(1-e^{-b})e^{-t}}{(e^{-a}+e^{-t})\sqrt{(1+e^{-t})(1+e^{a-b-t})}}.
\]
**Exact finite-width statement.** The complete multiset of positive singular values of \(K_{m,n}(r)\), counted with multiplicities, is
\[
\big\{F_{a,b}(jh):j\in\mathbb Z\big\}.
\]
The profile is strictly log-concave, vanishes at both infinities, and has a unique real maximizer. Write \(M(a,b)=\max_{t\in\mathbb R}F_{a,b}(t)>0\). For \(0<u<M(a,b)\), let \(\ell_{a,b}(u)\) be the length of the interval \(\{t:F_{a,b}(t)>u\}\), and let \(N_{r;m,n}(u)\) count singular values strictly above \(u\). Then, for every annulus radius and all positive integer degrees, including unequal degrees,
\[
\boxed{\left|N_{r;m,n}(u)-\frac{\ell_{a,b}(u)}h\right|\le1.}
\]
For every real \(p>0\), with \(H_p(a,b)=\int_{\mathbb R}F_{a,b}(t)^p\,dt\), the all-Schatten finite-size estimate is
\[
\boxed{\left|\|K_{m,n}(r)\|_{\mathcal S_p}^{p}-\frac{H_p(a,b)}h\right|\le M(a,b)^p.}
\]
Both bounds have an absolute discrepancy independent of radius, the two degrees, and \(p\).

**Two-parameter thin-annulus/high-degree crossover.** Suppose \(r_k\uparrow1\), \(h_k=-2\log r_k\downarrow0\), and two sequences of positive integers satisfy \(m_kh_k\to a>0\) and \(n_kh_k\to b>0\). Then for every fixed \(p>0\),
\[
\boxed{h_k\|K_{m_k,n_k}(r_k)\|_{\mathcal S_p}^p\longrightarrow H_p(a,b),\quad\|K_{m_k,n_k}(r_k)\|\longrightarrow M(a,b).}
\]
For \(0<u<M(a,b)\), the rescaled singular-value counting function converges to \(\ell_{a,b}(u)\). The profiles satisfy a degree-exchange identity
\[
F_{a,b}(t)=F_{b,a}(t+b-a),
\]
so the two opposite cross-commutators have identical singular-value distributions, though the location of their Fourier modes shifts.

For the Hilbert--Schmidt crossover there is a closed elementary logarithmic expression. Set \(\alpha=e^{-a}\) and \(\beta=e^{-b}\). When \(a\ne b\),
\[
\boxed{\begin{aligned}
H_2(a,b)=(1-\alpha)^2(1-\beta)^2\Bigg[&-\frac1{(1-\alpha)(1-\beta)}\\
&-\frac{\alpha\log\alpha}{(1-\alpha)^2(\alpha-\beta)}
+\frac{\beta\log\beta}{(\alpha-\beta)(1-\beta)^2}\Bigg].
\end{aligned}}
\]
The continuous diagonal value is \(H_2(a,a)=a(1-e^{-2a})-2(1-e^{-a})^2\). The non-diagonal expression is generally not the one-degree hyperbolic-cosine profile.

## Assumptions and scope

The space \(H_r\) is the completion of Laurent polynomials for
\[
\left\|\sum_{j\in\mathbb Z}c_jz^j\right\|^2=\sum_{j\in\mathbb Z}(1+r^{2j})|c_j|^2.
\]
Both boundary circles carry normalized angular measure of total mass one. The powers \(m,n\) are positive integers, \(0<r<1\), and \(p>0\). For \(p<1\), \(\mathcal S_p\) is a quasi-Schatten class. No positivity or self-adjointness is asserted for \(K_{m,n}(r)\) when \(m\ne n\). Counting always uses a strict threshold and multiplicity. The scaling limits require two strictly positive finite limits \(a,b\), and counting limits require \(u\) strictly below the limiting continuous peak.

## Proof

**Step 1: full singular spectrum.** Write \(q=r^2=e^{-h}\), \(V_j=1+q^j\), and \(e_j=z^j/\sqrt{V_j}\). Then \(S_me_j=\sqrt{V_{j+m}/V_j}\,e_{j+m}\). Direct multiplication gives
\[
K_{m,n}(r)e_j=\left(\frac{V_{j+n}}{\sqrt{V_jV_{j+n-m}}}-\frac{\sqrt{V_jV_{j+n-m}}}{V_{j-m}}\right)e_{j+n-m}.
\]
With \(x=q^j\), \(\alpha=q^m\), and \(\beta=q^n\), the coefficient simplifies exactly to
\[
\frac{(1-\alpha)(1-\beta)x}{(\alpha+x)\sqrt{(1+x)(1+\beta x/\alpha)}}=F_{a,b}(jh)>0.
\]
As \(j\to\pm\infty\), these coefficients decay geometrically. The output indices \(j+n-m\) are pairwise distinct. Hence \(K^*K\) is diagonal with eigenvalues \(F_{a,b}(jh)^2\), proving that every positive singular value is exactly one sampled profile value, that there are no other positive singular values, and that \(K\in\mathcal S_p\) for all \(p>0\).

**Step 2: strict logarithmic concavity.** Apart from additive constants,
\[
\log F_{a,b}(t)=-t-\log(e^{-a}+e^{-t})-\tfrac12\log(1+e^{-t})-\tfrac12\log(1+e^{a-b-t}).
\]
Each negative logarithm of a two-term positive exponential sum has strictly negative second derivative. Thus \(\log F\) is strictly concave. Its derivative tends to \(+1\) at \(-\infty\) and \(-1\) at \(+\infty\), proving a unique maximum and that every nontrivial upper level set is a bounded open interval. The maximizing discrete index, if desired, belongs to the two integers adjacent to the continuous peak divided by \(h\).

**Step 3: sharp lattice discrepancy.** Every upper level interval \((t_-,t_+)\) has length \(\ell=t_+-t_-\). The number of points of \(h\mathbb Z\) strictly inside it differs from \(\ell/h\) by at most one, even when an endpoint lies on the lattice. Since the singular values are exactly the samples and \(N=0\) above the peak, this proves the counting estimate for all thresholds. The constant one is a universal lattice-rounding bound; no asymptotic assumption enters.

**Step 4: every Schatten exponent.** Geometric tails justify the layer-cake identity
\[
\sum_{j\in\mathbb Z}F_{a,b}(jh)^p=p\int_0^{M(a,b)}u^{p-1}N_{r;m,n}(u)\,du.
\]
Fubini also yields \(H_p(a,b)=p\int_0^{M(a,b)}u^{p-1}\ell_{a,b}(u)\,du\). Integrating the constant-one discrepancy gives the bound \(p\int_0^Mu^{p-1}du=M^p\), for every real \(p>0\), including the quasi-Schatten range.

**Step 5: moving-degree limits.** For \((a_k,b_k)\to(a,b)\in(0,\infty)^2\), the profiles converge locally uniformly, while the exponential tails admit uniform integrable envelopes on a compact neighborhood of \((a,b)\). Therefore \(H_p(a_k,b_k)\to H_p(a,b)\). Multiplying the Step 4 bound by \(h_k\) proves the normalized Schatten limit. The strict logarithmic concavity, uniform tail bounds, and density of the lattice as \(h_k\downarrow0\) prove convergence of the sampled maximum to \(M(a,b)\). Continuity and strict monotonicity of the two sides of each upper-level profile give convergence of the two endpoints, proving the counting limit. Substitution \(x=e^{-t}\) proves the degree-exchange identity.

**Step 6: explicit second moment.** With the same substitution,
\[
H_2(a,b)=(1-\alpha)^2(1-\beta)^2\int_0^\infty\frac{\alpha x}{(x+\alpha)^2(1+x)(\alpha+\beta x)}\,dx.
\]
Elementary partial fractions, evaluated at zero and infinity, give the boxed expression for \(\alpha\ne\beta\); cancellation of the logarithmic divergences is exact. Taking the continuous limit \(\beta\to\alpha\), or integrating directly in the equal-degree case, gives the stated diagonal value. No finite numerical experiment is used to prove the improper integral identity.

## Verification

The standalone `checker.py` evaluates the exact coefficient numerator with rational arithmetic for independent parameters; checks positivity and degree exchange; compares the derived Hilbert--Schmidt logarithmic constant with independent numerical quadrature; and tests the lattice counting bounds at unequal degrees. Its executed output was `HARDY_CROSS_COMMUTATOR_DIAGNOSTICS_OK 5332`. These are finite diagnostic assertions; the universal conclusions rely on Steps 1--6. The complete theorem and code use the same normalized boundary measures.

## Relationship to prior work

Adhikari and Das (2026) characterize Toeplitz multiplication and products on this annular Hardy space; their results do not compute the singular-value spectrum of these two-degree cross-commutators. Earlier published work titled *Exact counting law and thin-annulus scaling for monomial self-commutators* already proves a sharp lattice bound and width-degree limit when the two degrees **coincide**. The diagonal specialization here is not claimed as original.

A second closely related published result, *Half-Schatten perimeter law and spectral Weyl profile for pinching annular Hardy multipliers*, already derives the **exact mixed commutator matrix coefficients** for any fixed pair of Laurent monomial degrees, and proves a spectral Weyl law when all degrees remain fixed while the annulus pinches. We do not claim novelty for those coefficients or fixed-degree limits. The proposed additional statement is the unequal-degree, jointly moving-power two-parameter singular-value distribution, its globally uniform count and Schatten remainders, and the two-variable closed Hilbert--Schmidt crossover. A fixed-degree limit has \(mh\to0\) and \(nh\to0\) and does not imply the positive-parameter result. Douglas and Kim's classification of reducing subspaces of annular monomial multipliers does not give this spectral limit.

## Limitations

The theorem concerns equal-normalized-boundary Hardy norms, positive monomial degrees, and their cross-adjoint commutator; it does not treat arbitrary symbols, other Hardy norms, or multi-band commutator sums. Exact algebraic cross-commutator coefficients and the equal-degree spectral law are prior knowledge. The sharpness of the *lattice* discrepancy is elementary once the unimodal profile is identified; the value claimed here is its uniform two-degree spectral application, not a new general sampling theorem. Some historical equivalent presentations in bilateral-shift or Hankel-product literature may remain unidentified. The result is analytically reviewed within this package but has not undergone independent audit.

## References

1. S. Adhikari and S. Das, *Algebraic properties of Toeplitz operators on annulus and multiply connected domains*, arXiv:2611.01717v1, first posted 2026-11-01, https://arxiv.org/html/2611.01717v1.
2. *Exact counting law and thin-annulus scaling for monomial self-commutators*, public mathematical record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-counting-law-and-thin-annulus-scaling-for-monomial-self-co--10f66dd5f49c.
3. *Half-Schatten perimeter law and spectral Weyl profile for pinching annular Hardy multipliers*, public mathematical record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-schatten-perimeter-law-and-spectral-weyl-profile-for-pinchi--afd674958865.
4. R. G. Douglas and Y.-S. Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794, first posted 2009-02-11, https://arxiv.org/abs/0902.1794.
