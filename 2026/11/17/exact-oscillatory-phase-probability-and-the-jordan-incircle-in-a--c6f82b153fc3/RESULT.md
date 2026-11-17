# Exact oscillatory-phase probability and the Jordan incircle in a three-locus recombination cycle

## Finding
For the directed three-locus specialization of the quadratic stochastic population operator of Omirov and Rozikov [1], the fiber evolution has an exact real-to-complex spectral transition along the **incircle** of the conserved-mass triangle. At every strictly positive mass triple on this incircle, the two nonstationary eigenvalues coalesce into a **genuine size-two Jordan block** at \(1/2\). The resulting transient includes an explicitly determined polynomial factor multiplying exponential decay.

If the six initial population coordinates are sampled **uniformly on the five-dimensional probability simplex**, the probability that the two nonstationary fiber eigenvalues are nonreal is exactly
\[
\boxed{\mathbb P(\text{nonreal relaxation pair})=\frac{25\pi}{54\sqrt3}=0.839721927886\ldots.}
\]
The real-distinct phase has the complementary probability \(1-25\pi/(54\sqrt3)\); the defective boundary has probability zero. This is an exact natural-volume classification for this nonlinear population system, not merely a spectral description at one chosen mass vector.

## Assumptions and scope
There are six nonnegative population coordinates \(x_{i,+},x_{i,-}\) indexed by \(i\in\{1,2,3\}\), with total sum one. All indices below are cyclic, so \(i+1=1\) when \(i=3\). The autonomous evolution rule is
\[
\begin{aligned}
x'_{i,+}&=x_{i,+}+x_{i,-}x_{i+1,+}-x_{i,+}x_{i+1,-},\\
x'_{i,-}&=x_{i,-}-x_{i,-}x_{i+1,+}+x_{i,+}x_{i+1,-}.
\end{aligned}
\]
This is equation (1.5) of [1] with coefficients \(a_{i,i+1}=1\) and all other \(a_{ij}=0\); unlike the symmetric example in [1], these coefficients describe a genuinely directed cycle. Let \(c_i=x_{i,+}+x_{i,-}\), and suppose \(c_i>0\) for each \(i\). Write \(u_i=x_{i,+}\), so \(0\le u_i\le c_i\). The deterministic assertions quantify over **every** such invariant mass triple and every admissible initial \(u\). The random assertion uses normalized Lebesgue measure on the **whole five-simplex**, equivalently \(\operatorname{Dirichlet}(1,1,1,1,1,1)\); the three mass sums then have \(\operatorname{Dirichlet}(2,2,2)\) law. Thus the sampling measure is fixed and not a freely chosen prior on the mass triangle.

## Proof
**1. The exact invariant fiber and its spectrum.** Every pair sum \(c_i\) is preserved. Substituting \(x_{i,-}=c_i-u_i\) reduces the quadratic evolution to the linear recurrence \(u'=B_cu\), where
\[
 B_c=\begin{pmatrix}
 1-c_2&c_1&0\\
 0&1-c_3&c_2\\
 c_3&0&1-c_1
 \end{pmatrix},\qquad c_1+c_2+c_3=1.
\]
Let \(s=c_1c_2+c_2c_3+c_3c_1\). Direct determinant expansion gives
\[
\det(tI-B_c)=(t-1)(t^2-t+s),\qquad
\lambda_\pm=\frac{1\pm\sqrt{1-4s}}2.
\]
Since \(1-4s=2(c_1^2+c_2^2+c_3^2)-1\), the eigenvalues are real distinct for \(\sum_i c_i^2>1/2\), nonreal conjugates for \(\sum_i c_i^2<1/2\), and coalesce at \(1/2\) for equality. In the nonreal region their modulus is \(\sqrt s<1\); in the real region both roots lie strictly between zero and one. Hence both nonstationary modes decay, except for a polynomial correction at coalescence.

**2. The critical circle is entirely admissible.** Set
\[
 c_1=\frac13+\frac{u}{\sqrt2}+\frac{v}{\sqrt6},\quad
 c_2=\frac13-\frac{u}{\sqrt2}+\frac{v}{\sqrt6},\quad
 c_3=\frac13-\frac{2v}{\sqrt6}.
\]
Then \(\sum_i c_i^2=1/3+u^2+v^2\). Thus the nonreal phase is exactly the open disk \(u^2+v^2<1/6\). The three lines \(c_i=0\) are tangent to its boundary, so this is precisely the incircle of the equilateral mass simplex in these orthonormal planar coordinates. Every point of the critical circle other than its three tangencies to the mass-triangle sides has strictly positive masses.

**3. Every interior critical point is defective, and the time law is exact.** The right eigenvector of \(B_c\) at eigenvalue one is \(c=(c_1,c_2,c_3)^\mathsf T\), and a normalized left eigenvector is
\[
 w=\frac1s(c_3,c_1,c_2)^\mathsf T,\qquad w^\mathsf T c=1.
\]
The similarity \(D^{-1}B_cD\), where \(D=\operatorname{diag}(c_1,c_2,c_3)\), is the irreducible, aperiodic row-stochastic transition operator of the normalized allele ratios; hence the eigenvalue one is simple. Define \(\Pi=cw^\mathsf T\), \(E=I-\Pi\), and, on the critical circle, \(N=(B_c-\tfrac12 I)E\). Cayley–Hamilton on the invariant two-dimensional range of \(E\) yields \(N^2=0\). If \(N=0\), then \(B_c=\Pi+\tfrac12 E\), whose \((1,3)\)-entry is \(c_1w_3/2>0\), contradicting \((B_c)_{13}=0\). Therefore \(N\ne0\) and the double eigenvalue is one Jordan block. Because \(\Pi E=E\Pi=\Pi N=N\Pi=0\), the binomial identity gives, for every integer \(n\ge1\),
\[
 \boxed{u^{(n)}=\Pi u^{(0)}+2^{-n}E u^{(0)}+n2^{-(n-1)}N u^{(0)}.}
\]
The limit is \(\Pi u^{(0)}\). The polynomially enhanced term is nonzero for all initial fiber points outside the proper subspace \(\ker N\), subject to the admissible box.

**4. Exact five-simplex probability.** Under \(\operatorname{Dirichlet}(1,1,1,1,1,1)\) sampling, grouping each pair of coordinates gives \((c_1,c_2,c_3)\sim\operatorname{Dirichlet}(2,2,2)\), with normalized density \(120c_1c_2c_3\) relative to \(dc_1dc_2\). The above coordinate change has Jacobian \(dc_1dc_2=du\,dv/\sqrt3\). Expanding the cubic product gives
\[
 c_1c_2c_3=\frac1{27}-\frac{u^2+v^2}{6}+H_3(u,v),
\]
where \(H_3\) is homogeneous of odd degree three. Its integral over the centered disk vanishes by inversion symmetry. With \(R^2=1/6\), polar integration yields
\[
\begin{aligned}
\mathbb P(\text{nonreal pair})
&=\frac{120}{\sqrt3}\int_{u^2+v^2<R^2}c_1c_2c_3\,du\,dv\\
&=\frac{120\pi}{\sqrt3}\left(\frac{R^2}{27}-\frac{R^4}{12}\right)
=\frac{25\pi}{54\sqrt3}.
\end{aligned}
\]
The circle and the three simplex edges have zero probability under the continuous mass density; no classification of boundary-degenerate fiber matrices is needed for the probability statement. This proves the assertions. \(\square\)

## Verification
Run `python checks/verify.py` from the extracted result directory; it requires only the Python standard library. The exact-rational program verifies the fiber stationary vectors and spectral polynomial identity for every positive three-mass rational triple with common denominator from three through thirteen; checks the nonzero square-zero Jordan term and its power formula on all rational critical triples in this range; tests ten iterates of the **original six-coordinate quadratic map** against its independent Jordan expression at the exact critical masses \((1/6,1/6,2/3)\); and checks the exact coefficient of the polar integral. This checker was executed successfully. Exhausting these finite grids is not a proof for arbitrary masses, and evaluating the rational coefficient is not a numerical integration of an infinite domain; the general proof is the symbolic derivation above.

## Relationship to prior work
Omirov and Rozikov [1] introduce the quadratic many-loci family, prove invariant-fiber reduction in Lemma 2, establish the eigenvalue-one direction, and characterize limiting equilibria in Theorem 2. None of these foundational facts is asserted as new. Their explicit three-locus example uses symmetric interaction coefficients; it is not the directed cycle considered here. A later study [2] treats **the very same directed cyclic coefficient choice** and proves high-dimensional Dirichlet equilibrium-selection fluctuation laws as the number of loci grows. That related selection problem does not imply the present fixed-three-locus spectral incircle, Jordan formula, or exact uniform-initialization oscillatory probability. General studies of three-state stochastic matrices with nonreal spectra and exceptional points are acknowledged: Guerry [3] analyzes stochastic **matrix roots and embeddability**, and [4] studies a **continuous-time**, uniform-stationary, bidirectionally weighted three-state ring and dissipation–frequency bounds. Such general spectral frameworks do not give the specified nonlinear-fiber geometry or its induced five-simplex probability. In particular, complex eigenvalues and Jordan behavior for general nonreversible chains are established prior concepts and are not claimed as novel by themselves.

## Limitations
The exact probability applies only to three directed cyclic loci with the stated unit nearest-neighbor coupling and six-coordinate uniform-simplex sampling. Other initial ensembles change the probability, and other interaction graphs change the phase geometry. The Jordan identity concerns strictly positive invariant masses on the critical circle, not side-tangency fibers. The deterministic spectral result alone does not imply an oscillatory coordinate time series for every initial point (a stationary initial point has no transient). The calculation has not been independently validated, and publication priority against every unindexed equivalent treatment cannot be guaranteed; in particular broader matrix-spectrum results may include some elementary spectral ingredients.

## References
[1] B. A. Omirov and U. A. Rozikov, *A many-loci system with evolution characterized by uncountable linear operators*, arXiv:2409.19687v1 (first publicly posted 2024-09-29), https://arxiv.org/abs/2409.19687; equations (1.5), (2.3), Lemma 3, and Theorem 2.

[2] *Logarithmically anomalous equilibrium selection in a directed many-loci recombination cycle* (public research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-logarithmically-anomalous-equilibrium-selection-in-a-directed-ma--e41bc379b29f.

[3] M.-A. Guerry, *Matrix roots and embedding conditions for three-state discrete-time Markov chains with complex eigenvalues*, *Communications in Mathematics and Statistics* **10** (2022), 435–450, https://doi.org/10.1007/s40304-020-00226-3; accepted manuscript https://cris.vub.be/ws/portalfiles/portal/76279221/Guerry_CIMS_April_2020.pdf.

[4] *Disorder barriers and a sharp dissipation–frequency frontier on a three-state Markov cycle* (public research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-disorder-barriers-and-a-sharp-dissipation-frequency-frontier-on--8d74749dd242.
