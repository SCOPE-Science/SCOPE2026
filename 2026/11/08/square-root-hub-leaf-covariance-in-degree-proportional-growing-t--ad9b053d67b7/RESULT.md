# Square-root hub–leaf covariance in degree-proportional growing trees

## Finding
For a degree-proportional growing tree begun from one edge, the degree of the first vertex has a **positive** covariance with the total number of leaves for every size at least four. Despite this positive covariance growing at square-root scale, the associated correlation decays at inverse-square-root scale.

For integers \(n\ge2\), let
\[
q_n=\frac{1}{4^{n-2}}\binom{2n-4}{n-2}.
\]
The finite-size law is
\[
\boxed{\operatorname{Cov}(D_n,L_n)=\frac{2nq_n-4}{3}+\frac13\sum_{k=2}^{n-1}\frac{(2k-3)q_k^2}{(k-1)^2}.}
\]
The sum is empty if \(n=2\). The covariance is zero at \(n=2,3\), positive for every \(n\ge4\), and satisfies
\[
\operatorname{Cov}(D_n,L_n)=\frac{2}{3\sqrt\pi}\sqrt n+O(1),\qquad
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(D_n,L_n)=\sqrt{\frac{2}{\pi-2}}.
\]
The correlation assertion concerns \(n\ge4\), for which both variables are nondegenerate.

## Assumptions and scope
Start with a single edge between labeled vertices 1 and 2. Given a tree on vertices \(1,\dots,m\), \(m\ge2\), add vertex \(m+1\) and connect it by one edge to an existing vertex \(v\), selected with probability \(\deg(v)/[2(m-1)]\), conditional on the existing tree. Each successive choice uses the specified conditional law. The tree is finite, labeled by arrival order, and has no loops or multiple edges. Let \(D_m\) be the ordinary *undirected* degree of vertex 1; let \(L_m\) be the total number of vertices of undirected degree exactly one, including vertex 1 if appropriate; let \(Q_m\) indicate that vertex 1 is a leaf.

The proof applies to every integer \(m\ge2\); no stationarity or independence between \(D_m\) and \(L_m\) is assumed.

## Proof
Put \(h_m=[2(m-1)]^{-1}\), \(a_m=\mathbb E D_m\), \(b_m=\mathbb E L_m\), and \(q_m=\mathbb E Q_m\). Write \(I_m\) for the event that the new vertex attaches to vertex 1 and \(J_m\) for attachment to a leaf. For a given current tree \(\mathcal T_m\),
\[
D_{m+1}=D_m+I_m,\quad L_{m+1}=L_m+1-J_m,
\quad\mathbb E[I_m\mid\mathcal T_m]=h_mD_m,\quad\mathbb E[J_m\mid\mathcal T_m]=h_mL_m.
\]
The events \(I_m\) and \(J_m\) intersect exactly when vertex 1 is a leaf and receives the new edge. Hence \(\mathbb E[I_mJ_m\mid\mathcal T_m]=h_mQ_m\), not \(h_m^2D_mL_m\). Taking first moments gives
\[
a_{m+1}=(1+h_m)a_m,\quad b_{m+1}=(1-h_m)b_m+1,\quad q_{m+1}=(1-h_m)q_m,
\]
with initial values \((a_2,b_2,q_2)=(1,2,1)\). In the third equation the root, once it has ceased to be a leaf, cannot become a leaf again. Solving gives
\[
q_m=4^{-(m-2)}\binom{2m-4}{m-2},\quad
a_m=(2m-3)q_m,\quad b_m=\frac{2(m-1)}3+\frac43q_m.
\]

Multiplying the two increment equations, and retaining the intersection term, yields
\[
\mathbb E[D_{m+1}L_{m+1}]=\mathbb E[D_mL_m]+(1+h_m)a_m-h_mq_m.
\]
Subtracting the product of the displayed first-moment recurrences proves the exact covariance increment identity
\[
c_{m+1}-c_m=h_m^2a_mb_m-h_mq_m
=\frac{q_m}{3}\left(\frac{m-3}{m-1}+\frac{(2m-3)q_m}{(m-1)^2}\right),
\qquad c_m=\operatorname{Cov}(D_m,L_m).
\]
For \(m=2\) this increment is zero; for every \(m\ge3\) it is strictly positive. Since \(c_2=0\), the finite-size sign assertions follow.

To sum explicitly, note that \(q_{m+1}=q_m[1-1/(2(m-1))]\) and therefore
\[
\sum_{m=2}^{n-1}q_m=(2n-4)q_n,
\qquad \sum_{m=2}^{n-1}\frac{q_m}{m-1}=2(1-q_n).
\]
The first identity follows by induction, and the second telescopes from \(q_m-q_{m+1}=q_m/[2(m-1)]\). Summing the increment identity proves the boxed covariance formula.

By the central-binomial asymptotic \(q_m=(\pi m)^{-1/2}(1+O(m^{-1}))\), the non-sum term equals \(\frac{2}{3\sqrt\pi}\sqrt n+O(1)\). The remaining sum is bounded uniformly in \(n\), because its summand is \(O(m^{-2})\). This proves the covariance asymptotic.

For the correlation, conditional increments also imply
\[
\mathbb E[D_{m+1}(D_{m+1}+1)\mid\mathcal T_m]
=\left(1+\frac1{m-1}\right)D_m(D_m+1).
\]
Thus \(\mathbb E[D_n(D_n+1)]=2(n-1)\) and
\[
\operatorname{Var}(D_n)=2(n-1)-a_n-a_n^2
=\left(2-\frac4\pi\right)n+O(\sqrt n).
\]
Writing \(v_m=\operatorname{Var}(L_m)\), conditional Bernoulli increments and total variance give
\[
v_{m+1}=\left(1-\frac1{m-1}\right)v_m+p_m(1-p_m),
\qquad p_m=\frac{b_m}{2(m-1)}\longrightarrow\frac13.
\]
With \(v_3=0\), summing this linear recurrence, or applying weighted Cesàro averaging, shows \(v_n/n\to1/9\). Inserting these two variance limits and the covariance asymptotic yields
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(D_n,L_n)
=\frac{2/\sqrt\pi}{\sqrt{2-4/\pi}}=\sqrt{\frac2{\pi-2}}.
\]

## Verification
A standalone Python 3 checker, `verify.py`, accompanies this statement. It independently enumerates **every** arrival-parent history through nine vertices and computes its exact probability as a rational product of attachment probabilities, then compares the four claimed moments (root-degree mean, leaf-count mean, root-leaf probability and covariance) against the closed formulas. It separately replays exact moment recurrences to size 90 and evaluates large-size asymptotic diagnostics through 100,001 vertices. The checker executed successfully with 132 assertions. Enumeration is finite corroboration only; the proof of the all-size theorem is the analytic recurrence argument above.

Run from the extracted artifact directory:

```sh
python3 verify.py
```

## Relationship to prior work
Degree-proportional attachment and depth stratification are studied by Ben-Naim and Krapivsky (arXiv:0905.1920, first public May 12, 2009). Berger, Borgs, Chayes and Saberi (arXiv:1401.2792, 2014) derive local limits and typical-neighbor joint degree statistics; their uniformly selected root is not the distinguished *oldest* vertex considered here. Holmgren, Janson and Šileikis (arXiv:1603.08125, 2016) analyze joint fringe-subtree counts rather than the distinguished-hub/total-leaf covariance.

Hartle and Krapivsky (arXiv:2602.01021, 2026) derive detailed global leaf-count moments and joint degree–leafdegree statistics for typical vertices. Their exact leaf-count mean and asymptotic variance are consistent with those used above; neither their local joint degree–leafdegree law nor their joint counts of bounded-degree classes directly imply the oldest-vertex mixed covariance and its square-root asymptotic. The novel claim is this *mixed distinguished-hub/global leaf* dependence, not the previously known marginal statistics. A related published result for a **different**, uniformly attaching recursive-tree model has a bounded rather than square-root-order root-degree/leaf covariance.

## Limitations
This is not a result for uniform attachment, shifted-linear preferential attachment, multiple edges per new vertex, or all root labels. The initial edge and ordinary degree-proportional rule are essential to the stated constants. The limiting correlation does not imply asymptotic independence without further analysis. The exact joint law of these variables is not classified here. The 2009 source was examined in its full six-page primary text, while the 2016 fringe-tree preprint was examined only through its public abstract and index. Implicit coverage in broader historical generating-function or urn treatments remains an originality risk. Independent audit has not been performed.

## References
1. E. Ben-Naim and P. L. Krapivsky, *Stratification in the Preferential Attachment Network*, arXiv:0905.1920v1, first public 2009-05-12. https://arxiv.org/abs/0905.1920
2. N. Berger, C. Borgs, J. T. Chayes and A. Saberi, *Asymptotic behavior and distributional limits of preferential attachment graphs*, arXiv:1401.2792v1, 2014. https://arxiv.org/abs/1401.2792
3. C. Holmgren, S. Janson and M. Šileikis, *Multivariate normal limit laws for the numbers of fringe subtrees in m-ary search trees and preferential attachment trees*, arXiv:1603.08125v1, first public 2016-03-26. https://arxiv.org/abs/1603.08125
4. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1, 2026. https://arxiv.org/abs/2602.01021
