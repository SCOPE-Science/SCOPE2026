# The sharp near-one stability threshold for four-term Egyptian underapproximation

## Finding

Put \(\beta=41/42\). For \(\theta\in(\beta,1]\), let \(a(\theta)=\lfloor1/(\theta-\beta)\rfloor+1\). An Egyptian four-term underapproximation is a nondecreasing integer quadruple \(2\le x_1\le x_2\le x_3\le x_4\) for which \(\sum_{i=1}^4 1/x_i<\theta\). Its value is that sum; a best underapproximation has the largest admissible value.

**Theorem.** For every real \(\theta\in(629/630,1]\), the unique best four-term Egyptian underapproximation is the greedy tuple \((2,3,7,a(\theta))\). The lower endpoint is sharp in the sense that for every \(\theta\in(599/600,629/630]\), the greedy tuple is \((2,3,7,46)\) and is strictly beaten by \((2,3,8,25)\).

A sharper auxiliary statement isolates the arithmetic reason: among all nondecreasing integer quadruples whose reciprocals sum to less than \(1\), whose first three denominators differ from \((2,3,7)\), and whose sum exceeds \(41/42\), the unique largest sum is \(599/600\), realized by \((2,3,8,25)\).

## Assumptions and scope

All denominators are positive integers and may repeat; the first is at least \(2\). All comparisons are *strict* underapproximations. The real parameter is unrestricted except for the displayed interval. The theorem concerns exactly four summands, not arbitrary lengths or the full phase diagram below \(599/600\).

## Proof

**Step 1 (three-term extremum).** The classical Curtiss–Takenouchi/Sylvester optimality theorem implies that every nondecreasing triple \((u,v,w)\), with \(2\le u\le v\le w\) and \(1/u+1/v+1/w<1\), obeys
\[
\frac1u+\frac1v+\frac1w\le\frac12+\frac13+\frac17=\beta,
\]
with equality only for \((2,3,7)\). This is the three-term instance of the best-underapproximation theorem recalled in Nathanson's Section 4. Therefore a four-term tuple whose total is below \(1\) either starts with \((2,3,7)\) or has a triple prefix of sum \(s<\beta\).

**Step 2 (exhaustive finite bound for the other prefixes).** Suppose a four-term tuple with a non-special triple prefix has value greater than \(\beta\). At depth \(j\in\{0,1,2\}\), write \(s_j=\sum_{i=1}^j1/x_i\) (with \(s_0=0\)). Since subsequent denominators are at least \(x_{j+1}\), a necessary condition is
\[
\beta<s_j+\frac{4-j}{x_{j+1}},\qquad
x_{j+1}<\frac{4-j}{\beta-s_j}.
\]
Also require \(x_{j+1}\ge x_j\) when \(j>0\) and \(s_j+1/x_{j+1}<1\). These strict rational inequalities have only the following possible triples, grouped by their first two entries. The right column is the **largest** value strictly below \(1\) obtainable by completing any triple in the indicated range with a fourth denominator at least its third:

| First two denominators | Possible third denominators | Largest completed value excluding \((2,3,7)\) |
| --- | --- | --- |
| \((2,3)\) | \(8,9,10,11,12,13\) | \(599/600\) |
| \((2,4)\) | \(5,6,7,8\) | \(419/420\) |
| \((2,5)\) | \(5,6,7\) | \(119/120\) |
| \((2,6)\) | \(6\) | \(41/42\) |
| \((3,3)\) | \(4,5,6\) | \(155/156\) |
| \((3,4)\) | \(4,5\) | \(59/60\) |
| \((4,4)\) | \(4\) | \(19/20\) |

To verify the table entries without any cutoff assumption: the first bound forces \(x_1\in\{2,3,4\}\); applying it successively with the ordering constraint gives precisely the seven first-two groups and the listed third denominators, together with the single special triple \((2,3,7)\). For a triple of sum \(s<1\) and third denominator \(z\), the smallest legal last denominator is exactly
\[
m(s,z)=\max\left\{z,\left\lfloor\frac1{1-s}\right\rfloor+1\right\},
\]
so its maximal completed value is \(s+1/m(s,z)\). Substituting the finite listed third-denominator ranges and comparing rational numbers gives the right column. For example, \((2,3,8)\) has \(s=23/24\), so \(m=25\) and \(s+1/m=599/600\). The next-largest row maximum is \(419/420<599/600\), and within the first row the only maximizer is \((2,3,8,25)\). Every unlisted quadruple with a non-special triple prefix has value at most \(\beta<599/600\). This proves the auxiliary statement.

**Step 3 (unique greedy optimum above the threshold).** For \(\theta>629/630>\beta\), the first three greedy denominators are \((2,3,7)\); this follows from \(1/2+1/3+1/6=1\) and the strict greedy inequalities. The fourth is \(a(\theta)=\lfloor1/(\theta-\beta)\rfloor+1\), so its sum \(G(\theta)=\beta+1/a(\theta)\) is strictly below \(\theta\). Since \(\theta-\beta>1/45\), we have \(a(\theta)\le45\) and
\[
G(\theta)\ge\beta+\frac1{45}=\frac{629}{630}>\frac{599}{600}.
\]
By Step 2, no tuple with a different triple prefix can match \(G(\theta)\). Among tuples with prefix \((2,3,7)\), strict underapproximation forces the last denominator to be at least \(a(\theta)\), with equality uniquely maximizing their sum. Thus the greedy tuple is the unique best.

**Step 4 (sharp endpoint).** If \(599/600<\theta\le629/630\), then
\[
\frac1{46}<\theta-\beta\le\frac1{45},
\]
so the greedy last denominator equals \(46\). Its value is
\[
\beta+\frac1{46}=\frac{482}{483}<\frac{599}{600}
=\frac12+\frac13+\frac18+\frac1{25}<\theta.
\]
Hence the other displayed tuple strictly improves it throughout the entire asserted half-open interval, including the threshold itself. This completes the proof.

## Verification

`check_egyptian4.py` uses exact `fractions.Fraction` arithmetic to regenerate the complete finite list from the strict algebraic bounds. It finds \(21\) candidate triple prefixes (one special and \(20\) other), verifies each group's maximum and the unique non-special maximum \(599/600\). A separately structured four-coordinate enumeration finds exactly \(103\) non-special quadruples with sum strictly between \(41/42\) and \(1\), all bounded above by \(599/600\). Rational test points check both sides of the threshold. The finite enumeration is exhaustive because the displayed inequalities prove every relevant next denominator lies in the loop's finite range; the results are not extrapolated from a truncated search.

## Relationship to prior work

Nathanson's *Underapproximation by Egyptian fractions* (first public version 2022-02-01; journal 2023) establishes a general greedy framework and determines best two-term cases; its Section 8 asks for a better understanding of greedy failures and uniqueness for \(n\ge3\). Its recalled Curtiss–Takenouchi theorem supplies the three-term extremal bound used here, but none of those results states the present sharp real interval or the maximal non-special four-term sum. Chu's 2023 paper gives a threshold in the **two-term** problem, not the four-term classification. Kovač–Tang's 2026 eventual optimality results for rational inputs concern sufficiently long expansions, not this fixed four-term real interval. A non-indexed equivalent of the four-term second-best calculation could exist.

## Limitations

This determines the first sharp transition below \(1\) for the **four-term** greedy algorithm, not a global description of all exceptional intervals. It does not show what is best for parameters at or below \(599/600\). A separate independent mathematical review has not been conducted.

## References

1. M. B. Nathanson, *Underapproximation by Egyptian fractions*, arXiv:2202.00191 (first posted 2022-02-01), especially Sections 1, 4, 7, and 8. https://arxiv.org/html/2202.00191v2
2. H. V. Chu, *A Threshold for the Best Two-term Underapproximation by Egyptian Fractions*, arXiv:2306.12564 (2023). https://arxiv.org/abs/2306.12564
3. V. Kovač and Q. Tang, *Eventually greedy best Egyptian underapproximations of rational numbers via optimal control*, arXiv:2607.28387 (2026). https://arxiv.org/abs/2607.28387
