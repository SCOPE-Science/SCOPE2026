# Strict disjoint-pair connectivity covariance in homogeneous \(K_{2,n}\) random-cluster gases

## Finding
Let \(n\ge 6\), let \(G=K_{2,n}\) have two hub vertices and \(n\) labeled leaf vertices, and sample a bond set \(F\subseteq E(G)\) with probability proportional to \(q^{k(F)}v^{|F|}\), where \(q>0\), \(v>0\), and \(k(F)\) is the number of connected components of the spanning subgraph \((V(G),F)\), including isolated vertices. For four *distinct* leaves \(a,b,c,d\), set \(X=\mathbf1_{\{a\leftrightarrow b\}}\) and \(Y=\mathbf1_{\{c\leftrightarrow d\}}\). Define
\[
A=q+2v,\quad B=q+2v+v^2,\quad r=A/B,\quad u=qv/B,\quad y=(2+u)^2/2.
\]
Then the following exact formula holds:
\[
\operatorname{Cov}(X,Y)=\frac{4v^4 r^{n-4}}{B^4[1+(q-1)r^n]^2}
\big\{q(1-r^n)+(y-2)[2+(q-1)y]\big\}>0.
\]
This gives a strict connectivity-event covariance inequality for every member of an unbounded, noncactus two-hub graph family, including the range \(0<q<1\) in which the usual positive-association argument does not apply. For fixed \(q,v>0\), it also gives the sharp exponential asymptotic
\[
\operatorname{Cov}(X,Y)\sim\frac{4v^4}{B^4}
\{q+(y-2)[2+(q-1)y]\}\,r^{n-4}\qquad(n\to\infty).
\]

## Assumptions and scope
The graph is simple and complete bipartite, with exactly two hubs and at least six leaves. All \(2n\) edge activities are the same strictly positive real number \(v\). The cluster weight \(q\) is an arbitrary positive real number, not necessarily an integer. Events concern connectivity in the *occupied-edge subgraph*, not direct edge occupation. The four marked leaves must be distinct. No claim is made for heterogeneous activities, general series-parallel networks, or every possible pair of connectivity events on \(K_{2,n}\).

## Proof
For each leaf, record which of its two hub spokes are occupied. The possibilities \(00,10,01,11\) carry activities \(1,v,v,v^2\), respectively. If no leaf has state \(11\), the hubs are disconnected, so each isolated leaf contributes a cluster factor \(q\) and the two hub components contribute \(q^2\). Thus this sector has partition sum \(q^2 A^n\). If at least one leaf has state \(11\), the hubs are connected, giving partition sum \(q(B^n-A^n)\). Consequently
\[
Z=q[B^n+(q-1)A^n]>0.
\]

Let \(H_X\) denote the unnormalized weight of \(X=1\), and \(H_{XY}\) the unnormalized weight of \(X=Y=1\). With disconnected hubs, two marked leaves connect exactly when their spokes attach to the same hub; there are two choices. With connected hubs, they connect exactly when each has at least one occupied spoke; remove configurations without any state \(11\). Therefore, writing \(s=v^2(2+v)^2\),
\[
H_X=q\{sB^{n-2}+2(q-2)v^2A^{n-2}\}.
\]
For two disjoint pairs the disconnected-hub sector has four valid assignments, and the connected-hub sector requires all four marked leaves to have nonzero states. Hence
\[
H_{XY}=q\{s^2B^{n-4}+4(q-4)v^4A^{n-4}\}.
\]
These two expressions follow from exhaustive, disjoint sector partitions, so no independence assumption is used.

Now \(\operatorname{Cov}(X,Y)=(ZH_{XY}-H_X^2)/Z^2\). Substitution, division by positive factors, and \((2+v)A/B=2+qv/B\) yield
\[
ZH_{XY}-H_X^2=4q^2v^4B^{2n-4}r^{n-4}
\{q(1-r^n)+(y-2)[2+(q-1)y]\}.
\]
The displayed covariance formula follows.

It remains to prove strict positivity for all stated parameters. Since \(B>A>0\), we have \(0<r<1\), while \(u>0\) and \(y>2\). If \(q\ge1\), then \(2+(q-1)y>0\). If \(0<q<1\), the bound \(B>2v\) gives \(0<u<q/2\) and hence \(y<(2+q/2)^2/2\). But
\[
(1-q)(2+q/2)^2=4-2q-\tfrac74q^2-\tfrac14q^3<4,
\]
so again \(2+(q-1)y=2-(1-q)y>0\). Thus both terms inside braces are strictly positive. Finally \(r^n\to0\) gives the asymptotic with a strictly positive prefactor.

## Verification
The standalone `verify.py` independently enumerates all \(2^{2n}\) occupied-edge configurations for \(4\le n\le7\), at fifteen pairs of positive rational values of \(q,v\), and compares exact rational partition sums and connection-event moments with both closed formulas. It also checks the factored covariance expression and its positivity. The script makes 60 full finite-state comparisons; these are supplementary checks, not the all-size proof. Run using `python3 verify.py` with only the Python standard library.

## Relationship to prior work
The Fortuin–Kasteleyn random-cluster model and the special difficulty of dependence below cluster weight one are classical. Grimmett and Winkler (2003) studied edge-negative association and its random-cluster context, not the present joint connectivity-event observable. Çiçeksiz and Ravichandran (2026, Section 6, Conjecture 6.3) formulated positive covariance of disjoint pair-connectivity events for arbitrary graphs when the cluster weight is below one; their theorem establishes different edge-correlation or high-fugacity forest claims, not this finite-activity two-hub family. Previously published cactus-graph connection-covariance results do not cover \(K_{2,n}\) for \(n\ge3\), since its cycles share multiple edges. A separate finite-core random-cluster asymptotic reduction addresses vanishing edge activities and does not, from its accessible statement, imply the finite-size, all-activity sign established here. A finite small-bipartite-graph coefficient certificate covers some small \(K_{2,n}\) examples but not arbitrarily many leaves.

## Limitations
Only two disjoint leaf-pair events, homogeneous positive spoke activities and finite graphs are addressed. The positive-covariance theorem is not a proof of general connectivity-event association, nor a claim about edge-correlation signs. The expression is for fixed cluster weight and fugacity; the displayed large-graph asymptotic holds with those parameters fixed. Historical priority is not independently established. The available summaries of some closely related published results were not substitutes for full-text inspection, so stronger unnoticed prior implications remain possible.

## References
1. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185 (first submitted 17 February 2003), especially Sections 1 and 4. https://arxiv.org/abs/math/0302185
2. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the q<1 Random Cluster Model*, arXiv:2610.00549 (30 September 2026), especially Section 6 and Conjecture 6.3. https://arxiv.org/abs/2610.00549
3. Related published mathematical summaries examined for scope comparison: *Positive connectivity correlations on every weighted cactus random-cluster graph* (2026), and *Finite-core Fortuin–Kasteleyn reduction and mixed-Gaussian cluster fluctuations* (2026). Their accessible summaries, not independently obtained full manuscripts, were used only to assess possible overlap.
