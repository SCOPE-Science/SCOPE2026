# Parity-sensitive sharp volume tails of quasiperiodic Stuart–Landau tori

## Finding

For every integer \(N\ge3\), the \(N\)-dimensional quasiperiodic invariant-torus family of the isotropic \(2N\)- or \((2N+1)\)-dimensional Stuart–Landau flow has an exact sampling law for its intrinsic volume. Uniform angular sampling of the initial condition (and, more generally, any nondegenerate spherically symmetric initial distribution) determines the same law. Its *two* geometric tails change sharply with ambient parity.

Let \(\mathcal V\) be the intrinsic \(N\)-dimensional Riemannian volume of the omega-limit torus and set
\[
R=\frac{\mathcal V}{(2\pi)^N(\rho/N)^{N/2}}\in(0,1].
\]
For \(s>-2\), its exact Mellin moments are
\[
\mathbb E[R^s]=N^{Ns/2}\frac{\Gamma(N+\eta)\Gamma(1+s/2)^N}{\Gamma(N+\eta+Ns/2)},\qquad
\eta=\begin{cases}0,&D=2N,\\1/2,&D=2N+1.\end{cases}
\]
These moments are infinite for every real \(s\le-2\). There is also a **finite independent-beta factorization** of the entire volume law:
\[
R^2\stackrel{\rm law}=\prod_{b\in\mathcal B_\eta}B_b,\qquad B_b\text{ independent and }B_b\sim\mathrm{Beta}(1,b),
\]
with \(\mathcal B_0=\{1/N,2/N,\ldots,(N-1)/N\}\) and \(\mathcal B_{1/2}=\{(k+1/2)/N:0\le k<N\}\). As \(r\downarrow0\),
\[
\Pr(R\le r)\sim\begin{cases}
\displaystyle\frac{N(N-1)}{N^N}r^2[2\log(1/r)]^{N-2},&D=2N,\\[5pt]
\displaystyle\frac{\Gamma(N+1/2)}{\sqrt\pi\,(N-1)!N^N}r^2[2\log(1/r)]^{N-1},&D=2N+1.
\end{cases}
\]
At the *opposite* endpoint, writing \(\varepsilon\downarrow0\),
\[
\Pr(R>1-\varepsilon)\sim\begin{cases}
\displaystyle K_{N,0}\varepsilon^{(N-1)/2},&D=2N,\\[3pt]
\displaystyle K_{N,1/2}\varepsilon^{N/2},&D=2N+1,
\end{cases}
\]
where the positive explicit constants are
\[
K_{N,0}=\frac{(N-1)!}{\sqrt N}\left(\frac2N\right)^{N-1}\frac{\pi^{(N-1)/2}}{\Gamma((N+1)/2)},\qquad
K_{N,1/2}=\frac{\Gamma(N+1/2)}{\sqrt N}\left(\frac2N\right)^{N-1/2}\frac{\pi^{(N-1)/2}}{\Gamma(N/2+1)}.
\]
Thus adjoining one stationary coordinate introduces one extra power of logarithm in the small-volume tail and one extra half-power of distance in the near-maximal tail, despite leaving the torus dimension unchanged.

## Assumptions and scope

Fix an integer \(N\ge3\), a scalar \(\rho>0\), and \(D\in\{2N,2N+1\}\). On \(\mathbb R^D\), consider the smooth autonomous system
\[
\dot x=(\rho-\lVert x\rVert^2)x+Ax,
\]
where \(A^\top=-A\), with \(N\) nonzero rotation-block frequencies \(\omega_1,\ldots,\omega_N\) which are rationally independent over the integers. For odd \(D\), require a one-dimensional kernel of \(A\). These conditions make a generic positive-mode orbit dense in its product torus. Let \(x(0)\) have any spherically symmetric law on \(\mathbb R^D\) with \(\Pr(x(0)=0)=0\); no radial density, moment, or boundedness assumption is required. The exceptional initial directions with zero paired-mode amplitude have probability zero. All volumes are intrinsic, measured in the Euclidean metric induced from \(\mathbb R^D\); they are not the ambient volume of the attractor (which is zero).

The maximum used to normalize \(R\) is the supremum of the intrinsic torus volume at fixed \(\rho\). In odd dimension it is attained only if the unpaired coordinate vanishes; this event has angular measure zero. All limits have fixed \(N\) and fixed \(\rho\). The result makes no assertion about commensurate frequencies, nonspherical sampling, perturbations destroying the integrable mode decomposition, or uniqueness of an ergodic stationary measure on the whole sphere.

## Proof

**1. Dynamics and geometrical reduction.** Orthogonal conjugation turns \(A\) into \(N\) planar rotation blocks and, when \(D\) is odd, a zero block. Denote the paired complex coordinates by \(z_j\). Orthogonality gives \(\frac{d}{dt}\lVert x\rVert^2=2(\rho-\lVert x\rVert^2)\lVert x\rVert^2\). For every nonzero initial state, its squared radius tends to \(\rho\), while \(\dot z_j=((\rho-\lVert x\rVert^2)+i\omega_j)z_j\). Therefore the asymptotic radius in the \(j\)-th block is
\[
a_j=\sqrt\rho\frac{|z_j(0)|}{\lVert x(0)\rVert}.
\]
Rational independence of the frequencies implies that the omega-limit set is the full embedded flat product torus with circle radii \(a_j\). Its induced Riemannian metric in angle coordinates is \(\operatorname{diag}(a_1^2,\ldots,a_N^2)\), hence
\[
\mathcal V=(2\pi)^N\prod_{j=1}^N a_j=(2\pi)^N\rho^{N/2}\sqrt{\prod_{j=1}^N U_j},
\quad U_j=\frac{|z_j(0)|^2}{\lVert x(0)\rVert^2}.
\]
The arithmetic–geometric mean inequality, and \(\sum U_j\le1\), yield the claimed normalization and \(R=N^{N/2}(\prod U_j)^{1/2}\).

**2. Distribution of mode energies and exact moments.** A spherically symmetric direction is uniform on the unit sphere, hence representable by independent standard Gaussian coordinates divided by their Euclidean norm. The \(N\) squared norms of two-dimensional Gaussian blocks are independent Gamma random variables of shape \(1\) and common scale; in odd dimension the extra squared scalar has shape \(1/2\). Thus
\[
(U_1,\ldots,U_N)\sim\mathrm{Dirichlet}(1,\ldots,1)
\quad (D=2N),
\]
while in odd dimension \((U_1,\ldots,U_N,U_0)\sim\mathrm{Dirichlet}(1,\ldots,1,1/2)\). The standard Dirichlet integral (evaluated by independent gamma variables and a change to their sum) gives
\[
\mathbb E\left[\prod_{j=1}^N U_j^{s/2}\right]
=\frac{\Gamma(N+\eta)\Gamma(1+s/2)^N}{\Gamma(N+\eta+Ns/2)}.
\]
This is finite precisely when each shape parameter plus \(s/2\) is positive, i.e. \(s>-2\). At and below this threshold any one paired coordinate approaching zero makes the nonnegative integral diverge.

Gauss's gamma multiplication identity also proves the stronger independent-beta factorization stated above. Indeed, for \(t\ge0\), the gamma ratio for \(\mathbb E[R^{2t}]\) equals \(\prod_{b\in\mathcal B_\eta}\Gamma(1+t)\Gamma(1+b)/\Gamma(1+t+b)\). (For \(\eta=0\), the extra gamma factor at \(b=0\) cancels.) These are exactly the product moments of independent \(\mathrm{Beta}(1,b)\) variables. Uniqueness of moments for probability measures on \([0,1]\) yields equality in distribution. This factorization will also give an elementary route to the two endpoint constants.

**3. Sharp lower endpoint.** Set \(W=\prod_{j=1}^N U_j\), so \(R^2=N^N W\). For complex \(z\) with \(0<\Re z<1\),
\[
M_\eta(z)=\mathbb E[W^{-z}]
=\frac{\Gamma(N+\eta)\Gamma(1-z)^N}{\Gamma(N+\eta-Nz)}.
\]
Mellin–Perron inversion for the continuous distribution of \(W\) gives
\[
\Pr(W\le w)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
\frac{w^z M_\eta(z)}z\,dz,\qquad 0<c<1.
\]
The gamma quotient, divided by \(z\), decreases vertically at least as \(|\Im z|^{-(N+1)/2-\eta}\) on fixed vertical lines avoiding its poles (by Stirling's formula). For \(N\ge3\), this is integrable, so the contour may be shifted to \(\Re z=1+\theta\), for any fixed \(0<\theta<1\), crossing only the pole at \(z=1\). In even dimension \(1/\Gamma(N(1-z))\sim N(1-z)\); hence this pole has order \(N-1\) and leading coefficient \(N\Gamma(N)\). In odd dimension the denominator instead tends to \(\Gamma(1/2)\), so it has order \(N\) and leading coefficient \(\Gamma(N+1/2)/\Gamma(1/2)\). Computing the residues, including the sign of the rightward contour shift, yields
\[
\Pr(W\le w)=\begin{cases}
\displaystyle N(N-1)w[\log(1/w)]^{N-2}(1+o(1)),&\eta=0,\\[3pt]
\displaystyle\frac{\Gamma(N+1/2)}{\sqrt\pi\,(N-1)!}w[\log(1/w)]^{N-1}(1+o(1)),&\eta=1/2.
\end{cases}
\]
The shifted contour is \(O(w^{1+\theta})\); lower terms in each residue polynomial have one less power of logarithm. Substituting \(w=r^2/N^N\) establishes both lower-tail formulas.

There is an independent *real-variable check* using the beta factorization. If \(B\sim\mathrm{Beta}(1,b)\), then the density of \(Y=-\log B\) is \(b e^{-y}(1-e^{-y})^{b-1}\), which is asymptotic to \(b e^{-y}\) as \(y\to\infty\). Convolving \(m\) such densities gives \(\Pr(\sum Y_j\ge t)\sim(\prod b_j)e^{-t}t^{m-1}/(m-1)!\), because each rescaled convolution kernel approaches its finite limiting value in the interior, and its integrable endpoint singularities contribute lower order. Here \(m=N-1\) for even \(D\) and \(m=N\) for odd \(D\). The products of beta parameters are \((N-1)!/N^{N-1}\) and \(\Gamma(N+1/2)/(\sqrt\pi N^N)\), respectively. With \(\sum Y_j=-2\log R\), these independently reproduce the same sharp lower tails.

**4. Sharp upper endpoint, even dimension.** Since \(U_N=1-\sum_{j=1}^{N-1}U_j\), write \(U_j=1/N+v_j\), \(v_N=-\sum_{j=1}^{N-1}v_j\). In a neighborhood of the unique volume maximizer,
\[
1-R=\frac{N^2}{4}\left(\sum_{j=1}^{N-1}v_j^2+
\left(\sum_{j=1}^{N-1}v_j\right)^2\right)+O(\lVert v\rVert^3).
\]
The \((N-1)\)-dimensional Dirichlet simplex has constant density \((N-1)!\). The quadratic form in parentheses has Gram matrix \(I+\mathbf1\mathbf1^\top\) and determinant \(N\). The ellipsoid-volume formula, with the uniform Taylor error, yields
\[
\Pr(R>1-\varepsilon)\sim
\frac{(N-1)!}{\sqrt N}\frac{\pi^{(N-1)/2}}{\Gamma((N+1)/2)}
\left(\frac{2}{N}\right)^{N-1}\varepsilon^{(N-1)/2}.
\]

**5. Sharp upper endpoint, odd dimension.** Let \(B=U_0\). The Dirichlet aggregation identity gives independent variables \(B\sim\mathrm{Beta}(1/2,N)\) and \((U_1,\ldots,U_N)/(1-B)\sim\mathrm{Dirichlet}(1,\ldots,1)\). Thus \(R=(1-B)^{N/2}R_{\rm even}\). Near \(B=0\) its density is
\[
\frac{\Gamma(N+1/2)}{\Gamma(1/2)\Gamma(N)}B^{-1/2}(1+O(B)).
\]
Since \(1-R=(N/2)B+(1-R_{\rm even})+o(B+1-R_{\rm even})\), integrate the even-dimensional endpoint law against this beta density. Dominated rescaling \(B=2\varepsilon t/N\) gives the additional factor
\[
\frac{\Gamma(N+1/2)}{\Gamma(1/2)\Gamma(N)}
\sqrt{\frac2N}\,\mathrm B\left(\frac12,\frac{N+1}{2}\right)
\]
and an additional \(\varepsilon^{1/2}\). Simplifying the beta and gamma factors gives \(K_{N,1/2}\). The independent-beta factorization provides an additional joint check of both upper constants: the density of \(Y=-\log B\) is \(b y^{b-1}(1+O(y))\) near zero. Its independent sum has lower-tail coefficient \(\prod_b\Gamma(1+b)/\Gamma(1+\sum b)\), and \(-2\log R\sim2(1-R)\). Therefore \(\Pr(R>1-\varepsilon)\sim 2^{\sum b}\prod_b\Gamma(1+b)/\Gamma(1+\sum b)\,\varepsilon^{\sum b}\). Multiplication of the gamma factors recovers exactly \(K_{N,0}\) and \(K_{N,1/2}\), with \(\sum b=(N-1)/2\) or \(N/2\). This completes the proof.

## Verification

A standalone Python script `verify_torus_volume.py` checks the gamma formulas and exact special-case constants, samples isotropic Gaussian directions in dimensions \(6,7,8,9\), compares their empirical normalized-volume moments against the exact Mellin moments, and spot-checks finite-threshold survival probabilities against the leading upper-tail approximations. Run with `python3 verify_torus_volume.py` using only the Python standard library. The run ended with `TORUS_VOLUME_CHECK_OK`. Monte Carlo is a consistency check, not proof of the limiting asymptotics; the latter are established above by contour inversion and local simplex geometry.

## Relationship to prior work

Gogoi, Ghosh, Ghoshal, Prasad, and Ramaswamy (2024, DOI below) establish the solvable higher-dimensional Stuart–Landau flow, the normal-mode decomposition, the cone basins, and the continuum of asymptotic tori. Those dynamical facts are used here, not re-claimed. Their complete openly available author version (arXiv:2511.05160, posted in 2025) was inspected through the main derivation, torus discussion, and concluding sections; it does not provide the isotropic-sampling intrinsic-volume law, both endpoint constants, or the ambient-parity comparison.

Nadarajah and Kotz (2004) explicitly derive the product distribution of *two* Dirichlet components with hypergeometric functions. Springer and Thompson (1970) derive general independent-beta-product densities via Meijer G functions. These works, together with the classical Dirichlet moment integral, are relevant prior probability theory and supply general distribution machinery; we do **not** claim the general beta-product law as new. The present theorem is restricted to \(N\ge3\) and concerns the dynamically defined *\(N\)-factor* torus volume with simultaneous sharp endpoints and distinct even/odd ambient geometries. Mellin inversion, gamma multiplication, and beta-product asymptotics are standard machinery; only the geometric identification of this volume statistic and its specific parity-sensitive sharp tail constants are asserted here, subject to the literature-coverage limitation below.

## Limitations

This is a mathematical statement for a specified integrable oscillator and isotropic initial-direction sampling. Its source's qualitative torus structure is not new; the Dirichlet moment identity and Mellin residue methods are classical. The result has not been independently audited; unindexed literature on arbitrary products of Dirichlet components or other equivalent torus-volume models could contain the stated endpoint asymptotics. Springer and Thompson's full 1970 text was not accessible, so explicit general beta-product asymptotics appearing there could already imply the probabilistic endpoint coefficients. The source paper's journal publication date is used as the earliest *verified* public date; the freely accessible author version is dated later. The claim does not extend to arbitrary skew matrices with frequency resonances, nor to non-isotropic initial directions.

## References

1. P. Bhuyan Gogoi, R. Ghosh, D. Ghoshal, A. Prasad, and R. Ramaswamy, "Exactly solvable Stuart–Landau models in arbitrary dimensions," *Physical Review E* **110**, L032202, published September 25, 2024. DOI: https://doi.org/10.1103/PhysRevE.110.L032202. Author-version full text: https://arxiv.org/abs/2511.05160 (posted November 7, 2025).
2. S. Nadarajah and S. Kotz, "Exact and approximate distributions for the product of Dirichlet components," *Kybernetika* **40** (2004), 735–744. Full text: https://www.kybernetika.cz/content/2004/6/735/paper.pdf.
3. M. D. Springer and W. E. Thompson, "The distribution of products of beta, gamma and Gaussian random variables," *SIAM Journal on Applied Mathematics* **18** (1970), 721–737. DOI: https://doi.org/10.1137/0118065. Only the publisher abstract was accessible.
4. Classical Dirichlet–gamma normalizations, Euler beta integral, gamma multiplication, Stirling's formula, and Mellin inversion: standard tools used explicitly in the proof.
