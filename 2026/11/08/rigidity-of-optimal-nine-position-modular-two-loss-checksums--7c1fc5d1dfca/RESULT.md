# Rigidity of optimal nine-position modular two-loss checksums

## Finding

Let \(B\subseteq\mathbb Z_{56}\) be a set of nine distinct residues, and call it a *pair-separating checksum set* if the \(\binom92=36\) residues \(b+b'\pmod{56}\), for unordered pairs of distinct \(b,b'\in B\), are pairwise different. There are **exactly \(1344\)** such nine-element sets \(B\). All of them are related by an affine unit map \(x\mapsto ux+v\pmod{56}\), with \(\gcd(u,56)=1\). In particular there is **exactly one affine equivalence class**, represented by

\[
B_0=\{0,2,4,18,19,25,28,31,36\}.
\]

The affine action is free on these sets: the \(\varphi(56)\cdot56=1344\) affine maps produce pairwise different images of \(B_0\). Exactly \(216\) of the valid sets contain zero. The minimum modulus \(56\) for nine pair-separating checksums is a *previously established fact*, not part of the new priority claim; the contribution is the exact census and classification at this minimum modulus.

In a binary nine-position word, if exactly two \(1\to0\) losses occur, the difference between the original checksum \(\sum_j b_jx_j\pmod{56}\) and the received checksum uniquely identifies the two lost positions. Thus this classifies the coefficient **sets** for minimum-modulus nine-position two-loss checksums, modulo residue affine transformations and coordinate reordering, provided the number of losses is known to be exactly two.

## Assumptions and scope

The ambient additive group is \(\mathbb Z_{56}\). Coefficients are distinct. Only sums of **two different** coefficients must be unique; repeated-index sums \(2b\) are not constrained. The checksum interpretation assumes the loss count equals two. The conclusion classifies sets, not labeled tuples: assigning the nine coefficients to nine distinguished coordinates introduces \(9!\) coordinate permutations, which are not being separately counted.

An affine transformation consists of multiplication by a unit modulo \(56\), followed by translation modulo \(56\). Such transformations preserve distinctness of unordered two-element sums: both sides of each possible equality are multiplied by \(u\) and shifted by \(2v\).

## Proof

**Step 1: a valid representative and its affine orbit.** For \(B_0\) above, compute all \(36\) unordered two-element sums modulo \(56\); they are distinct. The standalone `checker.py` independently verifies this by computing the complete sum list. There are \(\varphi(56)=24\) units modulo \(56\). The same checker constructs the sets

\[
\mathcal O=\bigl\{\{ub+v\bmod56:b\in B_0\}:\gcd(u,56)=1,\ 0\le v<56\bigr\}
\]

and verifies that they are all different, so \(|\mathcal O|=1344\); exactly \(216\) contain zero.

**Step 2: a complete finite search containing zero.** Every valid set can be translated to contain zero. To count those containing zero without orbit assumptions, consider exactly the sorted tuples

\[
0=b_0<b_1<\cdots<b_8\le55.
\]

For a prefix \(b_0,\ldots,b_{k-1}\), maintain the set \(T_k\) of pair sums of distinct earlier terms, represented by a 56-bit integer. A candidate \(b_k=v>b_{k-1}\) is admissible precisely when none of the \(k\) residues \(v+b_i\pmod{56}\), for \(0\le i<k\), occurs in \(T_k\); the \(k\) new residues are mutually distinct automatically because the earlier terms are distinct. Upon acceptance update \(T_{k+1}=T_k\cup\{v+b_i\pmod{56}:i<k\}\). Prune values that leave fewer than the required remaining distinct larger residues.

This recursive test is both necessary and sufficient for extendability as a valid *prefix*: every valid sorted nine-set containing zero follows one branch; each completed branch is valid and appears exactly once. The explicit standard-library implementation, `checker.py`, executes the full search from \((b_0,T_1)=(0,\varnothing)\). It visits \(3{,}455{,}863\) recursive nodes and produces exactly **\(216\)** completed nine-sets containing zero. Moreover the resulting bit-mask set equals the independently generated set of \(216\) zero-containing affine images from Step 1. The separate C++ implementation, `independent.cpp`, also counts \(216\) complete branches and finds one affine canonical mask; this is a cross-check, not a replacement for the exhaustive-search proof.

**Step 3: count all unanchored sets and deduce rigidity.** Let \(\mathcal F\) be the collection of all valid nine-sets. Count incidences \((B,b)\) with \(B\in\mathcal F\) and \(b\in B\) in two ways. There are \(9|\mathcal F|\) incidences. For each \(b\), translation by \(-b\) bijects sets containing \(b\) with sets containing zero, so there are exactly \(216\) of them. Summing over all \(56\) possible \(b\) gives

\[
9|\mathcal F|=56\cdot216,\qquad |\mathcal F|=1344.
\]

The orbit \(\mathcal O\subseteq\mathcal F\) from Step 1 already has \(1344\) members. Consequently \(\mathcal F=\mathcal O\), proving the census, freeness, and unique affine equivalence class.

**Step 4: checksum interpretation.** Let the nine coefficient values \(b_0,\ldots,b_8\) be assigned bijectively to nine binary positions. If an input \(x\) loses exactly two ones, at positions \(i,j\), then, for received \(y\),

\[
\sum_{k=0}^{8} b_k(x_k-y_k)\equiv b_i+b_j\pmod{56}.
\]

Pair-sum uniqueness determines the unordered pair \(\{i,j\}\) from the syndrome difference. For an affine relabeling \(b'_k=ub_k+v\), the two-loss syndrome difference becomes \(u(b_i+b_j)+2v\); multiplication by a unit and known translation preserve injective decoding. Therefore all minimum-modulus coefficient sets yield the same pair-identification structure under this natural equivalence.

## Verification

Run `python3 checker.py` using Python 3 with no third-party dependencies. The checker derives all \(216\) valid zero-containing sets, generates every affine image of \(B_0\), checks the two collections coincide, verifies orbit size \(1344\), rechecks every orbit member's \(36\) sums, and validates the double count. Expected line:

`PASS: anchored valid sets=216, search nodes=3455863, orbit=1344, unique affine class`

For a second implementation, compile `independent.cpp` with `c++ -std=c++17 -O2 independent.cpp -o check_independent` and run `./check_independent`. It reports `containing_zero=216 orbit_count=1`. The proof of exhaustiveness depends on the recursion invariants in Step 2, not on the mere fact that a program terminated.

## Relationship to prior work

Ye, Sabary, Gabrys, Yaakobi and Elishco (2026, arXiv:2608.08018, first public August 8, 2026), Section III-C, use weak \(B_e\)-sets as checksum coefficients for composite-DNA asymmetric errors. Their finite table gives examples only through seven coefficients and the eight-coefficient two-loss case; it does not classify the nine-coefficient minimum case.

Haanpää, Huima and Östergård (2004, DOI 10.1016/S0166-218X(03)00273-7) previously established the minimum cyclic modulus \(56\) for nine distinct-pair sums; this is also recorded in OEIS A004135 and A260998. The related Haanpää–Östergård 2004 technical report (A87) explains affine equivalence and gives maximum set sizes and sample sets, but its reported tables do not provide the count \(1344\), the zero-containing count \(216\), or a complete one-orbit classification for nine-element sets in \(\mathbb Z_{56}\). In particular the known numerical minimum is not being relabeled as new.

## Limitations

This is a finite classification conditional on the previously known minimal modulus. It treats unordered sums of distinct pairs only, not ordinary stronger Sidon sets allowing repeated indices. It does not establish the smallest modulus for higher dimensions or higher deletion counts, nor the performance of a full composite-DNA code beyond the injective single-row syndrome ingredient. The original full text of the 2004 cyclic-group paper was not accessible in this review; an unpublished enumeration or unindexed affine orbit count may already exist.

## References

1. Z. Ye, O. Sabary, R. Gabrys, E. Yaakobi, O. Elishco, *More on Codes for Combinatorial Composite DNA*, arXiv:2608.08018, first released 2026-08-08. https://arxiv.org/abs/2608.08018
2. H. Haanpää, A. Huima, P. R. J. Östergård, *Sets in Z_n with Distinct Sums of Pairs*, Discrete Applied Mathematics 138 (2004), 99–106. https://doi.org/10.1016/S0166-218X(03)00273-7
3. H. Haanpää, P. R. J. Östergård, *Sets in Abelian Groups with Distinct Sums of Pairs*, Research Report HUT-TCS-A87 (2004), Section 4 and Tables 1–3. https://www.tcs.hut.fi/Publications/bibdb/HUT-TCS-A87.pdf
4. OEIS A004135, least cyclic modulus for distinct sums of pairs. https://oeis.org/A004135
5. OEIS A260998, maximal size of pair-sum-distinct subsets of a cyclic group. https://oeis.org/A260998
