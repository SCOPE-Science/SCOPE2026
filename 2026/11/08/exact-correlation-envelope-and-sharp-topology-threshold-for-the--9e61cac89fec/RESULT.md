# Exact correlation envelope and sharp topology threshold for the node-based generalized friendship paradox

## Finding

For every finite connected simple nonregular undirected graph \(G=(V,E)\) with \(n=|V|\ge 3\), let \(d_i\) denote the degrees and put
\[
\delta_i=\sum_{j\sim i}\frac{1}{d_j},\qquad
s=\operatorname{Corr}(d,\delta).
\]
One has \(0<s\le1\). Fix any nonconstant real-valued vertex attribute \(a\), its population standard deviation \(\sigma_a>0\), its degree correlation \(x=\operatorname{Corr}(d,a)\), and its node-averaged singular generalized friendship-paradox (SGFP) gap
\[
g_G(a)=\frac1n\sum_{i\in V}\left(\frac1{d_i}\sum_{j\sim i}a_j-a_i\right).
\]
Then, with \(\sigma_\delta=\sqrt{n^{-1}\sum_i(\delta_i-1)^2}\), the normalized gap \(h=g_G(a)/(\sigma_\delta\sigma_a)=\operatorname{Corr}(\delta,a)\) obeys the exact sharp bounds
\[
\boxed{
 sx-\sqrt{(1-s^2)(1-x^2)}\ \le\ h\ \le\ sx+\sqrt{(1-s^2)(1-x^2)}.}
\]
For **every** \(x\in[-1,1]\), each endpoint is achieved by some nonconstant assignment \(a:V\to[0,1]\). When \(n\ge4\) every intervening normalized gap is also achievable; for \(s=1\) both endpoints coincide. Consequently, for each prescribed degree–attribute correlation \(x\), **some** attribute assignment with correlation \(x\) fails SGFP (strict negative gap) **if and only if**
\[
\boxed{x<\rho_G,\qquad \rho_G=\sqrt{1-\operatorname{Corr}(d,\delta)^2}.}
\]
Thus \(\rho_G\) is the sharp supremum of degree–attribute correlations compatible with a negative singular gap on the fixed graph; at the threshold, failure is impossible. In particular, \(\rho_G=0\) exactly for the pro-SGFP topologies characterized by \(s=1\), and \(\rho_G>0\) otherwise.

The four-vertex *paw* graph with edges \(\{0,1\},\{0,2\},\{1,2\},\{0,3\}\) has
\[
(d_i)=(3,2,2,1),\qquad (\delta_i)=(2,5/6,5/6,1/3),
\]
\[
\operatorname{Corr}(d,\delta)^2=25/27,
\qquad \boxed{\rho_G=\sqrt{2/27}\approx0.27216552698}.
\]
This illustrates the exact distinction between a strict failure supremum and a finite-margin numerical lower bound.

## Assumptions and scope

The graph is finite, undirected, simple, connected, nonregular and without isolates. Connectivity ensures all degrees are positive. Attributes are arbitrary nonconstant real-valued node numbers: the transformation \(a_i\mapsto\alpha a_i+\beta\) with \(\alpha>0\) preserves both Pearson correlations and the sign of the gap, so the same sharp bounds hold when requiring \(a_i\in[0,1]\). Uniform population (rather than edge) averaging defines the singular gap. The graph is fixed as the attribute assignment varies; no random graph, empirical sampling, or distributional assumption is made. Pearson correlations use population centering, and are defined because the vectors used below are nonconstant.

## Proof

**Step 1 (transpose identity and positivity).** Summing over neighbor pairs and reversing the sums yields
\[
\sum_i\delta_i=\sum_j\frac{d_j}{d_j}=n,\qquad
ng_G(a)=\sum_i(\delta_i-1)a_i.
\]
Let \(\bar d=n^{-1}\sum_i d_i\), \(u_i=d_i-\bar d\), and \(w_i=\delta_i-1\). Then \(\sum_i u_i=\sum_i w_i=0\), \(ng_G(a)=w\cdot a\), and
\[
D:=u\cdot w=\sum_i d_i\delta_i-\sum_i d_i
=\sum_{\{i,j\}\in E}\frac{(d_i-d_j)^2}{d_i d_j}>0.
\]
The equality follows because an undirected edge contributes \(d_i/d_j+d_j/d_i-2\) to the preceding difference. Connected nonregularity implies at least one unequal-degree edge and hence strict positivity. Thus \(U=u\cdot u>0\), \(W=w\cdot w>0\), and by Cauchy–Schwarz \(s=D/\sqrt{UW}\in(0,1]\).

**Step 2 (sharp fixed-correlation bounds).** Put \(\hat u=u/\sqrt U\), \(\hat w=w/\sqrt W\) and \(y=(a-\bar a\mathbf1)/\sqrt{\sum_i(a_i-\bar a)^2}\). These are centered unit vectors and
\[
x=\hat u\cdot y,\qquad h=\hat w\cdot y.
\]
If \(s<1\), form the centered unit vector \(v=(\hat w-s\hat u)/\sqrt{1-s^2}\), orthogonal to \(\hat u\). Then
\[
h=sx+\sqrt{1-s^2}\,(v\cdot y),\qquad
|v\cdot y|\le\sqrt{1-x^2}.
\]
The inequality follows from orthogonality and \(\|y-x\hat u\|^2=1-x^2\). Equality at either sign is realized by
\[
y_\pm=x\hat u\pm\sqrt{1-x^2}\,v.
\]
These vectors are centered unit vectors for every \(x\in[-1,1]\), hence are valid attribute vectors after shifting and positive scaling. If \(n\ge4\), the centered space has dimension at least three. Choose another centered unit vector orthogonal to both \(\hat u\) and \(v\), allowing \(v\cdot y\) to take every value in \([-\sqrt{1-x^2},\sqrt{1-x^2}]\) by mixing its orthogonal components at fixed norm. When \(s=1\), one has \(\hat w=\hat u\), so \(h=x\) and both bounds collapse, completing the exact envelope statement for all cases.

**Step 3 (threshold, strictness and sharpness).** For fixed \(x\), the minimum possible normalized gap is
\[
L(x)=sx-\sqrt{(1-s^2)(1-x^2)}.
\]
Because \(s>0\), this is strictly negative for every \(x<0\). For \(0\le x\le1\), the inequality \(L(x)<0\) is equivalent, after squaring two nonnegative sides, to \(x^2<1-s^2\). Thus across \([-1,1]\), \(L(x)<0\) holds exactly when \(x<\sqrt{1-s^2}\). The endpoint construction in Step 2 realizes a strictly negative gap whenever this inequality holds. Conversely all attributes have \(h\ge L(x)\), so at or above the threshold no negative gap is possible. The threshold itself is attained with \(g_G(a)=0\) when \(s<1\), not with a negative gap. For \(s=1\), one has \(h=x\), and the corresponding threshold is zero. This proves both iff and supremum assertions.

**Step 4 (explicit four-vertex calculation).** In the indicated paw graph, \(u=(1,0,0,-1)\), \(w=(1,-1/6,-1/6,-2/3)\), hence \(U=2\), \(W=3/2\), and \(D=5/3\). Thus \(s^2=D^2/(UW)=25/27\), which gives \(\rho_G^2=2/27\). All calculations are exact rational identities.

## Verification

The standalone `verify.py` uses only Python's standard-library rational arithmetic. It enumerates every labeled simple graph on three, four, or five vertices, filters connected nonregular cases, and checks the transposed gap formula, positivity, the Gram-matrix envelope inequality, equality on the extremal two-dimensional span, and zero-gap boundary witnesses. It also checks the paw graph's degrees, reciprocal-degree neighborhood totals, Gram data and threshold using exact fractions. The successful run examined **752 connected nonregular labeled graphs**, of which **90** have \(s=1\). These are finite checks only: the proof of the statements for arbitrary finite orders is the algebraic argument above.

To reproduce, run `python3 verify.py` with Python 3.9 or newer; there are no third-party dependencies. For any additional graph, the threshold needs only its degree sequence and the reciprocal-degree neighbor sum \(\delta\), not a numerical optimization over attributes.

## Relationship to prior work

Evtushenko and Kleinberg [1] introduce the singular node-averaged generalized friendship-paradox setting, its gap expression and the degree–\(\delta\) characterization of pro-/anti-SGFP graphs. They also define the topology-dependent boundary \(\varrho_G\) as an infimum, prove it is less than one, and compute numerical **lower bounds** on large SGFP-failing correlations using constrained linear optimization with a finite negative-gap margin. The theorem here evaluates that particular sharp boundary exactly for every connected nonregular graph, including the strict endpoint, and solves the stronger *fixed-correlation gap-envelope problem*.

Evtushenko and Kleinberg [2] develop a broader unweighted/weighted attribute framework and the sign rule governed by correlations with reciprocal-neighbor degree. That sign rule evaluates a **given** attribute assignment; it does not in the inspected main text solve optimization over *all* attributes of a specified degree correlation or provide the exact topology threshold. The envelope follows by orthogonal projection of the two fixed centered graph vectors, supplying this previously unquantified relationship. Jo, Lee and Eom [3] study correlated attributes with ensemble/coupling approximations; the same deterministic fixed-graph boundary is not asserted in their abstract and searched descriptions.

## Limitations

The result is not a new graph-by-graph classification of pro-/anti-SGFP structures; that classification is contained in [1]. It quantifies the sharp permitted correlations and gap range on each fixed topology. The extremal assignments are mathematically constructed and need not model naturally occurring correlated social attributes. Normalization divides by \(\sigma_a\), so no quantitative absolute-gap lower bound can be claimed without constraining attribute variance. The formula does not extend as written to directed graphs, isolates, or non-Pearson correlations. A relevant supplementary PDF to [1] was not fully inspected, and unindexed equivalent formulations remain a literature-priority risk; no independent validation has been performed.

## References

1. A. Evtushenko and J. Kleinberg, *Node-based Generalized Friendship Paradox fails*, arXiv:2110.11821 (first public 2021-10-22), https://arxiv.org/abs/2110.11821 ; open-access full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9902489/ .
2. A. Evtushenko and J. Kleinberg, *A comprehensive generalization of the Friendship Paradox to weights and attributes*, arXiv:2406.10423 (2024), https://arxiv.org/abs/2406.10423 ; open access https://pmc.ncbi.nlm.nih.gov/articles/PMC11178832/ .
3. H.-H. Jo, E. Lee and Y.-H. Eom, *Analytical approach to the generalized friendship paradox in networks with correlated attributes*, arXiv:2107.05838 (2021), https://arxiv.org/abs/2107.05838 .
