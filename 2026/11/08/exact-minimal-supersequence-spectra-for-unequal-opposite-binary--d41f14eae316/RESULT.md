# Exact minimal-supersequence spectra for unequal opposite binary runs

## Finding

For arbitrary **distinct positive integers** \(a,b\), put \(A=0^a1^b\) and \(B=1^b0^a\). Let \(\mathcal M_{a,b}\) be the set of words containing both as scattered subsequences, but containing no *proper* scattered subsequence with that property. For any integer \(t\), the exact length spectrum is

\[
\#\{w\in\mathcal M_{a,b}:|w|=2(a+b)-t\}
=\mathbf 1_{1\le t\le b}\binom{a+b-t-1}{a-1}^{2}
+\mathbf 1_{1\le t\le a}\binom{a+b-t-1}{b-1}^{2}.
\]

All other lengths have zero members. Precisely one word attains the shortest length \(2(a+b)-\max(a,b)\), while precisely \(2\binom{a+b-2}{a-1}^{2}\) attain the longest length \(2(a+b)-1\). At the central sharing parameter \(t=\min(a,b)\), the spectrum changes from a single constructive branch to two: for \(t>\min(a,b)\), only the branch sharing the more frequent symbol survives, whereas for \(1\le t\le\min(a,b)\), both branches occur. Every intermediate integer length occurs.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); words are linear and finite. A pattern \(p\) is a *scattered subsequence* of \(w\) when an order-preserving choice of positions in \(w\) spells \(p\). A *minimal common supersequence* here is inclusion-minimal under subsequence deletion, **not** merely a shortest common supersequence. It suffices to check the deletion of every single position, since any proper subsequence is reachable by successive single-position deletions and the common-supersequence property is upward closed.

For the two disjoint constructive types below, a parameter \(t\) is an integer satisfying the indicated inequalities. Word concatenation is written without an operator. A binomial coefficient with the displayed in-range parameters has its usual integer meaning.

**Type I:** choose \(1\le t\le b\); independently choose \(U,V\) having exactly \(a\) zeros and \(b-t\) ones each, with the *last* symbol of \(U\) equal to \(0\) and the *first* symbol of \(V\) equal to \(0\). Then
\[w=U1^tV.\]

**Type II:** choose \(1\le t\le a\); independently choose \(U,V\) having exactly \(a-t\) zeros and \(b\) ones each, with the *last* symbol of \(U\) equal to \(1\) and the *first* symbol of \(V\) equal to \(1\). Then
\[w=U0^tV.\]

## Proof

**1. Positionwise essentiality and count dichotomy.** Denote by \(Z\) and \(O\) the numbers of zeros and ones in a minimal common supersequence \(w\). A zero can be essential for \(A\) only if it belongs to the first \(a\) zeros of \(w\): deleting a later zero leaves those \(a\) zeros untouched, and hence the greedy earliest embedding of \(A\) remains. A zero can be essential for \(B\) only if it belongs to the last \(a\) zeros. Similarly an essential one for \(A\) must be among the last \(b\) ones and an essential one for \(B\) among the first \(b\) ones. Since every position is essential to at least one input, \(Z\le 2a\) and \(O\le 2b\).

If \(Z<2a\) and \(O<2b\), any embeddings of \(A\) and \(B\) share a zero and share a one. In \(A\), the shared zero must precede the shared one; in \(B\), the shared one must precede the shared zero. This is impossible. Thus \(Z=2a\) or \(O=2b\).

They cannot both be equalities. Write \(z_1<\cdots<z_{2a}\) and \(o_1<\cdots<o_{2b}\) for the corresponding positions. Essentiality of all the *last* \(b\) ones for \(A\) forces \(o_b<z_a\): otherwise \(b+1\) ones would be available after \(z_a\), so some last-half one could be removed without destroying \(A\). Essentiality of all the *last* \(a\) zeros for \(B\), by the symmetric argument, forces \(z_a<o_b\). Contradiction. Consequently **exactly one** of \(Z=2a\) and \(O=2b\) holds.

**2. Classification when \(Z=2a\).** Put \(O=2b-t\); since \(b\le O<2b\), \(1\le t\le b\). Any embedding of \(A\) must use \(a\) zeros before the last \(b\) ones, giving \(z_a<o_{b-t+1}\). Any embedding of \(B\) must use the first \(b\) ones before \(a\) zeros, giving \(o_b<z_{a+1}\). Thus the \(t\) ones \(o_{b-t+1},\ldots,o_b\) lie strictly between consecutive zeros \(z_a,z_{a+1}\).

If \(b-t>0\), the final \(b-t\) ones can be essential only for \(A\), because they lie beyond the first \(b\) ones. In particular, deletion of \(o_{b+1}\) must destroy \(A\). If \(o_{b-t}\) also followed \(z_a\), at least \(b+1\) ones would follow \(z_a\), and deleting \(o_{b+1}\) would not destroy \(A\); therefore \(o_{b-t}<z_a\). Symmetrically, the initial \(b-t\) ones can be essential only for \(B\), so deletion of \(o_1\) must destroy \(B\). It follows that \(z_{a+1}<o_{b+1}\). When \(b-t=0\), both inequalities involving absent outside ones are vacuous. In all cases the word has uniquely the Type-I form \(U1^tV\), where \(U\) consists of the first \(a\) zeros and first \(b-t\) ones, and \(V\) comprises the remaining positions; \(U\) ends in zero and \(V\) begins in zero.

**3. Classification when \(O=2b\).** Exchange the letters and interchange the two input words. The preceding argument yields Type II, with \(1\le t\le a\). The two types cannot intersect, since Type I has exactly \(2a\) zeros and fewer than \(2b\) ones, while Type II has exactly \(2b\) ones and fewer than \(2a\) zeros.

**4. Sufficiency.** In Type I, \(A\) must use all \(a\) zeros in \(U\) and all \(b\) ones in the central run and \(V\); \(B\) must use all \(b\) ones in \(U\) and the central run and all \(a\) zeros in \(V\). Thus every position is needed for at least one input, and deleting it destroys that input. Type II is symmetrical. Both forms are therefore minimal common supersequences.

**5. Counting and endpoints.** The number of admissible \(U\)'s in Type I is \(\binom{a+b-t-1}{a-1}\) (fix its final zero); the same count holds for \(V\) (fix its initial zero). Type II similarly contributes \(\binom{a+b-t-1}{b-1}^2\). This gives the displayed spectrum. For \(t=\max(a,b)\) and \(a\ne b\), only the longer central run is allowed, and its two outside words have no other symbol: there is one shortest word. At \(t=1\), both branches contribute \(\binom{a+b-2}{a-1}^2\), using binomial symmetry. All intermediate \(t\)'s occur because the corresponding binomial coefficients are positive.

## Verification

The accompanying standalone \(\texttt{verification/verify.py}\) checks the classification without relying on this proof. It enumerates every binary candidate directly and tests single-position deletion minimality for all \(16\) ordered parameter pairs \((a,b)\) with \(1\le a,b\le4\), including the excluded diagonal as an independent boundary check. It separately generates all interleavings, deduplicates them and filters by minimality for four larger asymmetric pairs \((1,6),(2,5),(3,5),(5,3)\). It checks every predicted length frequency and extreme count. Passing output:

\(\texttt{OPPOSITE\_RUN\_MCS\_VERIFY\_OK}\) (the final words give the checked case counts).

These are finite checks; the infinite two-parameter theorem rests on the proof above.

## Relationship to prior work

Sopp, Liyanage, Gong and Zhu (2026) give algorithms to compute and enumerate minimal common supersequences of arbitrary input pairs, rather than this closed-form two-run spectrum. Sun and Ge (2026, Section 5) characterize fixed-length minimal supersequences as primitive insertion layers and derive upper bounds, but do not give the present two-run classification or its sharp phase transition. Lin (2026, Lemma 3.1) gives a bound at each fixed excess length but no exact parameterized value. The equal-run specialization has previously been considered and is **not claimed to be new**; the present theorem's subject is the unequal-run, two-parameter classification and unique-shortest transition.

The arXiv 2022 version of Alon et al. states a general total-count bound for minimal common supersequences whose literal application is inconsistent with a directly checkable asymmetric instance: at \((a,b)=(2,3)\), this theorem counts \(24\) minimal common supersequences, whereas that version's Lemma 8 would give an upper bound \(6\). This discrepancy is reported as a source-comparison caveat; no step of the proof uses the disputed bound. It requires checking against a final corrected version before drawing bibliographic conclusions.

## Limitations

The exact formula applies to two opposite **single-transition binary** input words with positive unequal run lengths. It does not extend automatically to words with more runs, larger alphabets or more than two input strings. Finite tests are not an independent proof. A 1994/1996 treatment by Fraser and Irving (and later Middendorf) was located bibliographically, but its complete text was not accessible for comparison; an equivalent earlier formulation or unpublished table remains a priority risk. Independent mathematical review and full historical priority verification have not been performed.

## References

1. B. Sopp, A. Liyanage, M. Gong and B. Zhu (2026), *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591, https://arxiv.org/abs/2603.22591 (first posted 2026-03-23).
2. Y. Sun and G. Ge (2026), *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822, https://arxiv.org/abs/2606.25822.
3. A. D. Lin (2026), *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, https://arxiv.org/abs/2609.26650.
4. N. Alon, G. Bourla, B. Graham, X. He and N. Kravitz (2022, arXiv version), *Logarithmically Larger Deletion Codes of All Distances*, arXiv:2209.11882, https://arxiv.org/abs/2209.11882.
5. R. W. Irving and C. B. Fraser (1994), *Maximal Common Subsequences and Minimal Common Supersequences*, CPM 1994, Lecture Notes in Computer Science 807, pp. 173–183, DOI 10.1007/3-540-58094-8_16 (abstract and bibliographic record only). Related: C. B. Fraser, R. W. Irving and M. Middendorf (1996), *Maximal Common Subsequences and Minimal Common Supersequences*, *Information and Computation* 124(2), 145–153.
