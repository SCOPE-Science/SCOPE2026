# The exceptional quotient 289 has no local ternary Newman representations

## Finding
Let \(\mathcal P\) be the set of polynomials with coefficients in \(\{0,1\}\), constant term \(1\), and finite degree. **Every pair** \(p,q\in\mathcal P\) satisfying \(p(3)=289q(3)\) obeys the exact polynomial identity
\[
p(x)=\bigl(x^5+x^4-x^3-x^2+1\bigr)q(x).
\]
Therefore the integer \(289\) has **no local representation** as a quotient of two sums of distinct powers of three, in the terminology of Anders, Dawsey, Reznick, and Sisneros-Thiry. Such pairs exist: for example
\[
q(x)=1+x^2+x^3+x^5,\qquad p(x)=1+x^7+x^9+x^{10},
\]
with \(p(3)=80920=289\cdot280=289q(3)\). The polynomial quotient is the same for *every* representation.

## Assumptions and scope
A Newman polynomial here has only zero-or-one coefficients and constant term one. Degrees of \(p\) and \(q\) are unrestricted. A representation is *universal* if \(q(x)\) divides \(p(x)\) in \(\mathbb Z[x]\), and *local* otherwise [1, Definition 1.1]. The claim treats the exact integer multiplier \(289\), not its neighbors nor arbitrary integer multipliers. Both numerator and denominator may have any number of terms.

## Proof
**1. Exact carry automaton.** Write \(p(x)=\sum_{i\ge0}p_i x^i\) and \(q(x)=\sum_{i\ge0}q_i x^i\), padding the digit sequences with zeros. For the lower \(i\) digits define the multiplication carry by \(c_0=0\) and
\[
c_{i+1}=\frac{c_i+289q_i-p_i}{3}.
\]
The condition \(p(3)=289q(3)\) implies that all carries are integers, because the difference of the truncated sums is divisible by the corresponding power of three; the terminal carry is zero after enough trailing zeros. Starting at zero, every carry lies in \(\{0,\ldots,144\}\). Indeed, the four possible digit pairs, constrained by divisibility by three, give the complete transition rule
\[
\begin{array}{c|c|c}
c\pmod3 &(p_i,q_i)&c_{i+1}\\\hline
0&(0,0)\text{ or }(1,1)&c/3\text{ or }(c+288)/3\\
1&(1,0)&(c-1)/3\\
2&(0,1)&(c+289)/3
\end{array}
\]
(the order of alternatives in the first row matches the two digit pairs). This rule directly preserves the stated range for an integral transition starting inside it.

**2. Finite trapping certificate.** Introduce the disjoint sets
\[
\begin{aligned}
L={}&\{0,1,4,11,12,32,33,37,44,48,96,100,107,111,112,132,133,140,143,144\},\\
D={}&\{5,14,15,16,43,46,98,101,128,129,130,139\}.
\end{aligned}
\]
Applying the four residue rules to the \(32\) states in \(L\cup D\) verifies: every outgoing transition from \(L\cup D\) stays in \(L\cup D\), and every outgoing transition from \(D\) stays in \(D\). This is an exhaustive finite arithmetic check, reproducible with the included checker. Since \(c_0=0\in L\), and every finite representation ends at \(c=0\notin D\), no such carry path can enter \(D\); every carry therefore belongs to \(L\). In particular, this conclusion holds for *arbitrarily long* digit strings, not only strings up to a computational cutoff.

**3. The exact local identity.** Set
\[
R(x)=1-x^2-x^3+x^4+x^5.
\]
Its value at three is \(R(3)=289\). Define the weights
\[
(W_1,W_2,W_3,W_4,W_5)=(96,32,11,4,1),\qquad
W_j=\sum_{k=j}^{5}r_k3^{k-j},
\]
where \(r_k\) is the coefficient of \(x^k\) in \(R(x)\). Since every weight is greater than the sum of all later weights, weighted sums of five bits have unique encodings. The following table lists, for all \(20\) live carries, the unique five-bit vector \(h(c)=(h_1,\dots,h_5)\) with \(c=96h_1+32h_2+11h_3+4h_4+h_5\), together with **every** allowed transition. The digit pair is ordered \((p_i,q_i)\).

| Carry | Encoded past denominator bits, newest first | Next carry and current digit pair |
|---:|:---:|:---|
| `0` | `00000` | `0` with `(p,q)=(0,0)`; `96` with `(p,q)=(1,1)` |
| `1` | `00001` | `0` with `(p,q)=(1,0)` |
| `4` | `00010` | `1` with `(p,q)=(1,0)` |
| `11` | `00100` | `100` with `(p,q)=(0,1)` |
| `12` | `00101` | `4` with `(p,q)=(0,0)`; `100` with `(p,q)=(1,1)` |
| `32` | `01000` | `107` with `(p,q)=(0,1)` |
| `33` | `01001` | `11` with `(p,q)=(0,0)`; `107` with `(p,q)=(1,1)` |
| `37` | `01011` | `12` with `(p,q)=(1,0)` |
| `44` | `01101` | `111` with `(p,q)=(0,1)` |
| `48` | `01111` | `16` with `(p,q)=(0,0)` (dead); `112` with `(p,q)=(1,1)` |
| `96` | `10000` | `32` with `(p,q)=(0,0)`; `128` with `(p,q)=(1,1)` (dead) |
| `100` | `10010` | `33` with `(p,q)=(1,0)` |
| `107` | `10100` | `132` with `(p,q)=(0,1)` |
| `111` | `10110` | `37` with `(p,q)=(0,0)`; `133` with `(p,q)=(1,1)` |
| `112` | `10111` | `37` with `(p,q)=(1,0)` |
| `132` | `11010` | `44` with `(p,q)=(0,0)`; `140` with `(p,q)=(1,1)` |
| `133` | `11011` | `44` with `(p,q)=(1,0)` |
| `140` | `11101` | `143` with `(p,q)=(0,1)` |
| `143` | `11110` | `144` with `(p,q)=(0,1)` |
| `144` | `11111` | `48` with `(p,q)=(0,0)`; `144` with `(p,q)=(1,1)` |

The only edges from \(L\) to \(D\) are from \(48\) to \(16\) and from \(96\) to \(128\); as established in Step 2, a returning path cannot use them. On each of the other \(26\) listed edges \(c\to d\), direct substitution verifies the two finite identities
\[
h(d)=(q_i,h_1(c),h_2(c),h_3(c),h_4(c))
\quad\text{and}\quad
p_i=q_i-h_2(c)-h_3(c)+h_4(c)+h_5(c).
\]
These are identities of integers, with no limiting arguments. Since the initial state \(0\) has encoded bits \((0,0,0,0,0)\), induction along the whole returning path gives \(h_j(c_i)=q_{i-j}\) (putting \(q_k=0\) for \(k<0\)). Therefore for every index \(i\),
\[
p_i=q_i-q_{i-2}-q_{i-3}+q_{i-4}+q_{i-5},
\]
which is precisely the coefficient of \(x^i\) in \(R(x)q(x)\). Outside the finite polynomial supports, all coefficients are zero. Consequently \(p(x)=R(x)q(x)\) as polynomials, and the theorem follows.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The self-contained script checks \(R(3)=289\), the five carry weights, superincreasing uniqueness, all \(32\) complete outgoing transition sets, absorbing behavior of the \(12\) dead states, the \(20\) live-state encodings, and the exact digit identity on all \(26\) live-to-live transitions. As independent cross-checks, it reconstructs the precise reachable/returnable state sets, directly checks \(1,022\) returning walks of bounded length, and verifies an explicit positive representation and a known local example for multiplier \(22\). These finite checks furnish a complete certificate because the **proof** shows the finite transition assertions apply to digit strings of arbitrary length; the bounded walks alone do not prove the theorem.

## Relationship to prior work
Anders, Dawsey, Reznick, and Sisneros-Thiry [1] define universal and local representations, establish special families having only universal representations in their Theorem 2.4, analyze the quotient \(100\) in Theorem 2.6, and explicitly mark the existence of local representations of \(289\) with a question mark in Section 4's table. Their four families in Theorem 2.4 do not give the two-consecutive-positive, two-consecutive-negative polynomial quotient \(R(x)\), nor does their result for \(100\) settle the distinct multiplier \(289\). Their carry-digraph framework motivates the finite-state approach used here. Bai and collaborators [2] discuss related digit-representation automata but do not provide the universal-versus-local classification here.

## Limitations
The conclusion is specific to \(289\). It does not classify other unresolved multipliers or give a formula for the number of representations of a specified length. The \(32\)-state invariant has been checked by an executable exact-arithmetic program and its complete live transitions are reproduced above; the proof is conditional only on independently checkable finite integer arithmetic, not on a probabilistic experiment. No independent scientific audit has been performed, and an equivalent solution in unindexed literature remains possible.

## References
[1] Katie Anders, Madeline Locus Dawsey, Bruce Reznick, Simone Sisneros-Thiry, *Representations of integers as quotients of sums of distinct powers of three*, arXiv:2308.07252, first submitted 14 August 2023; Definition 1.1, Theorems 2.4 and 2.6, Section 4 (the row for \(289\)). https://arxiv.org/abs/2308.07252

[2] *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694 (2022), related automata and ternary digit constraints. https://arxiv.org/abs/2202.13694
