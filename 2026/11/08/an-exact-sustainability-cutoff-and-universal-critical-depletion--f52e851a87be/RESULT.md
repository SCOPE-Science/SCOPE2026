# An exact sustainability cutoff and universal critical depletion in a logistic-response resource game

## Finding

The logistic resource-response process has one and only one sustainability threshold. At the threshold, every trajectory with initially positive resources depletes at an exact universal reciprocal-time rate; above it, every such trajectory approaches the same sustainable state. The threshold, two critical asymptotic constants, and the first slope of the sustainable branch are explicit.

Set
\[
q=\frac{1-b}{d-b},\qquad
k_c=\frac{1}{c}\log\frac{d-1}{1-b},\qquad
\kappa=1+(d-b)k_cq(1-q).
\]
For \(k=k_c\), the universal physical-time limits are
\[
\lim_{t\to\infty}tR(t)=\kappa^{-1},\qquad
\lim_{t\to\infty}t\left[x(t)-(1-q)\right]=-\frac{k_cq(1-q)}{\kappa}.
\]
The positive equilibrium, when it exists, has onset law
\[
R_*(k)=\frac{(d-b)cq(1-q)}{\kappa}(k-k_c)+O((k-k_c)^2)
\quad(k\downarrow k_c).
\]

## Assumptions and scope

The fully specified deterministic system, in the original time unit with resource-growth coefficient \(T=1\) and carrying capacity \(K=1\), is
\[
\dot R=R[1-R-bx-d(1-x)],\qquad
\dot x=1-x-p_k(R),\quad
p_k(R)=\frac{1}{1+\exp[-k(R-c)]}.
\]
The normalized extraction rates satisfy \(0<b<1<d\) and \(b+d>2\); the response midpoint satisfies \(0<c<1\), and sensitivity \(k>0\). For every initial state \(0<R(0)\le1\), \(0\le x(0)\le1\), there is one global nonnegative solution. The rectangle \([0,1]^2\) is invariant, and resource positivity is preserved at every finite time.

The full classification is:

- For \(k<k_c\), \(R(t)\to0\) and \(x(t)\to1-p_k(0)\), with exponential resource decline.
- For \(k=k_c\), the same limiting equilibrium is approached, but the displayed universal reciprocal-time limits hold for **every** positive-resource initial state.
- For \(k>k_c\), there is exactly one positive-resource equilibrium \((x_*,R_*)\), determined by
\[
x_*=1-p_k(R_*),\qquad R_*=1-b-(d-b)p_k(R_*),
\]
and every positive-resource solution converges to it. The equilibrium is locally asymptotically stable and the onset formula above holds.

For the invariant depleted face \(R(0)=0\), the resource remains zero for every parameter value; the positive-resource qualifier is essential.

## Proof

**1. Positivity and boundary linearization.** At \(x=0\) the strategy derivative is \(1-p_k(R)>0\); at \(x=1\) it is \(-p_k(R)<0\). At \(R=1\), resource derivative is \(-bx-d(1-x)<0\). Since \(\dot R=R G(x,R)\), an initially positive resource remains positive. The unique depleted equilibrium is \((x_0,0)\) with \(x_0=1-p_k(0)\). Its two linear eigenvalues are \(-1\) and
\[
\lambda(k)=1-b-(d-b)p_k(0).
\]
Because \(p_k(0)=[1+e^{kc}]^{-1}\) decreases strictly with \(k\), \(\lambda(k)\) increases strictly. The hypothesis \(b+d>2\) is equivalent to \(q=(1-b)/(d-b)<1/2\), so there is exactly one positive solution \(k=k_c\) of \(p_{k_c}(0)=q\), giving the formula in the finding.

**2. Sustainable equilibria and local stability.** Define
\[
F_k(R)=1-b-(d-b)p_k(R)-R.
\]
Its derivative is \(F'_k(R)=-1-(d-b)p'_k(R)<0\), with \(F_k(1)<0\), and \(F_k(0)=\lambda(k)\). Consequently \(F_k\) has exactly one root \(R_*\in(0,1)\) if and only if \(k>k_c\), and no positive root otherwise. At that equilibrium the Jacobian in the order \((x,R)\) is
\[
J_* = \begin{pmatrix}-1&-p'_k(R_*)\\(d-b)R_*&-R_*\end{pmatrix}.
\]
Its trace is \(-1-R_*<0\) and determinant \(R_*[1+(d-b)p'_k(R_*)]>0\).

**3. Global attraction when \(k>k_c\).** Put \(u=x-x_*\) and \(\Delta p=p_k(R)-p_k(R_*)\). Define
\[
V(x,R)=\frac{d-b}{2}(x-x_*)^2+
\int_{R_*}^{R}\frac{p_k(s)-p_k(R_*)}{s}\,ds.
\]
Strict increase of \(p_k\) makes both terms nonnegative and makes \(V=0\) only at \((x_*,R_*)\). The integral tends to \(+\infty\) as \(R\downarrow0\), since \(p_k(0)<p_k(R_*)\). Along the system,
\[
\dot u=-u-\Delta p,\qquad
\dot R/R=(d-b)u-(R-R_*),
\]
and the mixed terms cancel exactly:
\[
\dot V=-(d-b)u^2-\Delta p\,(R-R_*)\le0.
\]
Equality is possible only at the equilibrium. Since the initial sublevel of \(V\) is compact inside \(\{R>0\}\cap[0,1]^2\), the Lyapunov/LaSalle argument proves global convergence for every positive-resource initial condition, without an assumption that the initial opinion is near equilibrium.

**4. Global depletion for \(k\le k_c\).** Set \(e=x-x_0\) and \(\Delta_0p=p_k(R)-p_k(0)\ge0\). Then \(\dot e=-e-\Delta_0p\) and
\[
e(t)\le e(0)e^{-t},\qquad
\dot R=R[\lambda(k)+(d-b)e-R].
\]
If \(\lambda(k)<0\), integration gives \(R(t)\le R(0)\exp[\lambda(k)t+(d-b)e(0)(1-e^{-t})]\), proving exponential depletion. If \(\lambda(k)=0\), write \(W=1/R\) and \(C=(d-b)e(0)\). The same inequality gives
\[
\frac{d}{dt}\bigl[W(t)e^{C(1-e^{-t})}\bigr]\ge e^{C(1-e^{-t})}.
\]
The right side is bounded below by a positive constant, so \(W(t)\to\infty\), hence \(R(t)\to0\). In either case the equation \(\dot e=-e-\Delta_0p\), with forcing tending to zero, implies \(e(t)\to0\).

**5. Exact critical profile.** Fix \(k=k_c\), so \(p_k(0)=q\) and \(x_0=1-q\). Let \(a=p'_k(0)=k_cq(1-q)>0\). Since \(R(t),e(t)\to0\),
\[
\frac{d}{dt}\log R=(d-b)e-R\to0.
\]
The variation-of-constants identity is
\[
e(t)=e^{-t}e(0)-\int_0^t e^{-(t-s)}[p_k(R(s))-p_k(0)]\,ds.
\]
As \(t\to\infty\), on every fixed retrospective window \(s=t-v\), the ratio \(R(t-v)/R(t)\to1\) because \((\log R)'\to0\). For all sufficiently late times its ratio is bounded by \(e^{\varepsilon v}\) for any fixed \(0<\varepsilon<1\). The logistic secant \([p_k(R)-p_k(0)]/R\) is bounded and tends to \(a\). Dominated convergence, with an exponentially negligible early-time integral, therefore gives
\[
\frac{e(t)}{R(t)}\longrightarrow -a.
\]
The initial exponential term is negligible because \(\log R(t)=o(t)\). Finally
\[
\frac{d}{dt}\frac1R=1-(d-b)\frac{e}{R}\longrightarrow
1+(d-b)a=\kappa.
\]
Integration and a Cesàro limit yield \(1/R(t)=\kappa t+o(t)\), hence the two universal limits in the finding. The coefficient \(\kappa\) is strictly positive.

**6. The branch slope.** Since \(F_{k_c}(0)=0\) and \(\partial_R F_{k_c}(0)=-\kappa\), the implicit-function theorem gives a smooth branch \(R_*(k)\) through the origin. As \(\partial_k p_k(0)=-c p_k(0)[1-p_k(0)]\), differentiation yields
\[
\left.\frac{dR_*}{dk}\right|_{k_c}
=\frac{(d-b)cq(1-q)}{\kappa}>0.
\]
The previously established uniqueness ensures that the positive part of this branch is the actual sustainable equilibrium.

## Verification

The included `verify.py` evaluates the exact threshold identities for \(b=7/10\), \(d=2\), \(c=1/2\) using symbolic arithmetic and numerically integrates the system on both sides of the threshold and at criticality from two distinct initial states. It prints `VERIFY_OK` on successful replay. These computations support the formulas; infinite-time convergence and global stability are proved above rather than inferred from finite simulations.

For this example,
\[
q=\frac3{13},\quad k_c=2\log\frac{10}{3}\approx2.407945609,\quad
\kappa=1+\frac6{13}\log\frac{10}{3}\approx1.555679756,
\]
with \(tR(t)\to0.6428058193\) and \(t[x(t)-10/13]\to-0.2747647544\).

## Relationship to prior work

Tu, Chen, Fan and Yang introduced the precise logistic-response strategy equation and coupled resource equation in arXiv:2401.11269, Equations (1), (8), and (14). Their Section 3.6 describes numerical low-/high-intensity outcomes and expressly notes difficulty in analytic stability analysis; the model and that qualitative contrast are prior work, not claimed here. The present claim gives the threshold as a function of all admissible extraction and response parameters in the normalized subclass, proves attraction for all positive-resource initial conditions, and supplies the equality-case asymptotic coefficient and branch slope.

Tu, Menegazzo, D'Odorico and Suweis (arXiv:2405.01271) studied a different Allee-effect resource growth law with replicator or step-type knowledge feedback. Its global phase behavior and analytic thresholds do not give the formulas for the no-Allee logistic strategy-response system here. General observations about tipping under increased response sensitivity do not evaluate this model-specific critical time profile. No exhaustive claim of publication uniqueness is made.

## Limitations

The theorem concerns the exact deterministic two-state system with resource-growth coefficient \(T=1\), unit normalized carrying capacity and strictly increasing logistic response. It does not cover other time normalizations without corresponding coefficient changes, stochastic finite populations, external shocks, alternative behavioral update rules, zero initial resource, Allee dynamics, or asymptotic coefficients beyond the leading critical terms. Numerical verification is not an independent proof; an external independent audit remains unperformed. Publication-priority uncertainty from unindexed equivalent results remains.

## References

1. Chengyi Tu, Renfei Chen, Ying Fan, Yongliang Yang, *Coevolution of Resource and Strategies in Common-Pool Resource Dilemmas: A Coupled Human-Environmental System Model*, arXiv:2401.11269v1 (first posted 2024-01-20), https://arxiv.org/abs/2401.11269. Equations (1), (8), (14), Section 3.6.
2. Chengyi Tu, Fabio Menegazzo, Paolo D'Odorico, Samir Suweis, *The role of the Allee effect in common-pool resource and its sustainability*, arXiv:2405.01271 (first posted 2024-05-02), https://arxiv.org/abs/2405.01271. Sections on knowledge-feedback and resource-growth law.
3. *Tipping points in coupled human–environment system models: a review*, Earth System Dynamics 15 (2024), https://esd.copernicus.org/articles/15/947/2024/. Background sensitivity-threshold discussion, not a theorem about the present equations.
