# Sharp three-round equivalence of finite Boolean inclusion posets

## Finding
For each integer \(n\ge1\), let \(\mathcal B_n=(\mathcal P(\{1,\ldots,n\}),\subseteq)\). Work in the purely relational first-order language with equality and one binary inclusion predicate, with no named constants or Boolean operations. Write \(\equiv_3\) for agreement on sentences of quantifier rank at most three. Then for all positive integers \(m,n\),
\[
\mathcal B_m\equiv_3\mathcal B_n\quad\Longleftrightarrow\quad\min(m,6)=\min(n,6).
\]
There are exactly six rank-three theories within this family. The least representative of the eventual class has six atoms and sixty-four elements. The threshold six is sharp.

## Assumptions and scope
The structure's elements are **subsets**, not individual underlying atoms. The only nonlogical relation is reflexive inclusion \(X\subseteq Y\). Equality is logical equality, not a separately added predicate. No names for top, bottom, join, meet, complement, the atom predicate, or cardinality are present; some are first-order definable with additional quantifier depth but are not atomic. Quantifier rank counts nested quantifiers. The result is strictly at rank three, for all \(m,n\ge1\).

## Proof
**Atomic types.** Fix ordered previously chosen subsets \(X_1,\dots,X_k\). Their membership vectors partition the underlying atom set into \(2^k\) disjoint Venn cells \(C_s\), indexed by bit vectors \(s\). Write \(c_s=|C_s|\). The full atomic diagram of the chosen tuple is exactly the list of inclusion truths \(X_i\subseteq X_j\): each holds if and only if all cells with \(s_i=1\) and \(s_j=0\) are empty. Thus it depends on which cells have cardinality zero. Selecting one additional subset splits each cell independently into a chosen and unchosen part.

**One remaining round after two selections.** Let \(T(c_{00},c_{10},c_{01},c_{11})\) denote the pair's atomic diagram together with the **set of all** atomic diagrams obtainable by adding one more chosen subset. Every diagram after the last selection depends only on emptiness of its eight Venn cells. A parent cell of size zero permits only \((0,0)\), size one permits \((0,1)\) and \((1,0)\), and every size at least two permits all three qualitative splits \((0,+)\), \((+,0)\), and \((+,+)\). Hence \(T\) is unchanged on replacing any parent cell size by \(\min(c_s,2)\).

The following two reduction identities hold for all nonnegative integers \(a,b\):
\[
T(a,2,b,2)=T(a,2,b,1),\qquad
T(2,a,2,b)=T(1,a,2,b).
\]
They are **not** claims that the four Venn cell cardinalities agree: they assert equality of the pair atomic diagram and of the sets of possible third-move atomic diagrams. The finite certificate `verify_reductions.py` enumerates all nine choices of \((\min(a,2),\min(b,2))\) for each identity, constructs all qualitative third-move splits, and checks equality of the resulting diagrams. Because \(T\) depends only on cell sizes truncated at two, these eighteen exact comparisons exhaust all possible \(a,b\). In each identity the cells of sizes two and two belong to the same side of the **first** selected subset, and the identities allow a \((2,2)\) split to be represented by \((2,1)\) or \((1,2)\) without changing the final-round type.

**Two remaining rounds after one selection.** For a first selected subset \(X\), put \(u=|X|\), \(v=n-|X|\). Selecting a second subset splits each of these two regions into two Venn cells. Because of the preceding truncation and identities, the set of attainable \(T\)-types depends on \(u,v\) only through \(\min(u,3),\min(v,3)\): for a region of cardinality below three all splits are copied exactly; for size at least three a split with a zero or singleton part is copied using a three-element region; a split with both parts at least two is replaced, via the relevant identity above, by a split \((2,1)\) or \((1,2)\) of a three-element region. Conversely, each of the four possible split-size pairs for a three-element region has the same capped-two qualitative description as a split of every larger region. The two regions split independently. By the standard recursive definition of Ehrenfeucht–Fraïssé types, this establishes equality of the complete two-remaining-round types whenever the two truncated region-size pairs agree.

**Infinite tail.** At the start of a three-round game, the possible first-move types therefore depend only on the set
\[
\left\{\bigl(\min(u,3),\min(n-u,3)\bigr):0\le u\le n\right\}.
\]
For every \(n\ge6\), this set is the same: the boundary pairs \((0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\). Hence \(\mathcal B_m\equiv_3\mathcal B_n\) whenever \(m,n\ge6\).

**Sharpness and all remaining cases.** The exact type recurrence implemented in `verify_orbits.py` is
\[
F_0(\mathbf c)=\operatorname{atomic}(\mathbf c),\qquad
F_{r+1}(\mathbf c)=\left(\operatorname{atomic}(\mathbf c),\left\{F_r(\mathbf c-\mathbf d,\mathbf d):\mathbf 0\le\mathbf d\le\mathbf c\right\}\right).
\]
All vectors are finite nonnegative integer vectors; each child vector is formed by the four (or fewer) independent cell splits, and the sets discard duplicate isomorphic extension types. For \(n=1,\ldots,7\) the six types for \(n=1,\ldots,6\) are pairwise distinct while those for \(n=6\) and \(n=7\) coincide. This is an exhaustive finite mathematical certificate for the lower range; it is also independently recomputed by `verify_direct.py` by enumerating the actual subsets and every next move, rather than using Venn-cell symmetries. Combining these finite separations with the infinite-tail proof yields the stated iff classification for all positive parameters.

## Verification
`verify_reductions.py` checked all eighteen exact local reduction identities. `verify_orbits.py` computed the complete three-round recursive types for \(n=1\) through \(n=12\), obtaining consecutive interned IDs \(14,41,63,74,77,79,79,79,79,79,79,79\). `verify_direct.py` independently computed the complete three-round types of actual subset-posets through \(n=7\), obtaining \(14,41,63,74,77,79,79\). The IDs are internal canonicalization labels, not universal numerical invariants; the equality pattern is what matters. In the direct computation 2,418,849 memoized tuple states were visited. These finite checks prove the finite boundary; the reduction argument proves the infinite claim.

All scripts are standalone Python 3 standard-library programs. Run each from an ordinary directory using `python3 verify_reductions.py`, `python3 verify_orbits.py`, and `python3 verify_direct.py`. Their recorded outputs appear in `checks_output.txt`. Every file needed to reproduce the computation is included.

## Relationship to prior work
Libkin, *Elements of Finite Model Theory*, Chapter 5, Lemma 5.5 and Claim 5.7, works with this **same inclusion-only powerset language** and proves that all sufficiently large \(\mathcal B_n\) agree up to rank \(q\) provided both atom counts are at least \(2^q\). At rank three this is the sufficient threshold eight. It does not prove the sharper threshold six, its sharpness, or the exact six-class classification. The improvement is obtained by using the restricted atomic inclusion comparisons instead of full Venn-cell occupancy preservation.

A separately published statement titled *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras* establishes the exact \(2^q\) threshold in the **functional Boolean-algebra language** with \(0,1,\wedge,\vee,\neg\). That stronger signature permits arbitrary Boolean terms as atomic formulas; its rank-three eight-atom result implies a sufficient bound of eight in the inclusion reduct but does not imply the sharp six-atom statement (notably the comparison of six- and seven-atom models). Kuncak and Rinard investigate Venn-cell quantifier elimination for Boolean algebras with cardinality constraints, not the exact three-round inclusion-poset classification. Abu Zaid discusses model-checking bounds and algebraic signatures, not this sharp classification.

## Limitations
This result concerns the pure inclusion reduct and quantifier rank exactly three, not the full Boolean functional signature, additional constants or counting predicates, or a formula-by-formula classification for higher ranks. The finite certificate exhausts the indicated finite boundary but alone would not establish the infinite tail. No claim is made to exhaustive historical priority; earlier folklore or inaccessible sources may contain an equivalent statement. No independent mathematical audit is claimed.

## References
1. Leonid Libkin, *Elements of Finite Model Theory*, Springer, first published 2004-07-02, Chapter 5, Lemma 5.5 and Claim 5.7, DOI 10.1007/978-3-662-07003-1. Open full text: https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf.
2. Viktor Kuncak and Martin Rinard, *The First-Order Theory of Sets with Cardinality Constraints is Decidable*, arXiv:cs/0407045, first posted 2004-07-17. https://arxiv.org/pdf/cs/0407045.
3. Faried Abu Zaid, *Uniformly Automatic Classes of Finite Structures*, FSTTCS 2018, DOI 10.4230/LIPIcs.FSTTCS.2018.10.
4. *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-2-q-atom-visibility-threshold-for-finite-boolean-algebras--938cb5f89dc7.
