# The unique fort orbit separating Clebsch zero forcing from binary information sets

## Finding

Let \(C\) be the five-regular Clebsch graph, regarded as the folded five-cube. The closed-neighborhood matrix \(M=I+A(C)\) over \(\mathbb F_2\) has rank six. A six-element set \(W\) of initially white vertices supports a successful *ordinary* zero-forcing process from its black complement exactly when the six columns \(M[:,W]\) are independent **and** \(C[W]\not\cong P_3\sqcup3K_1\). Thus the natural linear-recovery test has a single exceptional induced-graph type:

\[
\begin{array}{c|r}
\text{six-set class}&\text{count}\\\hline
\operatorname{rank}_{\mathbb F_2}M[:,W]<6&3976\\
\operatorname{rank}_{\mathbb F_2}M[:,W]=6,\ C[W]\cong P_3\sqcup3K_1&160\\
\operatorname{rank}_{\mathbb F_2}M[:,W]=6,\ C[W]\not\cong P_3\sqcup3K_1&3872
\end{array}
\]

All 160 exceptional six-sets are one orbit of the full affine automorphism group. The 3872 forceable white complements are not bases of any matroid even though they lie inside the rank-six binary column-matroid basis family. The count of 3872 ordinary optimum zero-forcing sets and the value \(Z(C)=10\) were known; the new assertion is their exact comparison with binary information sets and the exceptional-fort classification.

## Assumptions and scope

Vertices are the integers \(0,\ldots,15\), interpreted as four-bit vectors; write \(u\oplus v\) for bitwise XOR. Set
\[
D=\{1,2,4,8,15\},\qquad u\sim v\iff u\oplus v\in D.
\]
The graph is simple and five-regular. Write \(A\) for its zero-diagonal adjacency matrix. All matrix ranks below are over \(\mathbb F_2\), not over \(\mathbb R\). A *zero-forcing step* recolours the unique white neighbour of a black vertex black; simultaneous applications are allowed only as a test of eventual success, equivalent to arbitrary legal sequential steps. A *fort* is a nonempty white set \(W\) such that every vertex outside \(W\) has a number of neighbours in \(W\) different from one. The theorem concerns precisely all \(\binom{16}{6}=8008\) choices of \(W\); no claim is made for other graphs or about a universal binary-matroid description of zero forcing.

## Proof

**1. Binary code and necessary condition.** The vector in column \(w\) of \(M\) has a one at \(w\) and at each neighbour of \(w\). Gaussian elimination of its 16 integer-bitmask columns, using XOR, gives exactly six independent pivots. Thus the row-space code is binary \([16,6,6]\); direct enumeration of its 64 words gives weights \(0:1,6:16,8:30,10:16,16:1\). If \(V\setminus W\) is a successful zero-forcing set and some vector \(x\in\ker M\) is supported within \(W\), apply the linear equation at a currently black forcing vertex: its unique still-white neighbour must have zero coordinate in \(x\). Induct along a complete forcing sequence. Eventually \(x=0\), so the six columns \(M[:,W]\) are independent. This proves necessity without computation except for the graph-specific rank.

**2. The geometric exception is one orbit of 160 forts.** Every induced three-vertex path has a unique centre. Since the Clebsch graph is triangle-free and five-regular, the number of induced paths on three vertices is \(16\binom52=160\). The affine group of translations together with permutations of the five direction vectors in \(D\) is transitive on such paths. For the canonical path \(0-1\) and \(0-2\), the common nonneighbours outside the path are exactly \(7,11,12\). They are mutually nonadjacent, so this path extends **uniquely** to a six-set inducing \(P_3\sqcup3K_1\):
\[
W_0=\{0,1,2,7,11,12\}.
\]
For every vertex outside \(W_0\), the numbers of neighbours in \(W_0\), in increasing vertex order \(3,4,5,6,8,9,10,13,14,15\), are \(5,3,2,2,3,2,2,2,2,3\). None is one, hence \(W_0\) is a fort. Gaussian elimination shows \(\operatorname{rank}M[:,W_0]=6\). These properties are invariant under the affine graph automorphisms, so all 160 sets are independent-column forts. The group \(\mathbb F_2^4\rtimes S_5\) has order 1920, and the 160-set orbit has stabilizer order 12.

**3. Exhaustive sufficiency certificate.** It remains to show that no other independent-column six-set resists forcing. The two standalone scripts specify, without external data, the adjacency graph and enumerate each unordered six-set exactly once. On each, they independently test rank-six, the induced degree sequence \((0,0,0,1,1,2)\), and ordinary forcing. The logical assertion checked for every one of the 8008 sets is
\[
\operatorname{ZF}(V\setminus W)\iff
\big(\operatorname{rank}_{\mathbb F_2}M[:,W]=6\big)
\land\big(C[W]\not\cong P_3\sqcup3K_1\big).
\]
The Python checker uses synchronous colour updates and column-echelon rank; the C++17 checker uses sequential first-legal moves and independent on-the-fly binary elimination. Their matching complete results are the three rows of the table. The finite loops cover all \(\binom{16}{6}\) cases, rather than sampling a subset; these exact computations certify this finite graph claim, not an infinite-family theorem. The known existence of 3872 successful ten-sets and the rank bound also independently confirm \(Z(C)=10\).

**4. Basis-exchange obstruction.** Take
\[
W_1=\{1,6,11,12,14,15\},\qquad W_2=\{1,2,5,8,10,15\}.
\]
Both have forceable black complements. But after deleting 14 from \(W_1\), none of the four choices \(2,5,8,10\) from \(W_2\setminus W_1\) restores a forceable white complement. The choices 2,5,8 yield dependent columns; the choice 10 yields an independent-column set inducing \(P_3\sqcup3K_1\). This violates the basis exchange axiom for the forceable-white-complement family. The rank-six column bases themselves do satisfy the matroid axioms; the obstruction concerns their forcing subfamily.

## Verification

Run from an extracted copy of the package:

```bash
python3 clebsch_information_sets.py
g++ -O2 -std=c++17 clebsch_information_sets.cpp -o clebsch_check
./clebsch_check
```

Both produce `PASS` upon checking all 8008 six-vertex subsets. The Python program additionally tests the 160-member exceptional orbit using eight explicit generators and checks the weight enumerator of the 64 binary codewords. The scripts are complete and standalone; no external graph tables, network access, third-party packages, or precomputed certificates are required.

## Relationship to prior work

The original zero-forcing/minimum-rank literature provides the propagation rule and linear nullity bound. The folded-cube literature identifies the canonical five-regular Clebsch model. Work on matroidal null supports and forts supplies the broader linear-algebraic motivation. Earlier computations of this same graph already established its ordinary zero-forcing number ten, the 3872 optimum sets, seven symmetry orbits, and their exchange geometry. Those results are treated as prior coverage, not as new here. The present comparison newly identifies a binary linear-algebraic relaxation with 4032 bases and its exact 160-instance geometric failure mode. None of the inspected primary sources gives that exact if-and-only-if characterization.

## Limitations

The proof of the sufficiency direction uses a complete finite enumeration for this 16-vertex graph, while the fort count and necessity have independent structural arguments. The binary matrix \(I+A\) is a particular matrix, not every matrix supported on this graph, and binary rank is not asserted equal to real minimum rank. Full historical priority cannot be guaranteed: unindexed coding-theory tabulations or unpublished computations might contain an equivalent condition. No result about all folded cubes, all linear codes, or efficient recognition on arbitrary graphs is claimed. Verification is same-model, not independent scholarly audit.

## References

1. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, first publicly available 26 November 2007, https://www.mat.uc.pt/~leal/FCT09/AIM08.pdf ; journal version *Linear Algebra and its Applications* 428 (2008), 1628–1648, doi:10.1016/j.laa.2007.10.009.
2. *Cores of cubelike graphs*, *European Journal of Combinatorics* 2020, doi:10.1016/j.ejc.2020.103092 (folded-cube Cayley construction).
3. L. Deaett, V. Furst, J. Hutchens, L. Mitchell, *A matroid characterization of the combinatorially symmetric maximum nullity of a graph*, arXiv:2611.01102 (2026), https://arxiv.org/abs/2611.01102.
4. *Propagation time for zero forcing on a graph*, arXiv:1410.4191 (2014), https://arxiv.org/abs/1410.4191.
