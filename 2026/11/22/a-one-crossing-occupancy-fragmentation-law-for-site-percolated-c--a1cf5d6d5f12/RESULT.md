# A one-crossing occupancy–fragmentation law for site-percolated complete bipartite graphs

## Finding

Let \(1\leq a\leq b\) be integers. Retain every vertex of \(K_{a,b}\) independently with probability \(p\in[0,1]\), retaining all edges whose endpoints survive. Let \(N\) be the number of retained vertices and \(C\) the number of nonempty connected components of the induced graph, with \(C=0\) if no vertices survive. Put \(q=1-p\), \(n=a+b\),
\[
 u=\frac{b(a+1)}n,\qquad v=\frac{a(b+1)}n,\qquad
 H_{a,b}(p)=1-up+q^{b-a}(1-vp)-q^b.
\]
Then, **exactly for every** \(p\in[0,1]\),
\[
 \operatorname{Cov}(N,C)=npq^aH_{a,b}(p).
\]
For \((a,b)=(1,1)\), this covariance is positive for every \(0<p<1\). For every other pair \(1\le a\le b\), there is a **unique** \(p_{a,b}\in(0,1)\) for which the covariance is zero. It is positive for \(0<p<p_{a,b}\) and negative for \(p_{a,b}<p<1\). Equivalently, \(p_{a,b}\) is the unique maximizer of the expected number of connected components, whose maximum exceeds one.

The location of the transition has two distinct regimes. If \(n=a+b\to\infty\) and \(a/n\to\alpha\in(0,1/2]\), set \(\beta=1-\alpha\). Then
\[
 np_{a,b}\longrightarrow\tau_\alpha,
\quad (1-\alpha\beta\tau_\alpha)
 [1+e^{-(\beta-\alpha)\tau_\alpha}]-e^{-\beta\tau_\alpha}=0,
\]
where the displayed equation has exactly one positive solution. In the balanced case \(a=b=m\to\infty\),
\[
 mp_{m,m}\longrightarrow c_*=1.8414056604\ldots,
 \qquad c_*+e^{-c_*}=2.
\]
Conversely, if \(a\ge1\) is held fixed while \(b\to\infty\), then \(p_{a,b}\to1/(a+1)\). Thus proportional and strongly unbalanced bicliques have distinct critical retention scales.

## Assumptions and scope

Vertices are independently retained with a common Bernoulli probability. All surviving edges are deterministic; this is **site**, not bond, percolation. The host is the finite complete bipartite graph with two nonempty parts. Isolated retained vertices each count as a component, and the empty configuration contributes zero. The covariance theorem and uniqueness hold at every finite integer size (with the single-edge exception stated above); the limit statements apply only under their stated sequences.

## Proof

**1. Exact mean and score covariance.** Let \(A\sim\operatorname{Bin}(a,p)\) and \(B\sim\operatorname{Bin}(b,p)\) independently. The occupied induced graph is connected when both classes are nonempty, and otherwise consists solely of the occupied vertices in one class. Consequently
\[
 C={\bf1}_{\{A>0,B>0\}}+A{\bf1}_{\{B=0\}}+B{\bf1}_{\{A=0\}},
\]
so its mean is
\[
 F(p)=(1-q^a)(1-q^b)+apq^b+bpq^a.
\]
The product Bernoulli likelihood differentiated in \(p\) gives, for \(0<p<1\),
\[
 F'(p)=\frac{\operatorname{Cov}(N,C)}{pq}.
\]
Differentiate the explicit \(F\) and collect powers of \(q\):
\[
 F'(p)=nq^{a-1}\left[1-\frac{b(a+1)}n p
 +q^{b-a}\left(1-\frac{a(b+1)}n p\right)-q^b\right].
\]
This yields the asserted covariance; the identity extends to the endpoints by continuity.

**2. Strict one-crossing property.** Rewrite \(H\) as a polynomial in \(q\):
\[
 H(q)=1-u+uq+(1-v)q^r+vq^{r+1}-q^b,
 \qquad r=b-a.
\]
If \(r=0\), then \(a=b=m\), \(H=2-(m+1)p-q^m\), and \(dH/dq=m+1-mq^{m-1}>0\) on \([0,1]\). If \(r\ge1\),
\[
 \frac{dH}{dq}=u+r(1-v)q^{r-1}+(r+1)vq^r-bq^{b-1}.
\]
Since \(b-1\ge r\), \(q^{b-1}\le q^r\) for \(q\in[0,1]\). An exact simplification then gives
\[
 \frac{dH}{dq}\ge
 u-\frac{a-1}{n}q^{r-1}[br(1-q)+aq].
\]
Because \(a\le b\), the bracketed product is at most \(bq^{r-1}[r(1-q)+q]\le b\). The last inequality follows since \(q^{r-1}[r(1-q)+q]\) increases to one on \([0,1]\) (differentiate, obtaining \(r(r-1)q^{r-2}(1-q)\ge0\) for \(r>1\); for \(r=1\) it is identically one). Therefore
\[
 \frac{dH}{dq}\ge u-\frac{b(a-1)}n=\frac{2b}{n}>0.
\]
Thus \(H\) strictly decreases with \(p\). Moreover \(H(0)=1\). At \(p=1\), if \(a<b\), \(H(1)=-a(b-1)/n<0\); if \(a=b=m\), \(H(1)=1-m\), negative for \(m\ge2\) and zero for \(m=1\). The intermediate value theorem proves exactly one interior sign change except on \(K_{1,1}\), for which \(H=q\) and no interior zero exists. The signs of \(F'\) and the strict maximum follow.

**3. Scaling laws.** If \(a/n\to\alpha>0\), \(b/n\to\beta\), and \(p=t/n\) at fixed \(t\ge0\), then \(q^{b-a}\to e^{-(\beta-\alpha)t}\), \(q^b\to e^{-\beta t}\), and \(up,vp\to\alpha\beta t\). Therefore \(H(t/n)\to J_\alpha(t)\), the continuous expression displayed in the finding. Each \(H\) is strictly decreasing, so \(J_\alpha\) is nonincreasing. It is real analytic, starts at \(J_\alpha(0)=1\), and tends to \(-\infty\): for \(\alpha<1/2\), the factor \(1-\alpha\beta t\) dominates, while for \(\alpha=1/2\) it is doubled. Hence it has precisely one positive zero (two zeros would force a plateau and thus an identically zero analytic function). Bracketing this root using pointwise convergence proves \(np_{a,b}\to\tau_\alpha\). Setting \(\alpha=1/2\), \(t=2c\) yields \(c+e^{-c}=2\). Finally, with fixed \(a\), \(b\to\infty\), for each fixed \(p\in(0,1)\), \(q^{b-a},q^b\to0\), and \(u\to a+1\). Therefore \(H_{a,b}(p)\to1-(a+1)p\); the same root-bracketing argument gives \(p_{a,b}\to1/(a+1)\).

## Verification

The standalone `verification/check.py` enumerates all Bernoulli occupancy configurations for each \(1\le a\le4\), \(a\le b\le5\) and probabilities \(1/5,1/2,4/5\); it independently calculates the mean and covariance as rational numbers and compares them to the derived formulas. It additionally checks exact endpoint signs and strict monotonicity on rational grids for \(1\le a\le15\), \(a\le b\le21\). A local replay completed **713 exact rational equalities/inequalities**. These finite checks do not establish the universal theorem or any limiting law: those follow from the proof above.

## Relationship to prior work

Allard, Hébert-Dufresne, Young and Dubé's general percolation formalism (initially posted 2015-09-03) provides exact component-distribution machinery for arbitrary finite random networks and discusses site versus bond percolation; its general formulas furnish contextual, broader computational coverage. The assessed result is the explicit **joint occupancy–component covariance**, its **global one-crossing sign theorem for every complete bipartite host**, and its two asymptotically distinct threshold regimes. These claims do not follow merely from the availability of a finite enumeration method without the monotonicity argument. Other random-graph results on bond percolation, fixed-edge isolation, and bipartite random walks address different probability spaces or statistics.

## Limitations

This theorem does not claim a comparable one-crossing property for arbitrary host graphs, unequal retention probabilities on the two vertex classes, or bond percolation. The only size-independent exception is the single-edge host \(K_{1,1}\). The results are analytically proved but have not undergone independent mathematical validation. A broader historical literature could contain an equivalent specialization; absence from targeted searches does not prove absolute priority.

## References

1. P. Allard, L. Hébert-Dufresne, J.-G. Young and L. J. Dubé, *General and exact approach to percolation on random graphs*, arXiv:1509.01207v1 (first public version, 2015-09-03), https://arxiv.org/abs/1509.01207.
2. P. Allard et al., *Exact solution of bond percolation on small arbitrary graphs*, arXiv:1201.4369 (2012), https://arxiv.org/abs/1201.4369. Cited for contrasting bond-percolation methodology, not as the primary source for this site-percolation question.
