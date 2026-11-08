# Exact output-switch distributions for connected binary bireversible transducers

## Finding

For every integer \(n\ge1\), label the states \(Q=\{0,\ldots,n-1\}\) and fix the ordered input/output alphabet \(\{0,1\}\). A complete invertible reversible Mealy transducer is specified by two permutations \(A,B\in S_n\) (next-state maps on inputs \(0,1\)) and a subset \(S\subseteq Q\) (exactly the states that swap the output letters). Call it *bireversible* when the inverse Mealy transducer is also reversible. Let \(e_{n,k}\) count labeled bireversible machines with \(|S|=k\), and let \(c_{n,k}\) count those among them whose underlying transition digraph is strongly connected.

The complete output-switch enumerator is
\[
E_n(y)=\sum_{k=0}^{n}e_{n,k}y^k=(n!)^2\sum_{k=0}^{n}y^k.
\]
In particular, exactly \((n!)^2\) such machines have each possible number of switching states; the probability of bireversibility among uniformly sampled invertible reversible machines is \((n+1)/2^n\). Conditional on bireversibility, the random variable \(|S|\) is exactly uniform on \(\{0,\ldots,n\}\).

The connected machines have an equally exact, but generally nonuniform, complete generating series:
\[
\boxed{\quad\sum_{n\ge1}\sum_{k=0}^n c_{n,k}\frac{z^n}{n!}y^k
 =\log\!\left(\sum_{m\ge0}m!z^m\sum_{j=0}^m y^j\right).\quad}
\]
All series are **formal** in \(z\) with polynomial coefficients in \(y\); no convergence of the factorial series is asserted. This determines the count for every state number and every output-switch number.

For example, the connected switch-count vectors for \(n=2,3,4,5\), in order \(k=0,\ldots,n\), are respectively
\[
(3,2,3),\quad(26,18,18,26),\quad(426,312,300,312,426),
\quad(11064,8520,8160,8160,8520,11064).
\]
These are machine counts with labeled states and labeled input/output symbols, **not** counts of state-isomorphism classes, minimized transducers, or the generated groups.

## Assumptions and scope

The state set \(Q\) and alphabet \(\{0,1\}\) are fixed as labeled sets; different transition/output tables are distinct, including isomorphic tables. There is no distinguished start state. Every state has exactly one transition for each input, and each output map is either identity or the binary swap. Reversibility means that \(A\) and \(B\) are permutations. Bireversibility means invertibility, reversibility, and reversibility of the inverse transducer. Strong connectivity refers only to the directed graph with edges \(q\to A(q)\) and \(q\to B(q)\), not to transitivity of the generated group on infinite binary words. The empty machine occurs solely as the identity term of the formal generating function.

## Proof

**1. Characterization.** Given a state \(q\), its output on input \(x\) is \(x\oplus\mathbf 1_{q\in S}\). The next-state map of the inverse transducer at output symbol \(0\) therefore sends \(q\) to \(A(q)\) if \(q\notin S\), and to \(B(q)\) if \(q\in S\). Its image is the disjoint union candidate \(A(Q\setminus S)\cup B(S)\). Since \(A\) and \(B\) are permutations, this map is bijective if and only if \(B(S)=A(S)\). The inverse map at output symbol \(1\) has image \(B(Q\setminus S)\cup A(S)\), and it is bijective under exactly the same condition. Thus bireversibility holds precisely when \(S\) is invariant under the permutation \(T=A^{-1}B\).

**2. Uniform switch distribution.** Fix a particular \(k\)-element set \(S\subseteq Q\). Choose \(A\) arbitrarily in \(n!\) ways. By the characterization, \(B=AT\) for a permutation \(T\) preserving \(S\), and there are exactly \(k!(n-k)!\) such \(T\). Consequently, the number for this \(S\) is \(n!k!(n-k)!\). There are \(\binom nk\) choices of \(S\), so
\[
e_{n,k}=\binom nk n!k!(n-k)!=(n!)^2\qquad(0\le k\le n).\]
There are \((n!)^2 2^n\) invertible reversible tables altogether, proving the stated total and probability. These counts include the boundary cases \(k=0,n\) and \(n=1\).

**3. Connected decomposition.** Because \(A\) and \(B\) are permutations, the orbits of the subgroup \(\langle A,B\rangle\) partition \(Q\). Each orbit is a strongly connected component of the directed transition graph: inverses of permutation powers are positive powers on a finite orbit, so the semigroup and group orbits coincide. Both transition maps preserve every orbit, and the restriction of the output-swap set and of the bireversibility condition to each orbit is independent of the other orbits. Conversely, an unordered labeled set of connected bireversible transducers on disjoint state sets assembles uniquely into a bireversible transducer. The switching statistic is additive under this decomposition.

Let \(E_0(y)=1\) and \(E_n(y)=(n!)^2\sum_{k=0}^n y^k\) for \(n\ge1\). The labeled exponential formula therefore gives
\[
\sum_{n\ge0}E_n(y)\frac{z^n}{n!}
 =\exp\!\left(\sum_{n\ge1}C_n(y)\frac{z^n}{n!}\right),
\qquad C_n(y)=\sum_{k=0}^n c_{n,k}y^k.
\]
Taking formal logarithms proves the displayed connected enumerator.

For a purely finite recurrence, distinguish the component containing state \(0\). If its size is \(j\), choose the other \(j-1\) labels in \(\binom{n-1}{j-1}\) ways, decorate that component by \(C_j(y)\), and decorate the complement by \(E_{n-j}(y)\). Hence
\[
C_n(y)=E_n(y)-\sum_{j=1}^{n-1}\binom{n-1}{j-1}C_j(y)E_{n-j}(y),
\quad n\ge1,
\]
with the sum empty for \(n=1\). This recurrence makes all counts exact integer coefficients without analyticity assumptions, and gives the listed examples. Swapping every output permutation (\(S\mapsto Q\setminus S\)) preserves bireversibility and strong connectivity, so \(c_{n,k}=c_{n,n-k}\). The example \(C_3(y)=26+18y+18y^2+26y^3\) demonstrates that the connected distribution is not generally uniform. This completes the proof.

## Verification

The accompanying independent Python standard-library checker enumerates every pair of transition permutations and every state-output assignment for \(1\le n\le5\), and tests inverse-transducer reversibility **directly** from its output-conditioned transition maps, rather than using the invariant-subset characterization. It separately tests transition-graph reachability and compares the resulting coefficients with a finite binomial-convolution implementation of the connected recurrence. The exact replay checks \(470{,}322\) complete invertible reversible tables in those five state sizes and agrees at every coefficient. It also computes nonnegative, reversal-symmetric connected count vectors through \(n=9\). These finite checks corroborate but do not replace the proof for arbitrary \(n\).

Run: `python3 checker.py`. No external package, data file, or network connection is required.

## Relationship to prior work

The notions of bireversibility and connectedness are standard in Mealy-automaton theory. Godin's *Generic properties in some classes of automaton groups* (2019), especially Proposition 3.2, bounds the probability of bireversibility in the general fixed-alphabet random model but does not give the exact binary switch-statistic distribution or connected bivariate counts. D'Angeli and Rodaro, *Freeness Obstructions for Self-Similar Groups Acting on Rooted Trees* (first posted 2025), use bireversibility and connected components in group-freeness arguments, not the present labeled enumeration. Curtin and Savchuk, *Combinatorial structures connecting Latin squares and bireversible automata* (2026), present the pertinent general combinatorial characterization; its complete primary text was not accessible for definitive comparison, so priority is not established by the available source inspection. Its abstract does not assert this exact enumerator, but that is not a claim about everything in the paper. Related two-state classifications under state relabeling concern a different quotient and do not automatically imply the arbitrary-state labeled, connected output-switch enumerator.

## Limitations

The alphabet is strictly binary, the transition and output tables are labeled, and the connected notion is state-transition strong connectivity. The theorem does not count automata up to isomorphism, their generated automaton groups, minimal-state representations, or machines over larger alphabets. The 2026 combinatorial-structure preprint remains a relevant primary full-text priority risk. No independent mathematical audit has yet been performed.

## References

1. B. Curtin and D. Savchuk, *Combinatorial structures connecting Latin squares and bireversible automata*, arXiv:2607.26013, first posted July 28, 2026. https://arxiv.org/abs/2607.26013
2. T. Godin, *Generic properties in some classes of automaton groups*, arXiv:1903.11315, March 27, 2019. https://arxiv.org/abs/1903.11315
3. D. D'Angeli and E. Rodaro, *Freeness Obstructions for Self-Similar Groups Acting on Rooted Trees*, arXiv:2504.11048, first posted April 15, 2025. https://arxiv.org/abs/2504.11048
4. D. Francoeur, *Bireversible automata generating lamplighter groups*, *Bulletin of the London Mathematical Society* (2023), doi:10.1112/blms.12772. https://doi.org/10.1112/blms.12772
