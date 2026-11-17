# Sharp invariant-disc threshold and optimal network synchronization for holomorphic hyperbolic-tangent flows

## Finding

**Theorem (sharp invariant-disc and nonlinear spectral-gap law).** Let \(G\) be any finite connected undirected graph on \(N\ge2\) vertices, with symmetric nonnegative edge weights and combinatorial Laplacian \(L\). Write \(\lambda_2>0\) for the smallest positive eigenvalue of \(L\). Let \(\alpha,\beta,\kappa>0\), \(0<R<1\), and consider the complex holomorphic network
\[
 \dot z_i=-\alpha z_i+\beta\tanh z_i-\kappa(Lz)_i,\qquad i=1,\ldots,N.
\]
Put \(c_R=\tan R/R\) and \(\delta=\alpha-\beta c_R\). The closed product disc \(\mathcal K_R=\{z\in\mathbb C^N:|z_i|\le R\}\) is forward invariant **if and only if** \(\delta\ge0\). All trajectories starting in \(\mathcal K_R\) converge to the zero vector **if and only if** \(\delta>0\), with the conjunction interpreted as forward invariance and convergence within that set. At \(\delta=0\), the two nonzero synchronized configurations \(z_i=\pm iR\) are equilibria.

For \(\delta>0\), define \(P=I-\mathbf1\mathbf1^\top/N\), \(w=Pz\), and \(\rho=\alpha-\beta+\kappa\lambda_2\). Then every initial condition in \(\mathcal K_R\) satisfies, for every \(t\ge0\),
\[
 \max_i|z_i(t)|\le R e^{-\delta t},
 \qquad
 \|w(t)\|_2\le
 \exp\!\left[\frac{\beta\tan^2 R}{2\delta}(1-e^{-2\delta t})\right]e^{-\rho t}\|w(0)\|_2.
\]
The spectral-gap exponent \(\rho\) is **optimal**: for every connected graph and all parameters in this regime, some arbitrarily small initial configurations have \(\liminf_{t\to\infty}e^{\rho t}\|w(t)\|_2>0\). Hence no uniform-in-initial-data estimate with any strictly larger exponential rate is possible.

On the unit disc, use the Kobayashi infinitesimal normalization \(F_K(z,v)=|v|/(1-|z|^2)\) and the resulting distance \(d_K\). Define the root-mean-square pairwise distance \(Q_K(t)=\big[N^{-1}(N-1)^{-1}\sum_{i\ne j}d_K(z_i(t),z_j(t))^2\big]^{1/2}\). The same optimal exponential rate has an all-time intrinsic-distance bound
\[
 Q_K(t)\le\frac{\exp\!\big(\beta\tan^2R/(2\delta)\big)}{1-R^2}\,e^{-\rho t}Q_K(0).
\]

## Assumptions and scope

The graph is undirected, finite, connected, and may carry arbitrary nonnegative symmetric edge weights. The complex arguments remain inside \(|z|\le R<1\), where \(\tanh\) is analytic. The result is deterministic and concerns the exact nonlinear finite-dimensional network, not merely its linearization. All claims quantify over **every** initial configuration in the stated closed polydisc. Rates are expressed in the original continuous-time units. The positive coupling gain \(\kappa\) is not normalized by vertex degree. The theorem does not claim that the product disc is forward invariant when \(\delta<0\).

## Proof

**1. Exact boundary constant.** For \(|\zeta|\le u<\pi/2\), write \(\zeta=x+iy\). The identity \(|\cosh\zeta|^2=\sinh^2x+\cos^2y\ge\cos^2u\) gives \(|\operatorname{sech}^2\zeta|\le\sec^2u\). Integrating \(\tanh z=z\int_0^1\operatorname{sech}^2(sz)\,ds\) along the radial segment yields
\[
 |\tanh z|\le |z|\int_0^1\sec^2(sR)\,ds=c_R|z|\quad(|z|\le R).
\]
Thus \(\operatorname{Re}(\overline z\tanh z)\le c_R|z|^2\), with equality at \(z=iR\), since \(\tanh(iR)=i\tan R\). This also proves \(\operatorname{Re}\operatorname{sech}^2\zeta\le1+|\tanh\zeta|^2\le1+c_R^2|\zeta|^2\), using \(\operatorname{sech}^2\zeta=1-\tanh^2\zeta\).

**2. Sharp forward invariance and decay.** At any vertex \(i\) attaining the current largest modulus \(M=\max_j|z_j|>0\),
\[
 \operatorname{Re}\left(\overline z_i[-\kappa(Lz)_i]\right)
 =\kappa\sum_j a_{ij}\operatorname{Re}\left(\overline z_i z_j-|z_i|^2\right)\le0.
\]
The first step therefore implies the upper Dini differential inequality \(D^+M\le-\delta M\) whenever \(M\le R\). When \(\delta\ge0\), the standard first-exit argument establishes invariance. When \(\delta>0\), comparison gives \(M(t)\le R e^{-\delta t}\), proving convergence to zero. If \(\delta<0\), initialize every vertex at \(iR\): the Laplacian vanishes, while \(\dot z_i=iR(-\alpha+\beta c_R)\) points strictly outward, disproving invariance. If \(\delta=0\), \(z_i=iR\) and \(z_i=-iR\) are nonzero equilibria, disproving attraction to zero. These are exact endpoint witnesses, not perturbative arguments.

**3. All-time graph-sharp disagreement inequality.** Set \(\bar z=N^{-1}\sum_jz_j\), so \(w_i=z_i-\bar z\). Since \(\sum_iw_i=0\), \(PL=L\), and \(\langle w,Lw\rangle\ge\lambda_2\|w\|_2^2\),
\[
 \tfrac12\tfrac d{dt}\|w\|_2^2
 =\sum_i\operatorname{Re}\{\overline{w_i}[f(z_i)-f(\bar z)]\}-\kappa\langle w,Lw\rangle,
 \qquad f(z)=-\alpha z+\beta\tanh z.
\]
For each \(i\), the entire segment from \(\bar z\) to \(z_i\) has modulus at most \(M(t)\), and
\[
 f(z_i)-f(\bar z)=w_i\int_0^1f'(\bar z+s w_i)\,ds,
 \qquad
 \operatorname{Re}f'(\zeta)\le-\alpha+\beta+\beta c_R^2M(t)^2.
\]
Consequently, with \(\rho=\alpha-\beta+\kappa\lambda_2\),
\[
 \tfrac12\tfrac d{dt}\|w\|_2^2\le[-\rho+\beta c_R^2R^2e^{-2\delta t}]\|w\|_2^2.
\]
Integration, \(c_R^2R^2=\tan^2R\), and a square root give the stated all-time estimate, including its explicit prefactor. It applies as written when \(w=0\), in which case synchrony persists exactly.

**4. No faster uniform rate.** Let \(v\in\mathbb R^N\) be a unit Fiedler eigenvector, \(Lv=\lambda_2v\) and \(\sum v_i=0\). Initialize \(z(0)=\varepsilon v\) with real \(\varepsilon>0\) sufficiently small. Write \(f(z)=-(\alpha-\beta)z+n(z)\), where \(n(z)=\beta(\tanh z-z)\) and \(|n'(\zeta)|=\beta|\tanh\zeta|^2\le\beta c_R^2|\zeta|^2\). Because \(P n(\bar z\mathbf1)=0\), the same segment estimate gives \(\|P n(z(t))\|_2\le\beta c_R^2M(t)^2\|w(t)\|_2\). The quantity \(b(t)=e^{\rho t}\langle v,w(t)\rangle\) thus satisfies
\[
 |b'(t)|\le e^{\rho t}\beta c_R^2 M(t)^2\|w(t)\|_2
 \le C_R\beta c_R^2\varepsilon^3e^{-2\delta t},
 \qquad C_R=e^{\beta\tan^2R/(2\delta)},
\]
where \(M(0)\le\varepsilon\) and Step 3 was used. Therefore \(b(t)\) converges, with \(|b(\infty)-\varepsilon|\le C_R\beta c_R^2\varepsilon^3/(2\delta)\). For sufficiently small \(\varepsilon\), its limit is nonzero. Cauchy–Schwarz now implies \(\liminf_{t\to\infty}e^{\rho t}\|w(t)\|_2\ge |b(\infty)|>0\). This establishes the optimality assertion for every graph, not just the six-cycle.

**5. Intrinsic distances.** The Kobayashi length of a straight segment inside \(|z|\le R\) is bounded above by Euclidean segment length divided by \(1-R^2\); every Kobayashi curve has length at least its Euclidean length. Hence \(|z_i-z_j|\le d_K(z_i,z_j)\le|z_i-z_j|/(1-R^2)\). The identity \(\sum_{i\ne j}|z_i-z_j|^2=2N\|Pz\|_2^2\) compares \(Q_K\) to \(\sqrt{2/(N-1)}\|w\|_2\). Applying the two bounds at times \(0,t\) yields the displayed intrinsic estimate. The sequence from Step 4 also proves sharpness of its exponent, since all involved distances are uniformly comparable and approach the Euclidean metric near zero.

## Verification

A standalone Python 3 checker in `check.py` evaluates the exact radial boundary identity, the exact extremal derivative on the imaginary axis, and a 10,000-step fourth-order integration of the six-cycle example described below. It compares actual Euclidean disagreement against the **global** theorem bound at five finite times. Run `python3 check.py` with only the standard library. Finite checks corroborate constants and sign conventions but are not a proof of the universally quantified theorem.

For the six-cycle used in the motivating article, \((\alpha,\beta,\kappa,R)=(1,0.35,1.2,0.7)\), one has \(\lambda_2=1\), \(\delta=0.578855809768\ldots\), the **optimal** nonlinear disagreement rate \(\rho=1.85\), and uniform Euclidean prefactor \(C_R=1.239218848211\ldots\). The earlier node-wise uniform contraction guarantee was approximately \(0.402\); the observed transverse rate was near \(1.85\). The present global inequality proves the sharp rate for all initial states in the certified polydisc, rather than inferring it from a local linearization or finite simulations.

## Relationship to prior work

Sarkar (arXiv:2608.07551v1, Sections 6 and 9) proves an invariant-polydisc criterion, verifies a particular radius numerically, and presents an empirical transverse synchronization rate consistent with \(\alpha-\beta+\kappa\lambda_2\). In Section 9.4 this rate is **already predicted by linearization**, which is explicitly credited here. What is established here beyond that prediction is: the necessary-and-sufficient invariant-disc threshold at every radius \(0<R<1\), a full nonlinear all-initial-data estimate at the exact asymptotically sharp exponent and with an explicit uniform transient factor, and the sharp endpoint obstruction. Generic graph-coupling and synchronization principles are classical and are not claimed as new.

Yang–Meng–Shi–Hong–Johansson (arXiv:1401.6541) establish exponential synchronization for Lipschitz nonlinear agents under network conditions. Their general Lipschitz-rate criterion does not supply the exact model-specific invariant-disc threshold or the all-time bound at the **equilibrium** spectral rate with this explicit transient constant. Al-Radhawi–Angeli–Sontag (arXiv:2307.13678) develop contraction theory for biological interaction networks in nonstandard norms; they do not identify the displayed complex hyperbolic-tangent network or these sharp constants. These are implication comparisons, not priority certificates; related general exponential-dichotomy methods may yield other derivations.

## Limitations

The theorem does not assert that every trajectory has exactly the rate \(\rho\); fully synchronized trajectories have zero disagreement, and exceptional trajectories may decay faster. Sharpness means **some arbitrarily small initial states** asymptotically realize the rate, so no larger *uniform* exponent is valid. Only connected undirected graphs, the specified holomorphic nonlinearity, positive parameters, and \(0<R<1\) are covered. The radius threshold concerns the specified closed polydisc, not arbitrary invariant domains. The result is not an independent audit or an assertion of historical uniqueness; broader classical stabilization theory may subsume parts of the method.

## References

1. S. Sarkar, *Contraction Analysis of Holomorphic Dynamical Systems via the Intrinsic Kobayashi Metric*, arXiv:2608.07551v1 (public 2026-08-01), https://arxiv.org/html/2608.07551, Sections 6, 9, 10.
2. T. Yang, Z. Meng, G. Shi, Y. Hong, and K. H. Johansson, *Network Synchronization with Nonlinear Dynamics and Switching Interactions*, arXiv:1401.6541 (2014), https://arxiv.org/abs/1401.6541.
3. M. A. Al-Radhawi, D. Angeli, and E. D. Sontag, *On Structural Contraction of Biological Interaction Networks*, arXiv:2307.13678 (2023; revised later), https://arxiv.org/abs/2307.13678.
