# A half-order allocation transition for inverse Laplacian spectral moments on cyclic prisms

## Finding
For every integer \(m\ge3\) and every fixed real \(p>0\), let \(G_m=C_m\square K_2\) be the simple circular ladder (cyclic prism) with \(2m\) rail edges and \(m\) rungs. Independently choose a nonnegative conductance on every edge, with total conductance exactly one, and minimize the inverse spectral moment
\[
\mathcal F_p(L)=\operatorname{tr}_{\mathbf1^\perp}(L^{-p})=\sum_{\lambda_j(L)>0}\lambda_j(L)^{-p}.
\]
A disconnected network has infinite cost. The unique global minimizer has a common rail conductance \(a_{m,p}>0\) and common rung conductance \(b_{m,p}>0\), without imposing symmetry beforehand. Put \(t_{m,p}=b_{m,p}/a_{m,p}\) and \(\mu_k=4\sin^2(\pi k/m)\). Then \(t_{m,p}\) is the **unique positive root** of
\[
\boxed{\sum_{k=1}^{m-1}\mu_k^{-p}=\sum_{k=0}^{m-1}\frac{4-\mu_k}{(\mu_k+2t)^{p+1}}},\qquad
\boxed{a_{m,p}=\frac{1}{m(2+t_{m,p})},\quad b_{m,p}=t_{m,p}a_{m,p}}.
\]
The following is a sharp phase transition in the **spectral order**, not in network topology or edge prices. Define
\[
I_p=\frac{4^{-p}\Gamma(\tfrac12-p)}{\sqrt\pi\,\Gamma(1-p)},\quad
C_p=\frac{2\zeta(2p)}{(4\pi^2)^p},\quad
D_p=\frac{2^{1/2-p}\Gamma(p+1/2)}{\sqrt\pi\,\Gamma(p+1)}.
\]
For \(0<p<1/2\), \(t_{m,p}\to t_p>0\), where \(t_p\) is the unique positive root of
\[
\boxed{I_p=\int_0^1\frac{4-4\sin^2(\pi x)}{[4\sin^2(\pi x)+2t_p]^{p+1}}\,dx}.
\]
At the critical order and above it,
\[
\boxed{t_{m,1/2}\sim\frac{2}{\log m}},\qquad
\boxed{t_{m,p}\sim\left(\frac{D_p}{C_p}\right)^{1/(p+1/2)}m^{-\frac{2(2p-1)}{2p+1}}\quad(p>1/2)}.
\]
Thus the rung share of the conductance budget, \(t_{m,p}/(2+t_{m,p})\), has a positive limit below order \(1/2\) but tends to zero at and above that order, with a logarithmic critical law and a continuously varying power beyond criticality. Moreover,
\[
\boxed{t_p\sim2(1-2p)\quad\text{as }p\uparrow1/2},\qquad
\boxed{t_p\longrightarrow2/3\quad\text{as }p\downarrow0}.
\]
The established first- and second-inverse-moment constants are recovered as \(t_{m,1}\sim18^{1/3}m^{-2/3}\) and \(t_{m,2}\sim540^{2/5}m^{-6/5}/2\). Those endpoints alone do not imply the continuous-order phase transition.

## Assumptions and scope
The vertex set is \(\{(i,\ell):i\in\mathbb Z/m\mathbb Z,\ell\in\{0,1\}\}\). The two rails connect successive cyclic indices at fixed layer, and the rungs connect the two layers at each index. Each of the \(3m\) individual undirected edge conductances is independently adjustable, including zero; total conductance expenditure is exactly \(1\), with identical unit prices. The objective uses ordinary, unnormalized weighted Laplacian eigenvalues on the mean-zero subspace. A disconnected allocation is assigned \(+\infty\), rather than taking the pseudoinverse trace over its multiple zero eigenvalues. Every limit \(m\to\infty\) fixes \(p\); the statements are not uniform in simultaneously diverging \(p\) and \(m\). The index \(p\) is a real spectral-loss parameter, with \(p=1\) and \(p=2\) proportional to standard first- and second-order coherence metrics under their respective stochastic models.

## Proof
**1. Unrestricted uniqueness and symmetry.** Restrict every connected weighted Laplacian to \(\mathbf1^\perp\), where it is positive definite. For \(f(x)=x^{-p}\), \(f'(x)=-px^{-p-1}\) is strictly increasing on \((0,\infty)\). In an eigenbasis of a positive matrix \(A\), the second differential of \(\operatorname{tr}f(A)\) in any nonzero symmetric direction \(H\) is a sum of \(|H_{ij}|^2\) multiplied by the strictly positive divided differences \([f'(\lambda_i)-f'(\lambda_j)]/(\lambda_i-\lambda_j)\), with the diagonal/repeated-eigenvalue value \(f''(\lambda_i)>0\). Hence \(\operatorname{tr}A^{-p}\) is strictly convex on positive-definite matrices. Distinct edge-weight vectors give distinct restricted Laplacians because their off-diagonal edge entries distinguish the original Laplacians; thus the objective is strictly convex over connected conductance vectors. The budget simplex is compact, a strictly positive feasible vector exists, and every sequence approaching a disconnected allocation has a positive Laplacian eigenvalue tending to zero, making the objective diverge. Therefore exactly one minimizer exists. Rotations of the cycle and interchange of the two rails preserve the problem and act transitively on each of the two edge classes. Uniqueness forces common rail and rung rates \(a,b\). Either class entirely absent would disconnect the network, so both rates are positive.

**2. Exact scalar equation.** The class budget is \(m(2a+b)=1\). Set \(t=b/a\). Fourier modes along the cycle and symmetric/antisymmetric layer modes give the nonzero Laplacian spectrum
\[
\{a\mu_k:1\le k<m\}\ \cup\ \{a(\mu_k+2t):0\le k<m\}.
\]
Consequently, writing \(S_p(m)=\sum_{k=1}^{m-1}\mu_k^{-p}\) and \(T_p(m,t)=\sum_{k=0}^{m-1}(\mu_k+2t)^{-p}\), the cost is exactly
\[
\Phi_{m,p}(t)=[m(2+t)]^p[S_p(m)+T_p(m,t)].
\]
Differentiate and divide by the positive factor \(p[m(2+t)]^p/(2+t)\). Stationarity becomes
\[
S_p+T_p=2(2+t)\sum_{k=0}^{m-1}(\mu_k+2t)^{-p-1},
\]
which rearranges to the boxed root equation because \(T_p=\sum(\mu_k+2t)(\mu_k+2t)^{-p-1}\). On the root equation's right-hand side, every coefficient \(4-\mu_k\) is nonnegative and the \(k=0\) coefficient is strictly positive. Thus the right-hand side decreases strictly from infinity to zero as \(t\) goes from zero to infinity; the left side is fixed and positive. There is exactly one positive root, and it is the unrestricted global minimizer already established.

**3. Uniform resolvent singularity.** Define \(R_{m,p}(t)=\sum_{k=0}^{m-1}(4-\mu_k)(\mu_k+2t)^{-p-1}\) and its continuous counterpart
\[
J_p(t)=\int_0^1\frac{4-4\sin^2(\pi x)}{[4\sin^2(\pi x)+2t]^{p+1}}\,dx.
\]
As \(t\downarrow0\), the two ends of the integral are the same periodic quadratic singularity. Rescale the local angle by \(\sqrt{2t}\) and use dominated convergence away from this singularity to obtain
\[
J_p(t)\sim D_p t^{-p-1/2},\quad D_p=\frac{2^{1/2-p}\Gamma(p+1/2)}{\sqrt\pi\,\Gamma(p+1)}.
\]
For \(p>0\), the summand as a function of cyclic angle is nonnegative, symmetric, and decreasing from the zero angle to the half-period. Its Riemann-sum error satisfies \(|R_{m,p}(t)/m-J_p(t)|\le O_p(m^{-1}t^{-p-1})\). Therefore, whenever \(t\downarrow0\) but \(m\sqrt t\to\infty\),
\[
R_{m,p}(t)\sim mD_p t^{-p-1/2}.
\]
These estimates also hold for \(p\) in a compact subinterval of \((0,\infty)\), which is used below near the critical order.

**4. Three order regimes.** For \(0<p<1/2\), the endpoint singularity of \(\mu(x)^{-p}\) is integrable. Riemann sums give \(S_p(m)/m\to I_p\), with the beta-integral expression displayed in the finding. The strictly decreasing continuous function \(J_p(t)\) ranges from infinity to zero, so its root \(J_p(t_p)=I_p\) exists uniquely. Evaluate the exact finite root equation at any two fixed positive values straddling \(t_p\), and pass to the limit in the Riemann sums; this brackets \(t_{m,p}\) and proves convergence to \(t_p\).

For \(p=1/2\), comparison of \(\sin(\pi k/m)\) with \(\pi k/m\) near the two ends and a harmonic-sum estimate show \(S_{1/2}(m)=(m/\pi)\log m+O(m)\). For \(p>1/2\), dominated convergence after scaling by \(m^{2p}\) gives \(S_p(m)\sim C_pm^{2p}\), where \(C_p=2\zeta(2p)/(4\pi^2)^p\). In either case, \(S_p(m)/m\to\infty\), so the exact decreasing root equation implies \(t_{m,p}\to0\).

It remains to justify replacing the root sum by the uniform integral asymptotic. The \(k=0\) term gives \(R_{m,p}(t)\ge4(2t)^{-p-1}\); at the root this implies \(t_{m,p}\ge\tfrac12[4/S_p(m)]^{1/(p+1)}\). Therefore, for \(p=1/2\), \(m\sqrt{t_{m,p}}\gtrsim m^{2/3}/(\log m)^{1/3}\to\infty\). For fixed \(p>1/2\), the corresponding bound is \(m\sqrt{t_{m,p}}\gtrsim m^{1/(p+1)}\to\infty\). Apply Step 3 to the root equation. At criticality, \((m/\pi)\log m\sim (2m/\pi)t^{-1}\), giving \(t_{m,1/2}\sim2/\log m\). Above criticality, \(C_pm^{2p}\sim mD_pt^{-p-1/2}\); solving yields the stated exponent and coefficient.

**5. Endpoint behavior of the subcritical limit.** The beta integral gives \(I_p\sim1/[\pi(1-2p)]\) as \(p\uparrow1/2\). Since \(J_p(t)\sim D_pt^{-p-1/2}\), with \(D_p\to2/\pi\), the unique root has \(t_p\to0\) and \(t_p\sim2(1-2p)\); the small exponent correction disappears because \((1/2-p)\log(1/2-p)\to0\). As \(p\downarrow0\), \(I_p\to1\), while the elementary integral evaluates to \(J_0(t)=(t+2)/\sqrt{t(t+2)}-1\). Its unique positive root at level one is \(t=2/3\), and root continuity proves \(t_p\to2/3\).

## Verification
The accompanying standalone `verify.py` uses NumPy and SciPy, and on a standard Python 3 installation completes \(1401\) asserted finite checks. It compares two-layer Laplacian matrix eigenvalues with the asserted Fourier spectrum, checks power-sum traces and scalar derivatives, verifies strict finite scalar optimality on numerous sizes and orders, compares hundreds of independent asymmetric positive-weight candidates, and checks representative subcritical, critical, supercritical, and near-critical asymptotic ratios. It independently checks the exact constants at \(p=1\) and \(p=2\). These checks illustrate and catch implementation errors; they are **not** used as a proof of the universal or limiting statements. Proofs are given in the preceding section.

## Relationship to prior work
Bamieh, Jovanović, Mitra and Patterson (arXiv:1112.4011v1, 2011) study Fourier-mode coherence and dimensional scaling for fixed local-feedback networks and periodic lattices, rather than allocating a conductance budget over the real spectral-order family. Patterson and Bamieh (arXiv:1310.2592v1, 2013) establish the first- and second-inverse-moment interpretations of network coherence but do not derive the stated order-varying optimal design. Ghosh, Boyd and Saberi (2008) establish inverse-trace conductance optimization and strict convexity; that is methodological coverage, not a derivation of the half-order transition.

Specialized publicly available results already cover the **fixed** inverse-first-moment optimum on cyclic prisms, including its \(m^{-2/3}\) rung-rate law, and the distinct determinant objective, which has a positive fixed-price limiting rung rate. The present theorem does not claim those endpoint facts as new; its new statement is the complete \(p\)-indexed trichotomy, the exact critical logarithmic law, the continuous post-critical exponent, and the limiting subcritical boundary amplitude. The previously known first- and second-moment formulae alone do not imply a transition at the fractional order \(1/2\). Public specialist matches identified in the references were compared at claim level and for relevant full-text results; an unindexed equivalent analysis remains a priority risk.

## Limitations
This is an exact theorem only for two-layer cyclic prisms with equal per-edge costs and an unrestricted fixed total conductance budget. The spectral family at noninteger \(p\) is a mathematical loss interpolation, not automatically the performance of any specifically asserted physical stochastic dynamics. Limits fix \(p\) as the cycle grows, and the near-critical \(p\uparrow1/2\) limit of the infinite-network subcritical solution is distinct from a joint \(p\)-versus-\(m\) crossover theorem. The finite optimum above zero is implicit, although uniquely solvable. Nonuniform edge prices, missing rungs, arbitrary graph families, and publication-priority uniqueness are not established. No independent mathematical audit is claimed.

## References
1. B. Bamieh, M. R. Jovanović, P. Mitra and S. Patterson, *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback*, arXiv:1112.4011v1, first publicly posted December 17, 2011, https://arxiv.org/abs/1112.4011 .
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1, first publicly posted October 9, 2013, https://arxiv.org/abs/1310.2592 .
3. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1):37–66 (2008), DOI 10.1137/050645452, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf .
4. *Mesoscopic rung allocation in resistance-optimal prism networks*, published mathematical research record, November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-mesoscopic-rung-allocation-in-resistance-optimal-prism-networks--58e191d42f66 .
5. *D-optimal cyclic ladders with a linear-price crossover*, published mathematical research record, November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-d-optimal-cyclic-ladders-with-a-linear-price-crossover--1c968d5ff6c5 .
