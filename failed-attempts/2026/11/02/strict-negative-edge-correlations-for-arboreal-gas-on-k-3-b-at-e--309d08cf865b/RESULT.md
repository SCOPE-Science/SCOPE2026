# Strict negative edge correlations for arboreal gas on \(K_{3,b}\) at every fugacity

## Finding

For every integer \(b\ge 2\) and every real edge fugacity \(x>0\), let \(F\) be a random spanning forest of the complete bipartite graph \(K_{3,b}\), including isolated vertices, with probability proportional to \(x^{|F|}\). For any two distinct graph edges \(e\ne f\),

\[
\mathbb{P}_x(e,f\in F)<\mathbb{P}_x(e\in F)\mathbb{P}_x(f\in F).
\]

The assertion is strict for each positive fugacity, including the uniform forest distribution \(x=1\). It holds simultaneously for all sizes, including non-series-parallel graphs \(K_{3,b}\) with \(b\ge3\). The three different edge-pair orbits have explicit Rayleigh-difference factors with strictly positive coefficients, given below.

## Assumptions and scope

Fix \(b\in\mathbb{Z}\) with \(b\ge2\). Label the left vertices \(0,1,2\) and the right vertices \(1,\ldots,b\). A spanning forest here means **any acyclic subset of graph edges**, not necessarily a connected tree; vertices without incident edges are retained as isolates. Write

\[
Z_b(x)=\sum_{F\subseteq E(K_{3,b}):\,F\text{ acyclic}}x^{|F|},\qquad
\mathbb{P}_x(F)=\frac{x^{|F|}}{Z_b(x)}.
\]

All edge activities are the **same** positive real number \(x\). We do not assert the corresponding result for arbitrary different edge weights, higher left-part sizes, or full negative association for disjoint collections of edge events.

## Proof

**1. Classification of acyclic right-column patterns.** A right vertex is adjacent to a subset of the three left vertices of size zero, one, two, or three. If a right column has degree three, every other column must have degree at most one: any other degree-two column creates a cycle through that degree-three vertex. Otherwise, degree-two columns correspond to edges on the three left vertices; to avoid cycles there can be at most two, and if there are two, their two unordered left-vertex pairs must be distinct. Degree-zero and degree-one columns cannot create cycles. Conversely, each configuration permitted by these rules is acyclic, since after suppressing degree-two right vertices its left-vertex multigraph is a forest on three vertices.

Set \(a=1+3x\): a column of degree zero or one contributes total weight \(a\). The preceding classification gives

\[
\begin{split}
Z_b(x)&=a^b+b(3x^2+x^3)a^{b-1}+3b(b-1)x^4a^{b-2}\\
&=a^{b-2}H_b(x),\\
H_b(x)&=1+6x+(9+3b)x^2+10bx^3+3b^2x^4.
\end{split}
\]

**2. Single-edge and double-edge weights.** All \(3b\) edges are equivalent. Fix one edge \(e\) and let \(U_b(x)=\sum_{F\ni e}x^{|F|}\). Differentiating the partition function by the common fugacity gives \(U_b=xZ'_b/(3b)\). Direct differentiation and factorization yield

\[
U_b(x)=a^{b-3}A_b(x),\qquad
A_b(x)=x\bigl[1+8x+19x^2+10x^3+b(3x^2+14x^3+6x^4)+3b^2x^4\bigr].
\]

There are exactly three orbits for two distinct edges: \(R\), edges in the same right column; \(L\), edges in different right columns sharing one left vertex; and \(D\), edges in different right columns with different left endpoints. Write \(V_O(x)=\sum_{F\ni e,f}x^{|F|}\), with orbit \(O\in\{R,L,D\}\). Counting the two designated columns using the same acyclicity classification gives \(V_O=a^{b-4}B_O\), where

\[
\begin{aligned}
B_R&=x^2a^2\bigl[1+4x+(2b+1)x^2\bigr],\\
B_L&=x^2\bigl[1+10x+(31+3b)x^2+(24+18b)x^3+(3b^2+12b)x^4\bigr],\\
B_D&=x^2\bigl[1+10x+(32+3b)x^2+(30+18b)x^3+(3b^2+12b+9)x^4\bigr].
\end{aligned}
\]

For completeness, set \(q=b-2\), and let \(Z_q=a^q+q(3x^2+x^3)a^{q-1}+3q(q-1)x^4a^{q-2}\) (the terms with zero integer coefficients vanish when \(q=0,1\)). The same-right double-edge weight is \(V_R=x^2(1+x)a^{b-1}+2(b-1)x^4a^{b-2}\). For different-right edges, the weight from both designated columns being singletons is \(x^2Z_q\); exactly one designated column of degree two contributes \(4x^3[a^q+2qx^2a^{q-1}]\). The remaining choices contribute \(4x^4a^q\) for type \(L\) and \(5x^4a^q\) for type \(D\): these include one degree-three column, or two distinct degree-two pair types. These expressions expand to the three displayed \(B_O\).

**3. Positive polynomial certificates.** Put \(\Delta_O=A_b^2-H_bB_O\), so that the desired covariance equals

\[
\operatorname{Cov}_x(\mathbf 1_{\{e\in F\}},\mathbf 1_{\{f\in F\}})
=-\frac{a^{2b-6}\Delta_O(x,b)}{Z_b(x)^2}.
\]

Write \(t=b-1\), which is positive. Exact polynomial expansion gives \(\Delta_R=x^4(b-1)P_R\), where

\[
\begin{aligned}
P_R={}&9t^3x^6+t^2(18x^6+48x^5+12x^4)\\
&+t(9x^6+66x^5+106x^4+46x^3+6x^2)\\
&+18x^5+75x^4+98x^3+52x^2+12x+1.
\end{aligned}
\]

Similarly \(\Delta_D=x^4P_D\), where

\[
\begin{aligned}
P_D={}&9b^2x^6+18b^2x^5+7b^2x^4\\
&+30bx^5+73bx^4+44bx^3+7bx^2\\
&+19x^4+56x^3+44x^2+12x+1.
\end{aligned}
\]

Finally, \(B_D-B_L=x^4a^2\), hence \(\Delta_L=\Delta_D+x^4a^2H_b\). Every summand in the displayed factors is nonnegative for \(b\ge2\), \(t\ge1\), and \(x>0\), with strictly positive constant terms in \(P_R,P_D\). Also \(H_b>0\). Thus \(\Delta_R,\Delta_D,\Delta_L>0\). Since \(Z_b>0\), the covariance is strictly negative for each of the three orbits. They exhaust all distinct edge pairs, proving the claim. \(\square\)

## Verification

Run `python3 verify.py` with Python's standard library. It independently enumerates *all* edge subsets of \(K_{3,b}\) for \(2\le b\le5\), rejects cycles using a union-find algorithm, and compares exact partition, single-edge, and the three joint-edge sums at fugacities \(1/2,1,3/2,2\). It also certifies the displayed polynomial identities on a Cartesian integer grid: all relevant polynomial differences have degree at most four in \(b\) and at most ten in \(x\), so vanishing at five distinct values of \(b\) and eleven of \(x\) is an exact interpolation proof. The script reports `VERIFY_OK 308 independent exact rational and polynomial comparisons`. These calculations check the algebraic identities and small-graph classification; the general result also uses the analytic acyclicity argument and positivity of the coefficient certificates.

## Relationship to prior work

Grimmett and Winkler (2003) formulated the uniform-forest negative edge-correlation conjecture and verified finite graphs by computation. Erickson (2010) proved a stronger multivariate Rayleigh sum-of-squares certificate for **series-parallel** graphs; \(K_{3,b}\) for \(b\ge3\) is not series-parallel. Stones (2014) counted labelled spanning forests of general \(K_{m,n}\) by their number of edges, but that unmarked count does not determine simultaneous inclusion of two specified edges. Bauerschmidt, Crawford, Helmuth and Swan (first public version December 10, 2019) study the positive-fugacity arboreal gas model motivating this question. Bencs and Csikvári (2021) explicitly describe edge negative correlation in uniform forests as a conjecture. Çiçeksiz and Ravichandran (2026) obtain general-graph sufficiently-large-fugacity results under transfer-current assumptions, not every positive fugacity for the infinite biclique family. Gupta (2026) proves an all-size result for complete **non-bipartite** graphs at unit fugacity, not this family. These comparisons do not constitute exhaustive historical priority certification; independently validating the theorem and checking potentially overlooked specialized literature remains appropriate.

## Limitations

The result concerns homogeneous positive fugacity on \(K_{3,b}\) and pairwise edge indicators only. It does not prove multivariate Rayleigh positivity for all edge-specific weights, full negative association, or the unrestricted graph conjecture. Exact polynomial checks are self-contained but have not received independent review; none of the referenced publications should be interpreted as endorsing this calculation.

## References

- G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs* (2003), https://arxiv.org/abs/math/0302185.
- A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs* (first version 2010), https://arxiv.org/abs/1008.3660.
- R. J. Stones, *Computing the number of spanning forests in a complete bipartite graph* (2014), https://dmtcs.episciences.org/articles/1248.
- R. Bauerschmidt, N. Crawford, T. Helmuth and A. Swan, *Random spanning forests and hyperbolic symmetry* (first posted 2019-12-10), https://arxiv.org/abs/1912.04854.
- F. Bencs and P. Csikvári, *An upper bound for the number of spanning forests of a regular graph* (2021), https://arxiv.org/abs/2105.06801.
- R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the q<1 Random Cluster Model* (2026), https://arxiv.org/abs/2610.00549.
- A. Gupta, *Edges of the uniform random forest of K_n are pairwise negatively correlated for every n* (2026), https://arxiv.org/abs/2609.26134.
