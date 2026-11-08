# Exactly five consecutive Lucas–Niven terms in infinitely many step-two progressions

## Finding
Let \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\). Let \(s_L(n)\) count the ones in the unique legal Lucas representation of \(n\), and call \(n\) Lucas–Niven if \(s_L(n)\mid n\). For an integer \(J\ge9\), set \(N_J=L_J+23\). Then
\[
\bigwedge_{r=0}^{4}s_L(N_J+2r)\mid(N_J+2r)
\quad\Longleftrightarrow\quad J\equiv7,13\pmod{24}.
\]
For every such \(J\), neither immediate step-two neighbor \(N_J-2\) nor \(N_J+10\) is Lucas–Niven. These are therefore infinitely many maximal five-term runs in step-two arithmetic progressions. The smallest member of this constructed family begins at \(N_{13}=544\), giving \(544,546,548,550,552\).

If \(R(X)=\#\{J\ge9:N_J\le X,\ J\equiv7,13\pmod{24}\}\), then
\[
R(X)=\frac{\log X}{12\log\varphi}+O(1),\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
Here starting points are distinct because Lucas numbers increase strictly at these indices. This is a count of a specified family, not a count of all five-term runs.

## Assumptions and scope
A legal Lucas representation is a finite sum of *distinct* Lucas numbers with no two consecutive indices selected, and with indices \(0\) and \(2\) not both selected. Brown's canonical decomposition theorem, stated as Theorem 1.2 in Lao et al., gives existence and uniqueness. Divisibility is ordinary integer divisibility. The theorem concerns the consecutive five terms of a step-two progression and the two immediately adjacent step-two positions, for every integer \(J\ge9\), without an upper bound.

## Proof
Write \(H=L_J\). The seven low offsets, from left immediate neighbor through right immediate neighbor, have the following legal Lucas representations:

| Offset \(t\) | Low-index sum representing \(t\) | Number of summands in \(H+t\) |
|---:|---|---:|
| 21 | \(L_6+L_2=18+3\) | 3 |
| 23 | \(L_6+L_3+L_1=18+4+1\) | 4 |
| 25 | \(L_6+L_4=18+7\) | 3 |
| 27 | \(L_6+L_4+L_0=18+7+2\) | 4 |
| 29 | \(L_7=29\) | 2 |
| 31 | \(L_7+L_0=29+2\) | 3 |
| 33 | \(L_7+L_3=29+4\) | 3 |

All displayed low-index sums satisfy both canonical restrictions, and \(J\ge9\) leaves a gap of at least two between \(J\) and the largest low index, which is \(7\). Adding \(L_J\) thus gives legal representations. By uniqueness, these are the canonical representations for all seven values \(H+t\), and the final-column digit counts are exact.

For the five interior offsets, Lucas–Niven divisibility is equivalent, in the displayed order, to
\[
4\mid H+23,\quad 3\mid H+25,\quad 4\mid H+27,\quad 2\mid H+29,\quad 3\mid H+31.
\]
The two conditions modulo four are identical, as are the conditions modulo three. The modulus-two condition follows from the modulus-four condition. By the Chinese remainder theorem, all five conditions hold exactly when
\[
H\equiv1\pmod4,\quad H\equiv2\pmod3
\quad\Longleftrightarrow\quad L_J\equiv5\pmod{12}.
\]
The recurrence modulo \(12\) is periodic: direct iteration gives \((L_{24},L_{25})\equiv(L_0,L_1)\equiv(2,1)\pmod{12}\); the recurrence then repeats the entire sequence modulo \(12\) with period dividing \(24\). Inspection of its \(24\) values shows
\[
\{r\in\{0,1,\ldots,23\}:L_r\equiv5\pmod{12}\}=\{7,13\}.
\]
This proves the if-and-only-if statement for every \(J\ge9\).

For the immediately preceding and following step-two positions the digit sum is three, from the first and last rows of the table. The five-term condition implies \(H\equiv2\pmod3\). Thus \(H+21\equiv H+33\equiv2\pmod3\), and neither neighbor is Lucas–Niven. This proves maximality in the step-two progression.

Finally the Binet identity \(L_J=\varphi^J+(1-\varphi)^J\), where \(0<|1-\varphi|<1\), implies the largest possible index with \(L_J+23\le X\) is \(\log X/\log\varphi+O(1)\). Exactly two residue classes out of every \(24\) consecutive indices qualify, giving \(R(X)=\log X/(12\log\varphi)+O(1)\). The proof is algebraic and covers infinitely many indices; no finite search is extrapolated.

## Verification
Run `python3 verify_lucas.py` using only the Python standard library. It independently enumerates all legal Lucas representations with low indices at most \(17\), confirms uniqueness and coverage of the full guaranteed range below \(L_{18}\), and compares them with a greedy canonical generator. It also verifies every displayed low-digit pattern, the residue classes modulo \(24\), maximal-neighbor obstructions, and the theorem for all indices \(9\le J\le300\). The finite checks are cross-checks; the preceding proof is valid for all \(J\ge9\).

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong, and Zhang prove that every arithmetic progression contains infinitely many Lucas–Niven numbers (Theorem 3.4 of their 2026 paper). Their consecutive-term results in Sections 4–5 concern **Zeckendorf–Niven**, not Lucas–Niven, numbers. Infinitely many isolated runs with five simultaneous Lucas–Niven terms in step-two progressions do not follow from individual-term infinitude. OEIS A351714 records Lucas–Niven integers; OEIS A351716 records runs of three **consecutive integers** (step one), not step-two five-term progressions. A published construction of Zeckendorf–Niven five-runs does not establish the distinct Lucas digit restrictions. The indicated restricted-family count and the two-sided maximality are not supplied by those sources. Mathematical research-record searches found no covering theorem; this does not prove global priority.

## Limitations
No assertion is made about the maximum possible run length among all Lucas–Niven step-two progressions, or about the density of every such run. The growth law counts only starting points of the explicit one-high-digit family. Independent historical-priority verification is not available; potentially unindexed equivalent work remains a risk. The numeric verifier checks finitely many cases and does not independently prove the infinite statement.

## References
1. K. Lao, S. J. Miller, N. Rosa, M. Shiliaev, G. Tresch, T. W. H. Wong, and H. Zhang, *On Zeckendorf-Niven Numbers and Arithmetic Progressions*, arXiv:2606.24006v1 (publicly posted June 22, 2026), https://arxiv.org/html/2606.24006v1, especially Theorem 1.2, Theorem 3.4, and Sections 4–5.
2. *The On-Line Encyclopedia of Integer Sequences*, A351714, Lucas–Niven numbers, https://oeis.org/A351714.
3. *The On-Line Encyclopedia of Integer Sequences*, A351716, Starts of runs of three consecutive Lucas–Niven numbers, https://oeis.org/A351716.
4. H. G. Grundman, *Consecutive Zeckendorf-Niven and lazy-Fibonacci-Niven numbers*, Fibonacci Quarterly 45 (2007); DOI: 10.1080/00150517.2007.12428220.
