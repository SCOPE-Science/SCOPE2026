# Exact Hausdorff spectrum of finite-slope drift in integer-base Takagi functions

## Finding

Let \(b\ge2\) be an integer, let \(\phi(x)=\operatorname{dist}(x,\mathbb Z)\), and write
\[
F_{b,n}(x)=\sum_{j=0}^{n-1}b^{-j}\phi(b^jx),\qquad S_{b,n}(x)=F_{b,n}'(x).
\]
Away from the countable set of breakpoints of the summands, \(S_{b,n}\) exists for every \(n\). For each prescribed normalized slope \(u\in[-1,1]\), define
\[
E_b(u)=\left\{x\in(0,1)\setminus\mathcal B_b:\lim_{n\to\infty}\frac{S_{b,n}(x)}n=u\right\},
\quad \mathcal B_b=\bigcup_{j\ge0}\left\{\frac{k}{2b^j}:0\le k\le2b^j\right\}.
\]
Put \(a=\lceil b/2\rceil\), \(c=\lfloor b/2\rfloor\), and
\[
P_b(t)=\log\left(a\cosh t+\sqrt{a^2\sinh^2t+c^2}\right).
\]
Then the *complete exact Hausdorff-dimension spectrum* is
\[
\boxed{\dim_H E_b(u)=\frac1{\log b}\inf_{t\in\mathbb R}\{P_b(t)-tu\},\qquad -1\le u\le1.}
\]
In particular,
\[
\dim_H E_b(0)=1,\qquad
\dim_H E_b(1)=\dim_H E_b(-1)=\frac{\log\lceil b/2\rceil}{\log b}.
\]
For every \(u\in(-1,1)\) the infimum is attained at the unique real solution of \(P_b'(t)=u\). The spectrum is even, continuous and strictly concave, with a unique maximum at \(u=0\). For even \(b\), the formula simplifies to
\[
\dim_HE_b(u)=\frac{\log(b/2)+H((1+u)/2)}{\log b},\quad
H(p)=-p\log p-(1-p)\log(1-p),
\]
with \(H(0)=H(1)=0\). In odd bases, the nontrivial persistence of consecutive slope signs gives the distinct square-root pressure above. This is a frequency spectrum of slopes of finite approximants, **not** a claim about derivatives or level sets of the limiting nowhere-differentiable function.

## Assumptions and scope

The base \(b\) is any fixed integer at least two; \(x\) lies in the open unit interval outside the explicitly excluded countable kink set; \(n\) tends to positive infinity; \(u\) is any real number from \(-1\) to \(1\), endpoints included. The metric and Hausdorff dimension are Euclidean on \([0,1]\). Logarithms are natural. Each summand has derivative \(+1\) or \(-1\) away from its kinks, so \(S_{b,n}\) is an integer in \([-n,n]\). Outside this range of normalized slopes no point satisfies the defining limit. No assertion equates \(S_{b,n}\) to any derivative of the infinite sum.

## Proof

**1. Exact tree of slope-sign histories.** At stage \(n=1\), the two sign classes are \((0,1/2)\) and \((1/2,1)\), each represented by a half-interval of length \(1/2\). Every elementary stage-\(n\) half-interval has length \(1/(2b^{n-1})\), with endpoints in \(\mathcal B_b\), and the sign history of the first \(n\) summands is constant in its interior. Multiplication by \(b\) maps the fractional coordinate in any such half-interval through one of the two half-circles; dividing it into \(b\) equal children yields exactly \(a=\lceil b/2\rceil\) children preserving the last sign and \(c=\lfloor b/2\rfloor\) reversing it. This follows by inspecting consecutive halves in the partition of each interval and is valid for either parent sign. Hence the number of elementary stage-\(n\) intervals bearing a prescribed sign history \(\varepsilon_1,\ldots,\varepsilon_n\in\{-1,1\}\) is exactly
\[
a^{\#\{j\ge2:\varepsilon_j=\varepsilon_{j-1}\}}
 c^{\#\{j\ge2:\varepsilon_j\ne\varepsilon_{j-1}\}}.
\]
In particular all sign words occur, but their cylinder multiplicities differ in odd bases. This refinement fact is also implicit in Allaart's known correlated-walk lemma; it is not asserted as a new discovery.

**2. Weighted cylinder pressure.** Assign weight \(e^{t\varepsilon_j}\) to each sign at step \(j\). The weighted adjacency matrix of the two-state directed *multigraph* is
\[
B_b(t)=\begin{pmatrix} a e^t&c e^{-t}\\c e^t&a e^{-t}\end{pmatrix}.
\]
Its entries count distinct half-interval children, not just admissible sign transitions. For \(n\ge1\), the exact weighted sum over the \(2b^{n-1}\) elementary intervals is
\[
Z_n(t)=(e^t,e^{-t})B_b(t)^{n-1}\binom11.
\]
The matrix has strictly positive entries. Its Perron eigenvalue is
\[
\rho_b(t)=a\cosh t+\sqrt{a^2\sinh^2t+c^2}.
\]
Thus \(\lim_{n\to\infty}n^{-1}\log Z_n(t)=\log\rho_b(t)=P_b(t)\). This identity follows from a two-by-two characteristic polynomial and the positive Perron eigenvectors, uniformly for each fixed \(t\). Notice \(P_b(0)=\log b\). Strict convexity follows because the underlying irreducible positive edge shift admits two different sign averages; equivalently, differentiating this explicit pressure gives \(P_b''(t)>0\) for all finite \(t\). Moreover \(P_b'(t)\to\pm1\) as \(t\to\pm\infty\).

**3. Hausdorff upper bound.** Fix \(u\in[-1,1]\), \(t\in\mathbb R\) and \(\delta>0\). At each large level \(n\), retain those elementary cylinders satisfying \(|S_{b,n}/n-u|<\delta\). The number of retained cylinders obeys
\[
\#\mathscr C_{n,\delta}\le
\exp(n(|t|\delta-tu)) Z_n(t).
\]
Indeed each retained cylinder contributes at least \(\exp(n(tu-|t|\delta))\) to \(Z_n(t)\). Each has Euclidean length \(1/(2b^{n-1})\). Since a point in \(E_b(u)\) belongs to retained cylinders for all sufficiently large \(n\), the usual limsup cover and the pressure limit yield
\[
\dim_H E_b(u)\le [P_b(t)-tu+|t|\delta]/\log b.
\]
Let \(\delta\downarrow0\), then take the infimum over \(t\).

**4. Matching lower bound for interior drift.** For every \(u\in(-1,1)\), choose the unique \(t\) satisfying \(P_b'(t)=u\). Perron left and right eigenvectors of \(B_b(t)\) define a stationary irreducible edge-Markov probability on the multigraph, with each of the \(a\) equal-sign or \(c\) switched-sign child edges treated separately. An edge from sign \(i\) to sign \(j\) has probability proportional to \(e^{tj}v_j/(\rho_b(t)v_i)\). By the ergodic theorem, almost every such infinite edge path has normalized sign sum \(u\); the Shannon–McMillan theorem gives its entropy per step \(h=P_b(t)-tu\). Distinct edge paths determine nested disjoint half-intervals with common contraction \(1/b\); their endpoints form a countable exceptional set with measure zero. The measure therefore pushes to a Borel measure on \(E_b(u)\) of exact local dimension \(h/\log b\), using the standard constant-ratio separated-interval cylinder argument (or mass-distribution and exact-dimensionality theorems). Hence \(\dim_H E_b(u)\ge [P_b(t)-tu]/\log b\).

**5. Endpoints.** As \(t\to+\infty\), \(P_b(t)-t\to\log a\), and similarly \(P_b(t)+t\to\log a\) as \(t\to-\infty\), proving matching upper bounds for \(u=\pm1\). For the lower bound, restrict to paths that never switch the selected sign: each cylinder has exactly \(a\) children of scale \(1/b\). The resulting equal-ratio Moran set has dimension \(\log a/\log b\); removing the countable set \(\mathcal B_b\) does not change this dimension when \(a\ge2\). When \(a=1\) (only \(b=2\)), instead take paths with a prescribed sparse infinite set of wrong-sign steps of zero asymptotic density and not eventually periodic, giving a nonempty subset of \(E_b(\pm1)\) and dimension zero. Therefore the claimed endpoint dimensions hold in every base.

**6. Parity specialization.** When \(b\) is even, \(a=c=b/2\), and \(\rho_b(t)=b\cosh t\). Its Legendre dual is the binary entropy expression displayed above. Strict concavity, evenness, continuity and uniqueness of the maximum follow from the analytic strictly convex pressure and its limiting slopes.

## Verification

Execute `python3 CHECK.py` with Python 3.8 or newer. It independently samples midpoints of every elementary half-base cylinder for integer bases 2 through 7 and lengths 1 through 6, reconstructs all sign histories using integer arithmetic, and compares their exact multiplicities to the tree formula. It also checks the characteristic-root formula against independently iterated positive matrices at five tilt parameters per base and checks the central and near-boundary dimensions numerically. The run produced 756 exact sign-word comparisons, 30 spectral comparisons, and central/endpoint comparisons for six bases, all passing. These computations support the finite combinatorial premises; the all-parameter pressure and Hausdorff assertions follow from the preceding proof, not from finite enumeration.

## Relationship to prior work

Allaart's 2014 work [1] **already establishes** the correlated-random-walk law and the exact persistence parameters of the finite-slope signs; neither that law nor the classical central limit theorem is claimed here as novel. Nakano and Takei [2] derive limit and localization theorems for the same process; Jiang, Ying and Zhang [3] study local level sets for the same integer-base functions and explicitly define the signed cumulative slopes. Suzuki [4] treats a different beta-expansion Takagi generalization. The present claim is the *closed-form, all-drift Euclidean Hausdorff spectrum of asymptotic finite-slope averages*, with its boundary dimensions and odd/even split. Standard finite-state thermodynamic formalism supplies a general route to the pressure variational principle; the explicit two-state edge multiplicities and evaluated pressure give the particular exact invariant. This is an application of established methods, not a claim to have invented those methods.

## Limitations

The spectrum is not the Hausdorff dimension of the function's height level sets, nor an infinite-derivative classification. No local modulus-of-continuity equivalence is asserted at exceptional points. A general thermodynamic-formalism theorem together with the known Markov coding yields an abstract spectral formula, so only the explicit evaluation and complete specialization are proposed as the contribution. Historical priority is not independently certified: older treatments of the correlated walk or its multifractal spectrum might contain an equivalent closed form under different notation. Finite tests and negative searches cannot establish originality; no independent validation has been performed.

## References

1. Pieter C. Allaart, *On the level sets of the Takagi-van der Waerden functions*, J. Math. Anal. Appl. 419 (2014), 1168–1180; arXiv:1312.2119v2, https://arxiv.org/html/1312.2119v2, esp. Section 3.
2. Yuzaburo Nakano and Masato Takei, *Limit theorems for elephant random walks remembering the recent past, with applications to the Takagi–van der Waerden class functions*, arXiv:2505.08285v1, https://arxiv.org/abs/2505.08285 (first public 2025-05-13).
3. Lai Jiang, Ting-Ting Ying and Yi-Yang Zhang, *Local level sets of the Takagi–van der Waerden function*, arXiv:2610.08572v1, https://arxiv.org/html/2610.08572v1 (first public 2026-10-06).
4. Shintaro Suzuki, *A generalization of the Takagi function for beta-expansions*, arXiv:2604.17809v1, https://arxiv.org/html/2604.17809v1 (first public 2026-04-20).
