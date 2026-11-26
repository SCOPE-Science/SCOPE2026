# Exact frequencies of all six gaps in the binary-partition three-square exceptional set

## Finding

Let \(b(n)\) count partitions of the nonnegative integer \(n\) into powers of two, repetitions allowed. Enumerate in increasing order
\[
E=\{n\ge 0:b(2n)\ne x^2+y^2+z^2\text{ for all }x,y,z\in\mathbb Z\}
=\{f_0<f_1<f_2<\cdots\},
\]
and let \(g_j=f_{j+1}-f_j\). For \(J\ge1\) and each \(d\in\{6,8,10,16,18,24\}\), define \(N_d(J)=\#\{0\le j<J:g_j=d\}\).

**Theorem.** For all integers \(J\ge1\), with an absolute implied constant,
\[
N_d(J)=p_dJ+O(\log(J+2)),\qquad
(p_6,p_8,p_{10},p_{16},p_{18},p_{24})
=\left(\frac14,\frac14,\frac1{16},\frac3{16},\frac3{16},\frac1{16}\right).
\]
In particular the limiting frequency of **each** of the six gaps exists and has the value displayed. Equivalently, for real \(X\ge1\),
\[
\#\{j\ge0:f_j<X,\ g_j=d\}=\frac{p_d}{12}X+O(\log(X+2)).
\]
The result determines the full empirical gap distribution, not merely the set of possible gap lengths.

## Assumptions and scope

All sets are subsets of the nonnegative integers; \(b(0)=1\). The symbols \(x,y,z\) in the definition of \(E\) range independently over all integers. Gaps are differences of consecutive elements of \(E\), not gaps in the argument of \(b(n)\) itself. Logarithms in big-O terms may have any fixed base greater than one. No claim is made about whether the ordered gap sequence is automatic.

Write \(\tau(n)\in\{0,1\}\) for the parity of the binary digit sum of \(n\), and \(\chi(n)=\mathbf1_E(n)\). Sobolewski and Ulas [1, Corollary 3.3] prove the exact criterion
\[
\chi(n)=1\ \Longleftrightarrow\ n=2^{2k+1}(4s+1)
\quad\text{for some integers }k,s\ge0\text{ with }\tau(s)=1.
\tag{1}
\]
Their Proposition 3.4 proves that the six displayed gap lengths are the only possibilities, and all occur infinitely often. The present theorem quantitatively refines their spectrum.

## Proof

**1. Digit-parity and exceptional-set counting.** Put \(u_n=(-1)^{\tau(n)}\). Then
\(u_{2m}=u_m\) and \(u_{2m+1}=-u_m\). Thus partial sums of \(u_n\) are bounded by \(1\). Criterion (1) implies
\[
\#\{0\le n<X:\chi(n)=1\}=\frac{X}{12}+O(\log(X+2)),\tag{2}
\]
because, at fixed \(k\), the integer \(s\) has density one half in the arithmetic parametrization \(2^{2k+1}(4s+1)\), with bounded counting error, and the sum of the densities is
\(\sum_{k\ge0}2^{-(2k+4)}=1/12\). There are \(O(\log(X+2))\) relevant values of \(k\).

For pair counts, define \(C(N)=\sum_{n=0}^{N-1}u_nu_{n+1}\). The digit recurrences give, for every \(M\ge0\),
\[
C(2M)=-M-C(M),\qquad C(2M+1)=-M-C(M)-1.
\]
Hence \(D(N)=C(N)+N/3\) satisfies \(D(2M)=-D(M)\) and \(D(2M+1)=-D(M)-2/3\). Binary descent proves \(D(N)=O(\log(N+2))\). Since \(\tau(n)\) is balanced with bounded prefix error, the frequencies of the ordered adjacent parity pairs are
\[
\begin{array}{c|cccc}
(a,b)&(0,0)&(0,1)&(1,0)&(1,1)\\\hline
\lim_{N\to\infty}N^{-1}\#\{n<N:(\tau(n),\tau(n+1))=(a,b)\}
&1/6&1/3&1/3&1/6.
\end{array}\tag{3}
\]
Each pair count differs from its main term by \(O(\log(N+2))\).

**2. Four exact block types.** For each \(n\ge0\), examine the positions of ones in \((\chi(16n+i))_{0\le i<16}\). The criterion (1), or the equivalent recurrence in [1, Corollary 3.3(d)], gives exactly the following possibilities:
\[
\begin{array}{c|c|c}
\text{type}&\text{condition on }n&\text{positions }i\text{ with }\chi(16n+i)=1\\\hline
A&\chi(n)=1&\{0,10\}\\
E&\chi(n)=0,\ \tau(n)=1,\ n\text{ even}&\{2,8\}\\
F&\chi(n)=0,\ \tau(n)=1,\ n\text{ odd}&\{2\}\\
G&\chi(n)=0,\ \tau(n)=0&\{10\}.
\end{array}\tag{4}
\]
Indeed \(\chi(n)=1\) forces \(n\) even and \(\tau(n)=0\), by (1); at positions \(0,2,8,10\), the recurrence yields respectively
\(\chi(n),\tau(n),\mathbf1_{2\mid n}\tau(n),1-\tau(n)\), and all other positions vanish.

The frequencies of the types \((A,E,F,G)\) are \((1/12,1/4,1/4,5/12)\), each with logarithmic discrepancy, by (2) and the digit recurrences.

**3. Adjacent-block transition frequencies.** Every type-A index is even and has digit parity zero, so its following odd index is of type F. Every type-E index similarly is followed by G. If \(n=2m+1\) has type F, then \(\tau(m)=0\); by (3), the successor is of type E at rate \((1/2)(1/3)=1/6\), and of type G at rate \((1/2)(1/6)=1/12\). It cannot be of type A: (1) implies that for any positive exceptional even integer \(r\), its immediate predecessor \(r-1\) has \(\tau(r-1)=0\). Indeed subtraction of one contributes precisely \(2k+1\) trailing ones, flipping \(\tau(s)=1\) to zero.

For a type-G index, the successor is of type E exactly when its index is odd and the underlying adjacent parity pair is \((1,1)\), giving rate \(1/12\). A type-G even index has successor F at rate \(1/4-1/12=1/6\), since every type-A even index is followed by F. Every A is preceded by a G, accounting for G-to-A rate \(1/12\). The remaining G-to-G rate is \(1/12\). Thus the complete list of nonzero transitions and asymptotic counts per \(N\) starting blocks is
\[
\begin{array}{c|cccccccc}
\text{transition}&A\to F&E\to G&F\to E&F\to G&G\to A&G\to E&G\to F&G\to G\\\hline
\text{rate}&1/12&1/4&1/6&1/12&1/12&1/12&1/6&1/12
\end{array}.\tag{5}
\]
By (2)–(3), every transition count has error \(O(\log(N+2))\). No other transition is possible.

**4. Exact gap accounting.** Every block in (4) contains at least one exceptional index. Type A contributes a within-block gap of length \(10\), and E contributes one of length \(6\). The cross-block gap determined by each transition in the order (5) is
\[
(8,18,16,24,6,8,8,16).
\]
For example A-to-F joins position \(10\) to position \(16+2\), and G-to-A joins position \(10\) to position \(16+0\). Combining internal and cross-block gaps gives the counts per \(N\) blocks, with error \(O(\log(N+2))\):
\[
\begin{array}{c|rrrrrr}
\text{gap length }d&6&8&10&16&18&24\\\hline
\text{rate }q_d&1/3&1/3&1/12&1/4&1/4&1/12.
\end{array}\tag{6}
\]
The total is \(\sum_d q_d=4/3\) consecutive gaps per 16-block. Dividing (6) by 16 gives the spatial rates \(q_d/16=p_d/12\). Cutting the integer interval at an arbitrary position changes counts by \(O(1)\), since any gap is contained in a block or spans one adjacent-block boundary. This proves the asserted \(X\)-based formula.

Finally (2) and the bounded-gap conclusion give \(f_J=12J+O(\log(J+2))\). Substitution \(X=f_J\) in the spatial formula gives \(N_d(J)=p_dJ+O(\log(J+2))\). \(\square\)

## Verification

The included self-contained Python checker `verify_gap_law.py` uses (i) an independent recurrence for the binary partition function and the classical three-square exclusion criterion, (ii) two equivalent definitions of \(\chi\), (iii) exact block membership and transition tests, and (iv) enumeration of every exceptional index in a fixed finite interval. Run `python verify_gap_law.py` using Python 3.10 or newer. It reported

`VERIFY_OK independent_partitions= 4097 block_cases= 65538 transitions= 65536 enumerated_gaps= 87381 gap_counts= {6: 21845, 8: 21846, 10: 5461, 16: 16384, 18: 16384, 24: 5461} finite_rational_checks=passed`

The finite numerical checks are corroboration only. The infinite result and logarithmic errors are established by the proof above, including the digit-pair correlation recurrence.

## Relationship to prior work

Sobolewski and Ulas [1] gave the exact indicator criterion (1), its 16-block structure, the exhaustive six-gap **spectrum** (Proposition 3.4), and a sharp counting estimate for the exceptional set as a whole (Theorem 6.1). Those statements motivate but do not state the individual **gap frequencies** or their logarithmic discrepancy. The new step counts all admissible transitions between adjacent block types using the two-point Thue–Morse correlation, then converts those counts into the full six-component frequency vector. The OEIS entry [2] gives the ordered exceptional positions and an equivalent indicator formula, not the frequency vector. The result does not resolve the authors' separate question about automaticity of the ordered gap sequence.

## Limitations

The law is specific to the ordinary (uncolored) binary partition function and to exceptional indices for three-square representability. The result does not determine whether the gap sequence is automatic, nor give exact finite-prefix counts without an error term. An equivalent theorem in unindexed literature cannot be categorically excluded. No independent mathematical audit has been performed.

## References

[1] B. Sobolewski and M. Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares*, arXiv:2211.16622 (first publicly posted 29 November 2022); *Results in Mathematics* 78, 188 (2023), DOI: 10.1007/s00025-023-01966-8. https://arxiv.org/abs/2211.16622 ; https://link.springer.com/article/10.1007/s00025-023-01966-8

[2] OEIS A363769, *Integers k such that the number of binary partitions of 2k is not a sum of three squares*. https://oeis.org/A363769
