# Uniform trace law for cyclic permutations and sharp online arc shattering

## Finding
For each integer \(n\ge3\), let \(D_n=\{(u,v):u,v\in[n],\ u\ne v\}\), the directed arcs of the loopless complete symmetric digraph. Let \(\mathcal C_n\) be the incidence-function concept class of all directed Hamiltonian cycles on \([n]\), equivalently all permutations consisting of one cycle. Thus a hypothesis assigns label one to precisely the arcs \((u,\sigma(u))\), where \(\sigma\) is an \(n\)-cycle.

**Complete support criterion.** A set of distinct queries \(S\subseteq D_n\) is shattered by \(\mathcal C_n\) if and only if \(S\) is a vertex-disjoint union of consistently directed paths (isolated vertices allowed) with at most \(n-2\) arcs. In particular, a directed cycle, a vertex with two incoming arcs, or a vertex with two outgoing arcs cannot occur in a nonempty shattered support.

**Uniform trace law.** Suppose \(S\) is such a path forest, \(k=|S|\le n-2\), and a labeling is positive on exactly \(f\) of its arcs, with \(0\le f\le k\). The number of directed Hamiltonian cycles realizing this *exact* labeling equals
\[
T(n,k,f)=\sum_{j=0}^{k-f}(-1)^j\binom{k-f}{j}(n-f-j-1)!.
\]
It depends only on \(n,k,f\), not on the path lengths, positions, or the particular positive arcs. Moreover \(T(n,k,f)>0\) throughout the stated domain.

The full shattered-support generating polynomial therefore is
\[
\Phi_n(z)=\sum_{k=0}^{n-2}\frac{n!}{(n-k)!}\binom{n-1}{k}z^k.
\]
In the usual membership-query model, static and online dimensions coincide:
\[
\operatorname{VCdim}(\mathcal C_n)=\operatorname{Ldim}(\mathcal C_n)=n-2.
\]

## Assumptions and scope
All vertex sets are labeled, all directed arcs have distinct endpoints, and a directed Hamiltonian cycle is a cyclic ordering modulo rotation but **not** modulo reversal. Its incidence concept contains exactly \(n\) positive arcs. The class has \((n-1)!\) distinct hypotheses. A support is shattered when every map \(S\to\{0,1\}\) occurs as the restriction of some concept. Littlestone dimension is the greatest depth of a complete binary tree whose internal nodes are arc queries and whose root-to-leaf labels are simultaneously realizable. Repeating a query along one root-to-leaf path cannot generate two viable children at the repeated occurrence.

The statement concerns \(n\ge3\) only; the empty support contributes constant coefficient one. A directed path component may have one vertex and no arcs. Edges of opposite direction between the same two vertices form a directed 2-cycle and are never simultaneously positive in an \(n\)-cycle for \(n\ge3\).

## Proof
**1. Supports containing an all-positive witness.** If \(S\) is shattered, its all-one labeling is realized by some directed Hamiltonian cycle \(H\). Thus \(S\subseteq H\). Every proper subset of the arc set of \(H\) is a vertex-disjoint union of directed paths, and its number of path components, including isolated vertices, is \(n-|S|\). A full \(n\)-cycle cannot be shattered because removing one of its arcs as a required negative while keeping the other \(n-1\) positive arcs is impossible. If \(|S|=n-1\), take \(F=S\setminus\{e\}\): the \(n-2\) positive arcs of \(F\) contract into two directed path blocks. The only directed Hamiltonian cycle on those two blocks uses the missing arc \(e\), contradicting the desired negative label. Hence \(|S|\le n-2\).

**2. Construct every labeling on a path forest.** Conversely, let \(S\subseteq H\) have \(k\le n-2\) arcs, where \(H\) is some fixed directed Hamiltonian cycle. An arbitrary labeling specifies a set \(F\subseteq S\) of positive arcs, with \(f=|F|\). Contract every directed path of \(F\) to a block, preserving its internal order. There are \(m=n-f\) blocks. Each forbidden arc in \(S\setminus F\) goes from one block to the next in the cyclic ordering induced by \(H\). If there is at least one forbidden arc, then \(f\le k-1\le n-3\), hence \(m\ge3\). Arrange the \(m\) blocks in the **reverse cyclic order** to that of \(H\), preserving the internal order within each block. This is a directed Hamiltonian cycle that contains all of \(F\) and none of the arcs in \(S\setminus F\), because for \(m\ge3\) no forward interblock arc of the original quotient cycle is an arc of the reverse quotient cycle. If no arc is forbidden, the original cycle \(H\) is a witness. Every labeling is therefore realizable.

**3. Count every exact trace.** Fix a positive set \(F\subseteq S\), \(f=|F|\). For any subset \(J\subseteq S\setminus F\) of size \(j\), the \(f+j\) arcs of \(F\cup J\) are a path forest and contract into \(n-f-j\ge2\) blocks. Directed Hamiltonian cycles extending these positive arcs are cyclic arrangements of the blocks, numbering \((n-f-j-1)!\). Inclusion-exclusion over the forbidden arcs gives \(T(n,k,f)\), and Step 2 ensures strict positivity. No term of the formula refers to the layout of \(S\).

**4. Count the shattered supports.** For \(k\le n-2\), a path forest with \(k\) arcs has \(r=n-k\) nonempty directed path components. Represent its components as \(r\) nonempty strings of distinct labeled vertices. First order all \(n\) labels, then choose the \(r-1\) cuts among the \(n-1\) inter-label positions, then discard the order of the \(r\) path components. Each forest occurs precisely \(r!\) times. The coefficient is
\[
\frac{n!}{r!}\binom{n-1}{r-1}=\frac{n!}{(n-k)!}\binom{n-1}{k}.
\]
Steps 1 and 2 say exactly these forests, and no others, are shattered.

**5. Determine online dimension.** Step 2 gives a shattered set of size \(n-2\), so \(\operatorname{Ldim}(\mathcal C_n)\ge\operatorname{VCdim}(\mathcal C_n)=n-2\). Suppose a complete depth-\((n-1)\) mistake tree existed. Along its all-positive path, the first \(n-2\) queries must be distinct (otherwise the 0-child of a repeated query would be inconsistent), and their all-positive assignment must be realized. By Step 1 they form a directed path forest with \(n-2\) arcs. There is exactly \((n-(n-2)-1)!=1\) Hamiltonian cycle extending them. Thus the next query cannot have both positive and negative realizable children, contradiction. Hence the online dimension is at most \(n-2\), proving equality.

## Verification
The standalone Python 3 standard-library checker `check_cyclic_permutations.py` enumerates all directed Hamiltonian cycles for each \(3\le n\le6\), enumerates every support contained in one of those cycles (which exhausts all potentially shattered supports), and computes the exact trace multiplicity for every labeling. It checks the iff criterion, all coefficients of \(\Phi_n\), and the inclusion-exclusion formula. Run `python3 check_cyclic_permutations.py` from the directory containing the file. A successful run prints `CYCLIC_PERMUTATION_ARC_TRACE_PASS`. The checked polynomial coefficient lists, including the zero coefficients at \(k=n-1,n\), are:

- \(n=3\): \((1,6,0,0)\).
- \(n=4\): \((1,12,36,0,0)\).
- \(n=5\): \((1,20,120,240,0,0)\).
- \(n=6\): \((1,30,300,1200,1800,0,0)\).

These finite checks are corroboration only. The unrestricted result follows from the five mathematical steps above.

## Relationship to prior work
Albert, Bouvel and Féray's 2018 preprint (published in 2020) compares permutations viewed as bijections and as ordered words and studies their logical expressibility; it does not give arc-query shattering profiles of the single-cycle class. Guingona, Kolesnikov, Nierwinski and Soucy's 2021 paper derives equal VC/Littlestone dimensions for families of zero sets of linear combinations, not cyclic-permutation incidence. Adler, Benediktsson and Macpherson's 2020 work studies neighborhood shattering on Johnson and Hamming graphs, not directed-cycle arc traces. The present structural result belongs to the permutation-as-bijection viewpoint but uses an incidence learning problem absent from those sources.

The undirected Hamiltonian-tour incidence problem is not interchangeable: forgetting orientation identifies reversal pairs and changes exact trace multiplicities. The directed all-support classification is uniform across path-component sizes, while the undirected endpoint cases are more restrictive; neither distinction follows from the undirected support criterion alone. Standard labeled-path-forest counting by permutation cuts supplies the coefficient count once the directed shattering criterion has been proved, but does not establish the criterion or the online bound.

## Limitations
No claim is made for Hamiltonian cycles of noncomplete digraphs, mixed cycle types, weighted queries, or graph-isomorphism-unlabeled concepts. The formula does not assert that all path forests with \(n-1\) arcs are shattered; they are explicitly excluded. Full historical priority across every possible alternative terminology has not been established, and no independent mathematical audit has been performed.

## References
1. M. Albert, M. Bouvel and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459 (first public version 2018-08-16), J. Combin. Theory Ser. A 171 (2020), 105158. https://arxiv.org/abs/1808.05459
2. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (2021). https://arxiv.org/abs/2109.04805
3. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (2020). https://arxiv.org/abs/2007.16042
4. S. Cambie, A. Girão and R. J. Kang, *VC Dimension and a Union Theorem for Set Systems*, Electron. J. Combin. 26(3) (2019), P3.24. https://doi.org/10.37236/8288
