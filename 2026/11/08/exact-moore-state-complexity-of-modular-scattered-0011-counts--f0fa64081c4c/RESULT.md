# Exact Moore-state complexity of modular scattered \(0011\) counts

## Finding

For every integer \(m\ge2\), let \(\binom{w}{u}\) be the number of embeddings of a finite binary word \(u\) as an **ordered, not necessarily contiguous** subsequence of \(w\). Consider the residue-valued function
\[
 f_m:\{0,1\}^*\longrightarrow \mathbb Z/m\mathbb Z,
 \qquad f_m(w)=\binom{w}{0011}\bmod m.
\]
A complete deterministic Moore machine reads \(w\) left to right, starts in a designated state, and outputs \(f_m(w)\) after the whole input (equivalently, after each prefix). Its minimal possible number of states is exactly
\[
 \boxed{\operatorname{sc}_{\mathrm{Moore}}(f_m)=m^3\gcd(m,2).}
\]
Thus the count is \(m^3\) for odd \(m\) and \(2m^3\) for even \(m\). The same formula holds for the reversed and complemented pattern \(1100\), by interchanging the two input letters in the Moore machine.

## Assumptions and scope

The input alphabet is exactly \(\{0,1\}\). A subsequence embedding is a strictly increasing choice of index positions, and distinct embeddings are counted separately. The modulus is any integer \(m\ge2\), not necessarily prime. The output alphabet is the ring \(\mathbb Z/m\mathbb Z\). This result concerns **complete deterministic Moore machines for the entire residue-valued function**; it does not claim the same number of states for a Boolean acceptor testing only one residue class or for nondeterministic automata.

The first externally documented mathematical motivation is the 2026 examination of binary subsequence statistics in Parikh-matrix classes by Fazekas, Huang and Mercaş (arXiv:2610.06717, first submitted October 5, 2026). The present result concerns a different question: exact finite memory for a four-symbol scattered-count output.

## Proof

**1. A four-coordinate construction.** For an input prefix \(w\), store, modulo \(m\),
\[
(a,b,c,d)=\left(\binom{w}{0},\binom{w}{00},\binom{w}{001},\binom{w}{0011}\right).
\]
The initial state is \((0,0,0,0)\). Appending \(0\) or \(1\), respectively, produces
\[
 T_0(a,b,c,d)=(a+1,b+a,c,d),\qquad
 T_1(a,b,c,d)=(a,b,c+b,d+c),
\]
with every coordinate reduced modulo \(m\). These updates follow directly by separating subsequence embeddings according to whether they use the last letter. The Moore output is the fourth coordinate \(d\). All transitions are total.

**2. The exact number of possible first-two-coordinate pairs.** If the prefix contains \(t\ge0\) zeros, then
\[
 (a,b)=(t,\tbinom t2)\bmod m.
\]
For every integer \(t\),
\[
 \binom{t+m}{2}-\binom t2=mt+\binom m2.
\]
If \(m\) is odd, the right-hand side is zero modulo \(m\), so the first two coordinates have period \(m\). Since the first coordinate is \(t\bmod m\), there are exactly \(m\) distinct pairs. If \(m\) is even, increasing \(t\) by \(m\) changes the second coordinate by \(m/2\) modulo \(m\), whereas increasing \(t\) by \(2m\) returns both coordinates. Therefore every first-coordinate residue has two distinct second-coordinate values and there are exactly \(2m\) pairs. Unified, the number of pairs is \(m\gcd(m,2)\). Consequently the constructed Moore machine has at most \(m^3\gcd(m,2)\) reachable states.

**3. All these states are reachable.** Set
\[
 U=1,\qquad W=1^{m-1}0010^{2m-2}.
\]
Here exponentiation denotes word repetition, and \(0^0\) is the empty word. When the first two coordinates are zero, appending \(U\) sends \((0,0,c,d)\) to \((0,0,c,d+c)\). Appending \(W\) sends it to \((0,0,c+1,d)\): the initial \(m-1\) ones subtract \(c\) from \(d\), the next two zeros make the second coordinate \(1\), the next one adds \(1\) to \(c\) and the old \(c\) to \(d\), and the last \(2m-2\) zeros bring the first two coordinates back to zero because \(\binom{2m}{2}\equiv0\pmod m\). Thus \(U\) and \(W\) generate every pair \((c,d)\in(\mathbb Z/m\mathbb Z)^2\) on the zero-phase fiber.

For clarity, given arbitrary residues \(c,d\in\{0,\ldots,m-1\}\), the positive word
\[
 W\,U^d\,W^{(c-1)\bmod m}
\]
reaches \((0,0,c,d)\) from the initial state. Appending \(0^t\) for any \(0\le t<2m\) preserves \(c,d\) and reaches exactly
\[
 \left(t\bmod m,\binom t2\bmod m,c,d\right).
\]
Since those values exhaust all possible first-two-coordinate pairs, precisely \(m^3\gcd(m,2)\) states are reachable.

**4. All reachable states are pairwise distinguishable.** Let \(o_q(s)\) denote the output obtained by starting in state \(q=(a,b,c,d)\) and reading the suffix \(s\). The four suffixes \(\varepsilon,1,11,011\) produce the four residues
\[
 \bigl(o_q(\varepsilon),o_q(1),o_q(11),o_q(011)\bigr)
 = (d,\ d+c,\ d+2c+b,\ d+2c+b+a).
\]
This signature recovers all four coordinates in order: subtract the first from the second to get \(c\); subtract \(d+2c\) from the third to get \(b\); subtract the third from the fourth to get \(a\). Hence no two distinct reachable states can have identical right-output behavior. Every equivalent Moore machine therefore needs at least this many states, matching the construction.

## Verification

Run `python3 checker.py` in a Python 3 environment with only the standard library. It checks the subsequence-recursion output against independent four-index counting for all binary words of length at most \(16\); exhaustively enumerates reachable states for each \(2\le m\le30\); checks phase fibers and all four-suffix distinguishability signatures; checks explicit reaching words for each \(2\le m\le11\); and performs an independent Moore partition-refinement minimization for each \(2\le m\le11\). The recorded replay ended with `PASS`.

The computations are finite sanity checks. The conclusions for arbitrary moduli follow from Steps 1–4, not from extrapolating the finite verification range.

## Relationship to prior work

The binary Parikh-matrix investigations of Fazekas, Huang and Mercaş (2026) concern subsequence universality, Parikh-class arithmetic and probability approximations; the inspected accessible abstract does not state an exact modular Moore-state count for \(0011\). Fazekas and Huang (2024) develop generalized Parikh matrices that record subsequences, and their matrix framework motivates the recurrence used here, but their accessible abstract does not claim minimal deterministic output-state counts. The Myhill–Nerode viewpoint is classical; the contribution here is an exact reachable-orbit computation together with a four-suffix minimality certificate for this first balanced two-run pattern.

A related earlier calculation gives the output complexity of modular scattered \(010\), but a result about \(010\) does not imply this result for \(0011\): the patterns have different residual counters and opposite parity behavior. Their respective counts are \(m^3/\gcd(m,2)\) and \(m^3\gcd(m,2)\).

## Limitations

This theorem is specific to the literal scattered pattern \(0011\) (and its alphabet complement \(1100\)), and to deterministic residue-output Moore machines. It does not classify arbitrary patterns, all target-residue Boolean DFAs, or memory measures beyond state count. The primary papers' full texts could not be accessed in the source-retrieval environment; therefore prior implicit coverage in a more general published theorem remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first publicly submitted 2026-10-05), https://arxiv.org/abs/2610.06717.
2. S. Z. Fazekas, X. Huang, *Generalized Parikh Matrices For Tracking Subsequence Occurrences*, arXiv:2407.04462 (first publicly submitted 2024-07-05), https://arxiv.org/abs/2407.04462.
3. M. Rigo, P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, Theoretical Computer Science 601 (2015), 47–57, https://orbi.uliege.be/handle/2268/178703.
4. J. Myhill and A. Nerode, classical right-context equivalence and minimization principle for deterministic automata.
