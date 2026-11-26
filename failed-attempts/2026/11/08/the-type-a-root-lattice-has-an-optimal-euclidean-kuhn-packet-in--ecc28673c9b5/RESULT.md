# The type-A root lattice has an optimal Euclidean Kuhn packet in every dimension

## Finding
For every integer \(n\ge5\), put \(N=n+1\), let \(H=\{x\in\mathbb R^N:\sum_{j=1}^N x_j=0\}\) with its induced Euclidean metric, let \(A_n=H\cap\mathbb Z^N\), and let \(B_2^n\) denote the unit ball of \(H\). The common-frame Kuhn-packet radius of Fei Xue equals the ordinary lattice covering radius:
\[
\boxed{\kappa(B_2^n,A_n)=\mu(B_2^n,A_n)=\sqrt{\frac{\lfloor N^2/4\rfloor}{N}}.}
\]
A single **fixed** optimal frame is the standard simple-root basis \(B=(e_1-e_2,e_2-e_3,\ldots,e_n-e_{n+1})\). This is optimal under the original common-independent-frame definition, without passing to the relaxed periodic-triangulation invariant.

The same fixed frame has an explicit **circumsphere spectrum**. Given a permutation \(\sigma\in S_n\), let \(p_i=\sigma^{-1}(i)\) and \(k_\sigma=1+\#\{i\in\{1,\ldots,n-1\}:p_i<p_{i+1}\}\). The unique Euclidean sphere through all \(n+1\) vertices of its permutation simplex has squared radius
\[
\boxed{\rho_\sigma^2=\frac{k_\sigma(N-k_\sigma)}{N}.}
\]
For every \(1\le k\le n\), exactly \(\left\langle {n\atop k-1}\right\rangle\) permutations have \(k_\sigma=k\), where the brackets are the Eulerian numbers. These are **circumsphere** radii, not asserted to be the individual minimum-enclosing-ball radii. Their largest value is the common optimal fitting-radius square. In particular, when \(N=2m\) the largest cosphere radius occurs for exactly \(\left\langle{2m-1\atop m-1}\right\rangle\) permutations; when \(N=2m+1\) the count is \(2\left\langle{2m\atop m-1}\right\rangle\).

## Assumptions and scope
The lattice is the **root** lattice \(A_n=\{z\in\mathbb Z^{n+1}:\sum z_j=0\}\), not its dual or an arbitrarily rescaled realization; all radii use the Euclidean metric inherited from \(\mathbb R^{n+1}\). The lattice dimension is \(n\), and \(n\ge5\) in the stated new result. The argument itself also holds for smaller dimensions, where some special cases were previously known. No assertion of optimality or uniqueness among **all** frames is made beyond the exhibited optimal frame.

For a compact set \(C\subset H\), let \(r(C)=\inf\{r\ge0:C\subset c+rB_2^n\text{ for some }c\in H\}\). For an ordered linearly independent lattice frame \(F=(b_1,\dots,b_n)\) and \(\sigma\in S_n\), let
\[
\Delta_\sigma(F)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},\ldots,\sum_{i=1}^n b_i\}.
\]
Set \(\kappa_F=\max_{\sigma\in S_n}r(\Delta_\sigma(F))\) and \(\kappa=\inf_F\kappa_F\). The lattice covering radius \(\mu\) is the least \(r\) such that \(A_n+rB_2^n=H\).

## Proof
**Step 1: covering-radius lower bound.** The Voronoi cell of \(A_n\) at the origin is exactly
\[
V=\{x\in H:\max_jx_j-\min_jx_j\le1\}.
\]
Indeed, every root \(e_i-e_j\) belongs to \(A_n\) and has squared norm \(2\), so the Voronoi inequalities \(2\langle x,e_i-e_j\rangle\le2\) force the stated range bound. Conversely, if the range is at most \(1\) and \(z\in A_n\), write \(t=\sum_{z_j>0}z_j=\sum_{z_j<0}(-z_j)\). Then
\[
\langle x,z\rangle\le t(\max x-\min x)\le t\le\tfrac12\sum_jz_j^2=\tfrac12\|z\|^2,
\]
using \(z_j^2\ge|z_j|\) for integral coordinates. Thus \(x\) lies in the origin Voronoi cell.

Let \(P(y)=y-(\sum_jy_j/N)\mathbf1\) be orthogonal projection onto \(H\). The range criterion implies \(V=P([0,1]^N)\): projection does not change coordinate range, and any \(x\in V\) admits a diagonal translate into \([0,1]^N\). Every \(y\in[0,1]^N\) is a convex combination of its vertices, and the squared norm is convex, so the maximum norm on \(V\) occurs at some \(P(\mathbf1_S)\), for \(S\subseteq\{1,\ldots,N\}\). For \(|S|=k\),
\[
\|P(\mathbf1_S)\|^2=k-\frac{k^2}{N}=\frac{k(N-k)}{N}.
\]
Consequently \(\mu^2=\lfloor N^2/4\rfloor/N\). This Voronoi characterization and projected-cube picture are classical, and are included here with a self-contained proof to fix the normalization.

**Step 2: a common root frame fits every permutation simplex.** Fix \(b_i=e_i-e_{i+1}\). These are a lattice basis, since every \(z\in A_n\) has the telescoping decomposition \(z=\sum_{i=1}^{n}(\sum_{j=1}^{i}z_j)b_i\). For \(\sigma\in S_n\), let \(p_i\) be the position of \(i\) in \(\sigma\). Define an integer vector \(m=m(\sigma)\in\mathbb Z^N\) by
\[
m_1=0,\quad m_N=-1,\qquad
m_j=\begin{cases}-1,&p_{j-1}<p_j,\\0,&p_{j-1}>p_j,\end{cases}\quad (2\le j\le N-1).
\]
Hence \(\sum_jm_j=-k_\sigma\). At any prefix of the ordered roots, coordinate \(j\) is \(+1\) if root \(b_j\) has appeared but \(b_{j-1}\) has not, \(-1\) if \(b_{j-1}\) has appeared but \(b_j\) has not, and \(0\) otherwise, with missing boundary roots interpreted as absent. Therefore **every** vertex \(v\) of \(\Delta_\sigma(B)\) satisfies
\[
v_j\in\{m_j,m_j+1\}\quad(1\le j\le N),\qquad \sum_jv_j=0.
\]
The vector \(a=m+\frac12\mathbf1\) is the center of this shifted unit cube, and its orthogonal projection
\[
c_\sigma=P(a)=m+\frac{k_\sigma}{N}\mathbf1\in H
\]
is the center of a Euclidean sphere containing all \(n+1\) simplex vertices. For every such vertex, \(\|v-a\|^2=N/4\) and \(\langle v-a,\mathbf1/\sqrt N\rangle=(k_\sigma-N/2)/\sqrt N\). Orthogonal Pythagoras therefore gives
\[
\|v-c_\sigma\|^2=\frac N4-\frac{(k_\sigma-N/2)^2}{N}=\frac{k_\sigma(N-k_\sigma)}{N}.
\]
The vertices are affinely independent because \(B\) is a lattice basis, so this is their **unique circumsphere**. Convexity of the closed Euclidean ball shows that the **entire** simplex lies in that radius-\(\rho_\sigma\) ball. Since \(1\le k_\sigma\le n=N-1\),
\[
\kappa_B^2=\left(\max_\sigma r(\Delta_\sigma(B))\right)^2\le\max_{1\le k\le N-1}\frac{k(N-k)}{N}=\mu^2.
\]
Fei Xue's general comparison \(\mu\le\kappa\) (or its standard triangulation covering argument), together with \(\kappa\le\kappa_B\), yields \(\mu\le\kappa\le\kappa_B\le\mu\), proving equality and optimality of this fixed frame. This argument does not assume that each displayed circumsphere is a minimum enclosing sphere of its simplex.

**Step 3: the spectrum is Eulerian.** The integer \(k_\sigma-1\) counts ascents in the inverse permutation \(\sigma^{-1}\). The inverse map is a bijection of \(S_n\); by definition, the number with \(k_\sigma=k\) is the Eulerian number \(\left\langle{n\atop k-1}\right\rangle\). The function \(k\mapsto k(N-k)\) is largest at the middle integer(s). Eulerian symmetry \(\left\langle{n\atop r}\right\rangle=\left\langle{n\atop n-1-r}\right\rangle\) gives the stated peak multiplicities. This completes the proof for all \(n\ge5\) (in fact, the identities hold in every positive dimension).

## Verification
Run the standalone Python 3 file `verify.py`; it uses only the standard library. It checks all \(n!\) root permutations and all \(n+1\) simplex vertices for each \(1\le n\le7\), verifies the exact rational circumsphere equation and independently generated Eulerian counts, and tests finitely many integer Voronoi inequalities for \(n\le3\). The checked run returned `PASS: 46387 exact finite checks`. These finite computations are supplementary consistency checks, **not** a proof for infinitely many dimensions. The universal proof is the coordinate-and-Voronoi argument above.

## Relationship to prior work
Fei Xue, *On \(\kappa\)-covering minima* (arXiv:2610.39034v1, first public 2026-10-28), defines the common-frame invariant, proves \(\mu\le\kappa\), and computes equality for coordinate lattices with \(\ell_p\) bodies. The inspected primary text does not state the type-A root-lattice equality, the exhibited simple-root frame, or the Eulerian cosphere spectrum. Minho Kim, *Algebraic Characterization of the Voronoi Cell Structure of the \(A_n\) Lattice* (arXiv:2304.10186v1), establishes the classical projected-cube Voronoi picture. That structural fact fixes the lower bound but does not provide the new common-frame upper construction. Earlier special-dimensional computations, including a rank-four case, must not be treated as new; the substantive range here is **all \(n\ge5\)** and the all-dimensional spectrum. Koca et al. (2018) study root-lattice Voronoi and Delaunay cells, not the newly defined packet invariant in the available abstract.

## Limitations
This concerns Euclidean balls and the unscaled root lattice \(A_n\) only. It does not classify all optimal frames, assert optimal individual simplex balls at the explicitly exhibited circumsphere centers, or extend equality to arbitrary lattices; Xue proves that some Euclidean lattice families have a large \(\kappa/\mu\) gap. The result is established by direct proof and finite supplementary checks, not an independent mathematical audit. An older equivalent formulation under unrelated triangulation language remains a possible historical-priority risk, especially in full texts that were inaccessible during this review.

## References
- F. Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1 (2026-10-28). https://arxiv.org/html/2610.39034v1 .
- M. Kim, *Algebraic Characterization of the Voronoi Cell Structure of the \(A_n\) Lattice*, arXiv:2304.10186v1 (2023-04-20). https://arxiv.org/html/2304.10186v1 .
- M. Koca, N. O. Koca, A. Al-Siyabi, R. Koc, *Explicit Construction of the Voronoi and Delaunay Cells of \(W(A_n)\) and \(W(D_n)\) Lattices and Their Facets*, arXiv:1804.05836 (2018-04-16). https://arxiv.org/abs/1804.05836 .
- Y. Lian and F. Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584 (2026-06-12). https://arxiv.org/abs/2606.14584 .
