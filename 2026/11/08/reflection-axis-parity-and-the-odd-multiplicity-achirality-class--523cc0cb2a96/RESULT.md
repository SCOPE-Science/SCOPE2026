# Reflection-axis parity and the odd-multiplicity achirality classification of perfect necklaces

## Finding
Let \(q\ge 2\), \(k\ge 1\), and \(n\ge 1\) be integers, and let \(\Sigma\) be an alphabet of size \(q\). A \((k,n)\)-perfect necklace is a circular word of length \(L=nq^k\) in which every \(k\)-letter word appears at exactly \(n\) cyclic starting positions, one in each residue class modulo \(n\). It is *achiral* if its reversal is one of its rotations.

**Theorem.** The following assertions hold.

1. For **every odd** \(n\), an achiral \((k,n)\)-perfect necklace exists if and only if \(q=2\) and \(k\in\{1,2\}\). In the exceptional cases the binary necklaces represented by \((01)^n\) for \(k=1\), and by \((0011)^n\) for \(k=2\), are achiral and perfect.
2. For **every even** \(n\), if a \((k,n)\)-perfect word \(w\) obeys \(w_i=w_{c-i}\) for all \(i\in\mathbb Z/L\mathbb Z\), then \(c-k+1\) is odd. In other words, the reflection of the \(k\)-window starting positions must have no fixed residue modulo \(n\).
3. Let \(P_q(k,n)\) be the number of \((k,n)\)-perfect necklaces (rotations identified) and \(B_q(k,n)\) the number of their bracelets (rotations and reversal identified). For odd \(n\) and \((q,k)\notin\{(2,1),(2,2)\}\),
   \[
   B_q(k,n)=\frac{P_q(k,n)}2.
   \]
   Thus the known necklace-count formula immediately gives the complete bracelet count in this parameter range, without any additional fixed-point term.

The even-multiplicity axis restriction is nonvacuous: the circular binary word `0001011100111010` is \((3,2)\)-perfect and achiral, with a reflection \(w_i=w_{1-i}\).

## Assumptions and scope
We index cyclic positions by \(\mathbb Z/L\mathbb Z\), and every window is read cyclically, including those wrapping over the end of a representative. Two representatives of the same necklace differ by rotation. Reversal does **not** permute alphabet symbols; reverse-complement symmetry is a different operation. We do not assert that all even-multiplicity parameters admit achiral representatives.

## Proof
Fix an achiral perfect necklace and a representative \(w\). Achirality means that there is an integer \(c\) such that \(w_i=w_{c-i}\) for all \(i\pmod L\). For every cyclic window \(U_i=w_iw_{i+1}\cdots w_{i+k-1}\), symmetry gives
\[
U_{c-k+1-i}=\operatorname{rev}(U_i).
\]
Write \(C=c-k+1\). There are exactly \(q^{\lceil k/2\rceil}\) palindromic words of length \(k\), since the first \(\lceil k/2\rceil\) letters specify the remainder.

For any such palindrome \(u\), let \(I_u=\{i\pmod L:U_i=u\}\). Perfection says that reduction modulo \(n\) maps \(I_u\) bijectively to \(\mathbb Z/n\mathbb Z\). The reflection \(i\mapsto C-i\) preserves \(I_u\). Thus every fixed residue of the induced reflection \(r\mapsto C-r\pmod n\) determines **one actual fixed position** \(i\in I_u\) of the reflection modulo \(L\): the reflected occurrence has the same residue and the same palindromic factor, so uniqueness of the occurrence in that residue forces it to equal the original position. Distinct palindrome types yield disjoint fixed positions.

Let \(f_m(C)=|\{r\pmod m:2r\equiv C\pmod m\}|\). The preceding argument proves the key bound
\[
q^{\lceil k/2\rceil} f_n(C)\le f_L(C)\le 2.
\]
For odd \(n\), \(f_n(C)=1\). Therefore \(q^{\lceil k/2\rceil}\le2\), which, because \(q\ge2\), is equivalent to \(q=2\) and \(k\in\{1,2\}\). This proves the necessity in the first assertion.

For sufficiency, consider first \((01)^n\). Its two one-letter factors begin at positions separated by steps of two, so each appears once per residue modulo odd \(n\) because \(\gcd(2,n)=1\). For \(k=2\), the four circular two-letter windows of `0011` are `00`, `01`, `11`, `10`, in that order. In \((0011)^n\), each occurs at one fixed residue modulo four, repeated at steps of four; those starts cover all residues modulo odd \(n\) since \(\gcd(4,n)=1\). Both base blocks are conjugate to their reversals, so their repetitions are achiral. Hence the first assertion is an exact existence classification.

For even \(n\), if \(C\) were even, then \(2r\equiv C\pmod n\) would have exactly two solutions. Because \(L=nq^k\) is also even, \(f_L(C)=2\). Our bound would imply \(2q^{\lceil k/2\rceil}\le2\), contradicting \(q\ge2\). Therefore \(C\) is odd and the window-start residue reflection has no fixed point. This proves the second assertion.

Finally, reversal preserves perfect necklaces: it permutes length-\(k\) factors by word reversal and sends occurrence residues by an affine bijection. For the odd-multiplicity parameters in the theorem's third assertion, there are no reversal-fixed necklaces by part 1, so reversal partitions the \(P_q(k,n)\) necklaces into pairs. Quotienting these pairs proves the bracelet formula.

For the even-multiplicity example, direct cyclic enumeration gives each of the eight binary three-letter factors twice, once at each residue modulo two. The displayed string is invariant under \(i\mapsto1-i\), verifying that oddness of \(n\) in the existence obstruction cannot be removed.

## Verification
The accompanying standalone `verify.py` independently enumerates indexed words and their exact cyclic window starts for 14 finite parameter configurations, comprising 92,219 words, of which 700 satisfy perfection. It checks every reflection axis of each perfect word, both necessary parity assertions, the positive classification at sampled odd multiplicities, and the explicit even-multiplicity witness. It also checks the two infinite-family constructions at each odd \(n\le19\) by direct factor enumeration. Running `python verify.py` prints `VERIFY_OK configurations=14 words=92219 perfect_labeled=700 symmetric_labeled=180 witnesses=21` when successful. These are finite regressions; the infinite statement follows from the proof, not the enumeration.

## Relationship to prior work
Álvarez, Becher, Ferrari, and Yuhjtman introduced \((k,n)\)-perfect necklaces, proved closure under reversal (their Proposition 7), and counted rotation classes (their Theorem 20). Neither closure nor that enumeration determines which rotation classes are fixed by reversal, which is the missing dihedral fixed-point question settled above at every odd multiplicity. Becher and Tropea's later lexicographic construction concerns extremal representatives rather than this fixed-point classification. The classical no-reversal theorem for de Bruijn necklaces covers the multiplicity-one binary subcase, but does not imply the odd-multiplicity classification or the even-axis restriction. Reverse-complement symmetry is likewise not the same involution.

## Limitations
No existence classification is asserted for even multiplicities: only the necessary parity of possible reflection axes is established there. The bracelet formula in part 3 uses the already-known count \(P_q(k,n)\), and does not claim that this rotation-class count is new. Historical priority for generalized perfect-necklace reflection fixed points may remain in unindexed literature; independent mathematical audit has not been performed.

## References
1. N. Álvarez, V. Becher, P. A. Ferrari, and S. A. Yuhjtman, *Perfect Necklaces*, arXiv:1601.07975 (first public version 2016-01-29), subsequently *Advances in Applied Mathematics* 80 (2016), 48–61, DOI:10.1016/j.aam.2016.05.002.
2. V. Becher and T. Tropea, *Lyndon pairs and the lexicographically greatest perfect necklace*, arXiv:2405.17812 (2024).
3. Z. Chang and Q. Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794 (2024), referring to classical pure-reversal inequivalence.
4. Y. Zelenyuk and Y. Zelenyuk, *Counting Symmetric Bracelets*, DOI:10.1017/S0004972713000701 (first published online 2013-08-22).
