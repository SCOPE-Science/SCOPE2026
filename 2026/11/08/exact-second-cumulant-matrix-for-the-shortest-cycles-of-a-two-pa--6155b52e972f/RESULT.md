# Exact triangle underdispersion in the two-parent uniform-attachment multigraph

## Finding

Start with vertex 1. Independently for each vertex $j\ge2$, choose two independently uniform targets in $\{1,\ldots,j-1\}$ and add the two labeled edges from $j$ to those targets. Retain parallel edges. Let $C_3(n)$ count triangles on three distinct vertices through size $n$, ignoring the edge directions and counting each choice of labeled edges separately. Write $H_m^{(r)}=\sum_{j=1}^m j^{-r}$, $H_m=H_m^{(1)}$, and $S_m=\sum_{t=2}^m H_{t-1}/t^2$. For every $n\ge2$ the exact variance correction is
\[
\boxed{\operatorname{Var}C_3(n)-\mathbb EC_3(n)=4S_{n-1}-16\big(H_{n-1}^{(2)}-2H_{n-1}^{(3)}+H_{n-1}^{(4)}\big).}
\]
The known mean is $4(H_{n-1}-H_{n-1}^{(2)})$. The correction is zero at $n=2,3$, strictly negative at every $n\ge4$, and converges to $36\zeta(3)-16\zeta(2)-16\zeta(4)\approx -0.3620682952$.

## Assumptions and scope

Both outgoing edges are labeled, sampling is with replacement, and outdegree is exactly two. The triangle convention includes two choices when the older edge of a given triangle is double; this is not a simple-graph or directed-cycle statistic.

## Proof

Let $\mathcal F_t$ be the history after vertex $t$, $M_t(u,v)$ the old multiplicity between distinct vertices, $D_t$ the number of double pairs, and $X_{t+1}$ the number of new triangles. If the two targets coincide, $X_{t+1}=0$; otherwise it equals the multiplicity between them. There are $2(t-1)$ old labeled edges, and no multiplicities above two, so
\[
\sum_{u<v}M_t(u,v)=2(t-1),\qquad \sum_{u<v}M_t(u,v)^2=2(t-1)+2D_t.
\]
Each unordered target pair occurs with probability $2/t^2$. Thus
\[
\mathbb E[X_{t+1}\mid\mathcal F_t]=\mu_t:=4(t-1)/t^2,\qquad
\mathbb E[X_{t+1}^2\mid\mathcal F_t]=\mu_t+4D_t/t^2.
\]
The deterministic conditional mean makes the centered increments orthogonal in $L^2$. Also, $\mathbb ED_t=H_{t-1}$ since the double-edge probability at each birth $j$ is $1/(j-1)$. Subtracting the summed mean from the summed variances gives $\sum_{t=2}^{n-1}(4H_{t-1}/t^2-\mu_t^2)$, which is the displayed formula. The first term converges using $\sum_{t=2}^\infty H_{t-1}/t^2=\zeta(3)$: expand $\tfrac12\log^2(1-x)$ into the power series with coefficient $H_{t-1}/t$ and integrate against $1/x$ on $[0,1]$. Alternatively the resulting integral is $\tfrac12\int_0^1\log^2 y/(1-y)\,dy$, evaluated termwise by the geometric series. The other sums converge absolutely to their zeta values.

For the strict finite-size sign, write the $t$th summand as $4f(t)/t^2$ with $f(t)=H_{t-1}-4(1-1/t)^2$. We have $f(2)=0$. Direct rational substitution gives $f(3),\ldots,f(7), f(21)<0<f(22)$. For $t\ge7$,
\[
f(t+1)-f(t)=\frac1t\left[1-\frac4{t+1}\left(2-\frac1t-\frac1{t+1}\right)\right]>0.
\]
Hence the corrections decrease strictly after $n=3$ until the minimum and then increase. The limit is negative: with $R=100$ the integral tail bound gives
\[
36\zeta(3)-16\zeta(2)-16\zeta(4)
\le36\left(H_R^{(3)}+\frac1{2R^2}\right)-16H_R^{(2)}-16H_R^{(4)}<-\frac15.
\]
The last inequality is a rational comparison. Together these facts prove negativity at every $n\ge4$.

## Verification

The bundled `checker.py` can be run using Python 3 and its standard library. It compares exact rational moments by exhaustive histories through $n=6$ and checks the rational sign and tail bounds. Its other, previously known moment identities are included as cross-checks of the sampling convention. Finite enumeration does not establish the theorem for general $n$; the calculation above supplies that proof.

## Relationship to prior work

Björklund, Holmgren, Janson and Lo give the exact triangle mean (Example 3.4, Eq. (3.10)) and product-Poisson approximation (Theorem 3.3) in the same labeled-edge convention. Variance-order and overlap bounds do not determine the order-one correction above. The earlier Resultary finding *Exact negative covariance of two- and three-cycle counts in uniform attachment* proves the exact parallel-pair variance and cross-covariance for general fixed outdegree, including the signs and limits of those earlier corrections. In particular, restricting its results to outdegree two does not produce a new parallel-pair variance or cross-covariance. The present finding is only the triangle diagonal: its exact finite correction, sign, and limiting constant. That correction quantifies the variance discrepancy left invisible by a first-order Poisson approximation with a diverging mean.

## Limitations

No variance formula for larger outdegree, simple-graph triangles, longer cycles, or higher cumulants is claimed. The prior-work comparison cannot exclude an unlocated equivalent triangle calculation.

## References

- J. Björklund, C. Holmgren, S. Janson and T. Y. Y. Lo, *Approximation of Subgraph Counts in the Uniform Attachment Model*, https://doi.org/10.1017/S0963548324000294 ; https://arxiv.org/abs/2311.04184 .
- *Exact negative covariance of two- and three-cycle counts in uniform attachment*, Resultary, October 25, 2026 UTC, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-negative-covariance-of-two-and-three-cycle-counts-in-unifo--0b5f2161f223/RESULT.md .
