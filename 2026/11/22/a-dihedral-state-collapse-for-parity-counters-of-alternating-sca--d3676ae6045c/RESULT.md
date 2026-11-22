# A dihedral state collapse for parity counters of alternating scattered words

## Finding

Let \(P_k\) be the alternating binary word of length \(k\ge1\) beginning with \(0\), so its letters in zero-based positions are \(0,1,0,1,\ldots\). For an arbitrary finite binary input \(w\), let \(\binom{w}{P_k}\) count ordered selections of \(k\) increasing positions that spell \(P_k\). Set
\[
 f_k(w)=\binom{w}{P_k}\bmod2.
\]
A complete deterministic Moore machine must report \(f_k(w)\) after reading any input prefix \(w\), including the empty prefix. Its exact minimum reachable state count is
\[
 \boxed{\operatorname{sc}(f_k)=2^{\lceil\log_2(k+1)\rceil}.}
\]
Equivalently, the number of states is the smallest power of two strictly larger than \(k\). Exchanging the letters yields the same conclusion for the alternating pattern starting with \(1\).

A minimal machine has states \(t\in\mathbb Z/L\mathbb Z\), where \(L=2^{\lceil\log_2(k+1)\rceil}\), initial state \(0\), transitions
\[
 t\xrightarrow{0}-t-1\pmod L,\qquad t\xrightarrow{1}-t\pmod L,
\]
and output
\[
 h_k(t)=\binom{t+\lfloor k/2\rfloor}{k}\bmod2.
\]
The binomial coefficient may be evaluated using any integer representative of \(t\); the residue is well defined. Equivalently, with \(u=(t+\lfloor k/2\rfloor)\bmod L\), the output equals one precisely when each binary one-bit of \(k\) is also a one-bit of \(u\).

## Assumptions and scope

Inputs are finite words on \(\{0,1\}\), the empty word is allowed, and \(k\) is any fixed positive integer. An occurrence is a choice of positions, not a distinct subsequence value or a contiguous factor. The deterministic machine emits a bit after every prefix. The stated minimum is for this output map and hence also for the accepting DFA of the single parity-one residue (since the output alphabet already has two values). No statement is made here about residues modulo integers other than two or nonalternating patterns.

For a generalized binomial coefficient with an integer upper argument, \(\binom{u}{j}=u(u-1)\cdots(u-j+1)/j!\), with \(\binom{u}{0}=1\), and calculations below are reduced modulo two after evaluating the integer.

## Proof

**1. A simultaneous invariant for all alternating prefixes.** For \(0\le j\le k\), let \(P_j\) be the first \(j\) letters of the alternating infinite word and put \(v_0(t)=1\) and
\[
 v_j(t)=\binom{t+\lfloor j/2\rfloor}{j}\bmod2\qquad(1\le j\le k).
\]
Pascal's identity and the reflected-binomial identity \(\binom{-u}{j}=(-1)^j\binom{u+j-1}{j}\) imply, for every integer \(t\),
\[
 v_j(-t-1)=v_j(t)+\mathbf1_{j\,\mathrm{odd}}v_{j-1}(t),
 \qquad
 v_j(-t)=v_j(t)+\mathbf1_{j\,\mathrm{even}}v_{j-1}(t)
 \pmod2.
\]
Indeed, for \(j=2r\), reflection gives \(v_{2r}(-t-1)=\binom{t+r}{2r}=v_{2r}(t)\) and \(v_{2r}(-t)=\binom{t+r-1}{2r}\equiv v_{2r}(t)+\binom{t+r-1}{2r-1}\); the final term is \(v_{2r-1}(t)\). For \(j=2r+1\), reflection gives \(v_{2r+1}(-t)=v_{2r+1}(t)\) and \(v_{2r+1}(-t-1)=\binom{t+r+1}{2r+1}\equiv v_{2r+1}(t)+\binom{t+r}{2r}\). The case \(j=1\) also uses \(v_0=1\).

On appending one letter \(b\), the scattered-subsequence count for \(P_j\) increments exactly by the previous count for \(P_{j-1}\) if and only if the last letter of \(P_j\) equals \(b\). For the alternating pattern, that last letter is zero for odd \(j\), one for even \(j\). Thus the displayed identities are *precisely* the recurrence for all counters \(\binom{w}{P_j}\bmod2\). At the empty word, \(t=0\), and \(v_j(0)=\binom{\lfloor j/2\rfloor}{j}=0\) for \(j\ge1\). Induction on the input length establishes \(f_k(w)=v_k(t_w)\), where \(t_w\) evolves by the two reflected transitions.

**2. Reduction modulo a power of two.** The function \(t\mapsto\binom{t+c}{j}\bmod2\), for any fixed integer \(c\) and \(0\le j<L\), is periodic with period \(L\). One proof uses coefficient extraction from \((1+X)^{t+c}\) in the truncated ring \(\mathbb F_2[X]/(X^{k+1})\): since \(L\) is a power of two strictly exceeding \(k\), \((1+X)^L=1+X^L\equiv1\), and this holds for negative exponents too since the truncated series has a multiplicative inverse. Consequently all \(v_j\), and both transitions, are well-defined on the stated cyclic state set. The construction has \(L\) states and gives an upper bound of \(L\) on the minimum.

**3. All states are reachable.** The word `01` transforms \(t\) first into \(-t-1\) and then into \(t+1\pmod L\). Thus \((01)^s\) reaches the state \(s\bmod L\) from zero, for all \(s\ge0\).

**4. Every pair of states is distinguishable.** Let \(g(t)=h_k(t)\), viewed as an \(L\)-periodic binary sequence. Let \(H=L/2\), the highest binary place occurring in the positive integer \(k\), so its \(H\)-bit is one. By the parity form of Lucas's theorem,
\[
 \binom{u}{k}\bmod2=1\quad\Longleftrightarrow\quad (u\mathbin{\&}k)=k
\]
for \(0\le u<L\). The residue \(t_*=k-\lfloor k/2\rfloor\pmod L\) has \(g(t_*)=1\), but the residue \(t_*+H\) toggles that highest bit without modifying lower bits and therefore has \(g(t_*+H)=0\). Hence \(H\) is not a period of \(g\). Since the least period of an \(L\)-periodic sequence divides \(L\), and every proper divisor of the power of two \(L\) divides \(H\), the least period of \(g\) is exactly \(L\).

For any two distinct states \(t\ne s\pmod L\), the least-period conclusion supplies an integer \(r\ge0\) with \(g(t+r)\ne g(s+r)\). Appending \((01)^r\) advances both states by \(r\), so the two states have different output continuations. Thus all \(L\) reachable states are pairwise inequivalent, proving the lower bound of \(L\). Exchange of zero and one proves the second starting-symbol case. \(\square\)

## Verification

Two standalone Python programs are supplied. `check_literal.py` compares the cyclic construction with direct enumeration of increasing position tuples for every binary word of length at most 12 and every pattern length 1 through 12 (98,292 comparisons). `check_states.py` independently explores the full vector of prefix counters under both letter updates, verifies that the orbit is exactly the proposed cyclic orbit and that its states are all inequivalent by an explicit Moore partition refinement for every pattern length 1 through 90 (12,372 letter-transition checks, 510 period tests, and 6,186 minimized states in total). They require only Python 3 standard libraries and can be run as `python3 check_literal.py` and `python3 check_states.py`. Corresponding captured outputs are provided. Finite tests are checks, not the infinite proof; Steps 1–4 establish the theorem for every positive integer \(k\).

## Relationship to prior work

Richomme's 2025 full-text study of binomial coefficients of binary words concentrates on the two-letter patterns and two-binomial equivalence classes; it provides the current vocabulary for the subsequence statistics but does not identify the modular parity congruence or minimum Moore-machine size for alternating patterns of arbitrary length. Fazekas, Huang and Mercaş (2026) study subsequence universality and probabilities in binary Parikh-matrix classes with fixed letter and `01` counts, rather than output-machine minimization for an arbitrary alternating pattern. The 2024 work of Golafshan, Rigo and Whiteland studies binomial complexity of factors of generalized Thue–Morse words, not this prefix-output map. Černý's 2010 paper sets up general Parikh-mapping and scattered-subword-counting frameworks without this exact all-length state count.

The directly closest published specialization, *Exact output-state complexity for modular alternating scattered triples* (2026), determines the shortest alternating pattern of length three: for modulus two it has four states, exactly agreeing with the present formula at \(k=3\). Its theorem addresses only the patterns `010` and `101` for variable modulus and does not imply the growth law across arbitrary pattern lengths. Likewise, earlier modular two-run pattern results do not cover patterns having at least three changes of letter. The novelty claimed here is the uniform exact arbitrary-length statement and the two-reflection representation, not the known length-three value or elementary binomial-counting recurrences.

## Limitations

The modulus is exactly two and the target word is exactly alternating. Nothing here identifies minimal machines for arbitrary patterns or arbitrary moduli. The uniformity in the pattern length is proven by elementary generalized-binomial identities and Lucas's parity criterion; no unproved computer extrapolation is used. The historical-priority assessment is limited by inaccessible or unindexed earlier sources, notably the 2011 trie-automaton paper and papers not discoverable in the examined indexes. This mathematical result has not undergone independent expert validation.

## References

1. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (first public 2025-10-08). https://arxiv.org/html/2510.07159v1
2. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first public 2026-10-05). https://arxiv.org/abs/2610.06717
3. A. Golafshan, M. Rigo, M. A. Whiteland, *Computing k-binomial complexity of generalized Thue–Morse words*, arXiv:2412.18425 (2024). https://arxiv.org/abs/2412.18425
4. A. Černý, *Generalizations of Parikh Mappings*, RAIRO Theoretical Informatics and Applications 44 (2010), 209–228. https://doi.org/10.1051/ita/2009021
5. *Exact output-state complexity for modular alternating scattered triples* (2026), published record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-output-state-complexity-for-modular-alternating-scattered--f8d46c1509db
6. H. M. K. Alazemi, A. Černý, *Counting Subwords Using a Trie Automaton*, International Journal of Foundations of Computer Science 22 (2011), 1457–1469. https://doi.org/10.1142/S0129054111008817
