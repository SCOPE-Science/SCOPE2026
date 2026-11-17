# Sharp Gini contraction of half-lazy random walks on balanced bicliques

## Finding
For every integer \(m\ge1\), on the complete bipartite graph \(K_{m,m}\) the half-lazy random-walk operator \(P_m=(I+D^{-1}A)/2\) satisfies the **exact attained** complete-pair Gini norm formula
\[
\|P_m\|_{G_m}=\frac{3(m-1)}{2(2m-1)},\qquad
G_m(f)=\sum_{u<v}|f(u)-f(v)|.
\]
The right side is zero at \(m=1\). For every \(m\ge3\), a nonconstant signal attains this coefficient if and only if it is a scalar multiple of the indicator of a single vertex, up to an additive constant. At \(m=2\), the coefficient is \(1/2\), with possible additional extremizers. The coefficients are strictly increasing in \(m\) and
\[
\sup_{m\ge1}\|P_m\|_{G_m}=\frac34,
\]
with no finite graph attaining the supremum.

## Assumptions and scope
The graph is finite, simple, unweighted and balanced, with two independent sets of exactly \(m\) vertices each. The averaging is on real vertex signals in one discrete step, with holding probability exactly \(1/2\). The seminorm is the unweighted sum over **all** unordered vertex pairs, not only graph edges. Constants are annihilated by the seminorm; the quotient operator norm is taken over nonconstant real signals. The formula holds for every integer \(m\ge1\) with no asymptotic assumption.

## Proof
Let the bipartition sets be \(A\) and \(B\), each of size \(m\). Every real signal admits a layer-cake decomposition into nested binary cuts plus a constant. By linearity and the triangle inequality for \(G_m\), the exact operator seminorm is the maximum of \(G_m(P_m1_S)/G_m(1_S)\) over all nontrivial subsets \(S\). Thus it suffices to study cuts.

Let \(r=|S\cap A|\), \(s=|S\cap B|\), \(k=r+s\), and \(d=|r-s|\). Each selected vertex in \(A\) is sent to \((1+s/m)/2\), and each unselected vertex in \(A\) to \(s/(2m)\); in \(B\), interchange \(r\) and \(s\). Direct pair counting, including within-class and cross-class pairs, gives
\[
G_m(P_m1_S)=mk-(r^2+s^2)+\frac{d}{2m}\big[rs+(m-r)(m-s)\big].
\]
Since \(G_m(1_S)=k(2m-k)\), the quotient simplifies exactly to
\[
R_{m,k,d}=\frac12+\frac{d\big[m^2+(m-k)^2-2md-d^2\big]}{4mk(2m-k)}.
\]
The complement cut has the same quotient, so assume \(1\le k\le m\), hence \(0\le d\le k\). When \(d=0\), the quotient is \(1/2\). When \(d>0\), the bracket in the numerator is nonpositive, the same upper bound applies. Otherwise use \(d/k\le1\) and \(d\ge1\) to get
\[
R_{m,k,d}\le\frac12+\frac{m^2+(m-k)^2-2m-1}{4m(2m-k)}.
\]
If the last numerator is negative, this estimate still holds, but it cannot improve the final maximum. Put \(t=m-k\), so \(0\le t\le m-1\). The nontrivial second term is \(F_m(t)/(4m)\), where
\[
F_m(t)=\frac{m^2+t^2-2m-1}{m+t}=t-m+\frac{2m^2-2m-1}{m+t}.
\]
For \(m\ge2\), \(F_m\) is strictly convex. The endpoint values satisfy
\[
F_m(m-1)=\frac{2m(m-2)}{2m-1},\qquad F_m(0)=m-2-\frac1m,
\]
with \(F_m(m-1)>F_m(0)\) for \(m\ge2\). Consequently
\[
R_{m,k,d}\le\frac12+\frac{m-2}{2(2m-1)}=\frac{3(m-1)}{2(2m-1)}.
\]
The cut with \(r=1,s=0\) attains equality. For \(m=1\), \(P_m\) is the averaging projection to constants, so its quotient seminorm is zero.

For \(m\ge3\), strict endpoint convexity, \(d/k\le1\), and \(d\ge1\) force every maximizing cut, up to complement, to have \(k=d=1\). In the layer-cake representation equality for a real signal then forces all its nontrivial superlevel sets to be a singleton or its complement. Their nesting implies the signal has exactly one exceptional coordinate, establishing the equality classification. Lastly \(3(m-1)/(2(2m-1))\) increases strictly with \(m\) and tends to \(3/4\), never reaching it at finite \(m\).

## Verification
The standalone `checker.py` uses exact rational arithmetic. It exhaustively checks all nontrivial binary signals on \(K_{m,m}\) for \(1\le m\le7\), all count-orbit cuts through \(m=100\), the explicit counting identity, strict monotonicity and the sharp limit. The infinite theorem follows from the preceding argument, not from finite computations. Running `python checker.py` prints successful check markers.

## Relationship to prior work
Lazy reversible Markov chains and their total-variation mixing have a substantial literature, including Peres and Sousi (first publicly available 2011) and Peres, Sauerwald, Sousi and Stauffer (2014). Their mixing-time and hitting/intersection-time statements concern probability-law total variation rather than this unweighted complete-pair Gini seminorm on vertex signals. A related calculation of edge-variation contraction for lazy walks on complete bipartite graphs uses only cross-part graph edges, which is a different seminorm. Existing continuous-time heat contraction formulas on complete bipartite graphs do not directly determine the exact norm of the single discrete half-lazy averaging step. No priority beyond the comparisons made is asserted.

## Limitations
The theorem does not cover unequal bipartition sizes, alternative holding probabilities, graph-edge variation, general stochastic kernels, or repeated discrete steps. The equality classification is asserted only for \(m\ge3\); the \(m=1\) and \(m=2\) norm constants are included. The literature comparison does not exclude unindexed historical equivalents, and no independent audit has been performed.

## References
- Y. Peres and P. Sousi, *Mixing times are hitting times of large sets*, arXiv:1108.0133, first submitted 2011-07-31, https://arxiv.org/abs/1108.0133.
- Y. Peres, T. Sauerwald, P. Sousi and A. Stauffer, *Intersection and mixing times for reversible chains*, arXiv:1412.8458, first submitted 2014-12-29, https://arxiv.org/abs/1412.8458.
- *Sharp edge-variation contraction of lazy walks on complete bipartite graphs*, published mathematical record, identifier `77f0e7590ff5` (distinct graph-edge seminorm).
