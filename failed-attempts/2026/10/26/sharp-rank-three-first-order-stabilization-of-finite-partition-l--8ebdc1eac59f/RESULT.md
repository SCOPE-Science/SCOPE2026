# Sharp rank-three first-order stabilization of finite partition lattices

## Finding

For every integer \(n\ge 1\), let \(\Pi_n\) denote the lattice of all partitions of an \(n\)-element set, ordered by refinement. Regard it as a structure in the first-order language \(\{\le,=\}\), without naming the bottom, top, atoms, blocks, or lattice operations. For all positive integers \(n,m\),
\[
\Pi_n\equiv_3\Pi_m\quad\Longleftrightarrow\quad
\min(n,7)=\min(m,7).
\]
Thus the family has exactly seven theories at quantifier rank at most three, and its optimal largest representative has \(B_7=877\) elements, where \(B_7\) is the seventh Bell number. In particular, \(\Pi_7\equiv_3\Pi_n\) for every \(n\ge7\), while consecutive members up to that threshold are distinguishable by explicit rank-three sentences.

## Assumptions and scope

All structures are finite, and a partition \(P\) refines \(Q\), written \(P\le Q\), exactly when every block of \(P\) is contained in a block of \(Q\). Its rank is \(h(P)=n-b(P)\), where \(b(P)\) is the number of blocks; its corank is \(c(P)=b(P)-1\). The unique minimum is the discrete partition and the unique maximum is the indiscrete partition. We use ordinary first-order logic with equality and the one binary order predicate, with quantifier rank (maximum nesting depth) at most three, not counting logic, counting colour refinement, or an enriched lattice signature. The equivalence symbol \(\equiv_3\) means agreement on all sentences of that rank.

## Proof

**1. Exact two-point extension lemma.** For two partitions \(P,Q\), put \(\rho(R,P)\in\{E,L,G,I\}\) for the atomic comparison of \(R\) with \(P\): equal, strictly below, strictly above, or incomparable. Let \(\mathcal E(P,Q)\) be the set of all pairs \((\rho(R,P),\rho(R,Q))\) realized by partitions \(R\) of the same underlying set. The following list is exact. Here \(h_P=h(P)\), \(c_P=c(P)\), and similarly for \(Q\).

* If \(P=Q\): \((E,E)\) is present; \((L,L)\) iff \(h_P>0\); \((G,G)\) iff \(c_P>0\); \((I,I)\) iff \(h_Pc_P>0\).
* If \(P<Q\): \((E,L),(G,E)\) are present. Both \((L,L),(I,L)\) occur iff \(h_P>0\). Both \((G,G),(G,I)\) occur iff \(c_Q>0\). The pattern \((G,L)\) occurs iff \(h_Q-h_P\ge2\). Finally \((I,I)\) occurs iff \(h_P>0\) and \(c_Q>0\). The case \(P>Q\) is obtained by interchanging the coordinates.
* If \(P\parallel Q\): \((E,I),(I,E),(L,L),(G,G),(I,I)\) always occur. The additional patterns \((L,I),(I,L),(G,I),(I,G)\) occur, respectively, iff \(h_P\ge2,h_Q\ge2,c_P\ge2,c_Q\ge2\).

To justify completeness, the position of \(R\) relative to either chosen partition forces each listed rank/corank condition; an element strictly between two comparable partitions exists precisely when their ranks differ by at least two. The converse witnesses use the atomistic and coatomistic descriptions of the partition lattice. Every atom merges one ground-set pair, and every coatom has exactly two blocks. If \(P\not\le Q\), some pair of points merged by \(P\) is separated by \(Q\): its atom is below \(P\) but not below \(Q\). Dually, if \(P\not\ge Q\), a two-block coarsening of \(P\) separates a pair merged by \(Q\). For incomparable \(P,Q\), some pair is separated by both: otherwise two different blocks of \(P\) would be universally joined in \(Q\), forcing \(Q\) to be the maximum; its atom witnesses \((I,I)\). For \(P<Q\), \(P>\bot\), \(Q<\top\), an atom merging a pair separated by \(Q\) witnesses \((I,I)\). All remaining cases follow by the same atom/coatom witnesses, by the extremal elements, or by choosing a saturated chain. This proves the table for every \(n\ge1\).

**2. The pointed rank-two invariant.** Atomic two-variable types record only \(\rho(P,Q)\). A rank-one two-variable type is exactly the atomic type of \((P,Q)\), augmented by its attainable third-vertex comparisons \(\mathcal E(P,Q)\); all first-order formulas with two free variables and at most one additional nested quantifier are Boolean combinations of these data. Hence the rank-two pointed type of \(P\) is exactly the set
\[
\mathcal T(P)=\{\big(\rho(P,Q),\mathcal E(P,Q)\big):Q\in\Pi_n\}.
\]

For \(n\ge5\), this set depends only on
\[
\alpha(P)=\bigl(\min\{b(P),4\},\min\{h(P),3\}\bigr),
\]
and different values of \(\alpha\) yield different \(\mathcal T\). Here is a parameter-by-parameter derivation. For \(Q>P\), the extension table only tests whether \(Q=\top\), whether \(Q\) covers \(P\), and whether it is separated from both by at least two rank steps; all these possibilities depend only on \(b(P)=1,2,3,\text{or}\ \ge4\). Indeed \([P,\top]\) is canonically the partition lattice on the \(b(P)\) blocks. For \(Q<P\), the same table tests \(Q=\bot\), the cover relation, and whether the rank gap exceeds one, depending only on \(h(P)=0,1,2,\text{or}\ \ge3\). These two collections recover both truncated coordinates: the presence of an upper element, an upper element at distance at least two, and a nontop upper element at distance at least two distinguish the four possible truncated block counts; the corresponding lower properties distinguish the four truncated heights.

For \(P\parallel Q\), the table depends on \(Q\) only through the categories \(h(Q)=1\) versus \(h(Q)\ge2\) and \(c(Q)=1\) versus \(c(Q)\ge2\). Every interior \(P\), when \(n\ge5\), has incomparable witnesses \(Q\) in each of the three feasible categories: an atom, a coatom, and a rank-two partition of corank at least two. For an atom \(P\), choose the rank-two partition by merging three other points; for a partition of rank two, choose a different rank-two partition; for greater rank, merge three points including two separated by \(P\). The atom and coatom witnesses follow from the preceding paragraph; if \(P\) is already an atom or coatom, take a distinct one. There are no incomparable elements when \(P\) is extremal. Consequently the incomparable part of \(\mathcal T(P)\) introduces no further dependence on block sizes. Conversely, the upper and lower parameter tests just listed recover \(\alpha(P)\) from \(\mathcal T(P)\), proving the assertion.

**3. Rank-three stabilization.** A rank-three sentence is determined by the set of all realized pointed rank-two types. Therefore the rank-three sentence type of \(\Pi_n\), for \(n\ge5\), is determined precisely by
\[
A_n=\{(\min\{b,4\},\min\{n-b,3\}):1\le b\le n\}.
\]
For every \(n\ge7\), this is the fixed seven-element set
\[
\{(1,3),(2,3),(3,3),(4,3),(4,2),(4,1),(4,0)\}.
\]
Thus all lattices \(\Pi_n\) with \(n\ge7\) are rank-three equivalent. This is an infinite argument, independent of the finite tests below.

**4. Sharpness and all smaller classes.** Use the quantifier-free relation \(x<y\) abbreviating \(x\le y\land x\ne y\). Define \(D_j(x)\), for \(j=0,1,2,3\), to assert a chain of \(j\) strict steps below \(x\). Take \(D_0(x)\) as truth, \(D_1(x)=\exists y(y<x)\), \(D_2(x)=\exists y\exists z(z<y<x)\), and
\[
D_3(x)=\exists y\bigl(y<x\ \land\ (\exists z\ z<y)\ \land\ (\exists w\ y<w<x)\bigr).
\]
The formulas \(U_j(x)\) are their order duals, counting strict steps above. Despite encoding a three-step chain, \(D_3\) and \(U_3\) have quantifier rank two: the two inner witnesses sit in different branches. For each \(t=1,\ldots,6\), put \(i=\max(0,t-3)\), \(j=t-i\), and
\[
\Phi_t=\exists x\bigl(D_i(x)\land U_j(x)\bigr).
\]
This sentence has rank at most three, and holds in \(\Pi_n\) precisely when the lattice height \(n-1\) is at least \(t\). Hence \(\Phi_t\) separates \(\Pi_t\) from \(\Pi_{t+1}\) and, more generally, separates every two distinct indices below seven. The first seven theories are therefore pairwise distinct, and the class at index seven cannot have a representative at a smaller index.

Since \(|\Pi_n|=B_n\) is strictly increasing for \(n\ge1\), the smallest representative of the stabilized class is \(\Pi_7\), of size \(B_7=877\). This is the optimal maximum representative size within the stated family.

## Verification

Run `python3 verify_partition_lattices.py` with a standard Python 3 interpreter. The supplied `verification_output.txt` records the replay. The verifier constructs canonical restricted-growth words, exactly reconstructs the refinement order, and compares every two-point extension table against the explicit structural lemma for all partitions of \(n\le7\). For \(n=8\), it checks 50,000 reproducibly selected ordered pairs. It separately reconstructs every pointed logical type up to dimension eight (for each automorphism orbit representative), confirms the rank-three class sequence, and checks the abstract saturated parameter set through \(n=300\). In the first seven dimensions the complete pair-table test includes 769,129 ordered pairs at \(n=7\). All recorded checks returned `VERIFY_OK`.

These finite computations cross-check the exact table and small boundary. The unrestricted theorem requires the structural proof above; neither sampling nor testing \(n\le300\) is treated as a proof for all integers.

## Relationship to prior work

Jenča and Sarkoci, *Linear extensions and order-preserving poset partitions*, arXiv:1112.5782 (first publicly posted 2011-12-25), consider the lattice of order-preserving partitions, including the ordinary set-partition lattice as the antichain specialization; their conclusions are topological, concerning order complexes and linear extensions. Idziak (1987) recalls known hereditary undecidability phenomena for the full first-order theory of the class of finite partition lattices. Those statements neither identify the bounded quantifier-rank-three equivalence classes nor imply the sharp seven-point stabilization: undecidability at unbounded logical depth is compatible with a finite classification at fixed depth.

Burris and Sankappanavar's 1975 paper on lattice-theoretic decision problems is historically pertinent, but its full text was not accessible for comprehensive comparison. Existing results on counting colour refinement of the partition lattice recover individual partition block profiles; that is a different, counting-based invariant *within* a single lattice and does not give equivalence of different lattices under pure first-order logic with three nested quantifiers. The claimed result here is the sharp classification across the whole sequence \(\Pi_n\).

## Limitations

The language is exactly \(\{\le,=\}\), and the bound is restricted to quantifier rank three. Stronger signatures, formulas with more nested quantifiers, and counting extensions are not classified here. The 877-element minimum is relative to representatives within the partition-lattice family, not among all finite posets. Computational checks are finite supplements, not infinite certificates. An inaccessible relevant historical paper and potentially unindexed older results leave residual literature-overlap risk. Independent external scientific validation has not been performed.

## References

1. G. Jenča and P. Sarkoci, *Linear extensions and order-preserving poset partitions*, arXiv:1112.5782v1, first submitted 2011-12-25. https://arxiv.org/abs/1112.5782
2. P. M. Idziak, *Undecidability of Free Pseudo-Complemented Semilattices*, Publ. Res. Inst. Math. Sci. **23** (1987), 559–564, DOI 10.2977/PRIMS/1195176449. https://ems.press/journals/prims/articles/3357
3. S. Burris and H. P. Sankappanavar, *Lattice-theoretic decision problems in universal algebra*, 1975, DOI 10.1007/BF02485250. https://doi.org/10.1007/BF02485250
