# 2-rainbow domination polynomial of complete split graphs
## Finding
For integers \(r,n\ge 2\), let \(S_{r,n}=K_r\vee\overline{K_n}\), with clique part \(C\) of size \(r\) and independent part \(I\) of size \(n\). A 2-rainbow dominating function is a map
\[
f:V(S_{r,n})\to\{\varnothing,\{1\},\{2\},\{1,2\}\}
\]
such that every vertex labeled \(\varnothing\) sees both colors among its neighbors. Its weight is \(w(f)=\sum_{v\in V(S_{r,n})}|f(v)|\). Define the all-weight enumerator
\[
\mathcal R_{r,n}(x)=\sum_f x^{w(f)},
\]
where the sum ranges over all 2-rainbow dominating functions. Then
\[
\mathcal R_{r,n}(x)
=(1+x)^{2r}(2x+x^2)^n
-2x^n\bigl((1+x)^r-x^r\bigr)
+\bigl((1+x)^{2r}-2(1+x)^r+1\bigr)
 \bigl((1+x)^{2n}-(2x+x^2)^n\bigr).
\]
In particular,
\[
\gamma_{r2}(S_{r,n})=2.
\]
The number of minimum-weight functions is \(r^2+2\) when \(n=2\), and \(r^2\) when \(n\ge3\). The total number of 2-rainbow dominating functions is
\[
4^r3^n-2(2^r-1)+(4^r-2^{r+1}+1)(4^n-3^n).
\]

## Assumptions and scope
The graph is finite, simple, and has \(r,n\ge2\). This range isolates the genuinely complete-split regime: when \(r=1\) the graph is a star and belongs to the already studied complete-multipartite class, while \(n=1\) gives a complete graph. Colors \(1\) and \(2\) are distinguished, as in the standard definition of 2-rainbow domination.

## Proof
Write \(A=(1+x)^2=1+2x+x^2\) for the weight polynomial of the four possible labels on one unrestricted vertex, and \(B=2x+x^2\) for the weight polynomial of the three nonempty labels.

First suppose no vertex of \(I\) is empty. If no vertex of \(C\) is empty either, every labeling is feasible and contributes \(B^{r+n}\). If at least one clique vertex is empty, every such empty clique vertex sees all other vertices, so feasibility is equivalent to requiring both colors somewhere outside that empty vertex. Starting from \(B^n(A^r-B^r)\), exactly two monochromatic families violate this condition: for either color, every independent vertex must carry that singleton color and the clique may use only the empty label or that same singleton, with at least one empty clique vertex. Their combined weight polynomial is
\[
2x^n\bigl((1+x)^r-x^r\bigr).
\]
Thus the case with no empty independent vertex contributes
\[
A^rB^n-2x^n\bigl((1+x)^r-x^r\bigr).
\]

Now suppose at least one vertex of \(I\) is empty. Such a vertex has neighborhood exactly \(C\), so both colors must occur on the clique. By inclusion-exclusion, clique labelings containing both colors have weight polynomial
\[
A^r-2(1+x)^r+1.
\]
The independent side is otherwise unrestricted but must contain an empty label, contributing
\[
A^n-B^n.
\]
Multiplying these independent choices gives the third term in the displayed formula. The two cases are disjoint and exhaustive, proving the enumerator.

The coefficient of the smallest positive weight is at weight \(2\). For \(n\ge3\), a minimum function either assigns \(\{1,2\}\) to one clique vertex, or assigns \(\{1\}\) and \(\{2\}\) to two distinct clique vertices; there are \(r+r(r-1)=r^2\) such functions. When \(n=2\), there are two additional functions obtained by placing the two singleton colors on the two independent vertices. Evaluating the enumerator at \(x=1\) gives the stated total count.

## Verification
The proof is symbolic and valid for every \(r,n\ge2\). The accompanying `verify.py` independently implements the literal neighborhood definition and exhaustively checks all \(4^{r+n}\) labelings for every pair \(2\le r,n\le4\). It compares every weight coefficient with the closed formula and separately checks the minimum coefficient and total count. Its replay output is:

`VERIFY_OK r_range=2..4 n_range=2..4 labelings=112896 coefficient_checks=117 minimum_checks=9 total_checks=9 max_order=8`

The finite replay is a boundary and transcription check, not an extrapolation to arbitrary order.

## Relationship to prior work
Rainbow domination was introduced in the early Cartesian-product literature, and the standard 2-rainbow parameter is classified under MSC 05C69. A foundational paper proves a weight-preserving bijection between \(k\)-rainbow dominating functions of a graph \(G\) and dominating sets of \(G\square K_k\). Therefore the formula above is simultaneously the ordinary domination polynomial of \(S_{r,n}\square K_2\).

Prior work on 2-rainbow domination establishes complexity, bounds, and exact minimum values for several graph classes. General domination-polynomial work supplies recurrence and splitting machinery. Searches of those sources and of indexed literature did not locate an all-weight formula for complete split graphs or for their \(K_2\)-prisms. A nearby all-weight result for complete multipartite graphs does not cover \(S_{r,n}\) when \(r\ge2\), because the vertices of \(C\) are mutually adjacent.

## Limitations
The theorem concerns the classical two-color rainbow domination model and the complete-split family only. It does not address \(k\)-rainbow domination for \(k>2\), arbitrary split graphs, or asymptotic root properties of the polynomial. The literature comparison reduces but cannot eliminate the possibility of a poorly indexed equivalent formula.

## References
1. B. Brešar, M. A. Henning, D. F. Rall, “Paired-domination of Cartesian products of graphs and rainbow domination,” *Electronic Notes in Discrete Mathematics* 22 (2005), 233–237. DOI:10.1016/j.endm.2005.06.059.
2. B. Brešar, M. A. Henning, D. F. Rall, “Rainbow domination in graphs,” *Taiwanese Journal of Mathematics* 12 (2008), 213–225. DOI:10.11650/twjm/1500602498.
3. B. Brešar, T. Kraner Šumenjak, “On the 2-rainbow domination in graphs,” *Discrete Applied Mathematics* 155 (2007), 2394–2400. DOI:10.1016/j.dam.2007.07.018.
4. T. Kotek, J. Preen, F. Simon, P. Tittmann, M. Trinks, “Recurrence Relations and Splitting Formulas for the Domination Polynomial,” *Electronic Journal of Combinatorics* 19(3) (2012), P47. DOI:10.37236/2475.
