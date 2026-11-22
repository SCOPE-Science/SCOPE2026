# Two-phase concentration and one-defect law for tetrahedron-free hypergraph singleton types
## Finding
Let \(M\) be the countable homogeneous tetrahedron-free 3-uniform hypergraph. For \(n\ge1\), individually name an induced complete tripartite 3-hypergraph \(A_n\) with shores \(\{a\}\), \(B\), \(C\) of cardinalities \(1,n,n\), and all old triples \(\{a,b,c\}\) with \(b\in B\), \(c\in C\). Let \(P_n(z)\) enumerate complete nonalgebraic singleton types over \(A_n\) by the number of new hyperedges meeting the singleton. Then, for every integer \(n\ge1\),
\[
\boxed{P_n(z)=(1+z)^{n(n-1)}\sum_{i=0}^n\sum_{j=0}^n\binom ni\binom nj z^{i+j}(1+z)^{n^2-ij}.}
\]
In particular, if \(T_n=P_n(1)\),
\[
T_n=2^{2n^2-n}S_n,\qquad
S_n=\sum_{i,j=0}^n\binom ni\binom nj 2^{-ij}
=2^{n+1}+2n(3/2)^n+o\bigl(n(3/2)^n\bigr).
\]
Choose a complete nonalgebraic type uniformly from those counted by \(T_n\). Let \(I\subseteq B\) and \(J\subseteq C\) be the old vertices forming new triples with the singleton and \(a\). Then
\[
\boxed{\Pr(I\ne\varnothing,\ J\ne\varnothing)\sim n(3/4)^n.}
\]
With probability tending to one, exactly one of \(I,J\) is empty, each choice of empty shore having asymptotic probability one half. On the occupied shore the size, divided by \(n\), converges in probability to \(1/2\). Conditioned on the exponentially rare event \(I,J\ne\varnothing\), with probability tending to one the smaller of \(|I|,|J|\) is exactly one and the larger size, divided by \(n\), converges in probability to \(1/3\). The two choices of exceptional singleton shore have asymptotic conditional probability one half. In fact, conditioned on \(|I|=1\) and \(|J|\ge1\), \(|J|\) has exactly the \(\operatorname{Bin}(n,1/3)\) law conditioned to be positive, and similarly with the shores exchanged.

## Assumptions and scope
A tetrahedron means all four triples on some four vertices, not a graph-theoretic 4-clique. The language has one irreflexive symmetric ternary relation. The finite old hypergraph \(A_n\) consists of \(2n+1\) individually named vertices. No old triples except those with one vertex from each of the three shores are present. This is tetrahedron-free (any four-set contains at most two of these triples). The count treats every old vertex as named, and excludes algebraic types realized by old vertices. All singleton types are complete in the theory of \(M\). The number \(n\) tends to infinity along positive integers. The distribution is uniform on *admissible labelled singleton types*, not on random realized vertices of \(M\).

## Proof
**1. Admissible link assignments.** Finite tetrahedron-free 3-hypergraphs form a free-amalgamation Fraïssé class. Over a finite named old hypergraph, each complete nonalgebraic new-point type corresponds to one consistent assignment of the ternary relation on triples containing the new point \(x\) and two distinct old vertices; every such assignment is realized infinitely often. Write \(L\subseteq\binom{A_n}{2}\) for those old pairs \(uv\) for which \(\{x,u,v\}\) is a new triple. The only forbidden configurations arise when an old triple \(\{a,b,c\}\) and all three link pairs \(ab,ac,bc\) occur.

**2. Exact polynomial.** Set \(I=\{b\in B:ab\in L\}\), \(J=\{c\in C:ac\in L\}\), and \(i=|I|\), \(j=|J|\). Precisely the \(ij\) cross-shore pairs in \(I\times J\) must be absent from \(L\). All other cross-shore pairs are independent choices. Every within-shore pair is free: there are \(2\binom n2=n(n-1)\) such pairs. Thus a fixed \((I,J)\) contributes \(z^{i+j}(1+z)^{n(n-1)+n^2-ij}\), proving the displayed identity after summing \(\binom ni\binom nj\) possible pairs of sets. Evaluation at \(z=1\) gives \(T_n=2^{2n^2-n}S_n\).

**3. Exact separation and asymptotic remainder.** The configurations with \(i=0\) or \(j=0\) contribute \(2^{n+1}-1\) to \(S_n\). Among configurations with \(i,j\ge1\), those with \(i=1\) or \(j=1\) contribute
\[
2n\big((3/2)^n-1\big)-n^2/2.
\]
The subtracted term is the \(i=j=1\) intersection counted twice. Define the remaining nonnegative term
\[
R_n=\sum_{i,j\ge2}\binom ni\binom nj2^{-ij}.
\]
To bound it, split off those ordered pairs with \(2\le\min(i,j)\le4\). Their total is at most \(2\sum_{i=2}^4\binom ni(5/4)^n=O(n^4(5/4)^n)\). For \(i,j\ge5\), the elementary inequality \(ij\ge\tfrac52(i+j)\) yields
\[
\sum_{i,j\ge5}\binom ni\binom nj2^{-ij}\le(1+2^{-5/2})^{2n}.
\]
Put \(\rho=(1+2^{-5/2})^2\). Since \(\rho<3/2\),
\[
R_n=O\bigl(n^4(5/4)^n+\rho^n\bigr)=o\bigl(n(3/2)^n\bigr).
\]
Consequently \(S_n=2^{n+1}-1+2n((3/2)^n-1)-n^2/2+R_n\), proving the two-term asymptotic. The mixed-shore mass is precisely \(S_n-(2^{n+1}-1)=2n(3/2)^n(1+o(1))\), whereas \(S_n\sim2^{n+1}\). The ratio is \(n(3/4)^n(1+o(1))\).

**4. Typical and exceptional laws.** For \(I=\varnothing\), all \(J\subseteq C\) contribute equally to the normalized count; hence the conditional \(|J|\) distribution is \(\operatorname{Bin}(n,1/2)\). The symmetric phase is the same. The overlap \(I=J=\varnothing\) has weight one, negligible compared with \(2^{n+1}\). The mixed-event probability tends to zero, so the pure-phase size conclusions follow from the binomial law of large numbers.

Let \(E_B\) denote \(|I|=1,|J|\ge1\) and \(E_C\) its symmetric analogue. Each has normalized weight \(n((3/2)^n-1)\), and their overlap has weight \(n^2/2\). By the bound on \(R_n\), the mass of mixed configurations outside \(E_B\cup E_C\) is negligible compared with \(2n(3/2)^n\). Thus conditioned on being mixed, the two exclusive singleton-shore cases each have asymptotic probability \(1/2\). For \(E_B\), fixing \(I\) with one element gives the exact conditional distribution
\[
\Pr(|J|=j\mid E_B)
=\frac{\binom nj2^{-j}}{(3/2)^n-1},\qquad 1\le j\le n.
\]
This equals a \(\operatorname{Bin}(n,1/3)\) conditioned on being positive, which satisfies \(|J|/n\to1/3\) in probability. The symmetric case is identical. This proves the exceptional size claim.

## Verification
The bundled \(hypergraph_link_verify.py\) uses only the Python standard library. It computes the graded polynomial from the shore formula and independently from inclusion-exclusion on all forbidden old triples for \(1\le n\le4\). For \(1\le n\le3\), it further directly enumerates every binary link assignment on \(\binom{2n+1}{2}\) old pairs, checking forbidden tetrahedra. It verifies exact rational type-count and mixed decomposition identities for \(n\le4\), and tests the convergence ratio for \(n=8,12,20,40,60,100\). Recorded counts are \(T_1=7\), \(T_2=644\), \(T_3=832576\), \(T_4=15724974080\). The final output line is \(\texttt{VERIFY\_OK}\). These finite checks support, but do not replace, the unrestricted proof and its explicit remainder bound.

## Relationship to prior work
The free-amalgamation and quantifier-elimination setting for generic forbidden-clique hypergraphs is established in Conant (2015). A published exact overlap-matching lower bound for singleton-type counts in the *same* tetrahedron-free age applies to any finite base and is a stronger statement about a **different invariant** (a general lower bound), not an evaluation of the present balanced-tripartite spectrum or its conditional rare-event law. Its pair-pencil example has all old triples sharing a fixed pair, while the present family has \(n^2\) old triples supported on a two-shore crossing and a single hub. The published type-polynomial result for the \(K_4^-\)-free age forbids even three triples on four vertices; its local link restrictions therefore differ from those here. Classical hard-core phase coexistence and related two-spin models provide conceptual analogies but do not by themselves determine the finite logical-type defect coefficient \(n(3/4)^n\) or the conditional \(1/3\)-density in this family. These established ingredients and analogies are not claimed new; the assessed contribution is their exact type-spectrum specialization and sharp rare one-defect law.

## Limitations
The results concern complete one-point types over the specifically described balanced tripartite old hypergraphs, and uniform sampling among *types*, not random realizations. No higher-arity type distribution, unbalanced shore limit, or concentration across randomly chosen old hypergraphs is asserted. While targeted literature searches and relevant full-text comparisons have not found the precise claim, unindexed equivalent formulations of the complete-bipartite two-spin partition function could affect historical originality. Independent mathematical audit has not been performed.

## References
1. G. Conant, “An axiomatic approach to free amalgamation,” first public arXiv posting 2015-05-04, arXiv:1505.00762; *Journal of Symbolic Logic* 82 (2017), 648–671. https://arxiv.org/abs/1505.00762 .
2. “Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-overlap-matching-bounds-for-one-point-types-of-the-generic--5ae2c90229c3 .
3. “Triangle-free envelopes for 1-types in the random K4-minus-free 3-hypergraph,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-triangle-free-envelopes-for-1-types-in-the-random-k4-minus-free--ae10e5d4346d .
4. J. Kahn, “An entropy approach to the hard-core model on bipartite graphs,” *Combinatorics, Probability and Computing* 10 (2001), 219–237. DOI:10.1017/S0963548301004631. The analogy is probabilistic, not a claimed use of Kahn's theorem.
