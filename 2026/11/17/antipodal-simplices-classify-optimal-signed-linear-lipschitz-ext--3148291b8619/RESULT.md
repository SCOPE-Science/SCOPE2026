# Antipodal simplices classify optimal signed linear Lipschitz extensions from finite cycles

## Finding

**Theorem (sharp signed-optimizer classification).** On the unweighted shortest-path cycle \(C_n\), \(n\ge3\), write the vertices as \(\mathbb Z/n\mathbb Z\), with \(d(i,j)=\min\{|i-j|,n-|i-j|\}\). Put
\[
 c_n=\frac{\lfloor n^2/4\rfloor}{n},\qquad \Phi(w)=\max_{i\in C_n}\left\|\delta_i-\sum_{j\in C_n}w_j\delta_j\right\|_{\mathcal F(C_n)},
 \quad\sum_j w_j=1.
\]
The coefficients may be **signed**. The exact minimum is \(\min_w\Phi(w)=c_n\). Its **complete** minimizer set is
\[
\operatorname*{argmin}\Phi=\begin{cases}
\{(1/n,\dots,1/n)\},& n\text{ odd},\\[3pt]
\operatorname{conv}\big\{\tfrac12(\mathbf e_j+\mathbf e_{j+m}):0\le j<m\big\},&n=2m\text{ even}.
\end{cases}
\]
In the even case this is a simplex of affine dimension \(m-1\); in the odd case it is a singleton.

Adjoin one new point \(o\) with \(d(o,j)=R\) for all old vertices, where \(R\ge\lfloor n/2\rfloor/2\) (the exact necessary and sufficient triangle-inequality bound). Among all real-linear simultaneous extension operators \(E:\operatorname{Lip}(C_n)\to\operatorname{Lip}(C_n\cup\{o\})\) bounded for the Lipschitz seminorm,
\[
 \min_E\|E\|=\max\left\{1,\frac{c_n}{R}\right\}.
\]
For \(R\le c_n\), the set of **all** optimal extensions is exactly the signed-coefficient minimizer set above. For \(R>c_n\), it is the compact full-dimensional (dimension \(n-1\)) convex polytope
\[
 \Big\{w\in\mathbb R^n:\sum_jw_j=1,\ \Phi(w)\le R\Big\}.
\]
For even \(n=2m\) the metric bound already forces \(R\ge c_n=m/2\); hence the antipodal simplex occurs exactly at the metric boundary and a full-dimensional optimal polytope occurs above it. For odd cycles the uniform optimizer is unique throughout the interval \(\lfloor n/2\rfloor/2\le R\le c_n\).

## Assumptions and scope

The graph metric has unit-length cycle edges and **no other edges**; its diameter is \(\lfloor n/2\rfloor\). All functions are real-valued, all operators real-linear, and the Lipschitz seminorm is \(\max_{i\ne j}|f(i)-f(j)|/d(i,j)\). In a finite-dimensional seminormed space a bounded extension must preserve constants: a zero-seminorm constant cannot acquire a nonconstant extension. Thus every candidate has \((Ef)(i)=f(i)\) on old vertices and \((Ef)(o)=\sum_jw_jf(j)\) with \(\sum_j w_j=1\). The notation \(\mathcal F(C_n)\) is the real Lipschitz-free space modulo constants, and the displayed signed Dirac combination is a mass-zero element. No positivity assumption is built into the minimax problem.

## Proof

**1. Exact extension norm and universal lower bound.** By definition of the Lipschitz-free norm,
\[
 \|E_w\|=\max\{1,\Phi(w)/R\}.
\]
Let \(D\) denote the cycle distance matrix, \(D_{ij}=d(i,j)\). For every \(i\), the function \(f_i(j)=-d(i,j)\) has Lipschitz seminorm one. As \(f_i(i)=0\), it yields
\[
 \Phi(w)\ge \sum_jw_j d(i,j)=(Dw)_i.
\]
Every row and column of \(D\) has sum \(n c_n\), so \(n^{-1}\sum_i(Dw)_i=c_n\), even for signed coefficients. Hence \(\Phi(w)\ge c_n\). Uniform coefficients \(w_j=1/n\) are nonnegative, and for every one-Lipschitz \(f\),
\[
 \left|f(i)-\sum_j w_jf(j)\right|\le \sum_j w_jd(i,j)=c_n.
\]
Consequently uniform weights attain the bound, proving both the exact minimax radius and the extension-norm formula. This optimal **value**, by itself, follows more generally from earlier transitive-metric averaging and is **not** asserted to be new.

**2. A necessary discrete harmonic equation.** If \(\Phi(w)=c_n\), then each \((Dw)_i\le c_n\) while their arithmetic mean is \(c_n\). Thus \(Dw=c_n\mathbf1\). Let \(g=Dw\), and form \(\Delta^2g_i=g_{i-1}-2g_i+g_{i+1}\), with subscripts mod \(n\). Directly taking the second differences of the cycle distance profile gives, for odd \(n=2m+1\),
\[
 \Delta^2g_i=2w_i-w_{i+m}-w_{i+m+1}=0.
\]
For even \(n=2m\) one gets
\[
 \Delta^2g_i=2w_i-2w_{i+m}=0.
\]
These identities can also be verified directly by noting that the cycle distance profile has discrete second derivative \(+2\) at zero and negative masses at its one or two antipodes.

**3. Odd cycles: rigidity even for signed coefficients.** For odd \(n\), every weight is the arithmetic mean of the weights shifted by \(m\) and \(m+1\). Choose an index attaining the maximum weight (the weights are real and finite). Both shifted weights must attain that same maximum. Iterating the shift by \(m\) visits all vertices, since \(\gcd(m,2m+1)=1\). All weights are therefore equal, and their sum forces \(w_j=1/n\).

**4. Even cycles: an antipodal simplex and signed positivity.** The even second-difference equation requires \(w_i=w_{i+m}\) for every \(i\). Suppose one of these coefficients, say \(w_j\), is strictly negative, and take \(i=j+m\). Start with \(f(k)=-d(i,k)\). Then \(f(i)-\sum_kw_kf(k)=(Dw)_i=c_n\). Increase only \(f(j)\) by exactly \(1\); at the antipode \(j\), the original value is \(-m\), and both neighbors have value \(-m+1\). Therefore all cycle-edge differences remain at most one and the perturbed function is still one-Lipschitz for the entire shortest-path metric. Its displayed signed functional grows by \(-w_j>0\), contradicting \(\Phi(w)=c_n\). All weights must therefore be nonnegative.

Conversely, if \(w_j=w_{j+m}\ge0\) and \(\sum_j w_j=1\), then \(d(i,j)+d(i,j+m)=m\) for every \(i,j\). Thus \((Dw)_i=m/2=c_n\). Positivity and the triangle inequality yield \(\Phi(w)\le\max_i(Dw)_i=c_n\); the universal lower bound gives equality. The independent coordinates \(w_0,\ldots,w_{m-1}\) are nonnegative and sum to \(1/2\), proving exactly the claimed simplex and its dimension.

**5. All operators and the phase transition.** If \(R\le c_n\), \(\max\{1,\Phi(w)/R\}\) is minimal precisely when \(\Phi(w)=c_n\). If \(R>c_n\), the minimum is one and the optimizer set is exactly the sublevel polytope \(\Phi(w)\le R\). This sublevel set is a polytope because \(\Phi\) is a maximum of finitely many affine functionals and their negatives, using the finitely many extreme points of the finite Lipschitz dual polytope. The uniform vector has strict slack, so the set has dimension \(n-1\) in the coefficient hyperplane. It is bounded because \(\Phi\) controls the norm of the mass-zero vector \(\sum_j w_j\delta_j-\delta_0\) up to an additive bounded term, and the Lipschitz-free norm is nondegenerate on the zero-sum subspace. Hence the polytope is compact.

## Verification

The standalone Python 3 script `verification/check_cycle_extensions.py` enumerates all integer one-Lipschitz dual potentials with a fixed anchor on each cycle \(3\le n\le12\), then tests exact rational dual radii of the uniform and antipodal measures, signed antipodal perturbations, non-antipodal candidates and odd-cycle nonuniform signed weights. The integer potential enumeration is exhaustive for those finite dual polytopes because the graph-edge difference-constraint matrix is totally unimodular, so every extreme point has integer vertex values after anchoring. The script independently checks the distance-matrix row sum identity and prints `SIGNED_CYCLE_CHEBYSHEV_SIMPLEX_ALL_CHECKS_PASS`. This finite computation does not establish the infinite-dimensional-parameter theorem, which is proved analytically above.

## Relationship to prior work

Bruè, Di Marino and Stra (2018) construct general simultaneous real-linear Lipschitz extensions by random projections; Ambrosio and Puglisi (2016) relate extension operators to transport and Lipschitz-free geometry. Pass (2020) gives a general probability-measure minimax/variance framework. Crucially, the published regular-polygon snowflake result listed below already proves the **optimal norm by transitive averaging for any finite homogeneous metric**. Applying that value statement to a cycle gives the value \(\max\{1,c_n/R\}\). The claim here deliberately **excludes novelty of that optimal value**: its contribution is the *complete equality-set classification for arbitrary signed linear coefficients*, including the positivity-forcing antipodal argument, odd/even dimension law, and full optimizer polytope after the radius threshold. Neither the fully inspected 2016/2018/2020 sources nor the inspected published regular-polygon result states those stronger equality and signed-rigidity conclusions for intrinsic graph-cycle metrics. The graph-cycle metric is also not the polygonal chord-distance snowflake used in the regular-polygon study.

## Limitations

The theorem is restricted to unit-edge shortest-path cycles, one equidistant extra point satisfying the metric triangle inequality, real scalar functions and bounded real-linear extensions. It does not classify unequal edge-weight cycles, multiple added points or complex-linear operators. Even-cycle distance-matrix nullities are classical and not claimed original. Prior formulations of signed optimal-transport one-centers or graph facility-location minimizers could imply an equivalent equality classification; absence of a discovered formulation does not prove priority. No independent mathematical audit has been performed.

## References

1. E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and C¹ extension operators through random projection*, arXiv:1801.07533v1 (first public 2018-01-23), https://arxiv.org/abs/1801.07533. Sections 3–4.
2. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450v1 (2016-09-06), https://arxiv.org/abs/1609.01450. Section 2.
3. B. Pass, *Generalized barycenters and variance maximization on metric spaces*, arXiv:2006.02984v1 (2020-05-29), https://arxiv.org/abs/2006.02984. Proposition 10.
4. *A sharp snowflake threshold for simultaneous linear Lipschitz extensions from regular polygons*, publicly available result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-snowflake-threshold-for-simultaneous-linear-lipschitz-ex--55dc55bc9348. Its Step 1 explicitly proves the general homogeneous-metric optimal-value assertion and is acknowledged as prior work.
