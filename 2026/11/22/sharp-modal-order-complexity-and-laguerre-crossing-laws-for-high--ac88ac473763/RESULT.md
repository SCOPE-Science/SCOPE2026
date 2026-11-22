# Sharp modal-order complexity and Laguerre crossing laws for higher Landau disk concentration

## Finding
For each integer \(q\ge3\), let \(\lambda_{q,k}(x)\), \(k\ge0\), be the centered-disk concentration eigenvalues in the pure order-\(q\) polyanalytic Gaussian Fock space, with squared disk radius \(x>0\). Put \(A_{q,k}(x)=L_q^{(k-q)}(x)\), with the generalized Laguerre polynomial defined by its finite binomial sum even when \(k<q\). Then the **exact neighboring-mode difference**, for every \(k\ge0\), is
\[
\lambda_{q,k+1}(x)-\lambda_{q,k}(x)
=-\frac{q!}{(k+1)!}e^{-x}x^{k-q+1}A_{q,k}(x)A_{q,k+1}(x).
\]
Consequently, the two adjacent concentration curves exchange strict order at exactly \(2k+1\) distinct, simple positive squared radii if \(0\le k<q\), and at exactly \(2q\) distinct, simple positive squared radii if \(k\ge q\). Every crossing reverses the order, with no other positive-radius ties.

At each fixed \(x>0\), there are **at most \(q\) strict ascending Hermite-index steps** \(\lambda_{q,k+1}(x)>\lambda_{q,k}(x)\), and hence at most \(q+1\) local-maximum plateaux in the entire infinite spectrum. Both bounds are sharp: for every sufficiently large \(x\), except radii satisfying \(A_{q,k}(x)=0\) for an integer \(k\ge0\), there are exactly \(q\) ascending steps, isolated by descending steps, and exactly \(q+1\) strict local maxima. The \(q\) real roots \(\kappa_j(x)\) of the degree-\(q\) index polynomial \(k\mapsto A_{q,k}(x)\), in increasing order, obey
\[
\kappa_j(x)=x+\xi_j\sqrt{x}+o_q(\sqrt{x})\qquad(x\to\infty),
\]
where \(\xi_1<\cdots<\xi_q\) are the distinct zeros of the probabilists' Hermite polynomial \(\operatorname{He}_q\). For each \(x>0\) the index polynomial has \(q\) simple positive real roots, and a strict upward spectral step can occur only across a unit interval containing a root. The fixed orders \(q=0,1,2\) are included in the identity as contextual special cases but are not separately claimed as new results.

## Assumptions and scope
Work in \(L^2(\mathbb C,\pi^{-1}e^{-|z|^2}dA)\), and let \(\mathcal F_{(q+1)}\) be the pure true-polyanalytic Fock space of antiholomorphic order exactly \(q\), spanned by normalized complex Hermite functions \(\Phi_{q,k}\), \(k=0,1,\ldots\). Let \(T_{q,x}=P_{q}\mathbf1_{\{|z|^2\le x\}}P_{q}\), restricted to this space. Polar symmetry makes \(T_{q,x}\Phi_{q,k}=\lambda_{q,k}(x)\Phi_{q,k}\). Its eigenvalue is the known exact Laguerre integral
\[
\lambda_{q,k}(x)=\frac{q!}{k!}\int_0^x e^{-t}t^{k-q}[L_q^{(k-q)}(t)]^2\,dt
=\frac{\min(q,k)!}{\max(q,k)!}\int_0^x e^{-t}t^{|k-q|}[L_{\min(q,k)}^{(|k-q|)}(t)]^2dt.
\]
The first integrand has removable apparent negative powers for \(k<q\). We use \(L_q^{(k-q)}(t)=\sum_{s=0}^q(-1)^s\binom{k}{q-s}t^s/s!\), with generalized binomial coefficients and integer \(k\ge0\). The word *crossing* refers to zeros of the neighboring eigenvalue difference as a function of \(x>0\). A *strict ascending step* refers to an integer \(k\ge0\) for which the difference is positive at a fixed \(x\). The claim about maxima refers to maximal constant-value runs with nonincreasing neighbors and excludes infinite-tail limits, since \(\lambda_{q,k}(x)\to0\) as \(k\to\infty\) at each fixed \(x\).

## Proof
**1. Differential factorization.** Fix integers \(q,k\ge0\), put \(A=L_q^{(k-q)}\), \(B=L_q^{(k-q+1)}\). Standard contiguous Laguerre relations, valid also for nonpositive integer parameters by their polynomial definitions, give
\[
A'=A-B,\qquad xB'=(k+1)A-(k-q+1)B.
\]
Direct differentiation therefore yields the exact identity
\[
\frac{d}{dx}\bigl[e^{-x}x^{k-q+1}AB\bigr]
=e^{-x}x^{k-q}\bigl[(k+1)A^2-xB^2\bigr].
\]
Multiplying by \(-q!/(k+1)!\), the derivative is exactly the difference of the two Laguerre-integral densities in the assumptions. The boundary expression tends to zero as \(x\downarrow0\): for \(k\ge q\), its exponent is positive, while for \(k<q\), use \(L_q^{(-p)}(x)=(-x)^p(q-p)!L_{q-p}^{(p)}(x)/q!\) for \(1\le p\le q\), showing sufficient cancellation. Thus integration from zero proves the claimed exact neighboring-mode formula without an integration constant.

**2. Exact number and simplicity of radial crossings.** For \(k\ge q\), each factor is a degree-\(q\) generalized Laguerre polynomial with parameter respectively \(k-q\) and \(k-q+1\), so each has \(q\) distinct simple positive zeros. For \(k<q\), the same negative-parameter reduction shows that \(A\) has \(k\) simple positive zeros and a separate root at zero of order \(q-k\); \(B\) has \(k+1\) simple positive zeros and a separate root at zero of order \(q-k-1\). In every case there are no shared positive zeros: if \(A(x_0)=B(x_0)=0\) with \(x_0>0\), the displayed first-order linear differential system for \((A,B)\) would have identically zero solution by local uniqueness, contradicting the nonzero polynomials. Hence their product has exactly \(2q\), or \(2k+1\), **distinct simple** positive roots. The scalar factor in the neighboring-difference identity is strictly negative on \(x>0\), so each root gives a genuine sign-changing crossing and the enumeration is exhaustive.

**3. An exact Poisson orthogonality for the index polynomial.** Fix \(x>0\) and extend the index to a real variable \(y\). The polynomial \(F_q(y;x)=L_q^{(y-q)}(x)\) is the coefficient of \(t^q\) in \((1+t)^ye^{-xt}\), of degree \(q\) with positive leading coefficient \(1/q!\). Using the positive Poisson weights \(w_x(k)=e^{-x}x^k/k!\), the generating functions satisfy
\[
\sum_{k=0}^\infty w_x(k)(1+s)^k e^{-xs}(1+t)^k e^{-xt}=e^{xst}.
\]
Comparing coefficients gives \(\sum_{k=0}^{\infty}w_x(k)F_p(k;x)F_q(k;x)=\delta_{pq}x^q/q!\). Thus \(F_q\) is the degree-\(q\) orthogonal polynomial for an infinite-support positive measure on \(\{0,1,\ldots\}\). The standard elementary zero argument for orthogonal polynomials gives exactly \(q\) distinct simple roots on \((0,\infty)\): fewer sign changes on the convex hull would produce a lower-degree sign polynomial whose product with \(F_q\) is nonnegative on the support, contradicting orthogonality. This last argument also excludes a root at zero by the positive atom there.

**4. Optimal number of spectral ascents.** The gap factorization says a strict ascent at \(k\) requires \(F_q(k;x)F_q(k+1;x)<0\), hence at least one real root of \(F_q(\cdot;x)\) in the open unit interval \((k,k+1)\). These intervals are disjoint, so there can be at most \(q\) ascents. Every maximal local-maximum plateau after index zero must be preceded by at least one ascent; therefore there are at most \(q+1\) such plateaux, with or without index ties.

**5. Sharpness and Gaussian index-root asymptotics.** Set \(y=x+u\sqrt{x}\) and \(t=v/\sqrt{x}\) in the generating function for \(F_q\). Uniformly for bounded complex \(u,v\),
\[
(1+v/\sqrt{x})^{x+u\sqrt{x}}e^{-v\sqrt{x}}
\longrightarrow e^{uv-v^2/2}.
\]
Coefficient comparison for fixed \(q\) shows \(x^{-q/2}F_q(x+u\sqrt{x};x)\to \operatorname{He}_q(u)/q!\) locally uniformly. The \(q\) distinct real Hermite roots are stable under this coefficientwise convergence. Therefore the index roots satisfy the asserted asymptotics and become separated by more than one unit for all sufficiently large \(x\), while all lie to the right of zero. Outside the (countable) set of radii where an index root is an integer, each falls into a different integer unit interval and causes one strict ascent. Every intervening step is strictly descending; the sequence begins with descending steps and eventually descends to zero. Hence there are exactly \(q\) ascents and \(q+1\) strict local maxima. This proves sharpness.

## Verification
The accompanying standalone `verify_laguerre.py` checks 452 assertions: exact neighboring-gap derivative identities and both contiguous relations for \(0\le q\le7\), \(0\le k\le12\), the negative-parameter cancellations and positive-root count for each finite tested case, and high-area index-root separation with Hermite scaling for \(1\le q\le7\). Running `python verify_laguerre.py` with SymPy and SciPy prints `LANDAU_LAGUERRE_PASS checks=452`. The all-index crossing count and sharp all-level ascent bound are consequences of the proof, not of numerical sampling.

## Relationship to prior work
Abreu, Gröchenig and Romero (2017/2019), especially their Section 4.2, Lemma 4.2 and Remark 4.3, establish Hermite-mode disk localization and the spectral Laguerre integral, and note a first-window crossing without an all-level crossing census or a uniform mode-ascent bound. Maximenko and Tellería-Romero (2019) give the diagonal radial Toeplitz/Laguerre basis and operator framework, not the all-level neighboring difference classification. Mouayn, Mahboubi and El Moize (2023), Appendix B and Eq. (5.12), give precisely the polyanalytic Ginibre disk eigenvalues, mean and variance; their incomplete-gamma expansions are not an implication of an exact neighboring-mode crossing census or a sharp global bound on index ascents.

For comparison, the known explicit first- and second-excited-window calculations yield neighboring differences and spectral transitions for \(q=1,2\), including exceptional triple plateaux and the special pronic areas in order two. These are recognized special cases, not separately presented as new findings. A related Jacobi/Zernike single-mode theorem yields \(2q\)-type crossing counts but for a different radial weight and for changing angular order; it does not imply the Gaussian Laguerre factorization, the Poisson-orthogonal *index* root theorem, or the sharp \(q\) spectral ascent bound. No checked source provides a dominating all-\(q\ge3\) result. Historical priority remains best-knowledge rather than independently certified.

## Limitations
The disk is centered, the Gaussian magnetic-field normalization is fixed, and each eigenvalue is indexed by the Hermite basis; arbitrary masks, mixed Landau levels, full rankings by decreasing eigenvalue, and exact nonadjacent spectral coincidences are outside the theorem. It does not determine the top eigenvalue's maximizing index at each finite radius, although it bounds the number of local maxima. The classical Laguerre identities and Charlier/Poisson orthogonality are mathematical ingredients rather than original discoveries. The main new contribution asserted is their complete, sharp application to all higher pure Landau disk spectral crossings and ascent complexity. Published historical coverage may be incomplete.

## References
1. L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic Analysis in Phase Space and Finite Weyl-Heisenberg Ensembles*, arXiv:1704.03042, first posted 10 April 2017; J. Stat. Phys. 174 (2019), 1104–1136. https://arxiv.org/html/1704.03042v3 ; especially Section 4.2, Lemma 4.2, Remark 4.3.
2. E. A. Maximenko and A. M. Tellería-Romero, *Radial Operators on Polyanalytic Bargmann–Segal–Fock Spaces*, arXiv:1905.00978, first posted 2 May 2019. https://arxiv.org/html/1905.00978v2 ; especially Section 2 and radial-operator sections.
3. Z. Mouayn, M. Mahboubi, O. El Moize, *Mean and Variance of the Cardinality of Particles in Polyanalytic Ginibre Processes via a Quantization Method*, arXiv:2305.04354, first posted 7 May 2023. https://arxiv.org/abs/2305.04354 ; especially Eq. (5.12), Section 6, Appendix B.
4. Classical generalized Laguerre zeros, recurrence and Charlier orthogonality: G. Szegő, *Orthogonal Polynomials*, 4th edition, American Mathematical Society, 1975.
