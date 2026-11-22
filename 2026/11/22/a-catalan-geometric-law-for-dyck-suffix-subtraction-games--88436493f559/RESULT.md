# A Catalan–geometric law for Dyck-suffix subtraction games

## Finding

Let the alphabet be \(\{a,b\}\). In the normal-play word subtraction game, a move deletes a nonempty suffix that is a Dyck word, with \(a\) interpreted as an upstep and \(b\) as a downstep. Every finite word \(w\) has a unique representation
\[
w=u d_1d_2\cdots d_k,
\]
where \(u\) has no nonempty Dyck suffix and each \(d_i\) is a **primitive Dyck word** (strictly positive balance at all proper nonempty prefixes). The Sprague–Grundy number is precisely \(G(w)=k\), not just its zero/nonzero outcome.

Write \(C_m=\binom{2m}{m}/(m+1)\) for the Catalan numbers and
\[
D(z)=\sum_{m\ge1}C_{m-1}z^{2m}=\frac{1-\sqrt{1-4z^2}}2.
\]
The complete bivariate counting series (formal power series in \(z\), polynomial coefficients in \(t\)) is
\[
F(z,t)=\sum_{w\in\{a,b\}^*} z^{|w|}t^{G(w)}
=\frac{1+\sqrt{1-4z^2}}{2(1-2z)\left(1-\frac t2(1-\sqrt{1-4z^2})\right)}.
\]
In particular, for every integer \(n\ge1\),
\[
\#\{w\in\{a,b\}^n:G(w)=0\}
=2^{n-1}+\binom{n-1}{\lfloor(n-1)/2\rfloor};
\]
for \(n=0\), the single empty word is losing. For each \(n\ge0\), the maximum possible nimber is \(\lfloor n/2\rfloor\). At even \(n=2k\ge2\), the unique maximizer is \((ab)^k\); at odd \(n=2k+1\ge1\), the two maximizers are \(a(ab)^k\) and \(b(ab)^k\). Finally, if \(W_n\) is uniformly random among all \(2^n\) binary words of length \(n\), then, for every fixed integer \(k\ge0\),
\[
\lim_{n\to\infty}\Pr(G(W_n)=k)=2^{-k-1}.
\]

## Assumptions and scope

A *Dyck word* is a balanced word in \(\{a,b\}^{2m}\), with \(m\ge0\), whose every left-to-right prefix has nonnegative difference between \(a\)- and \(b\)-counts. A *primitive Dyck word* is a nonempty Dyck word whose proper nonempty prefixes have strictly positive balance. Only nonempty Dyck words may be removed. Every move removes a contiguous **suffix**, rather than a scattered subsequence, factor, or prefix. Normal-play impartial rules apply; the empty word has Grundy number zero. All conclusions concern arbitrary finite binary words, not just Dyck positions.

## Proof

**Canonical factorization and options.** If \(w\) has no nonempty Dyck suffix, put \(u=w\) and \(k=0\). Otherwise choose its longest Dyck suffix \(v\), leaving \(w=uv\); by maximality, \(u\) has no nonempty Dyck suffix. Every nonempty Dyck word decomposes uniquely at its zero-balance return times into primitive Dyck components \(v=d_1\cdots d_k\). Suppose a nonempty Dyck suffix of \(w\) begins inside some primitive component \(d_i\). The remaining proper suffix of \(d_i\) has strictly negative balance (since the proper prefix to its left has strictly positive balance), so appending the subsequent whole balanced components cannot restore zero balance. Thus a Dyck suffix begins only at a component boundary. It cannot begin to the left of \(v\), by maximality of \(v\). Accordingly the legal moves lead to precisely
\[
u,\quad u d_1,\quad\ldots,\quad u d_1\cdots d_{k-1}.
\]
Those words have canonical component counts \(0,1,\ldots,k-1\), respectively: if a longer Dyck suffix emerged after truncation, appending the removed Dyck components would produce a longer Dyck suffix of \(w\), a contradiction. Induction on length, using the mex definition, now gives \(G(w)=\operatorname{mex}\{0,\ldots,k-1\}=k\).

**Exact enumeration.** The primitive Dyck words of length \(2m\) are exactly \(aDb\) with \(D\) a Dyck word of length \(2m-2\), hence are counted by \(C_{m-1}\). If \(B(z)\) counts cores \(u\) with no nonempty Dyck suffix, the canonical decomposition and the geometric series of primitive components imply
\[
\frac{1}{1-2z}=\frac{B(z)}{1-D(z)},\qquad
B(z)=\frac{1-D(z)}{1-2z}.
\]
Marking each primitive component by \(t\) gives \(F(z,t)=B(z)/(1-tD(z))\), proving the displayed formula.

**Losing language and its count.** The core language is exactly the empty word, all nonempty words ending in \(a\), and nonempty words ending in \(b\) whose final running balance is a strict new minimum. Indeed, any Dyck suffix ends in \(b\). If a word ends in \(b\), a nonempty Dyck suffix exists exactly when the final running balance has been visited earlier: take its last preceding visit; every intermediate balance is strictly larger, since otherwise an additional visit would occur before the end. Because each step changes balance by one and the last step is negative, failure to revisit the final height is equivalent to a strict new minimum. Words ending in \(a\) number \(2^{n-1}\). For the other cores, reverse the word: the reversed walk must have strictly negative height at **every** positive time. Its first letter must be \(b\), and the remaining \(n-1\) steps are an ordinary simple walk whose cumulative heights never become positive. The reflection principle counts these by \(\binom{n-1}{\lfloor(n-1)/2\rfloor}\). The two sets are disjoint, giving the count. The core language is deterministic one-counter (track height above the running minimum and whether the final letter makes a strict new minimum) and nonregular: its intersection with \(a^+b^+\) is \(\{a^ib^j:i,j\ge1,\ j>i\}\), which is nonregular by the pumping lemma.

**Sharp maximum.** Every primitive Dyck component has length at least two. Thus \(k\le\lfloor n/2\rfloor\). Equality at even positive length forces an empty core and every component to equal \(ab\). Equality at odd length forces a one-letter core (either \(a\) or \(b\)) followed by the same \(ab\) components. These are all possible cases.

**Limit law.** Couple all uniform random words as finite right-to-left prefixes of an infinite independent fair binary stream. Reading such a word from right to left, a primitive Dyck suffix corresponds to a walk excursion that first steps down, stays strictly below zero until returning to zero, and then starts the next excursion. At zero, an upstep (probability \(1/2\)) prevents any further Dyck suffix, while a downstep (probability \(1/2\)) starts an excursion which returns almost surely by recurrence of the one-dimensional symmetric walk. By the strong Markov property, the number of complete excursions before the first upstep at zero is geometric with probabilities \(2^{-k-1}\). The finite-prefix Grundy counts converge almost surely to this finite excursion count; their one-dimensional distributions consequently converge.

## Verification

`verify_bruteforce.py` independently enumerates all \(8191\) binary words of lengths zero through twelve, computes legal moves literally, recursively obtains their mex values, and checks the factorization, losing criterion, length counts, and maximizing words. `verify_series.py` independently implements the exact Catalan renewal recurrence through length seventy and checks all coefficients' total counts, losses, and maximal nimbers; together the tests use only Python's standard library. Their recorded outputs are embedded alongside the programs. These finite checks are consistency tests; the arguments above establish the claims for all lengths.

## Relationship to prior work

Inoue and Inazu, *Word Subtraction Games* (first public release 6 November 2026, arXiv:2611.09157v1), define the suffix-deletion framework and discuss finite, regular and some context-free subtraction sets. Their result for regular subtraction sets implies regular languages for fixed Grundy levels. The Dyck move language here is nonregular, so that result does not imply the present counting theorem. The paper identifies Dyck words as losing positions of a distinct two-sided prefix/suffix game with regular move sets; it does **not** use all nonempty Dyck words as the sole suffix-deletion move set. Its discussion of full Grundy functions does not supply this nimber classification or its exact Catalan/geometric distributions. Previous work on ordinary Dyck enumeration supplies the Catalan numbers, but not this game-theoretic correspondence.

## Limitations

This is an exact result for one specified binary, one-sided, normal-play game. It does not classify games with arbitrary context-free subtraction sets, nor misère play, nor two-sided deletion. Independence of review has not been established; searches and inspected sources do not exclude an unindexed earlier equivalent. Asymptotic convergence here concerns the uniform iid binary measure only, not nonuniform or correlated sources.

## References

1. Yusuke Inoue and Hiroki Inazu, *Word Subtraction Games*, arXiv:2611.09157v1 (publicly posted 6 November 2026), https://arxiv.org/abs/2611.09157.
2. Richard P. Stanley, *Enumerative Combinatorics*, Vol. 2, Cambridge University Press, 1999. Classical Catalan-number and Dyck-path facts.
3. J. H. Conway, *On Numbers and Games*, Academic Press, 1976. Normal-play impartial-game mex definitions.
