# Square-zero multiplication operators in graph evolution algebras: a four-cycle boundary and an exact cycle-rank law

## Finding
For a finite simple loopless graph \(G=(V,E)\), take the (commutative but generally nonassociative) graphical evolution algebra over \(k=\mathbb F_q\), with natural basis \((e_v)\), products \(e_ve_w=0\) for \(v\ne w\), and \(e_v^2=\sum_{w\sim v}e_w\). For \(x=\sum_{v\in V}x_ve_v\), write \(L_x(y)=xy\). **Square-zero below means the ordinary composition \(L_x\circ L_x=0\), not the algebra element equation \(x^2=0\).** We count parameter vectors \(x\), not distinct matrices with multiplicity suppressed.

**Structural theorem.** Over every field, whenever \(G\) has no four-cycle (whether induced or not),
\[
L_x^2=0\quad\Longleftrightarrow\quad \operatorname{supp}(x)=\{v:x_v\ne0\}\text{ is independent in }G.
\]
Thus for any finite field and any such graph,
\[
\#\{x:L_x^2=0\}=I_G(q-1),\qquad I_G(t)=\sum_{S\subseteq V\text{ independent}}t^{|S|}.
\]
The condition cannot be dropped for all graphs: on the four-cycle \(C_4\) over \(\mathbb F_3\), the full-support vector \(x=e_0+e_1-e_2-e_3\) has \(L_x^2=0\).

**Complete rank law for cycles.** For \(n\ge5\), let \(G=C_n\), and write
\[
Q_{n,q}(z)=\sum_{x\in E_G(\mathbb F_q):L_x^2=0}z^{\operatorname{rank}_k(L_x)}.
\]
With \(w=q-1\), the exact closed polynomial is
\[
\boxed{Q_{n,q}(z)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}w^jz^j+\Delta_{n,q}(z),}
\]
where \(\Delta_{n,q}(z)=0\) for odd \(n\), and for even \(n\),
\[
\Delta_{n,q}(z)=\begin{cases}2w^{n/2}(z^{n/2-1}-z^{n/2}),&\operatorname{char}k=2\ \text{or}\ 4\mid n,\\0,&\text{otherwise}.\end{cases}
\]
Thus over \(\mathbb F_2\), \(Q_{6,2}(z)=1+6z+11z^2\); over \(\mathbb F_3\), \(Q_{6,3}(z)=1+12z+36z^2+16z^3\). In particular the square-zero operator count \(Q_{n,q}(1)=I_{C_n}(q-1)\) is independent of the field's characteristic when the field cardinality is held fixed, but the **rank distribution** can jump with the characteristic.

## Assumptions and scope
The graph is finite, undirected, simple, and loopless, possibly disconnected or with isolated vertices; a four-cycle means any subgraph isomorphic to \(C_4\), not only an induced cycle. The general support theorem holds over every field. The enumerators are for finite fields of any characteristic, including extension fields. Cycles have \(n\ge5\) vertices so the exceptional four-cycle is excluded from the closed formula. Rank is linear-operator rank over the base field. Algebraic products \(x^2\) and operator compositions \(L_x^2\) are distinct operations and are never conflated.

## Proof
**1. Multiplication matrix and the easy implication.** Let \(A\) be the ordinary \(0,1\) adjacency matrix of \(G\) over \(k\). By the defining products, \(L_x=A\operatorname{diag}(x)\). Its square has entries
\[
(L_x^2)_{ij}=x_j\sum_{h\in N(i)\cap N(j)}x_h.
\]
If \(S=\operatorname{supp}(x)\) is independent, every neighbor of a \(j\in S\) has coordinate zero, so each column of \(L_x^2\) vanishes. This holds for every graph.

**2. Converse for four-cycle-free graphs.** Suppose some edge \(\{u,v\}\) has \(x_ux_v\ne0\). If either endpoint, say \(v\), has a second neighbor \(w\ne u\), then \(w\) and \(u\) have exactly one common neighbor: \(v\). Indeed another distinct common neighbor would make the four-cycle \(u-v-w-h-u\). Hence \((L_x^2)_{wu}=x_ux_v\ne0\). If both \(u\) and \(v\) have degree one, \(N(u)=\{v\}\) and \((L_x^2)_{uu}=x_ux_v\ne0\). Consequently \(L_x^2=0\) forces independent support. Each independent support \(S\) admits exactly \((q-1)^{|S|}\) vectors over \(\mathbb F_q\), proving the graph formula.

**3. Failure at a four-cycle.** Number the vertices cyclically \(0,1,2,3\), and take \(x=(1,1,-1,-1)\) over \(\mathbb F_3\). For each vertex the sum of the two neighboring \(x\)-coordinates is zero, and the two length-two walks from one vertex to the opposite vertex have canceling middle coordinates. Directly \(L_x^2=0\) although every coordinate is nonzero and adjacent pairs occur. No necessity of the four-cycle-free condition for individual graphs is claimed.

**4. All possible column dependencies on a cycle.** For \(n\ge5\), the equation \(Av=0\) is the cyclic recurrence \(v_{i+2}=-v_i\). For odd \(n\) it gives only the zero vector unless \(\operatorname{char}k=2\), when the kernel consists of constant vectors; the unique nonzero dependency has full support. For even \(n\), the two vertex parity classes each follow a chain of length \(n/2\) with successive sign changes. A nonzero solution on either parity class exists precisely when \(\operatorname{char}k=2\) or \(n/2\) is even. In that case \(\ker A\) is the direct sum of the one-dimensional lines supported on the two parity classes, each with every coordinate on its class nonzero. Otherwise \(A\) is nonsingular. Because \(L_x\) rescales exactly the columns indexed by \(S=\operatorname{supp}(x)\), its rank is \(\operatorname{rank}A_{[:,S]}\), independent of the particular nonzero coefficients.

**5. Rank correction for independent supports.** When \(n\) is odd, an independent set is proper and cannot support a nonzero vector of \(\ker A\); hence \(\operatorname{rank}L_x=|S|\). When \(n\) is even, a nonzero dependency can have support inside an independent set only if the set contains an entire parity class. The only such independent sets are the two alternating sets of cardinality \(n/2\). In the resonance cases of Step 4, each loses precisely one rank; otherwise all independent supports have full column rank.

**6. Count cycle independent sets.** For \(0\le j\le\lfloor n/2\rfloor\), the number of independent vertex subsets of size \(j\) in the labeled cycle is \(\frac{n}{n-j}\binom{n-j}{j}\). For \(j=0\) this is one. For \(j\ge1\), mark the \(j\) chosen vertices and the positive lengths of the intervening zero-gaps around the cycle; the usual cyclic gap count gives \(\frac nj\binom{n-j-1}{j-1}\), equal to the displayed coefficient. Multiply each support by \(w^j\), then move the two alternating support contributions from exponent \(n/2\) to \(n/2-1\) exactly in the resonance cases. This gives the boxed rank polynomial for all allowed \(n,q\).

## Verification
The included dependency-free script `check_square_zero.py` constructs all multiplication matrices and squares for the cycle graphs \(C_n\), \(5\le n\le9\), over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) in 13 complete finite-field cases, computing all rank strata by modular elimination rather than by the support formula. It separately exhausts every simple four-cycle-free graph on up to five vertices in the indicated small fields: 613 distinct labeled graphs and 22,147 coefficient vectors; the square-zero/independent-support equivalence holds throughout. An explicit four-cycle counterexample is checked. The output is in `verification_output.txt`. These finite tests corroborate but do not prove the general field and graph statements; extensions beyond prime fields are covered by the field-independent proof, not computational testing.

## Relationship to prior work
Elduque and Labra (2013) establish the natural-basis graph correspondence for evolution algebras and analyze algebra nilpotency, connectedness and automorphisms, but not the square-zero **left-multiplication-operator** support locus or its rank-refined cycle census. Brijder, Hoogeboom and Traldi (2011/2012) study adjacency column matroids over \(\mathbb F_2\) and their Tutte polynomials; that theory supplies a classical language for the column-dependency portion, but does not identify the operator square-zero condition in evolution algebras or the all-characteristic support theorem. The published graph-face-algebra multiplication-rank formula concerns associative squarefree Artinian quotients with a distinct multiplication law; it does not imply \(L_x^2=0\) in the present nonassociative graphical evolution algebra. The published square-zero geometry of complete multipartite evolution algebras concerns **elements** \(x^2=0\), not operators \(L_x^2=0\), and likewise does not cover the claimed equations. The basic independent-set polynomial and cyclic gap numbers are standard; the new contribution claimed here is their exact realization as the operator square-zero locus for a structural graph class, combined with the all-rank characteristic-sensitive cycle law. These comparisons establish novelty under inspected sources, not comprehensive priority certification.

## Limitations
The characterization may hold for additional graphs containing four-cycles, but no complete converse classification of such graphs is claimed. Only square-zero **individual multiplication operators** are counted, not all nilpotent operators of higher index, nor the algebra element square-zero variety, nor multiplication-operator similarity types. For arbitrary four-cycle-free graphs the unrefined count is an independence-polynomial evaluation; the explicit rank-refined formula is proved only for cycles. Some classical adjacency-matroid results may yield parts of the rank correction by specialization; earlier equivalent operator-nilpotence statements remain possible. No independent mathematical audit is asserted.

## References
- A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685, first posted 2013-12-17, especially Sections 2–4. https://arxiv.org/abs/1312.4685
- R. Brijder, H. J. Hoogeboom and L. Traldi, *The adjacency matroid of a graph*, arXiv:1107.5493, first posted 2011-07-27, especially Definition 4 and the Tutte-polynomial discussion. https://arxiv.org/abs/1107.5493
- *Finite-field multiplication-rank spectra of graph face algebras*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-finite-field-multiplication-rank-spectra-of-graph-face-algebras--d37be33201da
- *Finite-field square-zero geometry of complete multipartite evolution algebras*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-field-square-zero-geometry-of-complete-multipartite-evolu--555bc289f00b
