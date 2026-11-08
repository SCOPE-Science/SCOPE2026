# Reverse-complement factor spectra and exact densities of the 111 and 1111 pattern-parity words

## Finding

For \(d\in\{3,4\}\), let \(f_d(n)\) be the parity of the number of overlapping occurrences of the binary pattern \(1^d\) in the usual base-two expansion of \(n\), with \(f_d(0)=0\). A finite binary word \(u=u_0\cdots u_{h-1}\) is a *reverse-complement factor* if it occurs consecutively in \(f_d(0)f_d(1)\cdots\) and \(u_j=1-u_{h-1-j}\) for all indices \(j\). All nonempty such factors have even length.

Define the two families (including their bitwise complements)
\[
A_m=0^m1^m,\qquad B_m=0^{m-1}10\,1^{m-1}.
\]
For \(d=3\), the complete set is \(A_m,\overline{A_m}\) for \(1\le m\le5\), and \(B_m,\overline{B_m}\) for \(2\le m\le7\). For \(d=4\), replace these ranges by \(1\le m\le9\) and \(2\le m\le15\). These are disjoint except that \(B_1=\overline{A_1}\), which is therefore not separately included. Consequently the numbers of distinct nonempty reverse-complement factors are respectively \(22\) and \(46\), and their longest lengths are respectively \(14\) and \(30\).

Every factor has an exact natural starting-position density. In each row below, the displayed density applies separately to the indicated word and its bitwise complement; an omitted range means the word does not occur.

| \(d\) | Family | \(m\) | Density of each word |
|---|---|---|---|
| 3 | \(A_m\) | 1; 2; 3–5 | \(7/48;\ 3/128;\ 1/128\) |
| 3 | \(B_m\) | 2–3; 4–7 | \(5/384;\ 1/256\) |
| 4 | \(A_m\) | 1; 2; 3–4; 5–9 | \(5/64;\ 7/512;\ 3/512;\ 1/512\) |
| 4 | \(B_m\) | 2–3; 4–15 | \(3/512;\ 1/1024\) |

For the longest factor \(B_{2^d-1}\), all zero-based occurrences are exactly
\[
2^{d+1}t+2^d\quad(t\ge0),\qquad
S_d(t)=(0,1,2^{d-1}-2),
\]
where \(S_d(t)=(f_d(t),f_d(t+1),t\bmod 2^{d-1})\). The complement occurs at the same residue with state \((1,0,2^{d-1}-2)\). The density of each longest word is \(1/2^{2d+2}\).

## Assumptions and scope

The binary expansion is finite and leading zeros do not count toward new occurrences of \(1^d\). Pattern occurrences may overlap. Starting indices range over all nonnegative integers. No claim is made for patterns of lengths \(d\ge5\), for arbitrary binary patterns, or for ordinary palindromes. Densities are limits over all initial index intervals, not merely dyadic cutoffs.

## Proof

**Digit recursion.** Put \(Q=2^{d-1}\). Appending binary zero creates no new occurrence of \(1^d\); appending binary one creates exactly one new occurrence when the parent ends in \(d-1\) ones. Hence, for every \(t\ge0\),
\[
f_d(2t)=f_d(t),\qquad f_d(2t+1)=f_d(t)\oplus[t\equiv Q-1\pmod Q],
\]
with addition \(\oplus\) modulo two. Thus the state \(S_d(t)=(a,b,r)=(f_d(t),f_d(t+1),t\bmod Q)\) evolves on appended digits by
\[
T_0(a,b,r)=(a,a\oplus e,2r\bmod Q),\quad
T_1(a,b,r)=(a\oplus e,b,(2r+1)\bmod Q),\qquad e=[r=Q-1].
\]
Every nonnegative integer has a binary expansion and therefore every state ever realized belongs to the smallest set containing \((0,0,0)\) and closed under \(T_0,T_1\). Conversely, every state in that closure is realized by an integer, since each appended digit corresponds to doubling or doubling-and-one.

**Bounded complete factor reduction.** Put \(k=d+1\), \(H=2^k\). Write an arbitrary starting index as \(Ht+r\), with \(0\le r<H\). For \(0\le j<H\), a length-\(k\) binary expansion of \(j\) gives
\[
 f_d(Ht+j)=f_d(t)\oplus f_d(j)\oplus
\bigoplus_{\ell=1}^{d-1}
 [t\equiv2^\ell-1\pmod{2^\ell}]
 [\text{the leading }d-\ell\text{ bits of the }k\text{-bit }j\text{ are all }1].
\]
The summands correspond bijectively to occurrences of \(1^d\) wholly in the parent, wholly in the lower block, and crossing their boundary. For \(H\le j<2H\), use the same formula with parent \(t+1\), whose parity and lower residue are already recorded by \(S_d(t)\). Therefore *every* factor of length at most \(H\) is determined by one of the finite pairs \((S_d(t),r)\). Conversely every enumerated pair is achieved, so this is an exact infinite-word reduction, not a prefix heuristic.

**Exact finite part.** The accompanying standard-library program `check_factors.py` constructs the complete reachable state closures (\(14\) states for \(d=3\), \(24\) for \(d=4\)) and enumerates every state, residue, and even factor length through \(H\). It checks the derived factors against the explicit \(A/B\) families and checks every rational density in the table. It finds no reverse-complement factor of length \(H\), which excludes every greater even length: deleting equal numbers of letters at both ends of any longer reverse-complement word yields one of length \(H\). Odd lengths are impossible because their central bit would equal its own complement. This proves the complete classifications and sharp cutoffs.

**Exact frequencies.** Let the state transition matrix \(P_d\) give probability \(1/2\) to each appended bit. The same finite program verifies that its reachable state graph is strongly connected and has a self-loop at \((0,0,0)\). Thus \(P_d\) is primitive and has a unique rational positive stationary probability vector \(\pi_d\), computed by exact rational Gaussian elimination and checked in the program. Uniformly distributed \(h\)-bit integers have state distribution \(\delta_{(0,0,0)}P_d^h\), which tends to \(\pi_d\). The convergence also holds over arbitrary initial intervals \([0,T)\): partition into binary subintervals, use uniform mixing for every sufficiently large subinterval, and bound the total length of the remaining small subintervals independently of \(T\). Hence a factor corresponding to pairs \((s,r)\) has natural starting-position density \(H^{-1}\sum_{(s,r)}\pi_d(s)\). Exact aggregation gives every value in the table.

For maximal factors the program also checks that there is exactly one state/residue pair for each of the two words: \((S_d(t),r)=((0,1,2),8)\) at \(d=3\) and \(((0,1,6),16)\) at \(d=4\), with complementing the first two coordinates giving the complementary factor. Stationary state masses are respectively \(1/16\) and \(1/32\); dividing by \(H\) proves the displayed densities and the occurrence rule.

## Verification

Run `python3 check_factors.py` using a standard Python interpreter. The program independently checks the digit recursion and block identity against direct pattern counting for the first \(512\) parents; these checks are supplementary. Its decisive finite-state certificate covers every reachable state and every residue, with \(1792\) state/residue/length cases for \(d=3\) and \(12288\) for \(d=4\). Exact rational equations are solved and checked without floating-point arithmetic. The code asserts all factor spectra, frequency values, maximal occurrence-state descriptions, and the empty factor set at the next even length.

## Relationship to prior work

Sun and Winterhof (2019) explicitly introduce binary \(1^d\)-occurrence parity sequences, but analyze maximum-order complexity of square-indexed subsequences, not contiguous reverse-complement factors. Frid, Laborde and Peltomäki (2020) analyze ordinary palindromic factorizations for the classical Rudin–Shapiro and paperfolding words, not the two higher-pattern reverse-complement spectra. Allouche and Shallit (1993) study ordinary factor complexity of a related generalized Rudin–Shapiro family; their complexity count does not decide which factors are fixed by the reverse-complement involution nor their individual densities. No general factor-complexity result is used as an originality claim for this invariant.

## Limitations

This is a two-parameter exact classification, not a theorem for arbitrary pattern lengths. The exhaustive calculation is finite but complete because the proved block/state reduction covers all positions and the next-length obstruction rules out all longer words. The stationary frequencies rely on the finite graph's primitive property as checked by the standalone program. An unindexed equivalent statement remains a possible literature risk. No independent scientific audit has been performed.

## References

1. Z. Sun and A. Winterhof, *On the maximum order complexity of subsequences of the Thue-Morse and Rudin-Shapiro sequence along squares*, 2019, https://arxiv.org/abs/1910.13763 (first public 2019-10-30).
2. A. E. Frid, E. Laborde, and J. Peltomäki, *On prefix palindromic length of automatic words*, 2020, https://arxiv.org/abs/2009.02934.
3. J.-P. Allouche and J. O. Shallit, *Complexité des suites de Rudin-Shapiro généralisées*, 1993, https://doi.org/10.5802/jtnb.94.
