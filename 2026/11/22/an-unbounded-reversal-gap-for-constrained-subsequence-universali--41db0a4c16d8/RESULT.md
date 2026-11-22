# An unbounded reversal gap for constrained subsequence-universality automata

## Finding

Fix integers \(d\ge2\) and \(k\ge1\). Let \(U_k\) be the language of binary words containing **every** binary word of length \(k\) as a scattered subsequence. For a binary word \(p\), let \(\operatorname{Av}(p)\) denote the language of words with no **contiguous** occurrence of \(p\), and let \(\kappa(L)\) denote the number of states in the smallest **complete deterministic** finite automaton for \(L\). Put

\[
L^+_{d,k}=U_k\cap\operatorname{Av}(0^d1),\qquad
L^-_{d,k}=U_k\cap\operatorname{Av}(10^d).
\]

Then, for every such \(d,k\),

\[
\boxed{\kappa(L^+_{d,k})=(d+2)k+d+1,\qquad
\kappa(L^-_{d,k})=(d+2)k+2.}
\]

Since scattered-subsequence universality is invariant under word reversal, \((L^+_{d,k})^{\mathrm R}=L^-_{d,k}\). Hence the two languages have the same number of words at every length, yet their **left-to-right** deterministic state complexities differ by exactly \(d-1\). The gap is unbounded as \(d\) increases and is independent of \(k\).

## Assumptions and scope

The alphabet is fixed to \(\{0,1\}\), the words are finite, and the forbidden patterns \(0^d1\), \(10^d\) are contiguous factors, **not** forbidden scattered subsequences. A scattered subsequence may skip positions but preserves order. All parameters \(d\ge2,k\ge1\) are integers. Automata are complete, count a rejecting sink, and read left to right. The claimed minimal-state formulas do not concern nondeterministic or right-to-left automata.

An **arch** is the shortest currently unread prefix containing both letters. Repeatedly delete this arch, starting from the left, leaving a remainder containing at most one distinct letter. Write \(c(w)\) for the number of completed arches, and write \(a(w)\in\{\bot,0,1\}\) for the remainder type (\(\bot\) if the remainder is empty). Once \(c(w)\ge k\), the arch count is saturated at \(k\). The accepting condition is \(c(w)\ge k\) together with factor avoidance.

## Proof

**1. The arch criterion.** Every arch is a nonempty run of one letter followed by a single occurrence of the other letter. If there are at least \(k\) arches, choose the next requested symbol within each of the first \(k\) arches; every length-\(k\) binary pattern embeds. Conversely, if there are \(c\) arches, take the final letter of each arch, followed by a letter absent from the final remainder. The greedy leftmost embedding of these \(c+1\) letters would have to consume the last symbol of each arch in turn, and the final required letter does not occur in the remainder. Therefore it does not embed. Thus \(w\in U_k\) exactly when \(c(w)\ge k\).

The arch tracker has configurations \((c,a)\), with \(c\in\{0,\ldots,k\}\). For \(c<k\), reading a letter of a new type completes an arch; reading the first or a repeated remainder letter extends the remainder. On reaching \(c=k\), further input leaves \(c\) saturated. Combine this tracker with the familiar one-pattern factor-avoidance monitor.

**2. Avoiding \(0^d1\).** The factor monitor records the trailing-zero length \(z\in\{0,1,\ldots,d\}\), saturated at \(d\). Reading \(1\) when \(z=d\) rejects; otherwise reading \(1\) resets \(z=0\), and reading \(0\) increments/saturates \(z\). If \(c<k\) and \(z=d\), no future \(1\) is permitted, and no further full arch can occur. All such configurations have empty right language and merge with the forbidden-factor rejecting sink.

Every other reachable configuration falls in exactly one of the following disjoint groups:

| Completed arches | Remainder and zero-run data | Number |
|---|---|---:|
| \(c=0\) | \((\bot,0)\), \((1,0)\), \((0,j)\) for \(1\le j<d\) | \(d+1\) |
| \(1\le c<k\) | \((\bot,0),(\bot,1),(1,0)\), and \((0,j)\) for \(1\le j<d\) | \(d+2\) each level |
| \(c=k\) | saturated arch tracker and \(z=0,1,\ldots,d\) | \(d+1\) |
| sink | forbidden factor or unreachable completion | \(1\) |

All listed states are reachable: at each positive intermediate level use \((01)^c\) and \((10)^c\) to end an arch in either letter; append \(1\) or a legal zero run to enter the corresponding pending states. At level zero use the empty word, \(1\), and \(0^j\); at the accepting level append \(0^j\) for \(0\le j\le d\) after \((01)^k\). Therefore the number of candidate residuals is

\[
(d+1)+(k-1)(d+2)+(d+1)+1=(d+2)k+d+1.
\]

**3. Avoiding \(10^d\).** There are two kinds of legal factor-monitor states: *pre-one*, before the first \(1\) (any number of initial zeros is allowed), and a count \(t\in\{0,\ldots,d-1\}\) of zeros since the most recent \(1\). Reading a \(1\) starts/resets at \(t=0\); reading a \(0\) at \(t=d-1\) rejects. The reachable configurations are:

| Completed arches | Remainder and factor data | Number |
|---|---|---:|
| \(c=0\) | \((\bot,\mathrm{pre1}),(0,\mathrm{pre1}),(1,t=0)\) | \(3\) |
| \(1\le c<k\) | \((\bot,t=0),(\bot,t=1),(1,t=0)\), and \((0,t)\) for \(1\le t<d\) | \(d+2\) each level |
| \(c=k\) | saturated arch tracker and \(t=0,\ldots,d-1\) | \(d\) |
| sink | forbidden factor | \(1\) |

For level zero use \(\varepsilon,0,1\). For any positive level \(c\), the prefixes \((01)^c\), \((10)^c\), \((01)^c1\), and \((01)^c0^t\) reach all indicated states (the pending remainder is understood). At level \(k\), \((01)^k0^t\) reaches every legal factor state. All prefixes avoid \(10^d\), since \(d\ge2\). The candidate count is

\[
3+(k-1)(d+2)+d+1=(d+2)k+2.
\]

**4. Proof that neither count can be reduced.** Consider either candidate automaton and a nonaccepting, nonsink state with \(c<k\). Set \(r=k-c\). The shortest length of any accepted continuation from this state is exactly \(2r\) when the current remainder is empty and \(2r-1\) when its first letter has been seen. The lower bounds follow because each new full binary arch needs two letters (apart from the already-started arch); equality is reached by alternating suffixes beginning with the letter that safely completes or starts the next arch. Such suffixes can always be chosen to avoid the relevant forbidden factor because \(d\ge2\).

Consequently, different arch levels are distinguishable, empty and nonempty remainders are distinguishable, and these nonaccepting states are distinguishable from accepting states and the sink. For a fixed level and nonempty remainder, a pending \(0\) differs from a pending \(1\): with \(r\) arches still required, the continuation \(1(01)^{r-1}\) has exactly the necessary \(2r-1\) symbols to accept from a pending \(0\), but cannot complete \(r\) arches from a pending \(1\). The continuation is legal from any listed pending-zero configuration.

It remains to separate the factor-monitor states within the same level/remainder class. In the \(0^d1\)-avoiding automaton, two pending-zero configurations with trailing counts \(1\le j<t<d\) are separated by

\[
0^{d-t}1(01)^{r-1}:
\]

this continuation accepts from count \(j\), but contains a forbidden factor from count \(t\). The two empty-remainder configurations (when both exist) are separated by \(0^{d-1}1(01)^{r-1}\): it accepts from trailing count zero, but not trailing count one. The accepting factor states \(z<t\) are separated by \(0^{d-t}1\), which is legal from \(z\) and forbidden from \(t\).

In the \(10^d\)-avoiding automaton, two pending-zero configurations with counts \(1\le j<t<d\) of zeros since the last one are likewise separated by \(0^{d-t}1(01)^{r-1}\). The two empty-remainder configurations are separated by \(0^{d-1}1(01)^{r-1}\), which is legal after zero zeros since the last one but forbidden after one zero. Accepting factor states with counts \(j<t\) are separated by \(0^{d-t}\). Within level zero, pending-zero and pending-one configurations are already separated by the first-letter continuation argument.

These cases exhaust all pairs of distinct candidate states. All candidates are reachable and pairwise Myhill–Nerode distinguishable, proving both formulas.

**5. Reversal and the gap.** Reversing a binary word preserves the property of containing every length-\(k\) binary scattered subsequence, because it reverses the family of all such patterns bijectively. It also carries avoidance of \(0^d1\) to avoidance of \(10^d\). Hence the languages are reversals and are equinumerous at each word length. Subtracting their independently proved minimal-state counts yields precisely \(d-1\), which is arbitrarily large as \(d\) varies.

## Verification

The included standalone Python 3 program `verify.py` constructs the product of a greedy-arch monitor and a pattern-avoidance prefix automaton, explores its reachable states, and minimizes it by exact partition refinement. It independently verifies both formulas for \(2\le d\le13\) and \(1\le k\le16\): **384** complete automata. Separately, it compares direct pattern embedding and forbidden-factor tests against automaton acceptance in **196,584** cases with \(2\le d\le5\), \(1\le k\le3\), and lengths \(0\) through \(12\).

Run with `python3 verify.py` in a directory containing this document and the script. Both tests passed. These finite computations validate implementation and boundary conditions; the arbitrary-parameter conclusion follows from the explicit right-quotient proof above.

## Relationship to prior work

Barker et al. (2020) developed scattered-factor universality and arch-based algorithms, including repetition and circular variants. Adamson et al. (2023) studied universal words accepted by regular languages, with existence, counting, and ranking algorithms. The present languages fit their regular-restriction framework, but the claim here is the **exact smallest complete DFA size** for two explicit reversed forbidden-factor families, with an unbounded directional complexity gap. Neither paper's inspected results states these formulas or the stated reversal gap. Earlier general upper bounds for intersection of regular languages are not equality classifications for these languages.

An indexed mathematical record on prefix-sorting the \(0^d1\)-avoiding language concerns Wheeler automata for the forbidden-factor language alone, without the added universal-subsequence requirement. An earlier exact run-capped universality result forbids runs \(0^r\) or \(1^s\), rather than a zero-run **followed by a one**. These restrictions are inequivalent: arbitrary terminal zero runs remain legal here. Neither corresponding statement yields the formulas above.

## Limitations

The formulas require \(d\ge2\) and \(k\ge1\); no statement is made for other domains, other factor patterns, or nondeterministic state complexity. The result establishes exact one-way left-to-right deterministic memory in the classical state-count model, not bit-optimal data structures with arbitrary preprocessing. The mathematical proof is accompanied by finite reproducibility checks; independent certification has not been performed. Possible unindexed equivalent prior results remain a priority risk.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (first public 2020-03-10), https://arxiv.org/html/2003.04629v1.
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *\(k\)-Universality of Regular Languages*, arXiv:2311.10658v1 (first public 2023-11-17), https://arxiv.org/abs/2311.10658; ISAAC 2023, DOI:10.4230/LIPIcs.ISAAC.2023.4.
