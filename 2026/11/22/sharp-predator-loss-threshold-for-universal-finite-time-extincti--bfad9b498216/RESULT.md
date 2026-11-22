# Sharp predator-loss threshold for universal finite-time extinction below an Allee threshold

## Finding

Consider susceptible prey \(s\) and predator \(p\) on the infection-free invariant face of an Allee–fear–aggregation system. Let \(K>L>0\), \(b,d,e,\mu>0\), \(k\geq 0\), and \(0<r<1\). For every \(0<s_0<L\), \(p_0>0\), solve, while \(s>0\),
\[
\dot s=-\frac{b s(1-s/K)(L-s)}{1+kp}-d s^r p,
\qquad \dot p=(e s^r-\mu)p.
\]
Write \(T_*=\inf\{t\geq0:s(t)=0\}\), with \(T_*=\infty\) when no finite zero occurs, and define \(\beta=(1-r)bL\).

**Sharp global classification:** For every admissible \((s_0,p_0)\), \(T_*<\infty\) if \(\mu\leq\beta\), including equality. If \(\mu>\beta\), then for every fixed \(s_0\in(0,L)\) there is an \(\varepsilon(s_0)>0\) such that all \(0<p_0<\varepsilon(s_0)\) give \(T_*=\infty\), whereas every \(p_0>\mu s_0^{1-r}/[(1-r)d]\) gives \(T_*<\infty\). Every infinite-lifetime orbit still has \(s(t),p(t)\to0\) as \(t\to\infty\).

Thus \(\mu=\beta\) exactly separates universal finite-time prey extinction from coexistence of finite-time and merely asymptotic extinction outcomes at the same model parameters.

## Assumptions and scope

The equations are the \(I=0\) invariant reduction of the susceptible–infected–predator model in Reference 1, with \(b=b_0\), \(d=d_0\), \(e=d_2\), \(\mu=a_2\), \(k=k_1\). Initial prey is strictly below the positive strong-Allee threshold; the carrying capacity is greater than that threshold. No positive lower bound on the predator density is imposed. The vector field is smooth on \(s>0,p>0\) and solutions there are unique. At the first hit, \(s=0\) is taken as an absorbing state, so finite-time extinction means that first hit, not subsequent biological recovery. Infection-free initial conditions remain infection-free; the theorem does not cover initially infected prey.

## Proof

**1. Transformation, monotonicity and bounds.** Define \(q=s^{1-r}\), \(c=(1-r)d\), and
\[
a(s,p)=(1-r)b\frac{(1-s/K)(L-s)}{1+kp}.
\]
On \(0<s\leq s_0<L\), \(q'=-a(s,p)q-cp\) and \(p'=(e s^r-\mu)p\). In particular, \(s\) decreases strictly and \(0<a(s,p)\leq\beta\). The positive weighted biomass \(H=s+(d/e)p\) satisfies
\[
H'=-\frac{b s(1-s/K)(L-s)}{1+kp}-\frac{d\mu}{e}p\leq0.
\]
Hence \(p(t)\leq p_0+(e/d)s_0=:P_{\max}\) before any prey hit; neither population can blow up in finite time. While \(s>0\), the Allee term gives the uniform bound
\[
\frac{\dot s}{s}\leq-\kappa,\qquad
\kappa=\frac{b(1-s_0/K)(L-s_0)}{1+kP_{\max}}>0.
\]
Thus any globally positive orbit has \(s(t)\leq s_0e^{-\kappa t}\), so \(s,s^r\in L^1(0,\infty)\). Also \(p\) is bounded and, from its exact equation,
\[
p(t)=p_0\exp\Bigl[-\mu t+e\int_0^t s(u)^r\,du\Bigr]
=C_p e^{-\mu t}(1+o(1)),\quad C_p>0.
\]
Because \(a(s,p)=\beta+O(s+p)\) as \((s,p)\to(0,0)\), the same globally positive orbit satisfies \(A(t)=\int_0^t a(s(u),p(u))\,du=\beta t+C_A+o(1)\) for some finite \(C_A\).

**2. All positive predator introductions give finite-time extinction at or below threshold.** Integrating the exact linear equation for \(q\) yields
\[
q(t)e^{A(t)}=q_0-c\int_0^t p(u)e^{A(u)}\,du,
\qquad q_0=s_0^{1-r}>0.
\]
If a solution remained prey-positive for all time, then by Step 1 the integrand would be asymptotic to \(C_p e^{C_A}e^{(\beta-\mu)t}\). For \(\mu\leq\beta\), its integral diverges, including linearly at equality, contradicting the nonnegativity of the left-hand side. Therefore the unique pre-hit solution must reach \(q=s=0\) in finite time.

**3. A strictly positive prey trajectory for small predator introductions above threshold.** If \(\mu>\beta\), choose \(\delta\in(0,L)\) so small that \(\lambda=\mu-e\delta^r>\beta\). Whenever \(0<s_0\leq\delta\), we have \(p(t)\leq p_0e^{-\lambda t}\) and, since \(a\leq\beta\),
\[
q(t)\geq e^{-\beta t}\left(q_0-\frac{cp_0}{\lambda-\beta}\right)>0
\quad\text{if}\quad 0<p_0<\frac{q_0(\lambda-\beta)}c.
\]
This estimate is self-consistent on every finite interval, so it excludes a finite prey hit. For any prescribed \(s_0\in(0,L)\), the predator-free solution has \(s(t)\downarrow0\) and reaches \(s(T)<\delta\) at some finite \(T\). Continuous dependence on \(p_0\) near zero up to that \(T\) guarantees \(s(T)<\delta\), \(s(T)>0\), and a sufficiently small \(p(T)>0\) satisfying the displayed invariant no-hit inequality. This supplies \(\varepsilon(s_0)>0\). Step 1 ensures that prey and predator both eventually approach zero, despite never reaching zero at finite time.

**4. Finite-time extinction also occurs for large predator introductions above threshold.** For every positive pre-hit trajectory, \(p'(t)\geq-\mu p(t)\) and hence \(p(t)\geq p_0e^{-\mu t}\). Because \(q'(t)\leq-cp(t)\),
\[
q(t)\leq q_0-\frac{cp_0}{\mu}(1-e^{-\mu t}).
\]
When \(p_0>\mu q_0/c\), the right side reaches zero at the finite time
\[
T_{\rm upper}=-\mu^{-1}\log\left(1-\frac{\mu q_0}{cp_0}\right).
\]
Continuity implies \(T_*\leq T_{\rm upper}<\infty\). This proves every assertion.

## Verification

The standalone `verify.py` uses rational arithmetic to check a strict positive no-hit wedge, a strict finite-hit inequality, and the exact critical rate for the following parameter family:
\[
b=2,\ L=1,\ K=4,\ r=1/2,\ k=1/5,\ d=1,\ e=1/10,\ s_0=1/4.
\]
Here \(\beta=1\), \(q_0=c=1/2\). For \(\mu=3/2\), \(\lambda=29/20>1\), and \(p_0=1/10<9/20\), the global rigorous lower bound is \(q(t)\geq(7/18)e^{-t}\); hence extinction is only asymptotic. Conversely \(p_0=2>3/2\) forces \(T_*\leq0.924196241\ldots\). For \(\mu=1/2\) or \(\mu=1\), every positive predator introduction causes finite-time extinction by the theorem. A standard-library RK4 check illustrates the four regimes; no finite numerical trajectory is used as proof of the infinite-time statement.

Reproduce with `python3 verify.py` using only Python's standard library.

## Relationship to prior work

Reference 1 specifies this exact family within its infection-free invariant manifold and proves finite-time extinction under an assumed uniform positive lower bound on predator density (Theorem 6.2). That hypothesis cannot hold for globally prey-positive trajectories here, since the predator approaches zero. The new result instead proves a complete mortality-threshold dichotomy for **endogenous** predator dynamics, including equality and both outcome types above threshold. References 2 and 3 analyze related SIP formulations and finite-time prey loss, but do not supply the stated universal/initial-condition separation. References 4 and 5 study nonsmooth herd predation and finite-time extinction with different prey-growth and predator-response terms. Their general separatrix and finite-loss phenomena are acknowledged as prior ideas; the exact threshold \(\mu=(1-r)bL\) for this strong-Allee infection-free subsystem is the specific contribution assessed here. The literature comparison is bounded; priority outside inspected material remains a risk.

## Limitations

The proof is mathematical for a deterministic infection-free reduction only. It uses \(0<r<1\), \(0<s_0<L<K\), positive fixed parameters and an absorbing extinction boundary. It does not classify all initial predator-density thresholds when \(\mu>\beta\), nor infer effects for positive infected-prey initial conditions, stochastic extinction, measured ecological populations, or treatment policies. Numerical paths neither certify infinite-time trajectories nor establish historical uniqueness. Independent validation has not been performed.

## References

1. K. Antwi-Fordjour and E. M. Takyi, *Aggregation as a Double-Edged Sword: Fear, Allee Effects, and Finite-Time Collapse* (2026), arXiv:2606.17586v1, §§2 and 6, https://arxiv.org/abs/2606.17586. First public posting June 16, 2026.
2. K. Antwi-Fordjour, Z. Overton and D. Lee, *Dynamics of Diseased-Impacted Prey Populations: Defense and Allee Effect Mechanisms* (2025), arXiv:2505.01952, https://arxiv.org/abs/2505.01952.
3. K. Antwi-Fordjour, S. P. Westmoreland and K. H. Bearden, *Dual Fear Phenomenon in an Eco-Epidemiological Model with Prey Aggregation* (2023/2024), arXiv:2308.06772, https://arxiv.org/abs/2308.06772.
4. K. Antwi-Fordjour, R. D. Parshad, H. E. Thompson and S. B. Westaway, *Fear-driven extinction and (de)stabilization in a predator-prey model incorporating prey herd behavior and mutual interference* (2022/2023), AIMS Mathematics 8 (2023), 3353–3377, DOI:10.3934/math.2023173, https://www.aimspress.com/article/doi/10.3934/math.2023173.
5. K. Vilches-Ponce, E. González-Olivares and A. Rojas-Palma, *Prey herd behavior modeled by a generic non-differentiable functional response* (2018), Mathematical Modelling of Natural Phenomena 13, 26, DOI:10.1051/mmnp/2018038.
