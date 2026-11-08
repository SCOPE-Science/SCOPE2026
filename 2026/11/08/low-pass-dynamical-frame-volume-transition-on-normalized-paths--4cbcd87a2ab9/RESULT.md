# Low-pass dynamical frame-volume transition on normalized paths

## Finding
Let \(P_{n+1}\) be the path with vertices \(0,1,\ldots,n\), where \(n\ge2\), and let \(\mathcal H_r\) be the span of its \(r\) lowest normalized-Laplacian eigenvectors, with \(2\le r\le n+1\). For any spectral evolution whose eigenvalues on these modes are pairwise distinct, take the \(r\) consecutive-time measurements at one fixed vertex \(j\). Write \(G_{r,j}\) for the resulting \(r\)-dimensional frame Gramian. With \(d_0=d_n=1\) and \(d_j=2\) otherwise, the **exact D-optimal volume ratio** is

\[
\frac{\det G_{r,j}}{\det G_{r,0}}
=d_j^r\prod_{k=1}^{r-1}\cos^2\!\left(\frac{\pi k j}{n}\right).
\]

In particular, for the first **three** modes, the unique maximizing vertices are exactly \(\{0,n\}\) when \(2\le n\le5\), and exactly \(\{1,n-1\}\) when \(n\ge6\). Thus a path of **seven vertices** is the sharp transition from endpoint sensors to their immediate neighbors.

More generally, for every \(r\ge2\), if \(n\ge4(r-1)^3\), the only D-optimal vertices are \(1\) and \(n-1\). The statement applies, for example, to normalized adjacency evolution and to every positive-time heat evolution, not just to one chosen time propagator.

## Assumptions and scope
We work over \(\mathbb C\) with its standard Euclidean inner product. Denote path degrees by \(d_j\), let \(A\) be ordinary adjacency, let \(D\) be the diagonal degree matrix, and put \(B=D^{-1/2}AD^{-1/2}\). The normalized Laplacian is \(L=I-B\). Its ordered eigenvalues are \(1-\cos(\pi k/n)\), \(k=0,\ldots,n\).

For fixed \(2\le r\le n+1\), define \(\mathcal H_r\) to be the span of the eigenvectors indexed by \(0\le k<r\). An admissible spectral evolution \(T\) has these eigenvectors and assigns pairwise distinct (possibly complex) eigenvalues \(a_0,\ldots,a_{r-1}\); outside \(\mathcal H_r\) its action is irrelevant. For each vertex \(j\), define
\[
\mathcal O_{r,j}f=\bigl((T^t f)(j)\bigr)_{t=0}^{r-1},\qquad
G_{r,j}=\mathcal O_{r,j}^{*}\mathcal O_{r,j}\quad\text{on }\mathcal H_r.
\]
D-optimality means maximizing \(\det G_{r,j}\), equivalently maximizing the squared volume spanned by the \(r\) analysis vectors. No assertion about minimizing the condition number or maximizing the smallest eigenvalue is made. Since the endpoint Gramian has positive determinant, the volume ratio is well-defined.

## Proof
**1. Exact normalized-path eigenvectors.** For \(0\le k\le n\) the real eigenvector
\[
 u_k(j)=c_k\sqrt{d_j}\cos\!\left(\frac{\pi kj}{n}\right),\qquad
 c_k=\begin{cases}(2n)^{-1/2},& k\in\{0,n\},\\ n^{-1/2},&1\le k<n,\end{cases}
\]
is orthonormal and satisfies \(Bu_k=\cos(\pi k/n)u_k\). The eigenvector relation follows at interior vertices from the cosine addition formula, and at the two endpoints from the degree-one boundary equations. Orthogonality follows from symmetry of \(B\) and simplicity of the displayed eigenvalues; normalization follows by summing \(d_j\cos^2(\pi kj/n)\). These formulas remain valid at both endpoints and when \(n=2\).

**2. Exact frame-volume factorization.** Express \(\mathcal O_{r,j}\) in the eigenbasis \(u_0,\ldots,u_{r-1}\). Its entries are \(a_k^t u_k(j)\). Its determinant is
\[
 \det\mathcal O_{r,j}
 =\left(\prod_{k=0}^{r-1}u_k(j)\right)
   \prod_{0\le h<k<r}(a_k-a_h).
\]
Distinctness of the \(a_k\) makes the Vandermonde factor nonzero, independently of \(j\). At the endpoint \(j=0\), the eigenvectors have entries \(u_k(0)=c_k\), while at a general vertex the ratio of each entry is \(\sqrt{d_j}\cos(\pi kj/n)\). Squaring absolute determinants proves the displayed Gramian ratio, including its zero cases and the absence of evolution-dependent terms.

**3. Sharp three-mode transition.** With \(r=3\), maximizing the determinant is equivalent to maximizing
\[
 Q_j=d_j^{3/2}\left|\cos\!\left(\frac{\pi j}{n}\right)
\cos\!\left(\frac{2\pi j}{n}\right)\right|.
\]
The endpoints have value \(1\). Direct exact trigonometric evaluation for \(n=2,3,4,5\) shows that every interior value is strictly below \(1\); the largest is at most \(1/\sqrt2\). For \(n\ge6\), use reflection to restrict to \(0\le j\le n/2\) and write \(f(\theta)=|\cos\theta\cos2\theta|\). On \([0,\pi/4]\), \(f\) is strictly decreasing; on \([\pi/4,\pi/2]\), its maximum is exactly \(2/(3\sqrt6)\) (differentiate \(\cos\theta-2\cos^3\theta\)). Since
\[
 f(\pi/n)\ge f(\pi/6)=\sqrt3/4>2/(3\sqrt6),
\]
the nearest interior vertices \(j=1,n-1\) uniquely maximize \(Q_j\) among interior vertices. They also strictly beat endpoints, since \(2^{3/2}\sqrt3/4=\sqrt6/2>1\). This proves both sides of the exact transition.

**4. All fixed bandwidths: an explicit eventual bound.** Put \(k=r-1\), assume \(n\ge4k^3\), and write \(F_k(\theta)=\prod_{\ell=1}^k|\cos(\ell\theta)|\). By reflection it suffices to compare \(\theta=\pi j/n\) in \([0,\pi/2]\). On \([0,\pi/(2k)]\), every cosine factor is nonnegative and the product is strictly decreasing in positive \(\theta\). On \([\pi/(2k),\pi/2]\),
\[
 F_k(\theta)\le\cos\theta\le\cos\!\left(\frac{\pi}{2k}\right).
\]
Because \(n\ge4k^3\) and \(\sum_{\ell=1}^k\ell^2\le k^3\), the elementary inequalities \(\cos t\ge1-t^2/2\) and \(\prod(1-b_i)\ge1-\sum b_i\) yield
\[
 F_k(\pi/n)\ge1-\frac{\pi^2k^3}{2n^2}
 \ge1-\frac{\pi^2}{32k^3}
 >1-\frac{1}{2k^2}
 \ge\cos\!\left(\frac{\pi}{2k}\right).
\]
The final inequality follows from \(\sin t\ge2t/\pi\) on \([0,\pi/2]\). Thus \(j=1,n-1\) uniquely maximize among interior vertices. They beat endpoints: for \(k\ge2\), the product is greater than \(\cos(\pi/(2k))\ge1/\sqrt2\), and the interior degree factor is \(2^{r/2}\ge2^{3/2}\); for \(k=1\), \(n\ge4\) gives \(2\cos(\pi/n)>1\). Hence they are the unique global maximizing sites.

## Verification
The companion `CHECK.py` uses only the Python standard library. It verifies the normalized-path eigenvector formulas against tridiagonal matrix multiplication, computes three-time sensing determinants independently from matrix iteration for small paths, checks the sharp three-mode maximizer classification for every \(2\le n\le250\), and checks the all-band sufficient-bound sites for \(2\le r\le14\). Run `python3 CHECK.py` after extracting the file. These are reproducibility and error-detection checks; the all-parameter assertion is proved by the inequalities above rather than by finite enumeration.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani introduce dynamical frames on graph Paley–Wiener spaces, with a finite-path numerical study. The present statement gives an exact D-optimal one-vertex criterion and a sharp three-mode phase transition, independent of the selected injective spectral evolution. Parlangeli and Notarstefano investigate observability for path and cycle graphs using the combinatorial Laplacian; observability alone does not rank D-optimal frame volumes. A previously reported theorem on **full-band** normalized-path dynamical sampling gives endpoint optimality. The present low-pass problem is different and has the opposite optimal vertices as soon as the three-mode path has at least seven vertices. The general finite-index dynamical-frame theory of Cabrelli and collaborators supplies the overarching frame framework but does not itself provide the evaluated vertex-optimality law.

## Limitations
The result is for paths, one vertex, \(r\) consecutive times, and D-optimal determinant volume. It does not optimize condition numbers or smallest singular values, multiple simultaneous sensors, arbitrary graph families, or arbitrary nonconsecutive observation times. The all-band sufficient length \(n\ge4(r-1)^3\) is not claimed sharp. Publication priority cannot be fully certified: the accessible introduction and abstract of the 2026 graph-sampling source were read, but the detailed finite-path section was not accessible on subsequent fetches; an earlier equivalent exact D-optimal calculation under different terminology remains possible. Independent scientific validation has not been performed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472 (first submitted 2026-09-21). https://arxiv.org/abs/2609.25472
2. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556 (2011). https://arxiv.org/abs/1109.3556
3. C. Cabrelli, U. Molter, V. Paternostro, F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384 (2017). https://arxiv.org/abs/1702.03384
4. *Universal endpoint optimality for dynamical sampling on normalized paths*, publicly indexed result (2026-10-11). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f
5. I. Yin and L. P. Schaposnik, *Movement Stability of D-Optimal Sensor Placement Under Projector Perturbations*, arXiv:2610.08152 (2026). https://arxiv.org/abs/2610.08152
