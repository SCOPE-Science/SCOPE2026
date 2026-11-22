# Eulerian cumulant sign staircases and reentrance in the biclique hard-core gas

## Finding

Consider the positive-activity hard-core lattice gas on the complete bipartite graph \(K_{m,n}\), with common activity \(z>0\), where \(m,n\geq1\). Write \(X_v\) for the occupation indicator at vertex \(v\). Mark \(r\) distinct vertices on the \(m\)-vertex shore and one vertex on the \(n\)-vertex shore, with integers \(2\leq r\leq m\). Let \(\kappa_{r+1}(z)\) be their **ordinary joint cumulant**, with all \(r+1\) variables appearing once. Put

\[
 x=1+z,\quad Z=x^m+x^n-1,\quad p=\frac{z}{x},\quad a=\frac{x^m}{Z},\quad b=\frac{x^n}{Z}.
\]

Define the polynomial

\[
 F_r(a)=\sum_{k=1}^{r}(-1)^k k!\,\left\{\!\begin{matrix}r\\k\end{matrix}\!\right\}a^k,
\]

where the braces denote Stirling numbers of the second kind. Then the **exact all-order identity** is

\[
 \boxed{\kappa_{r+1}(z)=b\,p^{r+1}F_r(a).}
\]

For every \(r\geq2\), \(F_r\) has precisely \(r-1\) distinct, simple roots in \((0,1)\). Denote these roots in increasing order by \(c_{r,1},\ldots,c_{r,r-1}\). The complete classification of positive-activity zeros and **sign reversals** is:

1. **Larger opposite shore** \(n>m\): exactly \(r-1\) simple positive-activity zeros, each a sign reversal, occurring successively at the unique solutions of \(a(z)=c_{r,j}\).
2. **Equal shores** \(n=m\): exactly \(\lfloor(r-1)/2\rfloor\) simple positive-activity zeros, each a sign reversal, corresponding exactly to the roots \(c_{r,j}>1/2\). If \(r\) is even, the root \(1/2\) is approached only as \(z\to\infty\), never reached at a finite activity.
3. **Larger marked shore** \(m>n\): let
   \[
   x_* = \left(\frac{m}{m-n}\right)^{1/n},\qquad
   a_* = \frac{x_*^m}{x_*^m+x_*^n-1}.
   \]
   Every root \(c_{r,j}>a_*\) is attained at exactly **two** positive activities and produces two sign reversals; every root equal to \(a_*\) gives exactly one tangential zero with **no** sign reversal; and roots below \(a_*\) are never attained. Thus the total number of sign reversals is exactly \(2\#\{j:c_{r,j}>a_*\}\).

The simplest explicit reentrant example uses \(K_{3,2}\), with all three sites on its larger shore and one on its smaller shore. Here

\[
 F_3(a)=-a(1-6a+6a^2),\qquad c_{3,2}=\frac{3+\sqrt3}{6}.
\]

Since \(a_*=3\sqrt3/(3\sqrt3+2)<c_{3,2}\), the fourth connected correlation has exactly two sign reversals, with signs **negative, positive, negative** as \(z\) increases. These occur at

\[
 z_1=0.2185163175\ldots,\qquad z_2=2.4113546067\ldots,
\]

where \(1+z_i\) are the two roots greater than one of

\[
 (1-c_{3,2})x^3-c_{3,2}x^2+c_{3,2}=0.
\]

No thermodynamic phase transition is asserted: all results concern finite Gibbs measures and connected correlations.

## Assumptions and scope

The graph is the simple complete bipartite graph with positive integers \(m,n\), the activity \(z\) is the same at every vertex, and the probability of an independent set \(I\) is \(z^{|I|}/Z\). The marked vertices are distinct, with exactly \(r\) in the first shore and one in the second, \(2\leq r\leq m\). The word *reversal* means a strict sign change through a finite positive-activity zero; an isolated tangential zero is not a reversal. The direction of the sign staircase is determined by the displayed polynomial, not by an unspecified sign convention.

## Proof

**1. Exact joint moments.** Every independent set of a complete bipartite graph lies wholly on one shore. Its partition function is

\[
 Z=(1+z)^m+(1+z)^n-1.
\]

For any nonempty selection of \(s\) distinct marked first-shore vertices, the occupation-product expectation is \(z^s(1+z)^{m-s}/Z=a p^s\); for the selected second-shore vertex it is \(bp\). Any joint moment containing at least one site on each shore vanishes, because simultaneous occupation is forbidden.

**2. Moment–cumulant inversion.** Apply the standard partition formula to \(r+1\) distinct variables. All nonzero contributing partitions must leave the one second-shore variable in a singleton block. If the \(r\) first-shore indices are divided into \(k\) nonempty blocks, there are \(\left\{\!\begin{smallmatrix}r\\k\end{smallmatrix}\!\right\}\) choices, each contributing the factor \((-1)^k k!\,b p^{r+1}a^k\). Summing proves the boxed identity with no approximation.

**3. Simple interior roots.** Let \(A_r(t)=\sum_{\pi\in S_r} t^{\operatorname{des}(\pi)}\) be the ordinary Eulerian polynomial. The identity \(\sum_{j\geq1}j^r t^j=tA_r(t)/(1-t)^{r+1}\) yields the polynomial equality

\[
 F_r(a)=-a(1-a)^{r-1}A_r\left(-\frac{a}{1-a}\right).
\]

Initially this follows by expanding \(1/(1-a+ae^u)\) at small \(a\), then everywhere by polynomial identity. For completeness, the Eulerian recurrence

\[
 A_{r+1}(t)=(1+rt)A_r(t)+t(1-t)A'_r(t)
\]

proves inductively that \(A_r\) has \(r-1\) *simple negative* roots. At each negative root of \(A_r\), the sign of \(A_{r+1}\) is that of \(t(1-t)A'_r(t)\), alternating along the roots. Together with \(A_{r+1}(0)=1\) and its leading sign as \(t\to-\infty\), the intermediate-value theorem supplies one new root in each of the \(r\) disjoint intervals. Degree \(r\) proves there are no others. Base \(A_1=1\), \(A_2=1+t\). The change of variables \(t=-a/(1-a)\) maps negative roots bijectively into \((0,1)\), preserving simplicity.

**4. Activity geometry.** For \(x>1\), elementary differentiation gives

\[
 \frac{da}{dx}=\frac{x^{m-1}\bigl((m-n)x^n-m\bigr)}{(x^m+x^n-1)^2}.
\]

If \(m<n\), the function decreases strictly from \(1\) to \(0\). If \(m=n\), it decreases strictly from \(1\) to \(1/2\). Eulerian coefficient symmetry makes \(A_r\) reciprocal; its negative roots pair as reciprocals and the corresponding \(a\)-roots pair as \(c\leftrightarrow1-c\). When \(r\) is even, one is \(c=1/2\), giving exactly \(\lfloor(r-1)/2\rfloor\) roots in \((1/2,1)\). Finally if \(m>n\), the derivative changes once, from negative to positive, at \(x_*\), while \(a\) begins and ends at \(1\). Every level between \(a_*\) and \(1\) is therefore attained exactly twice and transversely; the minimum is attained once with quadratic tangency. Since \(b p^{r+1}>0\), these observations give precisely the stated sign classifications.

**5. Reentrant five-site example.** For \(m=3,n=2,r=3\), \(x_*=\sqrt3\) and \(a_*=3\sqrt3/(3\sqrt3+2)\). The smaller Eulerian zero \((3-\sqrt3)/6\) lies below \(a_*\), while \((3+\sqrt3)/6>a_*\). The first and last signs are both negative because \(F_3(1)=-1\), whereas between the two crossings \(F_3(a)>0\). The two crossing activities solve the displayed cubic and are simple by the strict derivative signs on opposite sides of \(x_*\).

## Verification

The standalone file `verify_cumulants.py` constructs all hard-core independent sets on each test graph, evaluates their exact rational moments, assembles the joint cumulant directly using the full set-partition formula, and independently compares it to the closed Stirling-polynomial expression. Running `python verify_cumulants.py` gives `MIXED_CUMULANTS_EXACT: 392` and `K_3_2_REENTRANT_SIGNS: [-1, 1, -1]`. Cases include all \(2\leq m\leq6\), \(1\leq n\leq7\), \(2\leq r\leq\min(m,5)\), and four rational positive activities. These tests are finite corroboration, **not** the all-orders proof, which is given above. The irrational crossing values are obtained from a polynomial root calculation rather than from an exhaustive finite grid.

## Relationship to prior work

The hard-core model and bipartite independent-set partition functions are standard. Kahn (2001) develops hard-core occupation and counting bounds for regular bipartite graphs. Galvin (arXiv:1206.3206, publicly posted 14 June 2012) analyzes the independent-set polynomial and the extremal status of complete bipartite graphs; in Section 3, the biclique polynomial appears explicitly. These statements supply the established partition-function context but do not give the cross-shore all-order mixed cumulant, the Eulerian-root sign classification, or the two-crossing five-site response. The Eulerian-polynomial real-rootedness theorem is classical; Athanasiadis (2025) discusses its mathematical context. The contribution here is the specific identification and exact finite-system sign diagram, **not** a new real-rootedness theorem. Related work on hard-core crown-graph precision and Widom–Rowlinson occupancy uses different observables or measures and does not imply this classification directly.

## Limitations

No statement is made for arbitrary bipartite graphs, inhomogeneous fugacities, repeated-site cumulants, multiple marked sites from the opposite shore, positive-temperature singularities, or thermodynamic phase transitions. The result is a closed structural corollary of an elementary biclique partition function plus the established Eulerian-root phenomenon, and its novelty claim is limited to the combined cross-shore cumulant sign law; a historical unindexed equivalent calculation remains possible. No independent scientific audit has been carried out.

## References

1. J. Kahn, *An Entropy Approach to the Hard-Core Model on Bipartite Graphs*, Combinatorics, Probability and Computing 10 (2001), 219–237, https://doi.org/10.1017/S0963548301004631 (first verified public online date: 2001-06-25).
2. D. Galvin, *Two problems on independent sets in graphs*, arXiv:1206.3206, first posted 2012-06-14, https://arxiv.org/abs/1206.3206 (see particularly Sections 1 and 3).
3. C. A. Athanasiadis, *On the real-rootedness of the Eulerian transformation*, Journal of the London Mathematical Society (2025), https://doi.org/10.1112/jlms.70083 (classical Eulerian-root background and related transformations).
