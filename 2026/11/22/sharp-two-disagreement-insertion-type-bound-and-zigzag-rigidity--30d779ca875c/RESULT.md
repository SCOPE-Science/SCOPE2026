# Sharp two-disagreement insertion-type bound and zigzag rigidity in the homogeneous two-order structure

## Finding

For any \(n\ge2\), fix \(n\) *individually named* distinct parameters in the countable homogeneous structure \(\Pi\) carrying two independent linear orders. Name them \(1,\ldots,n\) in the first order, and write their sequence in the second order as \(\pi=(\pi_1,\ldots,\pi_n)\). There are exactly \((n+1)^2\) complete nonalgebraic one-point types, indexed by two insertion gaps. Let \(c_2(\pi)\) count those types for which the two placements disagree on exactly two of the named parameters. Then

\[
\boxed{c_2(\pi)\le3(n-1).}
\]

The bound is attained for every size, and the equality cases are complete:

- At \(n=2\), exactly \(\pi=21\).
- At \(n=3\), exactly \(\pi=231,312,321\).
- At every \(n\ge4\), exactly two patterns, mutually inverse. They come from the two orientations of the unique Hamilton cycle in the square of the path on \(1,\ldots,n\), with allowed edges \(\{a,b\}\) satisfying \(1\le |a-b|\le2\). A canonical cyclic vertex list is: start at \(1\), traverse the even vertices increasingly, then the odd vertices greater than \(1\) decreasingly, and return to \(1\). Orient this cycle in either direction to obtain the two permutations.

At four named points these are \(2413\) and \(3142\), patterns already appearing in a distinct adjacency characterization in Cameron's 2002 paper. For instance, at five points the two patterns are \(24153\) and \(31524\), and the sharp count is \(12\).

## Assumptions and scope

An *insertion type* here is a complete one-point type of a new point distinct from all named parameters in the language with the two order relations. As the structure is ultrahomogeneous and all combinations of insertion gaps occur, an insertion pair completely determines a type. A placement at first-order gap \(i\) means the new point is above exactly the first \(i\) parameters in the first order. Define the prefix sets

\[
P_i=\{1,\ldots,i\},\qquad Q_j=\{\pi_1,\ldots,\pi_j\},\qquad 0\le i,j\le n.
\]

The discrepancy of the insertion type \((i,j)\) is exactly \(|P_i\triangle Q_j|\); it counts parameters lying before the new point in exactly one of the two orders. The theorem counts discrepancy exactly two, without assuming any particular orientation or pattern of the named parameter permutation.

## Proof

**Step 1: Exhaust all potentially contributing gap pairs.** If \(|P_i\triangle Q_j|=2\), then \(|i-j|\le2\) and \(i-j\) is even because \(|P_i|+|Q_j|-|P_i\triangle Q_j|\) is even. Therefore the only candidates are \((i,i)\) for \(1\le i\le n-1\), and \((i,i+2)\), \((i+2,i)\) for \(0\le i\le n-2\). There are exactly \(3(n-1)\) such pairs. Endpoints \((0,0)\) and \((n,n)\) have discrepancy zero. Thus \(c_2(\pi)\le3(n-1)\), and equality means every candidate pair contributes.

**Step 2: Convert equality to a permutation condition.** At diagonal \((i,i)\), the discrepancy equals twice the number of edges of the permutation map \(t\mapsto\pi_t\) directed across the cut \(\{1,\ldots,i\}\) from the left to the right. Thus all \(n-1\) diagonal pairs contribute exactly when every nontrivial cut has precisely one crossing in each direction. The two off-diagonal families contribute exactly when \(P_i\subseteq Q_{i+2}\) and \(Q_i\subseteq P_{i+2}\), respectively. These inclusions for all indices are equivalent, first, to \(\pi_t\le t+2\) for every \(t\), and second, to \(\pi^{-1}(v)\le v+2\) for every \(v\). Substituting \(v=\pi_t\) into the second inequality gives \(t\le\pi_t+2\). Hence all off-diagonal pairs contribute if and only if

\[
|\pi_t-t|\le2\quad\text{for every }1\le t\le n.
\]

**Step 3: The crossing condition forces one Hamiltonian permutation cycle.** Decompose \(t\mapsto\pi_t\) into disjoint directed cycles. Each nontrivial cycle crosses every cut between its least and greatest vertices in at least one direction. No two such cycle intervals can overlap in a cut, because that would give at least two outgoing crossings there. They also cannot occupy disjoint proper intervals with all cuts covered: disjoint vertex supports leave a cut between their intervals uncovered. Since every cut is crossed exactly once outwards, there is a unique nontrivial cycle containing both the least and greatest vertices, \(1\) and \(n\); all other vertices, if any, are fixed.

Suppose \(n\ge4\) and an internal vertex \(j\), with \(1<j<n\), were fixed. The spanning cycle contains vertices on each side of \(j\), so it crosses the bipartition from \(\{1,\ldots,j-1\}\) to \(\{j+1,\ldots,n\}\) both ways. Under the displacement-two condition, the only possible crossing is between \(j-1\) and \(j+1\). Both directions would force these two vertices to form a separate two-cycle, contradicting that the spanning cycle has at least three vertices. Thus no vertex is fixed and the permutation is an \(n\)-cycle using only jumps of length one or two. Conversely, any such Hamiltonian directed cycle has exactly one crossing per cut if it is the unique Hamilton cycle described in Step 4.

**Step 4: The path square has exactly one undirected Hamilton cycle for \(n\ge3\).** Let \(H_n\) be the graph on \(\{1,\ldots,n\}\) with edges between distinct vertices whose difference is at most two. In any Hamilton cycle \(C\) of \(H_n\), vertex \(1\) has exactly two neighbors, \(2\) and \(3\), so both \(1-2\) and \(1-3\) must occur. For \(n\ge4\), deleting \(1\) and joining \(2\) to \(3\) yields a Hamilton cycle of \(H_{n-1}\) on \(2,\ldots,n\). In reverse, every Hamilton cycle of \(H_{n-1}\) must contain the edge \(2-3\), because vertex \(2\) in that graph has precisely two neighbors, \(3\) and \(4\). Replacing \(2-3\) by \(2-1-3\) recovers the unique preimage. Thus deletion and insertion give a bijection of Hamilton cycles for successive sizes. The base \(H_3\) is a triangle, with one Hamilton cycle. Induction proves uniqueness for every \(n\ge3\), and the even-then-odd zigzag is plainly that cycle. Its two orientations correspond to inverse permutations. Each oriented Hamilton cycle crosses each proper initial segment of the path in exactly one edge in each direction (as follows from the recursive cycle construction, or directly from the zigzag list), so it satisfies Step 2 and attains all \(3(n-1)\) candidate insertion pairs.

**Step 5: Small cases.** At \(n=2\), the two patterns are \(12\) and \(21\), and only \(21\) has three discrepancy-two insertion types. At \(n=3\), direct evaluation of the six insertion matrices yields precisely \(231\), \(312\), and \(321\), each with six discrepancy-two types. The two directed three-cycles are supplemented by reversal \(321\), which has a fixed middle vertex. This exhausts all exceptions.

## Verification

The self-contained standard-library program `verify.py` enumerates all \(409112\) permutations of lengths two through nine and checks the bound and exact equality lists. It independently computes disagreement by direct parameterwise order comparisons through size six and enumerates all directed Hamiltonian cycles of \(H_n\) through size ten. Its full deterministic stdout appears in `verification_output.txt`; rerun with `python verify.py`. Finite enumeration is diagnostic only: Steps 1–5 prove the theorem for all \(n\).

## Relationship to prior work

Cameron's *Homogeneous Permutations* (2002) introduces the double-order viewpoint, the unrestricted homogeneous two-order limit, and identifies the two size-four permutations \(2413\) and \(3142\) in a different theorem: they are the only four-point patterns in which each pair is adjacent in at least one order (see p. 5). Their occurrence at the four-point endpoint is explicitly **not** claimed as new. The present statement concerns a count of complete insertion types of discrepancy two, determines its maximum for every \(n\), and gives an all-size rigidity classification of its maximizers. The existing four-point property is not an all-size implication of the present bound.

Linman–Pinsker's *Permutations on the Random Permutation* (2015) establishes the reduct classification and supplies the homogeneous and finite-type context, but the inspected introductory, structural, and type sections do not state this extremal count. Cameron's oligomorphic-group enumeration framework (2000) likewise concerns general orbit profiles rather than this discrepancy filtration. Searches of mathematical records and relevant literature did not locate an equivalent all-size result. An equivalent theorem under other permutation terminology may exist; this is a literature search, not proof of historical priority.

## Limitations

The result treats complete one-point types of new elements, with fixed individually named parameters and **exactly** two order-disagreement positions. It does not reconstruct the entire base pattern from the statistic, count higher-arity types, or treat a uniformly random point as a uniform sample from type space. The proofs are mathematical arguments; finite tests do not establish infinite validity on their own. An independent audit and definitive priority determination have not been performed.

## References

1. P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2) (2002), R2, first published 2002-10-31. https://doi.org/10.37236/1674 ; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf/
2. J. Linman and M. Pinsker, *Permutations on the Random Permutation*, Electronic Journal of Combinatorics 22(2) (2015), P2.54, first published 2015-06-22. https://arxiv.org/abs/1405.4297 ; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p54/pdf/
3. P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*, Journal of Integer Sequences 3 (2000), Article 00.1.5. https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html
