# Exact shattered-edge supports of Hamiltonian tours in complete graphs

## Finding
Let \(n\ge3\), let \(E_n=\binom{[n]}2\), and let \(\mathcal H_n\subseteq2^{E_n}\) consist of the edge sets of all undirected Hamiltonian cycles of the complete graph \(K_n\). A support \(S\subseteq E_n\) is *shattered* if for every \(T\subseteq S\) a Hamiltonian cycle \(C\) satisfies \(C\cap S=T\). A *linear forest* is a spanning graph on \([n]\) all of whose components are paths (singletons are permitted); its component lengths count edges, not vertices.

**Exact classification.** A support \(S\) is shattered if and only if it is a linear forest satisfying one of the following:

1. \(|S|\le n-3\); or
2. \(|S|=n-2\), hence it has precisely two path components, and either one component is a singleton while the other contains at least three edges, or both components contain at least three edges.

No support of size \(n-1\) or greater is shattered. In particular,
\[
\operatorname{VCdim}(\mathcal H_n)=
\begin{cases}0&n=3,\\1&n=4,\\n-2&n\ge5.\end{cases}
\]

**Complete polynomial.** Put \(\Phi_n(z)=\sum_{m\ge0}s_m(n)z^m\), where \(s_m(n)\) counts unordered shattered supports of size \(m\). For \(0\le m\le n-3\),
\[
 s_m(n)=n!\,[x^n z^m]\exp\!\left(x+\frac{x^2z}{2(1-xz)}\right).
\]
For \(n\ge5\), the only additional nonzero coefficient is
\[
 s_{n-2}(n)=\frac{n!}{2}
 +\frac{n!}{4}\max\!\left\{0,\left\lfloor\frac{n-1}{2}\right\rfloor-3\right\}
 +\frac{n!}{8}\,\mathbf1_{\{n\ge8\text{ even}\}}.
\]
For \(n=3,4\), this top coefficient is zero. Thus \(\Phi_3(z)=1\), \(\Phi_4(z)=1+6z\), and
\[
\Phi_5(z)=1+10z+45z^2+60z^3,\quad
\Phi_6(z)=1+15z+105z^2+375z^3+360z^4.
\]
At the upper edge count a genuine geometric exception occurs: two disjoint spanning paths can be shattered together only when **each has at least three edges**.

## Assumptions and scope
Graphs are finite, simple, loopless, undirected, and labeled on \([n]\). Hamiltonian cycles use all \(n\) vertices and are identified up to rotation and reversal. The concept domain is the **edge set**, not the graph's vertex set, and the hypotheses are **spanning Hamiltonian cycles only**, not arbitrary simple cycles, connected edge sets, or paths. We take the empty support as shattered because \(\mathcal H_n\ne\varnothing\) for \(n\ge3\). Coefficient extraction is formal power-series extraction; \(\mathbf1\) denotes an indicator.

## Proof
**1. Necessary forest and size restrictions.** Since the trace \(S\) itself must occur, a shattered support is contained in a Hamiltonian cycle. Every proper subset of a simple cycle is a linear forest. If \(|S|\ge n\), its only possible containment is equality with one cycle, but then the trace \(S\setminus\{e\}\) cannot be realized while preserving all other \(n-1\) cycle edges. If \(|S|=n-1\), \(S\) is a spanning Hamiltonian path \(v_1v_2\cdots v_n\). The trace consisting of all its edges except \(v_1v_2\) is impossible: its remaining forced path has endpoints \(v_2,v_n\), so the sole leftover vertex \(v_1\) must attach to both endpoints, necessarily introducing the forbidden edge \(v_1v_2\). Thus a shattered support is a linear forest with at most \(n-2\) edges.

**2. A path-complement lemma.** For every \(b\ge5\), the complement in \(K_b\) of any linear forest on its \(b\) vertices contains a Hamiltonian cycle. Every linear forest is a subgraph of a spanning path. For \(b=5\), the complement of the path \(1-2-3-4-5\) contains the cycle \(1-3-5-2-4-1\). For \(b\ge6\), after deleting the edges of any linear forest each vertex retains degree at least \(b-3\ge b/2\), and Dirac's Hamiltonicity theorem applies. This includes isolated vertices and empty forests.

**3. Contracting any prescribed positive trace.** Fix a linear forest \(S\) and target trace \(T\subseteq S\). Contract each path component of the spanning graph \(([n],T)\) to a block. There are exactly \(b=n-|T|\) blocks. The \(|S\setminus T|\) forbidden edges induce a linear forest \(F\) on the blocks: deletion and contraction in the paths of \(S\) preserve the path-forest property. If \(b\ge5\), the lemma supplies a cyclic block order avoiding every edge of \(F\). Traversing the forced paths inside their blocks and joining successive blocks using the endpoints gives a Hamiltonian cycle. No joining edge belongs to \(S\setminus T\), since the chosen block order avoids all the corresponding block adjacencies. A singleton block has one vertex used for both external joins.

**4. Supports with \(|S|\le n-3\).** Only \(b=3,4\) remain to check. If \(b=3\), then \(|T|=n-3\), forcing \(T=S\) and \(S\setminus T=\varnothing\); the three paths can plainly be joined into a cycle. If \(b=4\), then \(|T|=n-4\) and at most one forbidden block edge remains; \(K_4\) minus at most one edge has a four-cycle. This proves shattering for every linear forest in the asserted range.

**5. Top-size sufficiency.** Suppose \(|S|=n-2\) and its two original path components either consist of one isolated vertex and a path with at least three edges, or are both paths with at least three edges. The case \(b\ge5\) is covered by step 3. If \(b=2\), then \(T=S\); join the two path components by two cross-edges, using both endpoints of each nontrivial path, or the same isolated vertex twice if one component is a singleton. If \(b=3\), exactly one original path edge was omitted; that original path splits into two blocks \(A,B\), and the other original component is block \(D\). Since the split path had at least three edges, at least one of \(A,B\) has two or more vertices. Connect their *far endpoints* (not the omitted cut-edge endpoints) and attach their other endpoints to \(D\), completing a triangle of blocks without the forbidden edge.

If \(b=4\), two edges were omitted. When they lie in different original components, the forbidden block graph is a matching of two edges, and its complement in \(K_4\) has a Hamiltonian four-cycle. Otherwise the two cuts split one original path in order into blocks \(A,B,C\), while the other original component stays intact as \(D\). At least one of \(A,B,C\) has two or more vertices because the original path has at least three edges. If \(A\) is nontrivial, order the blocks \(A,B,D,C\) cyclically and join \(A\) to \(B\) at the *far* endpoint of \(A\); if \(A\) is a singleton but \(B\) is nontrivial, use the same order and join \(A\) to the far endpoint of \(B\). The other three links in that order cannot be forbidden. If both \(A\) and \(B\) are singletons, \(C\) is nontrivial; use the cyclic order \(A,C,B,D\), attaching \(B\) to the far endpoint of \(C\). The resulting cycle avoids both cut edges. These cases exhaust all \(T\subseteq S\).

**6. Top-size necessity.** Because \(|S|=n-2\), exactly two path components exist. If one is isolated and the other has at most two edges, then \(n\le4\). At \(n=3\) the unique cycle contains every edge, so an edge cannot be omitted; at \(n=4\) the middle vertex of a two-edge path has only one allowed neighbor in \(K_4\setminus S\), so the empty trace is impossible. If both components have positive length but one has just one edge \(uv\), prescribe all other edges and forbid \(uv\): the two singleton endpoints and the other forced path form three blocks, so the endpoints must be joined, contradicting the forbidden edge. If a shortest component is a two-edge path \(u-v-w\), prescribe all edges of the other component and forbid \(uv,vw\): contraction yields four blocks \(u,v,w,D\), in which the singleton \(v\) has only \(D\) as a permissible neighbor, impossible in a Hamiltonian cycle. Hence the two stated top-size patterns are the only ones.

**7. Enumeration.** An undirected labeled path on \(j\ge2\) vertices has \(j!/2\) possible edge sets, while a singleton has one. The exponential formula for disjoint components gives the exponential generating function for all linear forests:
\[
\sum_{n\ge0}\frac{x^n}{n!}\sum_{S\text{ linear forest on }[n]}z^{|S|}
=\exp\!\left(x+\sum_{j\ge2}\frac{x^jz^{j-1}}2\right)
=\exp\!\left(x+\frac{x^2z}{2(1-xz)}\right).
\]
By step 4 its coefficients are the shattered-support counts through degree \(n-3\). At degree \(n-2\), a path on \(n-1\) vertices together with an isolated vertex contributes \(n!/2\). Each pair of unequal component vertex sizes \(4\le p<q\), \(p+q=n\), contributes \(n!/4\); the equal-size case, possible for even \(n\ge8\), contributes \(n!/8\). The number of unequal size pairs is \(\max\{0,\lfloor(n-1)/2\rfloor-3\}\). No higher term occurs by step 1. The displayed formulas and VC dimensions follow.

## Verification
The attached standalone Python 3 file `verify_hamiltonian.py` enumerates all undirected Hamiltonian cycles directly and tests every Boolean trace without using the proof's contraction lemma. It checks every edge support of sizes zero through \(n\) for \(3\le n\le7\), independently compares the complete count vectors with labeled linear-forest enumeration, and tests all path-component-length types for \(n=8,9\). The replay reports 209,087 nonempty fully tested supports and 50 further representatives. This verifies finite cases only; universality follows from the argument above.

## Relationship to prior work
Kranakis, Krizanc, Ruf, Urrutia, and Woeginger (1994), *VC-Dimensions for Graphs*, define edge-VC systems and prove results for all connected edge sets (their Section 7) while their cycle-VC dimension shatters **vertices** (Section 6). Their substantially larger connected-edge concept family does not determine which edge patterns can be traces of *spanning Hamiltonian cycles*. Schaefer's (2000) path-VC complexity result also concerns vertex shattering by arbitrary paths/cycles. Coudert, Csikós, Ducoffe, and Viennot's publicly posted May 13, 2024 paper gives algorithms and bounds for **closed-neighborhood** VC dimension of graphs, not Hamiltonian-cycle edge incidence. The present result is a coefficientwise and supportwise statement, not merely the existence of a largest shattered support. Relevant terminology includes edge-shattering, tour-incidence projections, linear forests, and traces of Hamiltonian cycles.

## Limitations
The theorem is for complete graphs and undirected *Hamiltonian* tours only; it does not extend as stated to general host graphs, nonspanning cycles, directed tours, or arbitrary connected edge sets. The available literature searches and inspected primary texts do not prove historical uniqueness; an equivalent classification under tour-polytope projection terminology might exist. No independent mathematical audit has been performed.

## References
- D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (first public version May 13, 2024), subsequently SEA 2024, DOI: 10.4230/LIPIcs.SEA.2024.8. https://arxiv.org/abs/2405.07588
- E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, and G. J. Woeginger, *VC-Dimensions for Graphs*, Carleton SCS-TR-255 (1994), Sections 6–7. https://carleton.ca/scs/wp-content/uploads/sites/260/TR255.pdf
- M. Schaefer, *Deciding the VC Dimension is Sigma-3-p-complete, II*, DePaul technical report (October 30, 2000). https://ovid.cs.depaul.edu/documents/TR00-006.pdf
- G. A. Dirac, *Some theorems on abstract graphs*, Proc. London Math. Soc. (1952), the minimum-degree Hamiltonicity theorem.
