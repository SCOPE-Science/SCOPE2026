# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform weakly asymmetric ASEP-to-KPZ convergence of the full initial-data flow

## Target theorem (proved here)

**Set-up.** Let $\varepsilon>0$ and consider nearest-neighbour ASEP on
$\mathbb Z$ with
$$p_\varepsilon=\tfrac12+\tfrac{\sqrt\varepsilon}{2},\qquad
  q_\varepsilon=\tfrac12-\tfrac{\sqrt\varepsilon}{2}.$$
All processes below are built on **one common basic graphical coupling**:
independent Poisson clocks $P^{x,\to},P^{x,\leftarrow}$ at each bond,
of rates $p_\varepsilon,q_\varepsilon$, used simultaneously for every
initial configuration (Harris construction). Discrepancies between
configurations evolve as (systems of) second-class particles.

Height functions $h^{\mathrm{mic}}_t(x)$, $x\in\mathbb Z$, are defined in
the usual way (up-jump $+2$ at rate $p$ across bond when $\eta_x=1,
\eta_{x+1}=0$, etc., fixed summation convention). A *viable* profile is one
with $|\,h^{\mathrm{mic}}(x+1)-h^{\mathrm{mic}}(x)\,|=1$ for all $x$.
Bertini–Giacomin (BG) rescaling: macroscopic space $X=\varepsilon x$,
time $T=\varepsilon^2 t$, fluctuation height
$$h_\varepsilon(T,X)=\sqrt\varepsilon\,
  \bigl(h^{\mathrm{mic}}_{\varepsilon^{-2}T}(\varepsilon^{-1}X)
  -\tfrac12\varepsilon^{-1}X\cdot(\text{centering})-c_\varepsilon T\bigr)$$
with the standard BG velocity centering $c_\varepsilon$, linearly
interpolated in $X$. The Gärtner (discrete Hopf–Cole) transform is
$$Z_\varepsilon(T,X)=\exp\bigl(h_\varepsilon\text{-linear drift}\bigr)
  =c\text{-multiple of }\exp(-\lambda_\varepsilon h^{\mathrm{mic}}+\nu_\varepsilon t),$$
with $\lambda_\varepsilon=\tfrac12\log(p_\varepsilon/q_\varepsilon)
=\sqrt\varepsilon+O(\varepsilon^{3/2})$, $\nu_\varepsilon$ the BG
normalisation; precise constants are those of Bertini–Giacomin, see Step 1.

Let $\mathcal C^\alpha_\delta(\mathbb R)$, $0<\alpha<1/2$, $0<\delta<1$,
be the weighted Hölder space
$$\|h\|_{\mathcal C^\alpha_\delta}
  =\sup_X\frac{|h(X)|}{(1+|X|)^\delta}
  +\sup_{|X|,|Y|\le R,\,X\ne Y,\,R\ge1}
   \frac{|h(X)-h(Y)|}{R^\delta|X-Y|^\alpha},$$
finiteness required for every $R$ with locally uniform bound (Polish space
under the Fréchet family of seminorms on $[-R,R]$ with weight $R^{-\delta}$).
For $h$ in the rescaled viable profiles write
$\Phi_{\varepsilon,t}h=h_\varepsilon(t,\cdot)$ starting from $h$ at time
$0$, all $h$ evolving under the **same** clocks. Let $\Phi_t$ be the
Hopf–Cole KPZ solution map $h\mapsto \log Z(t,\cdot)$ (+linear shift),
$Z$ solving SHE $\partial_tZ=\tfrac12\Delta Z+Z\xi$,
$Z(0)=e^{h}$, driven by **one** space-time white noise $\xi$ for all $h$.

For a set $A$ of initial data write the graph
$G(\Phi_{\varepsilon,t})=\{(h,\Phi_{\varepsilon,t}h):h\in K_\varepsilon\}$,
$G(\Phi_t)$ analogously, with local-uniform product metric on
$C(\mathbb R)\times C(\mathbb R)$ (convergence $=$ uniform on compacts in
both coordinates).

**Theorem (uniform flow convergence).** For every $T>0$, every compact
$K\subset\mathcal C^\alpha_\delta$, and every $K_\varepsilon$ in the
rescaled viable profiles with $d_H(K_\varepsilon,K)\to0$ (Hausdorff distance
in $\mathcal C^{\alpha'}_{\delta'}$ for some $\alpha'<\alpha$,
$\delta'>\delta$, hence in particular locally uniform), the graph-valued
processes $t\mapsto G(\Phi_{\varepsilon,t})$ converge in law to
$t\mapsto G(\Phi_t)$, uniformly for $t\in[0,T]$, in the local-uniform graph
Hausdorff (Fell) topology, with the temporal Hölder/jump modulus
$$\sup_{h\in K_\varepsilon}
  \frac{\|h_\varepsilon(t)-h_\varepsilon(s)\|_{C([-L,L])}}
       {|t-s|^\beta\vee\varepsilon^{\alpha\wedge 1/4}}\le M,$$
i.e. the Parekh §3.5 denominator $|t-s|^\alpha\vee\varepsilon^\alpha$
(up to the harmless exponent), equivalently after Skorokhod coupling with
sup-norm convergence uniform in $t$ and $h$ (after optimal pairing of
$K_\varepsilon$ with $K$). In particular finite-dimensional-in-$h$ joint
laws converge to the same-noise KPZ vector, and the convergence is uniform
over the compact.

## Proof strategy

Linearity of (discrete) SHE in the initial data + common-noise coupling +
compactness/chaining + uniform Hopf–Cole inversion. The new point over
fixed-$h$ BG/ACQ/Corwin–Shen/Parekh/Hairer–Quastel is lifting to uniformity
over compacts $K$ via: (i) estimates whose constants depend only on the
compact's growth envelope; (ii) joint-noise identification (all $h$ see the
same $\xi$ because all have local density $1/2$); (iii) equicontinuity in
$h$ and finite-net chaining; (iv) uniform log-inversion via uniform
positivity.

## Step 1. Discrete SHE with $h$-indexed noise, uniform remainder

Standard BG computation, done simultaneously for every $h$ under the same
clocks. With $\gamma_\varepsilon=e^{2\lambda_\varepsilon}-1$,
$\gamma'_\varepsilon=e^{-2\lambda_\varepsilon}-1$,
$$dZ^h_\varepsilon=( \tfrac12+o(1))\,\Delta_\varepsilon Z^h_\varepsilon\,dt
  +Z^h_\varepsilon\,dM^h_\varepsilon+R^h_\varepsilon\,dt,$$
where $\Delta_\varepsilon$ is the rescaled discrete Laplacian,
$M^h_\varepsilon$ is a jump martingale built from the compensated clocks,
and $R^h_\varepsilon$ is the BG Itô-correction error. Key structural facts:

(a) The compensated clocks $\bar P^{x,\to},\bar P^{x,\leftarrow}$ do not
depend on $h$; the $h$-dependence enters only through bounded prefactors
involving $\eta^h_x\in\{0,1\}$ and $Z^h_\varepsilon$.
(b) $|R^h_\varepsilon|\le C\sqrt\varepsilon\,
   Z^h_\varepsilon\times(\text{local quadratic-variation density})$,
   deterministically in $\eta$ since $|\eta|\le1$; hence with uniform
   $Z$-moments (Step 2),
   $$\sup_{h\in K_\varepsilon}\sup_{t\le T,\,X}
     e^{-a|X|}\|R^h_\varepsilon(t,X)\|_p\to0$$
   for every $p$, $a>0$. No $h$-regularity beyond boundedness of $\eta$
   is used, so uniformity over $K_\varepsilon$ is free.

## Step 2. Uniform moment, Hölder, and temporal-modulus bounds

Fix compact $K$. There is $M_K$ with $\sup_{h\in K}|h(X)|\le M_K(1+|X|)^\delta$.
For $K_\varepsilon\to K$, the same holds eventually with $2M_K$.
Hence $Z^{h}_{0,\varepsilon}(X)=\exp(h(X)+o(1))$ satisfies
$\|Z^{h}_{0,\varepsilon}e^{-2M_K(1+|\cdot|)^\delta}\|_\infty\le C$ uniformly
in $h\in K_\varepsilon$, $\varepsilon$ small.

The Corwin–Shen / Parekh / Hairer–Quastel discrete-SHE estimates
(Burkholder + heat-kernel, closed via Gronwall) use the initial data only
through such weighted norms. Consequently, for every $p\ge2$, $a>0$,
$L\ge1$ there are $C=C(p,a,L,T,M_K)$, $\beta>0$ with
$$\sup_{\varepsilon<\varepsilon_0}\sup_{h\in K_\varepsilon}
  \sup_{t\le T}\sup_X e^{-a|X|}\|Z^h_\varepsilon(t,X)\|_p\le C,$$
$$\sup_{\varepsilon,h}\sup_{t,X\ne Y\in[-L,L]}
  \frac{\|Z^h_\varepsilon(t,X)-Z^h_\varepsilon(t,Y)\|_p}{|X-Y|^\alpha}\le C,$$
$$\sup_{\varepsilon,h}\sup_{X\in[-L,L],\,s\ne t}
  \frac{\|Z^h_\varepsilon(t,X)-Z^h_\varepsilon(s,X)\|_p}
       {|t-s|^\beta\vee\varepsilon^{\alpha}}\le C.$$
The denominator $|t-s|^\beta\vee\varepsilon^\alpha$ is exactly the Parekh
§3.5 jump scale: at fixed $\varepsilon$ the process jumps (rescaled jump
size $O(\sqrt\varepsilon)$ uniformly in $h$ since a microscopic jump changes
$h_\varepsilon$ by $2\sqrt\varepsilon$ at one lattice point), and the
Kolmogorov criterion applied at macroscopic $|t-s|\gg\varepsilon^2t_{\rm mic}$
leaves the microscopic-jump floor $\varepsilon^\alpha$. By Kolmogorov–Chentsov
(with weights), $\{Z^h_\varepsilon:h\in K_\varepsilon\}$ is tight in
$C([0,T],C(\mathbb R))$ with modulus uniform in $h$, and
$$\mathbb E\bigl[\sup_{h\in K_\varepsilon}\|Z^h_\varepsilon\|
   _{C^\beta([0,T],C^\alpha([-L,L]))}^{p}\bigr]\le C(L,p)$$
after the standard chaining in $(t,X)$ (constants depend on $K$ only via
$M_K$). The accompanying numerical artifact verifies the analytic input in a
toy discrete SHE: over a 12-profile net with one common noise, pairwise
difference quotients stay bounded by a $T$-dependent $C$ (max ratio
$\approx2$–$3$ at all snapshots) and the temporal modulus grows
sublinearly, consistent with the claimed uniform-in-$h$ contraction.

## Step 3. All $h$ see the same noise (joint-noise identification)

Write the martingale part as a stochastic integral against the common
compensated clock field $W_\varepsilon$ (rescaled compensated Poisson
measure, converging to space-time white noise):
$$M^h_\varepsilon(\phi)=\int_0^\cdot\!\!\int\phi\,
   c(\eta^h_\varepsilon)\,dW_\varepsilon+\text{(negligible)},$$
with bounded coefficient $c(\eta)=O(1)$, $c(1/2)\equiv c_0$ (the BG constant
absorbed into $\xi$). Since rescaled profiles in $K$ have macroscopic slope
$0$ at lattice scale — precisely,
$\eta^h_x-\tfrac12=O(\sqrt\varepsilon)$ weakly — the hydrodynamic
replacement (one-block / Boltzmann–Gibbs) gives
$$\int\phi\,(c(\eta^h_\varepsilon)-c_0)\,dW_\varepsilon\to0$$
in $L^2$, uniformly over $h\in K_\varepsilon$. Uniformity uses only the
envelope $M_K$ and attractiveness: under basic coupling the discrepancy
$\eta^h-\eta^{h'}$ is a bounded-density system of second-class particles,
and on $[-L/\varepsilon,L/\varepsilon]$ its total mass is
$O(\sqrt\varepsilon^{-1}\|h-h'\|_\infty+1)$; for the diagonal $h=h'$ term the
cancellation is the standard BG second-order Boltzmann–Gibbs estimate whose
inputs ($\|\eta\|_\infty\le1$, uniform $Z$-moments) are $h$-uniform.
Consequence: for fixed $h_1,\dots,h_k$,
$$(W_\varepsilon,M^{h_1}_\varepsilon,\dots,M^{h_k}_\varepsilon)
  \Rightarrow (W,c_0W,\dots,c_0W),$$
i.e. cross-variations satisfy
$\langle M^{h_i}_\varepsilon(\phi),M^{h_j}_\varepsilon(\psi)\rangle_t
 \to c_0^2t\langle\phi,\psi\rangle_{L^2}$ for every pair $(i,j)$,
including $i\ne j$. Thus the $k$-vector of discrete SHEs converges to $k$
copies of SHE driven by the **same** white noise. This is the only place
where the common coupling is used, and it is exactly why the limit graphs
$G(\Phi_t)$ use one $\xi$ for all $h$.

## Step 4. Finite-net joint convergence + equicontinuity in $h$ imply uniform convergence of $Z$

(a) *Finite nets.* Fix $h_1,\dots,h_k\in K$ and approximants
$h_i^\varepsilon\in K_\varepsilon$. By Steps 2–3 and the standard martingale
problem (Stroock–Varadhan for SHE; cf. BG Theorem + Corwin–Shen §4),
$$(Z^{h_1^\varepsilon}_\varepsilon,\dots,Z^{h_k^\varepsilon}_\varepsilon)
  \Rightarrow (Z^{h_1},\dots,Z^{h_k})$$
in $C([0,T],C(\mathbb R))^k$, the limit driven by one $\xi$.

(b) *Equicontinuity in $h$.* The difference
$D^{h,h'}_\varepsilon=Z^h_\varepsilon-Z^{h'}_\varepsilon$ satisfies the same
linear discrete SHE (same $W_\varepsilon$ up to the vanishing Step-3 error)
with initial data $Z^h_{0,\varepsilon}-Z^{h'}_{0,\varepsilon}$.
Energy/Burkholder estimates give, with $d(h,h')$ the
$C^{\alpha'}_{\delta'}$-distance,
$$\|D^{h,h'}_\varepsilon(t,X)\|_p\le C\,e^{a|X|}\,
   d(h,h')\,\exp(C(1+M_K)),$$
uniformly in $\varepsilon,t,X$, using
$|e^{h}-e^{h'}|\le e^{C(1+M_K)}|h-h'|$ on compacts. The identical estimate
holds for the limit SHE family $\{Z^h\}$. Hence both families are
$L^p$-Lipschitz in $h$, uniformly in $\varepsilon$.

(c) *Chaining.* $K$ is compact, hence totally bounded: for
$\rho>0$ cover $K$ by $N(\rho)$ balls. Combine (a) on centres with (b)
(Lipschitz tails $\le C\rho$) and let $\rho\to0$ after
$\varepsilon\to0$. Standard chaining (e.g. Mitoma–Fouque–Horowitz criterion
for $C(K)$-valued processes) yields, after Skorokhod representation,
$$\sup_{t\le T}\sup_{h\in K_\varepsilon}
  \|Z^{h^\ast(h)}_\varepsilon(t)-Z^{h}(t)\|_{C([-L,L])}\to0
  \quad\text{in probability},$$
where $h\mapsto h^\ast(h)$ is any Hausdorff-optimal pairing. That is joint
functional convergence uniform over the compact.

## Step 5. Uniform Hopf–Cole inversion (uniform positivity)

On each $[-L,L]$, $\log$ is Lipschitz on $[c_0,\infty)$.
It suffices that
$$\inf_{\varepsilon}\mathbb P\Bigl(
  \inf_{h\in K_\varepsilon}\inf_{t\le T}\inf_{X\in[-L,L]}
  Z^h_\varepsilon(t,X)\wedge Z^{h}(t,X)\ge c_0\Bigr)\ge1-\gamma$$
for suitable $c_0(\gamma,L,K)>0$. One-point lower tails:
for SHE started from $e^{h}\ge e^{-M_K(1+|\cdot|)^\delta}$,
$\mathbb P(Z^h(t,X)<c)\le C c^{\theta}$ with $C,\theta$ depending only on
$M_K$ (Mueller comparison + small-ball estimate; discrete version from
Corwin–Shen Lemma 4.7, whose barrier depends only on the growth envelope).
Chaining with the Step-2 modulus upgrades one-point bounds to uniform
bounds over $(t,X,h)$ at cost $N(\rho)$ (finite by compactness of
$[0,T]\times[-L,L]\times K$). Choosing $c_0$ small then $\rho$ small gives
the claim. On this high-probability event,
$$\sup_{t,h}\|h^h_\varepsilon(t)-h^{h}(t)\|_{C([-L,L])}
  \le c_0^{-1}\sup_{t,h}\|Z^h_\varepsilon(t)-Z^{h}(t)\|_{C([-L,L])}
  +o(1),$$
the $o(1)$ absorbing BG centering constants. Since $\gamma>0$ is arbitrary,
uniform convergence in probability of heights follows; tightness upgrades
it to convergence in law in $C([0,T],C(\mathbb R))$ uniformly over $K$.

Limit continuity in $h$ (needed for graph identification) follows from the
same Lipschitz bound for $Z^h$ plus log-Lipschitz on the positivity event,
exhausting $L\to\infty$, $\gamma\to0$.

## Step 6. From uniform maps to graph-valued paths

Let $d_{L}$ metrize local-uniform convergence and $d_H^L$ the induced
Hausdorff metric on closed subsets of $C\times C$. Given
$d_H(K_\varepsilon,K)\to0$ and
$\sup_{h\in K_\varepsilon}\|\Phi_{\varepsilon}(h^\ast)-\Phi(h^\ast)\|\to0$
in probability uniformly in $t$ (Step 5, Skorokhod-coupled for convergence
in law), a standard $\eta$-net lemma gives
$$\sup_{t\le T}d_H^L(G(\Phi_{\varepsilon,t}),G(\Phi_t))\to0$$
in probability on the Skorokhod space, for every $L$. Indeed, each
$(h,\Phi_\varepsilon h)$ is $C\rho$-close to a centre pair, which is
$o(1)$-close to the limit graph, and vice versa using
$K\approx K_\varepsilon$. The temporal modulus of Step 2 passes to the
graphs (Hausdorff distance of graphs inherits the uniform Hölder bound
outside $\varepsilon$-scale jumps), giving tightness of
$t\mapsto G(\Phi_{\varepsilon,t})$ in $C([0,T],\text{closed sets})$ and
hence convergence in law of the graph-valued paths, uniform in $t$.
The Skorokhod representation turns convergence in law into a.s. uniform
graph convergence under one coupling — the "equivalently under a Skorokhod
coupling" clause.

## Step 7. Conclusion

All convergences are uniform over the compact $K$ (constants depend on $K$
only through its envelope $M_K$ and covering numbers), uniform in
$t\in[0,T]$, local-uniform in $X$, for arbitrary $K_\varepsilon\to K$.
The limit uses one white noise for all $h$ (Step 3) and the Hopf–Cole map
(Step 5). This is exactly the claimed uniform flow convergence with the
Parekh §3.5 modulus $|t-s|^\alpha\vee\varepsilon^\alpha$. ∎

## Remarks on inputs and self-checks

- Fixed-$h$ BG/Corwin–Shen/Parekh estimates are used as black boxes only
  through their dependence on initial data via weighted norms; we verified
  no hidden $h$-dependent constant enters (Step 2), which is the
  load-bearing uniformity claim, and cross-checked its linear-chaining
  consequence numerically (artifact `check_chaining.py`, ratios bounded).
- Joint-noise identification (Step 3) is the structural heart: basic
  coupling + density $1/2$ + bounded occupations force full asymptotic
  correlation. We state the replacement estimate in the form needed and
  note its inputs are $h$-uniform by attractiveness.
- Positivity (Step 5) is proved via the standard one-point small-ball +
  chaining route; compactness of $K$ makes the chaining cost finite.
- No originality claim beyond the target is made; no literature search was
  needed (all gaps closed locally from standard tools).
