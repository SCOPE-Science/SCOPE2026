# Single-edge deletion stability of maximum cuts in two-token complete graphs

## Finding

Let \(n\ge3\) be an integer, let \(a,b\) be distinct vertices of \(K_n\), and put \(G_n=K_n-ab\). Write \(F_2(G_n)\) for the ordinary unweighted two-token graph, whose vertices are all unordered two-element subsets of \(V(G_n)\), with two token states adjacent exactly when their symmetric difference is an edge of \(G_n\). Write \(m(H)\) for the maximum number of edges crossing a vertex bipartition of a graph \(H\).

Set
\[
M_n=n\left\lfloor\frac{(n-1)^2}{4}\right\rfloor-\mathbf{1}_{n\equiv3\pmod4}.
\]
The sharp deletion-stability theorem is
\[
\boxed{m(F_2(K_n-ab))=M_n-2\mathbf{1}_{n=5}.}
\]
In particular, deleting a base edge removes \(n-2\) edges from the triangular Johnson graph \(F_2(K_n)=J(n,2)\), yet leaves its maximum-cut value unchanged except at order five. The source motivating the problem is the 2025 study of token-graph spectral bounds and cut-based comparisons by Apte, Parekh and Sud [1]; a later, separately dated 2026 preprint [2] obtains the undeleted Johnson optimum but does not determine this edge-deleted optimum.

There is also an exact description of its optimal cuts. Identify a token-state colour class with a spanning simple red graph \(R\) on the \(n\) base labels: \(uv\in E(R)\) means that the token state \(\{u,v\}\) is on the red side of the cut. For \(n\ne5\), this cut is optimal exactly when its red degrees obey the following conditions and \(aw\in E(R)\iff bw\in E(R)\) for each \(w\notin\{a,b\}\):

* If \(n\equiv1\pmod4\), every red degree is \((n-1)/2\).
* If \(n\equiv3\pmod4\), exactly one red degree differs by one from \((n-1)/2\), and all other red degrees equal \((n-1)/2\).
* If \(n\) is even, each red degree belongs to \(\{(n-2)/2,n/2\}\).

For \(n=5\), an optimal cut is exactly either a two-colouring in which \(R\) is a five-cycle, or a two-colouring satisfying the endpoint-synchrony condition above and having exactly two red degrees at distance one from two, with the other three degrees equal to two. There are precisely \(32\) ordered red/blue optimal cuts, equivalently \(16\) cuts up to exchanging colours.

## Assumptions and scope

All graphs are simple, finite and unweighted. The distinguished deleted edge \(ab\) may be any edge of \(K_n\); by symmetry its identity does not affect the answer. The two-token graph retains all \(\binom n2\) token states, including the state \(\{a,b\}\). An ordered cut treats its two colour classes as named; its unordered version identifies a cut with its colour reversal. No claim is made for higher token counts, other deleted-edge configurations, or arbitrary base graphs.

## Proof

### 1. Exact projection to an incidence-degree objective

Fix a red token-state set \(R\subseteq\binom{[n]}2\) and put \(r_v=|\{w:\{v,w\}\in R\}|\). Every edge of the triangular Johnson graph \(J(n,2)\) joins two pairs sharing a unique label \(v\). For that label, the \(n-1\) incident pairs induce a clique. Thus its cut has size
\[
C_J(R)=\sum_{v=1}^{n}r_v(n-1-r_v).
\tag{1}
\]
After deleting \(ab\) in the base graph, precisely the \(n-2\) token edges \((\{a,w\},\{b,w\})\), with \(w\notin\{a,b\}\), disappear. Define
\[
p(R)=\sum_{w\notin\{a,b\}}\mathbf{1}_{\{a,w\}\in R\;\mathrm{xor}\;\{b,w\}\in R}.
\]
Therefore the exact remaining cut size is
\[
C_G(R)=C_J(R)-p(R),\qquad 0\le p(R)\le n-2.
\tag{2}
\]
In particular \(C_G(R)\le C_J(R)\). Each summand of (1) is bounded by \(\lfloor(n-1)^2/4\rfloor\). If \(n\equiv3\pmod4\), its maximizing red degree \((n-1)/2\) is odd, so an all-maximizing sequence would have odd degree sum on an odd number of vertices, impossible by the handshake lemma. Therefore at least one summand loses one, giving the upper bound \(C_J(R)\le M_n\) for all \(n\ge3\). This is a self-contained bound requiring no unverified external extremal theorem. Hence \(m(F_2(K_n-ab))\le M_n\).

Equality requires both \(C_J(R)=M_n\) and \(p(R)=0\). Equality in the incidence-degree upper bound has exactly the red-degree patterns stated in the Finding: for odd order \(n\equiv1\pmod4\), all degrees are exactly central; for odd order \(n\equiv3\pmod4\), precisely one is off by one; and for even order every degree is one of the two central integers. The case \(n\equiv3\pmod4\) cannot have all degrees central because the proposed total red degree would be odd. Conversely each displayed degree pattern gives \(C_J(R)=M_n\). The condition \(p(R)=0\) is precisely the stated endpoint synchrony.

### 2. Simultaneously balanced and synchronized constructions

It remains to exhibit such an \(R\) for every \(n\ne5\). Fix \(a=0,b=1\). For \(n=3\), choose \(R=\{ab\}\). For \(n=4\), choose two disjoint red edges, one of them \(ab\). Direct substitution into (1)–(2) gives the desired \(M_n\) in both cases.

For \(n\ge6\), partition the other \(n-2\) labels into \(S\sqcup T\) of the indicated sizes. In all four cases choose \(ab\) red, choose both \(as,bs\) red for every \(s\in S\), choose both \(at,bt\) blue for every \(t\in T\), and make \(T\) a red clique. Make the red graph induced on \(S\) a complete graph minus a specified graph \(D\). Choose the red cross-edges between \(S\) and \(T\) as follows:

| Order | \(|S|\) | \(|T|\) | Deleted \(D\) within \(S\) | Red cross-edges |
|---|---:|---:|---|---|
| \(n=4q\), \(q\ge2\) | \(2q-1\) | \(2q-1\) | A length-two path plus a matching on the remaining \(2q-4\) vertices | Perfect matching between \(S,T\) |
| \(n=4q+1\), \(q\ge2\) | \(2q-1\) | \(2q\) | A length-two path plus a matching on the remaining \(2q-4\) vertices | Each \(t\in T\) has one red neighbour in \(S\); the centre of the deleted path has two such neighbours, and each other \(s\in S\) has one |
| \(n=4q+2\), \(q\ge1\) | \(2q\) | \(2q\) | A perfect matching on \(S\) | Perfect matching between \(S,T\) |
| \(n=4q+3\), \(q\ge1\) | \(2q\) | \(2q+1\) | A perfect matching on \(S\) | A matching that covers \(S\) and all but one vertex of \(T\) |

Every clause is feasible: when a length-two path is deleted, its centre and two endpoints consume three of the odd number \(2q-1\) of vertices of \(S\), leaving an even number for the matching. The cross-edge degree requirement at \(n=4q+1\) uses \(2+(2q-2)=2q=|T|\) incidences.

Inspecting red degrees gives, respectively:

* \(n=4q\): the degrees of \(a,b\) are \(2q\); one vertex of \(S\) has degree \(2q-1\), the others have degree \(2q\); each vertex of \(T\) has degree \(2q-1\).
* \(n=4q+1\): every degree is \(2q\).
* \(n=4q+2\): \(a,b\) and all of \(S\) have degree \(2q+1\), while every vertex of \(T\) has degree \(2q\).
* \(n=4q+3\): every degree is \(2q+1\), except the unmatched vertex of \(T\), whose degree is \(2q\).

The two deleted-edge endpoints always have identical red/blue incidences to every external label, so \(p(R)=0\). These degrees attain the full Johnson optimum. Hence \(C_G(R)=M_n\) for every \(n\ne5\).

### 3. Why exactly five vertices lose two edges

For \(n=5\), equation (1) may be written as
\[
C_J(R)=20-\sum_{v}(r_v-2)^2.
\tag{3}
\]
It is impossible for this score to be \(19\): a sum of squares equal to one would mean that exactly one red degree is odd, contradicting the even sum of red degrees. A cut with score \(20\) has every red degree two; the red graph must therefore be a five-cycle. For any two distinct vertices of a five-cycle, their red adjacencies to the remaining three vertices differ in exactly two positions, whether they are adjacent or nonadjacent along the cycle. Thus \(p(R)=2\) for every Johnson-optimal cut. Every other cut has \(C_J(R)\le18\), and by (2) its reduced score is at most 18. Taking any red five-cycle yields score \(20-2=18\). This proves the exceptional optimum.

To count the optimal cuts, there are exactly \((5-1)!/2=12\) labelled red five-cycles, each supplying one ordered red/blue cut. Every other optimum must have \(C_J(R)=18\) and \(p(R)=0\). Put \(t=\mathbf{1}_{ab\in R}\) and let \(s\) be the number of the three remaining vertices joined in red to both \(a\) and \(b\). Then \(r_a=r_b=t+s\). The condition \(C_J(R)=18\) is, by (3), precisely two vertices of red degree one or three and three of degree two. Exhausting the possible edge sets on the remaining three labelled vertices under these degree constraints gives:

| \((t,s)\) | Number of ordered cuts |
|---|---:|
| \((1,0)\) | 1 |
| \((0,3)\) | 1 |
| \((0,2)\) | 9 |
| \((1,1)\) | 9 |

For the two middle cases with \(t+s=2\), choose the two-element set of synchronized red neighbours in three ways and then choose either of the two single-defect edges or the symmetric double-defect pair, giving \(3(2+1)=9\) possibilities; the second case is the colour complement of the first. The two remaining cases are respectively the all-red triangle on the three external vertices with only \(ab\) red at the endpoints, and its complement. Thus there are \(12+1+1+9+9=32\) ordered optimal cuts. Since none is invariant under swapping the two named sides, there are \(16\) unordered cuts.

These arguments also give the claimed if-and-only-if characterizations of all optimal cuts. \(\square\)

## Verification

The standalone Python 3 script `verify.py` constructs a cut for every order from \(3\) through \(100\), checks endpoint synchronization and the exact cut scores, and independently enumerates every ordered two-colouring of the token states for each order \(3\le n\le6\). The independent enumeration builds the token edges directly from symmetric differences, rather than trusting the degree identity. Its output is:

```text
EXPLICIT_ALL_RESIDUE_CONSTRUCTIONS_PASS n=3..100
INDEPENDENT_TOKEN_EDGE_EXHAUSTIVE_PASS 3 8 2 2
INDEPENDENT_TOKEN_EDGE_EXHAUSTIVE_PASS 4 64 8 2
INDEPENDENT_TOKEN_EDGE_EXHAUSTIVE_PASS 5 1024 18 32
INDEPENDENT_TOKEN_EDGE_EXHAUSTIVE_PASS 6 32768 36 56
EXCEPTIONAL_FIVE_VERTEX_CYCLE_PASS
VERIFY_OK
```

To reproduce, run `python3 verify.py` in a directory containing the extracted file. The exhaustive checks establish the finite cases listed; the proof above, not the finite experiments, establishes the all-order theorem.

## Relationship to prior work

Apte, Parekh and Sud [1, Sections 1.1, 2.1, A.3 and D.2] present token-graph definitions, identify the complete-graph token graph with a Johnson graph, and investigate token-graph spectral phenomena in relation to ordinary graph maximum cuts. Their objective differs from the exact maximum cut **of** a token graph; no assertion that their spectral results directly imply the theorem is made. Their first public preprint is dated 2025-06-03.

The later preprint by Alejandro-Soto et al. [2, Proposition 5], first posted 2026-11-18, calculates the maximum cut of the **intact** two-token complete graph. Its formula agrees with the upper bound derived independently from (1) here, but does not cover the graph with a missing base edge, the existence of synchronized optima, or the exceptional five-vertex census. It was inspected as strongly relevant comparative literature, not used to determine the claim's 2025 source date. Brouwer et al. [3] study eigenvalues of unperturbed Johnson and other distance-regular graphs; those spectra do not themselves determine maximum cuts of this perturbed family.

The present theorem treats a deletion of an \(n-2\)-edge **matching** from the triangular Johnson graph. The degree-balance and endpoint-synchronization construction and the five-vertex obstruction are required beyond either prior source.

## Limitations

The formula concerns a single missing base edge and exactly two tokens. It does not assert robustness for two or more deleted base edges or three or more tokens. The full classification of optimal cuts is structural; an all-order closed formula for the *number* of optimal cuts is not given. The existing published literature may include equivalent formulations under other graph names or optimization conventions; priority has not been independently certified.

## References

1. A. Apte, O. Parekh, and J. Sud. *Conjectured Bounds for 2-Local Hamiltonians via Token Graphs*. arXiv:2506.03441v1 (first publicly posted 2025-06-03). https://arxiv.org/html/2506.03441v1
2. J. A. Alejandro-Soto, P. T. Araujo, R. Fabila-Monroy, S. G. Gómez-Galicia, M. Hibat-Allah, M. M. R. Raj, M. A. Shamim, and A. L. Trujillo-Negrete. *Max-Cut on Token Graphs*. arXiv:2611.25153v1 (first posted 2026-11-18; comparison only). https://arxiv.org/html/2611.25153v1
3. A. E. Brouwer, S. M. Cioabă, F. Ihringer, and M. McGinnis. *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*. Journal of Combinatorial Theory, Series B 133 (2018), 88–121. arXiv:1709.09011. https://arxiv.org/abs/1709.09011
