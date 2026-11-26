# Exact three-symbol complement-deletion spectra of finite alternating binary words

## Finding

For any binary word \(w\) and a binary pattern \(u\) of length three, let \(C(w,u)\) be the **set of distinct residual words** obtained by erasing the positions of one order-preserving occurrence of \(u\) in \(w\). If no such occurrence exists, the set is empty. We completely determine \(|C(w,u)|\) for **every alternating binary source word of length at least three** and every one of the eight possible patterns \(u\).

All words starting with zero and alternating are either \(E_n=(01)^n\), \(n\ge2\), or \(O_n=(01)^n0\), \(n\ge1\). Write \(\binom{x}{r}=0\) for integers \(x\ge0\) and \(r>x\). The following table gives the exact cardinalities, including all short boundary cases:

| Deleted pattern \(u\) | \(|C(E_n,u)|\), \(n\ge2\) | \(|C(O_n,u)|\), \(n\ge1\) |
|:---:|:---|:---|
| `000` | \(\binom n3\) | \(\binom{n+1}3\) |
| `001` | \(\binom{n-1}3+\binom n2\) | \(\binom{n-1}3+\binom n2\) |
| `010` | \(\binom{n-1}3+n-1\) | \(\binom n3+n\) |
| `011` | \(\binom{n-1}3+\binom n2\) | \(\binom{n-1}3+\binom n2\) |
| `100` | \(\binom{n-2}3+\binom{n-1}2\) | \(\binom{n-1}3+\binom n2\) |
| `101` | \(\binom{n-1}3+n-1\) | \(\binom{n-1}3+n-1\) |
| `110` | \(\binom{n-2}3+\binom{n-1}2\) | \(\binom{n-1}3+\binom n2\) |
| `111` | \(\binom n3\) | \(\binom n3\) |

The source starting with one follows from the exact bit-complement bijection \(C(\overline w,\overline u)=\{\overline v:v\in C(w,u)\}\).

Two sharp contrasts persist at every length:
\[
|C(E_n,010)|-|C(E_n,100)|=1\quad(n\ge2),
\]
\[
|C(O_n,010)|-|C(O_n,001)|=1\quad(n\ge1).
\]
Thus the *ordering* of the three erased symbols matters even when their numbers of zeros and ones agree. All sixteen parity-and-pattern enumerators are rational with denominator \((1-z)^4\).

## Assumptions and scope

A positional embedding of \(u=u_1u_2u_3\) in \(w=w_1\cdots w_N\) is a triple \(1\le i_1<i_2<i_3\le N\) such that \(w_{i_j}=u_j\) for \(j=1,2,3\). Its residual is \(w\) with those three positions erased, without cyclic identification. Different embeddings with the same residual are counted once. \(C(w,u)\) contains residual strings of length \(N-3\); the empty residual is permitted when \(N=3\). Every source considered is alternating, with \(N\ge3\), and the entire binary pattern alphabet is enumerated. No statement about arbitrary nonalternating sources or longer deleted patterns is implied.

For compact verification, define \(A_u(z)=\sum_{n\ge2}|C(E_n,u)|z^{n-2}\) and \(B_u(z)=\sum_{n\ge1}|C(O_n,u)|z^{n-1}\). The exact numerators \((1-z)^4A_u(z)\) and \((1-z)^4B_u(z)\) are:

| \(u\) | \((1-z)^4 A_u(z)\) | \((1-z)^4 B_u(z)\) |
|:---:|:---|:---|
| `000` | \(z\) | \(z\) |
| `001` | \(1-z+z^2\) | \(z-z^2+z^3\) |
| `010` | \(1-2z+2z^2\) | \(1-2z+2z^2\) |
| `011` | \(1-z+z^2\) | \(z-z^2+z^3\) |
| `100` | \(z-z^2+z^3\) | \(z-z^2+z^3\) |
| `101` | \(1-2z+2z^2\) | \(z-2z^2+2z^3\) |
| `110` | \(z-z^2+z^3\) | \(z-z^2+z^3\) |
| `111` | \(z\) | \(z^2\) |

## Proof

**1. Exact interleaving automaton.** Fix a three-letter pattern \(u\). Consider an epsilon-NFA whose states are \((p,j)\), with \(p\in\{0,1\}\) the next required symbol of the alternating host and \(j\in\{0,1,2,3\}\) the number of erased-pattern letters already inserted. Its initial state is \((0,0)\). If \(j<3\) and \(u_{j+1}=p\), it may make an epsilon move to \((1-p,j+1)\), corresponding to inserting the next erased symbol. On reading a residual symbol \(c\), it may move to \((1-p,j)\) exactly when \(c=p\). There are no other moves. A read word is accepted for even-length sources when the epsilon closure after reading contains \((0,3)\), and for odd-length sources when it contains \((1,3)\).

Induction on the number of interleaved symbols proves that a path specifies exactly an interleaving of the read residual with \(u\), preserving both orders, that alternates from an initial zero. Conversely every prescribed triple deletion gives such a path, assigning the deleted positions to epsilon moves and the remaining positions to input moves. The terminal state specifies parity, while the length of the input fixes the host length. Therefore the accepted residuals of length \(2t+1\) for terminal phase zero are exactly \(C(E_{t+2},u)\); the accepted residuals of length \(2t\) for terminal phase one are exactly \(C(O_{t+1},u)\), for every integer \(t\ge0\).

**2. Determinize without overcounting.** Take epsilon closure of subsets of the eight NFA states. From an input subset \(S\), its transition under \(c\in\{0,1\}\) is the epsilon closure of \(\{(1-p,j):(p,j)\in S,\ p=c\}\). Breadth-first exploration from the initial closure produces at most ten reachable subsets for every pattern; it includes the empty sink. Distinct residual strings give distinct deterministic paths even when several NFA interleavings exist, so accepting-path counts of this DFA count **distinct residuals**, not embeddings.

Let \(T_u\) be its integer adjacency matrix: in the entry from state \(i\) to state \(j\), count how many of the two letters lead from \(i\) to \(j\). Let \(e\) be the row selecting the initial subset, and let \(h_{u,0}\), \(h_{u,1}\) be the zero-one columns selecting states containing \((0,3)\), \((1,3)\). Then, with \(Q_u=T_u^2\),
\[
|C(E_{t+2},u)|=eT_uQ_u^t h_{u,0},\qquad
|C(O_{t+1},u)|=eQ_u^t h_{u,1}.
\]
This identity is exact for all \(t\ge0\) by the preceding bijection.

**3. An exact finite linear-algebra certificate.** The attached `transfer_certificate.py` constructs the reachable subsets in specified breadth-first order using the two transition rules above, prints all transition rows and accepting-state indices, and checks only exact integer arithmetic. If \(q_u\) is the number of reachable subsets, its computed values are \(q_u=9\) for `000`, `001`, `010`, `011`, `110`, `111`, and \(q_u=10\) for `100` and `101`.

For **each** of the eight patterns it verifies the following finite identities for **every** integer \(0\le t<q_u\):
\[
eT_uQ_u^t(Q_u-I)^4h_{u,0}=0,\qquad
eQ_u^t(Q_u-I)^4h_{u,1}=0.
\]
There are 148 individual exact zero checks, each on matrices with at most ten rows; the transition rows, accepting-state columns and counts are printed in `transfer_output.txt`. These checks are independently reproducible by the explicit finite algorithm in the attached source. By Cayley–Hamilton, every scalar sequence \(eT_uQ_u^t v\) or \(eQ_u^t v\) obeys the characteristic recurrence of the \(q_u\)-dimensional matrix \(Q_u\). Hence \(q_u\) consecutive zeros starting at \(t=0\) imply zero for all \(t\ge0\). Applying this to \(v=(Q_u-I)^4h_{u,p}\) proves that the fourth forward differences of both counting sequences vanish at every nonnegative index. Both sequences are therefore polynomials of degree at most three in \(t\).

**4. Initial-value reconstruction and coefficients.** The same exact subset construction yields the following first four values for the even and odd source sequences, respectively:

| \(u\) | Even \(t=0,1,2,3\) | Odd \(t=0,1,2,3\) |
|:---:|:---|:---|
| `000` | 0, 1, 4, 10 | 0, 1, 4, 10 |
| `001` | 1, 3, 7, 14 | 0, 1, 3, 7 |
| `010` | 1, 2, 4, 8 | 1, 2, 4, 8 |
| `011` | 1, 3, 7, 14 | 0, 1, 3, 7 |
| `100` | 0, 1, 3, 7 | 0, 1, 3, 7 |
| `101` | 1, 2, 4, 8 | 0, 1, 2, 4 |
| `110` | 0, 1, 3, 7 | 0, 1, 3, 7 |
| `111` | 0, 1, 4, 10 | 0, 0, 1, 4 |

A degree-at-most-three counting sequence with initial terms \(s_0,\ldots,s_3\) has generating function \((1-z)^{-4}\sum_{i=0}^3 z^i\sum_{j=0}^i(-1)^j\binom4j s_{i-j}\). Substituting the table proves the sixteen generating-function identities. Binomial-series expansion gives the displayed all-length cardinalities. The two unit-gap identities follow by Pascal's rule; bitwise complement is a bijection between the two possible starting phases. This completes the infinite-length proof.

## Verification

Two independent checks are embedded and executable with standard Python 3, without external dependencies. `brute_check.py` directly chooses every three-position deletion in each alternating host of length 3 through 24, groups identical residual strings, and compares their counts with the formula for each of the eight erased patterns. It also checks the phase-flip bit-complement bijection. It covers 176 host-pattern cells for each initial phase. `transfer_certificate.py` separately constructs the epsilon-closure DFA, reports its exact transition graph and both accepting sets, verifies all sixteen initial-value polynomials, and checks the 148 integer identities used in the Cayley–Hamilton step. The files `brute_output.txt` and `transfer_output.txt` are captured outputs of the two supplied programs; they are not substitutes for the proof.

Reproduce by running `python3 brute_check.py` and `python3 transfer_certificate.py` in a directory containing these files. The first program exhausts the stated finite input range; the second establishes the all-length result using a finite matrix certificate plus the explicit Cayley–Hamilton argument.

## Relationship to prior work

Adamson, Fleischmann and Huch's March 2026 paper introduced \(C(w,u)\), provided general algorithms, proved structural assertions such as the perfect-shuffle singleton criterion, and explicitly identified closed formulas in specific cases as an open direction. Its full open-access HTML text, including the results in Sections 3–4 and the conclusion, was inspected. The general finite-input algorithm does not supply the present eight-pattern, both-parity closed formulas or the unit phase differences.

A published binomial-tail theorem determines \(C((01)^{m+k},(01)^k)\) for *even-length* erased patterns; that family excludes all length-three patterns. A published arbitrary-host run-pair theorem covers deletion of two distinct letters, not three. A published fixed-composition deletion spectrum counts all residuals obtainable by deleting any three positions with a prescribed surviving composition, **without prescribing the order of the deleted symbols**; the distinct formulas here for `001`, `010`, and `100`, which have identical composition, cannot be deduced from a weight-only total. Exact inspected statements and links appear in the accompanying review.

## Limitations

This is a complete theorem only for alternating binary host words and a prescribed deleted pattern of length exactly three. It does not give explicit cardinalities for arbitrary sources, larger alphabets, or longer deleted patterns. The direct enumeration is bounded by host length 24; the unrestricted proof rests on the verified small exact matrix identities and Cayley–Hamilton, not extrapolation. Although the inspected published sources do not state an equivalent of the complete table, a differently named or unindexed older shuffle/deletion enumeration remains a historical-priority risk. Independent external mathematical validation has not been performed.

## References

1. D. Adamson, P. Fleischmann and A. Huch, “(Sets of) Complement Scattered Factors,” first publicly posted 21 March 2026, arXiv:2603.20790v1, Sections 3–5. https://arxiv.org/html/2603.20790v1
2. “Binomial-tail law for complements of alternating words,” published research result, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92
3. “A run-pair formula for two-letter complement scattered factors,” published research result, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-run-pair-formula-for-two-letter-complement-scattered-factors--3b99e07a61fe
4. “Fixed-composition deletion spectra and parity bias for alternating binary words,” published research result, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-composition-deletion-spectra-and-parity-bias-for-alternati--4b7dc91ebfc9
