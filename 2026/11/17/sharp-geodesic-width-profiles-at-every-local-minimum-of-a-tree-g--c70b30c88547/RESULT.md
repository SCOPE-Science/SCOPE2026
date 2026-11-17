# Sharp geodesic width profiles at every local minimum of a tree graphical zonotope

## Finding
Let \(T=(V,E)\) be any unweighted tree with \(n=|V|\ge3\). In the zero-sum Euclidean subspace \(H=\{u\in\mathbb R^V:\sum_{v\in V}u_v=0\}\), consider its centered graphical zonotope
\[
Z_T=\sum_{\{a,b\}\in E}[-(e_a-e_b)/2,(e_a-e_b)/2].
\]
Its Euclidean projection width along a unit vector is
\[
W_T(u)=\sum_{\{a,b\}\in E}|u_a-u_b|,\qquad u\in H,\quad \|u\|_2=1.
\]
There are **exactly \(2(n-1)\) strict local minima** on this oriented unit sphere: for each edge \(e\), the two signs of the normalized centered indicator of either component of \(T\setminus e\). There are no other local minima.

For each edge \(e\), choose either component \(S_e\) of \(T\setminus e\), put \(s_e=|S_e|\), and define
\[
h_e=\mathbf1_{S_e}-\frac{s_e}{n}\mathbf1,\qquad
K_{ef}=\langle h_e,h_f\rangle=|S_e\cap S_f|-\frac{s_es_f}{n},\qquad
w_e=K_{ee}^{-1/2}=\sqrt{\frac{n}{s_e(n-s_e)}}.
\]
The two orientations of its local minimum are \(\pm u_e\), where \(u_e=h_e/\sqrt{K_{ee}}\). For every \(n\ge3\), define the strictly positive sharp angular coefficient
\[
\gamma_e=
\min_{f\in E\setminus\{e\}}
\frac{1-|K_{ef}|/K_{ee}}
{\sqrt{K_{ff}-K_{ef}^{2}/K_{ee}}}.
\]
This formula is independent of the arbitrary choices of component signs. At *every* sufficiently small prescribed spherical angle \(\theta\), the exact smallest width about \(u_e\) is
\[
\min_{\substack{v\in H,\ \|v\|_2=1\\ \langle v,u_e\rangle=\cos\theta}}
W_T(v)
=
w_e\cos\theta+\gamma_e\sin\theta,
\qquad 0<\theta<\arctan\left(\frac{w_e}{\sqrt2}\right).
\]
The minimum is attained for every angle in the stated interval. The same statement holds about \(-u_e\).

For the path on \(n\) vertices, an edge dividing the path into groups of sizes \(j\) and \(n-j\) has
\[
\gamma_e=\frac1{\sqrt{M(M-1)}},\quad M=\max\{j,n-j\}.
\]
For the star on \(n\) vertices, every edge has
\[
\gamma_e=\sqrt{\frac{n-2}{n-1}}.
\]
Thus leaf-edge directions in paths and stars have **the same width** \(\sqrt{n/(n-1)}\), but their sharp angular-growth coefficients differ by the factor \(n-2\).

## Assumptions and scope
All trees are finite, simple, unweighted, connected, and have at least three vertices. The Euclidean norm and spherical angle are those inherited from the ambient coordinate space. A local minimum means local minimality on the *entire* unit sphere in \(H\), not solely in a sign chamber. Directions are oriented, so antipodal minima count separately. The angle interval above is sufficient and uniform over tangent directions; no optimality of its endpoint is claimed.

## Proof
**1. Width and fundamental cut coordinates.** Each centered segment contributes \(|u_a-u_b|\) to the projection length, giving the width identity. Orient every edge \(e=(a_e,b_e)\) from the chosen side \(S_e\) to its complement, and define \(d_e(x)=x_{a_e}-x_{b_e}\). Removing a different edge \(f\ne e\) does not separate the endpoints of \(e\); consequently \(d_e(h_f)=0\), while \(d_e(h_e)=1\). Hence \(\{h_e:e\in E\}\) is a dual basis to the \(n-1\) edge-difference functionals on \(H\):
\[
x=\sum_{f\in E}d_f(x)h_f.
\]
The cut Gram formula is obtained by expanding the two centered indicators. In particular \(K_{ee}=s_e(n-s_e)/n>0\), and \(u_e\) has exactly one nonzero edge difference, equal to \(w_e\).

**2. Exclusion of all other local minima.** A unit vector in \(H\) cannot have zero active edges: connectedness would make it constant, hence zero. Let \(u\) have \(k\ge2\) nonzero edge differences. Within the linear subspace of vectors having zero differences at all its zero-difference edges, the dimension is \(k\): removing the \(k\) nonzero-difference edges leaves \(k+1\) connected components and imposing mean zero removes one degree of freedom. In a neighborhood of \(u\) inside this subspace the signs of the \(k\) nonzero differences are fixed, so \(W_T\) is a strictly positive *linear functional* on the intersection with the unit sphere. On a sphere of dimension \(k-1\ge1\), a positive linear functional cannot have a local minimum at a point where it is positive: its only stationary point with positive value is a strict local maximum. Thus every local minimum has exactly one nonzero edge difference and must be one of \(\pm u_e\).

**3. Strict positivity of the cut coefficients.** For any two proper nonempty subsets \(S,F\subset V\), write \(a=|S\cap F|\), \(b=|F\setminus S|\), and \(s=|S|\). Then
\[
\langle\mathbf1_S-s\mathbf1/n,\mathbf1_F-|F|\mathbf1/n\rangle
=\frac{(n-s)a-sb}{n}.
\]
Its absolute value is at most \(s(n-s)/n\), with equality only when \(F=S\) or \(F=V\setminus S\). Distinct tree edges define neither equal nor complementary splits. Therefore
\[
|K_{ef}|<K_{ee}\quad(e\ne f).
\]
Moreover the projected vectors defined next are nonzero because the centered indicators for distinct edges form a basis.

**4. Exact tangent minimization.** Fix \(e\). A tangent vector \(z\in H\) orthogonal to \(u_e\) has, by the dual cut basis and the orthogonality equation, the unique expansion
\[
z=\sum_{f\ne e}d_f(z)\,\overline h_f,\qquad
\overline h_f=h_f-\frac{K_{ef}}{K_{ee}}h_e,
\quad\|\overline h_f\|_2^2=K_{ff}-\frac{K_{ef}^2}{K_{ee}}>0.
\]
Its directional width increment at \(u_e\), where the edge \(e\) has positive difference, is
\[
L_e(z)=d_e(z)+\sum_{f\ne e}|d_f(z)|
=\sum_{f\ne e}\left(|d_f(z)|-\frac{K_{ef}}{K_{ee}}d_f(z)\right).
\]
Let \(\gamma_e\) be the displayed minimum of one-coordinate ratios. Using strict positivity of \(1-|K_{ef}|/K_{ee}\) and the triangle inequality,
\[
L_e(z)\ge\sum_{f\ne e}|d_f(z)|\left(1-\frac{|K_{ef}|}{K_{ee}}\right)
\ge\gamma_e\sum_{f\ne e}|d_f(z)|\|\overline h_f\|_2
\ge\gamma_e\|z\|_2.
\]
Equality holds on a single projected cut \(\overline h_f\), choosing the positive sign when \(K_{ef}\ge0\) and the negative sign otherwise, for an edge \(f\) attaining the smallest ratio. This proves the exact sharp tangent coefficient and its positivity.

**5. A uniform finite-angle interval.** Every unit tangent vector \(z\perp u_e\) satisfies \(|d_e(z)|\le\|e_{a_e}-e_{b_e}\|_2=\sqrt2\). For \(v=u_e\cos\theta+z\sin\theta\), the edge \(e\) difference stays positive whenever \(\tan\theta<w_e/\sqrt2\). At all other edges, the base vector has zero difference. Therefore throughout this interval
\[
W_T(v)=w_e\cos\theta+L_e(z)\sin\theta
\ge w_e\cos\theta+\gamma_e\sin\theta.
\]
Taking the equality tangent vector from Step 4 attains this bound at each angle. The positive first-order coefficient forces \(u_e\) to be a strict local minimum. Symmetry of \(W_T\) gives the antipodal statement.

**6. Path and star specializations.** For a path, index the edges in order and take its initial segments as the cut sides. For an edge at position \(j\), if \(i<j\), direct substitution into the Gram formula gives candidate coefficient \(\sqrt{(j-i)/(ij)}\). If \(i>j\), it gives \(\sqrt{(i-j)/((n-i)(n-j))}\). Within each range the minimum occurs at \(i=j-1\) or \(i=j+1\), respectively, whenever the neighboring edge exists. Their minimum is \(1/\sqrt{M(M-1)}\). For the star, choosing the singleton leaves as cut sides gives diagonal Gram entries \((n-1)/n\) and off-diagonal entries \(-1/n\); all candidate ratios equal \(\sqrt{(n-2)/(n-1)}\). The leaf-edge ratio follows by dividing the star coefficient by the path coefficient at \(j=1\).

## Verification
Run `python3 tree_width_checker.py` using Python 3. The checker generates **all 1,440 labeled trees with \(3\le n\le6\)** via Prüfer codes, verifies exact rational Gram formulas, tangent positivity and attained sharp ratios, and checks **56,262** additional exact tangent mixtures. It checks the path and star closed forms for \(3\le n\le14\), together with attained finite-angle formulas on sample geodesics. These finite tests are independent diagnostics; the arbitrary-size conclusion follows from the proof above.

## Relationship to prior work
Padrol, Pilaud and Poullot developed the deformation-cone and combinatorial theory of graphical zonotopes, including trees as a particularly simple class. General work on graph total variation and one-homogeneous Rayleigh quotients addresses optimization and global cuts. Earlier geometric results also identify global minimum widths through cut functionals. These foundations do not by themselves provide the complete classification of **all** strict spherical local minima together with the sharp, attained, tree-dependent angular coefficients and the path-versus-star stability factor obtained here. The global-minimum cut formula is not claimed as new.

## Limitations
The theorem is for **unweighted trees** with standard Euclidean coordinates. It does not classify local maxima, all critical points, weighted-graph landscapes, or angles beyond the stated interval. Historical novelty relative to inaccessible or unindexed work is not conclusively established; independent review is outstanding. The exact-rational program samples finitely many trees and angles and cannot replace the proof for all sizes.

## References
- A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 2021-11-24; *Discrete & Computational Geometry* 73 (2025), 447–465; DOI 10.1007/s00454-023-00586-x. Full text: https://link.springer.com/article/10.1007/s00454-023-00586-x
- T. Feld, J.-F. Aujol, G. Gilboa, N. Papadakis, *Rayleigh quotient minimization for absolutely one-homogeneous functionals*, *Inverse Problems* 35 (2019), 064003; DOI 10.1088/1361-6420/ab0cb2.
- V. Kolmogorov, T. Pock, M. Rolinek, *Total Variation on a Tree*, *SIAM Journal on Imaging Sciences* 9 (2016), 605–636; arXiv:1502.07770; DOI 10.1137/15M1010257.
