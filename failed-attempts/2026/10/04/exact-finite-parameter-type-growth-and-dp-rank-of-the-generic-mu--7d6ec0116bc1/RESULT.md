# Exact finite-parameter type growth and dp-rank of the generic multi-order
## Finding
For integers \(n,r\ge 1\), let \(M_n\) be the Fraïssé limit of all finite sets carrying \(n\) named linear orders. If \(A\subseteq M_n\) has \(m\) elements, define \(N_{n,r}(m)=|S_r(A)|\). Then \(N_{n,r}(m)\) depends only on \(m,n,r\), not on the induced multi-order on \(A\), and
\[
N_{n,r}(m)=\sum_{b=1}^r {r\brace b}\sum_{t=0}^b \binom bt (m)_t\left((m+1)^{\overline{b-t}}\right)^n.
\]
Here \({r\brace b}\) is a Stirling number of the second kind, \((m)_t=m(m-1)\cdots(m-t+1)\), and \((m+1)^{\overline s}=(m+1)(m+2)\cdots(m+s)\), with the empty product equal to \(1\). Hence
\[
N_{n,r}(m)=\Theta(m^{nr}),
\]
and the dp-rank of the full \(r\)-variable home sort is exactly \(nr\). In particular \(M_n\) has unary dp-rank \(n\).

For orientation, \(N_{1,1}(m)=2m+1\), while for the generic permutation \(M_2\),
\[
N_{2,1}(m)=m^2+3m+1,
\]
and
\[
N_{2,2}(m)=m^4+8m^3+19m^2+16m+5.
\]

## Assumptions and scope
The language consists only of the named linear orders. Types are complete first-order types over a finite set of real parameters in the home sort. The claim concerns finite \(n,r,m\); it makes no assertion about imaginaries, expansions, reducts, or types over infinite parameter sets.

## Proof
The generic \(n\)-multi-order eliminates quantifiers. Thus a complete \(r\)-type over \(A\) is determined by equality data together with, for each named order, the relative order of the tuple and \(A\).

First partition the \(r\) variable indices according to equality. Suppose the partition has \(b\) blocks; there are \({r\brace b}\) choices. Choose \(t\) of those blocks to be equal to parameters from \(A\), and inject those blocks into \(A\). This contributes \(\binom bt(m)_t\) choices. The remaining \(s=b-t\) blocks name distinct new elements outside \(A\).

Fix one of the \(n\) orders. Since the order already induced on the \(m\) named parameters is fixed, the number of total orders on the \(m+s\) elements extending that parameter order is
\[
\binom{m+s}s s!=\frac{(m+s)!}{m!}=(m+1)^{\overline s}.
\]
The \(n\) named orders are independent in the age, so the choices multiply to \(((m+1)^{\overline s})^n\). Every resulting finite multi-order extension is realized over \(A\) by the Fraïssé extension property, and quantifier elimination makes two different data sets different complete types. Summing over \(b\) and \(t\) gives the displayed formula.

The polynomial degree is \(nr\). Indeed a summand indexed by \(b,t\) has degree
\[
t+n(b-t)=nb-(n-1)t\le nr.
\]
For \(n>1\), equality occurs only at \(b=r,t=0\); for \(n=1\), the terms with \(b=r\) have degree \(r\). In all cases the leading coefficient is positive, so \(N_{n,r}(m)=\Theta(m^{nr})\).

For the dp-rank upper bound, suppose there were an ICT-pattern of depth \(d>nr\) in \(r\) object variables. Restrict each row to its first \(q\) entries. The union of the coordinates of these parameter tuples has size \(O(q)\). The ICT choice functions yield \(q^d\) distinct complete \(r\)-types over that union, because changing a row changes which instance is true and the pattern includes the negations of all nonchosen instances. But the exact count above is \(O(q^{nr})\), contradiction for arbitrarily large \(q\). Hence dp-rank is at most \(nr\).

For the lower bound, index \(nr\) rows by pairs \((a,i)\) with \(1\le a\le r\) and \(1\le i\le n\). In order \(<_i\), choose disjoint macro-intervals \(B_{1,i}< _i\cdots< _i B_{r,i}\), and inside each \(B_{a,i}\) choose infinitely many pairwise disjoint open intervals \(I_{a,i,j}=(u_{a,i,j},v_{a,i,j})\). Use
\[
\varphi_{a,i}(x_1,\ldots,x_r;u,v):=u<_i x_a<_i v.
\]
Each row is pairwise inconsistent. For any choice of one interval from every row, the chosen constraints prescribe one nonempty interval for each coordinate in each named order; the macro-interval ordering also fixes compatible cross-coordinate orders. The finite-extension property of the generic multi-order realizes all \(r\) points simultaneously. Because the intervals in each row are disjoint, all nonchosen instances are false. This is an ICT-pattern of depth \(nr\), proving the reverse inequality.

## Verification
The symbolic counting argument was checked against an independent finite enumerator bundled as `artifacts/verify.py`. For small \(m,n,r\), it enumerates equality partitions, parameter identifications, and all order extensions directly, then compares the resulting count with the closed formula. It also checks the displayed low-dimensional polynomials. The finite computation is a replay aid, not a substitute for the Fraïssé and ICT arguments.

## Relationship to prior work
Guingona and Hill introduced generic \(n\)-multi-orders as the Fraïssé limits of finite \(n\)-orders and record quantifier elimination for their theories. They also relate multi-order dimension to dp-rank. Simon later places the same generic multi-orders inside the classification of primitive rank-one NIP \(\omega\)-categorical structures and explicitly frames that program using polynomial growth of types over finite sets. The inspected sources do not state the exact finite-parameter \(r\)-type formula above or the resulting all-arity equality \(\operatorname{dp-rk}(M_n^r)=nr\).

## Limitations
The formula uses the pure generic multi-order. Adding definable or named structure can change finite-parameter type counts, and reducts can lower dp-rank. The originality search covered the primary multi-order papers, exact phrase searches, and a semantic database, but a short observation of this kind could exist in unindexed notes or folklore.

## References
Pierre Simon, “NIP \(\omega\)-categorical structures: the rank 1 case,” arXiv:1807.07102; Proc. London Math. Soc. 125 (2022), 1253–1331.

Vincent Guingona and Cameron Donnay Hill, “On a common generalization of Shelah's 2-rank, dp-rank, and o-minimal dimension,” arXiv:1307.4113; Ann. Pure Appl. Logic 166 (2015), 502–525.

Vincent Guingona and Miriam Parnes, “Ranks based on strong amalgamation Fraïssé classes,” arXiv:2007.02922; Arch. Math. Logic 62 (2023), 889–929.
