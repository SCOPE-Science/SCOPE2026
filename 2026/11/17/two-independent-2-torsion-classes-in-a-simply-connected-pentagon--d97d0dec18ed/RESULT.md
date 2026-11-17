# Two independent 2-torsion classes in a simply connected pentagonal dihedral graph-complex quotient

## Finding
Let \(Y=|\Delta^2_5|/D_5\), where \(\Delta^2_5\) is the complex of not-2-vertex-connected graphs on five labeled vertices and \(D_5\) permutes labels as a regular pentagon. Then
\[
\pi_1(Y)=1,\qquad \widetilde H_*(Y;\mathbb Q)=0,
\]
and
\[
\bigl(\dim_{\mathbb F_2} H_i(Y;\mathbb F_2)\bigr)_{i=0}^{6}=(1,0,0,0,2,2,0).
\]
There is no homology above degree six. Thus
\[
H_4(Y;\mathbb Z)[2]\cong(\mathbb Z/2\mathbb Z)^2,
\]
while the subgroup annihilated by multiplication by two vanishes in every other integral homology degree. This determines the exact number, but not the exponents, of the 2-primary cyclic summands in degree four.

## Assumptions and scope
The five graph vertices are \(\mathbb Z/5\mathbb Z\). A face is any nonempty subset of the ten unordered graph edges whose spanning graph is disconnected or has a cut vertex. All graphs include all five labeled vertices, even if isolated. The acting group is \(D_5=\langle r,s\mid r^5=s^2=1,\ srs=r^{-1}\rangle\), with \(r(i)=i+1\) and \(s(i)=-i\) modulo five. The quotient is an **ordinary geometric orbit space**, not a homotopy quotient or the complex consisting only of invariant graphs. We use integral homology unless coefficient fields are specified. In the formula \(A[2]\), the bracket means the subgroup of elements killed by two, not the full 2-primary component.

## Proof
**Labeled topology and fundamental group.** Babson–Björner–Linusson–Shareshian–Welker (1997), Theorem 3.1, proves \(|\Delta^2_n|\simeq\bigvee^{(n-2)!} S^{2n-5}\). For five labels the original realization is \(\bigvee^6S^5\), so it is simply connected. Every reflection of the pentagon fixes one label \(v\); the set of all four edges incident with \(v\) is an invariant face of \(\Delta^2_5\), since the star graph becomes disconnected upon deleting \(v\). Thus every reflection has a geometric fixed point. As the reflections generate \(D_5\), Armstrong's orbit-space theorem yields \(\pi_1(Y)=1\).

**Rational homology.** The same labeled theorem says that positive-dimensional rational homology of the original complex exists only in degree five, with dimension six. The signed Lefschetz alternating sum of the original edge-simplex action is \(-5\) at identity, \(0\) at any nonidentity rotation, and \(3\) at any reflection. Since the labeled realization is connected and has homology only in degrees zero and five, \(\operatorname{tr}(g|H_5)=1-L(g)\); its character values are respectively \(6,1,-2\). The average \((6+4\cdot1+5\cdot(-2))/10\) is zero. Rational transfer identifies rational orbit-space homology with rational invariants, so all positive rational homology of \(Y\) vanishes.

**Actual mod-two quotient chains.** Barycentrically subdivide \(\Delta^2_5\); a vertex now denotes a nonempty face (graph) and a simplex is a strict chain of faces. Because the chain faces have distinct edge counts, the dihedral action on this subdivision has no inversions: every element stabilizing a simplex fixes its vertices individually. Its orbit simplices therefore give a valid regular cellular chain description of the *geometric* quotient. The exhaustive enumeration in `verify.py` considers each of the \(2^{10}-1\) nonempty graph edge masks, checks connectivity after deletion of each possible graph vertex, and enumerates all orbit chains. It obtains the following numbers, with the boundary rank in each degree understood over \(\mathbb F_2\):

| Degree | Cells | Boundary rank |
|---:|---:|---:|
| 0 | 97 | 0 |
| 1 | 2286 | 96 |
| 2 | 15678 | 2190 |
| 3 | 44928 | 13488 |
| 4 | 61680 | 31440 |
| 5 | 40320 | 30238 |
| 6 | 10080 | 10080 |

The canonical orbit map is applied to every codimension-one flag deletion. Each mod-two boundary composition is checked directly to be zero. Since \(b_i=c_i-\operatorname{rank}\partial_i-\operatorname{rank}\partial_{i+1}\), these matrices yield \((b_0,\ldots,b_6)=(1,0,0,0,2,2,0)\). The quotient has no higher cells.

**Integral consequence.** The rational calculation gives zero positive-degree free rank. The universal coefficient exact sequence for mod-two homology implies the vanishing of all 2-torsion in degrees one through three. Its degree-four sequence then gives exactly two independent mod-two reductions of torsion classes in \(H_4(Y;\mathbb Z)\), and the degree-five sequence gives exactly two Tor classes arising from \(H_4(Y;\mathbb Z)\), leaving no 2-torsion in degree five. The degree-six sequence and finite dimensionality eliminate all higher 2-torsion. By the structure theorem for finitely generated abelian groups, the number of 2-primary cyclic summands in degree four is exactly two, hence \(H_4(Y;\mathbb Z)[2]\cong(\mathbb Z/2)^2\).

## Verification
Run `python3 verify.py` in a standard Python 3 environment. It uses only the standard library and performs a complete five-label enumeration, not sampling. It checks 785 nonempty labeled faces, all ten distinct dihedral label actions, the seven orbit-chain counts, every mod-two differential-square identity, all seven boundary ranks, the resulting Betti vector, and the signed Lefschetz values. The output terminates with `all boundary squares zero; all assertions passed`. The exact integral exponents and odd-primary torsion are outside the proved scope.

## Relationship to prior work
Babson et al., *Complexes of not \(i\)-connected graphs* (first public arXiv version 1997-05-11), establish the labeled sphere-wedge theorem and full rational symmetric-group character, including cyclic invariant multiplicities. Their published statements do not provide this nonfree dihedral orbit-space mod-two chain calculation. Jonsson's *Simplicial Complexes of Graphs*, Chapter 21, considers **dihedral variants of graph properties defined by polygon representations**, a different construction from quotienting the ordinary non-2-connected graph complex by a dihedral group. Shareshian's *Discrete Morse Theory for Complexes of 2-Connected Graphs* concerns the original labeled graph complex. Published computations for dihedral graph-Hom complexes are of distinct spaces and do not imply the present two-dimensional torsion subgroup.

## Limitations
The computation is a finite classification for precisely five labels under the full order-ten dihedral group. It does not determine the exponent of either 2-primary cyclic summand, odd-primary torsion, the full integral homology groups, or the complete homotopy type. Simple connectivity and rational acyclicity do not imply contractibility: the exhibited two-primary classes rule out contractibility. An equivalent result in unindexed literature remains possible. The reproducibility check validates exact mod-two ranks and the mathematical deductions stated, not an independent expert audit.

## References
- E. Babson, A. Björner, S. Linusson, J. Shareshian, V. Welker, *Complexes of not \(i\)-connected graphs*, arXiv:math/9705219, first version 1997-05-11; *Topology* 38 (1999), 271–299. https://arxiv.org/abs/math/9705219
- J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2007, Chapters 19 and 21. https://doi.org/10.1007/978-3-540-75859-4
- J. Shareshian, *Discrete Morse theory for complexes of 2-connected graphs*, *Topology* 40 (2001), 681–701. https://doi.org/10.1016/S0040-9383(99)00076-2
- M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, *Proceedings of the Cambridge Philosophical Society* 64 (1968), 299–301. https://doi.org/10.1017/S0305004100042845
