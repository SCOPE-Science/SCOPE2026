# Exact optimal open-packing census and generating series for cyclic clique cylinders

## Finding

Let \(m\geq3\), \(n\geq5\) be integers, and put \(X_{m,n}=C_n\square K_m\). An *open packing* is a vertex subset whose distinct vertices have disjoint open neighborhoods. Let \(\rho^{\mathrm o}(X_{m,n})\) denote its maximum size, and let \(B_{m,n}\) count all distinct maximum open-packing vertex subsets of the labelled product (without identifying rotations or permutations of clique labels). Put \(a=m-1\). Then

\[
\rho^{\mathrm o}(X_{m,n})=\left\lfloor\frac{2n}{3}\right\rfloor,
\qquad
B_{m,n}=
\begin{cases}
3\bigl(a^k+(-1)^k a\bigr),&n=3k,\\[2pt]
\dfrac{3k+1}{2}\bigl(2a^k+2a^{k-1}+ka^{k+1}+(-1)^{k-1}ka\bigr),&n=3k+1,\\[2pt]
(3k+2)a\bigl(a^k-(-1)^k\bigr),&n=3k+2.
\end{cases}
\]

For the first and second cases, \(k\geq2\), and for the third, \(k\geq1\), as required by the stated domain. The formula is integral in all cases.

More strongly, an exact *all-cardinality* enumerator is available. Define the formal polynomial
\[
H_{m,n}(q)=\sum_{S\text{ an open packing of }X_{m,n}}q^{\,2n-3|S|}.
\]
The exponents are nonnegative. For every \(n\geq5\),
\[
H_{m,n}(q)=[x^n]\left(-x\frac{\partial}{\partial x}\log D_m(x,q)\right),
\]
where the logarithm is expanded as a formal power series in \(x\), and
\[
D_m(x,q)=
\bigl(1-ax^3-aqx^2-q^2(x+x^4)-q^3x^3\bigr)
\bigl(1+x^3+qx^2\bigr)^a.
\]
Thus the complete open-packing polynomial in the cardinality variable is recovered by replacing every term \(q^{2n-3s}\) with the monomial of degree \(s\). The leading-cardinality coefficients are the displayed \(B_{m,n}\).

## Assumptions and scope

The graphs are finite, simple, undirected, and have cyclically indexed columns \(i\in\mathbb Z/n\mathbb Z\) and independently labelled clique coordinates \(c\in\{1,\dots,m\}\). The cycle length condition \(n\ge5\) avoids exceptional short-cycle common-neighbor configurations. Distinct chosen vertex subsets are counted separately; graph automorphism orbits are not being counted.

## Proof

**Local characterization.** At most one chosen vertex can lie in any \(K_m\)-column, because two vertices in the same column have a common neighbor in that column when \(m\ge3\). Encode an open packing by a cyclic word \(w_0\cdots w_{n-1}\) over \(\{0,1,\ldots,m\}\), where zero means an unoccupied column and a nonzero symbol is the selected clique coordinate. For \(n\ge5\), direct inspection of the product neighborhoods gives precisely these additional restrictions:

* If consecutive columns are occupied, their nonzero symbols must be equal.
* If columns at cyclic separation two are occupied, their nonzero symbols must be different.

Conversely, these two restrictions and the one-vertex-per-column property eliminate every common-neighbor collision, since two vertices of the Cartesian product can share a neighbor only within one column, between adjacent columns, or between columns at separation two. In particular, three consecutive columns cannot all be occupied: consecutive symbols would all be equal, contradicting the separation-two condition. Summing this three-window bound over the cycle yields \(3|S|\le2n\).

**Deficiency transfer.** The permitted ordered pairs of neighboring column symbols consist of the state \((0,0)\) together with \((0,c),(c,0),(c,c)\) for each \(1\le c\le m\), giving \(1+3m\) states. Transition from \((u,v)\) to \((v,w)\) is permitted if the displayed local restrictions hold, and is weighted by
\[
q^{2-\mathbf1_{u\ne0}-\mathbf1_{v\ne0}-\mathbf1_{w\ne0}}.
\]
The exponent is nonnegative. The product of these transition weights around a closed length-\(n\) walk is exactly \(q^{2n-3|S|}\). Each indexed cyclic word corresponds to exactly one such closed walk, so \(H_{m,n}(q)=\operatorname{tr}(M_m(q)^n)\).

Permutation of the \(m\) nonzero symbols commutes with this transfer. Decompose the color coordinate into its one-dimensional constant subspace and its \((m-1)\)-dimensional zero-sum subspace. On the constant-color part, in the state order \((0,0),(0,c),(c,0),(c,c)\), the induced transition matrix is
\[
T=\begin{pmatrix}
q^2&mq&0&0\\
0&0&q&1\\
q&a&0&0\\
0&0&1&0
\end{pmatrix}.
\]
On each of the \(a=m-1\) independent zero-sum components, in the state order \((0,c),(c,0),(c,c)\), it is
\[
U=\begin{pmatrix}
0&q&1\\
-1&0&0\\
0&1&0
\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\det(I-xT)=1-ax^3-aqx^2-q^2(x+x^4)-q^3x^3,
\qquad
\det(I-xU)=1+x^3+qx^2.
\]
Hence \(\det(I-xM_m(q))=D_m(x,q)\). The formal trace/determinant identity \(\sum_{n\ge1}\operatorname{tr}(M^n)x^n=-x\partial_x\log\det(I-xM)\) proves the all-cardinality formula.

**Extracting the optimum.** For each \(j\ge0\), write \(L_j(x)=[q^j]\log D_m(x,q)\). The terms needed at the smallest possible deficiency in each circumference class are
\[
\begin{aligned}
L_0(x)&=\log(1-ax^3)+a\log(1+x^3),\\
L_1(x)&=-\frac{ax^2}{1-ax^3}+\frac{ax^2}{1+x^3},\\
L_2(x)&=-\frac{x+x^4}{1-ax^3}-\frac{a^2x^4}{2(1-ax^3)^2}-\frac{ax^4}{2(1+x^3)^2}.
\end{aligned}
\]
These follow by expanding \(\log(1+t)\) formally through degree two in \(q\), with no asymptotic approximation. Applying \(-x\partial_x\) and the geometric/binomial series gives, respectively,
\[
\begin{aligned}
[x^{3k}q^0](-x\partial_x\log D_m)&=3(a^k+(-1)^ka),\\
[x^{3k+2}q^1](-x\partial_x\log D_m)&=(3k+2)a(a^k-(-1)^k),\\
[x^{3k+1}q^2](-x\partial_x\log D_m)&=\frac{3k+1}{2}(2a^k+2a^{k-1}+ka^{k+1}+(-1)^{k-1}ka).
\end{aligned}
\]
In all three cases the displayed quantity is positive for \(a\ge2\) and the stated \(k\)-ranges. Since deficiencies are nonnegative and \(2n-3|S|\equiv2n\pmod3\), these are necessarily the first nonzero deficiency terms. They therefore show that \(\lfloor2n/3\rfloor\) is attainable and count all optimal sets. This completes the proof.

## Verification

The supplied `verify_symbolic.py` computes the two determinants exactly and independently compares the factorization against the full \((1+3m)\)-state determinant for \(m=3,4,5\). The supplied `verify_transfer.py` directly enumerates cyclic color words using the local restrictions, checking the optimum size and its multiplicity over multiple circumferences and clique orders. The separate `verify_direct.cpp` enumerates actual subsets of graph vertices and tests intersections of explicitly built neighborhoods, without relying on the word/transfer characterization. Its checked cases include \((n,m)=(8,3)\) and \((6,4)\), each involving 24 vertices. The corresponding output logs are included. The unrestricted proof is the determinant and coefficient calculation above, not the finite enumerations.

For illustration, for \(m=3\), at circumferences \(n=5,6,7,8,9,10,11,12\) the optimum multiplicities are respectively \(30,18,84,48,18,390,198,54\).

## Relationship to prior work

Mojdeh, Peterin, Samadi and Yero (arXiv:1901.06813; 2019/2020), Theorem 3.4, bound the open packing number of \(G\square K_m\) by the \(2\)-independence number of \(G\) for \(m>2\) and give conditions for equality through a component coloring. For cycles, this already supplies the scalar optimum through a straightforward specialization; **the scalar value alone is not claimed as new**. Their result does not calculate the exact number of optimal vertex subsets for every circumference and clique order, or the all-cardinality generating determinant above.

Brešar, Klavžar and Rall (arXiv:2309.04963, first posted 10 September 2023) study open packings in bipartite prisms \(G\square K_2\) and hypercubes. Their two-vertex clique factor and maximum-size result do not imply this labelled \(m\ge3\) count, and a cycle is nonbipartite when its length is odd. Work on clique-path products involves \(P_n\), not the cyclic boundary conditions of \(C_n\). The nontrivial term \((-1)^k\) here is the closing-color obstruction for the cycle, and is not determined by the path counts.

## Limitations

No claim is made for clique order two or for cycles of length three or four; those cases require separate treatment. The enumerated optimum sets use labelled vertices, not unlabeled symmetry classes. No independent expert audit is claimed. The literature comparison cannot exclude an unindexed prior exact table or an equivalent cyclic-word enumeration under different terminology.

## References

1. D. A. Mojdeh, I. Peterin, B. Samadi, I. G. Yero, *(Open) packing number of some graph products*, Discrete Mathematics & Theoretical Computer Science 22(4), 2020; arXiv:1901.06813, https://arxiv.org/abs/1901.06813.
2. B. Brešar, S. Klavžar, D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963 (2023), https://arxiv.org/abs/2309.04963.
3. M. A. Shalu, V. K. Kirubakaran, *Open Packing in Graphs: Bounds and Complexity*, arXiv:2406.06982 (2024), https://arxiv.org/abs/2406.06982.
