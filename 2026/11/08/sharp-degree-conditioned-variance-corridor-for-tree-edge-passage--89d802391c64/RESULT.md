# Sharp degree-conditioned variance corridor for tree edge-passage times

## Finding

**Theorem.** Let \(T\) be any finite simple tree, let \(x\) and \(y\) be adjacent, and let \(S\) be the component containing \(x\) after the edge \(xy\) is deleted. Fix integers \(s=|S|\ge2\) and \(k=\deg_T(x)-1\), with \(1\le k\le s-1\). For discrete-time simple random walk begun at \(x\), let \(\tau_y=\inf\{t\ge0:X_t=y\}\). Write
\[
 s-1=ka+b,\qquad a\ge1,\quad 0\le b<k,\qquad t=s-k.
\]
Then, regardless of the rest of the tree on the \(y\)-side,
\[
 \mathbb E_x\tau_y=2s-1,
\]
and the variance satisfies the **sharp, simultaneous** bounds
\[
 \boxed{\;4s(s-1)+8\bigl[(k-b)a(a-1)+b a(a+1)\bigr]\;
 \le \operatorname{Var}_x(\tau_y)
 \le\;4s(s-1)+\frac83\bigl(t^3-t\bigr).\;}
\]
The lower equality holds exactly when the \(k\) rooted branches at \(x\) are stars rooted at their attachment vertices, with sizes \(a\) or \(a+1\) (exactly \(b\) of the latter). The upper equality holds exactly when one branch is a path of order \(s-k\) rooted at an endpoint, and the remaining \(k-1\) branches are single leaves. These characterizations are up to rooted isomorphism of the component \(S\); vertices and edges beyond \(y\) have no effect. If the two extremizers coincide in a small boundary case, both descriptions apply.

A separation consequence is that the mean, total order, starting degree and target degree together do not control hitting-time variance even within trees. Indeed, take \(s=2m+1\), \(k=m\) and make \(y\) a leaf for both extremizers. Their variances are
\[
 V_{\min}=16m^2+24m,
 \qquad V_{\max}=\frac83m^3+24m^2+\frac{40}{3}m,
 \qquad \frac{V_{\max}}{V_{\min}}\sim \frac m6.
\]
Both trees have \(2m+2\) vertices, \(\deg(x)=m+1\), \(\deg(y)=1\), and mean first-passage time \(4m+1\), while their variance ratio diverges.

## Assumptions and scope

The random walk is the ordinary **non-lazy** discrete-time walk, choosing uniformly among neighboring vertices at each step. The hitting time counts steps beginning at time zero and ends upon the first visit to \(y\). The edge \(xy\) is a bridge because \(T\) is a tree. The finite component \(S\) is rooted at \(x\), with \(k\) children; every other vertex has a unique parent toward \(x\). For each \(v\in S\), let \(s_v\) be the number of descendants of \(v\), including \(v\). All variance and expectation statements are exact; there are no asymptotic hypotheses in the main bound.

## Proof

**1. Edge-passage recursion.** For any vertex \(v\in S\), form the hitting time \(Z_v\) from \(v\) to its parent in the rooted tree with an absorbing parent edge. Write \(m_v=\mathbb EZ_v\), \(q_v=\mathbb EZ_v^2\), \(V_v=q_v-m_v^2\). If \(v\) has children \(c_1,\ldots,c_h\), then its degree for the stopped process is \(d=h+1\). By the strong Markov property, the first step goes directly to the parent with probability \(1/d\), or to child \(c\) with probability \(1/d\), leading to an excursion of length \(1+Z_c+Z_v'\), where \(Z_v'\) is independent and identically distributed with \(Z_v\). Thus
\[
 d m_v=d+\sum_c(m_c+m_v),
\]
so \(m_v=d+\sum_c m_c=2s_v-1\) by induction. Similarly,
\[
 d q_v=d+\sum_c\bigl[q_c+q_v+2m_c+2m_v+2m_cm_v\bigr],
\]
which gives \(q_v=\sum_cq_c+2m_v^2-d\) after using \(\sum_cm_c=m_v-d\). Subtracting \(m_v^2\), then inserting \(m_v=2s_v-1\) and \(m_c=2s_c-1\), yields the exact recurrence
\[
 V_v=4s_v(s_v-1)+\sum_c\bigl(V_c+4s_c(s_c-1)\bigr).
\]
Iterating it gives the **fringe-subtree identity**
\[
 \boxed{\;V_x=4s(s-1)+8\sum_{v\in S\setminus\{x\}}s_v(s_v-1).\;}
\]
All stopped moments are finite because the absorbing walk has a finite transient state space and a strictly positive probability of absorption in a bounded number of steps.

**2. Sharp lower bound.** Let the sizes of the \(k\) rooted child branches be \(t_1,\ldots,t_k\ge1\), summing to \(s-1\). Every child root contributes \(t_i(t_i-1)\) to the fringe-subtree sum, and all proper descendant contributions are nonnegative. Therefore
\[
 V_x\ge 4s(s-1)+8\sum_{i=1}^k t_i(t_i-1).
\]
Equality occurs exactly when no child branch has a non-root vertex whose fringe size is at least two: equivalently, every child branch is a star rooted at the child. Since \(u(u-1)\) is strictly discretely convex, replacing two unequal sizes \(u<v-1\) by \(u+1,v-1\) strictly decreases the sum. The unique minimizing multiset consists of \(k-b\) entries \(a\) and \(b\) entries \(a+1\). Substitution gives the claimed lower bound and its complete equality characterization.

**3. Sharp upper bound.** Define \(P(r)=\frac43r(r-1)(2r-1)\) and \(F(r)=P(r)+4r(r-1)=\frac83(r^3-r)\) for positive integers \(r\). We prove inductively that for every rooted tree of size \(r\), its parent-hitting variance is at most \(P(r)\), with equality exactly for a rooted path whose root is an endpoint. The claim is immediate for \(r=1\). If its child sizes are \(u_1,\ldots,u_j\), the variance recursion and induction give
\[
 V\le4r(r-1)+\sum_{i=1}^jF(u_i).
\]
The discrete first difference of \(F\) is \(F(u+1)-F(u)=8u(u+1)\), strictly increasing in \(u\ge1\). Repeatedly transferring one vertex from a smaller nontrivial child branch to a larger branch increases the sum. Consequently, among positive \(u_i\) of total \(r-1\), its unique maximizing multiset is \((r-j,1,\ldots,1)\), giving
\[
 V\le4r(r-1)+F(r-j)\le4r(r-1)+F(r-1)=P(r).
\]
For \(r\ge3\), equality in the final inequality forces \(j=1\), and equality in the inductive bound forces the only branch to be a rooted path. The \(r=1,2\) cases also have the asserted unique rooted shape. This establishes the induction. Now return to the prescribed root degree \(k\): the child variances are at most \(P(t_i)\), so again
\[
 V_x\le4s(s-1)+\sum_iF(t_i)\le4s(s-1)+F(s-k),
\]
with equality exactly when one child branch has size \(s-k\) and is a rooted path, all other children being leaves. This is the claimed upper bound and its complete equality characterization.

**4. Same-local-data dispersion gap.** With \(s=2m+1\) and \(k=m\), the balanced lower extremizer has \(m\) branches each of size two, giving \(V_{\min}=4(2m+1)(2m)+16m\). The upper extremizer has one branch of size \(m+1\) and \(m-1\) singleton branches, giving \(V_{\max}=4(2m+1)(2m)+\frac83((m+1)^3-(m+1))\). Simplification proves the displayed formulas and the ratio \(m/6+o(m)\). Adding one leaf \(y\) to each root produces two trees of the same total order with the same two marked degrees and the same mean, as asserted.

## Verification

The standalone file `verify.py` uses the finite absorbing transition matrix to calculate \(\mathbb E\tau_y\) and \(\operatorname{Var}(\tau_y)\) by exact rational linear algebra. It independently calculates each rooted fringe-subtree expression and the stated sharp bounds. It enumerates every nonisomorphic unrooted tree of orders two through eight and every choice of root, checks that the minima and maxima at every represented \((s,k)\) equal the formulas, and checks uniqueness up to rooted isomorphism. It also checks the displayed same-local-data variance formulas for \(2\le m<70\). Run: `python verify.py` (Python with `networkx` and `sympy`). These finite checks corroborate the recursions and boundary cases; **the induction, not enumeration, proves the theorem for all finite orders**.

## Relationship to prior work

Chiclana, *Nonconcentration of hitting times for random walks on graphs* (2026), proves general and tree-specific lower bounds on hitting-time variance and motivates quantitative dependence on tree geometry. Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, §5.3, Theorem 5.20, give a general, exact tree first-passage variance identity, which is acknowledged as underlying precedent for moment computations. The new point assessed here is the **degree-conditioned sharp optimization with all equality cases** and the linear-in-order possible variance separation with the same mean and marked degrees; these are not stated in the examined material. The general Aldous–Fill formula can be used as an alternative starting point, but deriving this degree-constrained extremal classification requires a distinct rooted-branch optimization.

The extremal expectations investigated by Meng Wang (2009), the cover-time results of Brightwell–Winkler (1990), and the tree hitting/meeting-time results of Beveridge et al. (2025) concern other functionals or optimization constraints. Their broad extremal terminology alone is not a match for the second-moment assertion here.

## Limitations

The bounds are for discrete-time simple random walk and a first traversal of an adjacent edge in a **tree**; they do not extend as stated to arbitrary non-tree graphs, arbitrary weighted or lazy transitions, or passage between nonadjacent endpoints. The theorem classifies variance extremizers, not distributions in stochastic or convex order. The general tree variance formula predates this result, and a historical source may have recorded this particular constrained optimization without indexed terminology; the priority assessment is provisional. The full text of the Wang honors thesis and the later parts of Chiclana's arXiv HTML were not accessible in the inspection; this is a concrete remaining literature risk. No independent mathematical audit has been performed.

## References

1. Rafael Chiclana, *Nonconcentration of hitting times for random walks on graphs* (2026), arXiv:2605.17513v1, first public date 2026-05-17. https://arxiv.org/abs/2605.17513
2. David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, §5.3, Theorem 5.20 (prepublication manuscript, 1996). https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch5.S3.html
3. Meng Wang, *Extremal Random Walks on Trees* (2009), Macalester honors project. https://digitalcommons.macalester.edu/mathcs_honors/12/
4. Graham Brightwell and Peter Winkler, *Extremal cover times for random walks on trees*, J. Graph Theory 14 (1990), 547–554. https://doi.org/10.1002/jgt.3190140505
5. Andrew Beveridge, Ben Bridenbaugh and Ari Holcombe Pomerance, *Random Walks and the Meeting Time for Trees* (2025), arXiv:2508.02804. https://arxiv.org/abs/2508.02804
