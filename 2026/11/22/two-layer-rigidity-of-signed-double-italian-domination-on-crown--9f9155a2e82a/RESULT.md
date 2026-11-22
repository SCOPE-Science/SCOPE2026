# Two-layer rigidity of signed double Italian domination on crown graphs

## Finding
Let \(C_n=K_{n,n}-M\) be the crown graph with bipartition \(\{u_1,\ldots,u_n\}\) and \(\{v_1,\ldots,v_n\}\), where \(u_i v_i\) are the deleted edges and \(n\ge4\). Let \(a_i=f(u_i)\) and \(b_i=f(v_i)\). A signed double Italian dominating function (SDIDF) assigns labels in \(L=\{-1,1,2,3\}\), requires each closed-neighborhood sum to be at least \(1\), and requires that the sum of positive neighboring labels is at least \(3\) at every vertex labeled \(-1\), and at least \(2\) at every vertex labeled \(1\). Its weight is the sum of all vertex labels. Let \(D_n(z)=\sum_f z^{w(f)}\), summed over all SDIDFs on \(C_n\).

Write \(Q(t)=1+t^2+t^3+t^4\). The minimum possible weight is \(2\), and the lowest two weight coefficients are exactly
\[
[z^2]D_n(z)=[t^{n+1}]Q(t)^n,
\qquad
[z^3]D_n(z)=2n\left([t^{n-1}]Q(t)^{n-1}+[t^{n-2}]Q(t)^{n-1}\right).
\]
Every weight-\(2\) function has \(a_i=b_i\) for all \(i\), with \(\sum_i a_i=1\); conversely **all** such duplicated label vectors are valid when \(n\ge4\). Every weight-\(3\) function has exactly one mismatched deleted pair, on which the labels are \((2,1)\) or \((3,2)\), or the reverse; all other pairs have equal labels. For \((2,1)\) the common labels on the remaining \(n-1\) pairs sum to \(0\), and for \((3,2)\) they sum to \(-1\); the same descriptions with the shore orientation reversed are exhaustive and sufficient.

Among weight-\(2\) SDIDFs, exactly \(E_n\) are **not** signed double Roman dominating functions (SDRDFs), where
\[
E_n=\begin{cases}
\binom{n}{(n-1)/2},& n\ge5\ \text{odd},\\
n\binom{n-1}{n/2},& n\ge4\ \text{even}.
\end{cases}
\]
These excluded functions use no label \(3\) and at most one label \(2\). The signed double Roman minimum itself is known from prior work; it is not asserted here as a new result. At \(n=4\), all twelve Italian minima are excluded, while at every \(n\ge5\) some Italian minima are also Roman minima. The connected boundary \(n=3\) has exactly three weight-\(2\) SDIDFs and no weight-\(3\) SDIDFs; it is excluded from the displayed \(n\ge4\) coefficient formulas.

## Assumptions and scope
Graphs are finite, undirected, and simple. The crown graph has all cross-edges \(u_i v_j\) for \(i\ne j\) and no within-shore edges. The defense condition used here is the original signed double Italian condition: for labels \(-1\) or \(1\) a suitable **subset** of the open neighborhood has sum at least \(3\) or \(2\), respectively. Because the permitted labels are \(-1,1,2,3\), existence of such a subset is equivalent to the stated positive-neighbor-sum test. It is not the stronger signed double Roman requirement of a \(3\)-neighbor or two \(2\)-neighbors at a \(-1\) vertex.

The polynomial \(D_n\) counts labeled vertices and uses integer weight (there can be negative individual labels). Only the first two coefficients, rather than the complete polynomial, are determined by the displayed formulas.

## Proof
Set \(A=\sum_i a_i\), \(B=\sum_i b_i\), and \(W=A+B\). The closed-neighborhood sums at the nonadjacent pair \(u_i,v_i\) are
\[
S_i=B+a_i-b_i,\qquad T_i=A+b_i-a_i,\qquad S_i+T_i=W.
\]
Each is at least \(1\), so \(W\ge2\). If \(W=2\), necessarily \(S_i=T_i=1\) for every \(i\), giving \(a_i-b_i=1-B\) for every \(i\). Summing over \(i\), and using \(A+B=2\), yields \((n-2)(1-B)=0\). Since \(n\ge3\), \(A=B=1\) and \(a_i=b_i\) for all \(i\).

Conversely, suppose \(a_i=b_i=c_i\), with \(\sum_i c_i=1\). All closed-neighborhood sums are then exactly \(1\). Write \(r\) for the number of indices where \(c_i=-1\); the sum of the positive labels on either shore is \(1+r\). A vertex labeled \(-1\) sees all positive opposite-shore labels, so its defense threshold is met exactly when \(r\ge2\). A vertex labeled \(1\) sees the same positive labels except its own matched label \(1\), again needing \(r\ge2\). A vector of sum \(1\) on \(n\ge4\) positions must have at least two negative entries: with at most one, its sum is at least \(n-2\ge2\). Hence every such duplicated vector is admissible; existence follows from \((-1,-1,1,2)\) at \(n=4\), from \((n+1)/2\) negative entries, two entries labeled \(2\) and \((n-5)/2\) entries labeled \(1\) for odd \(n\ge5\), and from \((n+2)/2\) negative entries, one \(2\), one \(3\) and \((n-6)/2\) ones for even \(n\ge6\). The exponent shift \(c_i\mapsto c_i+1\in\{0,2,3,4\}\) gives the stated coefficient \([t^{n+1}]Q(t)^n\). For \(n=3\), only permutations of \((-1,-1,3)\) survive; permutations of \((-1,1,1)\) fail the defense condition.

Now assume \(W=3\) and \(n\ge4\). Since \(S_i+T_i=3\) and both are at least \(1\), each \(S_i\) belongs to \(\{1,2\}\). Summation gives \(n\le\sum_iS_i=3+(n-2)B\le2n\), forcing the integer \(B\in\{1,2\}\). If \(B=1\), then \(A=2\) and all differences \(a_i-b_i\) lie in \(\{0,1\}\), with total sum \(A-B=1\). Exactly one difference is \(1\), and it must be \((a_i,b_i)=(2,1)\) or \((3,2)\). The other coordinates agree and sum to \(0\) or \(-1\), respectively. If \(B=2\), interchange the shores to obtain the reversed versions. These possibilities also ensure the closed-neighborhood inequalities.

For sufficiency of the defense conditions, any \(n-1\ge3\) common labels with sum \(0\) or \(-1\) must contain at least two occurrences of \(-1\); otherwise their total would be at least \(n-3\ge1\). Let the number of those negative entries be \(r\ge2\). Their positive-label sum is \(r\) in the sum-\(0\) case and \(r-1\) in the sum-\((-1)\) case. After adjoining \((2,1)\) or \((3,2)\), the full-shore positive-label sums are \(r+2\) and \(r+1\). A common \(-1\) vertex sees the entire opposite positive-label sum (at least \(3\)); a common \(1\) vertex sees that sum minus \(1\) (at least \(2\)). At the mismatched pair, only the vertex labeled \(1\) in \((2,1)\) has an additional requirement; it sees positive sum \(r\ge2\). All defense conditions hold. For each orientation, the mismatched position has \(n\) choices, and the common labels are arbitrary vectors of length \(n-1\) with sum \(0\) or \(-1\). Mapping each label \(c\) to exponent \(c+1\) gives the second formula.

Finally, a duplicated weight-\(2\) vector with at least two \(-1\) entries meets the stronger SDRDF rescue test exactly when it contains a \(3\) or at least two \(2\)'s. Indeed, either choice defends every \(-1\) and every \(1\); otherwise no \(-1\) has enough Roman defenders. The excluded vectors have no \(3\) and zero or one \(2\). In the zero-\(2\) case the sum-\(1\) constraint implies \(n\) odd and exactly \((n-1)/2\) negative entries, giving \(\binom{n}{(n-1)/2}\) labelings. In the one-\(2\) case \(n\) is even and exactly \(n/2\) of the remaining positions are negative, giving \(n\binom{n-1}{n/2}\). This proves the exclusion formula.

## Verification
The included `direct_crown.cpp` enumerates independently every labeling in \(\{-1,1,2,3\}^{2n}\) for \(3\le n\le6\), directly constructs each graph's adjacency lists, checks the closed-neighborhood sums, checks both Italian and Roman defender tests, and counts both Italian weight layers. It examines \(4^{2n}\) assignments for each \(n\), including \(16,777,216\) at \(n=6\). The included `symbolic_crown.py` obtains the low-weight coefficients by convolution of the four-label sum distributions for \(4\le n\le10\). They agree:

| \(n\) | Italian weight \(2\) | Italian weight \(3\) | Excluded Roman minima |
|---:|---:|---:|---:|
| 4 | 12 | 48 | 12 |
| 5 | 40 | 140 | 10 |
| 6 | 90 | 420 | 60 |
| 7 | 266 | 1330 | 35 |
| 8 | 672 | 3920 | 280 |

The direct verifier independently finds Roman minimum weight \(4\) when \(n=4\), and \(2\) when \(n=3,5,6\). The general formulas rest on the proof above, not finite computation.

## Relationship to prior work
A. Almulhim introduced signed double Italian domination in 2023 and determined minimum weights on paths, stars, cycles and the Petersen graph, without giving the crown-graph two-layer census in the inspected full article. In published mathematical research records, a signed double Roman \(k\)-domination theorem already determines the **stronger** Roman minimum on every crown graph, including the exception at \(n=4\). Its proof establishes duplication of paired labels at the Roman lower bound, but does not classify the larger Italian admissible family or its next weight layer. Consequently the scalar Roman optimum and the implied Italian lower-bound equality for \(n\ge5\) are not claimed as new. Other cited crown enumerations involve ordinary Italian, double Italian, perfect double Italian or signed total domination, each with different label and defense rules; their stated polynomials do not imply the present coefficients.

## Limitations
These results cover only the two lowest Italian weight layers on the connected crown graph family with \(n\ge4\), not a complete weight polynomial or arbitrary matching-deleted bipartite graphs. The literature comparison cannot rule out unindexed tables or differently named equivalent findings. Independent mathematical validation has not been performed.

## References
1. A. Almulhim, “Signed double Italian domination,” *AIMS Mathematics* 8 (2023), 30895–30909, published 2023-11-17. https://doi.org/10.3934/math.20231580 (full-text PDF: https://www.aimspress.com/aimspress-data/math/2023/12/PDF/math-08-12-1580.pdf).
2. M. A. Henning and L. Volkmann, “More results on the signed double Roman \(k\)-domination in graphs,” *Aequationes Mathematicae* 99 (2025), 1903–1921. https://doi.org/10.1007/s00010-025-01192-3.
3. “Signed double Roman \(k\)-domination of crown graphs,” published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-signed-double-roman-k-domination-of-crown-graphs--92f84e53e13a (scientific RESULT.md inspected).
4. “Complete Italian-domination polynomial and low-weight threshold for crown graphs,” published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-italian-domination-polynomial-and-low-weight-threshold--3564a580a47e (search summary inspected).
