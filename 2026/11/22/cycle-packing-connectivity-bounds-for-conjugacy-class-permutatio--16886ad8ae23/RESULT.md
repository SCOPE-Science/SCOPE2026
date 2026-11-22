# Cycle-packing connectivity bounds for conjugacy-class permutation complexes

## Finding

Fix an integer \(n\ge2\). Let \(\lambda=(\ell_1,\ldots,\ell_s)\) be a partition of \(n\), including parts of size one, and let \(C_\lambda\subseteq S_n\) be the conjugacy class of permutations of cycle type \(\lambda\). For \(\pi\in S_n\), identify \(\pi\) with its one-line word \(\pi(1)\cdots\pi(n)\). A subword means a **subsequence** with increasing original positions, not necessarily consecutive positions, and retains the exact letter values, not only their relative order. Define \(X_\lambda\) as the regular CW (semisimplicial) complex with one cell for each nonempty distinct injective subword of some member of \(C_\lambda\), and with alternating deletion face maps.

Define the cycle-packing capacity

\[
 c(\lambda)=\sum_{j=1}^{s}\left\lfloor\frac{\ell_j}{2}\right\rfloor.
\]

**Theorem (universal lower skeleton).** If \(c(\lambda)\ge1\), then every injective word on \([n]\) of length \(k\), for every \(1\le k\le c(\lambda)\), occurs in \(X_\lambda\). Consequently the regular CW \((c(\lambda)-1)\)-skeleton of \(X_\lambda\) is exactly the corresponding skeleton of the full complex \(\operatorname{Inj}([n])\), with

\[
 f_{k-1}(X_\lambda)=\frac{n!}{(n-k)!}\qquad(1\le k\le c(\lambda)).
\]

If \(c(\lambda)\ge2\), then

\[
 \pi_i(|X_\lambda|)=0\quad(0\le i\le c(\lambda)-2),
 \qquad \widetilde H_i(X_\lambda;\mathbb Z)=0\quad(0\le i\le c(\lambda)-2).
\]

Here \(\pi_0=0\) signifies path connectivity. The corresponding reduced-homology vanishing holds over any coefficient group. In particular \(c(\lambda)\ge3\) implies simple connectivity.

**Sharp natural family.** For the fixed-point-free involution class \(\lambda=(2^m)\), \(n=2m\) and \(c(\lambda)=m\). Its complete lower skeleton stops exactly at dimension \(m-1\): the increasing word \(1\,2\,\cdots\,(m+1)\) is absent, so the dimension-\(m\) skeleton is not the full injective-word skeleton, for every \(m\ge1\). No assertion is made that the lower homotopy connectivity is itself sharp.

## Assumptions and scope

The construction uses the full **group-theoretic conjugacy class**, not all derangements, a cyclic subgroup, a single chosen permutation, or a pattern-avoidance class. The chosen cycle decomposition contains precisely the lengths \(\ell_j\); singleton parts correspond to fixed points. The one-line positions are ordered by their numeric labels, and the target subword is an arbitrary ordered tuple of distinct *values*. The cells of \(X_\lambda\) have dimension one less than their word length. We use the regular semisimplicial realization; its barycentric subdivision is the order-complex convention in Chachólski–Levi–Meshulam and has the same homotopy type.

## Proof

**1. Packing any short word into a prescribed cycle type.** Let \(1\le k\le c(\lambda)\) and take an arbitrary injective word \(w=(a_1,\ldots,a_k)\) over \([n]\). Since \(c(\lambda)\le\lfloor n/2\rfloor\), the complement \([n]\setminus\{a_1,\ldots,a_k\}\) has at least \(k\) labels. Choose \(k\) distinct complementary labels in increasing order

\[
 b_1<b_2<\cdots<b_k.
\]

Demand the directed permutation edges \(b_i\mapsto a_i\), for \(1\le i\le k\). Their \(2k\) endpoints are pairwise distinct. Because \(\sum_j\lfloor\ell_j/2\rfloor\ge k\), allocate these \(k\) prescribed two-vertex directed paths to the \(s\) desired cycles, with \(t_j\) paths assigned to the cycle of length \(\ell_j\), where

\[
 0\le t_j\le\lfloor\ell_j/2\rfloor,
 \qquad \sum_{j=1}^{s}t_j=k.
\]

This allocation exists greedily by the total capacity inequality. There are \(n-2k=\sum_j(\ell_j-2t_j)\) unused labels. Allocate exactly \(\ell_j-2t_j\) of them to cycle \(j\). Treat each prescribed edge as a consecutive two-letter *block* \((b_i,a_i)\), and each allocated spare label as a one-letter block. Concatenate these blocks into a single cyclic ordering of exactly \(\ell_j\) labels, then let the permutation map each label to its next cyclic successor. This constructs a cycle of length \(\ell_j\), retaining all prescribed transitions \(b_i\mapsto a_i\). The cycles are disjoint and cover \([n]\), so their product \(\pi\) has type \(\lambda\).

At one-line positions \(b_1<\cdots<b_k\) its entries are \(\pi(b_i)=a_i\), in precisely the prescribed order. Therefore \(w\) is a subword of \(\pi\in C_\lambda\), as required. This works with even or odd cycle parts, fixed points, and all allowed target words; it does not rely on experiment.

**2. Connectivity from a common lower skeleton.** The complete injective-word complex \(I_n=\operatorname{Inj}([n])\) is known to be homotopy equivalent to a wedge of spheres of dimension \(n-1\) (Farmer; Björner–Wachs), so it is \((n-2)\)-connected. Step 1 says that the inclusion \(X_\lambda\hookrightarrow I_n\) is a CW inclusion with **no relative cells of dimension less than \(c(\lambda)\)**. By cellular approximation (or relative homotopy of a CW pair), it induces isomorphisms on \(\pi_i\) in degrees \(i\le c(\lambda)-2\). Since \(c(\lambda)\le n/2\), the corresponding homotopy groups of \(I_n\) vanish. The homology claim follows by the same skeletal comparison, or by connectivity and Hurewicz, and is integral, hence coefficient-independent.

**3. Sharpness of the universal skeleton for fixed-point-free involutions.** If \(\pi\) consists of \(m\) disjoint transpositions on \([2m]\), consider a transposition \((u\ v)\) with \(u<v\). In the one-line word \(\pi(1),\ldots,\pi(2m)\), the value \(v\) occurs at position \(u\), and \(u\) occurs at the later position \(v\). Thus the two values of each transposition occur in **decreasing** order. An increasing subsequence can use at most one value from each of the \(m\) transposition pairs, so it has length at most \(m\). Hence the increasing \((m+1)\)-letter word is absent in the entire conjugacy class, whereas Step 1 supplies all words through length \(m\). This proves the claimed exact skeleton threshold.

## Verification

Run `python3 verify.py` using Python's standard library. The checker exhaustively enumerates every permutation in symmetric groups of orders \(2\) through \(8\), groups by exact cycle type, and counts all subwords of the asserted maximal universal length. It obtains all expected ordered words for every nonidentity cycle type (respectively 1, 2, 4, 6, 10, 14, and 21 tested types). It also reconstructs an explicit prescribed-type witness for each observed short word, tests 4,560 deterministic constructions on twelve letters across seven cycle types, and checks the involution threshold for six even orders. Recorded results are embedded in `checks.txt`.

These finite checks corroborate but do **not** establish the all-\(n\) theorem. Its proof is the explicit block construction and the CW skeletal argument above. The code does not compute infinite homotopy groups, homology above the stated vanishing range, or a complete homotopy type.

## Relationship to prior work

Govc's November 8, 2026 preprint proves that fundamental groups of arbitrary permutation complexes are **free**, but does not give this cycle-type capacity, complete skeleton, or higher connectivity threshold. Chachólski–Levi–Meshulam introduce permutation complexes and analyze complexes generated by two permutations; their classical full-injective-word sphere result supplies the ambient connectivity used here, but does not imply that a given conjugacy-class subcomplex contains the ambient lower skeleton. Elizalde–Hanlon–Hersh (2026) study injective words avoiding **relative-order patterns**; their generators and avoidance condition differ from a fixed exact cycle type and do not yield the universal exact-letter subwords proved here. Small finite conjugacy-class homology calculations provide useful consistency checks but do not subsume the unrestricted cycle-packing statement.

## Limitations

The result is a **lower connectivity bound**, not a computation of all Betti numbers, torsion above the guaranteed vanishing degrees, or the complete integral homotopy type. The sharpness theorem concerns the *skeletal* range for the fixed-point-free involution family, not a proof that its first nontrivial homology occurs at that degree. General cycle types may admit longer universal subwords. The proof assumes the entire conjugacy class, and it does not extend unchanged to arbitrary permutation subsets or to pattern containment without retaining exact letter values. Priority against unindexed or inaccessible equivalent statements has not been independently certified.

## References

1. Dejan Govc, *Fundamental Groups of Permutation Complexes*, arXiv:2611.11362v1, first posted November 8, 2026. https://arxiv.org/abs/2611.11362
2. Wojtek Chachólski, Ran Levi and Roy Meshulam, *On the topology of complexes of injective words*, arXiv:1908.03394, 2019; J. Appl. Comput. Topol. 4 (2020), 29–44. https://arxiv.org/abs/1908.03394
3. Sergi Elizalde, Philip Hanlon and Patricia Hersh, *Complexes of pattern-avoiding injective words*, arXiv:2610.07303v1, first posted October 5, 2026. https://arxiv.org/abs/2610.07303
4. A. Björner and M. Wachs, *On lexicographically shellable posets*, Trans. Amer. Math. Soc. 277 (1983), 323–341; full injective-word sphere theorem as quoted in References 1–3.
5. F. D. Farmer, *Cellular homology for posets*, Math. Japon. 23 (1978/79), 607–613.
