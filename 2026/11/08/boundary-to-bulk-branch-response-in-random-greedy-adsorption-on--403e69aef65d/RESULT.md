# Boundary-to-bulk branch response in random greedy adsorption on paths

## Finding
Let \(I(G)\) be the size of the independent set obtained by inspecting the vertices of a finite graph \(G\) in a uniformly random order and accepting a vertex precisely when no previously accepted neighbor exists. Write \(P_n\) for the path on \(n\) vertices, and \(S(a,b,1)\) for the tree consisting of three internally disjoint arms of lengths \(a,b,1\) meeting at a single central vertex. For integers \(a,b\geq1\) define the excess
\[
E_{a,b}=\mathbb E I(S(a,b,1))-\mathbb E I(P_{a+b+2}).
\]
For each fixed integer \(a\geq1\), the limit \(E_a=\lim_{b\to\infty}E_{a,b}\) exists. Define
\[
c_j=\frac1{j!}\int_0^1\!\left[(1-t)e^{-t}t^j+\frac t2e^{-t}(2-t)^j+\frac t2e^{t-2}t^j\right]dt\qquad(j\geq1).
\]
Then the **complete boundary profile** is
\[
E_a=\sum_{j=1}^a(-1)^{j+1}c_j,\qquad c_1>c_2>\cdots>0.
\]
Consequently, among all fixed positive attachment depths, \(a=2\) is the **unique minimizer**, with
\[
\boxed{\min_{a\geq1}E_a=E_2=\frac{1-5e^{-2}}2>0.}
\]
The boundary profile oscillates around the bulk value, with \(|E_a-E_{\rm bulk}|\leq c_{a+1}\). If \(\min(a,b)\to\infty\), without any condition on the ratio of the two arm lengths, then
\[
\boxed{E_{a,b}\longrightarrow E_{\rm bulk}=\frac{1-e^{-2}}4.}
\]
More precisely, with \(R_m=\sum_{j=m+1}^{\infty}2^j/j!\) and \(m=\min(a,b)\),
\[
|E_{a,b}-E_{\rm bulk}|\leq 2e^2R_m+R_{a+b+1},
\qquad |E_{a,b}-E_a|\leq e^2R_b+R_{a+b+1}.
\]
These statements concern the expectation of the *final count*, not the typical density alone. An exact finite-parameter generating function and an exact rational coefficient formula are proved below.

## Assumptions and scope
All graphs are finite, simple, and unweighted. All vertices receive independent continuous uniform arrival times on \([0,1]\), equivalent to a uniform random ordering. An arm of length \(r\) has \(r\) edges and \(r\) noncentral vertices. Thus \(S(a,b,1)\) and \(P_{a+b+2}\) have the same order, \(a+b+2\). For algebraic purposes only, allow \(a=0\) or \(b=0\): the resulting tree is a path. Define \(\Delta_{a,b}=\mathbb E I(S(a,b,1))-\mathbb E I(P_{a+b+1})\) for \(a,b\geq0\); then \(E_{a,b}=\Delta_{a,b}-\Delta_{0,a+b+1}\).

## Proof
**1. Tree-cavity probabilities.** If the root of an isolated path branch has \(r\) vertices, the probability that the root has not become occupied by time \(t\), with its parent suppressed, is
\[
f_r(t)=\sum_{j=0}^r\frac{(-t)^j}{j!},\qquad f_0(t)=1.
\]
Indeed \(f_r'(t)=-f_{r-1}(t)\): the root is occupied at an arrival time \(t\) exactly when its sole child has remained unoccupied in the cavity process. For a tree, the cavity processes on distinct branches are independent. Thus the density at time \(t\) for occupancy of a vertex is the product of the incoming branch-vacancy probabilities.

**2. Exact perturbation identity.** Begin with the path whose center separates arms of lengths \(a\) and \(b\), then add one new private leaf to the center. The new leaf contributes
\[
1-\int_0^1(1-t)f_a(t)f_b(t)dt
\]
to the expected occupancy; the change at the center is \(-\int_0^1tf_a(t)f_b(t)dt\). Their sum is \(1-\int_0^1 f_a(t)f_b(t)dt\). For a vertex at distance \(j\) on the arm of length \(a\), the added leaf changes the incoming central cavity probability by \((-1)^{j-1}\mathcal I^j[t f_b(t)]\), where \(\mathcal I h(t)=\int_0^t h(s)ds\). Multiply by the independent opposite-branch probability \(f_{a-j}(t)\) and integrate over the vertex arrival time. Sum over \(1\leq j\leq a\), and add the symmetric contribution from the arm of length \(b\).

Using \(\sum_{r\geq0}f_r(t)z^r=e^{-zt}/(1-z)\) and
\[
\sum_{j\geq1}(-1)^{j-1}z^j\mathcal I^jh(t)=z\int_0^te^{-z(t-s)}h(s)ds,
\]
followed by interchange of the two finite-time integrals, gives the exact bivariate generating function
\[
\boxed{\sum_{a,b\geq0}\Delta_{a,b}x^ay^b=\frac{N(x,y)}{(1-x)(1-y)}}
\]
for \(|x|,|y|<1\), where the *entire* symmetric numerator is
\[
N(x,y)=1-\int_0^1\!\left[(1-t)e^{-(x+y)t}+\frac t2e^{-x(2-t)-yt}+\frac t2e^{-xt-y(2-t)}\right]dt.
\]
In particular \(N(0,0)=0\). For \(p+q>0\), the exact numerator coefficient is
\[
[x^py^q]N=\frac{(-1)^{p+q+1}}{p!q!}\!\int_0^1\!\left[(1-t)t^{p+q}+\frac t2(2-t)^pt^q+\frac t2t^p(2-t)^q\right]dt,
\]
and the coefficient at \((p,q)=(0,0)\) is zero. This formula consists entirely of rational numbers and gives every \(\Delta_{a,b}\) as a finite double partial sum.

**3. Boundary and bulk limits.** Since the displayed integrands have bases in \([0,2]\) and nonnegative weights summing to one, the numerator coefficients satisfy
\[
\big|[x^py^q]N\big|\leq\frac{2^{p+q}}{p!q!}.
\]
Absolute summability therefore justifies all coefficient limits and the stated factorial bounds. In particular, when \(b\to\infty\) with \(a\) fixed,
\[
\Delta_{a,b}\to[x^a]\frac{N(x,1)}{1-x},\qquad \Delta_{0,a+b+1}\to N(0,1).
\]
As \(a,b\to\infty\), \(\Delta_{a,b}\to N(1,1)\). Direct integration yields
\[
N(0,1)=\tfrac12(1-e^{-2}),\qquad N(1,1)=\tfrac34(1-e^{-2}),
\]
proving the bulk constant and the bounds from the coefficient majorant by the union bound on the two omitted coefficient tails.

The nonconstant coefficients of \(N(x,1)\) are exactly \([x^j]N(x,1)=(-1)^{j+1}c_j\) for \(j\geq1\), giving the boundary formula. Because each factor \(t\) or \(2-t\) in the integral defining \(c_j\) is in \([0,2]\),
\[
0<c_{j+1}<\frac{2}{j+1}c_j\leq c_j\qquad (j\geq1).
\]
Strictness at \(j=1\) holds because the positive integrand is supported on \(0<t<1\), where all these factors are strictly less than two. Therefore the alternating partial sum after its second term increases in pairs above its second partial sum; its first partial sum is also larger. Thus \(a=2\) uniquely minimizes the entire positive-integer boundary profile. Elementary integration gives
\[
c_1=\frac4e-1-e^{-2},\qquad c_2=\frac4e+\frac32e^{-2}-\frac32,
\]
and hence \(c_1-c_2=(1-5e^{-2})/2\). Positivity follows from \(e^2>5\). The alternating-series error gives \(|E_a-E_{\rm bulk}|\leq c_{a+1}\), since \(\lim_{a\to\infty}E_a=N(1,1)-N(0,1)\).

## Verification
The standalone file `verify.py` constructs the expectation independently from the first-arriving-vertex recursion
\[
M(G)=1+\frac1{|V(G)|}\sum_{v\in V(G)}M(G-N[v]),\quad M(\varnothing)=0,
\]
with disconnected components handled directly. It also enumerates every vertex-priority permutation on small instances. Exact rational coefficients of \(N\) are compared with the recurrence for all \(0\leq a,b\leq5\), and numerical convergence checks compare the boundary and bulk limits. Running `python3 verify.py` produced `VERIFY_OK 62 exact comparisons and limiting-value tests` on the packaged script. No finite enumeration is used as a proof of the infinite-parameter results.

## Relationship to prior work
Krivelevich, Mészáros, Michaeli and Shikhelman established path minimality for the random greedy independent-set expectation on trees, and identified the infinite-path occupation density. Their results do not state a finite-defect boundary profile, an optimal nonterminal attachment depth, or the boundary-to-bulk constant for one pendant-branch perturbation. Penrose and Sudbury established general blocking random-sequential-adsorption equations and exact formulas for regular infinite trees; those methods motivate the tree-cavity calculation, but the inspected material does not report this exact three-arm perturbation law. Here the subject is an **order-one excess**, which is invisible to the ordinary size-normalized local limit and is not determined by the general path-minimality inequality. Priority beyond the inspected sources is not established.

## Limitations
The unique minimum is proved for the limiting boundary profile \(E_a\) with \(a\) fixed and \(b\to\infty\), **not** for every finite \(b\) or among all nonpath trees. The bulk law assumes both long arms diverge. The result does not determine the full distribution of the greedy set, nor does it establish an independent priority audit. General RSA and tree transformation machinery may admit alternate derivations; exhaustive historical novelty is not proved.

## References
1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first publicly posted 2019-07-16), later *Random Structures & Algorithms* 64 (2024), DOI 10.1002/rsa.21200. https://arxiv.org/abs/1907.07216 and https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.21200
2. M. D. Penrose, A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519 (2005), *Annals of Applied Probability* 15 (2005), 853–889. https://arxiv.org/pdf/math/0503519
