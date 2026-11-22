# A degree-fifteen jump transition and sharp squared-error asymptotics for Bernstein sampling

## Finding
For every integer \(n\ge1\), let the classical Bernstein operator be
\[
(B_nf)(x)=\sum_{i=0}^{n}\binom ni x^i(1-x)^{n-i}f(i/n).
\]
Take real right-continuous Jordan bounded-variation functions on \([0,1)\), with a finite independently specified value at \(1\), and let \(\operatorname{Var}(f)\) be their ordinary pointwise total variation on \([0,1]\). The sharp norm
\[
C_n=\sup_{\operatorname{Var}(f)>0}
\frac{\|B_nf-f\|_{L^2(0,1)}}{\operatorname{Var}(f)}
\]
admits an **exact finite rational formula**. For \(0\le j\le n+1\), set
\[
F_{n,j}(x)=\sum_{i=j}^n\binom ni x^i(1-x)^{n-i},\qquad F_{n,0}=1,\quad F_{n,n+1}=0.
\]
For \(0\le k\le n\), \(j\in\{k,k+1\}\), set
\[
D_n(k,j)=\int_0^{k/n}F_{n,j}(x)^2\,dx
       +\int_{k/n}^1(1-F_{n,j}(x))^2\,dx.
\]
Then
\[
\boxed{C_n^2=\max_{0\le k\le n\atop j\in\{k,k+1\}}D_n(k,j).}\tag{1}
\]
All entries in this maximum are rational and explicitly computable with integer arithmetic. The endpoint candidate is \(D_n(n,n)=D_n(0,1)=1/(2n+1)\). Exact exhaustive rational comparison gives
\[
\boxed{C_n^2=\frac1{2n+1}\quad(1\le n\le14),}\tag{2}
\]
where all interior grid-boundary candidates are strictly smaller; the first degree at which an interior jump gives a strictly larger error is \(n=15\), with
\[
\boxed{C_{15}^2=\frac{7885956840965217}{239784545898437500}
>\frac1{31}.}\tag{3}
\]
At degree 15 the only maximizing one-sided grid-boundary traces are \((k,j)=(6,7)\) and \((9,9)\); the latter is attained by the right-continuous step \(f=\mathbf1_{[3/5,1]}\). No assertion is made that an interior maximizer persists at every degree above 15.

For large degree the exact sharp asymptotic and location of all asymptotically maximizing jumps are
\[
\boxed{\lim_{n\to\infty} n^{1/4}C_n
=\left(\frac{\sqrt2-1}{2\sqrt\pi}\right)^{1/2}
=0.341829619295\ldots.}\tag{4}
\]
For any sequence of jump positions \(t_n\in(0,1]\) whose squared errors equal the maximum in (1), or differ from it by \(o(n^{-1/2})\), one has \(t_n\to1/2\). In particular, endpoint impulses dominate the finite degrees through 14, whereas central interior jumps control the high-degree asymptotic.

## Assumptions and scope
The operator acts on **pointwise** Jordan-BV representatives, not on equivalence classes modulo almost-everywhere equality: sampling \(f(i/n)\) requires a representative. Right continuity is required at each point strictly below 1, and a jump at 1 is permitted. Thus \(\mathbf1_{\{1\}}\) is admissible and its squared Bernstein error is \(1/(2n+1)\). The output norm is Lebesgue \(L^2(0,1)\); the input seminorm is ordinary pointwise total variation. At a grid boundary we distinguish its left and right limiting step location since they have different sampled values. No general continuous-function supremum is asserted to be attained at its endpoint.

## Proof
**1. Reduction to a single jump.** For a right-continuous BV function there is a unique finite signed Stieltjes measure \(\mu\) on \((0,1]\) with \(f(x)=f(0)+\int_{(0,1]}\mathbf1_{[t,1]}(x)\,d\mu(t)\) and \(|\mu|((0,1])=\operatorname{Var}(f)\). As \(B_n\) reproduces constants, linearity, Fubini and the triangle inequality in \(L^2\) give
\[
\|B_nf-f\|_2\le\int_{(0,1]}
\|B_n\mathbf1_{[t,1]}-\mathbf1_{[t,1]}\|_2\,d|\mu|(t)
\le\operatorname{Var}(f)\sup_{t\in(0,1]}E_n(t),
\]
where \(E_n(t)\) is the \(L^2\) error of the single step. Conversely single steps have variation 1, so equality holds for the supremum.

**2. No hidden continuous optimization.** If \(t\in((j-1)/n,j/n)\), \(B_n\mathbf1_{[t,1]}=F_{n,j}\), independent of \(t\). Thus
\[
E_n(t)^2=\int_0^t F_{n,j}(x)^2\,dx+
\int_t^1(1-F_{n,j}(x))^2\,dx,
\qquad\frac{d}{dt}E_n(t)^2=2F_{n,j}(t)-1.
\]
The binomial tail \(F_{n,j}\) is nondecreasing, so \(E_n(t)^2\) is convex within every open sampling cell. Its supremum occurs at a one-sided endpoint limit. For \(t=k/n\), the sampled step has threshold \(j=k\), while the right-hand limit has \(j=k+1\). This proves (1), including the end-cell limits and the actual jump at 1.

**3. Exact finite comparisons.** For \(1\le j\le n\), the polynomial has coefficients
\[
F_{n,j}(x)=\sum_{r=j}^n a_r x^r,\qquad
 a_r=(-1)^{r-j}\binom nr\binom{r-1}{j-1}.
\]
Set \(a_0=1\) and all other coefficients zero when \(j=0\), and set all coefficients zero for \(j=n+1\). Then, with \(s=k/n\), every entry in (1) equals the rational expression
\[
D_n(k,j)=\sum_{r,q}\frac{a_ra_q}{r+q+1}
-2\sum_r\frac{a_r(1-s^{r+1})}{r+1}+1-s.\tag{5}
\]
The standalone `check.py` independently expands each binomial tail, computes (5) using Python integer fractions, and exhaustively verifies the inequalities for \(1\le n\le14\), strictness of all interior traces, and the exact two-way degree-15 maximum and value (3). There are no floating-point steps in this finite certificate.

**4. Interior Gaussian profile.** Let \(t_n\to t\in(0,1)\), with sampling threshold integer \(j_n\) satisfying \(|j_n/n-t_n|\le1/n\). Write \(\sigma_n=\sqrt{t_n(1-t_n)/n}\) and \(x=t_n+\sigma_nz\). The binomial central limit theorem with its threshold shift of at most one grid cell gives
\[
F_{n,j_n}(t_n+\sigma_nz)\longrightarrow\Phi(z)
\]
for every fixed real \(z\), where \(\Phi\) is the standard normal CDF. Binomial concentration bounds make the squared integrands uniformly integrable in \(z\) on each compact subinterval of \((0,1)\) for \(t_n\), so
\[
\frac{E_n(t_n)^2}{\sigma_n}\longrightarrow
I:=\int_{\mathbb R}(\Phi(z)-\mathbf1_{\{z\ge0\}})^2dz
=2\int_0^\infty(1-\Phi(z))^2dz
=\frac{\sqrt2-1}{\sqrt\pi}.\tag{6}
\]
The integral follows by integration by parts and \(\int_0^\infty\phi(z)^2dz=1/(4\sqrt\pi)\), with \(\phi\) the standard normal density.

**5. Uniform boundary control and global maximum.** Uniformly for \(t\in(0,1)\) and any threshold differing from \(nt\) by at most 1, the one-sided binomial concentration/variance inequality gives
\[
E_n(t)^2\le C\left(\sqrt{\frac{t(1-t)}n}+\frac1n\right).\tag{7}
\]
For completeness, when \(t\le1/2\), apply \(\Pr(|S_{n,x}-nx|\ge n|x-t|-1)\le\min\{1,nx(1-x)/(n|x-t|-1)^2\}\) wherever the denominator is positive. On \(x\le2t+4/n\), integrate its square, splitting at distance \(\sqrt{t/n}+1/n\) from \(t\); this contributes \(O(\sqrt{t/n}+1/n)\). On \(x>2t+4/n\), \(|x-t|-1/n\ge x/4\), so the squared probability is at most \(O((nx)^{-2})\), integrating to \(O(1/n)\). The case \(t\ge1/2\) follows by reflection. This establishes (7) with an absolute constant. Consequently, if \(t_n\to0\) or \(1\), then \(\sqrt nE_n(t_n)^2\to0\). The same holds for the one-sided traces at the grid boundaries, using a limiting \(t\) and the same threshold condition. On the other hand (6) implies \(\sqrt nE_n(1/2)^2\to I/2>0\). Compactness of the jump-position interval, (6), (7), and \(\sqrt{t(1-t)}\le1/2\) therefore prove \(\sqrt n C_n^2\to I/2\), with all asymptotically maximizing locations tending to 1/2. Taking square roots proves (4).

## Verification
Running `python3 check.py` on Python 3 with no third-party packages verifies 618 exact-rational assertions, including an independent coefficient identity, all finite boundary candidates in degrees 1 through 15, and the unique maximum pair of one-sided traces at degree 15. The infinite-dimensional jump reduction and the limit (4) are supplied analytically, not inferred from those tests. A separate numerical evaluation of beta/binomial tails for degrees up to 60 was used as an exploratory cross-check; these numbers are not needed by the proof.

## Relationship to prior work
Gzyl and Palacios (2003) give the probabilistic Bernstein representation of a discontinuous step and pointwise no-Gibbs behavior. Guan's preprint (first public 3 September 2009) studies classical and iterated Bernstein approximations chiefly for continuous inputs. Bustamante, García-Muñoz and Quesada (2014) give rates for discontinuous functions, but their plausible full text was not accessible during this comparison; only the abstract and the later citation to their theorem were inspected. Adell, Garrancho and Martínez-Sánchez (arXiv 2024, later 2025 journal publication) study local pointwise BV jump estimates; their accessible full HTML, particularly Sections 1 and 5, concerns pointwise bounds rather than sharp integrated squared-error constants. None of these inspected materials establishes (1)–(4). Classical binomial CLT and variation measure decomposition are used as standard inputs, not claimed as new. An existing sharp \(L^1\) Bernstein BV error formula does not imply an exact \(L^2\) operator norm or a degree-15 crossover. The precise priority claim remains subject to further specialist literature review.

## Limitations
The first interior crossover is proved exactly for degrees through 15; no complete classification of maximizing integer indices for all higher degrees is claimed. The constants concern Lebesgue \(L^2\) error and pointwise right-continuous Jordan BV, not arbitrary representatives or operator action on \(BV\) equivalence classes. Formula (4) does not furnish a convergence-rate remainder. The 2014 directly relevant full text could not be inspected, so an equivalent theorem there is an unresolved historical-priority risk. The 2003 article is dated by year in the inspected accessible material, but no exact first-public calendar day was verified for that earlier publication; the dated archival anchor is the verifiable first arXiv version of Guan (3 September 2009).

## References
1. H. Gzyl and J. L. Palacios, *On the Approximation Properties of Bernstein Polynomials via Probabilistic Tools*, Boletín de la Asociación Matemática Venezolana X (2003), 5–11. https://www.researchgate.net/publication/28075947_On_the_Approximation_Properties_of_Bernstein_Polynomials_via_Probabilistic_Tools
2. Z. Guan, *Iterated Bernstein polynomial approximations*, arXiv:0909.0684v1 (3 September 2009), https://arxiv.org/abs/0909.0684
3. J. Bustamante, M. A. García-Muñoz and J. M. Quesada, *Bernstein polynomial and discontinuous functions*, J. Math. Anal. Appl. 411 (2014), 829–837, https://doi.org/10.1016/j.jmaa.2013.10.024
4. J. A. Adell, P. Garrancho and F. J. Martínez-Sánchez, *Approximation of discontinuous functions by positive linear operators: A probabilistic approach*, arXiv:2410.19893 (2024), https://arxiv.org/abs/2410.19893
5. *Estimates for the moments of Bernstein polynomials*, J. Math. Anal. Appl. 432 (2015), 114–128, https://doi.org/10.1016/j.jmaa.2015.05.020
