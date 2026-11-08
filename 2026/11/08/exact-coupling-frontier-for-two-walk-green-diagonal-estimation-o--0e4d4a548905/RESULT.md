# Exact coupling frontier for two-walk Green-diagonal estimation on an edge

## Finding

Consider the connected two-vertex graph with permutation adjacency matrix \(P=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). Fix a stopping probability \(p\in(0,1)\), write \(q=1-p\), and let \(G=(I-qP)^{-1}\). A stopped walk starts at vertex zero, alternates deterministically along the edge and survives each potential move with probability \(q\). Each visited vertex receives unit load. If \(L\in\{0,1,2,\ldots\}\) is the number of moves, the load at the starting vertex is \(Z=1+\lfloor L/2\rfloor\), and \(\mathbb EZ=G_{00}=1/(1-q^2)\).

Estimate this entry with exactly two walks, \(\widehat G_{00}=(Z_1+Z_2)/2\), allowing an arbitrary dependence between their lengths but keeping each marginal geometric: \(\mathbb P(L_i\ge \ell)=q^\ell\). Define \(t=q^2\), \(r=(1-2p)_+=\max\{1-2p,0\}\), \(\mu=t/(1-t)\), and the finite sum

\[
J(t)=\sum_{j,k\ge1}\bigl(t^j+t^k-1\bigr)_+.
\]

**The exact minimum variance over all such couplings** is

\[
\boxed{V_*(p)=\tfrac12\bigl(\mu+J(t)\bigr).}
\]

It is achieved by *global inverse-CDF antithetic lengths*: take one \(U\) uniform on \((0,1)\), set \(L_1=F_L^{-1}(U)\) and \(L_2=F_L^{-1}(1-U)\). This is an optimal coupling, not necessarily a unique one.

For comparison, use the original **stepwise antithetic termination rule**, pairing fresh per-step uniforms by a half-cycle shift. Its exact variance is

\[
\boxed{V_{\mathrm{step}}(p)=\tfrac12\left[\mu+\frac{r^2(1+t)}{(1-r^2)(1-t)}\right].}
\]

Consequently \(V_*(p)<V_{\mathrm{step}}(p)\) for every \(0<p<1/2\), and \(V_*(p)=V_{\mathrm{step}}(p)\) for \(1/2\le p<1\). A second exact phase boundary is

\[
\boxed{J(t)=0\quad\Longleftrightarrow\quad p\ge 1-1/\sqrt2.}
\]

In this regime an optimal coupling never makes both walks revisit their starting vertex; nevertheless, stepwise antithetic termination still incurs a strictly positive overlap penalty whenever \(p<1/2\).

For instance, at \(p=1/3\),

\[
\boxed{V_*=2/5,\qquad V_{\mathrm{step}}=9/16,\qquad V_{\mathrm{iid}}=18/25.}
\]

This is an exact reduction of \(13/45\) in variance relative to stepwise antithetic termination, using two walks with the same length marginals. The long-walk limit is also sharp:

\[
\boxed{\lim_{p\downarrow0}\frac{V_*(p)}{V_{\mathrm{step}}(p)}=2-\frac{\pi^2}{6}\simeq0.355065933152,\qquad \lim_{p\downarrow0}\frac{V_{\mathrm{step}}(p)}{V_{\mathrm{iid}}(p)}=1.}
\]

Thus, on this canonical example, the globally length-antithetic coupling asymptotically removes about \(64.5\%\) of the variance left by stagewise antithetic stopping, whereas the latter's advantage over independent walks vanishes in relative terms.

## Assumptions and scope

All statements hold for every real \(p\in(0,1)\), with independent fair auxiliary uniforms at each stage of the stepwise method. Walks stop before the next proposed move with probability \(p\). The weight of an \(\ell\)-step path is \(q^\ell\), and its survival probability is \(q^\ell\), so the corresponding importance-corrected visit load is exactly one. Both methods therefore use the same unbiased walk-level estimator. Walk lengths may be jointly dependent but each must have the specified geometric marginal; walker directions on this single-edge graph are deterministic. Variance is per two-walk estimate, not per unit wall-clock time. No claim concerns the distinct, bilinear graph-random-feature estimator of the squared resolvent \((I-qP)^{-2}\).

The sum defining \(J(t)\) is actually finite for each \(t<1\): if \(j\) is large enough that \(t^j+t\le1\), all summands in its row vanish. A reproducible exact evaluation may use the finite cutoffs \(B=\max\{j\ge1:t^j+t>1\}\) (with an empty set interpreted as \(B=0\)) and \(b_j=\max\{k\ge1:t^j+t^k>1\}\), in which case

\[
J(t)=\sum_{j=1}^B\left[b_j(t^j-1)+\frac{t(1-t^{b_j})}{1-t}\right].
\]

The strict inequalities in these cutoffs accommodate all equality points without ambiguity.

## Proof

**1. Normalization and moment reduction.** The length law is \(\mathbb P(L=\ell)=pq^\ell\). The number of *additional* visits to vertex zero is \(K=\lfloor L/2\rfloor\). Thus, for every integer \(j\ge1\),

\[
\mathbb P(K\ge j)=\mathbb P(L\ge2j)=t^j.
\]

Consequently \(K\) has a geometric tail, \(\mathbb EK=\mu=t/(1-t)\) and \(\operatorname{Var}(K)=t/(1-t)^2=\mu+\mu^2\). In particular, \(\mathbb EZ=1+\mu=1/(1-t)\). The Neumann expansion of the resolvent yields the same diagonal, because \((P^{2j})_{00}=1\) and \((P^{2j+1})_{00}=0\).

For any coupling of \(K_1,K_2\) with these marginals, put \(M=\mathbb E[K_1K_2]\). Expanding the variance of their average gives the exact identity

\[
\operatorname{Var}(\widehat G_{00})=\frac12\bigl(\mu+M\bigr).
\]

In particular, independent walkers have \(M=\mu^2\) and variance \(V_{\mathrm{iid}}=\tfrac12\mu(1+\mu)=t/[2(1-t)^2]\).

**2. Attainable global minimum.** By the layer-cake formula for nonnegative integer variables and the elementary Fréchet intersection bound,

\[
M=\sum_{j,k\ge1}\mathbb P(K_1\ge j,K_2\ge k)
\ \ge\ \sum_{j,k\ge1}(t^j+t^k-1)_+=J(t).
\]

Use the generalized inverse CDF of the geometric length law and \(U,1-U\) as in the statement. As \(K\) is an increasing function of \(L\), this realizes \(K_1=F_K^{-1}(U)\), \(K_2=F_K^{-1}(1-U)\). Each pair of events becomes an interval intersection:

\[
\{K_1\ge j\}=\{U>1-t^j\},\qquad
\{K_2\ge k\}=\{U<t^k\}.
\]

Their intersection has length \((t^j+t^k-1)_+\), attaining all the lower bounds *simultaneously*. This proves the exact minimum and its attainability over all joint laws, not only over a finite family of permutations or a restricted optimization class. Since the largest term in \(J(t)\) is \((2t-1)_+\), and every other term is no larger, \(J(t)=0\) exactly when \(2t\le1\), equivalently \(p\ge1-1/\sqrt2\).

**3. Stagewise antithetic variance.** Independently at each potential move, draw \(R\) uniform on \((0,1)\), and apply stopping tests to \(R\) and \((R+1/2)\bmod1\). Each walker stops marginally with probability \(p\). The probability that *both* survive one common timestep is \(r=(1-2p)_+\), while any single walker survives a further timestep with probability \(q\). Therefore for any nonnegative integers \(u,v\),

\[
\mathbb P(L_1\ge u,L_2\ge v)=r^{\min(u,v)}q^{|u-v|}.
\]

The identity includes the case \(r=0\), interpreted using the usual empty-product convention. For \(K_i=\lfloor L_i/2\rfloor\),

\[
M_{\mathrm{step}}=\sum_{j,k\ge1}r^{2\min(j,k)}t^{|j-k|}
=\left(1+2\sum_{d\ge1}t^d\right)\sum_{m\ge1}r^{2m}
=\frac{r^2(1+t)}{(1-r^2)(1-t)}.
\]

Substituting into the variance identity gives the claimed exact expression. If \(p\ge1/2\), then \(r=0\), so \(M_{\mathrm{step}}=J(t)=0\). If \(0<p<1/2\), the event \(\{K_1\ge1,K_2\ge1\}\) under stepwise sampling has probability \(r^2\), strictly larger than its minimum \((2t-1)_+\): the excess is \(2p^2>0\) when \(2t>1\), and \(r^2>0\) otherwise. All the other joint-tail terms separately obey their Fréchet bounds. Hence \(M_{\mathrm{step}}>J(t)\) and the strict phase classification follows.

**4. Rational example.** At \(p=1/3\), \(t=4/9\), \(r=1/3\), \(\mu=4/5\), and \(J(t)=0\) since \(2t<1\). Also \(M_{\mathrm{step}}=13/40\), yielding \(V_*=2/5\), \(V_{\mathrm{step}}=9/16\), and \(V_{\mathrm{iid}}=18/25\) by direct substitution. The relative stagewise-to-global reduction is \(1-(2/5)/(9/16)=13/45\).

**5. Long-walk limit.** Write \(\varepsilon=1-t\), so \(\varepsilon\sim2p\) as \(p\downarrow0\). For the optimal inverse-CDF coupling, \(\varepsilon K_1\to-\log(1-U)\) and \(\varepsilon K_2\to-\log U\) pointwise outside a null set. For \(t\) sufficiently near one, the products are dominated by an integrable multiple of \((1+|\log U|)(1+|\log(1-U)|)\). Dominated convergence therefore yields

\[
\lim_{p\downarrow0}\varepsilon^2J(t)=\int_0^1\log u\,\log(1-u)\,du
=\sum_{n=1}^{\infty}\frac1{n(n+1)^2}
=2-\frac{\pi^2}{6}.
\]

The last equality follows by expanding the logarithm and partial fractions. On the other hand, \(\varepsilon^2\mu\to0\), while the explicit stagewise formula gives \(\varepsilon^2M_{\mathrm{step}}\to1\). Moreover \(\varepsilon^2\mu^2\to1\). Divide the variance formulas to obtain both long-walk ratios. The limiting constant is strictly positive since it is an integral of a positive function; it is strictly below one, as required by the strict antithetic improvement.

## Verification

Run `python3 verify.py` with standard Python 3. The file contains rational-arithmetic checks of the variance ordering and both phase boundaries at 64 rational stopping probabilities, independent joint-survival checks at 16 pairs of thresholds for each probability, exact rational quantile-partition checks for six representative probabilities, the entire worked example, and numerical sanity checks of the limit. The supplied \(`VERIFY_OUTPUT.txt`\) records successful execution with 1,296 checks. These finite verifications supplement, but do not substitute for, the analytic proof above.

## Relationship to prior work

Choromanski (2023) introduces graph random features and importance-corrected walk loads, motivating the resolvent entry estimator. Reid, Choromanski and Weller (2023) introduce stepwise antithetic termination and prove variance reductions for a *different*, bilinear two-regularized-Laplacian kernel objective. Reid, Markou, Choromanski, Turner and Weller (2024) explicitly introduce global optimal-transport coupling of geometric walk lengths and demonstrate improvements over stepwise antithetic termination. **That general method and the classical Fréchet countermonotone principle are not claimed new.** Their graph-kernel objective is a coupled bilinear feature product and is optimized approximately over quantile permutations, while here the object is the single-particle unsquared Green diagonal of a two-vertex edge. The contribution is the exact unrestricted all-probability benchmark, the two distinct sharp probability thresholds, and the explicit small-stopping asymptotic discrepancy between global and stagewise couplings. Neither source statement directly supplies these particular formulas; an equivalent calculation hidden in earlier specialized work remains possible.

The difference is scientifically material: the original bilinear graph-kernel objective should not be identified with the present one-walk Green diagonal, nor should the classical optimal-coupling theorem alone be mistaken for proof of the exact stagewise comparison and its asymptotics.

## Limitations

The graph has only one undirected edge and deterministic traversal directions. The calculation concerns a *linear* Green-resolvent entry estimator from two walkers, not the squared kernel or diagonal inner product of the general graph-random-feature scheme. It does not show that inverse-CDF antithetic lengths are globally optimal for arbitrary graphs, directions, modulation functions, more walkers or nonlinear feature-pair costs. All methods have the same expected number of traversals, but no wall-clock or overhead superiority is asserted. The inverse-CDF method uses a globally shared uniform variable, whereas stepwise antithetic termination uses fresh paired uniforms at each possible move. Exact unrestricted optimum does not imply uniqueness of the optimizer.

## References

1. K. Choromanski, *Taming graph kernels with random features*, arXiv:2305.00156, first posted April 29, 2023. https://arxiv.org/abs/2305.00156
2. I. Reid, K. Choromanski and A. Weller, *Quasi-Monte Carlo Graph Random Features*, arXiv:2305.12470, first posted May 21, 2023, especially Sections 3 and 8.5–8.6. https://arxiv.org/html/2305.12470v1
3. I. Reid, S. Markou, K. Choromanski, R. E. Turner and A. Weller, *Variance-Reducing Couplings for Random Features*, arXiv:2405.16541, first posted May 26, 2024, especially Section 4 and Appendices C and E. https://arxiv.org/html/2405.16541v2
4. Classical Fréchet–Hoeffding intersection bounds and countermonotone inverse-CDF coupling, used as standard probability facts rather than claimed original findings.
