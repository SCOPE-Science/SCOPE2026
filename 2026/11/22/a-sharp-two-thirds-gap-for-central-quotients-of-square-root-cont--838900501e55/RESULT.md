# A sharp two-thirds gap for central quotients of square-root continued fractions

## Finding
Let \(D>1\) be a nonsquare integer, \(A=\lfloor\sqrt D\rfloor\), and let its regular continued fraction have least period \(2r\), where \(r\ge1\):
\[
\sqrt D=[A;\overline{a_1,\ldots,a_{2r-1},2A}].
\]
Write \(C=a_r\) for the central partial quotient. Then
\[
\boxed{C\in\{A,A-1\}\ \cup\ \{1,\ldots,\lfloor 2A/3\rfloor\}.} \tag{1}
\]
The relative cutoff \(2/3\) is sharp: for every integer \(t\ge1\),
\[
\sqrt{9t^2+3}=[3t;\overline{2t,6t}],
\]
so its central quotient is exactly two-thirds of its initial quotient.

There is also a complete classification of the first coefficient below the two exceptional high values:
\[
\boxed{C=A-2\quad\Longleftrightarrow\quad D\in\{15,20,21,39\}}
\]
under the even-least-period hypothesis. Among least periods at least four, \(D=21\) is the unique case with \(C=A-2\).

## Assumptions and scope
All statements use the *least* period of the regular simple continued fraction of the positive irrational \(\sqrt D\). No restriction to squarefree \(D\) or prime \(D\) is imposed. The midpoint \(C\) is defined only for even least period. The endpoint \(A-1\) is retained formally in (1), even when \(A=1\); the actual midpoint is always positive.

For clarity, define integer complete-quotient states
\[
(m_0,q_0)=(0,1),\quad
m_{j+1}=q_ja_j-m_j,\quad
q_{j+1}=\frac{D-m_{j+1}^2}{q_j},\quad
 a_j=\left\lfloor\frac{A+m_j}{q_j}\right\rfloor\ (j\ge1),
\]
with \(a_0=A\). The standard square-root algorithm has \(m_j\in\{1,\ldots,A\}\) and \(q_j\) positive integers for \(j\ge1\); the terminal state is \((m_{2r},q_{2r},a_{2r})=(A,1,2A)\).

## Proof
**1. Midpoint identity.** The complete quotients satisfy the classical reversal symmetry
\[
m_j=m_{\ell+1-j}\qquad(1\le j\le\ell),\tag{2}
\]
where \(\ell\) is the least period length. This is the symmetry of the integer numerator in the standard square-root continued-fraction algorithm; it is also Perron's identity as recorded in Riche, Section 4, equation (4.11), after accounting for the one-step index shift. At \(\ell=2r\), equation (2) yields \(m_r=m_{r+1}\). The recurrence \(m_{r+1}=q_ra_r-m_r\) therefore gives the exact central relation
\[
\boxed{q_r C=2m_r.}\tag{3}
\]
This relation uses the parity of the **least period**, not merely a longer even multiple of a period.

**2. The only large central values.** For every \(j\ge1\), the conjugate of the complete quotient \((\sqrt D+m_j)/q_j\) lies in \((-1,0)\). Initially this follows from \(q_1=D-A^2\) and \(0<\sqrt D-A<q_1\). It is preserved by the continued-fraction operation because \(\bar\alpha_{j+1}=1/(\bar\alpha_j-a_j)\) with \(a_j\ge1\). Consequently,
\[
0<\sqrt D-m_j<q_j,\qquad 1\le m_j\le A.\tag{4}
\]
The case \(q_r=1\) is impossible: equation (4) then forces the integer \(m_r=A\), giving \(a_r=\lfloor\sqrt D+A\rfloor=2A\), the terminal partial quotient at step \(2r\), while \(r<2r\). Hence \(q_r\ge2\).

If \(q_r=2\), equation (4) gives \(m_r>\sqrt D-2>A-2\), hence \(m_r\in\{A-1,A\}\). Equation (3) says \(C=m_r\), producing precisely the two possible high values. If \(q_r\ge3\), equation (3) and \(m_r\le A\) yield \(3C\le2A\). Since \(C\) is positive, (1) follows.

**3. Sharpness.** Put \(A=3t\) and \(D=A^2+3\). The exact recurrence starts from \((m_0,q_0,a_0)=(0,1,A)\) and gives
\[
(m_1,q_1,a_1)=(A,3,2t),\qquad
(m_2,q_2,a_2)=(A,1,2A).
\]
Thus the least period is exactly two, with \(C=2t=2A/3\), for every \(t\ge1\).

**4. Classification at \(C=A-2\).** If \(C=A-2\), then \(A\ge3\). Equation (1) rules out the two high possibilities and gives \(A-2\le2A/3\), so \(A\le6\). It remains to exhaust the nonsquares \(A^2<D<(A+1)^2\) for \(A=3,4,5,6\), a finite set of \(36\) candidates. The recurrence above is exact integer arithmetic; its complete even-period outputs are as follows (pairs show \((D,C)\)):

| \(A\) | All even-period \((D,C)\) |
|---|---|
| 3 | (11,3), (12,2), (14,2), (15,1) |
| 4 | (18,4), (19,3), (20,2), (21,2), (22,4), (23,3), (24,1) |
| 5 | (27,5), (28,2), (30,2), (31,5), (32,1), (33,2), (34,4), (35,1) |
| 6 | (38,6), (39,4), (40,3), (42,2), (43,5), (44,2), (45,2), (46,6), (47,5), (48,1) |

The table is completely reproduced by the standalone exact-integer script `verify.py` (which explicitly loops over every integer in these four intervals and computes each least period). Reading off \(C=A-2\) gives exactly \(D=15,20,21,39\). Their least periods are respectively \(2,2,6,2\), proving the final assertion.

## Verification
Run `python3 verify.py` using Python 3. The program performs an exhaustive finite check of the decisive \(A=3,4,5,6\) intervals, checks every nonsquare \(2\le D\le100000\) against the midpoint relation and forbidden gap, and verifies the sharp family for \(1\le t\le500\). Observed results: `PASS: 99684 nonsquares through 100000, 88198 even periods`; `PASS: complete A=3..6 exceptional census [15, 20, 21, 39]`; and `PASS: sharp family, t=1..500`. The infinite claims rest on the exact argument above, not finite sample counts. The finite exceptional census *is* exhaustive because the proof reduces it to \(A\in\{3,4,5,6\}\).

## Relationship to prior work
Nimbran and Levrie (2023) investigate symmetric period patterns and concentrate specifically on midpoint values \(a_r=A\) and \(a_r=A-1\). The present theorem identifies the universal forbidden interval immediately below these values, gives an infinite family attaining its lower endpoint, and completely determines the first lower offset. The central reversal identities themselves are classical, not claimed as new. Riche (2024) derives parametrizations and parity restrictions for central partial quotients with prescribed surrounding patterns; his general constructions do not explicitly classify which central values can occur for a *fixed initial* quotient \(A\). The gap and four-case fixed-initial-quotient corollary require the denominator dichotomy in (3). The result does not claim all values \(1\le C\le\lfloor2A/3\rfloor\) are attained for each fixed \(A\).

## Limitations
The proof is elementary and depends on classical midpoint symmetry, so an older implicit or unindexed formulation may exist. The result is a necessary support restriction, not a full classification of attainable \((A,C)\) pairs. Riche's broader continued-fraction parametrization presents a material residual priority risk, since some inequalities may be extractable from it without being separately stated. A subsequent independent literature review is warranted; no independent audit is claimed.

## References
1. A. S. Nimbran and P. Levrie, *Patterns in Continued Fractions of Square Roots*, Journal of Integer Sequences **26** (2023), Article 23.2.8, published March 2, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Nimbran/nimbran14.pdf
2. S. Riche, *Parity of the central partial quotient of the continued fraction expansion of \(\sqrt D\)*, working paper, first posted July 1, 2024, revised October 28, 2024, DOI:10.33774/coe-2024-mmbtl-v2. https://www.cambridge.org/engage/coe/article-details/671d1d4e83f22e4214495946
3. A. S. Nimbran, *On the Structure of the Period of the continued fraction for \(\sqrt d\)*, arXiv:2207.06231, initial posting July 12, 2022. https://arxiv.org/abs/2207.06231
