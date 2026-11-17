# Sharp one-step Gini norm for the half-lazy reflecting path walk

## Finding

For every integer \(n\ge 2\), let \(P_n\) be the half-lazy simple-random-walk operator on the unweighted \(n\)-vertex path, with genuine degree-one endpoints. On real signals define the complete-pair Gini seminorm \(G_n(f)=\sum_{1\le i<j\le n}|f_i-f_j|\). The exact **attained** induced seminorm is

\[
\|P_n\|_{G_n\to G_n}=\begin{cases}
0,&n=2,\\
\frac12,&n=3,\\
1-\frac{1}{2\lfloor n^2/4\rfloor},&4\le n\le 8,\\
1+\frac{n-9}{4(n-1)},&n\ge 9.
\end{cases}
\]

For \(4\le n\le8\), the indicator of a balanced initial segment attains the norm; for every \(n\ge9\), the indicator of the second vertex attains it. Thus this finite-step smoother is nonexpansive exactly when \(2\le n\le9\), with equality at \(n=9\) and strict amplification for \(n\ge10\). Its norm tends from below to \(5/4\) as \(n\to\infty\).

## Assumptions and scope

All vectors are real and indexed by \(1,\ldots,n\). The stochastic operator is defined, for \(n\ge3\), by

\[
(P_nf)_1=\frac{f_1+f_2}{2},\quad
(P_nf)_n=\frac{f_{n-1}+f_n}{2},\quad
(P_nf)_i=\frac{f_{i-1}+2f_i+f_{i+1}}4\quad(2\le i\le n-1).
\]

For \(n=2\), both outputs are \((f_1+f_2)/2\). The induced seminorm is the supremum of \(G_n(P_nf)/G_n(f)\) over nonconstant real signals, and is finite because \(P_n\) preserves constant signals. **One step only** is considered; the endpoints have degree one and no artificial self-loop before lazification. The unweighted Gini sum ranges over every unordered pair, not only graph edges and not stationary-distribution weights.

## Proof

**1. Binary-cut reduction.** The operator is positive and fixes constants. Translate and scale a nonconstant \(f\) into \([0,1]^n\), and write its layer-cake representation \(f_i=\int_0^1\mathbf 1_{\{f_i>t\}}\,dt\). Triangle inequality gives \(G_n(P_nf)\le\int_0^1G_n(P_n\mathbf 1_{S_t})\,dt\), whereas \(G_n(f)=\int_0^1|S_t|(n-|S_t|)\,dt\). Hence the exact norm is the maximum over **all** nonempty proper binary cuts \(S\):

\[
\|P_n\|_{G_n\to G_n}=\max_S\frac{G_n(P_n\mathbf1_S)}{|S|(n-|S|)}.
\]

**2. Exact leakage identity.** Assume \(n\ge4\), write \(k=|S|\), and put \(x=\mathbf1_S\), \(y=P_nx\). Since the holding probability at every site is at least \(1/2\), each \(y_i\) with \(i\in S\) is at least \(1/2\), and each \(y_j\) with \(j\notin S\) is at most \(1/2\). Let \(u_1,u_2\) count sites of \(S\) where the leakage \(1-y_i\) is respectively \(1/4,1/2\), and let \(v_1,v_2\) count sites of \(S^c\) where the leakage \(y_j\) is respectively \(1/4,1/2\). Zero-leakage sites do not enter these counts. Define

\[
F(a,b)=a^2+2ab+2b^2,\qquad
 d=x_2+x_{n-1}-x_1-x_n.
\]

Splitting the Gini sum into cross-cut and within-cut pairs, and using the level multiplicities \(0,1/4,1/2\), gives the exact identity

\[
\boxed{G_n(y)=k(n-k)+\frac{(n-2k)d-F(u_1,u_2)-F(v_1,v_2)}4.}\tag{1}
\]

Indeed, if \(A=(u_1+2u_2)/4\) and \(B=(v_1+2v_2)/4\), the cross-cut pairs contribute \(k(n-k)-(n-k)A-kB\), while the within-cut pairs contribute \(kA-F(u_1,u_2)/4+(n-k)B-F(v_1,v_2)/4\). Moreover \(B-A=d/4\), since interior neighbor exchanges balance but the two endpoint edges contribute an additional quarter unit toward the adjacent interior site. This proves (1) without an approximation.

Let \(C\) be the number of edges of the path separating \(S\) and \(S^c\). Let \(e_S\), respectively \(e_{S^c}\), count separating endpoint edges whose degree-one endpoint belongs to \(S\), respectively \(S^c\). Counting leakage in units of \(1/4\) yields

\[
u_1+2u_2=C+e_S,\quad v_1+2v_2=C+e_{S^c},\quad d=e_{S^c}-e_S.\tag{2}\]

The elementary bound \(F(a,b)\ge (a+2b)^2/2\) follows by completing the square. Also \(F(u_1,u_2)+F(v_1,v_2)\ge2\) for a proper nonempty cut, because some edge crosses and produces positive leakage on both sides.

**3. Boundary-imbalance estimate for \(n\ge9\).** Replacing \(S\) by its complement leaves the ratio invariant, so suppose \(1\le k\le\lfloor n/2\rfloor\). There are five possible values \(d\in\{-2,-1,0,1,2\}\).

If \(d\le0\), (1) and nonnegativity of \(n-2k\) give \(G_n(y)\le k(n-k)-1/2\), so the ratio is strictly below one.

If \(d=1\), exactly one endpoint edge points from an excluded endpoint to an included adjacent interior vertex and the other endpoint edge does not cross the cut. If \(C=2\), the included sites form a single interval starting next to the excluded endpoint and ending before the opposite endpoint. The two boundary patterns force \(F(u_1,u_2)\ge2\), \(F(v_1,v_2)\ge5\). If \(C\ge3\), (2) and the square bound yield
\[
F(u_1,u_2)+F(v_1,v_2)\ge\frac{C^2+(C+1)^2}{2}>7.
\]
The remaining possibility \(C=1\) would require \(k=n-1\), excluded by \(k\le n/2\). Thus always \(F(u_1,u_2)+F(v_1,v_2)\ge7\), and
\[
\frac{G_n(y)}{k(n-k)}\le1+\frac{n-2k-7}{4k(n-k)}\le1+\frac{n-9}{4(n-1)}.\tag{3}
\]
The last inequality holds because a positive numerator decreases, and the denominator increases, as \(k\) rises from one toward \(n/2\); when the numerator is nonpositive the ratio is at most one.

If \(d=2\), both endpoints are outside \(S\) and both adjacent vertices are inside. Hence \(k\ge2\). Since \(k\le n/2\) and \(n\ge9\), the included vertices cannot form the entire interior interval. Thus \(C\) is even and \(C\ge4\). When \(C\ge6\), equation (2) gives
\[
F(u_1,u_2)+F(v_1,v_2)\ge\frac{C^2+(C+2)^2}{2}\ge50.
\]
When \(C=4\), there are exactly two included runs, one adjoining each endpoint's interior neighbor. Their intervening excluded run has at least two sites: a single missing interior site would force \(k=n-3>n/2\). Consequently \(v_1=v_2=2\), so \(F(v_1,v_2)=20\), and (2) gives \(F(u_1,u_2)\ge C^2/2=8\). Thus in every case the deficit sum is at least \(28\). Inserting this in (1),
\[
\frac{G_n(y)}{k(n-k)}\le1+\frac{2n-4k-28}{4k(n-k)}.
\]
If the numerator is positive, its largest possible quotient over \(2\le k\le n/2\) occurs at \(k=2\), giving \(1+(n-18)/[4(n-2)]\), strictly below \(1+(n-9)/[4(n-1)]\); otherwise the quotient is at most one. This completes the upper bound for all cuts when \(n\ge9\).

To attain equality, set \(S=\{2\}\) (or symmetrically \(\{n-1\}\)). The nonzero outputs of \(P_n\mathbf1_S\) are \(1/2,1/2,1/4\) at the first three vertices. Direct pair counting gives \(G_n(P_n\mathbf1_S)=(5n-13)/4\), while \(G_n(\mathbf1_S)=n-1\). Their ratio is exactly the upper bound in (3).

**4. Small dimensions.** For \(n=2,\ldots,8\), the separate exact-integer exhaustive certificate `check_exact.py` enumerates all \(2^n-2\) proper nonempty binary cuts (494 cuts in total), evaluates each image Gini sum after integer scaling by four, compares rational ratios exactly, and records attaining cuts. Its complete exhaustive finite computation, combined with Step 1, proves the stated small-dimensional constants. At \(n=3\), a one-endpoint indicator attains \(1/2\); at \(4\le n\le8\), balanced initial intervals attain \(1-1/[2\lfloor n^2/4\rfloor]\). No inference from a finite sample to unbounded \(n\) is used: Step 3 separately proves all \(n\ge9\).

## Verification

Run `python3 check_exact.py` with Python 3 standard library. The included verifier exhaustively checks all 131038 nontrivial binary cuts for \(2\le n\le16\) against the stated exact rational coefficient, and independently checks second-vertex equality for \(9\le n\le400\). The essential finite proof uses only the fully enumerated range \(2\le n\le8\); computations at larger \(n\) are supplementary stress tests. All important unbounded-dimension quantifiers are treated analytically in Step 3. No external dataset or stochastic sampling is required.

## Relationship to prior work

Gaubert and Qu (2013) give the Dobrushin contraction coefficient for a Markov operator in the Hopf oscillation seminorm and the dual total-variation norm on distributions; neither equals the *primal* complete-pair Gini seminorm here. Prior analysis of the continuous-time degree-normalized path heat semigroup identifies the same first size at which some positive-time Gini amplification can occur, but does not supply the sharp coefficient of the **single, fixed, half-lazy discrete update**, its switch from balanced intervals to a one-vertex optimizer, or its \(5/4\) limiting gain. The proof here uses endpoint leakage classification and an exact two-class dispersion identity rather than a semigroup argument. General Gini-dispersion inequalities and alternative descriptions of reflecting Markov walks remain possible sources of equivalent historical results.

## Limitations

This theorem is restricted to a **single** half-lazy step, the **unweighted** path with degree-one endpoints, the unweighted complete-pair Gini seminorm on **real** signals, and the operator as explicitly normalized above. It does not give optimal constants for arbitrary holding probabilities, multiple steps, stationary-weighted Gini variation, or arbitrary weighted paths. The finite checks do not establish historical priority or independent mathematical validation; the source comparison does not exclude inaccessible or unindexed equivalents.

## References

1. Stéphane Gaubert and Zheng Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, initially public 21 February 2013, https://arxiv.org/abs/1302.5226 .
2. Stéphane Gaubert and Zheng Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, initially public 17 July 2013, https://arxiv.org/abs/1307.4649 .
