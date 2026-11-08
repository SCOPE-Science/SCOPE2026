# Two sharp laziness thresholds for meeting on complete bipartite graphs

## Finding

Let \(m\ge s\ge1\), \(m\ge2\), and let two independent walkers start at distinct vertices of the connected complete bipartite graph \(K_{m,s}\). At each synchronous discrete step, each walker independently stays put with probability \(p\in(0,1)\) and otherwise moves to a uniformly chosen neighbor. Let \(\tau\) be the first positive time at which their positions coincide. Write \(H_L\) for \(\mathbb E[\tau]\) when the two initial vertices are in the part of size \(m\); write \(H_S\) when both are in the size-\(s\) part (defined only for \(s\ge2\)); and write \(H_X\) for opposite-part starts. All means are finite and

\[
H_L=\frac{2m(2s+p-1)}{(1-p^2)(m+s+p-1)},\qquad
H_S=\frac{2s(2m+p-1)}{(1-p^2)(m+s+p-1)},
\]

where the second formula is relevant only when \(s\ge2\), and

\[
H_X=\frac{1}{2p(1-p)}+\frac{m-1}{2m}H_L+\frac{s-1}{2s}H_S.
\]

**Complete phase diagram.** If \(m>s\ge2\), there are unique thresholds \(\alpha_{m,s}\) and \(\beta_{m,s}\) with

\[
\frac{5-\sqrt{17}}4<\alpha_{m,s}<\frac13<\beta_{m,s}<\frac12
\]

such that, with strict inequalities outside the threshold values,

\[
\begin{array}{ll}
0<p<\alpha_{m,s}:& H_L<H_S<H_X,\\
\alpha_{m,s}<p<\beta_{m,s}:& H_L<H_X<H_S,\\
\beta_{m,s}<p<1:& H_X<H_L<H_S.
\end{array}
\]

At \(p=\alpha_{m,s}\) only \(H_X=H_S\), while at \(p=\beta_{m,s}\) only \(H_X=H_L\). Define

\[
F_{a,b}(p)=\bigl(2(a-b)+3\bigr)p^2+(a+5b-4)p-(a+b-1).
\]

Then \(\alpha_{m,s}\) is the unique root in \((0,1)\) of \(F_{s,m}\), and \(\beta_{m,s}\) is the unique root in \((0,1)\) of \(F_{m,s}\). The bounds are sharp across the family: for each fixed \(s\ge2\), as \(m\to\infty\), \(\alpha_{m,s}\to(5-\sqrt{17})/4\) and \(\beta_{m,s}\to1/2\).

If \(m=s\ge2\), the same-part configurations have equal means and \(p=1/3\) is the unique parameter at which **all distinct starting pairs** have the same mean, namely \(H_L=H_S=H_X=9m/4\). Below \(1/3\) same-part starts meet sooner in mean; above \(1/3\) opposite-part starts meet sooner in mean.

If \(s=1<m\) (a star), only \(H_L\) and \(H_X\) are realizable. They have exactly one crossover, at the unique root \(\beta_{m,1}\in(1/3,1/2)\) of \(F_{m,1}\): \(H_L<H_X\) below it and \(H_X<H_L\) above it.

## Assumptions and scope

All graphs are finite, simple, unweighted complete bipartite graphs with no edge loops. The two walkers use independent random choices and move **simultaneously** at every unit-time step; any coincidence at a vertex ends the observation. Edge swaps without a common vertex do **not** count as meeting. Both walkers have the same fixed holding probability \(p\in(0,1)\). The initial vertices are distinct; if the initial vertices coincide, the first meeting time is zero by a different convention. \(H_S\) is not a realizable class when \(s=1\), and there is no realizable same-part class in \(K_{1,1}\), which is excluded.

The primary assertion is an ordering of **mean** meeting times across initial positions for a prescribed holding probability. It is not an optimization of holding probability itself, nor an assertion about stochastic ordering of meeting-time distributions.

## Proof

**Step 1: Three-class absorbing chain.** Write \(q=1-p\). The pre-meeting state of the pair is determined, up to graph automorphism, by the classes \(L\) (both distinct in the size-\(m\) part), \(S\) (both distinct in the size-\(s\) part), and \(X\) (opposite parts). Including a formal, unreachable class when \(s=1\), their substochastic transition matrix is

\[
Q=\begin{pmatrix}
p^2&q^2(s-1)/s&2pq\\
q^2(m-1)/m&p^2&2pq\\
pq(m-1)/m&pq(s-1)/s&p^2+q^2
\end{pmatrix}.
\]

For example, from \(L\), both walkers moving gives the same new vertex in the opposite part with probability \(q^2/s\), which is absorption; otherwise, if both move, they land at different opposite-part vertices, giving \(S\). From \(X\), one stays and the other moves into its part; this yields a meeting if and only if the mover selects the occupied vertex. There is a positive probability of meeting within a bounded number of steps from every realizable class: one walker can remain stationary while the other follows a path of length at most two. Finiteness and \(p,q>0\) thus imply almost-sure absorption with finite mean. Consequently the first-step equations \(H=\mathbf1+QH\) have a unique solution on realizable classes.

**Step 2: Solve the recurrences.** The first-step equations are

\[
\begin{aligned}
H_L&=1+p^2H_L+q^2\frac{s-1}{s}H_S+2pqH_X,\\
H_S&=1+q^2\frac{m-1}{m}H_L+p^2H_S+2pqH_X,\\
H_X&=1+pq\frac{m-1}{m}H_L+pq\frac{s-1}{s}H_S+(p^2+q^2)H_X.
\end{aligned}
\]

The third equation gives

\[
H_X=\frac1{2pq}+\frac{m-1}{2m}H_L+\frac{s-1}{2s}H_S.
\]

Substitution into the first two equations and elementary elimination gives the explicit expressions for \(H_L\) and \(H_S\) in the Finding section. When \(s=1\), transitions from the realizable classes never enter the formal \(S\) class, so the same formula for \(H_L,H_X\) follows directly from the remaining two equations.

Subtracting the formulas yields, with a strictly positive common denominator \(D=2p(1-p^2)(m+s+p-1)\),

\[
H_L-H_X=\frac{F_{m,s}(p)}D,\qquad
H_S-H_X=\frac{F_{s,m}(p)}D,
\]

and

\[
H_L-H_S=-\frac{2(m-s)}{(1+p)(m+s+p-1)}.
\]

The last comparison applies only to realizable classes and proves \(H_L<H_S\) whenever \(m>s\ge2\), for every \(p\in(0,1)\).

**Step 3: The two unique crossings.** If \(m\ge s\ge1\), the derivative of \(F_{m,s}\) is positive throughout \([0,1]\), because its quadratic coefficient \(2(m-s)+3\) and linear coefficient \(m+5s-4\) are positive. For \(F_{s,m}\), its derivative is linear and is positive at both endpoints: at \(0\) it equals \(s+5m-4>0\), and at \(1\) it equals \(5s+m+2>0\). Thus both polynomials are strictly increasing on \([0,1]\). Both start at \(-(m+s-1)<0\); both end at \(2(m+s)>0\), so each has exactly one zero in \((0,1)\).

Direct substitution gives

\[
F_{m,s}(1/3)=-\frac{4(m-s)}9,\quad
F_{s,m}(1/3)=\frac{4(m-s)}9,\quad
F_{m,s}(1/2)=s-\frac14>0.
\]

If \(m>s\ge2\), the two roots therefore lie strictly on opposite sides of \(1/3\), and the larger lies below \(1/2\). For the lower universal bound set \(r=(5-\sqrt{17})/4\), the smaller root of \(-2r^2+5r-1=0\). The remaining terms give

\[
F_{s,m}(r)=s(2r^2+r-1)+(3r^2-4r+1)
\le\frac{75-19\sqrt{17}}8<0,
\]

where \(2r^2+r-1=(11-3\sqrt{17})/2<0\) and \(s\ge1\). Hence the lower zero exceeds \(r\). Combining signs of the two differences with \(H_L<H_S\) proves all three regimes and both ties.

For fixed \(s\), dividing \(F_{s,m}\) and \(F_{m,s}\) by \(m\) and letting \(m\to\infty\) gives the limiting quadratics \(-2p^2+5p-1\) and \(2p^2+p-1\), whose unique roots in \((0,1)\) are \(r\) and \(1/2\), respectively. Monotonicity and endpoint signs guarantee convergence of the zeros, proving sharpness.

**Step 4: Equal part sizes and stars.** For \(m=s\), symmetry gives \(H_L=H_S\) and

\[
F_{m,m}(p)=(p-1/3)(3p+6m-3).
\]

The second factor is strictly positive on \((0,1)\) for \(m\ge2\), giving the unique crossover at \(1/3\). Substituting \(p=1/3\) into \(H_L\) gives \(9m/4\), and the vanishing difference proves equality with \(H_X\). For \(s=1\), discard the unrealizable \(S\) class and use the unique root of \(F_{m,1}\), which lies strictly between \(1/3\) and \(1/2\). This completes every stated case.

## Verification

The independently formulated `verify_meeting.py` enumerates all unordered pairs of distinct vertices of each \(K_{a,b}\) for \(1\le a,b\le4\), except \(K_{1,1}\), constructs the full two-particle transition matrix \(P\otimes P\) with diagonal meeting states absorbing, and solves the rational linear system directly by standard-library Gaussian elimination. It compares every resulting pair mean against the three-class formulas, then tests the difference identities and root-sign inequalities for part sizes through \(100\). The final standalone script was replayed from the included file path and returned `VERIFY_OK 31129 exact assertions`. This is a finite exact check; the arbitrary-size statements are established by the algebraic proof above, not by enumeration.

To reproduce, run `python3 verify_meeting.py` using a Python interpreter with the standard library. No external numerical packages or datasets are needed.

## Relationship to prior work

Alpern and Zeng (2021, arXiv:2111.05958) explicitly study independent synchronous lazy random walkers with shared holding probability and absorbing gathering configurations, but their analyzed graph families are paths, cycles, and small grids. Their exact three-agent cycle calculation identifies a laziness value \(1/3\) for a *different optimization objective*. No complete-bipartite starting-class crossing or universal two-threshold ordering is stated in the inspected methods, example sections, and full-text topic search.

Oliveira and Peres (2018, arXiv:1807.06858) establish general estimates for lazy-walk hitting, meeting, and coalescence times; these do not imply the exact three-class ordering by any displayed inequality. Sakumoto and Ohsaki (2020, arXiv:2005.11161) give spectral expressions and approximations for first meeting times in arbitrary-graph settings; their displayed spectral assumptions exclude bipartite graphs, and their approximate start-independent principal component is not an exact bipartite phase diagram. Eguchi et al. (2023, arXiv:2305.11590) consider a non-atomic one-moving-agent scheduling model, not two independently synchronous walkers. Avena et al. (2023, arXiv:2308.01832) concern asymptotic meeting/coalescence on random directed configuration graphs rather than this finite exact classification. The novelty claim is **only** the complete all-size initial-geometry phase diagram and its sharp thresholds, not the basic absorbing-chain method.

## Limitations

The phase diagram depends on synchronous independent movement and a common homogeneous holding probability. It is not asserted for asynchronous clocks, edge-crossing encounters, different holding probabilities, weighted bicliques, arbitrary graphs, or initial vertices allowed to coincide. Only expected first meeting times are ordered. A related 2023 University of Warwick thesis on laziness and gathering was found in search-indexed excerpts but its complete approximately 20 MB PDF could not be inspected; the accessible excerpts focused on path and cycle examples. This creates a residual historical-priority risk even though no covering biclique statement was established. No independent external mathematical audit has been performed.

## References

- S. Alpern and L. Zeng, *Social Distancing, Gathering, Search Games: Mobile Agents on Simple Networks*, arXiv:2111.05958, first posted 2021-11-10. https://arxiv.org/abs/2111.05958
- R. I. Oliveira and Y. Peres, *Random walks on graphs: new bounds on hitting, meeting, coalescing and returning*, arXiv:1807.06858, first posted 2018-07-18. https://arxiv.org/abs/1807.06858
- Y. Sakumoto and H. Ohsaki, *Graph Degree Heterogeneity Facilitates Random Walker Meetings*, arXiv:2005.11161, first posted 2020-05-22. https://arxiv.org/abs/2005.11161
- R. Eguchi, F. Ooshita, M. Inoue, and S. Tixeuil, *Meeting Times of Non-atomic Random Walks*, arXiv:2305.11590, first posted 2023-05-19. https://arxiv.org/abs/2305.11590
- L. Avena, F. Capannoli, R. S. Hazra, and M. Quattropani, *Meeting, coalescence and consensus time on random directed graphs*, arXiv:2308.01832, first posted 2023-08-03. https://arxiv.org/abs/2308.01832
- L. Zeng, *Mobile agents on simple networks: social distancing, gathering, dispersion and search games*, University of Warwick doctoral thesis (2023), bibliographic record and excerpts. https://wrap.warwick.ac.uk/id/eprint/184058/
