# The unrestricted four-frequency volume spectrum at the second Cantor level

## Finding
Let the four equally weighted second-generation middle-thirds Cantor points be
\[
X=\{0,2/9,6/9,8/9\}.
\]
For each four-element set \(\Lambda\subset\mathbb Z/9\mathbb Z\), define the square normalized Fourier sampling matrix
\[
F_\Lambda=(2^{-1}e^{2\pi i x\lambda})_{x\in X,\,\lambda\in\Lambda}.
\]
Put \(t=2\cos(2\pi/9)\), the unique zero of \(t^3-3t+1\) in \((3/2,8/5)\). The complete set of squared Fourier-volume values, **including every nonsingular and singular case**, is
\[
\boxed{\{|\det F_\Lambda|^2:|\Lambda|=4\}=\left\{0,\frac{27(2-t)}{256},\frac{27(4-t^2)}{256},\frac{81}{256},\frac{27(t+t^2)}{256}\right\}.}
\]
Exactly eighteen of the \(\binom94=126\) four-frequency sets have zero determinant; each of the other four values occurs exactly twenty-seven times. These five values appear in the increasing order displayed.

In particular, the unrestricted sharp volume is
\[
\boxed{\max_{|\Lambda|=4}|\det F_\Lambda|=\frac{\sqrt{27(t+t^2)}}{16}=0.639651398964\ldots.}
\]
The **complete** maximizer family consists of the nine frequency translates of each of
\[
\{0,1,2,4\},\qquad \{0,1,2,7\},\qquad \{0,2,4,6\}
\]
modulo nine; these are three disjoint translation orbits. By contrast, the maximum over the conventional binary frequency-digit towers \(\{0,a,3b,a+3b\}\), where \(a,b\in\{1,2\}\), is exactly \(9/16=0.5625\). Hence the natural digit-tower restriction incurs a **strict volume loss** already at depth two: the unrestricted maximum is larger by the factor \(\sqrt{(t+t^2)/3}>1\).

## Assumptions and scope
The frequencies are four distinct **integer** residue classes modulo nine, not arbitrary real frequencies. The points have equal probability weight \(1/4\), hence each matrix entry has modulus \(1/2\), giving unit-norm Fourier columns. The quantity optimized is absolute determinant (sampling volume), **not** smallest singular value, condition number, or an infinite-level Fourier-frame bound. Any ordering of the four spatial points or frequency classes gives the same absolute determinant. The origin of the spatial digits is the standard two-map Cantor construction with maps \(x\mapsto x/3\) and \(x\mapsto (x+2)/3\), truncated to two digits.

## Proof
Write \(\zeta=e^{2\pi i/9}\). Since the spatial numerators are \(\{0,2,6,8\}=2\{0,1,3,4\}\), if the frequencies are \(\lambda_1,\ldots,\lambda_4\) and \(w_j=\zeta^{2\lambda_j}\), the transpose of the unnormalized sampling matrix has rows \((1,w_j,w_j^3,w_j^4)\). The generalized Vandermonde (alternant) identity gives
\[
16\det F_\Lambda=\pm\left(\prod_{i<j}(w_j-w_i)\right)e_2(w_1,w_2,w_3,w_4),
\qquad e_2(w)=\sum_{i<j}w_iw_j.
\]
The sign depends only on the chosen ordering and is irrelevant to the volume. This factorization can also be checked directly by expanding the determinant and extracting the ordinary Vandermonde factor.

For any \(\Lambda\), simultaneous addition of a residue to every frequency multiplies each spatial row by a unit complex number and hence leaves \(|\det F_\Lambda|\) unchanged. A nonidentity translation of \(\mathbb Z/9\mathbb Z\) has orbits of size three or nine, so it cannot stabilize a four-element frequency subset. Thus every frequency-translation orbit has exactly nine members, and the \(126\) subsets form exactly fourteen orbits.

The following is the entire orbit certificate. Each cell lists representatives of distinct translation orbits, with frequency residues in increasing order. The squared determinant for all nine members of every listed orbit is the corresponding value.

| Squared determinant | Translation-orbit representatives |
|---|---|
| \(0\) | \(\{0,1,3,6\}\), \(\{0,1,4,7\}\) |
| \(27(2-t)/256\) | \(\{0,1,3,5\}\), \(\{0,1,4,5\}\), \(\{0,1,5,7\}\) |
| \(27(4-t^2)/256\) | \(\{0,1,2,3\}\), \(\{0,1,2,5\}\), \(\{0,1,2,6\}\) |
| \(81/256\) | \(\{0,1,3,4\}\), \(\{0,1,3,7\}\), \(\{0,1,4,6\}\) |
| \(27(t+t^2)/256\) | \(\{0,1,2,4\}\), \(\{0,1,2,7\}\), \(\{0,2,4,6\}\) |

To check the table without floating point, calculate the unnormalized determinant \(D=16\det F\) by the twenty-four-term Leibniz expansion in \(\mathbb Z[\zeta]\), then reduce \(D\overline D\) modulo \(\Phi_9(z)=z^6+z^3+1\). Every reduced answer is exactly one of
\[
0,\quad 54-27t,\quad 108-27t^2,\quad 81,\quad 27(t+t^2).
\]
An independent computation using the factored alternant gives the same results. The provided integer-only checker exhausts all \(126\) distinct four-sets, checks both determinant calculations separately, and verifies the value counts and the fourteen orbits; its loops implement exhaustive finite integer arithmetic rather than sampling or inference. Since there are \(2+3+3+3+3=14\) distinct orbit representatives, each of size nine, the displayed certificate covers every possible \(\Lambda\). Multiplying by the normalization factor \(1/256\) proves the five values and their exact multiplicities.

The root \(t=2\cos(2\pi/9)\) satisfies \(t^3-3t+1=0\) and \(3/2<t<8/5\). Thus \(0<2-t<4-t^2<3<t+t^2\), giving the asserted strict order and all maximizers. Finally, each of the four binary frequency-digit towers has volume \((\sqrt3/2)^4=9/16\) either by the displayed determinant formula or by the elementary two-level block determinant identity. All are represented in the \(81/256\) stratum. Strict improvement follows because \(t+t^2>3\).

## Verification
Run `python3 CHECK.py` with Python's standard library. It uses exact six-component integer arithmetic for \(\mathbb Z[z]/(z^6+z^3+1)\), performs an **independent** Leibniz determinant and alternant-factor determinant for each of the \(126\) four-subsets, conjugates exactly using \(z^{-1}=z^8\), and reports every determinant's coefficient triple in the real basis \(1,t,t^2-2\). It checks the five predicted classes, the counts \(18,27,27,27,27\), and the fourteen length-nine orbits. The observed terminal marker was `EXACT_CANTOR_9_FOURIER_DETERMINANT_CENSUS_PASSED`. The finite universe is exhausted exactly; no floating-point tolerance, random sampling, external symbolic algebra, or infinite extrapolation is involved.

## Relationship to prior work
De Dios Pont, Liehr and Taylor (2026), *Cantor measures with odd base do not admit Fourier frames*, prove nonexistence of Fourier frames for the **limiting** odd-base Cantor measures. That result motivates studying quantitative finite approximants but does not imply the present sharp level-two determinant spectrum. The closest finite-tower result, *Exact Fourier volume and the parity barrier in binary Cantor digit towers* (2026), optimizes the determinant **only among frequency-digit towers for every depth**, yielding the benchmark \(9/16\) here; the present finding optimizes over **all** four-frequency subsets at depth two and shows that the digit-tower class is not globally volume-optimal. *Exact full-spark criterion for the four-row Fourier pattern \(\{0,1,3,4\}\)* (2026) contains the same generalized Vandermonde factorization and the fact that singular minors exist at modulus nine, but does not give the five nonzero/zero determinant strata, their multiplicities, or the maximizing family. *Exact four-frequency determinant optimum on every cyclic grid* (2026) instead treats **four consecutive spatial rows**, not this nonconsecutive Cantor row pattern. Ferguson, Mayeli and Sothanaphan (2019) define and motivate finite-group exponential-basis determinant invariants, not this finite Cantor census.

## Limitations
This is a complete four-frequency integer-grid determinant census at exactly depth two. It does not address all-depth unrestricted optimal designs, real noninteger frequencies, smallest-singular-value optimization, or infinite fractal Fourier frames. The generalized Vandermonde factorization itself is known; the claimed contribution is the exact **unrestricted** five-level spectrum, multiplicities and optimizer classification for this motivated finite Cantor problem. An older equivalent special-case determinant table might exist under different terminology. The relevant 2026 infinite-measure paper was accessible in abstract and secondary mathematical exposition, but its primary full text could not be retrieved during this examination; this is a residual bibliographic risk, not evidence of uniqueness.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, first public 2026-07-09, arXiv:2607.08656, https://arxiv.org/abs/2607.08656.
2. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, first public 2019-04-09, arXiv:1904.04487, https://arxiv.org/abs/1904.04487.
3. *Exact Fourier volume and the parity barrier in binary Cantor digit towers* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fourier-volume-and-the-parity-barrier-in-binary-cantor-dig--078452622ace.
4. *Exact full-spark criterion for the four-row Fourier pattern*, (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-full-spark-criterion-for-the-four-row-fourier-pattern-0-1--de39e0486913.
5. *Exact four-frequency determinant optimum on every cyclic grid* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-four-frequency-determinant-optimum-on-every-cyclic-grid--bb69c4d14769.
