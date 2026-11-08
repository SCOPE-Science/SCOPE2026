# Universal critical decay and a spectral collision coefficient for a product-hazard SIS network

## Finding

**Theorem (sharp critical relaxation).** Let \(G\) be a finite, connected, undirected simple graph on \(n\geq2\) vertices, with symmetric adjacency matrix \(A\), spectral radius \(\rho>0\), and positive Perron vector \(v\) normalized by \(\sum_i v_i^2=1\). Choose \(0<\delta<1\) and \(\beta=\delta/\rho\). Starting from any \(x(0)\in[0,1]^n\setminus\{0\}\), iterate the product-hazard, independent-neighbor SIS map

\[
 x_i(t+1)=1-\bigl(1-(1-\delta)x_i(t)\bigr)
             \prod_{j:A_{ij}=1}\bigl(1-\beta x_j(t)\bigr).
\]

For every vertex \(i\), the infection coordinate tends to zero with the **exact, initial-condition-independent** asymptotic law

\[
\boxed{\lim_{t\to\infty}t\,x_i(t)=\frac{v_i}{K}},\qquad
 K=\delta\left[1-\frac{\delta}{2}\left(1+\frac1\rho\right)\right]
\sum_j v_j^3>0.
\]

In particular, the threshold itself is globally extinguishing but *not* exponentially so. If \(G\) is connected and \(d\)-regular, then each coordinate has the same sharp limit
\[
\lim_{t\to\infty}t\,x_i(t)
=\frac{1}{\delta\left[1-\frac{\delta}{2}\left(1+\frac1d\right)\right]}.
\]

This full critical law is different from the continuous-time or Euler-discretized NIMFA law: for the latter homogeneous system with matching linearization, the critical quadratic Perron coefficient is \(K_{\mathrm{NIMFA}}=\delta\sum_jv_j^3\), whereas the product-hazard system has
\[
\frac{K}{K_{\mathrm{NIMFA}}}
=1-\frac{\delta}{2}\left(1+\frac1\rho\right)\in(0,1).
\]

## Assumptions and scope

The graph is fixed and finite, connected, undirected and without loops; \(A_{ij}\in\{0,1\}\). Both the infection parameter \(\beta\) and the recovery parameter \(\delta\) are probabilities. The recurrence above is a deterministic approximation to infection probabilities under an independence-of-neighbors assumption, **not** the finite-state stochastic SIS Markov chain. The critical equality \(\beta\rho=\delta\) is exact. The hypothesis \(0<\delta<1\) guarantees a positive diagonal in the linearization and excludes a special periodic boundary case at \(\delta=1\). No assertion is made for directed, disconnected or heterogeneous networks. For \(x(0)=0\), the orbit is identically zero and the stated positive constant is inapplicable.

## Proof

**1. Comparison and strict positivity.** Set \(u_i(x)=1-\prod_{j:A_{ij}=1}(1-\beta x_j)\) and \(L=(1-\delta)I+\beta A\). Then the map \(F\) can be rewritten exactly as
\[
F_i(x)=(1-\delta)x_i+\bigl[1-(1-\delta)x_i\bigr]u_i(x)=(Lx)_i-H_i(x),
\]
where
\[
H_i(x)=\beta(Ax)_i-u_i(x)+(1-\delta)x_i u_i(x)\geq0.
\]
The inequality follows from \(u_i(x)\leq\beta(Ax)_i\), the finite union bound. Moreover, \(F_i(x)\geq(1-\delta)x_i\), while for every neighbor \(j\) of \(i\), \(F_i(x)\geq\delta\beta x_j\). Thus every nonzero orbit becomes strictly positive at all vertices after at most the graph diameter steps, and remains so. The map preserves \([0,1]^n\).

**2. Global extinction, including equality.** Because \(Av=\rho v\) and \(\beta\rho=\delta\), \(Lv=v\). Let \(a_t=v^{\mathsf T}x(t)>0\). Symmetry gives
\[
a_{t+1}=a_t-v^{\mathsf T}H(x(t))\leq a_t.
\]
Suppose the decreasing sequence had limit \(a_\infty>0\). At every time there would be a vertex with infection at least \(a_\infty/\sum_jv_j\). Following a path from that vertex to any other, repeatedly applying the two lower bounds on \(F\), and using the positive persistence factor \(1-\delta\) on idle steps, yields a uniform strictly positive lower bound for **all** coordinates after a fixed number of steps (no larger than the graph diameter). Since every vertex has at least one neighbor, the formula for \(H_i\) then gives \(H_i(x(t))\geq(1-\delta)x_i(t)u_i(x(t))\geq(1-\delta)\beta\epsilon^2\) for a time-uniform \(\epsilon>0\). This forces \(a_t\) to decrease by a fixed amount at every subsequent step, a contradiction. Hence \(a_t\to0\) and, as \(v>0\), \(x(t)\to0\) componentwise.

**3. Alignment with the Perron vector.** The symmetric nonnegative matrix \(L\) is primitive: the graph is connected and \(1-\delta>0\). Its Perron eigenvalue \(1\) is simple, and the norm of its restriction to \(v^\perp\) is a number \(\theta<1\) (all its other real eigenvalues have modulus less than one). Write \(x(t)=a_tv+z_t\) with \(v^{\mathsf T}z_t=0\). Since \(v_i>0\) and \(x(t)\geq0\), \(\lVert x(t)\rVert\leq C a_t\). The exact formula for \(H\) has no constant or linear term, so \(\lVert H(x(t))\rVert\leq C' a_t^2\) for all sufficiently late times. Consequently,
\[
\frac{a_{t+1}}{a_t}=1+O(a_t),\qquad
 z_{t+1}=Lz_t-(I-vv^{\mathsf T})H(x(t)).
\]
The ratios \(z_t/a_t\) are bounded and satisfy
\[
\left\lVert\frac{z_{t+1}}{a_{t+1}}\right\rVert
\leq\frac{\theta\lVert z_t/a_t\rVert+C'a_t}{1-C'a_t}.
\]
Because \(a_t\to0\) and \(\theta<1\), taking the upper limit proves \(z_t/a_t\to0\). Therefore \(x(t)/a_t\to v\).

**4. Nonlinear collision coefficient.** The Taylor expansion of the exact product map at the disease-free state is
\[
H_i(x)=(1-\delta)\beta x_i(Ax)_i
+\beta^2\!\sum_{\substack{j<k\\ A_{ij}=A_{ik}=1}}x_jx_k
+O(\lVert x\rVert^3).
\]
Put \(S_3=\sum_i v_i^3\). The Perron equation gives \((Av)_i=\rho v_i\) and, by symmetry of \(A\),
\[
\sum_i v_i\sum_{j:A_{ij}=1}v_j^2
=\sum_j v_j^2(Av)_j=\rho S_3.
\]
Hence
\[
\begin{aligned}
v^{\mathsf T}H_2(v)
&=(1-\delta)\beta\rho S_3
+\frac{\beta^2}{2}(\rho^2-\rho)S_3\\
&=\delta\left[1-\frac\delta2\left(1+\frac1\rho\right)\right]S_3=K,
\end{aligned}
\]
where \(H_2\) is the quadratic homogeneous part of \(H\). Since \(\rho\geq1\) and \(0<\delta<1\), \(K>0\).

**5. Exact rate.** Steps 3–4 yield \(v^{\mathsf T}H(x(t))=Ka_t^2+o(a_t^2)\), so
\[
a_{t+1}=a_t-Ka_t^2+o(a_t^2),\qquad
\frac1{a_{t+1}}-\frac1{a_t}\longrightarrow K.
\]
Summation and Cesàro averaging imply \(t a_t\to 1/K\). Combining this with \(x(t)/a_t\to v\) proves the limit in the statement. For a \(d\)-regular graph, \(\rho=d\), \(v_i=n^{-1/2}\), and \(S_3=n^{-1/2}\), which yields the stated vertex-wise constant. Finally, the usual continuous-time homogeneous NIMFA vector field \(\dot x=-\delta x+\beta(1-x)\odot(Ax)\) (and its unit-step Euler version) has quadratic Perron projection \(\beta\rho S_3=\delta S_3\), establishing the model comparison.

## Verification

Run the included, self-contained standard-library program with `python3 checker.py`. It enumerates all connected labelled simple graphs of sizes \(2\) through \(5\), using four interior recovery probabilities, and compares the spectral formula to both the graphwise quadratic expansion and the small-amplitude nonlinear map. It then tests five representative topologies with non-Perron-aligned starting profiles through \(10^5\) iterations. This calculation checks algebra and approximations; it **does not** constitute an exhaustive proof for arbitrary network sizes. The universal theorem rests on the five-step analytic proof above.

## Relationship to prior work

Chakrabarti, Wang, Wang, Leskovec and Faloutsos (2008), *Epidemic Thresholds in Real Networks*, introduced the same product-hazard nonlinear recursion and derived the spectral threshold and exponential extinction in the strictly subcritical region. The 2026 paper by Dung and Phuc, *An Epidemic Threshold Set for Networks*, uses the same recurrence, elaborates local/community thresholds, and motivates precise critical behavior on arbitrary connected networks. Neither of those papers' examined results yields the **critical equality-case, global sharp \(t^{-1}\) constant** here. Prasse and Van Mieghem (2019, 2020) study the related Euler-discrete or continuous-time NIMFA equations; their quadratic update is different because it omits multiple-neighbor product collisions. The ratio of quadratic Perron coefficients above makes that distinction explicit, rather than assuming the equations are interchangeable. Classical one-dimensional parabolic asymptotics motivate the proof strategy but alone do not determine the network-dependent coefficient or prove global alignment for this model.

## Limitations

This is a deterministic independent-neighbor probability approximation, not a theorem on the actual finite-population Markov-chain extinction time or its quasi-stationary distribution. The parameter \(\delta=1\) and graph heterogeneity, directed graphs and disconnected graphs are outside the theorem. The asymptotic is for fixed finite graph and arbitrarily large time: it is not a uniform finite-size or large-network limit. No assertion is made that general spectral center-manifold methods are new; the claim is the explicit nonlinear-network constant, its universal global basin, and the product-hazard versus additive-model comparison. Mathematical novelty is subject to possible earlier unindexed treatments of the same recursion and equality regime.

## References

1. Hoang Phi Dung and Nguyen Hong Phuc, *An Epidemic Threshold Set for Networks*, first posted 15 July 2026, https://arxiv.org/abs/2607.14048 (model equation (2) and community thresholds).
2. Deepayan Chakrabarti, Yang Wang, Chenxi Wang, Jurij Leskovec and Christos Faloutsos, *Epidemic Thresholds in Real Networks*, ACM Transactions on Information and System Security 10(4), 2008, https://doi.org/10.1145/1284680.1284681 ; author-hosted text https://www.cs.cmu.edu/~jure/pubs/virus-tissec.pdf (product recursion Eq. (7), strict subcritical Theorems 3–4, Appendix A).
3. Bastian Prasse and Piet Van Mieghem, *The Viral State Dynamics of the Discrete-Time NIMFA Epidemic Model*, 2019, https://arxiv.org/abs/1903.08027 (additive Euler-discretized equation (2)).
4. Bastian Prasse and Piet Van Mieghem, *Time-dependent solution of the NIMFA equations around the epidemic threshold*, Journal of Mathematical Biology 81 (2020), https://doi.org/10.1007/s00285-020-01542-6 (continuous-time NIMFA around threshold).
5. Clara Granell, *Probabilistic Discrete-Time Models for Spreading Processes in Complex Networks: A Review*, Annalen der Physik (2024), https://doi.org/10.1002/andp.202400078 (distinguishes discrete-time spreading closures).
