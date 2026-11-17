# Global predator exclusion and a universal critical recovery law in a double-Allee map

## Finding

For the discrete Holling-II predator–prey map introduced in [1], predator invasion has an exact global exclusion boundary. Within the forward-invariant region of prey density at most carrying capacity, predators disappear on **every** orbit when \(\beta\le(1+\alpha)\theta\), and the prey converges to one of its three predator-free equilibria. At equality, all orbits recovering to carrying capacity exhibit explicit, universal inverse-time relaxation:

\[
\lim_{n\to\infty} n(1-x_n)=\frac{1+\alpha}{\theta},\qquad
\lim_{n\to\infty}n y_n=\frac{(1-s)(1+\alpha)^2}{(1+w)\theta}.
\]

The first coefficient is independent of both Allee parameters. The recovery regime is attained on a nonempty open set of strictly positive initial states. The boundary is sharp for positive coexistence: immediately above it, an explicit positive coexistence equilibrium exists.

## Assumptions and scope

Fix \(0<s<1\), \(w>0\), \(\alpha>0\), \(\theta>0\), and \(\beta>0\). Given \(0<x_0\le1\) and \(y_0>0\), define for every integer \(n\ge0\)

\[
\begin{aligned}
x_{n+1}&=x_n\exp\!\left[\frac{(x_n-s)(1-x_n)}{x_n+w}-\frac{y_n}{1+\alpha x_n}\right],\\
y_{n+1}&=y_n\exp\!\left[\frac{\beta x_n}{1+\alpha x_n}-\theta\right].
\end{aligned}
\]

These are precisely the nondimensional semi-discrete population equations (3) in [1], restricted to the biologically significant strong-Allee and subcapacity initial region. All parameters and time indices in this theorem are fixed; the limits are taken along the entire orbit, not a subsequence.

Define \(\beta_c=(1+\alpha)\theta\). Then:

1. For \(\beta<\beta_c\), \(0<y_n\le y_0\exp[-(\theta-\beta/(1+\alpha))n]\), and \(x_n\) converges to one of \(0,s,1\).
2. For \(\beta=\beta_c\), \(y_n\) decreases to zero, \(x_n\) converges to one of \(0,s,1\), and every orbit with \(x_n\to1\) satisfies both limits in the Finding.
3. Such critical recovering orbits occur for all initial states in a nonempty open rectangle \(x_0\in(t,1)\), \(0<y_0<\eta\), with some \(s<t<1\) and \(\eta>0\).
4. For each sufficiently small \(\delta>0\), setting \(\beta=\beta_c+\delta\) gives the strictly positive equilibrium
\[
 x_* =\frac{\theta}{\theta+\delta},\qquad
 y_*=(1+\alpha x_*)\frac{(x_*-s)(1-x_*)}{x_*+w}.
\]
Consequently, no strictly positive periodic orbit or compact strictly positive invariant limit set can exist at or below \(\beta_c\). No claim is made that the nearby coexistence equilibrium is attracting.

## Proof

**1. The strip and increasing prey skeleton.** Write \(G(x)=(x-s)(1-x)/(x+w)\), \(g(x)=x\exp G(x)\). For \(0<x<1\), \(G(x)<1-x\) because \((x-s)/(x+w)<1\). Hence \(0<x_{n+1}\le g(x_n)<x_n\exp(1-x_n)<1\). If \(x_n=1\), the strictly positive predator forces \(x_{n+1}<1\). Positivity of both coordinates is preserved.

Direct differentiation gives
\[
 G'(x)=-1+\frac{(s+w)(1+w)}{(x+w)^2},\qquad
 1+xG'(x)=1-x+\frac{x(s+w)(1+w)}{(x+w)^2}>0
\]
for \(0<x\le1\). Thus \(g\) is strictly increasing on \([0,1]\), with fixed points exactly \(0,s,1\). The prey update \(f_y(x)=x\exp[G(x)-y/(1+\alpha x)]\) is also strictly increasing in \(x\), since \(\partial_x\log f_y=1/x+G'(x)+\alpha y/(1+\alpha x)^2>0\).

**2. Predator extinction, including equality.** Since \(x_n\le1\),
\[
 \log\frac{y_{n+1}}{y_n}
 \le\frac{\beta}{1+\alpha}-\theta.
\]
This proves exponential decay below the boundary. At the boundary the exact identity is
\[
\log\frac{y_{n+1}}{y_n}=-\frac{\theta(1-x_n)}{1+\alpha x_n}\le0.
\]
If the decreasing positive sequence had limit \(L>0\), summing this identity would force \(\sum_n(1-x_n)<\infty\), hence \(x_n\to1\). But then \(\log(x_{n+1}/x_n)=G(x_n)-y_n/(1+\alpha x_n)\to-L/(1+\alpha)<0\), contradicting \(x_n\to1\). Therefore \(y_n\to0\) also at equality.

**3. Complete prey-limit classification.** Uniformly for \(x\in[0,1]\), \(f_{y_n}(x)-g(x)\to0\), because \(y_n\to0\). Put \(l=\liminf x_n\) and \(L=\limsup x_n\). Monotonicity and continuity of \(g\) yield \(l=g(l)\) and \(L=g(L)\); each therefore belongs to \(\{0,s,1\}\). If any \(x_n\le s\), the prey update is strictly smaller than \(x_n\), and it remains below \(s\), so \(x_n\downarrow0\). Otherwise \(x_n>s\) forever and \(l\ge s\). If \(L=s\), convergence follows. If \(L>s\), fix \(t\in(s,L)\). Because \(g(t)>t\), for all sufficiently large \(n\), \(f_{y_n}(t)>t\). Since \(f_{y_n}\) is increasing and \(x_n>t\) infinitely often, eventually \(x_n>t\) holds forever. Thus \(l\ge t\). Letting \(t\uparrow L\) gives \(l=L\). The only remaining possible limits are \(s\) and \(1\).

**4. Exact critical amplitudes.** Suppose now \(\beta=\beta_c\) and \(x_n\to1\). Set \(u_n=1-x_n\), \(v_n=y_n\), and define
\[
a=\frac{1-s}{1+w}\in(0,1),\quad \rho=1-a,\quad
 b=\frac1{1+\alpha},\quad k=\frac{\theta}{1+\alpha}.
\]
Taylor expansion of the exact map at \((u,v)=(0,0)\) gives, uniformly as \((u,v)\to(0,0)\) in the nonnegative quadrant,
\[
 u_{n+1}=\rho u_n+bv_n+O((u_n+v_n)^2),\qquad
 \frac{v_{n+1}}{v_n}=\exp[-k u_n+O(u_n^2)].
\]
To justify division by \(v_n\), fix \(\rho<\rho'<1\) and \(b'>b\). For sufficiently large \(n\), positivity, the differentiability of the first update, and \(u_n,v_n\to0\) imply \(u_{n+1}\le\rho' u_n+b'v_n\). Also \(v_{n+1}\ge e^{-K\varepsilon}v_n\) whenever \(u_n\le\varepsilon\), for a fixed \(K>0\). Choose \(\varepsilon>0\) so \(\rho'e^{K\varepsilon}<1\). Hence \(u_n/v_n\) is bounded by a contracting affine recurrence. With this bound the quadratic remainder, divided by \(v_n\), is \(o(1)\), giving
\[
\frac{u_{n+1}}{v_{n+1}}=\rho\frac{u_n}{v_n}+b+o(1),
\quad\text{so}\quad
\frac{u_n}{v_n}\longrightarrow h:=\frac{b}{1-\rho}=\frac1{a(1+\alpha)}.
\]
The exact predator update then yields
\[
\frac1{v_{n+1}}-\frac1{v_n}
=\frac{\exp[ku_n+O(u_n^2)]-1}{v_n}
\longrightarrow kh>0.
\]
Cesàro averaging shows \((n v_n)^{-1}\to kh\), and multiplying by the ratio limit gives
\[
 n v_n\to \frac1{kh}=\frac{a(1+\alpha)^2}{\theta},
\quad
 n u_n\to\frac1k=\frac{1+\alpha}{\theta}.
\]
In particular, these rates are forced on every recovering orbit; numerical evidence is not used to infer the limits.

**5. Open recovery set and sharpness.** Choose any \(t\in(s,1)\). Then \(g(t)>t\), so there exists \(\eta>0\) such that \(f_\eta(t)>t\). At the critical boundary \(y_n\) decreases; therefore all orbits with \(t<x_0<1\), \(0<y_0<\eta\) stay above \(t\). Their prey limit cannot be \(0\) or \(s\), so it is \(1\). Finally, if \(\beta=\beta_c+\delta\) with sufficiently small \(\delta>0\), the displayed \((x_*,y_*)\) lies in \((s,1)\times(0,\infty)\) and makes both exponents vanish. This proves the boundary is sharp for the possibility of positive coexistence.

## Verification

The standalone Python 3 file `verify.py` checks 36 exact-rational differentiation and amplitude identities, six near-boundary positive equilibria, and three forward trajectories of 250,000 steps each at the critical boundary. The trajectory tests compare their rescaled outputs against the analytic limits within a relative tolerance of \(0.003\). Run it with `python3 verify.py` in the extracted directory. All these finite computations are diagnostics only; the proof above establishes the statements for all parameters and qualifying infinite trajectories.

## Relationship to prior work

Patra and Maitra [1], section 3, classify the boundary equilibrium locally and derive the positive equilibrium, while section 4 proves conditions for a Neimark–Sacker bifurcation and section 5 discusses numerical population collapse. These results supply the model and its local invasion condition; they do not assert global exclusion, the three-way prey-limit classification, the nonempty recovery wedge, or the exact critical inverse-time amplitudes. The 2026 journal version [2] shares this focus according to its accessible abstract, but its full subscription text could not be compared.

Xia and Li [3] study a different semi-discrete double-Allee map, with a polynomial prey-predation term and a different predator-response exponent. Their transcritical analysis does not imply the displayed amplitude coefficients for the Holling-II map. Standard center-manifold considerations anticipate inverse-time rates near a simple neutral direction, but do not by themselves prove global attraction to the boundary or eliminate nonstationary recurrent states. Published work on critical extinction for other predator–prey models is not treated as a uniqueness claim for this map.

## Limitations

The theorem is restricted to \(0<x_0\le1\) and \(0<s<1\), and does not classify above-capacity initial prey or the dynamics for arbitrary \(\beta>\beta_c\). The critical formulas apply only to those orbits with \(x_n\to1\); other critical initial states may tend to the Allee threshold or total extinction. The nearby coexistence equilibrium is asserted to exist, not to be stable. Priority against inaccessible journal full text and uncatalogued equivalent results has not been independently established.

## References

[1] R. R. Patra and S. Maitra, *Double Allee effect induced extinction and bifurcation in a discrete predator-prey model*, arXiv:2403.13316v1, publicly submitted 20 March 2024. https://arxiv.org/html/2403.13316v1

[2] R. R. Patra, S. Maitra and S. Sarkar, *Double Allee Effect-Induced Extinction and Bifurcation in a Discrete-Time Predator-Prey Model*, Journal of Applied Nonlinear Dynamics 15(3) (2026), 589–614. https://doi.org/10.5890/JAND.2026.09.006 (abstract accessible; full journal text subscription-restricted).

[3] S. Xia and X. Li, *Complicate dynamics of a discrete predator-prey model with double Allee effect*, Mathematical Modelling and Control 2(4) (2022), 282–295. https://doi.org/10.3934/mmc.2022027
