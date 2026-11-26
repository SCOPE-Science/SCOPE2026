# All ternary Newman representations of \(289\) are universal

## Finding
Let a *Newman polynomial* mean a nonzero polynomial with coefficients in \(\{0,1\}\), constant coefficient \(1\), and leading coefficient \(1\). For any two Newman polynomials \(P,Q\), the numerical identity \(P(3)=289Q(3)\) forces the **polynomial identity**
\[
P(X)=\bigl(X^5+X^4-X^3-X^2+1\bigr)Q(X).
\]
In particular, \(Q(X)\) divides \(P(X)\) in \(\mathbb Z[X]\). Thus **every** representation of \(289\) as a quotient of two sums of distinct nonnegative powers of \(3\), each including \(3^0\), is universal in the sense of Anders--Dawsey--Reznick--Sisneros-Thiry [1]. There is no local representation of this integer.

## Assumptions and scope
There is no bound on the degrees or numbers of terms in \(P,Q\). Coefficients must be \(0\) or \(1\); nonzero constant coefficients are assumed. The conclusion concerns the exact multiplier \(289\) and base \(3\). It is stronger than divisibility alone because the quotient polynomial is uniquely specified.

Let \(R(X)=1-X^2-X^3+X^4+X^5\). Direct evaluation gives \(R(3)=289\). A nontrivial instance exists:
\[
Q(X)=1+X^2+X^3+X^5,\qquad
P(X)=1+X^7+X^9+X^{10}=R(X)Q(X),
\]
and \(Q(3)=280\), \(P(3)=80920=289\cdot280\).

## Proof
Write \(Q(X)=\sum_{i\ge0}q_iX^i\) and \(P(X)=\sum_{i\ge0}p_iX^i\), using zero padding beyond their degrees. The constant coefficients are \(p_0=q_0=1\). Define integer carries \(c_0=0\) and
\[
c_{i+1}=\frac{c_i+289q_i-p_i}{3}.
\]
The equality \(P(3)=289Q(3)\) ensures that the carry recursion produces integers: inductively, reduction of the equality modulo \(3^{i+1}\) shows that \(c_i+289q_i-p_i\) is divisible by \(3\). Each carry is nonnegative, because for \(c_i\ge0\) its numerator is at least \(-1\), so any multiple of \(3\) must be at least zero. Moreover \(c_i\le144\) inductively, since \((144+289)/3<145\). The initial transition is \(c_1=96\), because \(q_0=p_0=1\). Once both polynomials' digit sequences terminate, the nonnegative integer carries are repeatedly divided by \(3\) and therefore eventually reach zero.

For a carry \(c\), all possible transitions \(c\xrightarrow{(q_i,p_i)}d\) are precisely
\[
\begin{array}{ll}
3k\to k\ (0,0),\quad3k\to k+96\ (1,1),\\
3k+1\to k\ (0,1),\\
3k+2\to k+97\ (1,0).
\end{array}
\]
Introduce the following **20 live carries** and **12 trap carries**:
\[
\begin{split}
L={}&\{0,1,4,11,12,32,33,37,44,48,96,100,107,111,112,132,133,140,143,144\},\\
T={}&\{5,14,15,16,43,46,98,101,128,129,130,139\}.
\end{split}
\]
The transition formulas give a finite closure certificate: every transition from \(L\cup T\) remains in \(L\cup T\); every transition from \(T\) remains in \(T\); and the **only transitions from \(L\) into \(T\)** are \(96\xrightarrow{(1,1)}128\) and \(48\xrightarrow{(0,0)}16\). This can be verified directly from the displayed lists and transition formulas, or with the bundled standalone checker. Since a valid representation begins at carry \(96\in L\) and ends at carry \(0\in L\), it can never visit \(T\). Every carry of such a representation therefore belongs to \(L\).

For each \(c\in L\), associate the following five-bit history mask \(h(c)\). The least significant bit records \(q_{i-1}\), the next \(q_{i-2}\), through the fifth bit \(q_{i-5}\), with \(q_j=0\) for \(j<0\).

| Carry \(c\) | Mask \(h(c)\) | Carry \(c\) | Mask \(h(c)\) |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 96 | 1 |
| 1 | 16 | 100 | 9 |
| 4 | 8 | 107 | 5 |
| 11 | 4 | 111 | 13 |
| 12 | 20 | 112 | 29 |
| 32 | 2 | 132 | 11 |
| 33 | 18 | 133 | 27 |
| 37 | 26 | 140 | 23 |
| 44 | 22 | 143 | 15 |
| 48 | 30 | 144 | 31 |

Writing \(h=\sum_{j=1}^5 q_{i-j}2^{j-1}\), its associated carry is exactly
\[
c_i=96q_{i-1}+32q_{i-2}+11q_{i-3}+4q_{i-4}+q_{i-5}.
\]
The initial state \(c_1=96\) has history mask \(1\). For every edge \(c\xrightarrow{(q_i,p_i)}d\) with \(c,d\in L\), direct substitution into the four transition rules and the 20-entry table verifies **both**
\[
h(d)\equiv 2h(c)+q_i\pmod{32},\qquad
p_i=q_i-q_{i-2}-q_{i-3}+q_{i-4}+q_{i-5}.
\]
This is an exhaustive finite check of \(26\) live-to-live edges, not an assertion based on a sample of integer representations. It inductively establishes that every output coefficient equals the corresponding coefficient of \(R(X)Q(X)\). At termination \(c_i=0\), the mask is \(h(0)=0\), so the last five denominator digits are zero; all remaining coefficients of \(R(X)Q(X)\) are therefore also zero. Thus the coefficient identities extend through the ends of both polynomials, proving \(P(X)=R(X)Q(X)\).

## Verification
The dependency-free file `verify.py` reconstructs the 289-multiplier carry transitions, verifies closure and the uniqueness of the 20 live histories, checks each live edge against the polynomial convolution and confirms the nontrivial example. Run `python3 verify.py` from the directory containing this file. A successful run prints `VERIFY_OK` followed by the exact state and bounded-walk counts. The finite-state closure and invariants constitute an exhaustive certificate for all degrees; the additional short-walk tests are corroborative only.

## Relationship to prior work
Anders, Dawsey, Reznick and Sisneros-Thiry [1] establish the ternary carry algorithm and distinguish universal from local Newman-polynomial quotient representations. Their Section 4 table marks the local-representation entry for \(289\) with a question mark, while identifying universal representations. The present exact polynomial identity resolves that specific entry negatively. It does not alter the paper's general algorithm or claim a classification for other integers. No equivalent or stronger statement was identified in the inspected literature, with the limitations in the review materials.

## Limitations
The method as presented is a complete exact certificate only for multiplier \(289\) in base \(3\). It does not settle the authors' broader classification problem or determine whether analogous unique polynomial quotients occur for other multipliers. The originality assessment is based on accessible literature and cannot exclude unindexed or unpublished work; no independent mathematical audit has been performed.

## References
[1] K. Anders, M. Locus Dawsey, B. Reznick, and S. Sisneros-Thiry, *Representations of integers as quotients of sums of distinct powers of three*, arXiv:2308.07252v1, first publicly posted 14 August 2023. https://arxiv.org/abs/2308.07252.
