# Complete phase portrait of the ternary fourth-power digit map

## Finding
For a positive integer \(n=\sum_{i=0}^{k-1}d_i3^i\), with ternary digits \(d_i\in\{0,1,2\}\), define
\[
T(n)=\sum_{i=0}^{k-1}d_i^4.
\]
Every positive orbit under \(T\) enters exactly one of the three periodic orbits
\[
(1),\qquad(16,18),\qquad(17,33).
\]
Here \(T(1)=1\), \(T(16)=18\), \(T(18)=16\), \(T(17)=33\), and \(T(33)=17\). No other positive fixed points or cycles exist. Every even positive integer reaches the cycle \((16,18)\); every odd positive integer reaches the fixed point or the cycle \((17,33)\).

## Assumptions and scope
The map acts on all strictly positive integers, interpreted in ordinary nonnegative base-three positional notation (zero digits permitted inside the expansion). Ternary numbers are converted to ordinary integers for the cycle labels above. Iteration is deterministic; a periodic orbit means a finite cycle under repeated evaluation of \(T\). No assumption is made about the number of digits of the starting integer.

## Proof
**Strict descent from long strings.** Suppose \(n\) has \(k\ge5\) ternary digits. The lowest such integer is \(3^{k-1}\); each digit contributes at most \(2^4=16\) to \(T(n)\). Thus
\[
T(n)\le16k<3^{k-1}\le n.
\]
The strict inequality holds at \(k=5\) since \(80<81\); induction follows because \(3\cdot16k>16(k+1)\) for \(k\ge5\). Consequently, while an orbit is above \(80\), its terms strictly decrease as positive integers. Hence every positive orbit eventually enters \([1,80]\).

**Exact finite image.** Every integer between \(1\) and \(80\) has at most four ternary digits. If \(a\) counts digits equal to one and \(b\) counts digits equal to two, then
\[
T(n)=a+16b,\qquad a,b\in\mathbb Z_{\ge0},\quad1\le a+b\le4.
\]
Every such count pair occurs in some nonzero four-digit-or-shorter ternary word, so the complete image is exactly the following fourteen-element set:
\[
U=\{1,2,3,4,16,17,18,19,32,33,34,48,49,64\}.
\]
Here are **all** fourteen transitions. Each is obtained by the displayed definition from the unique ternary expansion of its source:

| Input | Image | Input | Image |
|---:|---:|---:|---:|
| 1 | 1 | 19 | 17 |
| 2 | 16 | 32 | 18 |
| 3 | 1 | 33 | 17 |
| 4 | 2 | 34 | 18 |
| 16 | 18 | 48 | 18 |
| 17 | 33 | 49 | 19 |
| 18 | 16 | 64 | 18 |

In particular, \(T(U)\subseteq U\). The arrows show that every trajectory in \(U\) reaches exactly one of \((1)\), \((16,18)\), \((17,33)\), and none of the remaining nine states is periodic. Since all positive trajectories reach \(U\), this finishes the global cycle classification.

**Parity separation.** In base three, \(3\equiv1\pmod2\), and for each ternary digit \(d\), \(d^4\equiv d\pmod2\). Therefore
\[
T(n)\equiv\sum_i d_i\equiv n\pmod2.
\]
The only even periodic orbit is \((16,18)\), so every even input must converge to it. Odd inputs reach one of the other two periodic orbits. This also establishes the stated basin separation without claiming a formula for which odd inputs reach \(1\).

## Verification
The included standalone `verify.py` reconstructs the fourteen states from all possible digit-count pairs, recomputes each arrow via integer base-three digit extraction, checks finite image closure, and independently examines the forward orbit of each of the eighty possible small positive starting values. The full deterministic stdout is in `verification_output.txt`. The infinite assertion does not rely on the finite test range: it follows from the strict descent argument, exact description of \(U\), and exhaustive fourteen-arrow table.

## Relationship to prior work
Grundman and Teeple (2007, Theorem 2.1 and Lemma 2.1) establish parity restrictions and arbitrarily long sequences of generalized happy numbers for all exponents in base three, but do not give the quartic ternary cycle set. Hargreaves and Siksek (2010, Theorem 1 and Section 3) give a general finite upper bound and an algorithm to obtain all cycles for an arbitrary base and exponent, illustrating instead decimal fourth powers and other examples; the present result is an explicit exact evaluation for the previously unstated pair of parameters. Goedhart, Gurtas, and Harris (2024 preprint, Sections 3–4) give general child-counting and tree descriptions and examples with other exponents/bases; those do not state these exact three cycles. The classical proof machinery makes this example accessible but does not supply its completed fourteen-transition certificate in the inspected publications.

## Limitations
This classification concerns only the fourth-power digit map in base three. It does not characterize the odd positive integers in each of the two odd basins by digit formulas or determine their asymptotic densities. No assertion is made about other bases or exponents. The general computability of the cycle set is already known, and novelty is limited to the explicit exact phase portrait for this pair; equivalent unindexed enumerations or existing tables are possible. Independent audit has not been performed.

## References
1. E. G. Goedhart, Y. Gurtas and P. E. Harris, *A tree approach to the happy function*, arXiv:2410.13990v1 (first public posting 17 October 2024), https://arxiv.org/html/2410.13990v1.
2. K. Hargreaves and S. Siksek, *Cycles and fixed points of happy functions*, Journal of Combinatorics and Number Theory 2 (2010), 217–229, accessible text at https://citeseerx.ist.psu.edu/document?doi=bc54f5857ba3b538dfe6876e922ae75597cc080d&repid=rep1&type=pdf.
3. H. G. Grundman and E. A. Teeple, *Sequences of generalized happy numbers with small bases*, Journal of Integer Sequences 10 (2007), Article 07.1.8, https://geodesic.mathdoc.fr/item/JIS_2007__10_1_a5/.
4. H. G. Grundman and E. A. Teeple, *Generalized happy numbers*, Fibonacci Quarterly 39 (2001), 462–466, https://www.fq.math.ca/Scanned/39-5/grundman.pdf.
