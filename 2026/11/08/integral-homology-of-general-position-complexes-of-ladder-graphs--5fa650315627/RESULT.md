# Integral homology of general-position complexes of ladder graphs

## Finding

Let \(L_n=P_n\square K_2\) for every integer \(n\ge2\). Define the **graph-metric general-position complex** \(\Delta_n\) on \(V(L_n)\): a face is a vertex set containing no three points on a common shortest path of \(L_n\). Its reduced integral homology is torsion-free and concentrated in degrees one and two. More precisely,

\[
\widetilde H_1(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&n=2,\\
\mathbb Z^8,&n=3,\\
\mathbb Z^{3n+1},&n\ge4,
\end{cases}
\]

and

\[
\widetilde H_2(\Delta_n;\mathbb Z)\cong
\begin{cases}
0,&2\le n\le5,\\
\mathbb Z^{n(n-4)(n-5)/3},&n\ge6.
\end{cases}
\]

All remaining reduced homology groups are zero. In particular, \(n=6\) is the first ladder order for which the general-position complex has nontrivial second homology; its rank is four. This statement concerns graph-geodesic general position, not affine general position in Euclidean space.

## Assumptions and scope

Here \(P_n\) is the path on ordered columns \(0,1,\ldots,n-1\). Write \(a_i=(i,0)\) and \(b_i=(i,1)\). Distances are those of the whole ladder, not induced subgraphs:

\[
d((i,r),(j,s))=|i-j|+\mathbf1_{r\ne s}.
\]

Every pair of distinct vertices is a face. For \(i<j<k\), precisely the following two triples are faces:

\[
\{a_i,b_j,a_k\},\qquad \{b_i,a_j,b_k\}.
\]

There are no faces of cardinality four or greater. Consequently the complex has \(f\)-vector \(f_0=2n\), \(f_1=\binom{2n}{2}\), and \(f_2=2\binom n3\). The homology coefficients and all quantifiers above refer to all integer \(n\ge2\); no homotopy-equivalence type or symmetry representation is asserted.

## Proof

### Faces from distances

Two vertices in one column form a rung. Any third vertex lies in a row containing one endpoint of that rung, which therefore lies on a shortest path between the other rung endpoint and the third vertex. Thus no three-face has repeated columns. For distinct \(i<j<k\), direct substitution in the displayed distance formula shows that a triple is in general position if and only if the middle-column vertex lies on the opposite row from both outer-column vertices. Three vertices in a common row lie on one shortest path. If a four-vertex face existed, it would therefore contain two vertices from each row. Let the top-row columns be \(a<b\) and the bottom-row columns \(c<d\). The two-top/one-bottom triple condition forces both \(c\) and \(d\) to lie strictly between \(a\) and \(b\). The two-bottom/one-top condition forces both \(a\) and \(b\) to lie strictly between \(c\) and \(d\). These strict containments are incompatible. Thus there are no four-faces or larger faces. This proves the displayed face list without relying on an enumeration program.

### Boundary rank over an arbitrary field

Work initially over an arbitrary field \(\mathbb F\). Fix the edge orientation \(a_0<\cdots<a_{n-1}<b_0<\cdots<b_{n-1}\). Write a 1-cochain on the complete one-skeleton as \(U_{ik}\) on \((a_i,a_k)\), \(V_{ik}\) on \((b_i,b_k)\) for \(i<k\), and \(W_{ij}\) on \((a_i,b_j)\) for all \(i,j\). By the oriented triangle boundaries, it is a cocycle if and only if, for every \(i<j<k\),

\[
U_{ik}=W_{ij}-W_{kj},\qquad
V_{ik}=W_{jk}-W_{ji}.
\tag{1}
\]

For each gap \(k-i\ge2\), the variables \(U_{ik}\) and \(V_{ik}\) are determined by the off-diagonal array \(W\) and independence from the choice of intermediate \(j\). The variables \(U_{i,i+1}\) and \(V_{i,i+1}\) (a total of \(2(n-1)\)) are free, as are all \(n\) diagonal entries \(W_{ii}\). Independence of intermediate vertices in (1) is equivalent to two equations for every four indices \(i<j<k<\ell\):

\[
W_{ij}-W_{ik}-W_{\ell j}+W_{\ell k}=0,\tag{2}
\]

\[
W_{ji}-W_{j\ell}-W_{ki}+W_{k\ell}=0.\tag{3}
\]

We prove that, for every \(n\ge4\), the space of off-diagonal arrays satisfying (2)--(3) has dimension \(2n+2\), over **every** field. In fact all solutions have the form

\[
W_{ij}=p_i+q_j+c\mathbf1_{i<j}
+d\mathbf1_{(i,j)=(0,n-1)}
+e\mathbf1_{(i,j)=(n-1,0)},\qquad i\ne j.
\tag{4}
\]

Here \(p_i,q_j,c,d,e\in\mathbb F\) are arbitrary, modulo the sole redundancy \(p_i\mapsto p_i+t\), \(q_j\mapsto q_j-t\). Every such array satisfies (2)--(3): in a quadruple \(i<j<k<\ell\), both \(W_{ij}\) and \(W_{ik}\) use the upper indicator, both \(W_{\ell j}\) and \(W_{\ell k}\) use the lower indicator, and neither extreme-corner exceptional entry appears; the transposed equation is analogous.

To prove completeness of (4), induct on \(n\). For \(n=4\), (2)--(3) impose exactly two independent equations on twelve off-diagonal entries (they involve different ordered cells). The family (4) has dimension ten, as shown below, so it exhausts the solutions. Suppose (4) is complete for \(n\ge4\) and extend to indices \(0,\ldots,n\). Let \(R_j=W_{nj}\) and \(C_j=W_{jn}\) for \(0\le j<n\). In (2), the quadruples \((0,2,n-1,n)\) and \((1,2,n-1,n)\) must give the same value of \(R_2-R_{n-1}\). The first contains the old exceptional parameter \(d\) and the second does not, so \(d=0\). The corresponding two applications of (3) force the old \(e=0\). Now for every \(1\le j<k<n\), the quadruple \((0,j,k,n)\) in (2) gives \(R_j-R_k=q_j-q_k\), and in (3) gives \(C_j-C_k=p_j-p_k\). Thus there are constants \(\rho,\sigma\) such that \(R_j=q_j+\rho\) and \(C_j=p_j+\sigma\) whenever \(1\le j<n\). Extend (4) by setting \(p_n=\rho\), \(q_n=\sigma-c\). Its new extreme-corner entries \(R_0\) and \(C_0\) may be arbitrary, supplying the new \(e\) and \(d\). This completes the induction.

For completeness, the dimension of the parametric family (4) really is \(2n+2\). The additive arrays \(p_i+q_j\) on the off-diagonal positions form a \((2n-1)\)-dimensional space, since the connected bipartite incidence graph of these positions has exactly one additive redundancy for \(n\ge3\). The rectangle difference using rows \(0,1\) and columns \(n-2,n-1\) isolates \(-d\). The analogous difference using rows \(n-2,n-1\) and columns \(0,1\) isolates \(-e\). Once \(d=e=0\), the difference of entries in rows \(0,2\) and columns \(1,3\) isolates \(c\). Thus these three directions are independent modulo additive arrays, over any field (including characteristic two).

The off-diagonal \(W\) therefore contributes \(2n+2\) free dimensions. Adding the \(n\) diagonal entries and the \(2(n-1)\) adjacent monochromatic entries yields

\[
\dim_{\mathbb F}\ker(\partial_2^{\mathsf T})=(2n+2)+n+2(n-1)=5n.
\]

The complete one-skeleton has \(\binom{2n}{2}=2n^2-n\) edges. Rank-nullity gives, for \(n\ge4\),

\[
\operatorname{rank}_{\mathbb F}\partial_2=(2n^2-n)-5n=2n(n-3).
\tag{5}
\]

The same holds for every coefficient field, not only over the rationals. For \(n=3\), there are exactly two triangles with disjoint supports, so their boundaries are independent and \(\operatorname{rank}\partial_2=2\). For \(n=2\), there are no triangles.

### Integral homology

The complete one-skeleton is connected and has cycle-space dimension \(\binom{2n}{2}-2n+1\). There are no three-dimensional simplices, so \(H_2=\ker\partial_2\) has dimension \(2\binom n3-\operatorname{rank}\partial_2\), while \(H_1\) has dimension \(\binom{2n}{2}-2n+1-\operatorname{rank}\partial_2\). Substituting (5) gives \(3n+1\) and \(n(n-4)(n-5)/3\) for \(n\ge4\). Direct substitution of ranks zero and two gives the displayed \(n=2,3\) exceptions.

These are ranks over every field. Since \(H_2(\Delta_n;\mathbb Z)\) is a subgroup of the free chain group \(C_2\), it is free abelian. Since \(H_0\cong\mathbb Z\), the universal coefficient theorem says that any prime torsion in \(H_1(\Delta_n;\mathbb Z)\) would strictly increase its dimension over that prime field relative to its rational dimension. Field-independence of the ranks rules this out. Thus both integral groups are torsion-free, establishing the theorem.

## Verification

The standalone file `verify.py` constructs the metric directly, exhaustively checks every subset for \(2\le n\le8\), confirms the complete face description, independently assembles the oriented triangle-boundary matrix, and computes ranks over primes \(2\), \(3\), and \(101\) for every \(2\le n\le13\). It checks the Betti formulas and the first positive \(H_2\) instance. Run with `python3 verify.py` using Python 3.8 or later; it has no third-party dependencies. Finite tests are a cross-check, not the proof of the unbounded statement: the field-uniform induction above supplies that proof.

## Relationship to prior work

Klavžar, Patkós, Rus, and Yero (2019 preprint; 2021 journal) studied extremal general-position sets and counted general-position sets in Cartesian grids, including thin grids. Iršič, Klavžar, Rus, and Tuite (2024 preprint and article) gave the full general-position **cardinality polynomial**, including the thin-grid face counts. Welton, Khudairi, and Tuite (2024) studied smallest inclusion-maximal general-position sets in Cartesian products. These determine extremal/cardinality information but do not themselves identify the ranks of the alternating-triangle boundary map, the torsion, or the first appearance of two-dimensional homology. In particular, an \(f\)-vector does not determine simplicial homology. These earlier structural and enumerative facts are acknowledged; the new result concerns the **integral homology of the entire face complex**. The Euclidean affine general-position complex in geometric transversality theory is a different construction.

## Limitations

The result determines homology groups but not the homotopy type or any automorphism-module decomposition. It concerns path ladders, not circular ladders \(C_n\square K_2\) or other forbidden-path complexes. The novelty comparison is based on reachable primary text and indexed research records; a differently named or unindexed equivalent topology result may exist, so independent literature review remains valuable. The proof and finite checks are presented as mathematical evidence, not as a claim of external certification.

## References

1. S. Klavžar, B. Patkós, G. Rus, and I. G. Yero, *On general position sets in Cartesian products*, arXiv:1907.04535 (first posted 2019-07-10); *Results in Mathematics* 76 (2021), article 123. https://arxiv.org/abs/1907.04535 ; https://doi.org/10.1007/s00025-021-01438-x .
2. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General position polynomials*, arXiv:2401.05696 (first posted 2024-01-11); *Results in Mathematics* 79 (2024), article 110. https://arxiv.org/abs/2401.05696 ; https://doi.org/10.1007/s00025-024-02133-3 .
3. E. Kruft Welton, S. Khudairi, and J. Tuite, *Lower General Position in Cartesian Products*, arXiv:2404.19451 (first posted 2024-04-30). https://arxiv.org/abs/2404.19451 .
4. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first posted 2023-06-16). https://arxiv.org/abs/2306.09965 .
