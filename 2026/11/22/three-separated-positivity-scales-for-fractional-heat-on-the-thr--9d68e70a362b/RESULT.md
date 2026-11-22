# Three separated positivity scales for fractional heat on the three-cube

## Finding
Let \(Q_3\) be the unit-weight three-dimensional Boolean hypercube, let \(L=3I-A\) be its combinatorial Laplacian, and let \(K_\alpha(t)=\exp(-tL^\alpha)\), for every real \(\alpha>0\) and \(t\ge0\). Matrix entries depend only on the Hamming distance \(r\in\{0,1,2,3\}\) of their endpoints. Set
\[
 X=e^{-2^\alpha t},\qquad Y=e^{-4^\alpha t},\qquad Z=e^{-6^\alpha t}.
\]
The exact distance entries, multiplied by eight, are
\[
\begin{array}{c|l}
r&8k_r(t)\\\hline
0&1+3X+3Y+Z\\
1&1+X-Y-Z\\
2&1-X-Y+Z\\
3&1-3X+3Y-Z.
\end{array}
\]
For \(0<\alpha\le1\), all entries are strictly positive at every positive time. For every \(\alpha>1\), the distance-two entry has precisely one positive zero \(t_2(\alpha)\), being negative before and positive after that zero. The distance-one and diagonal entries remain strictly positive.

For \(1<\alpha\le2\), the opposite-corner (distance-three) entry likewise has exactly one positive zero, denoted \(t_3(\alpha)\), with negative sign before and positive sign after. In contrast, for **every \(\alpha>2\)** the opposite-corner entry has exactly two simple positive zeros \(0<t_-(\alpha)<t_+(\alpha)\); it is **positive, then negative, then positive** on the successive open time intervals. Despite this reentrant pairwise sign pattern, the *whole* matrix is entrywise nonnegative exactly at
\[
 \boxed{\{0\}\cup[t_+(\alpha),\infty)}\qquad(\alpha>2).
\]
Indeed the three positive characteristic times are strictly ordered:
\[
 \boxed{t_-<\frac{\log2}{4^\alpha}<t_2<\frac{\log2}{2^\alpha}<t_+.}
\]
For \(1<\alpha\le2\), the complete nonnegativity set is \(\{0\}\cup[\max\{t_2,t_3\},\infty)\).

The three characteristic times have **three different large-exponent scales**. If \(W\) is the principal real Lambert function, defined by \(W(z)e^{W(z)}=z\) for \(z>0\), then as \(\alpha\to\infty\),
\[
\boxed{
4^\alpha t_-\longrightarrow\log(3/2),\qquad
4^\alpha t_2=W(2^\alpha)+o(1),\qquad
2^\alpha t_+\longrightarrow\log3.
}
\]
In particular \(t_-=o(t_2)\) and \(t_2=o(t_+)\). The intermediate scale is enhanced by the growing factor \(W(2^\alpha)\sim\alpha\log2\); it is not simply a constant multiple of either exponential scale.

## Assumptions and scope
Vertices are the eight binary triples, with edges between triples differing in exactly one coordinate and all edge conductances one. Spectral powers \(L^\alpha\) use the real nonnegative functional calculus, with the zero eigenvalue mapped to zero. Nonnegativity is entrywise on the canonical coordinate cone, not positive semidefiniteness; all \(K_\alpha(t)\) are positive definite as quadratic forms. All times are dimensionless continuous times. Zeros always refer to *positive* time unless otherwise specified; at \(t=0\) the matrix is the identity. The limit holds with graph fixed and exponent diverging. No conclusion about other cube dimensions, weighted graphs, or normalized Laplacians is asserted.

## Proof
**1. Exact Walsh diagonalization.** The coordinate flip operators commute, and the eight Walsh characters diagonalize \(L\). A character of degree \(j\in\{0,1,2,3\}\) has eigenvalue \(2j\) and multiplicity \(\binom3j\). Summing \(e^{-t(2j)^\alpha}\) against characters at two vertices of Hamming distance \(r\) gives the four displayed rows. This also directly proves \(k_0>0\); moreover \(k_1=(1+X-Y-Z)/8>0\) because \(0<Z<1\) and \(0<Y<X<1\) for \(t>0\).

**2. The ordinary and subordinated range.** At \(\alpha=1\), tensorization gives \(k_r(t)=e^{-3t}(\sinh t)^r(\cosh t)^{3-r}>0\) for \(t>0\). For \(0<\alpha<1\), the completely monotone scalar function \(s\mapsto e^{-ts^\alpha}\) is a Laplace transform of a positive probability measure on \((0,\infty)\). The corresponding positive mixture of strictly positive ordinary graph-heat matrices \(e^{-uL}\) is strictly positive. This proves the first phase.

**3. A root-counting fact.** A nonzero generalized polynomial \(\sum_{j=0}^m c_j x^{\lambda_j}\), \(0< x<\infty\), with strictly ordered real exponents has no more positive roots, counted with multiplicities, than the number of sign variations in its nonzero ordered coefficient list. This follows by induction: divide by the first monomial, differentiate, and apply Rolle's theorem, including endpoint signs. Equivalently, the same bound applies to \(\sum_j c_j e^{-\lambda_jt}\) on the real line. We only use coefficient lists of three or four terms, with at most two or three sign variations.

**4. The distance-two crossing.** Put \(a=2^\alpha\), \(b=4^\alpha\), \(c=6^\alpha\), so \(0<a<b<c\). The numerator \(J(t)=8k_2(t)=1-e^{-at}-e^{-bt}+e^{-ct}\) has two sign changes in ascending exponent order, and has the root \(J(0)=0\). For \(\alpha>1\), superadditivity of \(u\mapsto u^\alpha\) gives \(c>a+b\), so \(J'(0)=a+b-c<0\). Yet \(J(t)\to1\). There is therefore exactly one further root \(t_2>0\), simple, and the stated negative-to-positive sign transition follows from the root-count bound.

**5. Exact distance-three phase transition.** Let \(H(t)=8k_3(t)=1-3e^{-at}+3e^{-bt}-e^{-ct}\). It has three sign changes, and \(H(0)=0\). Its initial slope is
\[
H'(0)=3a-3b+c=a\bigl(3-3\cdot2^\alpha+3^\alpha\bigr).
\]
As a function of \(\alpha\), the factor in parentheses has at most two real zeros by the same exponential-polynomial root bound, and it vanishes at exactly \(\alpha=1\) and \(\alpha=2\). Its value at \(\alpha=0\) is one, its value at \(\alpha=3/2\) is \(3(1-2\sqrt2+\sqrt3)<0\), and its value at \(\alpha=3\) is positive. The at-most-two-root bound and continuity therefore establish a negative sign for \(1<\alpha<2\) and a positive sign for \(\alpha>2\). At \(\alpha=2\), \(H'(0)=0\) but \(H''(0)=-576<0\), so \(H\) begins negative; this double time-zero root consumes two of the three allowed zeros. Consequently for \(1<\alpha\le2\), because \(H(t)\to1\), there is precisely one simple positive root and its sign change is negative-to-positive.

For \(\alpha>2\), \(H\) starts positive. Put \(t_0=(\log2)/b\) and \(p=b/a=2^\alpha\ge4\). Then
\[
H(t_0)=\frac52-3\,2^{-1/p}-2^{-c/b}
<\frac52-3\,2^{-1/4}<0,
\]
using \(2^{-1/4}>5/6\). Since \(H(t)\to1\), it has at least two positive sign-changing roots. The generalized Descartes bound, after counting \(t=0\), permits at most two, with multiplicity. Therefore they are exactly two simple roots and the signs are positive, negative, positive as claimed.

**6. The global positivity horizon for \(\alpha>2\).** At \(t_0=(\log2)/b\), the preceding proof gives \(t_-<t_0<t_+\). Moreover, writing \(r=c/b=(3/2)^\alpha\ge9/4\),
\[
J(t_0)=\frac12-2^{-1/p}+2^{-r}
\le\frac12-2^{-1/4}+2^{-9/4}<0.
\]
Thus \(t_0<t_2\). At \(t_1=(\log2)/a\), the inequalities \(p\ge4\) and \(c/a>p\) give
\[
J(t_1)=\frac12-2^{-p}+2^{-c/a}>0,
\qquad H(t_1)=-\frac12+3\cdot2^{-p}-2^{-c/a}<0.
\]
Hence \(t_2<t_1<t_+\). These strict inequalities establish the complete ordering. The distance-two entries are negative until \(t_2\), while opposite-corner entries are negative exactly on \((t_-,t_+)\). Therefore at every positive time less than \(t_+\) at least one entry is negative, and at \(t_+\) and all later times every entry is nonnegative. For \(1<\alpha\le2\), both nontrivial entry types have single negative-to-positive crossings, giving the stated maximum of the two roots.

**7. Three distinct large-exponent scales.** Write \(p=b/a=2^\alpha\to\infty\) and \(r=c/b=(3/2)^\alpha\to\infty\). For fixed \(u>0\),
\[
H(u/b)=1-3e^{-u/p}+3e^{-u}-e^{-ru}\longrightarrow -2+3e^{-u}.
\]
This limit changes sign exactly at \(u=\log(3/2)\). By bracketing with any two fixed positive \(u\)-values on opposite sides, and using uniqueness of the first root in \((0,t_0)\), we obtain \(b t_-\to\log(3/2)\).

Similarly, for fixed \(v>0\),
\[
H(v/a)=1-3e^{-v}+3e^{-pv}-e^{-(c/a)v}
\longrightarrow1-3e^{-v},
\]
whose unique zero is \(v=\log3\). The last root lies between fixed \(v\)-values bracketing this zero, so \(a t_+\to\log3\).

For the distance-two zero put \(u=bt_2\). Its defining equation is
\[
1-e^{-u/p}=e^{-u}-e^{-ru}.
\]
For each fixed \(\delta\in(0,1)\), comparing the left and right sides at \(u=(1-\delta)\log p\) and \(u=(1+\delta)\log p\) shows that the unique positive root satisfies \(u/\log p\to1\): the two sides are respectively asymptotic to \(u/p\) and \(e^{-u}\), with \(e^{-ru}\) negligible there. Rearranging the defining equality gives
\[
 e^u(1-e^{-u/p})=1-e^{-(r-1)u},
\]
so \(u e^u/p\to1\). Since \(u\mapsto u+\log u\) has derivative greater than one on positive arguments and \(W(p)e^{W(p)}=p\), it follows that \(u=W(p)+o(1)\). This proves all three limits and their strict asymptotic separation.

## Verification
The accompanying standalone `checker.py` reconstructs the eight-vertex graph independently, diagonalizes its matrix Laplacian, and compares the four closed-form entries against the numerical spectral functional calculus at 8,640 coordinate/time/exponent comparisons. It additionally performs 11 positive-root and sign-family checks across exponents on both sides of the critical value, prints the three rescaled characteristic times for exponents 6, 8, 10, 12 and 15, and checks the asymptotic Lambert expression numerically. Successful local execution reported `CHECK_OK 8640 matrix entries and 11 root-family checks`. Run with `python checker.py` after installing NumPy and SciPy. Such finite numerical tests do not prove a global sign classification or an asymptotic: the analytical root-count and limiting arguments above supply those proofs.

## Relationship to prior work
Riascos and Mateos (2014) define spectral fractional graph diffusion and investigate the Markovian range \(0<\alpha<1\), with exact work on rings and other networks. Their accessible author-supplied full text, especially Sections III–V, does not discuss superlinear spectral powers or a three-cube sign-reentry classification. Benzi and Simunec (2021) develop numerical rational Krylov methods for fractional graph diffusion, again in the Markovian exponent range \(0<\alpha<1\). Daners, Glück and Kennedy (2015) establish qualitative eventual-positivity theory, but not these precise Walsh entry signs and singularly separated exponent-dependent time scales.

Published analyses of *completed Radau IIA and Gauss–Legendre heat steps* on Boolean cubes concern rational numerical maps rather than the exact semigroup \(e^{-tL^\alpha}\); their reentry and dimension thresholds do not imply this result. Published fractional-heat classifications on complete multipartite graphs concern diameter-two families with at most three Laplacian spectral levels; \(Q_3\) has diameter three and four distinct spectral levels. The four-vertex path has a different Laplacian spectrum and its analogous fractional-heat sign behavior does not imply the exact cube classification or the Lambert-scale intermediate recovery. A published sharp spectral-window envelope theorem bounds *families* of symmetric generators by extremizing over eigenvectors; it does not determine this particular cube's four-mode sign pattern or roots. The generalized-polynomial zero-count principle is classical and is used, not claimed as new.

## Limitations
The result is specific to the unweighted three-cube and exact continuous spectral-power heat. The complete positivity horizon in the range \(1<\alpha<2\) is specified by the maximum of two uniquely defined scalar roots, without a simplification of which root is larger. The large-\(\alpha\) equivalents are asymptotic, not finite-exponent error bounds. No universal phase law for \(Q_d\) with \(d\ge4\), or graph-uniform perturbation theorem, is asserted. Literature search and full-text comparisons support originality but cannot certify historical priority against all unindexed sources. Independent validation has not been performed.

## References
1. A. P. Riascos and J. L. Mateos, “Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights,” *Physical Review E* **90** (2014), 032809, publicly dated 17 September 2014, DOI: https://doi.org/10.1103/PhysRevE.90.032809 ; author-supplied full text: https://www.researchgate.net/publication/265728770_Fractional_dynamics_on_networks_Emergence_of_anomalous_diffusion_and_Levy_flights ; arXiv:1506.06167 (19 June 2015).
2. M. Benzi and I. Simunec, “Rational Krylov methods for fractional diffusion problems on graphs,” *BIT Numerical Mathematics* **62** (2022), 357–385, open access online 1 July 2021, https://doi.org/10.1007/s10543-021-00881-0 .
3. D. Daners, J. Glück and J. B. Kennedy, “Eventually and asymptotically positive semigroups on Banach lattices,” arXiv:1511.05294 (17 November 2015), https://arxiv.org/abs/1511.05294 .
4. “A sharp positivity transition for fractional graph heat on complete multipartite networks,” published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1 .
5. “Sharp Radau positivity loss and reentry on Boolean hypercubes,” published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-radau-positivity-loss-and-reentry-on-boolean-hypercubes--093b06a03097 .
6. “Sharp entrywise spectral-window envelopes and the exact eventual-positivity horizon,” published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-entrywise-spectral-window-envelopes-and-the-exact-eventual--aea2a1d10bf1 .
