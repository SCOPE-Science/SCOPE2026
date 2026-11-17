# Parity-rigid shortest resets in a two-collapse Černý extension

## Finding
For every integer \(n\ge 2\), consider the complete deterministic automaton \(\mathcal A_n\) with state set \(Q=\mathbb Z/n\mathbb Z\) and three distinct letters \(a,b,c\) acting as follows:
\[
a(i)=i+1\pmod n,\qquad
b(n-1)=0,\qquad c(n-2)=n-1,
\]
where \(b\) and \(c\) fix every other state. Words act from left to right. The reset threshold, i.e. the minimum length of a word mapping all of \(Q\) to a singleton, is exactly
\[
\boxed{\operatorname{rt}(\mathcal A_n)=(n-2)\left\lfloor\frac n2\right\rfloor+1.}
\]
More precisely, write \(k=\lfloor n/2\rfloor\). If \(n=2k+1\) is odd, there is **exactly one** shortest reset word,
\[
\boxed{\;cb\bigl(a^{n-2}cb\bigr)^{k-1}\;}.
\]
If \(n=2k\) is even, there are **exactly two** shortest reset words,
\[
\boxed{\;b\bigl(a^{n-2}cb\bigr)^{k-1}
\quad\text{and}\quad
c\bigl(ba^{n-2}c\bigr)^{k-1}.\;}
\]
These statements include \(n=2\), when the two optimal words are \(b\) and \(c\). For odd \(n\), the optimal word resets to state \(0\); for even \(n\), the displayed words reset to states \(0\) and \(n-1\), respectively.

## Assumptions and scope
The automaton is labeled, and costs are unit length per letter. All formulas quantify over every integer \(n\ge 2\), with no parity or primality restriction. A circular interval of length \(s\), for \(1\le s\le n\), means \(\{L,L+1,\ldots,L+s-1\}\pmod n\), for some left endpoint \(L\). For \(s<n\), that endpoint is unique. Given a word \(w=f_1\cdots f_t\), write \(f_j^{-1}(S)\) for its set-theoretic preimage of the subset \(S\subseteq Q\).

## Proof
**1. Reverse preimages cannot lose states on a shortest resetting path.** Let \(w=f_1\cdots f_t\) be a shortest reset word with target \(q\). Starting with \(S_0=\{q\}\), process the letters in reverse order, forming \(S_j=f_{t-j+1}^{-1}(S_{j-1})\). The last set is \(S_t=Q\). Every set-theoretic inverse-image map is monotone: \(S\subseteq T\) implies \(f^{-1}(S)\subseteq f^{-1}(T)\). If an inverse step produced a subset of its preceding set, or left it unchanged, deleting the corresponding letter from \(w\) would still give \(Q\) as a preimage of \(\{q\}\), by monotonicity of all remaining inverse steps. This would be a shorter reset word, a contradiction. Therefore every inverse step in a shortest word must either preserve cardinality while genuinely translating its set, or strictly increase cardinality.

**2. All reverse sets are circular intervals.** The preimage of a circular interval under \(a\) is a circular interval of the same length whose left endpoint decreases by one modulo \(n\). For any subset \(S\),
\[
b^{-1}(S)=\bigl(S\setminus\{n-1\}\bigr)\cup\begin{cases}\{n-1\},&0\in S,\\\varnothing,&0\notin S,\end{cases}
\]
and
\[
c^{-1}(S)=\bigl(S\setminus\{n-2\}\bigr)\cup\begin{cases}\{n-2\},&n-1\in S,\\\varnothing,&n-1\notin S.\end{cases}
\]
For a proper circular interval, \(b^{-1}\) strictly expands the interval if and only if its left endpoint is \(0\). In that case it adds the point \(n-1\) to the left. Likewise \(c^{-1}\) strictly expands if and only if its left endpoint is \(n-1\), adding \(n-2\) to the left. All other \(b\)- or \(c\)-preimage steps are either unchanged or shrink the set, so Step 1 excludes them on a shortest reset path. Induction from \(S_0\) shows that all reverse sets are circular intervals. Every permissible reverse step, whether a rotation or an expansion, decreases the left endpoint by exactly one modulo \(n\). An expansion increases length by exactly one; a rotation keeps length unchanged.

**3. The sharp spacing bound.** Since the reverse path starts with length one and ends with length \(n\), it must contain exactly \(r=n-1\) expanding steps. If its initial left endpoint is \(L\), its consecutive pre-step endpoints are \(L,L-1,L-2,\ldots\pmod n\). Only endpoints \(0\) and \(n-1\) allow an expansion, and their labels are then forced to be \(b\) and \(c\), respectively. The possible expansion sites, traversed backwards around the cycle, occur as consecutive pairs, first \(0,n-1\), followed by a gap of \(n-2\) other endpoints, and so on. Consecutive pairs therefore repeat every \(n\) steps.

A shortest reverse path begins and ends at expanding steps: a reverse path starting with \(a^{-1}\) would correspond to a reset word ending in \(a\), whose final \(a\) could be deleted; a reverse path ending with \(a^{-1}\) corresponds to a reset word starting with \(a\), which may also be deleted because \(a(Q)=Q\). Thus the problem is to find the shortest consecutive span containing \(r\) eligible sites in the two-sites-per-\(n\) periodic pattern, with all eligible sites in that span used. If \(r=2k\), the unique shortest span begins at the first site of a pair and ends at the second site of the \(k\)-th pair; its length is \((k-1)n+2\). If \(r=2k-1\), there are exactly two shortest spans, beginning respectively at the first or second site of a pair, both of length \((k-1)n+1\). The case \(r=1\), including \(n=2\), follows with the same two possibilities. These claims also follow directly by comparing the alternating successive gaps \(1,n-1,1,n-1,\ldots\) between eligible steps. Skipping an eligible expansion cannot shorten a span with a prescribed number of expansions.

For \(n=2k+1\) this yields \((k-1)n+2=k(n-2)+1\); for \(n=2k\) it yields \((k-1)n+1=k(n-2)+1\). Hence every reset word obeys the claimed lower bound.

**4. Attainment and uniqueness.** For odd \(n=2k+1\), the unique shortest backwards expansion sequence uses \(b,c\), then \(n-2\) rotations, repeating until \(k\) pairs of expansions have been made. Reversing its letters gives \(cb(a^{n-2}cb)^{k-1}\). For even \(n=2k\), the two shortest spans produce, on reversing, \(b(a^{n-2}cb)^{k-1}\) and \(c(ba^{n-2}c)^{k-1}\). Each word is a valid inverse expansion path from its stated target to all \(n\) states, so each word resets the automaton and attains the lower bound. Since any shortest reverse path must use exactly the sites in a minimum span, and its letter is uniquely determined at every site (\(a\) outside the expansion sites; \(b\) or \(c\) at an expansion site), no other shortest reset words exist. \(\square\)

## Verification
The standalone \(\texttt{verify.py}\) implements the three transition maps independently as bitset transformations. For every \(2\le n\le15\), breadth-first search of the full subset automaton computes the exact shortest reset distance and number of shortest reset words and agrees with the theorem. For \(2\le n\le12\), the program also reconstructs and compares the complete sets of shortest words. A separate endpoint/event enumeration checks the optimal span length and multiplicity for \(2\le n\le50\). Running \(\texttt{python3 verify.py}\) returns `VERIFY_OK`. These finite checks are diagnostics and not substitutes for the argument for all \(n\).

## Relationship to prior work
The Černý automaton with only \(a,b\) has reset threshold \((n-1)^2\). Adding \(c\) here preserves the cyclic permutation and introduces a second adjacent rank-\((n-1)\) idempotent, but reduces the exact threshold to roughly one half of \(n^2\). De Bondt, Don and Zantema (arXiv:1609.06853, Sections 3 and 5) analyze extensions of Černý automata and establish that a nontrivial extension cannot retain the full Černý threshold when \(n>3\); they do not give this particular all-\(n\) threshold and classification of shortest words. Zhu (arXiv:2407.08135, Theorems 1.4 and 2.7) proves broader quadratic upper bounds for automata with defect-one letters and a transitive permutation group, not this sharp family-specific value. Gonze et al. (arXiv:1704.04047, Section 2.1) study an extension using one adjacent **transposition** in addition to a collapsing letter; that third letter is a permutation, unlike \(c\) here, and their resulting reset bounds do not imply the present formula. Published results on early rank compression for the two-letter Černý automaton concern a different alphabet. A literature search cannot exclude an unindexed equivalent formulation.

## Limitations
The classification applies only to the specified second collapse and unit letter costs, not to arbitrary three-letter extensions or weighted reset lengths. It gives optimal reset words but not the entire transformation semigroup. Computational tests cover only finite state sizes; the universal statement is proved by inverse-interval reasoning. The originality comparison is literature-based and is not an independent expert audit.

## References
1. Y. Zhu, *A quadratic upper bound on the reset thresholds of synchronizing automata containing a transitive permutation group*, arXiv:2407.08135 (first public 2024-07-11), https://arxiv.org/html/2407.08135v1 .
2. M. de Bondt, H. Don and H. Zantema, *Slowly synchronizing automata with fixed alphabet size*, arXiv:1609.06853 (first public 2016-09-22), https://arxiv.org/abs/1609.06853 .
3. F. Gonze, V. Gusev, B. Gerencsér, R. Jungers and M. Volkov, *On the interplay between Babai and Černý's conjectures*, arXiv:1704.04047 (first public 2017-04-13), https://arxiv.org/html/1704.04047v2 .
