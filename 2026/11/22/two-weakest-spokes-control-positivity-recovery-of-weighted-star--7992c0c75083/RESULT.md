# Two weakest spokes control positivity recovery of weighted-star biharmonic resolvents

## Finding
Let a star have one hub and \(m\ge2\) leaves, with arbitrary positive edge conductances ordered as \(0<w_1\le w_2\le\cdots\le w_m\). Let \(L\) be its symmetric combinatorial weighted Laplacian, and define the backward-Euler biharmonic map
\[
R(h)=(I+hL^2)^{-1},\qquad h\ge0.
\]
There is precisely one number \(\tau(w)>0\) for which
\[
R(h)\text{ is entrywise nonnegative}
\quad\Longleftrightarrow\quad h=0\ \text{or}\ h\ge\tau(w).
\]
The same condition characterizes \(\|R(h)\|_{\ell^\infty\to\ell^\infty}=1\). Every hub-to-leaf entry is strictly positive for \(h>0\), every diagonal entry is positive, and the entry joining the two least-conductive leaves is negative on \(0<h<\tau(w)\), zero at \(h=\tau(w)\), and positive afterward. In particular, no other pair determines a later loss-of-negativity threshold.

The unique positive root of the strictly decreasing scalar function
\[
F_w(h)=\frac1h-(m+1)w_1w_2+
\sum_{k=3}^{m}\frac{(w_k-w_1)(w_k-w_2)}{1+hw_k^2}
\]
is \(\tau(w)\). For every \(m\ge2\),
\[
\frac{1}{(m+1)w_1w_2}\le \tau(w)\le
\frac{m-1}{(m+1)w_1w_2}.
\]
The lower bound is attained exactly when \(w_3=\cdots=w_m=w_2\) (vacuously for \(m=2\)). For \(m\ge3\), the upper bound is strict for finite weights but is sharp as all \(w_3,\dots,w_m\) diverge with the first two fixed. For \(m=2\), both bounds are equal and \(\tau(w)=1/(3w_1w_2)\). Equal conductances \(w_i=w\) give \(\tau=1/((m+1)w^2)\).

## Assumptions and scope
The graph is finite, undirected, loop-free, with \(m\ge2\) leaves and unit vertex masses. Edge weights are positive conductances, not lengths or resistances. The hub is indexed by \(0\), the leaves by \(1,\ldots,m\), and the matrix acts on the real space \(\mathbb R^{m+1}\). Nonnegativity is entrywise, not positive semidefiniteness (the latter holds automatically). The step size \(h\) has units inverse conductance squared. No claims are made for trees that are not stars, for normalized Laplacians, or for the continuous-time heat semigroup.

## Proof
Write \(W=\sum_{i=1}^m w_i\). The star Laplacian has entries \(L_{00}=W\), \(L_{0i}=L_{i0}=-w_i\), \(L_{ii}=w_i\), and all other entries zero. For \(s=\sqrt h>0\), spectral calculus for the real symmetric matrix \(L\) gives
\[
R(h)=\operatorname{Re}(I+isL)^{-1}.
\]
Set \(d_i=1+isw_i\) and
\[
S=1+\sum_{k=1}^m\frac{isw_k}{1+isw_k}.
\]
The Schur-complement inversion of \(I+isL\) yields, for distinct leaves \(i,j\),
\[
(I+isL)^{-1}_{ij}=-\frac{s^2w_iw_j}{d_id_jS},
\qquad
(I+isL)^{-1}_{0i}=\frac{isw_i}{d_iS}.
\]
Indeed, the leaf diagonal block is \(\operatorname{diag}(d_i)\), and its hub Schur complement equals \(1+isW+s^2\sum_i w_i^2/d_i=S\). The real and imaginary parts of \(S\) are strictly positive:
\[
\operatorname{Re}S=1+\sum_k\frac{s^2w_k^2}{1+s^2w_k^2}>0,
\qquad
\operatorname{Im}S=\sum_k\frac{sw_k}{1+s^2w_k^2}>0.
\]
Put \(\theta_i=\arctan(sw_i)\in(0,\pi/2)\) and \(\phi=\arg S\in(0,\pi/2)\). The hub-to-leaf inverse entry has argument \(\pi/2-\theta_i-\phi\in(-\pi/2,\pi/2)\), hence \(R(h)_{0i}>0\). The diagonal entries of \(R(h)\) are positive because \(I+hL^2\) is positive definite.

For distinct leaves, \(R(h)_{ij}\) has the *opposite* sign to
\[
\operatorname{Re}\bigl(d_id_jS\bigr)
=|d_i d_j S|\cos(\theta_i+\theta_j+\phi).
\]
Since \(0<\theta_i+\theta_j+\phi<3\pi/2\), this leaf-to-leaf entry is nonnegative exactly when \(\theta_i+\theta_j+\phi\ge\pi/2\). Because \(w_1\le w_2\le\cdots\le w_m\), the pair \((1,2)\) has the smallest angle sum of every distinct pair. Consequently all leaf-to-leaf entries are nonnegative if and only if \(R(h)_{12}\ge0\), for each fixed \(h>0\), regardless of repeated weights.

An elementary expansion of the real part, using \(\operatorname{Re}(iz/(1+iz))=z^2/(1+z^2)\) for real \(z\), gives for all distinct leaves
\[
\frac{\operatorname{Re}(d_id_jS)}{h}
=\frac1h-(m+1)w_iw_j+
\sum_{k\notin\{i,j\}}
\frac{(w_k-w_i)(w_k-w_j)}{1+hw_k^2}.
\]
For the least-weight pair this is exactly \(F_w(h)\). Every term in its sum has nonnegative numerator; moreover
\[
F'_w(h)=-\frac1{h^2}
-\sum_{k=3}^m\frac{w_k^2(w_k-w_1)(w_k-w_2)}{(1+hw_k^2)^2}<0.
\]
The limits are \(F_w(0+)=+\infty\) and \(F_w(+\infty)=-(m+1)w_1w_2<0\). Thus the unique root \(\tau\) exists, and the sign rule proves that \(R(h)_{12}<0\) exactly on \((0,\tau)\). This proves the stated nonnegative-entry classification for positive steps. At \(h=0\), \(R(0)=I\), giving the isolated safe step. Also \(L\mathbf1=0\) implies \(R(h)\mathbf1=\mathbf1\). Any real matrix whose row sums are one has induced \(\ell^\infty\)-norm one if and only if every entry is nonnegative, proving the norm assertion.

Finally, \(F_w(h)\ge 1/h-(m+1)w_1w_2\), so its zero satisfies the lower bound, with equality precisely when each remaining numerator vanishes, namely \(w_k=w_2\). For \(m\ge3\) and finite positive weights,
\[
0\le\frac{(w_k-w_1)(w_k-w_2)}{1+hw_k^2}<\frac1h.
\]
Hence \(F_w(h)<(m-1)/h-(m+1)w_1w_2\), giving the strict upper bound. When \(w_3,\ldots,w_m\to\infty\) with \(w_1,w_2\) fixed, each displayed summand converges to \(1/h\), uniformly on compact subintervals of \((0,\infty)\). Uniqueness and monotonicity then imply convergence of the zero to the stated upper bound. The empty-sum case \(m=2\) is immediate.

## Verification
Run `python3 verify.py` from the directory containing the extracted file. The included standard-library script checks 70 exact-rational matrix inverses and leaf-entry signs for stars with two to six leaves, 300 positive-weight samples for the sharp bounds, ten equal-weight cases, and seven high-contrast limiting cases. These checks corroborate, but do not replace, the preceding infinite-family proof. For example, weights \((1,2,3,7)\) have an implicit threshold approximately \(0.16796625979123597\).

## Relationship to prior work
Gregorio and Mugnolo, *Bi-Laplacians on graphs and networks* (arXiv:1712.07370, first posted December 20, 2017), prove general continuous-time semigroup nonpositivity and eventual positivity statements, with a three-vertex path example (Section 2) and a discussion of degree-based semigroup transition sites (Remark 6.2). Those theorems do not specify the backward-Euler rational resolvent's sharp recovery step for arbitrary weighted stars. Fontan and Altafini, *On the properties of Laplacian pseudoinverses* (arXiv:2109.14587, 2021), address eventual exponential positivity and signed pseudoinverses rather than this discrete resolvent threshold. Related finite graph-propagator positivity results for Crank–Nicolson, Gauss–Legendre, and cyclic biharmonic smoothing concern different functions of their Laplacians, and their exact endpoints do not imply the formula above.

## Limitations
The statement is confined to strictly positive conductances and the unnormalized symmetric star Laplacian, and determines a positivity threshold rather than the full transient \(\ell^\infty\)-norm profile. It does not imply that each nonminimal leaf-to-leaf entry crosses zero only once. The sharp upper bound is a supremal limit, not an attained finite-weight value for \(m\ge3\). No independent validation or general historical-priority guarantee is claimed.

## References
1. F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370 (first posted 2017-12-20), https://arxiv.org/abs/1712.07370.
2. A. Fontan and C. Altafini, *On the properties of Laplacian pseudoinverses*, arXiv:2109.14587 (first posted 2021-09-29), https://arxiv.org/abs/2109.14587.
3. American Mathematical Society, MSC2020, code 47A10 (spectrum and resolvent), https://mathscinet.ams.org/msc/msc2020.html?t=47A10.
