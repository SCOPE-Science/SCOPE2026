# The sharp universal finite-horizon rank of first-order word classifiers

## Finding
Fix any finite nonempty alphabet \(\Sigma\). Represent a finite word by its linearly ordered positions and unary predicates recording its letters, in the standard \(\mathrm{FO}[<]\) signature. For a language \(L\subseteq\Sigma^*\) and integer \(N\ge1\), let \(\rho_L(N)\) be the minimum quantifier rank of a first-order sentence that agrees with \(L\) on every word of length at most \(N\), with no bound imposed on formula size.

**Theorem (sharp universal finite-horizon profile).** For every finite nonempty alphabet and every integer \(N\ge1\),
\[
\max_{L\subseteq\Sigma^*}\rho_L(N)=\left\lceil\log_2(N+1)\right\rceil.
\]
In fact, the same **regular language** \(E=\{w\in\Sigma^*: |w|\text{ is even}\}\) attains the maximum for every \(N\) simultaneously:
\[
\rho_E(N)=\left\lceil\log_2(N+1)\right\rceil.
\]

More precisely, writing \(u\equiv_q v\) when two words satisfy the same \(\mathrm{FO}[<]\) sentences of quantifier rank at most \(q\), for every integer \(q\ge1\):

1. Every two **distinct** words of lengths at most \(2^q-1\) are inequivalent under \(\equiv_q\).
2. This radius is optimal: for any letter \(a\in\Sigma\), the words \(a^{2^q-1}\) and \(a^{2^q}\) are \(q\)-equivalent.

## Assumptions and scope
The empty word is the empty ordered structure. Each position realizes exactly one unary letter predicate. The alphabet is finite and nonempty, and the signature has strict order and one unary predicate for each letter, without endpoint constants, arithmetic predicates or successor. Quantifier rank is the maximum nesting depth of quantifiers, allowing unrestricted Boolean combination. Rank-zero sentences in this signature cannot distinguish any pair of words. The claim concerns all languages, not just regular ones; its extremizing language is regular. The source motivating the invariant was first made public on 29 April 2026.

## Proof
Set \(T_q=2^q-1\). The first assertion is proved by induction on \(q\), in the Ehrenfeucht–Fraïssé game. Its operationally stronger form is: for any distinct two words \(u,v\) of lengths at most \(T_q\), Spoiler wins the \(q\)-round game, regardless of their letters, unless the words are identical.

For \(q=1\), words of length at most \(T_1=1\) are either empty or one letter. If exactly one is empty, Spoiler selects the unique position of the nonempty word. If both have one position but different letters, selecting either position immediately exposes the incompatible unary predicate. These are all the distinct cases.

Assume the assertion for \(q-1\) and let \(q\ge2\). Without loss of generality, \(|u|\ge |v|\). Put \(t=T_{q-1}\). Since \(|u|\le 2t+1\), select a position \(i\) in \(u\) with at most \(t\) positions to its left and at most \(t\) to its right. Spoiler plays this position. If no position in \(v\) has the same letter, Spoiler wins immediately. Otherwise Duplicator answers at some \(j\) having the same letter. Write \(u_\ell,u_r\) for the left and right subwords of \(u\) around \(i\), and \(v_\ell,v_r\) for those of \(v\) around \(j\).

If \(|u|>|v|\), at least one of \(|v_\ell|<|u_\ell|\) and \(|v_r|<|u_r|\) holds. Indeed, otherwise \(|v|=|v_\ell|+1+|v_r|\ge |u|\), a contradiction. Choose a side on which the shorter-side inequality holds. Both compared side lengths are at most \(t\); their words differ because their lengths differ. By the induction hypothesis, Spoiler wins the remaining \(q-1\) moves inside those intervals. If \(|u|=|v|\) but \(j\ne i\), one of the two same strict inequalities holds, and the same strategy applies. Finally, if \(|u|=|v|\) and \(j=i\), the selected letters match but \(u\ne v\); therefore one of the corresponding side words differs, and both side lengths are at most \(t\). Again the induction hypothesis applies. Every response outside the selected corresponding interval loses preservation of order with respect to the first selected points, so the restricted strategy is valid. This proves pairwise distinction at rank \(q\).

A finite family of words can be separated by a rank-\(q\) sentence whenever distinct words in the family are pairwise \(q\)-inequivalent: for each accepted word and each rejected word choose one distinguishing sentence, reverse its polarity as required, conjoin these for an accepted word and disjoin over accepted words. None of these Boolean operations raises quantifier rank. When a side of the partition is empty, use a rank-zero tautology or contradiction. As the ball \(\Sigma^{\le N}\) is finite, choosing \(q=\lceil\log_2(N+1)\rceil\) ensures \(N\le T_q\), proving the universal upper bound for every \(L\).

For optimality of the radius, we use the standard sharp finite-linear-order lemma: if \(m,n\ge T_q\), the monochromatic words \(a^m\) and \(a^n\) satisfy \(a^m\equiv_q a^n\). For clarity, this follows by the usual interval invariant. With \(r\) rounds left, the selected points partition both orders into corresponding gaps which are either of equal length below \(T_r\) or both have length at least \(T_r\). Initially both single gaps are long. A move in an equal short gap is mirrored at the same offset. A move in a long gap is answered so that the two new gaps are either equal short or both have length at least \(T_{r-1}\). This is possible because \(T_r=2T_{r-1}+1\): when the chosen point is within \(T_{r-1}\) places of an endpoint, duplicate that offset; otherwise select a point with \(T_{r-1}\) places on each side. All letter predicates agree. At \(r=0\), the pebble map is a partial isomorphism. In particular, \(a^{T_q}\equiv_q a^{T_q+1}\), even though the two words have different lengths.

For the parity language fix \(N\ge1\) and put \(s=\lceil\log_2(N+1)\rceil-1\). Then \(2^s\le N\), and both unary words \(a^{2^s-1}\) and \(a^{2^s}\) lie in the horizon. They have opposite length parity but agree on sentences of rank at most \(s\). When \(s=0\), this last statement follows simply because rank-zero sentences cannot distinguish the empty word from a one-letter word; for \(s\ge1\), it is the sharp-order lemma. Therefore \(\rho_E(N)\ge s+1=\lceil\log_2(N+1)\rceil\), matching the upper bound. This completes the proof.

## Verification
The included `checker.py` is a standalone Python 3 program, requiring only the standard library; run `python3 checker.py`. It independently computes exact coloured-word types through rank three from recursive vertex characters and compares them with direct two-sided Ehrenfeucht–Fraïssé game recursion on every pair of binary words of lengths at most four (2,883 game comparisons). It checks injectivity at ranks one, two, three through the cutoffs one, three and seven on all binary words through length eight; exact unary-order truncation through rank six on lengths up to 64; and the even-language horizon formula for horizons one through 63. The recorded successful output is:

`SHARP_FO_WORD_HORIZON_CHECKS_OK direct_game_comparisons= 2883 binary_word_lengths_through= 8 unary_lengths_through= 64 verified_ranks=1..6`

These finite checks are corroboration, not a proof for all horizons or alphabets. The inductive game argument above supplies the unbounded statement.

## Relationship to prior work
Bazarova and Alpay (2026) introduced this finite-horizon rank profile, proved a universal upper bound \(\rho_L(N)\le\lceil\log_2N\rceil+4\) and established that non-aperiodic regular languages have logarithmic profiles up to a language-dependent additive constant. They did **not** state the exact universal envelope or identify a single regular language attaining it at every horizon. The present exact result sharpens their additive upper bound to the optimal finite cutoff; it does not replace their algebraic dichotomy.

The sharp \(2^q-1\) equivalence threshold for *monochromatic* finite linear orders is classical, and is also recalled by Mwesigye and Truss (2011). Their more general coloured-order character recursion is compatible with the present finite calculation; neither their inspected general results nor the later work on optimal representatives (2017) states the exact universal all-colour horizon bound. A published note classifying the *one-red* subfamily similarly treats a restricted family rather than arbitrary coloured words and all-language profiles. The key additional step here is that all coloured words in the entire ball of size at most \(2^q-1\) have distinct rank-\(q\) types, which converts a classical lower-bound witness into a sharp all-language statement.

## Limitations
There is no claim about minimum formula length or size: the separating sentences may be extremely large. This theorem does not determine the individual finite-horizon profile of every regular language, classify all long-word rank types, or extend without modification to restricted-variable, alternation-bounded, arithmetic-enriched, or successor-only logics. Existing work on finite coloured orders or an uninspected earlier thesis could implicitly contain the all-colour separation lemma; the priority comparison is best-knowledge rather than an independent historical certification.

## References
1. M. Bazarova and F. Alpay, *Finite-Horizon First-Order Rank Profiles of Regular Languages*, arXiv:2604.27024, submitted 29 April 2026. https://arxiv.org/abs/2604.27024
2. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, *Order* 28 (2011), 387–397; published online 7 September 2010. DOI: 10.1007/s11083-010-9178-9.
3. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, arXiv:1705.04632 (2017).
4. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004, Chapter 3.
