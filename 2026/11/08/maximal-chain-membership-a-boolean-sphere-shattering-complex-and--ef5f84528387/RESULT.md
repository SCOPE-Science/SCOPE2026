# Maximal-chain membership: a Boolean-sphere shattering complex and online dimension \(n-1\)

## Finding

Fix an integer \(n\ge1\). A maximal chain of the Boolean lattice \(2^{[n]}\) is regarded as a binary concept on the set of nonempty proper subsets: a query asks whether its subset lies on the chain. A set of queries is **shattered if and only if its subsets are pairwise comparable by inclusion**. Thus the full family of shattered supports, not just its largest cardinality, is determined.

For \(0\le k\le n-1\), exactly \((k+1)!\,\left\{\begin{smallmatrix}n\\k+1\end{smallmatrix}\right\}\) supports of size \(k\) are shattered, where braces denote Stirling numbers of the second kind. Consequently

\[\Phi_n(z)=\sum_{k=0}^{n-1}(k+1)!\,\left\{\begin{smallmatrix}n\\k+1\end{smallmatrix}\right\}z^k,\qquad \operatorname{VCdim}(\mathcal C_n)=\operatorname{Ldim}(\mathcal C_n)=n-1.\]

For \(n\ge2\), the shattered-support complex is the barycentric subdivision of the boundary of an \((n-1)\)-simplex, homeomorphic to \(S^{n-2}\). Its \(h\)-polynomial is the ordinary Eulerian polynomial \(\sum_{j=0}^{n-1}\left\langle\begin{smallmatrix}n\\j\end{smallmatrix}\right\rangle t^j\). The topology and Eulerian identity themselves are standard results about Boolean order complexes; the learning-theoretic identification is the contribution here.

## Assumptions and scope

Write \([n]=\{1,\dots,n\}\) and \(X_n=2^{[n]}\setminus\{\varnothing,[n]\}\). For a permutation \(\pi=(\pi_1,\dots,\pi_n)\), its concept \(c_\pi:X_n\to\{0,1\}\) satisfies \(c_\pi(A)=1\) precisely when \(A=\{\pi_1,\dots,\pi_{|A|}\}\). All \(n!\) permutations are hypotheses; all nonempty proper subsets are allowed as queries. Shattering uses all binary labelings on a fixed support. Littlestone dimension is the greatest depth of a complete binary query tree whose root-to-leaf label sequences each have a consistent hypothesis. We take depth zero for a nonempty family with no informative queries.

The statements hold for every integer \(n\ge1\). The topological sphere assertion is for \(n\ge2\), since the query set is empty at \(n=1\). This is **not** the pairwise-comparison query class on permutations, where a query asks the relative order of two elements.

## Proof

**1. Characterization of shattered supports.** Suppose \(S\subseteq X_n\) is shattered. The all-positive labeling is realized by a maximal chain, which contains every member of \(S\); hence any two members of \(S\) are comparable.

Conversely, suppose \(S\) is a strict inclusion chain. Fix any assignment of zeros and ones on \(S\). List its positive sets in increasing order \(P_1\subsetneq\dots\subsetneq P_r\), and adjoin \(P_0=\varnothing\) and \(P_{r+1}=[n]\). For each \(0\le i\le r\), put \(D_i=P_{i+1}\setminus P_i\), which is nonempty. Every negatively labeled member between \(P_i\) and \(P_{i+1}\) has the form \(P_i\cup W\), where \(W\) is a proper nonempty subset of \(D_i\). These \(W\)'s are nested because the original support was a chain. If any occur, let \(W_{\max}\) be the largest and order the elements of \(D_i\) with an element of \(D_i\setminus W_{\max}\) first; otherwise order \(D_i\) arbitrarily. In this block no proper prefix can equal any forbidden \(W\), whereas the block endpoint \(P_{i+1}\) is reached. Concatenating all block orders yields a permutation whose chain visits every positive query and none of the negative queries. Thus every labeling is realized. The empty support is automatically shattered.

**2. Exact count, dimension and topology.** A strict chain of \(k\) nontrivial subsets produces \(k+1\) nonempty consecutive differences between the adjoined endpoints; conversely, an ordered partition into \(k+1\) nonempty blocks recovers the chain uniquely. There are \((k+1)!\,\left\{\begin{smallmatrix}n\\k+1\end{smallmatrix}\right\}\) such partitions. The longest supports have \(n-1\) members. The simplicial complex whose faces are all shattered supports is therefore precisely the order complex of the proper Boolean lattice, the barycentric subdivision of the boundary of the simplex on \([n]\). In particular it is a triangulated \((n-2)\)-sphere when \(n\ge2\). For its \(h\)-polynomial, the standard transform is

\[h_n(t)=\sum_{k=0}^{n-1}(k+1)!\,\left\{\begin{smallmatrix}n\\k+1\end{smallmatrix}\right\}t^k(1-t)^{n-1-k}.\]

The falling-factorial identity \(m^n=\sum_{r=1}^n\left\{\begin{smallmatrix}n\\r\end{smallmatrix}\right\}(m)_r\), summed over \(m\ge0\) with weight \(t^m\), identifies this transform with the Eulerian polynomial \(A_n(t)\), via \(\sum_{m\ge0}m^nt^m=tA_n(t)/(1-t)^{n+1}\) and \(\sum_{m\ge0}(m)_rt^m=r!t^r/(1-t)^{r+1}\). This is the classical Eulerian identity.

**3. Exact adaptive dimension.** We use the standard product lemma: for finite nonempty binary concept classes \(\mathcal H\) and \(\mathcal K\) on disjoint query domains,

\[\operatorname{Ldim}(\mathcal H\times\mathcal K)=\operatorname{Ldim}(\mathcal H)+\operatorname{Ldim}(\mathcal K).\]

To prove the lower bound, concatenate complete shattered query trees for the two factors, choosing the second tree independently below every first-tree leaf. For the upper bound, induct on the combined numbers of hypotheses. At a nonconstant query of the first factor, at least one of the two answer-branch classes has Littlestone dimension at most one smaller than the first factor's dimension; otherwise a deeper complete tree would exist. That child is a proper smaller family, so the induction hypothesis bounds the corresponding product child by the sum of dimensions minus one. The same holds for queries of the second factor. Constant queries cannot root a complete tree. The recursive definition of Littlestone dimension gives the upper bound. The base case is a singleton concept class.

Now induct on \(n\). At \(n=1\), no query exists and the dimension is zero. Fix a nonempty proper query \(A\subset[n]\) of cardinality \(k\), with \(1\le k\le n-1\). Conditional on answering \(1\), the unknown permutation consists of an arbitrary permutation of \(A\), then an arbitrary permutation of its complement. All other nonconstant query answers are prefix-membership questions strictly inside \(A\) or strictly above \(A\). Questions incomparable with \(A\) are forced zero, and the question \(A\) is forced one. Thus the positive-branch concept class is precisely the disjoint-domain product of \(\mathcal C_k\) and \(\mathcal C_{n-k}\) after deleting constant coordinates. Its Littlestone dimension is \((k-1)+(n-k-1)=n-2\) by induction and the product lemma. A complete binary mistake tree of depth \(n\) would have to start with some query \(A\) and have both children of dimension at least \(n-1\), contradicting the positive-branch bound \(n-2\). Therefore \(\operatorname{Ldim}(\mathcal C_n)\le n-1\). The already proved shattering of an \((n-1)\)-element support gives \(\operatorname{Ldim}(\mathcal C_n)\ge\operatorname{VCdim}(\mathcal C_n)=n-1\), proving equality.

## Verification

A separate finite checker, `check_boolean_chains.py`, enumerates all \(n!\) permutation chains and every candidate query support for \(1\le n\le5\), compares exact trace shattering against inclusion comparability and the Stirling formula, and independently computes complete-tree Littlestone ranks by memoized version-space recursion. It also checks Eulerian \(h\)-coefficients through \(n=9\). The terminal marker on replay is `BOOLEAN_CHAIN_SHATTERING_PASS face_n=1..5 ldim_n=1..5 eulerian_n=1..9`. The proof above, rather than finite checks, establishes every integer \(n\ge1\).

To reproduce, execute `python3 check_boolean_chains.py` using Python 3.10 or later; no third-party packages are required. The checker assumes exact integer arithmetic.

## Relationship to prior work

Chase and Freitag, *Model theory and combinatorics of banned sequences* (arXiv:1801.07640v1, 2018), develops general VC and Littlestone/thicket combinatorics. Its results do not enumerate shattered supports for maximal-chain prefix membership. Braun and Hough, *Homomorphism Complexes and Maximal Chains in Graded Posets* (arXiv:1812.07335v1, 2018), constructs a **different** homomorphism cell complex from chains of distributive lattices; in the Boolean case it is associated with cubical cells of the permutahedron, not with binary prefix-membership shattering. Chen, Eur, Yang and Zhang, *Free resolutions of function classes via order complexes* (arXiv:1909.02159v1, 2019), studies the order complex of a poset to resolve ideals of **intersection-closed** function classes: its hypotheses identify individual elements of an intersection-closed poset, rather than incidence indicators of its maximal chains. Neither construction is a proof of the present shattering equivalence or exact online rank. These established structural and algebraic facts are not claimed as new here.

## Limitations

This theorem concerns the finite Boolean lattice and a specific prefix-set membership query domain. It does not give the Littlestone dimension for arbitrary finite posets or for queries comparing pairs of labels. The Eulerian identity and barycentric sphere property are classical once the shattering-complex identification is made. Exhaustive tests stop at five ground-set elements for shattering and online rank; they are evidence for implementations, not finite substitutes for the general proofs. Priority assessment is limited to the identified and inspected literature, and an older result using another formulation could exist. No independent mathematical audit is claimed.

## References

1. Hunter Chase and James Freitag, *Model theory and combinatorics of banned sequences*, arXiv:1801.07640v1, 2018; later *Journal of Symbolic Logic* 87 (2022), 1–20. https://arxiv.org/abs/1801.07640.
2. Benjamin Braun and Wesley K. Hough, *Homomorphism Complexes and Maximal Chains in Graded Posets*, arXiv:1812.07335v1, 2018; *European Journal of Combinatorics* 81 (2019), 178–194. https://arxiv.org/abs/1812.07335.
3. Justin Chen, Christopher Eur, Greg Yang, and Mengyuan Zhang, *Free resolutions of function classes via order complexes*, arXiv:1909.02159v1, 2019; *Advances in Applied Mathematics* 120 (2020), 102074. https://arxiv.org/abs/1909.02159.
