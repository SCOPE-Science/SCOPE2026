# Subsequence universality in adjacency-distinct words: exact enumeration and renewal laws

## Finding

Fix an integer \(q\ge 2\), a labeled alphabet \(\Sigma\) of size \(q\), and the *adjacency-distinct* (also called Smirnov) language
\[
\mathcal P_q=\{w\in\Sigma^*:w_i\ne w_{i+1}\text{ at every adjacent pair}\}.
\]
For \(w\in\mathcal P_q\), let \(\iota(w)\) be the largest \(k\ge0\) such that every \(k\)-letter word over the **entire fixed alphabet** \(\Sigma\) occurs as a scattered subsequence of \(w\). Put
\[
a_q(n,k)=\#\{w\in\mathcal P_q:|w|=n,\ \iota(w)=k\}.
\]
The empty word contributes \(a_q(0,0)=1\).

Set
\[
D_q(z)=\prod_{h=0}^{q-2}(1-hz),\qquad
C_q(z)=\frac{(q-1)!z^{q-1}}{D_q(z)},
\]
and
\[
H_q(z)=\sum_{j=1}^{q-1}\frac{(q-1)!}{(q-j)!}\,
\frac{z^{j-1}}{\prod_{h=0}^{j-1}(1-hz)}.
\]
Empty products equal one. Then the **complete length–universality-index distribution**, for all integers \(q\ge2\), is the rational formal series
\[
\boxed{\sum_{n,k\ge0}a_q(n,k)z^nu^k
=\frac{1+qzH_q(z)+uzC_q(z)}{1-u(q-1)zC_q(z)}.}
\tag{1}
\]
For example, the ternary and quaternary specializations are
\[
F_3(z,u)=\frac{1+2z+3z^2+2uz^3}{1-z-4uz^3},\qquad
F_4(z,u)=\frac{1+z+2z^2+8z^3+6uz^4}{1-3z+2z^2-18uz^4}.
\]

Every \(k\)-universal word has length at least \(qk\). For \(k\ge1\), the exact number of shortest such adjacency-distinct words is
\[
\boxed{a_q(qk,k)=q!\bigl((q-1)(q-1)!\bigr)^{k-1}.}
\tag{2}
\]
For \(q=2\), every nonempty word in the language is alternating, and its index is \(\lfloor n/2\rfloor\). For every \(q\ge3\), however, **all** pairs \((n,k)\) with \(n\ge qk\) are attained (including \(k=0\)), and no pair with \(n<qk\) is attained.

There is also an exact random-word limit law. Choose the first letter uniformly from \(\Sigma\), then at every step choose uniformly among the \(q-1\) letters different from the previous one. Write \(W_n\) for the length-\(n\) prefix, and set
\[
\mu_q=1+(q-1)\sum_{j=1}^{q-1}\frac1j,\qquad
v_q=(q-1)^2\sum_{j=1}^{q-1}\frac1{j^2}-(q-1)\sum_{j=1}^{q-1}\frac1j.
\]
Under the natural infinite-prefix coupling,
\[
\boxed{\frac{\iota(W_n)}n\longrightarrow\frac1{\mu_q}}
\quad\text{almost surely},
\tag{3}
\]
and, for each fixed \(q\ge3\),
\[
\boxed{\frac{\iota(W_n)-n/\mu_q}{\sqrt n}
\ \xrightarrow{\mathrm d}\ \mathcal N\!\left(0,\frac{v_q}{\mu_q^3}\right).}
\tag{4}
\]
For \(q=2\), \(v_q=0\) and the index is the deterministic \(\lfloor n/2\rfloor\). In particular, for \(q=3\), the density is \(1/4\) and the limiting variance coefficient is \(1/32\).

## Assumptions and scope

All word counts use **labeled** symbols, not equivalence classes under alphabet permutations. The universe of requested subsequences is \(\Sigma^k\), not \(\operatorname{alph}(w)^k\). The variables \(z,u\) are formal markers of length and exact universality index, respectively. The asymptotic assertions hold for each fixed alphabet size \(q\), not uniformly in a growing alphabet. There is no restriction beyond adjacent inequality, and the empty word is included only in the generating function.

## Proof

**1. Greedy arches give exactly the index.** Read any word from left to right. Close an *arch* at the first position where all \(q\) alphabet letters have been seen since the previous closure, then reset the seen set. The final incomplete suffix uses fewer than \(q\) letters. If there are \(r\) complete arches, any requested length-\(r\) subsequence can be formed by choosing its successive symbols in successive arches. Conversely, choose in each completed arch the letter that first appears at that arch's **last** position, and in the remaining suffix choose an absent letter. The concatenation of these \(r+1\) selected letters cannot be a subsequence: its first selected letter can occur no earlier than the end of the first arch, and inductively the subsequent selected letters force their choices to the ends of successive arches; its final selected letter is absent from the remainder. Thus \(\iota(w)=r\). This also reconstructs the standard greedy-arch characterization without requiring a computation of all subsequences.

**2. The adjacency-distinct state collapse is exact.** After at least one letter, let \(s\in\{0,1,\ldots,q-1\}\) be the number of different symbols seen since the latest arch closure (\(s=0\) immediately after a closure). The last letter is remembered only in the sense that the next one must be different; when \(s\ge1\) that last letter lies among the \(s\) seen letters. Thus: from \(s=0\) there are \(q-1\) choices going to \(1\); from \(1\le s<q-1\) there are \(s-1\) choices keeping \(s\) and \(q-s\) choices going to \(s+1\); from \(s=q-1\) there are \(q-2\) choices staying and one completing an arch and going to \(0\). Crucially these counts depend only on \(s\), not on the identities or order of the letters. At the first position there are \(q\) choices, all leading to \(s=1\).

**3. Solve the state equations.** Let \(R_s(z,u)\) count all possible continuations of a nonempty prefix in state \(s\), including the empty continuation, with \(u\) marking any newly completed arches. The exact equations are
\[
\begin{aligned}
R_0&=1+(q-1)zR_1,\\
(1-(s-1)z)R_s&=1+(q-s)zR_{s+1}
\quad(1\le s\le q-2),\\
(1-(q-2)z)R_{q-1}&=1+uzR_0.
\end{aligned}
\]
Successive elimination gives \(R_1=H_q+uC_qR_0\), by multiplying the exact transition weights above. Hence
\[
R_0=\frac{1+(q-1)zH_q}{1-u(q-1)zC_q}.
\]
A word is either empty or starts with any of \(q\) letters, so \(F_q=1+qzR_1\). Inserting \(R_0\) and canceling the two mixed \(u z^2H_qC_q\) terms yields exactly equation (1). Since every recurrence has a constant-term-one denominator, all manipulations are valid in formal power series, with no convergence assumption.

**4. Extremal counts and sharp support.** Every arch contains at least \(q\) letters, so \(n\ge qk\). At equality there are exactly \(k\) arches, each a permutation of all letters and no residual suffix. The first block has \(q!\) choices. Given the preceding final letter, each subsequent permutation has \((q-1)q! / q=(q-1)(q-1)!\) choices for a different initial letter, proving equation (2). With two letters, adjacent inequality forces strict alternation and index \(\lfloor n/2\rfloor\). For \(q\ge3\), form any \(k\) successive full arches of minimum length, except extend the final arch by any prescribed number of letters: before its sole last unseen letter, alternate two already-seen distinct letters. This yields every \(n\ge qk\) with exactly \(k\) arches. For \(k=0\), alternate just two letters indefinitely, leaving at least one alphabet symbol unseen.

**5. Independent arch lengths and renewal limit.** Under uniform random admissible extensions, after the first letter of an arch the number of additional steps until the number of distinct seen symbols grows from \(s\) to \(s+1\) is geometric with success probability \((q-s)/(q-1)\), for \(1\le s\le q-1\), independently across stages. Thus each whole arch length has the distribution
\[
L=1+\sum_{s=1}^{q-1}G_s,\qquad
G_s\sim\operatorname{Geom}\!\left(\frac{q-s}{q-1}\right),
\]
where the geometric variable counts the successful draw and the summands are independent. At each arch boundary, letter-label symmetry makes the conditional distribution of the next whole-arch length the same, regardless of the preceding last letter; the successive lengths are therefore independent and identically distributed, including the first arch. Direct geometric moments give \(\mathbb E L=\mu_q\) and \(\operatorname{Var} L=v_q\) exactly. Since the arch count is the renewal counting process \(\max\{k:L_1+\cdots+L_k\le n\}\), the strong law and the renewal central limit theorem give equations (3) and (4). For \(q\ge3\), the length law has span one, positive variance, and exponential tails; for \(q=2\) it is the constant two.

## Verification

The included `verify.py` uses only Python's standard library. Run `python3 verify.py`. It checks the independent exact rational polynomial identity against the collapsed-state dynamic programming coefficients for every \(2\le q\le8\) and \(0\le n\le54\), checks those coefficients against brute-force enumeration of adjacency-distinct words, and separately tests the greedy index against direct testing of all possible subsequences on smaller words. It also tests the shortest-word formula, sharp support, and rational-log-derivative moment identities. The observed output is:

```
VERIFY_OK q=2..8 recurrence_n=0..54 coefficient_cells= 2064 exhaustive_proper_words= 79497 direct_subsequence_tests= 9771
```

These are finite sanity checks; the infinite-domain assertions follow from the five proof steps, not extrapolation from enumerated cases.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka (2020) establish the scattered-subsequence universality framework and the arch-factorization method. Adamson (2023) gives algorithms for counting and ranking unrestricted universal words, and Adamson, Fleischmann, Huch, Koß, Manea and Nowotka (2023) give general algorithms for universality and counting in regular languages. Those results make the constrained problem algorithmically approachable; the inspected sections do not provide equation (1) for the adjacency-distinct language across **all** alphabet sizes, the exact shortest-word count (2), the complete support dichotomy, or the renewal-index limit law (3)–(4). The present derivation exploits full alphabet symmetry to collapse an otherwise exponentially large seen-letter state to the scalar \(s\).

The expectation of a single arch is also interpretable as the classical cover time of a random walk on a loopless complete graph, so the stand-alone first-moment identity is not claimed as a new probability theorem. The jointly resolved enumeration, universal-length support, and complete-arch fluctuation law are the substantive statement.

## Limitations

The closed form relies on a uniform complete alphabet with the **same** prohibition against immediate repetition for every symbol. It does not claim a comparable scalar-state formula for nonuniform transition matrices, arbitrary forbidden adjacent pairs, or alphabets growing with word length. The literature search does not prove global uniqueness: an unindexed explicit formulation equivalent to equation (1) remains possible. No external independent proof audit is asserted.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first publicly posted 2020-03-10. https://arxiv.org/abs/2003.04629
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, first publicly posted 2023-04-10. https://arxiv.org/abs/2304.04583
3. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, first publicly posted 2023-11-17. https://arxiv.org/abs/2311.10658
