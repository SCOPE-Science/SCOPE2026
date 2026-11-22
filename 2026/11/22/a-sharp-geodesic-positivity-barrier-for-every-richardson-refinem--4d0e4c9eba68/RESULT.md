# A sharp geodesic positivity barrier for every Richardson refinement of backward Euler

## Finding

Let \(L\) be the unnormalized Laplacian of any finite connected undirected graph with strictly positive edge conductances. For each integer \(r\ge2\) define the completed second-order Richardson-extrapolated backward-Euler step
\[
T_r(h)=\frac{r(I+hL/r)^{-r}-(I+hL)^{-1}}{r-1},\qquad h\ge0.
\]
Define the strictly decreasing-in-\(k\) sequence (for \(k\ge1\))
\[
b_{r,k}=\binom{r+k-1}{k}r^{-k}
=\frac1{k!}\prod_{j=0}^{k-1}\left(1+\frac jr\right),\qquad
 d_r=\min\{k\ge2:r b_{r,k}<1\}.
\]
The integer \(d_r\) is finite. For distinct vertices \(u,v\) at graph distance \(d\), let \(\Gamma_d(u,v)\) be their length-\(d\) geodesics. The coefficient of the first graph-distance-permitted small-step power is exactly
\[
[T_r(h)]_{uv}=\frac{r b_{r,d}-1}{r-1}\,
\left(\sum_{\gamma\in\Gamma_d(u,v)}\prod_{e\in\gamma}w_e\right)h^d+O(h^{d+1})
\qquad(h\downarrow0).
\]
Thus for every integer \(r\ge2\), **every** such graph with diameter at least \(d_r\) has a strictly negative entry for **all sufficiently small positive** steps. The unit-weight path with \(d_r+1\) vertices is an explicit witness. Every connected finite graph nevertheless has strictly positive entries for all sufficiently large steps, because \(T_r(h)\) converges entrywise to the uniform stationary projector. Consequently each long-enough path exhibits a genuine small-step positivity failure followed by eventual recovery.

The barrier grows extremely slowly with refinement:
\[
\boxed{\displaystyle d_r\sim\frac{\log r}{\log\log r}\quad(r\longrightarrow\infty).}
\]
In particular \(d_r=4\) for \(2\le r\le17\), \(d_r=5\) for \(18\le r\le109\), and \(d_r=6\) for \(110\le r\le704\). For the usual two-half-step extrapolation, \(r=2\), the five-vertex path at \(h=1/100\) has endpoint-to-endpoint entry
\[
[T_2(1/100)]_{1,5}=-\frac{3579497503436509}{1090661149177367377845455}<0,
\]
even though each constituent backward-Euler transition is strictly positive.

## Assumptions and scope

The vertices and edges form a finite, connected, loopless, undirected weighted graph; each present edge has weight \(w_e>0\). Multiple edges may be collapsed by adding conductances. The combinatorial Laplacian has \(L_{ii}=\sum_{j\ne i}w_{ij}\) and \(L_{ij}=-w_{ij}\) for \(i\ne j\). The integer \(r\) counts equal backward-Euler substeps over the *same* macro-step \(h\); it is not an extrapolation depth. The completed extrapolated matrix is used once on a column state. All matrices are evaluated exactly as mathematical functions, with no roundoff assertions.

Distance refers to the **number of graph edges** in a shortest path, not effective resistance or weighted shortest-path length; the conductances determine the positive geodesic sum. The theorem supplies an exact small-step sign criterion for entries at each distance, a sufficient diameter obstruction, and eventual recovery. It does not claim full-step positivity of graphs with smaller diameter, nor classify every intermediate positivity interval.

## Proof

**Taylor coefficients.** For \(|z|\) sufficiently small, the negative-binomial identity gives
\[
(1+z/r)^{-r}=\sum_{k\ge0}(-1)^k b_{r,k}z^k,
\qquad
(1+z)^{-1}=\sum_{k\ge0}(-1)^k z^k.
\]
Consequently
\[
R_r(z):=\frac{r(1+z/r)^{-r}-(1+z)^{-1}}{r-1}
=\sum_{k\ge0}(-1)^k a_{r,k}z^k,
\qquad a_{r,k}=\frac{rb_{r,k}-1}{r-1}.
\]
In particular \(a_{r,0}=a_{r,1}=1\), \(a_{r,2}=1/2\), so the method is second-order consistent with exponential decay. The formula is analytic near zero, and matrix functional calculus permits substitution \(z=hL\).

**Sharp coefficient boundary.** For each integer \(k\ge1\),
\[
\frac{b_{r,k+1}}{b_{r,k}}=\frac{r+k}{r(k+1)}<1
\]
because \(r\ge2\) and \(k\ge1\). Also \(b_{r,1}=1\) and \(b_{r,k}\to0\), the latter from the explicit negative-binomial coefficients or the ratio limit \(1/r<1\). Hence \(d_r\) exists, \(a_{r,d_r}<0\), and all preceding \(a_{r,k}\), with \(1\le k<d_r\), are nonnegative. Equality is allowed (notably \(a_{2,3}=0\)); no stronger assertion about the next Taylor term of such an entry is made.

**Geodesic coefficient.** If \(u\ne v\) are separated by \(d\) edges, \((L^k)_{uv}=0\) for every \(k<d\): every nonzero matrix-product term must move between adjacent vertices at least \(d\) times. At \(k=d\), no diagonal factor or detour can occur and every nonzero term is a shortest path, giving
\[
(L^d)_{uv}=(-1)^d\sum_{\gamma\in\Gamma_d(u,v)}\prod_{e\in\gamma}w_e.
\]
The path-weight sum is strictly positive. Substituting the Taylor series of \(R_r(hL)\) and canceling the two signs proves the displayed leading term. If the graph diameter is at least \(d_r\), take a length-\(d_r\) subpath of a diameter geodesic. At its endpoints the coefficient is strictly negative, establishing the small-step failure.

**Eventual recovery.** The connected weighted Laplacian is symmetric positive semidefinite with a simple zero eigenvalue and all other eigenvalues strictly positive. Since \(R_r(0)=1\) and \(R_r(z)\to0\) for \(z\to+\infty\), the spectral theorem gives
\[
\lim_{h\to\infty}T_r(h)=\frac1n\mathbf1\mathbf1^\top.
\]
All its entries are \(1/n>0\); finite dimension therefore yields a common sufficiently large step after which every entry is strictly positive. Both backward-Euler constituent matrices are themselves strictly positive for any \(h>0\), by the irreducible nonsingular \(M\)-matrix inverse property or the positive-time resolvent integral. The sign failure is caused by subtraction in Richardson extrapolation.

**Refinement asymptotic.** Put \(A_r=\log r/\log\log r\). For each fixed \(\epsilon\in(0,1)\), let \(k_-=\lfloor(1-\epsilon)A_r\rfloor\) and \(k_+=\lceil(1+\epsilon)A_r\rceil\). These satisfy \(k_\pm^2/r\to0\). Uniformly for either choice,
\[
\log b_{r,k}=-\log(k!)+\sum_{j=0}^{k-1}\log(1+j/r)
=-\log(k!)+o(1).
\]
Stirling's formula yields \(\log(k_\pm!)=(1\pm\epsilon+o(1))\log r\), so \(r b_{r,k_-}>1\) and \(r b_{r,k_+}<1\) for all sufficiently large \(r\). Monotonicity in \(k\) implies \(k_-<d_r\le k_+\). Letting \(\epsilon\downarrow0\) proves \(d_r\sim A_r\). Exact integer comparisons of \(rb_{r,k}\) give the finite refinement ranges quoted above.

## Verification

The standalone `VERIFY.py` computes coefficients with integer binomial coefficients and rational numbers, verifies symbolic identities for the initial five coefficients, and checks the exact first-negative distances for integer refinement factors \(2,3,17,18,109,110,704,705\). It reconstructs the path graph's completed matrix by exact symbolic inversion and confirms the displayed rational negative endpoint at \(h=1/100\), its positive value \(2759/218405\) at \(h=1\), symmetry, preservation of the constant vector and positive diagonal entries in the chosen example. Run `python VERIFY.py` with Python 3 and SymPy available.

These finite checks illustrate and corroborate the formulas. The all-graph/all-refinement statements and their asymptotic are proved by the analytic, combinatorial and spectral arguments above, not by a finite enumeration.

## Relationship to prior work

Richardson extrapolation and its order improvement are classical. Zlatev, Faragó and Havasi (2011/2012) analyze compositions of extrapolation, implicit \(\theta\)-steps and splitting, including the completed two-half-step linear stability function; Mona, Lagzi and Havasi (2015) experimentally investigate extrapolation for one-dimensional reaction–diffusion, using forward Euler as base. These establish the method and motivation, not this graph-geodesic classification.

Publicly available related results include an exact **scalar** positivity threshold for the same Richardson map with all refinement factors, an exact **diagonal** positivity cutoff for two-half-step Richardson diffusion on weighted graphs, and a five-state **directed pure-birth** small-step sign hole. The scalar result concerns \(R_r(z)\) at positive real \(z\), the graph result only diagonal entries with \(r=2\), and the birth-chain result only one directed generator with \(r=2\). None of those statements determines a negative off-diagonal entry for every large-diameter undirected weighted graph at arbitrary refinement \(r\), nor the logarithmic-over-logarithmic geodesic barrier. Other rational integrators can have distance obstructions of their own, but their coefficients differ from those of this Richardson map.

## Limitations

The sufficient diameter condition is not asserted to be necessary for the existence of a negative entry at an intermediate timestep. No complete positivity phase diagram or optimal graph-order threshold for arbitrary steps is claimed. The asymptotic concerns the first **negative leading geodesic coefficient**, not the scalar stability-function positivity radius or a minimum total number of edges among all negative examples. The results assume connected symmetric Laplacians and exact arithmetic; nonsymmetric Markov generators, nonnormal stability, nonlinear maximum principles, and roundoff are outside scope. A relevant older extrapolation literature could contain an equivalent geodesic-coefficient statement not located in the inspected material; independent validation has not been performed.

## References

1. Z. Zlatev, I. Faragó, and Á. Havasi, *Richardson Extrapolation combined with the sequential splitting procedure and the \(\theta\)-method*, *Central European Journal of Mathematics* 10 (2012), 159–172, DOI https://doi.org/10.2478/s11533-011-0099-7. Accessible complete text: https://www.researchgate.net/publication/257907630_Richardson_Extrapolation_combined_with_the_sequential_splitting_procedure_and_the_th-method (publication month given as December 2011).
2. T. Mona, I. Lagzi, and Á. Havasi, *Solving Reaction-Diffusion and Advection Problems with Richardson Extrapolation*, *Journal of Chemistry* 2015, article 350362, first published April 1, 2015, https://doi.org/10.1155/2015/350362.
3. *Richardson acceleration creates a sharp positivity barrier for backward Euler*, public mathematical research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1.
4. *The sharp 28–29 self-transition barrier for Richardson-accelerated graph diffusion*, public mathematical research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-sharp-28-29-self-transition-barrier-for-richardson-accelerat--56edd79ad0f3.
5. *Re-entrant positivity of Richardson-extrapolated backward Euler on five-state pure-birth chains*, public mathematical research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-re-entrant-positivity-of-richardson-extrapolated-backward-euler--c08f9b38b493.
