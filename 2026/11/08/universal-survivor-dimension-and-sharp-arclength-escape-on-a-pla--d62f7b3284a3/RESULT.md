# Universal survivor dimension and sharp arclength escape on a planar invariant graph

## Finding

Let the continuous planar absolute-value map be
\[
F_b(x,y)=(|x|-y-1,\ x-|y|+b),\qquad 2\le b\le4.
\]
On the canonical finite invariant graph of Cima–Gasull–Mañosa–Mañosas, define the eight-edge expanding core \(J_b\) in the next section and its all-core survivor
\[
K_b=\bigcap_{k\ge0}F_b^{-k}(J_b)\cap J_b.
\]
The Hausdorff dimension is **independent of the parameter**:
\[
\boxed{\dim_H K_b=\frac{\log(1+\sqrt2)}{\log4}=0.635776651581806\ldots}\tag{1}
\]
Moreover, writing
\[
L_n(b)=\mathcal H^1\bigl(\{z\in J_b:F_b^k(z)\in J_b\text{ for }0\le k<n\}\bigr),\qquad n\ge1,
\]
there is an **exact eight-state formula** and a **sharp parameter-independent escape factor**
\[
\boxed{L_n(b)={\bf1}^{\mathsf T}M^{n-1}\ell_b,
\quad L_n(b)=C(b)r^{n-1}+o(r^{n-1})}\tag{2}
\]
where \(C(b)>0\), \(r=0.866111689758913\ldots\) is the unique positive root of
\[
16r^7-4r^4-4r^3-1=0,\tag{3}
\]
and the explicit matrix \(M\), vector \(\ell_b\), and coefficient \(C(b)\) are defined below. In particular, \(\mathcal H^1(K_b)=0\). Almost every point of the entire invariant graph eventually reaches one of its attracting period-three or period-four plateau cycles. The latter qualitative full-arclength conclusion is included only as a consequence, not asserted to be independently new; the claimed contributions are the sharp escape exponent, finite-time formula, and dimension.

## Assumptions and scope

Work with Euclidean arclength on the fixed compact polygonal invariant graph \(\Gamma_b\) for \(a=-1\), explicitly constructed in the first reference. No assertion about two-dimensional Lebesgue-area proportions of initial states is made. The source's edge configuration changes at \(b=3\), but the eight expanding core edges do not change combinatorial type.

For compact straight segments, write \([U,V]\) for the segment joining two labelled planar points. The following vertices have the indicated coordinates:
\[
\begin{aligned}
P_1&=(-b-2,-1),&P_2&=(b+2,-3),&P_3&=(b+4,2b-1),&P_4&=(4-b,5),\\
S&=(0,b+1),&X_1&=(0,-1),&X_2&=(0,b-1),&X_3&=(-b,1),\\
X_4&=(b-2,-1),&Y_1&=(b-1,0),&Y_2&=(b-2,2b-1),\\
Z_1&=(-b-1,0),&Z_2&=(b,-1),&Z_3&=(b,2b-1).
\end{aligned}
\]
The core \(J_b=A\cup B\cup C\cup D\cup E\cup G\cup I\cup H\) consists of
\[
\begin{array}{c|cccccccc}
\text{edge}&A&B&C&D&E&G&I&H\\\hline
\text{segment}&[Z_3,P_3]&[Y_2,Z_3]&[X_3,S]&[Z_1,P_1]&[P_1,X_1]&[Z_2,P_2]&[Y_1,Z_2]&[Y_1,X_2]
\end{array}
\]
with disjoint relative interiors. The remaining graph edges may be partitioned into four transient segments
\[
T=[X_3,Z_1],\quad U=[X_1,Z_2],\quad V=[X_2,Z_3],\quad
W=\begin{cases}[S,P_4],&2\le b\le3,\\[S,Y_2],&3\le b\le4.\end{cases}
\]
The points \(P_4\) and \(Y_2\) lie in the same line through \(S\); whichever is farther from \(S\) defines the full transient edge \(W\). Coincident vertices at endpoint parameters cause no arclength ambiguity.

Order the core states as \((A,B,C,D,E,G,I,H)\). The arclength vector and inverse expansion factors are
\[
\ell_b=(4,\ 2,\ b\sqrt2,\ \sqrt2,\ b+2,\ 2\sqrt2,\ \sqrt2,\ (b-1)\sqrt2)^{\mathsf T},
\]
\[
(s_A,s_B,s_C,s_D,s_E,s_G,s_I,s_H)=(\sqrt2,\sqrt2,\sqrt2,2,\sqrt2,\sqrt2,\sqrt2,2).
\]
Define the zero-one adjacency array \(Q\) by the arrows
\[
A\to C,\quad B\to D,\quad C\to E,\quad D\to G,\quad
E\to G,I,H,\quad G\to A,\quad I\to B,\quad H\to C,
\]
and put \(M_{ij}=Q_{ij}/s_i\). All other entries are zero. Thus the formulas are fully reproducible without relying on a diagram.

## Proof

**1. Exact branch dynamics.** On each of the eight core segments, the signs of both coordinates are constant in the relative interior, so \(F_b\) is affine and injective there. Direct substitution of the endpoint coordinates shows that the image of each source edge covers exactly the target core edges stated by \(Q\), plus the following transient portions:
\[
\begin{array}{c|l}
A&C\cup[S,P_4]\\
B&D\cup T\\
C&E\cup[X_1,X_4]\\
D&G\\
E&G\cup I\cup H\\
G&A\\
I&B\\
H&C\cup[S,Y_2].
\end{array}\tag{4}
\]
All unions in (4) are contiguous except for shared endpoints; the two extra subsegments of \(C,H\) have length zero at \(b=2\). The expansion of arclength on each source is the constant \(s_i\) above; this can also be checked from the branch Jacobians \(\begin{psmallmatrix}1&-1\\1&-1\end{psmallmatrix}\), \(\begin{psmallmatrix}1&-1\\1&1\end{psmallmatrix}\), etc., restricted to the indicated source directions. In particular, each full target edge \(j\) has a unique inverse branch inside a given source edge \(i\) whenever \(Q_{ij}=1\), and its inverse contraction is exactly \(s_i^{-1}\).

The transient pieces do not reenter the expanding core before visiting a plateau. Specifically \(F_b(T)\subset U\), \(F_b(U)=V\), \(F_b(V)=\{X_3\}\), and \(F_b(W)=\{P_1\}\). Also
\[
P_1\to P_2\to P_3\to P_4\to P_1
\]
and the eventual orbit of \(X_3\) is the period-three cycle \(X_3\to X_4\to(b-2,2b-3)\to X_3\). (The first arrow may be at a graph endpoint.) Consequently, outside the all-core survivor set every typical graph point is eventually captured by a collapsing orbit; the finitely many vertex coincidences at \(b=2,3,4\) do not affect the following arclength or dimension computations.

**2. Exact survivor length.** For any target edge \(j\), the pullback lying on source edge \(i\) has arclength \(\ell_{b,j}/s_i\) if \(Q_{ij}=1\), and zero otherwise. Distinct target-edge pullbacks have disjoint interiors. Iterating gives precisely (2)'s first equality. The same conclusion holds for all real \(b\in[2,4]\), including endpoints, because boundary points have \(\mathcal H^1\)-measure zero.

The directed graph is strongly connected: its return loops through \(C\) have lengths three, four and seven. Because the gcd of these lengths is one, \(M\) is primitive. Direct determinant expansion yields
\[
\det(tI-M)=\frac{t}{16}\bigl(16t^7-4t^4-4t^3-1\bigr).
\]
This polynomial has exactly one positive zero. Although \(M\) is not row-substochastic, its positive geometric length vector satisfies \(M\ell_b\le\ell_b\) componentwise, because the retained preimages inside every source edge have total length no larger than the source. Indeed, direct multiplication gives \(\ell_b-M\ell_b=(4-b,1,(b-2)/\sqrt2,0,0,0,0,(b-2)/\sqrt2)^{\mathsf T}\), so the \(B\)-row inequality is strict for every allowed \(b\). By irreducibility and the Perron–Frobenius comparison theorem the Perron root \(r\) is strictly less than one, and is positive. Let positive eigenvectors \(v,w\) satisfy \(Mv=rv\), \(w^{\mathsf T}M=rw^{\mathsf T}\). Perron–Frobenius convergence gives
\[
C(b)=\frac{({\bf1}^{\mathsf T}v)(w^{\mathsf T}\ell_b)}{w^{\mathsf T}v}>0
\]
and the sharp asymptotic. Hence \(\mathcal H^1(K_b)\le\lim_nL_n(b)=0\). In fact \(C(b)\) is strictly positive and affine in \(b\).

**3. Hausdorff dimension.** For every arrow \(i\to j\), restrict \(F_b^{-1}\) to its unique inverse branch from target edge \(j\) into source edge \(i\). It is a similarity with contraction \(s_i^{-1}\). By (4), images of different outgoing branches in the same source edge have disjoint interiors. Thus these inverse branches constitute a finite strongly connected graph-directed similarity construction satisfying the open-set condition (take the relative interiors of the source edges). The countable preimages of vertices, if present, do not affect Hausdorff dimension. By the standard graph-directed dimension theorem, the common survivor dimension \(d\) is characterized by spectral radius one for the matrix
\[
(M_d)_{ij}=Q_{ij}s_i^{-d}.
\]
Set \(z=2^{-d/2}\); the nonzero part of the characteristic polynomial of \(M_d\) is
\[
t^7-z^4t^4-z^4t^3-z^8.
\]
At the Perron eigenvalue \(t=1\), this becomes \(1-2z^4-z^8=0\). Writing \(u=z^4=4^{-d}\) gives \(u^2+2u-1=0\), with the unique positive solution \(u=\sqrt2-1\). Therefore \(4^d=1+\sqrt2\), proving (1), independently of \(b\).

## Verification

The included `check_survivor.py` uses exact rational arithmetic for the finite polygonal endpoint and segment-image identities at nine representative rational parameters, including \(b=2,3,4\). SymPy computes the exact weighted characteristic polynomial and symbolically checks the similarity-dimension equation. Running `python check_survivor.py` produces `POLYGONAL_CORE_EXACT_BRANCH_AND_CHARPOLY_OK parameter_samples=9 states=8`. The algebraic formulas in the proof, rather than the finite tests, establish universality for the whole interval.

## Relationship to prior work

Cima, Gasull, Mañosa and Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps* (first public arXiv version, 2024-10-01; 2025 journal version), supply the polygonal invariant graphs, expanding-edge principles, and the eight-edge symbolic adjacency for this exact parameter range. Their Proposition 38 determines the topological entropy from \(\lambda^7-\lambda^4-\lambda^3-1\), not the metric escape rate or survivor dimension. Their follow-up *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps* (2025, updated 2026), Theorem 3, proves full-arclength convergence only on other stated parameter ranges and does not furnish the quantitative assertions above. Qualitative full-arclength capture is treated solely as a consequence, not as a separate new contribution. The graph-directed dimension theorem of Mauldin–Williams is used as established mathematics, not presented as a new result.

## Limitations

The theorem is for the eight-edge core of the canonical invariant graph at \(2\le b\le4\). The dimension does not claim to measure an entire planar basin, any invariant physical probability, or all parameter values. The formula for \(L_n\) is for survival on the specified core; a first-capture-time law from a different sampling distribution requires a separate normalization. Mathematical originality remains subject to independently checking other, potentially unindexed sources. Independent audit has not been performed.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first submitted 2024-10-01); *Qualitative Theory of Dynamical Systems* 24 (2025), article 70, DOI:10.1007/s12346-025-01221-1; https://arxiv.org/abs/2410.01052 and https://link.springer.com/article/10.1007/s12346-025-01221-1.
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411, https://arxiv.org/abs/2503.02411.
3. R. D. Mauldin, S. C. Williams, *Hausdorff dimension in graph directed constructions*, *Transactions of the AMS* 309 (1988), 811–829, DOI:10.1090/S0002-9947-1988-0961615-4.
