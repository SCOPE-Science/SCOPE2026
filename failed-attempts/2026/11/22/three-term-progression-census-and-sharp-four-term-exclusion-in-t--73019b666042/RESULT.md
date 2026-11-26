# Three-term progression census and sharp four-term exclusion in the Baum–Sweet support

## Finding

Let \(A\) contain zero and all positive integers whose standard binary expansion has no maximal zero-run of odd length. Equivalently, \(A\) is the one-position set of the Baum–Sweet sequence with its original value \(b(0)=1\). For each integer \(L\ge0\), let
\[
T_L=\#\{(a,d)\in\mathbb Z_{\ge0}\times\mathbb Z_{>0}: a+2d<2^L,\ a,a+d,a+2d\in A\}.
\]
Then the **complete all-depth progression census** is
\[
\boxed{\sum_{L\ge0}T_Lz^L=\frac{z^3(1+z)}{(1-z-z^2)(1-z-3z^2+2z^4)}.}
\]
Its initial values \(T_0,T_1,\ldots,T_{12}\) are \(0,0,0,1,3,9,23,56,132,303,687,1539,3425\). No four distinct equally spaced nonnegative integers all lie in \(A\), whereas \((4^j,4^{j+1},7\cdot4^j)\) is a three-term progression in \(A\) for every integer \(j\ge0\). Hence the maximum length of a nonconstant arithmetic progression in \(A\) is **exactly three**.

## Assumptions and scope

Arithmetic progressions have strictly positive integer common difference and are not required to use consecutive members of \(A\). Each \((a,d)\) is counted once, and all three terms must be strictly below \(2^L\). The condition at zero is part of the definition: the empty binary representation has no forbidden zero-run and is accepted. In fact no positive-step three-term progression can start at zero: if \(d\in A\) and \(d>0\), then \(\nu_2(d)\) is even, whereas \(\nu_2(2d)\) is odd, so \(2d\notin A\). Thus the conclusions on nonconstant progressions are unchanged under the alternative convention excluding zero. The statements concern ordinary integer progressions, not cyclic progressions modulo \(2^L\). The variable \(z\) is formal; the generating function is a formal power series with integer coefficients.

## Proof

**Binary recurrences and sharp exclusion.** For every \(n\ge0\), the zero-run definition gives
\[
\mathbf1_A(4n)=\mathbf1_A(n),\qquad
\mathbf1_A(2n+1)=\mathbf1_A(n),\qquad
\mathbf1_A(4n+2)=0.
\tag{1}
\]
Suppose a four-term progression \(a,a+d,a+2d,a+3d\) lay in \(A\), with \(d>0\). If \(d\) is odd, its four residues modulo four include \(2\), violating (1). Otherwise, when \(a\) is odd, all four terms are odd; the second rule of (1) reduces the progression to \(((a-1)/2)+j(d/2)\), for \(0\le j\le3\), with a strictly smaller positive difference. When \(a\) is even, the first and third rules force \(4\mid a\) and \(4\mid d\); the first rule reduces the progression to \((a/4)+j(d/4)\), also with smaller difference. Induction on \(d\) rules out every four-term progression. The numbers \(1,4,7\) are in \(A\), and multiplication by four preserves membership, proving sharpness and infinitely many distinct examples.

**Ten-state binary carry census.** We read, least-significant digit first, a pair \((a,d)\). At digit position \(j\), let its digits be \(x,y\in\{0,1\}\). Simultaneously compute digits for \(a\), \(a+d\), and \(a+2d\). A state \((c_1,c_2;q_0,q_1,q_2;u)\) consists of the two incoming carries for the latter two sums, the parities of zero-runs already read since the most recent one-bit for each of the three numbers, and a flag \(u\) recording whether a one-bit of \(d\) has occurred. Initially all entries are zero. Form
\[
v_i=x+i y+c_i\quad(i=0,1,2),\qquad c_0=0,
\]
where \(c_i\) is the incoming carry. Its output digit is \(e_i=v_i\bmod2\), and its next carry is \(\lfloor v_i/2\rfloor\). A transition is forbidden if some \(e_i=1\) has \(q_i=1\), since that would close an odd zero-run. Otherwise replace \(q_i\) by \(0\) if \(e_i=1\), or by \(1-q_i\) if \(e_i=0\), and replace \(u\) by \(u\lor y\). At the end of exactly \(L\) bits, accept if and only if \(u=1\) and both carries vanish; the final zero-run parities are unrestricted, since excess zeros above the highest one-bit are leading zeros and irrelevant. This also correctly accepts the integer zero.

The complete reachable-state table follows. The columns give the destination state for input digits \((x,y)=00,01,10,11\), and `–` denotes a forbidden transition. In state notation, the first pair is \((c_1,c_2)\), the next triple is \((q_0,q_1,q_2)\), and the final digit is \(u\).

| State | \((c_1,c_2;q_0,q_1,q_2;u)\) | 00 | 01 | 10 | 11 | Accept |
|---|---|---|---|---|---|---|
| 0 | (00;000;0) | 1 | 2 | 0 | 3 | No |
| 1 | (00;111;0) | 0 | – | – | – | No |
| 2 | (01;101;1) | – | – | – | – | No |
| 3 | (11;010;1) | – | 4 | 5 | – | No |
| 4 | (11;100;1) | 6 | 3 | – | – | No |
| 5 | (11;001;1) | – | – | 3 | 7 | No |
| 6 | (00;000;1) | 8 | 2 | 6 | 3 | Yes |
| 7 | (12;000;1) | 2 | 9 | 3 | 7 | No |
| 8 | (00;111;1) | 6 | – | – | – | Yes |
| 9 | (12;111;1) | – | 7 | – | – | No |

For state \(i\), let \(G_i(z)\) count accepting continuations by the number of additional binary digits. The table yields the formal equations
\[
G_i(z)=f_i+z\sum_{i\to j}G_j(z),\qquad
f_6=f_8=1,\ f_i=0\ \text{otherwise}.
\tag{2}
\]
Parallel edges, if any, are counted with their multiplicity. The unique formal solution exists since the transition matrix is multiplied by \(z\). Let
\[
P(z)=(1-z-z^2)(1-z-3z^2+2z^4).
\]
An exact polynomial certificate for (2) is obtained by setting \(H_i(z)=P(z)G_i(z)\). The coefficients of \(H_i\), from constant term upward, are:

| \(i\) | Coefficients of \(H_i\) |
|---|---|
| 0 | 0,0,0,1,1 |
| 1 | 0,0,0,0,1,1 |
| 2 | 0 |
| 3 | 0,0,1,0,-2,-1 |
| 4 | 0,1,0,-3,-2,1,1 |
| 5 | 0,0,0,1,1,-1,-1 |
| 6 | 1,0,-4,-2,3,2 |
| 7 | 0,0,0,1,1 |
| 8 | 1,-1,-3,0,3,1 |
| 9 | 0,0,0,0,1,1 |

Direct coefficient comparison verifies \(H_i=P f_i+z\sum_{i\to j}H_j\) for all ten rows, without numerical extrapolation. Thus \(G_0=H_0/P=z^3(1+z)/P\). Every accepted length-\(L\) path corresponds bijectively to one ordered pair \((a,d)\) counted in \(T_L\), since the two input bit strings determine \((a,d)\) uniquely, the carries enforce the three values, and the two acceptance conditions enforce \(d>0\) and \(a+2d<2^L\). Hence \(G_0(z)=\sum_{L\ge0}T_Lz^L\), proving the claimed generating function.

## Verification

The accompanying standalone `CHECK.py` reconstructs the complete reachable carry graph independently from the digit rule, checks all 40 specified transitions and the polynomial identities in ten states over the integers, and compares generating-function coefficients with exact state counts through depth 24. It also performs independent direct enumeration for every depth at most 12 and validates the three binary recurrences on 30,000 integers. Execute `python3 CHECK.py`; a successful run reports `CHECK_OK 90102 exact assertions`. The graph closure and polynomial identity constitute a finite, exact certificate for the unrestricted generating-function formula; the brute-force computations are supplementary. The four-term exclusion uses the unrestricted descent proof, independently of the finite check.

## Relationship to prior work

Baum and Sweet's 1976 work introduces the sequence in characteristic two. The explicit zero-run rule and the index set \(A\) appear in the literature on automatic sequences and in OEIS A060142 (dated March 5, 2001); the initial-value convention at zero is clarified by OEIS A086747. Rowland–Yassawi (2012), Example 4.3, give the binary sequence as an example of automaticity and its realization via a linear cellular automaton; their result neither computes three-term progression counts nor proves four-term exclusion. A published study titled *Three exact additive sumsets of the zero-run-even integers* (2026) proves \(A+A=A+2A=\mathbb N_0\) and a restricted formula for \(A+4A\), as well as Fibonacci growth of \(\#(A\cap[0,2^L))\). These are two-summand existence and single-set counting statements; neither implies the evaluated positive-step three-term progression generating function or the maximal-length exclusion. Another published study counting progressions in the odd-coefficient supports of individual Pascal rows (2026) concerns different finite digit sets, with no identity mapping those supports to the present \(A\).

## Limitations

The theorem counts progressions completely inside dyadic intervals and establishes the maximum possible length. It does not classify individual common differences of three-term progressions or give counts on arbitrary interval endpoints. The source from 1976 has a documented year and month but no verified day in the inspected records; March 5, 2001 is the earliest individually day-dated public record verified for the zero-run set, not a claim that the set originated in 2001. A broader theorem on automatic-set arithmetic progressions might imply the result, but none of the relevant inspected sources established these evaluations. Historical priority has not been independently certified.

## References

1. L. E. Baum and M. M. Sweet, *Continued fractions of algebraic power series in characteristic 2*, Ann. Math. **103** (1976), 593–610, DOI: https://doi.org/10.2307/1970953.
2. OEIS A060142, *Ordered set defined by \(0\), \(x\mapsto2x+1\), and \(x\mapsto4x\)*, original entry credited to Clark Kimberling, March 5, 2001. https://oeis.org/A060142
3. OEIS A086747, *Baum–Sweet sequence*, explaining differing initial-value conventions. https://oeis.org/A086747
4. E. Rowland and R. Yassawi, *A characterization of \(p\)-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008v1 (September 26, 2012), Example 4.3. https://arxiv.org/abs/1209.6008
5. *Three exact additive sumsets of the zero-run-even integers*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-three-exact-additive-sumsets-of-the-zero-run-even-integers--0abca7625fff
6. *Exact arithmetic-progression census in odd-binomial Pascal rows*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-arithmetic-progression-census-in-odd-binomial-pascal-rows--50ffd95589d7
