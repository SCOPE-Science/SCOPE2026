# Exact ascending-run laws and the sharp ordinal-memory transition for integer expanding maps

## Finding
For every integer \(b\ge2\), the expanding integer-base map \(T_b(x)=bx\bmod 1\), under invariant Lebesgue measure, has an explicit law for a string of successive strict increases. Define
\[
A_j(x)=\mathbf1\{T_b^j(x)<T_b^{j+1}(x)\},\qquad j\ge0.
\]
For every integer \(n\ge1\),
\[
\boxed{\mathbb P(A_0=\cdots=A_{n-1}=1)=\frac{\binom{n+b-1}{b-2}}{(b-1)b^n}.}
\]
The process \((A_j)_{j\ge0}\) is independent fair Bernoulli for \(b=2\), whereas **for every integer \(b\ge3\) it has infinite Markov order**. Thus the memory classification across all integer expanding bases has a sharp boundary at two, despite the underlying base-\(b\) digits being independent in every case.

For \(b\ge3\), the conditional probability of another ascent after \(n\) consecutive ascents is
\[
\mathbb P(A_n=1\mid A_0=\cdots=A_{n-1}=1)=\frac{n+b}{b(n+2)},
\]
strictly decreasing to \(1/b\). For each fixed integer \(b\ge2\),
\[
\mathbb P(A_0=\cdots=A_{n-1}=1)\sim\frac{n^{b-2}}{(b-1)(b-2)!\,b^n}.
\]
In particular, the previously documented tripling-map case \(b=3\) is recovered as \((n+2)/(2\cdot3^n)\), but not counted as an independent discovery.

## Assumptions and scope
The space is \([0,1)\) with its Borel sigma algebra and normalized Lebesgue measure. \(T_b(x)=bx-\lfloor bx\rfloor\) for an integer \(b\ge2\). A sample \(x\) has the canonical nonterminating base-\(b\) expansion outside the null set of ambiguous base expansions; its digits \(D_j\in\{0,\ldots,b-1\}\) are independent and uniformly distributed. Pairs of equal successive iterates, which arise only on a null set, have no influence on these distributional identities. Finite Markov order means existence of \(r\ge0\) such that the conditional distribution of the next binary observation given any full positive-probability past depends only on its final \(r\) observations.

## Proof
1. Write \(T_b^j(x)=0.D_jD_{j+1}\ldots\) in base \(b\). Except on a null set, \(A_j=1\) exactly when the suffix beginning at position \(j\) is lexicographically smaller than the suffix beginning at \(j+1\). If \(D_j<D_{j+1}\), the comparison is immediately increasing; if \(D_j>D_{j+1}\), it is decreasing; if the two digits agree, the comparison reduces to \(A_{j+1}\). Hence \(n\) successive ascents hold if and only if \(D_0\le D_1\le\cdots\le D_{n-1}=v\) and the first future digit differing from \(v\) is greater than \(v\). The exceptional tail consisting only of \(v\)'s has probability zero.
2. For a fixed last digit \(v\), the number of weakly nondecreasing length-\(n\) words over \(\{0,\ldots,v\}\) ending at \(v\) is \(\binom{n+v-1}{n-1}\). The first future non-\(v\) digit has the uniform law on the other \(b-1\) symbols, so the chance it exceeds \(v\) is \((b-1-v)/(b-1)\). Independence of the first \(n\) digits and the tail therefore gives
\[
P_b(n)=\frac1{(b-1)b^n}\sum_{v=0}^{b-1}(b-1-v)\binom{n+v-1}{n-1}.
\]
3. The hockey-stick identity, applied twice, yields
\[
\sum_{v=0}^{b-1}(b-1-v)\binom{n+v-1}{n-1}
=\sum_{t=0}^{b-2}\binom{n+t}{n}
=\binom{n+b-1}{b-2}.
\]
This proves the formula for all integer \(b\ge2\) and \(n\ge1\). In particular, \(P_b(1)=1/2\), consistent with symmetry of consecutive iterates.
4. For \(b=2\), a run of equal digits at position \(j\) is eventually followed by the opposite digit almost surely. If \(D_j=0\) this makes the comparison increasing, and if \(D_j=1\) decreasing. Therefore \(A_j=1-D_j\) almost surely for all \(j\), and the binary observations are iid fair.
5. If \(b\ge3\), all ascent cylinders have positive probability and the exact conditional probability is
\[
\frac{P_b(n+1)}{P_b(n)}=\frac{n+b}{b(n+2)}.
\]
This varies strictly with \(n\), since the difference from \(1/b\) is \((b-2)/[b(n+2)]>0\), strictly decreasing as \(n\) grows. A stationary Markov process of any fixed order \(r\) would have the same conditional continuation probability for every all-one history of length at least \(r\), since its last \(r\) observations are identical. The observed variation contradicts finite order for every \(b\ge3\).
6. Finally, \(\binom{n+b-1}{b-2}=n^{b-2}/(b-2)!+O_b(n^{b-3})\) for fixed \(b\ge3\), with \(b=2\) exactly \(1\); substituting establishes the stated asymptotic.

## Verification
The standalone file `CHECK.py` independently constructs the exact order comparisons on the \(b^n\) branches of \(T_b^n\), isolates every rational equality boundary between successive iterates, and integrates the resulting increasing-event intervals exactly. These geometric probabilities were compared to the closed formula for all pairs \(2\le b\le7\), \(1\le n\le5\) with \(b^n\le5000\). An independently implemented combinatorial summation was compared with the formula for \(2\le b\le24\), \(1\le n\le39\), totaling 925 exact rational comparisons. Finite computation supplements, and does not prove, the quantified result; the complete proof is above.

## Relationship to prior work
Maga–Szepessy (2026) provide a recent conceptual setting for permutation entropy and ordinal partitions of measure-preserving interval maps; their generic-entropy theorems do not give this integer-base ascent process classification. Elizalde (2010) treats support and forbidden permutations of beta shifts, not the exact invariant-measure ascent-run probabilities established here. Bandt (2025) studies stationary random orders and pattern distributions, without this exact all-base deterministic construction in the inspected material. A related published tripling-map calculation already gives \(P_3(n)=(n+2)/(2\cdot3^n)\) and infinite Markov order; the new statement is a classification across **every integer base**, with the sharp iid-versus-infinite-memory boundary and varying polynomial prefactors. The tripling instance is prior work, not a separate new result.

## Limitations
These conclusions concern the binary successive-increase process, not the full ordinal-permutation process or any nonlinear/noisy observation. They do not assert that the binary process cannot have a countable-state representation, or describe general noninteger beta transformations. Historical priority for the all-base formula may reside in specialized permutation-pattern probability literature not located in the inspected sources. No independent audit has been performed.

## References
- B. Maga and S. Szepessy, *The generic behavior of permutation entropy for continuous maps*, arXiv:2611.12789v1, first posted 9 November 2026, https://arxiv.org/html/2611.12789v1.
- S. Elizalde, *Permutations and beta-shifts*, arXiv:1008.4167, first posted 24 August 2010, https://arxiv.org/abs/1008.4167.
- C. Bandt, *Ordinal Random Processes*, Entropy **27** (2025), 610, https://doi.org/10.3390/e27060610.
- *Algebraic infinite ordinal memory and exponential Markov-walk error for the tripling map*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-algebraic-infinite-ordinal-memory-and-exponential-markov-walk-er--5878a875c093 (the tripling instance is known).
