# Sharp Fibonacci-to-dyadic Fourier-rank bounds for permutation comparisons on trees

## Finding
For every tree \(T\) with \(n\ge4\) vertices, let \(f_T\) be the multiplicity function on \(\mathbb F_2^{E(T)}\) obtained by comparing vertex labels in each of the \(n!\) permutations. Its convolution operator has rank \(R(T)\), satisfying
\[
F_n\le R(T)\le 2^{n-2},
\]
where \(F_0=0\), \(F_1=1\), and \(F_{j+1}=F_j+F_{j-1}\). The lower equality holds if and only if \(T\cong P_n\); the upper equality holds if and only if \(T\cong K_{1,n-1}\). All assertions are for labelled trees, but the values depend only on the abstract tree.

## Assumptions and scope
A reference direction is chosen on every edge. Each bijection \(\sigma:V(T)\to\{1,\dots,n\}\) contributes the vector \(x_\sigma\) whose edge coordinate is one if the label decreases along that edge. We define \(f_T(x)=\#\{\sigma:x_\sigma=x\}\) and \((C_Tg)(x)=\sum_y f_T(y)g(x-y)\) on the Boolean group. For \(S\subseteq E(T)\), the Walsh multiplier is
\[
W_T(S)=\sum_\sigma(-1)^{\sum_{e\in S}x_\sigma(e)}.
\]
Its support cardinality is the rank \(R(T)\), since the Walsh characters diagonalize convolution. Changing reference directions only changes the signs of multipliers and not their zeros. We regard isolated vertices as connected components of order one.

## Proof
**Known nonvanishing input.** For a forest \(H=(V,S)\), comparison signs factor under independent relative orders on its connected components. If a component has an even number of vertices, hence an odd number of edges, reversing all labels inside that component pairs sign contributions with their negatives. Conversely, for a tree of odd order the absolute \(-1\) Eulerian evaluation is strictly positive: by Theorem 1.4 and Lemma 4.3 of Celano--Sieger--Spiro [2], it counts positive even sequences. Their factorization across components then gives the previously implicit support criterion
\[
W_T(S)\ne0\quad\Longleftrightarrow\quad\text{every component of }(V(T),S)\text{ has odd order}.
\]
Only the sharp global count and unique extremizers below are asserted as the new contribution.

**Two-state count.** For a rooted subtree \(H\), let \(A(H)\) count selected-edge subsets for which every component not containing the root has odd order and the root component has odd order. Define \(B(H)\) similarly but with the root component of even order. A single vertex has \((A,B)=(1,0)\). Suppose a rooted partial tree has states \((A,B)\), and an independent rooted child subtree has states \((a,b)\). Not selecting the joining edge requires its child root component to be odd; selecting it joins the root components and toggles the latter's parity precisely when the child's root component is odd. Therefore the exact update is
\[
(A',B')=\bigl(A(a+b)+Ba,\ B(a+b)+Aa\bigr).
\]
Rooting \(T\) arbitrarily and processing each child once gives \(R(T)=A(T)\), requiring a linear number of integer operations.

**Fibonacci lower bound.** We prove simultaneously for every rooted tree on \(m\ge1\) vertices that \(A\ge F_m\) and \(B\ge F_{m-1}\). The one-vertex case is equality. Starting from its root and attaching child subtrees consecutively, suppose the current rooted tree has \(p\) vertices and an attached child has \(q\). Induction and the recurrence yield
\[
A'\ge F_pF_{q+1}+F_{p-1}F_q=F_{p+q},
\]
\[
B'\ge F_{p-1}F_{q+1}+F_pF_q\ge F_{p+q-1},
\]
using Fibonacci addition identities and \(F_{q+1}\ge F_{q-1}\). Thus \(R(T)\ge F_n\).

**Uniqueness of lower equality.** Delete an arbitrary leaf \(v\) of \(T\), adjacent to \(u\), and write \(H=T-v\). The two-state count with root \(u\) gives \(R(T)=A(H)+B_u(H)\). Both summands have respective lower bounds \(F_{n-1}\) and \(F_{n-2}\). Suppose \(n\ge5\) and equality holds. The first summand forces \(H\) to be a path by induction (the case \(n=4\) is immediate from the two four-vertex tree shapes). If \(u\) were internal in that path, split it at \(u\) into two nonempty arms of sizes \(p-1\) and \(q\), where \(p\ge2\), \(q\ge1\). An endpoint-rooted path of order \(j\) has exactly \((A,B)=(F_j,F_{j-1})\), so the update gives
\[
B_u(H)=F_{p-1}F_{q+1}+F_pF_q
> F_{p-1}F_{q-1}+F_pF_q=F_{p+q-1}=F_{n-2}.
\]
This contradicts equality. Hence \(u\) is an endpoint and \(T\) is a path. Conversely endpoint-rooted path states show \(R(P_n)=F_n\).

**Sharp upper bound and uniqueness.** A permissible selected-edge forest has all component orders odd, so every component has an even number of edges and therefore \(|S|\) is even. At most half of the \(2^{n-1}\) edge subsets have even size: \(R(T)\le2^{n-2}\). For a star every even-size selected set is allowed, since all its selected edges form one odd-order component plus isolated vertices. If \(T\) is not a star, it has two disjoint edges. The subset consisting of those two edges has even cardinality but contains two inadmissible two-vertex components. Thus the upper inequality is strict. This completes the proof.

## Verification
The self-contained `verify.py` exhaustively checks all 1,441 labelled trees of orders two through six using Prüfer sequences, comparing rooted dynamic programming to independent edge-subset enumeration. It also directly computes 2,142 signed-permutation multipliers for all labelled trees of orders two through five, verifying the predicted zero/nonzero criterion at every frequency. It confirms both equality classifications from order four onward. These finite tests supplement but do not replace the all-order proof.

## Relationship to prior work
Foata--Schützenberger [1] supplies classical descent enumerations, including Eulerian evaluations at \(-1\). Celano--Sieger--Spiro [2, Theorem 1.4; Lemma 4.3] already imply nonvanishing for each selected forest if and only if all component orders are odd; their Theorem 1.6 bounds the *magnitude of a single* signed Eulerian evaluation among odd-order trees. The present theorem instead counts *how many edge-subset evaluations survive* for each tree and determines the sharp shape extremizers, which are not implied by those magnitude bounds alone. Backman--Hopkins [3] supplies a different graph-orientation framework. Existing permutation descent-profile formulas recover the path endpoint, but do not establish the comparison across every tree.

## Limitations
No formula for the full values, signs, or magnitudes of all individual multipliers is asserted. The sharp bounds concern convolution rank only, not condition numbers or optimal inverse norms. Earlier literature might contain an equivalent odd-component-forest enumerator extremum not indexed in the checked material. The all-order step uses the previously published nonvanishing theorem, not finite computation. No independent mathematical audit has been performed.

## References
[1] D. Foata and M.-P. Schützenberger, *Théorie géométrique des polynômes eulériens*, original 1970 monograph; publicly archived 2005-08-15, https://arxiv.org/abs/math/0508232.

[2] K. Celano, N. Sieger, S. Spiro, *Eulerian Polynomials for Digraphs*, first posted 2023-09-13, https://arxiv.org/abs/2309.07240, especially Theorem 1.4, Lemma 4.3, and Theorem 1.6.

[3] S. Backman and S. Hopkins, *Fourientations and the Tutte Polynomial*, first posted 2015-03-19, https://arxiv.org/abs/1503.05885.
