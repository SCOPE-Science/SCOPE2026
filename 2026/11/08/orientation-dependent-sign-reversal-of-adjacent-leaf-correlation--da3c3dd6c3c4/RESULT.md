# Orientation-dependent sign reversal of adjacent leaf correlations in uniform prism spanning trees

## Finding
Let \(G_m=C_m\square K_2\), \(m\ge3\), and let \(\mathcal T_m\) be a uniformly selected spanning tree of \(G_m\). Set \(L_v={\bf1}\{\deg_{\mathcal T_m}(v)=1\}\). For an adjacent pair \(u,v\), distinguish a **rail pair** (an edge belonging to either cycle) from a **rung pair** (an edge joining the layers). Then
\[
 \operatorname{Cov}(L_u,L_v)\begin{cases}<0,&\text{rail pair, }m=3,\\>0,&\text{rail pair, }m\ge4,\end{cases}
 \qquad
 \operatorname{Cov}(L_u,L_v)\begin{cases}>0,&\text{rung pair, }m=3,4,\\<0,&\text{rung pair, }m\ge5.\end{cases}
\]
In particular, for every \(m\ge5\), the two kinds of adjacent vertex pairs on the *same cubic vertex-transitive graph* have opposite signs of leaf-indicator covariance. The limits are
\[
 \lim_{m\to\infty}\operatorname{Cov}_{\rm rail}(L_u,L_v)=\frac{23\sqrt3}{3}-\frac{53}{4}>0,
 \qquad
 \lim_{m\to\infty}\operatorname{Cov}_{\rm rung}(L_u,L_v)=3\sqrt3-\frac{21}{4}<0.
\]

## Assumptions and scope
The prism has vertex set \(\{(j,\epsilon):j\in\mathbb Z/m\mathbb Z,\ \epsilon\in\{0,1\}\}\), with edges \((j,\epsilon)(j+1,\epsilon)\) and \((j,0)(j,1)\). For \(m=3\) the graph is the triangular prism; no parallel edges or self-loops are permitted. Spanning trees are uniformly weighted. Both covariances refer to the original vertices under the *same* randomly chosen tree.

Write \(A_m=T_m(2)\), \(B_m=U_{m-1}(2)\), where \(T_m,U_m\) are the classical Chebyshev polynomials of the first and second kinds. Equivalently \(A_0=1,A_1=2\), \(B_0=0,B_1=1\), and both obey \(X_{m+1}=4X_m-X_{m-1}\). Define the following integers:
\[
\begin{aligned}
 F_m&=m(A_m-1),\\
 H_m&=\tfrac12[A_m-B_m-mA_m+2mB_m-1],\\
 C_m&=\tfrac12[-A_m+2B_m-4mA_m+7mB_m-1],\\
 R_m&=B_{m-1}.
\end{aligned}
\]
Their interpretations are the spanning-tree counts of \(G_m\), of \(G_m\) with one marked vertex deleted, and with respectively two adjacent rail vertices or two adjacent rung vertices deleted. The full formulas for the probabilities and covariances are
\[
 \mathbb P(L_u=1)=\frac{3H_m}{F_m},\qquad
 \mathbb P(L_u=L_v=1)=\begin{cases}4C_m/F_m,&uv\text{ rail},\\4R_m/F_m,&uv\text{ rung},\end{cases}
\]
\[
 \operatorname{Cov}_{\rm rail}=\frac{4C_mF_m-9H_m^2}{F_m^2},
 \qquad
 \operatorname{Cov}_{\rm rung}=\frac{4R_mF_m-9H_m^2}{F_m^2}.
\]

## Proof
**1. Leaf deletion and the full prism count.** If a vertex of degree three is required to be a tree leaf, choose one of its three original incident edges and attach that leaf to a spanning tree of the graph with that vertex deleted. These choices are disjoint and exhaustive, giving \(3H_m\) possibilities. If two adjacent vertices are simultaneously leaves, their common edge cannot be selected in a tree with more than two vertices. Each therefore has exactly two choices for attachment to the complement; this yields \(4C_m\) or \(4R_m\) choices, respectively. The matrix-tree theorem, or the Laplacian spectrum \(2-2\cos(2\pi j/m)\) and \(4-2\cos(2\pi j/m)\) for \(0\le j<m\), yields
\[
 \tau(G_m)=m\left(T_m(2)-1\right)=F_m.
\]
Indeed, the nonzero Laplacian eigenvalues multiply to \(m^2\prod_{j=0}^{m-1}[4-2\cos(2\pi j/m)]\); dividing by the \(2m\) vertices and applying \(\prod_j[4-2\cos(2\pi j/m)]=2[T_m(2)-1]\) proves the identity. Deleting the two ends of a rung leaves the open ladder \(P_{m-1}\square K_2\), whose spanning-tree counts obey \(R_{m+2}=4R_{m+1}-R_m\) with \(R_3=4\) and \(R_4=15\); thus \(R_m=U_{m-2}(2)=B_{m-1}\).

**2. Transfer enumeration for the two remaining deletion counts.** Delete a marked top vertex. Slice the surviving graph along successive columns, keeping the bottom vertex of the first column as a distinguished pin \(p\) until closure. After processing a column the frontier consists of its top and bottom vertices \(a,b\) and the pin \(p\). A forest can have five relevant partitions of this frontier, in this order:
\[
 (a)(b)(p),\quad(a)(bp),\quad(ab)(p),\quad(abp),\quad(ap)(b).
\]
All cycles are forbidden and no component lacking all future frontier vertices may be discarded. Adding the next column entails a top horizontal edge, a bottom horizontal edge, and a rung, with each present or absent. Enumerating all eight choices subject to those two forest conditions gives the integer transfer matrix (columns index old partitions)
\[
 M=\begin{pmatrix}1&1&2&1&1\\0&1&0&1&0\\1&1&3&1&1\\0&1&0&3&1\\0&0&0&1&1\end{pmatrix}.
\]
After the first three columns, the initial frontier vectors are
\[
 h_0=(5,2,6,4,1)^{\mathsf T},\quad c_0=(2,1,2,1,0)^{\mathsf T}.
\]
The first vector arises with only the first marked top vertex missing, and the second with the first two adjacent top vertices missing; in both cases the bottom pin persists. Closing the bottom cycle, with optional final bottom edge to the pin, accepts exactly the partitions weighted by \(w=(0,0,1,1,1)^{\mathsf T}\). It follows, for each \(m\ge3\), that
\[
 H_m=w^{\mathsf T}M^{m-3}h_0,\qquad C_m=w^{\mathsf T}M^{m-3}c_0.
\]
Each transition and both initial vectors can be reconstructed by enumerating small local edge subsets; the supplied standalone checker does so independently, including the closure vector. Direct multiplication verifies
\[
 (M-I)(M^2-4M+I)^2=0.
\]
Therefore both sequences obey the order-five recurrence associated with \((x-1)(x^2-4x+1)^2\). The stated Chebyshev expressions have the same recurrence: their terms are linear combinations of \(1,(2+\sqrt3)^m,(2-\sqrt3)^m,m(2+\sqrt3)^m,m(2-\sqrt3)^m\). Both formulas agree with the transfer counts at five consecutive indices \(m=3,4,5,6,7\):
\[
 (H_m,C_m)=(11,3),(50,15),(216,65),(912,272),(3795,1121).
\]
The recurrence gives equality for every \(m\ge3\), not merely for the checked indices.

**3. Exact sign certificates valid for all sizes.** Set \(q=\sqrt3\), \(z=2+q>3\), and \(t=z^m\). The Chebyshev identities give \(A_m=(t+t^{-1})/2\) and \(B_m=(t-t^{-1})/(2q)\). Define \(D_{\rm rail}=4C_mF_m-9H_m^2\) and \(D_{\rm rung}=4R_mF_m-9H_m^2\). Since \(R_m=(t/z-z/t)/(2q)\), multiplying each \(D\) by \(16t^2\) gives quartic polynomials in \(t\):
\[
 16t^2D_\star=\sum_{j=0}^4 a_{\star,j}(m)t^j.
\]
For the rail case, the coefficients, in descending degree, are
\[
\begin{aligned}
 a_{h,4}&=(-53+92q/3)m^2+(22-38q/3)m-12+6q,\\
 a_{h,3}&=(64-112q/3)m^2+(-36+40q/3)m+36-12q,\\
 a_{h,2}&=-58m^2+28m-48,\\
 a_{h,1}&=(64+112q/3)m^2+(-36-40q/3)m+36+12q,\\
 a_{h,0}&=(-53-92q/3)m^2+(22+38q/3)m-12-6q.
\end{aligned}
\]
For the rung case,
\[
\begin{aligned}
 a_{r,4}&=(-21+12q)m^2+(14-22q/3)m-12+6q,\\
 a_{r,3}&=(-4+8q/3)m+36-12q,\\
 a_{r,2}&=6m^2-20m-48,\\
 a_{r,1}&=(-4-8q/3)m+36+12q,\\
 a_{r,0}&=(-21-12q)m^2+(14+22q/3)m-12-6q.
\end{aligned}
\]
For every integer \(m\ge5\), the rational bounds \(433/250<q<1733/1000\) yield
\[
\begin{aligned}
 a_{h,4}&>m^2/20,&(|a_{h,3}|,|a_{h,2}|,|a_{h,1}|,|a_{h,0}|)&<(5,66,144,117)m^2,\\
 a_{r,4}&<-m^2/125,&(|a_{r,3}|,|a_{r,2}|,|a_{r,1}|,|a_{r,0}|)&<(3/4,12,4,49)m^2.
\end{aligned}
\]
Here the componentwise inequalities follow by substitution of the two rational endpoints, using \(m\ge5\); in particular the sharper leading-coefficient checks reduce respectively to positivity of \(97m^2+92m-2412\) and \(294m^2-1937m+2403\), both positive for \(m\ge5\). With \(t>3^m\ge243\), the quartic is therefore positive for rails and negative for rungs, since
\[
\begin{aligned}
 t^{-4}\sum_{j=0}^4a_{h,j}t^j&>m^2\left(\frac1{20}-\frac5{243}-\frac{66}{243^2}-\frac{144}{243^3}-\frac{117}{243^4}\right)>0,\\
 t^{-4}\sum_{j=0}^4a_{r,j}t^j&<m^2\left(-\frac1{125}+\frac3{4\cdot243}+\frac{12}{243^2}+\frac4{243^3}+\frac{49}{243^4}\right)<0.
\end{aligned}
\]
The remaining cases are exact: at \(m=3\), the two covariances are respectively \(-21/625\) and \(37/1875\); at \(m=4\), both equal \(15/4096\). This proves both strict classifications including all boundaries.

**4. Infinite-volume constants.** As \(m\to\infty\), \(t=(2+\sqrt3)^m\to\infty\), and the \(m^2t^2\) leading terms give the stated limits. In particular, the common one-vertex leaf probability tends to \((2\sqrt3-3)/2\). The signs of the limiting constants can be checked by squaring positive rational comparisons with \(\sqrt3\).

## Verification
The standalone, standard-library `verify.py` checks the transfer matrix via independent local-forest enumeration, tests its polynomial identity by integer matrix arithmetic, reconstructs the closed formulas for \(3\le m\le50\), and independently computes exact matrix-tree minors for \(3\le m\le10\). These finite diagnostics are not used as a substitute for the all-size recurrence and polynomial inequalities proved above. Execute with `python3 verify.py`.

## Relationship to prior work
Azimi and Farrokhi Derakhshandeh Ghouchan (arXiv:2306.10497, first posted 18 June 2023), particularly Section 4, provide explicit circular-ladder resistance and Laplacian-pseudoinverse formulas and the complete spanning-tree count. Their Theorem 4.2 already supplies \(F_m\) in a different notation; it is *not* newly claimed. Their study does not state vertex-leaf covariance signs or the two orientations' opposite-sign regime. Nachmias and Peres (arXiv:2011.08833, first posted 17 November 2020) give a high-degree uniform-spanning-tree local limit; their degree-growth hypothesis excludes these fixed-degree-three prisms. The present contribution is the joint leaf-count identity and rigorous sharp sign classification, not the UST definition, matrix-tree theorem, classical ladder recurrences, or previously published total spanning-tree counts. Published and searchable-record comparisons found no explicit prior statement of these two sign transitions; that absence is not proof of historical priority.

## Limitations
The result concerns the uniform spanning-tree measure on unweighted finite prisms. No assertion is made for general cubic graphs, arbitrary pairs of vertices, weighted spanning trees, or monotonicity as \(m\) increases. Independent review of novelty and proof has not been performed. The nearest published paper already provides sufficient resistance-matrix information to facilitate another derivation, though establishing the claimed covariance sign theorem requires the additional joint-leaf enumeration and global sign argument.

## References
- A. Azimi and M. Farrokhi Derakhshandeh Ghouchan, *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497 (first publicly posted 2023-06-18), https://arxiv.org/html/2306.10497v1.
- A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833 (first publicly posted 2020-11-17), https://arxiv.org/abs/2011.08833.
- J. Hladký, A. Nachmias and T. Tran, *The local limit of the uniform spanning tree on dense graphs*, arXiv:1711.09788 (first posted 2017-11-27), https://arxiv.org/abs/1711.09788. Background only; its linear-degree premise does not apply to prisms.
