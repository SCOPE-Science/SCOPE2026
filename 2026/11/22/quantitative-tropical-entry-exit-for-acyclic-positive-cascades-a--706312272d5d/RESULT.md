# Quantitative tropical entry–exit for acyclic positive cascades and a Gaussian crossing law

## Finding
For a finite directed acyclic graph with arbitrary time-dependent scalar growth rates, strictly positive fast or slow linear feeds, and exponentially scaled initial concentrations, the finite-parameter logarithmic solution converges to its max-plus path value with a **uniform bound** \(O(\varepsilon\log(1/\varepsilon))\) on every time interval separated from the initial instant. The bound holds for every finite acyclic graph and is optimal over this class, not just for constant Jordan chains. An explicit two-species crossing exhibits a non-Jordan \(\frac12\varepsilon\log(1/\varepsilon)\) correction, an exact second-order exit-time expansion, and a Gaussian concentration of the times at which the outgoing population was supplied.

Here and below \(\varepsilon\downarrow0\). For an explicit example satisfying the assumptions, write
\[
\varepsilon x'=(t-3)x,\qquad \varepsilon y'=(2t-4)y+x,\qquad x(0)=1,\ y(0)=e^{-10/\varepsilon}.
\]
Let \(t_\varepsilon>2\) be the unique **upward** crossing of \(x(t)+y(t)=1\). Then, with \(t_*=2+\sqrt{7/2}\) and \(\ell_*=2\sqrt{7/2}\),
\[
t_\varepsilon=t_*+\frac{\varepsilon}{2\ell_*}\log\frac{\varepsilon}{2\pi}+o(\varepsilon).
\]
At \(t=t_*\), the logarithmic discrepancy between the exact downstream abundance and its max-plus value is \(\frac12\varepsilon\log(1/\varepsilon)+O(\varepsilon)\). The normalized distribution of feed times, defined precisely below, converges in total variation after centering at \(1\) and dividing by \(\sqrt\varepsilon\), to the standard Gaussian law.

## Assumptions and scope
Fix \(n\in\mathbb N\), \(T>0\), and a finite directed acyclic graph \(G\) with vertices \(1,\ldots,n\). Topologically order the vertices so every edge \(j\to i\) has \(j<i\). For each vertex take a continuous real-valued rate \(\lambda_i:[0,T]\to\mathbb R\). For each edge take a continuous strictly positive coefficient \(c_{ij}:[0,T]\to(0,\infty)\) and an exponent \(r_{ij}\in\{0,1\}\), respectively a fast or slow feed. Choose any finite real entry exponents \(a_i\). For \(0<\varepsilon<1\), consider the unique solution of
\[
\varepsilon z_i'=\lambda_i(t)z_i+\sum_{j\to i}\varepsilon^{r_{ij}}c_{ij}(t)z_j,
\qquad z_i(0)=\exp(a_i/\varepsilon).
\]
All coordinates remain strictly positive. No ordering among the rates, eigenvalue separation, or genericity of their crossings is assumed.

A directed path \(P=(i_0,\ldots,i_k=i)\) may have \(k=0\). For each ordered \(0\le s_1\le\cdots\le s_k\le t\), set \(s_0=0\), \(s_{k+1}=t\), and
\[
F_{P,t}(s_1,\ldots,s_k)=a_{i_0}+\sum_{h=0}^k\int_{s_h}^{s_{h+1}}\lambda_{i_h}(u)\,du.
\]
The max-plus path value is
\[
\psi_i(t)=\max_{P:\,i_k=i}\ \max_{0\le s_1\le\cdots\le s_k\le t}F_{P,t}(s_1,\ldots,s_k),
\]
including the length-zero path, whose value is \(a_i+\int_0^t\lambda_i\). In particular the graph may be disconnected and every \(a_i\) is finite. The statement is uniform on \([\theta,T]\) for each fixed \(\theta\in(0,T]\); it **does not** assert uniform agreement at \(t=0\). An instantaneous feed changes the tropical boundary value, while the differential solution initially retains its specified entry values.

## Proof
**Exact finite path expansion.** Variation of constants, iterated in the topological order, is a finite sum over directed paths ending at \(i\). The contribution of a path with \(k\ge1\) edges is exactly
\[
Z_{P,\varepsilon}(t)=\varepsilon^{-k+\sum_{h=1}^k r_{i_hi_{h-1}}}
\int_{0\le s_1\le\cdots\le s_k\le t}
\left(\prod_{h=1}^k c_{i_hi_{h-1}}(s_h)\right)
\exp(F_{P,t}(s)/\varepsilon)\,ds.
\]
For \(k=0\), its contribution is \(\exp(F_{P,t}/\varepsilon)\). This identity follows directly by applying the integrating factor for each scalar vertex and substituting each upstream solution. Because the graph is acyclic, paths cannot repeat a vertex, so the number of path terms is finite and all coefficients are nonnegative. Consequently no cancellation can invalidate a logarithmic maximum estimate.

**Uniform quantitative Laplace bounds.** Put \(M_P(t)=\max_{s\in\Delta_k(t)}F_{P,t}(s)\), where \(\Delta_k(t)\) is the ordered-time simplex. On the fixed finite data, all \(F_{P,t}\) are uniformly Lipschitz in their time coordinates: changing one transition time alters two integrals, with modulus bounded by twice the maximum of \(|\lambda_i|\). The product of feed coefficients lies between positive constants depending on the path. For \(0<\varepsilon<\min(\theta,1/2)\), the simplex volume and \(r_{ij}\ge0\) give
\[
Z_{P,\varepsilon}(t)\le C_P\varepsilon^{-k}\exp(M_P(t)/\varepsilon)
\qquad (\theta\le t\le T).
\]
Choose a maximizer \(s^*\in\Delta_k(t)\). The homothetic simplex
\[
(1-\varepsilon/t)s^*+(\varepsilon/t)\Delta_k(t)
\]
has volume \(\varepsilon^k/k!\), stays inside \(\Delta_k(t)\), and lies within coordinate distance \(\varepsilon\) of \(s^*\). On it, \(F_{P,t}\ge M_P(t)-C'_P\varepsilon\). Since each slow feed contributes no inverse power and each fast feed contributes \(\varepsilon^{-1}\), their common prefactor is at least \(1\). Thus
\[
Z_{P,\varepsilon}(t)\ge c_P\varepsilon^k\exp(M_P(t)/\varepsilon-C'_P).
\]
The case \(k=0\) is exact. Taking \(\varepsilon\log\) shows \(|\varepsilon\log Z_{P,\varepsilon}(t)-M_P(t)|\le C_{P,\theta}\varepsilon\log(1/\varepsilon)\), uniformly for \(t\in[\theta,T]\). Finally, \(z_i\) is a sum of a fixed finite number of positive path terms, so the elementary log-sum-exp bound proves
\[
\boxed{\ \sup_{\theta\le t\le T}\max_{1\le i\le n}
\left|\varepsilon\log z_i(t)-\psi_i(t)\right|
\le C_{\theta}\varepsilon\log(1/\varepsilon).\ }
\]
All constants depend on the fixed graph, rates, coefficients, entries, \(T\), and \(\theta\), never on \(\varepsilon\). Maximizing the path formula recursively is exactly the scalar linear specialization of the acyclic feed max-plus recursion. This provides a finite-size quantitative version rather than merely a limiting Laplace principle.

**Exact two-species crossing and sharpness.** For the displayed example define \(A_x(t)=t^2/2-3t\), \(A_y(t)=t^2-4t\). Integration gives
\[
x(t)=e^{A_x(t)/\varepsilon},\qquad
 y(t)=e^{A_y(t)/\varepsilon}\left[e^{-10/\varepsilon}+\frac1\varepsilon\int_0^t
 e^{(s-s^2/2)/\varepsilon}\,ds\right].
\]
The phase of the feed integral is \(s-s^2/2=1/2-(s-1)^2/2\). Its unique nondegenerate maximum on \([0,t]\), whenever \(t>1\), lies at \(s=1\). The ordinary Gaussian integral therefore yields, uniformly for \(t\) in a fixed neighbourhood of \(t_*>1\),
\[
y(t)=\sqrt{\frac{2\pi}{\varepsilon}}\exp\left(\frac{A_y(t)+1/2}{\varepsilon}\right)(1+o(1)).
\]
At \(t=t_*\), \(A_y(t_*)+1/2=0\), while the tropical value \(\psi_y(t_*)=0\); hence \(\varepsilon\log y(t_*)=\frac12\varepsilon\log(1/\varepsilon)+O(\varepsilon)\). This proves that the logarithmic order in the general theorem cannot be reduced to \(O(\varepsilon)\), even for two vertices with simple crossing diagonal rates, and not just for a constant Jordan matrix.

Since \((x+y)'=((t-2)x+(2t-4)y)/\varepsilon\), the total concentration decreases for \(0<t<2\) and increases for \(t>2\). For all sufficiently small \(\varepsilon\), it is below \(1\) at \(t=2\); hence there is one upward return \(t_\varepsilon>2\). The tropical first positive return occurs when \(A_y(t)+1/2=0\), at \(t_*\). Standard Gaussian bounds and strict monotonicity show \(t_\varepsilon\to t_*\). As \(A_x(t_*)<0\), \(x(t_\varepsilon)\) is exponentially small, and solving \(y(t_\varepsilon)=1+o(1)\) with \(A_y'(t_*)=\ell_*>0\) gives
\[
t_\varepsilon=t_*+\frac{\varepsilon}{\ell_*}\left(\tfrac12\log\varepsilon-\tfrac12\log(2\pi)\right)+o(\varepsilon),
\]
including its second-order constant. The Taylor remainder is \(O(\varepsilon\log^2\varepsilon)=o(1)\) after division by \(\varepsilon\), so this inversion is justified.

**Feed-time law.** Conditional on the downstream concentration at the return being supplied by the integral term, its normalized input-time measure is
\[
d\nu_\varepsilon(s)=\frac{\exp(-(s-1)^2/(2\varepsilon))\,\mathbf1_{[0,t_\varepsilon]}(s)\,ds}{\int_0^{t_\varepsilon}\exp(-(u-1)^2/(2\varepsilon))\,du}.
\]
The exponentially tiny initial downstream contribution does not affect its limiting share. Under \(s\mapsto(s-1)/\sqrt\varepsilon\), this measure is exactly standard normal distribution conditioned to the interval \([-1/\sqrt\varepsilon,(t_\varepsilon-1)/\sqrt\varepsilon]\). Both endpoints tend to infinite opposite limits. Its total variation distance from standard normal equals the omitted Gaussian tail probability and tends to zero. This is a statement about the linear feed integral, not a stochastic assertion about individual chemical reactions.

## Verification
Run `python3 checker.py` using only the Python standard library. It evaluates 1,944 exact two-vertex constant-rate parameter instances (both fast and slow feeds), checks the max-plus approximation on three positive observation times, and evaluates five crossing return times from the exact error-function formula. The checker also computes the exactly omitted Gaussian mass for the feed-time law. The log-error bound for arbitrary graphs and the limiting Gaussian statement are proved analytically above; finite examples are checks, not replacements for those proofs.

## Relationship to prior work
Borsotti, *The entry-exit function and nilpotent corrections in multidimensional slow-fast systems* (arXiv:2610.15670v1, first publicly posted 2026-10-11), derives logarithmic exit shifts caused by constant nilpotent Jordan blocks and a lexicographic selection among separately evolving spectral families. This established work already demonstrates that spectral balance alone cannot determine finite-parameter exit shifts. Its stated structural class consists of constant Jordan nilpotent pieces and their block-diagonal sums; it does not supply the present finite-graph max-plus path formula, an explicit uniform bound for positive time-dependent *off-diagonal* acyclic feeds with arbitrary exponentially scaled initial entries, or the normalized interior-transfer-time law. The new estimate and example are not proposed as new instances of the elementary Laplace method, which is the main proof tool.

Kaklamanos, Kuehn, Popović and Sensi, *Entry–Exit Functions in Fast–Slow Systems with Intersecting Eigenvalues* (first published online 2023), establish leading-order exit selection for two-dimensional eigendirection intersections; their Section 3.1 treats one-way coupling. In contrast, the present result permits arbitrary finite acyclic topologies and continuously time-dependent diagonal rates without ordering assumptions, gives a finite-parameter graph-wide logarithmic error bound, and resolves an explicit interior-time Gaussian prefactor including the constant in the first-return location. The precise example here is not their system and does not claim their qualitative eigenbranch analysis as new.

The max-plus leading path action and the first-order Laplace principle are standard. The potential contribution is their finite-parameter, graph-wide synthesis under positive feed, with a sharp small-parameter correction and a natural feed-time occupation law. Searches of semiring, positive-linear-system, and entry-exit literature did not reveal a theorem implying this exact combined statement; no absolute priority claim is made.

## Limitations
Only finite acyclic graphs, linear positive feeds, scalar vertices, bounded positive feed coefficients, finite exponential entry rates, and fixed positive observation times are covered. No conclusion for cyclic feeding, nonlinear hyperedges, matrix-valued irreducible blocks, or coupled slow-variable back-reaction is claimed. Initial boundary layers preclude uniform log convergence at \(t=0\) in general. The Gaussian law belongs to the displayed crossing model, not every acyclic cascade. The second-order coefficient is tied to the exact normalization of its return level and feed coefficients. Historical coverage by more general path-integral Laplace estimates remains a specific priority risk, despite inspection of the directly relevant published entry–exit proofs. No independent validation has been performed.

## References
- J. Borsotti, *The entry-exit function and nilpotent corrections in multidimensional slow-fast systems*, arXiv:2610.15670v1 (first posted October 11, 2026), https://arxiv.org/abs/2610.15670.
- P. Kaklamanos, C. Kuehn, N. Popović and M. Sensi, *Entry–Exit Functions in Fast–Slow Systems with Intersecting Eigenvalues*, Journal of Dynamics and Differential Equations 37 (2025), 559–576; first online June 3, 2023, https://doi.org/10.1007/s10884-023-10266-2.
- T.-H. Hsu and S. Ruan, *Relaxation Oscillations and the Entry-Exit Function in Multidimensional Slow-Fast Systems*, SIAM Journal on Mathematical Analysis, doi:10.1137/19M1295507, https://epubs.siam.org/doi/10.1137/19M1295507.
- S. L. Campbell and N. J. Rose, *Singular Perturbation of Autonomous Linear Systems*, SIAM Journal on Mathematical Analysis 10 (1979), 542–551, https://doi.org/10.1137/0510051.
