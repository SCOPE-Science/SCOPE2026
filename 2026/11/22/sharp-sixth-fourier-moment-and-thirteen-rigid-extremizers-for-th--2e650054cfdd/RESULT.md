# Sharp Sixth Fourier Moment and Thirteen Rigid Extremizers for the Order-Three Singer Spectrum

## Finding
Let \(G=\mathbb Z/13\mathbb Z\), \(E=\{0,1,3,9\}\subset G\), and \(\zeta=\exp(2\pi i/13)\). For every \((c_0,c_1,c_2,c_3)\in\mathbb C^4\), write
\[
F_c(x)=c_0+c_1\zeta^x+c_2\zeta^{3x}+c_3\zeta^{9x},\qquad x\in G.
\]
Then the exact sharp inequality is
\[
\frac1{13}\sum_{x=0}^{12}|F_c(x)|^6\ \le\ \frac{85}{16}\left(\sum_{j=0}^3|c_j|^2\right)^3.
\]
For nonzero coefficients, equality holds **if and only if** there are \(\eta\in\mathbb C\setminus\{0\}\) and \(\ell\in\{0,1,\ldots,12\}\) such that
\[
(c_0,c_1,c_2,c_3)=\eta(1,\zeta^\ell,\zeta^{3\ell},\zeta^{9\ell}).
\]
Thus, under the normalization \(\sum|c_j|^2=1\), the coefficient multiplier is \(|\eta|=1/2\), the sixth-power norm is \(85/16\), and all nonzero extremizers form precisely 13 complex projective lines. The sharp operator norm itself is \((85/16)^{1/6}\).

## Assumptions and scope
The Haar measure on \(G\) is the uniform probability measure. Frequencies are interpreted modulo 13, with four arbitrary complex Fourier coefficients. The claim concerns the synthesis map from coefficient \(\ell^2(E)\) into \(L^6(G)\), not Euclidean spherical Fourier restriction. In particular, the denominator 13 in the sixth moment and the normalization of coefficients are essential. The set \(E\) is an explicit planar \((13,4,1)\) cyclic Singer difference set: the twelve ordered differences of distinct elements exhaust \(G\setminus\{0\}\).

## Proof
**1. Exact triple-convolution formula.** By orthogonality of all 13 cyclic characters,
\[
\frac1{13}\sum_{x\in G}|F_c(x)|^6
=\sum_{m\in G}\left|\sum_{i,j,k\in\{0,1,2,3\}:e_i+e_j+e_k=m}c_ic_jc_k\right|^2,
\]
where \((e_0,e_1,e_2,e_3)=(0,1,3,9)\) and the inner sums are ordered. Set \(a_i=|c_i|\) and let \(T_m(a)\) be the corresponding nonnegative real triple-convolution sum. The triangle inequality proves that the sixth moment does not exceed the homogeneous sextic \(P(a)=\sum_{m=0}^{12}T_m(a)^2\).

**2. Rigorous all-magnitude bound.** Define the homogeneous integer polynomial
\[
Q(a_0,a_1,a_2,a_3)=85(a_0^2+a_1^2+a_2^2+a_3^2)^3-16P(a_0,a_1,a_2,a_3).
\]
Here is a finite, exact coefficient certificate valid over the entire positive orthant, not a numerical sample. For every one of the 24 permutations \(\pi\) of \(\{0,1,2,3\}\), substitute
\[
\begin{aligned}
a_{\pi(0)}&=t,&a_{\pi(1)}&=t+u,\\
a_{\pi(2)}&=t+u+v,&a_{\pi(3)}&=t+u+v+w,
\end{aligned}
\quad t,u,v,w\ge0.
\]
The resulting exact polynomial \(Q_\pi(t,u,v,w)\), computed by ordinary integer polynomial addition and multiplication, has exactly 80 nonzero monomials, all with **strictly positive integer coefficients**, the smallest positive coefficient over all chambers being 69. Every one of the 24 polynomials also has a positive coefficient on each of the monomials \(u^6\), \(v^6\), and \(w^6\), and the coefficient of \(t^6\) vanishes. The complete Python-standard-library integer-arithmetic certificate (`CHECKER.py`) constructs the 13 triple sums, the sextic, and all 24 full expansions and checks all 1,920 nonzero coefficients and the listed strictness conditions; every operation is exact and finite. Any nonnegative vector belongs to at least one order chamber, so \(Q\ge0\) everywhere, and \(Q=0\) for a nonzero vector only if \(u=v=w=0\), i.e. \(a_0=a_1=a_2=a_3\). Setting all four magnitudes to one gives \(P(1,1,1,1)=340\). Therefore equal normalized magnitudes \(1/2\) give \(340/64=85/16\), proving the sharp value for all magnitudes.

**3. Phases and complete equality classification.** Because strict equality in the amplitude step requires four nonzero equal magnitudes, equality also requires the triangle inequality to be an equality in each nonempty triple-convolution band. Writing \(c_j=a e^{i\phi_j}\), remove a common phase by \(\phi_0=0\). The actual modulo-13 triple collisions
\[
0+0+0\equiv1+3+9,\quad
0+0+3\equiv1+1+1,\quad
0+0+9\equiv3+3+3
\pmod {13}
\]
force, respectively,
\[
\phi_1+\phi_2+\phi_3\equiv0,\qquad
\phi_2\equiv3\phi_1,\qquad
\phi_3\equiv3\phi_2\pmod{2\pi}.
\]
Consequently \(13\phi_1\equiv0\) and necessarily
\( (e^{i\phi_1},e^{i\phi_2},e^{i\phi_3})=(\zeta^\ell,\zeta^{3\ell},\zeta^{9\ell})\) for a unique \(\ell\bmod13\). Conversely, these phases multiply every triple product in residue band \(m\) by the same factor \(\zeta^{\ell m}\), so all the triangle inequalities are equalities. This proves every equality case without restricting the phases in advance.

## Verification
Run `python3 CHECKER.py` from the directory containing this report. It requires only Python 3 standard library. The delivered `CHECKER_OUTPUT.txt` records a replay of that exact program. Its integer dictionary arithmetic independently derives the triple convolution from the 64 ordered triples, verifies all ordered differences, expands the 24 complete order chambers and asserts 1,920 strictly positive nonzero coefficients, the three gap pure-power coefficients in every chamber, \(P(1,1,1,1)=340\), and the three necessary phase collisions. All 13 phase vectors are separately checked for bandwise coherence. This is an exhaustive **finite symbolic proof certificate** for a continuous amplitude inequality; it is not an inference from floating-point tests or sampled points.

## Relationship to prior work
The four-frequency support is the \(q=3\) planar Singer difference-set instance, part of the classical finite-geometry construction; the difference-set identity is also confirmed by the cited Sage reference. Ortega–Prendiville (2021) treat Fourier uniformity of asymptotically extremal Sidon sets in intervals, not this sharp sixth moment. Ciccone–Gonçalves (2022) prove an adjoint Euclidean-circle Fourier extension inequality for arithmetically constrained spectra, with a different synthesis operator, target space and normalization. A related already-published finite-group result on the Fano Singer triple \(\{0,1,3\}\subset\mathbb Z_7\) has sharp sixth moment \(37/9\) and seven extremizing lines, but does not logically determine the \((13,4,1)\) four-frequency sextic. The published difference-set fourth-moment identity, where applicable, cannot imply this sixth-moment constant and its phase rigidity. A generic cubic-convolution maximum-fiber Cauchy–Schwarz estimate only yields the weaker sixth-power bound \(7\), since the largest of the 13 ordered triple-sum fibers has size seven. Priority is assessed on these exact statements, not on title similarity.

## Limitations
This is a single precisely specified cyclic difference set and a sixth moment, not a theorem for all cyclic difference sets, all exponents, or an asymptotic restriction estimate. The integer coefficient certificate must be independently examined and run before external mathematical validation; no independent audit has occurred. Literature indexing may omit an equivalent theorem expressed via design incidence, spectral graph norms, or cyclic convolutions. An exhaustive global claim of first discovery is not made.

## References
- M. Ortega and S. Prendiville, *Extremal Sidon sets are Fourier uniform, with applications to partition regularity*, arXiv:2110.13447, first public 2021-10-26. https://arxiv.org/abs/2110.13447
- V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle under Arithmetic Constraints*, arXiv:2208.09441, first public 2022-08-19. https://arxiv.org/abs/2208.09441
- SageMath, *Difference families*, `singer_difference_set(3,2)`: the planar \((13,4,1)\) difference set. https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/designs/difference_family.html
- Related published finite Fourier research: *Sharp sixth moment and complete extremizers for the Fano Singer spectrum* (\(\mathbb Z_7\), three frequencies). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-and-complete-extremizers-for-the-fano-singer--5260cc41f9aa
- Related published finite Fourier research: *Sharp fourth-moment extension and exact deficit for finite abelian difference sets*. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-exact-deficit-for-finite-abeli--f000b50fe5d9
