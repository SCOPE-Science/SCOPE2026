# Universal survivor dimension and sharp arclength escape on a planar invariant graph

## Finding

Let \(F_b(x,y)=(|x|-y-1,\;x-|y|+b)\) with \(2\le b\le4\). Use the canonical polygonal invariant graph \(\Gamma_b\) for this parameter range from [1]. Let \(J_b\) be the eight-edge core specified below, and let \(K_b=\{z\in J_b:F_b^k(z)\in J_b\text{ for all }k\ge0\}\). Then
\[
 \dim_H K_b=\frac{\log(1+\sqrt2)}{\log4}=0.635776651581806\ldots.
\]
For \(n\ge1\) let \(L_n(b)=\mathcal H^1\{z\in J_b:F_b^k(z)\in J_b\text{ for }0\le k<n\}\), using Euclidean arclength. There is an exact formula and a sharp escape factor:
\[
 L_n(b)={\bf1}^{\mathsf T}M^{n-1}\ell_b,
 \qquad L_n(b)=C(b)r^{n-1}+o(r^{n-1}),
\]
where \(C(b)>0\), and \(r=0.866111689758913\ldots\) is the unique positive root of \(16r^7-4r^4-4r^3-1=0\). The definitions of \(M\), \(\ell_b\), and \(C(b)\) are given below. In particular, \(\mathcal H^1(K_b)=0\).

As a consequence, almost every point of \(\Gamma_b\) enters a period-three or period-four plateau cycle in finitely many steps. This is a finite-time capture statement, not a claim of neighbourhood attraction for both cycles at the endpoints: at \(b=2\) the period-three cycle is not attracting a neighbourhood, and at \(b=4\) the period-four cycle is not attracting a neighbourhood.

## Assumptions and scope

Write \([P,Q]\) for a closed straight segment. Use the following coordinates:
\[
\begin{aligned}
P_1&=(-b-2,-1),&P_2&=(b+2,-3),&P_3&=(b+4,2b-1),&P_4&=(4-b,5),\\
S&=(0,b+1),&X_1&=(0,-1),&X_2&=(0,b-1),&X_3&=(-b,1),\\
X_4&=(b-2,-1),&Y_1&=(b-1,0),&Y_2&=(b-2,2b-1),\\
Z_1&=(-b-1,0),&Z_2&=(b,-1),&Z_3&=(b,2b-1).
\end{aligned}
\]
The core and its state order are
\[
\begin{array}{c|cccccccc}
\text{edge}&A&B&C&D&E&G&I&H\\\hline
\text{segment}&[Z_3,P_3]&[Y_2,Z_3]&[X_3,S]&[Z_1,P_1]&[P_1,X_1]&[Z_2,P_2]&[Y_1,Z_2]&[Y_1,X_2].
\end{array}
\]
The whole graph is the union of the core and \(T=[X_3,Z_1]\), \(U=[X_1,Z_2]\), \(V=[X_2,Z_3]\), and \(W=[S,P_4]\) for \(2\le b\le3\) or \(W=[S,Y_2]\) for \(3\le b\le4\). At \(b=3\) the two descriptions agree. Both \([S,P_4]\) and \([S,Y_2]\) lie on \(W\). The core edges have disjoint relative interiors even at endpoint parameters.

## Proof

**Branches and capture.** On each core edge both coordinate signs are constant in its relative interior, so the map is affine on the closed edge. Substitution gives the following images, with the displayed pieces in order along the image up to reversal:
\[
\begin{array}{c|l|c}
\text{edge}&\text{image}&\text{arclength expansion }s_i\\\hline
A&C\cup[S,P_4]&\sqrt2\\
B&T\cup D&\sqrt2\\
C&E\cup[X_1,X_4]&\sqrt2\\
D&G&2\\
E&G\cup I\cup H&\sqrt2\\
G&A&\sqrt2\\
I&B&\sqrt2\\
H&C\cup[S,Y_2]&2
\end{array}
\]
For example, on \(C\) the line is \(y=x+b+1\), the image is \((-2x-b-2,-1)\), and the extreme image points are \(P_1\) and \(X_4\). The edges \(G,I,H\) lie successively along \(y=b-1-x\) in the image of \(E\). All intersections of the transient segments with the core are finite: this follows from the lines in the definitions and their endpoint ranges. Thus, apart from finitely many points in each one-step image, the allowed arrows for core-to-core transitions are exactly
\[
A\to C,\quad B\to D,\quad C\to E,\quad D\to G,\quad E\to G,I,H,\quad G\to A,\quad I\to B,\quad H\to C.
\]
Each arrow has a unique inverse branch on the entire target segment and inverse ratio \(s_i^{-1}\) for source \(i\).

On the transient segments one has \(F_b(T)=[X_4,Z_2]\subset U\), \(F_b(U)=V\), \(F_b(V)=\{X_3\}\) and \(F_b(W)=\{P_1\}\). These identities follow by restricting to the respective lines \(y=x+b+1\) on \(T,W\), \(y=-1\) on \(U\), and \(y=x+b-1\) on \(V\), with the signs on each segment. The resulting cycles are
\[
 P_1\to P_2\to P_3\to P_4\to P_1,\qquad
 X_3\to X_4\to(b-2,2b-3)\to X_3.
\]
Every point of \(\Gamma_b\setminus K_b\) must at some step fail to be in \(J_b\) and then lie on one of these four transient segments; it therefore enters one of the cycles exactly.

**Survivor length.** Put \(Q_{ij}=1\) for the listed arrows and \(0\) otherwise, and \(M_{ij}=Q_{ij}/s_i\). The edge length vector is
\[
\ell_b=(4,2,b\sqrt2,\sqrt2,b+2,2\sqrt2,\sqrt2,(b-1)\sqrt2)^{\mathsf T}.
\]
One step of backwards survival multiplies the vector of retained lengths by \(M\): disjoint interiors allow addition, and the inverse branch into edge \(i\) scales length by \(s_i^{-1}\). Finite exceptional points carry no arclength, and their inverse images inside the finitely many core branches remain finite per step. Starting at \(n=1\) with \(\ell_b\) gives the stated exact length.

The arrow graph is strongly connected, with three simple return loops at \(C\) of lengths \(3,4,7\), so \(M\) is primitive. In the determinant, the three simple cycles all share \(C\), and their weights at the inverse arclength ratios are \(1/4,1/4,1/16\). Consequently
\[
 \det(tI-M)=t(t^7-t^4/4-t^3/4-1/16).
\]
The nonzero factor has a single positive root, since dividing the equation by \(t^7\) makes the sum of the three positive inverse powers strictly decreasing; the root is less than one. For positive right and left Perron vectors \(v,w\), respectively, Perron–Frobenius convergence gives the stated asymptotic with
\[
C(b)=\frac{({\bf1}^{\mathsf T}v)(w^{\mathsf T}\ell_b)}{w^{\mathsf T}v}>0.
\]
It follows that \(\mathcal H^1(K_b)=0\), proving almost-everywhere finite-time capture on the graph.

**Survivor dimension.** The full-edge inverse similarities define a strongly connected graph-directed construction satisfying the open-set condition, using the interiors of the individual edge intervals. If a survivor itinerary fails to use the recorded full-edge branches, it hits a vertex or a one-step exceptional intersection; all such points in the survivor form a countable set by injectivity on each core branch. Thus the dimension is that of the graph-directed limit. The dimension theorem [3] sets \(\rho(M_d)=1\) for \((M_d)_{ij}=Q_{ij}s_i^{-d}\). With \(z=2^{-d/2}\), the same three cycles now have weights \(z^4,z^4,z^8\), so the spectral equation at \(t=1\) is \(1-2z^4-z^8=0\). The positive solution is \(z^4=\sqrt2-1\), giving the claimed dimension.

**Endpoint distinction.** At \(b=2\), \(X_4=X_1\) and \((b-2,2b-3)=X_2\). The cycle starting at \(X_3\) lies at the boundary of the itinerary \(C\to E\to H\to C\). At \(b=4\), \(P_4=S\), and the cycle starting at \(S\) lies at the boundary of \(C\to E\to G\to A\to C\). In each case the inverse branch around the indicated loop is a contraction of ratio \(1/4\) from the closed edge \(C\) into itself, fixing the cycle's point on \(C\). The distinct loop \(C\to E\to I\to B\to D\to G\to A\to C\) has a fixed point for its inverse branch; this gives a periodic point on \(C\) not on the indicated endpoint cycle, since the latter does not lie on \(I\) at the second step. Iterating the short-loop inverse on this other periodic point gives points approaching the indicated endpoint cycle, whose forward orbits eventually follow the other periodic orbit. Thus even on the invariant graph no neighbourhood of the indicated cycle is attracted to it at the stated endpoint. This has no effect on the length or dimension formulas.

## Reproduction and limits

The supplied `check_survivor.py` checks exact endpoints and ordered image decompositions at nine rational parameters and checks the arclength-weighted determinant and dimension equation using SymPy. The analytic sign, inverse-branch and loop arguments establish the formulas for all real parameters in the interval; the numerical samples alone do not. All measure claims are confined to the one-dimensional graph, and the escape law is for initial arclength on the eight core edges, not a law for planar Lebesgue sampling.

## Relationship to prior work

Reference [1], §5.7 and Proposition 38, supplies the canonical invariant graph and its symbolic transitions; its topological entropy calculation uses the unweighted adjacency, not these Euclidean-arclength or dimension weights. Reference [2] studies orbit statistics and convergence on invariant graphs; [4] already gives qualitative full-arclength plateau capture on a broader parameter range. The quantitative findings here are the exact core survival law, sharp escape factor and dimension; qualitative finite-time capture is stated only as a consequence. Reference [3] supplies the general dimension theorem.

## References

1. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052, DOI:10.1007/s12346-025-01221-1.
2. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411.
3. R. D. Mauldin and S. C. Williams, *Hausdorff dimension in graph directed constructions*, Transactions of the AMS **309** (1988), 811–829, DOI:10.1090/S0002-9947-1988-0961615-4.
4. *Full-arclength absorption by flat branches for every parameter in the planar absolute-value family*, [research record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-full-arclength-absorption-by-flat-branches-for-every-parameter-i--335be622e78a).
