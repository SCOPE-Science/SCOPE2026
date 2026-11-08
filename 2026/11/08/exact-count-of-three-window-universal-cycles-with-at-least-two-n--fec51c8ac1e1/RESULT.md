# Exact count of three-window universal cycles with at least two nonzero symbols

## Finding

For every integer \(q\ge3\), take the alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\) with the symbol \(0\) distinguished. Write \(\mathcal W_q\) for the set of length-three words containing at least two nonzero symbols. A *universal cycle* is a cyclic sequence whose consecutive length-three windows, with wraparound, consist of each member of \(\mathcal W_q\) exactly once. Symbols are individually labeled. Two cycles are identified under cyclic rotation and **only** under cyclic rotation.

The exact number of universal cycles is
\[
\boxed{U_q=q^{q(q-2)}(q-1)^{2(q-2)}\big((q-2)!\big)^{2(q-1)}\big((q-1)!\big)^{(q-1)^2}.}
\]
Every such cycle has \((q-1)^2(q+2)\) letters. For \(q=3\), the exact count is \(1728\); for \(q=4\), it is \(3423782572130304\). The formula extends to the boundary \(q=2\), where it gives one cycle.

A structural intermediate result is that the associated restricted de Bruijn digraph has
\[
\boxed{\tau_q=q^{q(q-2)}(q-1)^{2(q-2)}}
\]
spanning directed in-arborescences toward each fixed vertex.

## Assumptions and scope

Here \(q\) is any integer at least three; no field or arithmetic on the alphabet is needed. A cyclic sequence is considered a word of length \(|\mathcal W_q|\) indexed modulo its length. We count cycles up to choosing a starting index, but do not quotient by reflection or by permutations of symbols. The windows are **ordered** words, not multisets or substring-composition profiles.

For a digraph with a loop, that loop is treated as an ordinary labeled edge when enumerating Euler circuits; it makes no contribution to a directed Laplacian's off-diagonal entries or arborescences. Each permitted triple uniquely labels one edge, so there are no parallel edges with the same ordered triple.

## Proof

**1. Restricted de Bruijn correspondence.** Put \(s=q-1\). Form a directed digraph \(G_q\) whose vertices are the \(q^2-1=s^2+2s\) ordered pairs \((a,b)\ne(0,0)\). A permitted triple \((a,b,c)\in\mathcal W_q\) gives a directed edge from \((a,b)\) to \((b,c)\). A vertex \((0,a)\) or \((a,0)\), where \(a>0\), has outdegree and indegree \(s\). A vertex \((a,b)\), with \(a,b>0\), has outdegree and indegree \(q\). Consequently the graph is balanced, and its edge count is
\[
E=2s\cdot s+s^2\cdot q=s^2(s+3)=(q-1)^2(q+2).
\]
It is strongly connected: from any vertex, appending a fixed nonzero symbol \(1\) twice reaches \((1,1)\), using only allowed edges. Conversely, from \((1,1)\), appending the two coordinates \(a,b\) of any target \((a,b)\ne(0,0)\) reaches that target through permitted edges. Thus Euler circuits exist, and they correspond bijectively to universal cycles after identifying rotations. Since every allowed triple occurs once, the cycle cannot have a shorter period; fix one distinguished triple as the first edge to choose a unique representative of each rotation class.

**2. Laplacian factorization.** Let \(L=D-A\) be the outdegree Laplacian acting on functions on vertices. For each nonzero \(a\) and \(b\), write
\[
v_a=f(0,a),\qquad u_a=f(a,0),\qquad z_{ab}=f(a,b),\qquad R_a=\sum_{b=1}^s z_{ab}.
\]
Directly from the allowed edges, the coordinates of \(Lf\) satisfy
\[
\begin{aligned}
(Lf)(0,a)&=s v_a-R_a,\\
(Lf)(a,0)&=s u_a-\sum_{b=1}^s v_b,\\
(Lf)(a,b)&=q z_{ab}-u_b-R_b.
\end{aligned}
\]
Taking row sums of the last identity gives
\[
R'_a=qR_a-\sum_{b=1}^s u_b-\sum_{b=1}^s R_b.
\]
The map \(f\mapsto (v,u,R)\) is onto a \(3s\)-dimensional quotient. Its kernel has dimension \(s^2-s\) and is acted on by \(L\) as the scalar \(q\). On the quotient, split each \(s\)-vector into its constant component and its coordinate-sum-zero component. On each of the \(s-1\) independent zero-sum coordinates, \(L\) acts triangularly with diagonal entries \(s,s,q\): explicitly \(v'=s v-R\), \(u'=s u\), \(R'=qR\). On the three-dimensional constant-component subspace, it acts as
\[
M=\begin{pmatrix}s&0&-1\\-s&s&0\\0&-s&1\end{pmatrix},
\qquad
\det(xI-M)=x\big(x^2-(2q-1)x+q^2-1\big).
\]
It follows by multiplying the invariant-subspace characteristic polynomials that the full Laplacian characteristic polynomial is
\[
\boxed{\det(xI-L)=x(x-q)^{q(q-2)}(x-(q-1))^{2(q-2)}\big(x^2-(2q-1)x+q^2-1\big).}
\]
This identity holds as a polynomial for every integer \(q\ge2\), not merely for the computational examples below. Note that the quotient decomposition requires no diagonalizability assumption: the characteristic polynomial of an operator preserving a subspace is the product of the characteristic polynomials on that subspace and the quotient.

**3. Directed matrix-tree theorem.** Because \(G_q\) is strongly connected and balanced, its \(q^2-1\) principal Laplacian cofactors are equal and count spanning in-arborescences toward their respective roots. The product of the nonzero eigenvalues is \((q^2-1)\) times this common cofactor. The displayed characteristic polynomial yields
\[
(q^2-1)\tau_q=q^{q(q-2)}(q-1)^{2(q-2)}(q^2-1),
\]
so \(\tau_q=q^{q(q-2)}(q-1)^{2(q-2)}\).

**4. BEST theorem and normalization.** Choose a distinguished allowed edge to fix the cyclic starting position. The directed BEST theorem counts Euler circuits beginning with that edge as
\[
\tau_q\prod_{v\in V(G_q)}(\deg^+(v)-1)!
=\tau_q\big((q-2)!\big)^{2(q-1)}\big((q-1)!\big)^{(q-1)^2}.
\]
Each Euler circuit encodes a unique cyclic string, and every such string contains the chosen edge exactly once. Therefore no extra division by the number of edges, vertex count, or alphabet symmetry is appropriate. Substituting the value of \(\tau_q\) proves the formula.

## Verification

Run `python3 CHECKER.py` in the directory containing the package. It builds the restricted graph from the original triple definition, computes integer Laplacian cofactors by exact Bareiss elimination, and independently enumerates Euler circuits with a fixed distinguished edge for \(q=2,3\). It checks the arborescence and universal-cycle formulas for \(q=2,3,4,5,6\). This is a finite numerical cross-check; the invariant-quotient determinant derivation above supplies the proof for all \(q\).

## Relationship to prior work

Mitchell and Wild [1], first public July 24, 2026, study existence and construction of universal cycles for consecutive weight classes on arbitrary finite alphabets. The present claim is the exact number, not mere existence, for the natural smallest length-three **upper two Hamming-weight layers**. The accessible abstract of [1] was compared, but the full manuscript could not be inspected; a hidden enumeration in that source remains a priority risk.

Sawada, Williams, and Wong [2] construct universal cycles for ranges of *binary* weights. Sawada and Williams [3] construct shorthand cycles for fixed-content families (its full public text was inspected); that problem uses different windows and proves existence/efficient construction rather than an enumeration of the present dense-three-letter class. Chen, Kitaev, and Sun [4] enumerate universal-cycle existence for deletions of a small number of allowed words, not the present large forbidden family, according to its accessible abstract.

Chang, Wang, and Xue [5] give exact enumeration of universal cycles for \(k\)-permutations with \(k=3,4\), but those windows have all distinct symbols; the present weight-2/3 family permits repeats and zeros and is not a special case. Classical directed Matrix-Tree and BEST theorems are used, not claimed as new. The claim is the closed factorization of the restricted Laplacian and the resulting entire-alphabet exact cycle enumeration.

## Limitations

The theorem counts length-three windows containing at least two nonzero symbols, for every integer alphabet size \(q\ge3\). It does not enumerate other window lengths, arbitrary weight ranges, reversal-equivalence classes, or alphabet-relabeling orbits. The full 2026 Mitchell–Wild manuscript and the 2013 binary weight-range article were not accessible for complete source-to-source comparison, so independent priority confirmation remains outstanding. No independent mathematical review has been performed.

## References

[1] C. J. Mitchell and P. R. Wild, *Weight-constrained universal sequences*, arXiv:2607.22350 (first submitted 2026-07-24), https://arxiv.org/abs/2607.22350 .

[2] J. Sawada, A. Williams, and D. Wong, *Universal Cycles for Weight-Range Binary Strings*, IWOCA 2013, pp. 388–401, https://doi.org/10.1007/978-3-642-45278-9_33 .

[3] J. Sawada and A. Williams, *A Universal Cycle for Strings with Fixed-Content (which are also known as Multiset Permutations)*, 2021, https://www.researchgate.net/publication/350948020_A_Universal_Cycle_for_Strings_with_Fixed-Content_which_are_also_known_as_Multiset_Permutations .

[4] H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8(5), 778 (2020), https://doi.org/10.3390/math8050778 .

[5] Z. Chang, Q. Wang, and J. Xue, *An effective approach to enumerate universal cycles for k-permutations*, Cryptography and Communications 17 (2025), 977–988, https://doi.org/10.1007/s12095-025-00798-3 .
