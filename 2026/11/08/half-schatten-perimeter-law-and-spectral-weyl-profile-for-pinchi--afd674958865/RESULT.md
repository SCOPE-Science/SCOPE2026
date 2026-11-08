# Half-Schatten perimeter law and spectral Weyl profile for pinching annular Hardy multipliers

## Finding
For each nonconstant finite Laurent polynomial \(\phi(z)=\sum_{k=-m}^{m}a_kz^k\), let \(M_{\phi,r}\) be analytic multiplication on the standard two-boundary Hardy space of \(\{r<|z|<1\}\), with **equal normalized measures on the two boundary circles**, and let
\[
C_{\phi,r}=M_{\phi,r}^{*}M_{\phi,r}-M_{\phi,r}M_{\phi,r}^{*}\geq0,
\qquad h=-\log r.
\]
The operator \(C_{\phi,r}\) belongs to every Schatten class \(\mathcal S_p\), \(p>0\), for every fixed \(r\in(0,1)\). Its complete pinching asymptotic is, for every fixed real \(p>0\),
\[
\boxed{\lim_{r\uparrow1}h^{1-2p}\operatorname{Tr}(C_{\phi,r}^{p})
=\frac{\sqrt\pi\,\Gamma(p)}{\Gamma(p+\tfrac12)}
\frac1{2\pi}\int_0^{2\pi}|\phi'(e^{i\theta})|^{2p}\,d\theta.}
\]
In particular, the critical half-Schatten exponent has the geometric limit
\[
\boxed{\lim_{r\uparrow1}\operatorname{Tr}(C_{\phi,r}^{1/2})
=\frac12\int_0^{2\pi}|\phi'(e^{i\theta})|\,d\theta,}
\]
exactly **half the parametrized arclength** of the boundary curve \(\phi(e^{i\theta})\), counting repetitions. For a nonconstant \(\phi\), the \(p\)-th Schatten-power trace tends to zero for \(p>\tfrac12\), has the positive finite limit above for \(p=\tfrac12\), and diverges for \(0<p<\tfrac12\), although \(\|C_{\phi,r}\|\to0\). Moreover,
\[
\boxed{\lim_{r\uparrow1}h^{-2}\|C_{\phi,r}\|
=\max_{|z|=1}|\phi'(z)|^2.}
\]
More generally, for any continuous \(F:[0,\infty)\to\mathbb R\) supported inside \((0,\infty)\),
\[
\boxed{\lim_{r\uparrow1}h\operatorname{Tr}\bigl[F(h^{-2}C_{\phi,r})\bigr]
=\int_{\mathbb R}\frac{dt}{2\pi}\int_0^{2\pi}
F\bigl(\operatorname{sech}^{2}(t)|\phi'(e^{i\theta})|^2\bigr)\,d\theta.}
\]
The latter is a locally finite positive-eigenvalue distribution; it is **not** a claim of a finite total number of eigenvalues.

## Assumptions and scope
The Hilbert space consists of Laurent series \(f(z)=\sum_{n\in\mathbb Z}c_nz^n\) with
\[\|f\|^2=\sum_{n\in\mathbb Z}|c_n|^2(1+r^{2n}).\]
The orthonormal basis is \(e_n=z^n/\sqrt{1+r^{2n}}\). The polynomial \(\phi\), its coefficients, and \(p\) are fixed while \(r\uparrow1\); no degree growth or coefficient dependence on \(r\) is asserted. The exponent \(p\) may be below one, in which case \(\mathcal S_p\) is a quasi-normed ideal. Constant \(\phi\) gives \(C_{\phi,r}=0\) and all limit formulas trivially hold, but the strict three-way phase transition is stated for nonconstant \(\phi\).

## Proof
**1. Exact commutator bands.** Put \(q=r^2=e^{-2h}\) and \(V_n=1+q^n\). For every integer \(k\),
\[M_{z^k}e_n=\sqrt{V_{n+k}/V_n}\,e_{n+k}.\]
The coefficient of \(e_{n+k-l}\) in \([M_{z^l}^{*},M_{z^k}]e_n\) is exactly
\[
B_{n;k,l}=
\frac{q^n(q^k-1)(1-q^{-l})}
{(1+q^{n-l})\sqrt{(1+q^n)(1+q^{n+k-l})}}.
\]
Indeed, the two terms of the commutator have coefficients \(V_{n+k}/\sqrt{V_nV_{n+k-l}}\) and \(\sqrt{V_nV_{n+k-l}}/V_{n-l}\), respectively; subtraction produces \(q^n(q^k-1)(1-q^{-l})\). Therefore \(C_{\phi,r}\) is a self-adjoint matrix with finitely many diagonals, with entry \(\sum_{k-l=s}a_k\overline{a_l}B_{n;k,l}\) at row \(n+s\), column \(n\).

**2. Positivity and trace ideals.** Multiplication by the analytic, bounded Laurent polynomial \(\phi\) leaves the annular Hardy subspace invariant inside \(L^2\) of both circles. Its ambient multiplication is normal. Thus it is subnormal, so \(C_{\phi,r}\geq0\). For every fixed pair \(k,l\), and uniformly for \(0<h\leq1\),
\[|B_{n;k,l}|\leq C_{k,l}h^2\operatorname{sech}^2(hn).\]
This follows from \(|q^k-1|\,|1-q^{-l}|=O(h^2)\) and uniform comparability of the denominator with \((1+q^n)^2\). Because there are finitely many bands and \(\operatorname{sech}(hn)\) decays exponentially, each band lies in every \(\mathcal S_p\), for \(p>0\), as does their sum. In particular the diagonal is summable. The exact trace can be obtained by telescoping the squares of the shift weights within each residue class:
\[
\operatorname{Tr}C_{\phi,r}=\sum_{k\ne0}|a_k|^2 k(1-q^k).
\]
There are no off-diagonal contributions to this trace, and each displayed summand is nonnegative.

**3. Local spectral symbol.** Fix a real \(t\) and integers \(n\) with \(hn\to t\). A second-order expansion of the exact coefficient gives
\[
h^{-2}B_{n;k,l}\longrightarrow kl\operatorname{sech}^2(t).
\]
The expansion is uniform for \(t\) in compact sets (indeed the uniform band error is \(O(h)\) after division by \(h^2\)). Hence the limiting Laurent/Fourier symbol of the band matrix \(h^{-2}C_{\phi,r}\) is
\[
v(t,\theta)=\operatorname{sech}^2(t)\left|\sum_{k=-m}^m ka_ke^{ik\theta}\right|^2
=\operatorname{sech}^2(t)|\phi'(e^{i\theta})|^2.
\]
For any fixed finite spatial window \(|hn|\leq R\), expansion of powers of the finite-band matrix into closed index walks and an ordinary Riemann sum give, for every positive integer \(j\),
\[
\lim_{h\downarrow0}h\operatorname{Tr}\left[(P_{R,h}C_{\phi,r}P_{R,h}/h^2)^j\right]
=\int_{-R}^{R}\frac{dt}{2\pi}\int_0^{2\pi}v(t,\theta)^j\,d\theta,
\]
where \(P_{R,h}\) projects onto the basis indices \(|hn|\leq R\). At most a fixed number of boundary rows are omitted in closed-walk counting, giving a vanishing contribution after multiplication by \(h\). The compressed matrices are positive, have dimension \(O(R/h)\), and are uniformly bounded after division by \(h^2\). Uniform polynomial approximation on their common compact spectral interval therefore extends the statement to every continuous spectral test function, including \(F(x)=x^p\) for any real \(p>0\), on this fixed window.

**4. Infinite tails and Schatten limits.** The exponential coefficient bound and the finite number of bands imply, for each fixed \(p>0\),
\[
\limsup_{h\downarrow0}h^{1-2p}
\|C_{\phi,r}-P_{R,h}C_{\phi,r}P_{R,h}\|_{\mathcal S_p}^{p}
\leq C_{p,\phi}e^{-c_pR}.
\]
To see this, decompose the difference into its finitely many weighted-shift diagonals; the Schatten \(p\)-power sum of each diagonal is the sum of the \(p\)-th powers of its coefficients, and their tails are bounded by an exponentially decaying Riemann sum. Apply the Schatten quasi-triangle inequality when \(0<p\leq1\); for \(p>1\), use the triangle inequality and the uniform normalized \(\mathcal S_p\) bounds. Letting \(R\to\infty\) proves the global \(p\)-power trace limit. The \(t\)-integral is
\[
\int_{\mathbb R}\operatorname{sech}^{2p}(t)\,dt
=B(\tfrac12,p)=\frac{\sqrt\pi\,\Gamma(p)}{\Gamma(p+\tfrac12)}.
\]
The same finite-window and tail argument proves the stated locally finite spectral distribution, whose test functions vanish near zero. The power exponent \(2p-1\) determines the three-way critical transition because the angular integral is positive for nonconstant \(\phi\).

**5. Norm and perimeter.** Let \(D_h\) be diagonal with entries \(\operatorname{sech}^{2}(hn)\), and let \(B\) be the bounded bilateral Laurent convolution operator having Fourier symbol \(|\phi'(e^{i\theta})|^2\). The uniform band expansions show
\[
\|h^{-2}C_{\phi,r}-D_h^{1/2}BD_h^{1/2}\|\longrightarrow0.
\]
The right-hand model has norm at most \(\max_{|z|=1}|\phi'(z)|^2\). Normalized Fourier wave packets of width \(h^{-1/2}\) centered at index zero, oscillating at an angle where \(|\phi'|\) is maximal, give the matching lower bound. At \(p=\tfrac12\), the beta integral equals \(\pi\), and the remaining boundary integral yields half the parametrized curve length.

## Verification
The accompanying standalone script `check_laurent.py` verifies the exact rational numerator identity for 8,967 cases across multiple rational radii, compares the complete nontrivial commutator matrix bands with independently assembled finite matrices, and checks several finite-volume spectral examples. Running `python check_laurent.py` returns `ANNULAR_LAURENT_CHECK_OK 12162`. These finite checks corroborate the algebra and normalization; the infinite-dimensional asymptotics follow from the analytical compact-window and tail arguments, not from numerical extrapolation.

## Relationship to prior work
Jain and Sarkar (2026) study algebraic characterizations and compact perturbations of annular Toeplitz operators. Their normalized Laurent basis is the starting setting here; they do not provide the mixed-symbol self-commutator's pinching spectral Weyl law. Das and Narayanan (2025) analyze zero products and compact Hankel operators on the same Hardy space, not the Schatten asymptotics of analytic multiplication self-commutators. Classical subnormality yields positivity and generic weighted-shift formulas yield individual matrix entries, but neither alone supplies the complete two-variable limiting symbol, universal \(p\)-power constants, nor the boundary-curve perimeter law. The special coordinate symbol \(\phi(z)=z\) is already known and is strictly subsumed by the present theorem; the new content is the full mixed-Laurent-polynomial spectral law, including nontrivial interference between Fourier modes.

## Limitations
The theorem applies to **fixed finite Laurent polynomials** on equal-weight two-boundary annular Hardy spaces. It does not assert the result for arbitrary bounded holomorphic symbols, changing coefficients or degree as \(r\uparrow1\), or other boundary weights. The spectral law is in the locally finite sense away from zero; there are infinitely many eigenvalues for each nonconstant symbol. The present literature check cannot certify global publication priority, and independent mathematical audit has not been performed.

## References
1. S. Jain and J. Sarkar, *Characterizations of Toeplitz operators on the annulus*, arXiv:2610.40118v1, first public 2026-10-29, https://arxiv.org/html/2610.40118v1.
2. S. Das and E. K. Narayanan, *Zero Products of Toeplitz operators on the Hardy and Bergman spaces over an annulus*, arXiv:2504.04270v1, first public 2025-04-05, https://arxiv.org/html/2504.04270v1.
3. J. N. Tattersall, *Toeplitz and Hankel operators on Hardy spaces of complex domains*, doctoral thesis (2015). The accessible introductory and contents portions concern annular Hardy-space operator theory; this work is not claimed as exhaustively inspected.
