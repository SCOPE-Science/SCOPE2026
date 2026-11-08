# Rank-one checkerboard leaf correlations under a single bipartite edge tilt

## Finding

Let \(a,b\ge2\) be integers, \(A,B\) disjoint labeled vertex sets with sizes \(a,b\), and \(x\in A,y\in B\). Assign conductance \(w\ge0\) to the distinguished edge \(xy\) of the complete bipartite graph \(K_{a,b}\), and conductance one to every other edge. Sample a spanning tree with probability proportional to the product of its edge conductances. At \(w=0\), the edge is simply deleted; the remaining graph is connected.

Let \(I_u=\mathbf 1\{\deg_T(u)=1\}\), and define
\[
\ell_A=(1-1/a)^{b-1},\qquad \ell_B=(1-1/b)^{a-1},\qquad
p=\frac{a+b-1}{ab},\qquad Z_w=1+(w-1)p.
\]
For \(u\in A\) and \(v\in B\), put
\[
\alpha_u=\begin{cases}1&u=x,\\-1/(a-1)&u\ne x,\end{cases}\qquad
\beta_v=\begin{cases}1&v=y,\\-1/(b-1)&v\ne y.\end{cases}
\]
**Theorem.** For all the stated integer parameters and every real \(w\ge0\),
\[
\boxed{\operatorname{Cov}_w(I_u,I_v)
=-\frac{w(w-1)\ell_A\ell_B}{abZ_w^2}\alpha_u\beta_v.}
\]
Thus the entire \(a\)-by-\(b\) cross-part leaf-covariance matrix has rank one for \(0<w\ne1\) and rank zero at \(w=0,1\). For \(w>1\), the pairs with both vertices distinguished or both undistinguished have negative covariance, whereas pairs with exactly one distinguished vertex have positive covariance; for \(0<w<1\), all four signs reverse. Every row sum and column sum of this matrix vanishes.

Let \(L_A=\sum_{u\in A}I_u\) and \(L_B=\sum_{v\in B}I_v\). Despite the local dependence, **the full joint distribution** of \((L_A,L_B)\) is independent of \(w\). Furthermore \(L_A,L_B\) are independent for every \(w\ge0\), with
\[
\Pr(L_A=r)=\binom ar\frac{(a-r)!\,S(b-1,a-r)}{a^{b-1}},\qquad
\Pr(L_B=s)=\binom bs\frac{(b-s)!\,S(a-1,b-s)}{b^{a-1}},
\]
where \(S(n,k)\) is a Stirling number of the second kind, \(S(n,0)=0\) for \(n\ge1\), and out-of-range values are zero.

## Assumptions and scope

All vertices are labeled; \(K_{a,b}\) is the undirected simple complete bipartite graph, and the law is the conductance-product spanning-tree Gibbs measure. The result concerns ordinary unweighted vertex degree within the random tree, not conductance-weighted degree or edge-indicator covariances. The covariance is cross-part only: one leaf indicator is indexed by \(A\), the other by \(B\). No assertion about same-part covariance is made. The condition \(a,b\ge2\) ensures \(0<p<1\) and \(Z_w>0\) even at \(w=0\).

## Proof

**1. Baseline leaf laws.** Let \(\mathbb P_1\) denote the uniform spanning-tree law. The number of spanning trees of \(K_{a,b}\) is \(a^{b-1}b^{a-1}\). Fix subsets \(U\subseteq A\), \(V\subseteq B\) of sizes \(r,s\). For \(r<a\), \(s<b\), forcing every vertex in \(U\cup V\) to be a leaf is equivalent to taking an arbitrary spanning tree of \(K_{a-r,b-s}\), then attaching each marked vertex to exactly one opposite-part unmarked vertex. The count is
\[
(a-r)^{b-s-1}(b-s)^{a-r-1}(b-s)^r(a-r)^s
=(a-r)^{b-1}(b-s)^{a-1}.
\]
If \(r=a\) or \(s=b\), the event is impossible for \(a,b\ge2\), and the same final ratio vanishes. Therefore
\[
\mathbb P_1(I_u=1\ (u\in U),\ I_v=1\ (v\in V))
=\left(1-\frac ra\right)^{b-1}
 \left(1-\frac sb\right)^{a-1}.
\tag{1}
\]
By finite inclusion-exclusion, the full leaf-indicator vectors on the two parts are independent under \(\mathbb P_1\), and the marginal vectors are the empty-box indicators from \(b-1\) iid uniform draws into \(a\) boxes and, respectively, \(a-1\) draws into \(b\) boxes. This proves the displayed Stirling-number marginals and their independence at \(w=1\), and also gives \(\mathbb P_1(I_u=1)=\ell_A\), \(\mathbb P_1(I_v=1)=\ell_B\), and \(\mathbb P_1(I_u=I_v=1)=\ell_A\ell_B\) for all cross-part pairs.

**2. Edge tilt and conditional edge incidences.** Write \(H=\mathbf1\{xy\in T\}\), \(q=w-1\). Under \(\mathbb P_1\), all \(ab\) edges are exchangeable, and a spanning tree has exactly \(a+b-1\) edges, so \(\mathbb P_1(H=1)=p\). Hence
\[
\mathbb P_w(E)=\frac{\mathbb E_1[\mathbf1_E(1+qH)]}{1+qp}
=\mathbb P_1(E)\frac{1+q\,\mathbb P_1(H=1\mid E)}{Z_w}.
\tag{2}
\]
For the leaf event of \(u\in A\), denote the conditional probability of \(H=1\) by \(r_u\), and analogously \(s_v\) for \(v\in B\). Leaf deletion and uniform attachment give
\[
r_u=\begin{cases}1/b&u=x,\\\frac{a+b-2}{(a-1)b}&u\ne x,\end{cases}
\qquad
s_v=\begin{cases}1/a&v=y,\\\frac{a+b-2}{a(b-1)}&v\ne y.\end{cases}
\tag{3}
\]
For the joint event that \(u\) and \(v\) are leaves, the conditional probability \(h_{uv}=\mathbb P_1(H=1\mid I_u=I_v=1)\) is
\[
\begin{array}{c|cc}
&v=y&v\ne y\\\hline
u=x&0&1/(b-1)\\
u\ne x&1/(a-1)&(a+b-3)/((a-1)(b-1))
\end{array}.
\tag{4}
\]
When neither marked leaf is an endpoint of \(xy\), the last entry follows because the remaining core is a uniform spanning tree of \(K_{a-1,b-1}\); its edge incidence probability is its \(a+b-3\) tree edges divided by its \((a-1)(b-1)\) possible edges. The other entries follow by choosing the attachment vertex uniformly, or observing that a tree with at least four vertices cannot contain an edge joining two leaves.

**3. Exact covariance and sign.** Equations (1)--(4) imply
\[
\operatorname{Cov}_w(I_u,I_v)=\frac{\ell_A\ell_B}{Z_w^2}
\bigl[(1+q h_{uv})Z_w-(1+q r_u)(1+q s_v)\bigr].
\]
Direct substitution of the four cases (3)--(4) gives the elementary exact identity
\[
(1+q h_{uv})Z_w-(1+q r_u)(1+q s_v)
=-\frac{q(q+1)}{ab}\alpha_u\beta_v.
\tag{5}
\]
Since \(q(q+1)=w(w-1)\), the boxed formula follows. All remaining factors apart from \(-w(w-1)\alpha_u\beta_v\) are positive. Because \(\sum_{u\in A}\alpha_u=0\) and \(\sum_{v\in B}\beta_v=0\), the cross-covariance matrix is rank one when its scalar is nonzero, has zero row and column sums, and has exactly the claimed four sign classes.

**4. Full aggregate invariance.** The joint event \(\{L_A=r,L_B=s\}\) is invariant under the automorphism group \(S_a\times S_b\), which acts transitively on the edges of \(K_{a,b}\). Hence, conditional on any such event of positive baseline probability, every edge has the same inclusion probability, necessarily \(p=(a+b-1)/(ab)\). Equation (2) then shows
\[
\mathbb P_w(L_A=r,L_B=s)=\mathbb P_1(L_A=r,L_B=s).
\]
Zero-probability events remain impossible. The independence and Stirling-number distributions from step 1 therefore hold for every \(w\ge0\). This completes the proof.

## Verification

The exact standalone checker `verify_edge_tilt.py` independently enumerates spanning trees for nine ordered pairs of part sizes, including the boundary \(a=b=2\), at conductances \(0,1/3,1,2,7\). For each test it checks the weighted partition function, every cross-part leaf covariance and the invariance and independence of the aggregate leaf-count distribution. It reports 520 exact-rational assertions passed. A separate symbolic simplification of the four alternatives in equation (5) also returned exact zero for each residual. These are finite consistency tests; the all-size conclusion is established by the proof, not by enumeration.

Reproduction: run `python verify_edge_tilt.py` with standard Python 3; no other modules are required.

## Relationship to prior work

Ge and Dong (2019) provide exact spanning-tree counts and electrical quantities for complete bipartite graphs with a deleted matching, including single-edge deletion. Dong and Ge (2021) enumerate spanning trees of complete bipartite graphs containing prescribed forests. These results support the base counting perspective but do not state the cross-part leaf-covariance checkerboard under a continuous one-edge tilt or the invariant joint leaf-count law. Rapoport (2023) gives general finite-graph uniform-spanning-tree degree-field probability formulas; the present theorem is a specifically evaluated, parameter-uniform sign and rank classification for a conductance-tilted law. Fita Sanmartín, Schnörr and Hamprecht (2024) provide weighted spanning-tree degree moment and covariance machinery, whereas the events treated here are non-linear degree-one indicators. General formulas can in principle compute these probabilities; the sign classification, cancellation and aggregate invariance need the additional explicit analysis above.

## Limitations

The assertion is restricted to one distinguished edge in a complete bipartite graph, to cross-part leaf indicator pairs, and to nonnegative edge conductance \(w\). It does not treat simultaneously perturbed edges, within-part covariance or non-bipartite graphs. The rank-one covariance is not independence of the complete labeled degree vectors. Claims of historical novelty are subject to independent literature confirmation; the general degree-field formulas remain relevant background and may yield alternate derivations.

## References

- J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs* (first public version 16 April 2019), https://arxiv.org/abs/1904.07766.
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest* (first public version 9 March 2021), https://arxiv.org/abs/2103.05294.
- A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach* (first public version 22 December 2023), https://arxiv.org/abs/2312.14992.
- E. Fita Sanmartín, C. Schnörr and F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees* (first public version 20 September 2024), https://arxiv.org/abs/2409.13472.
