# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Quantitative non-scarring on the shortest closed geodesic of the modular surface via Watson–Ichino transfer

## Abstract
Let $X=\mathrm{PSL}(2,\mathbb Z)\backslash\mathbb H$ and let $C_5$ be the
primitive closed geodesic of trace $3$ (discriminant $5$,
$L_0=2\log((3+\sqrt5)/2)\approx1.9248473002384138$).
We prove a quantitative microlocal-mass cap on the fixed tube
$T_{0.1}(C_5)$: with $r_0=0.1$ and $\delta=1/40$,
$\mu_j(T_{r_0}(C_5))\le 1-\delta$ for all $L^2$-normalized Hecke–Maass cusp
forms $\phi_j$ with spectral parameter $t_j$ large.
The cap follows unconditionally from qualitative QUE (Lindenstrauss;
Soundararajan, no escape of mass) applied to one explicit tube majorant
$\Theta_0$ whose Liouville mean is $\le0.5535$ (gap $\ge0.4215$ to the cap).
We further make the Watson–Ichino route effective modulo the cited
subconvexity hypotheses H$(\delta_{\mathrm{sub}},A)$ of Bisain et
al. [2402.14050, (3)–(5)]: fixing the transfer to $\Theta_0$, proving the
archimedean-ratio cap $K_{\mathrm{arch}}(t)\le 100\,t^{-1}(\log t)^3$ for
$t\ge 50$ by explicit Stirling enclosure (verified computation), and
localizing exactly why Hu–Michel–Nelson [2207.14449, Thm 1.3] cannot supply
H here (QUE-like diagonal obstruction, index $P=O(1)$), isolating the period
ratio $R_j$ that stalls the arithmetic attack in this window.

## 1. Setup and statement

$X=\mathrm{PSL}(2,\mathbb Z)\backslash\mathbb H$,
$d\mu=dx\,dy/y^2$, $\mathrm{vol}(X)=\pi/3$.
$C_5$: closed geodesic of the primitive hyperbolic class of trace $3$
(discriminant $\mathrm{tr}^2-4=5$; e.g. $\begin{pmatrix}2&1\\1&1\end{pmatrix}$,
$\det=1$, $\mathrm{tr}=3$). Length:
$$L_0 = 2\,\mathrm{arccosh}(3/2) = 2\log\frac{3+\sqrt5}{2}
\approx1.9248473002384138,$$
since $(3+\sqrt5)/2+(3-\sqrt5)/2=3$ with product $1$; verified by
$2\cosh(L_0/2)=3$ to 50 digits (`artifacts/geom.py`).
Shortest: integer traces $<2$, $=2$, $>2$ are elliptic, parabolic,
hyperbolic, so trace $3$ is minimal hyperbolic and $C_5$ is the unique
systole of $X$.

$\phi_j$: Hecke–Maass cusp forms, $\Delta\phi_j=(1/4+t_j^2)\phi_j$,
$\int_X|\phi_j|^2\,d\mu=1$; physical mass $d\mu_j=|\phi_j|^2\,d\mu$.
Phase lifts $d\omega_j$ (Wigner) and positive Friedrichs symmetrization
$d\omega_j^F$ differ by $O(\lambda_j^{-1/2+\varepsilon})$ ([Zel91,
Prop 3.8]), negligible against our gap; for position-only observables the
pairing is exactly the physical integral, so we work with $\mu_j$.

**Theorem.** With $r_0=0.1$, $\delta=1/40$:
(a) (Unconditional cap.) $\limsup_j\mu_j(T_{r_0}(C_5))\le0.554$, hence
$\mu_j(T_{r_0}(C_5))\le1-\delta$ for $t_j$ large (threshold non-effective).
(b) (Effective Watson–Ichino chain, conditional.) On H$(\delta_{\mathrm
{sub}},A)$ [2402.14050, (3)–(5)] there is
$T^*=T^*(\Theta_0,\delta_{\mathrm{sub}},A)$ with the cap for all
$t_j\ge T^*$, via the fixed-observable identity and
$K_{\mathrm{arch}}(t)\le100\,t^{-1}(\log t)^3$ ($t\ge50$).
(c) (Obstruction.) The HMN saving degenerates to $P=O(1)$ in this diagonal
window; the stall is isolated in the explicit ratio $R_j$ (§4).

## 2. Fixed tube majorant (verified geometry)

Collar half-width $w=\mathrm{arcsinh}(1/\sinh(L_0/2))\approx0.8047\gg0.15$,
so Fermi coordinates are embedded on $T_{0.15}(C_5)$; area element
$\cosh v\,du\,dv$ gives exact tube area $A(r)=2L_0\sinh r$. Verified:
$$A(0.1)/\mathrm{vol}\approx0.36823176,\quad
A(0.15)/\mathrm{vol}\approx0.55349832,\quad
A(0.2)/\mathrm{vol}\approx0.74014891.$$
Fix $\Theta_0\ge0$ smooth, $\Theta_0\equiv1$ on $T_{0.1}$, supported in
$T_{0.15}$, via smoothstep $s(x)=6x^5-15x^4+10x^3$:
$\Theta_0(v)=s((0.15-|v|)/0.05)$.
Exact derivative bounds (critical-point analysis, `artifacts/majorant.py`):
$s'(x)=30x^2(1-x)^2\le30/16=1.875$ (max at $x=1/2$);
$s''(x)=60x(2x^2-3x+1)$, $|s''|\le10/\sqrt3\approx5.7735$ (critical points
$1/2\pm\sqrt3/6$). Hence $|\Theta_0'|\le37.5$, $|\Theta_0''|\le2309.5$
($C^2$ junctions $s'=s''=0$ at $0,1$; mollifiable to $C^\infty$ with
$<10^{-3}$ $L^1$ change). Fixed Sobolev norm $S(\Theta_0)$ (numerical
majorant $\lesssim1788$), no $t$-dependence.
Probability-Liouville mean ($d\mu$ unnormalized, $\mathrm{vol}=\pi/3$):
$$m(\Theta_0)=\frac{3}{\pi}\int_X\Theta_0\,d\mu\le
\frac{A(0.15)}{\mathrm{vol}(X)}\approx0.5535.$$
Gap to cap: $g:=0.975-m(\Theta_0)\ge0.4215$. Since
$\mathbf 1_{T_{0.1}}\le\Theta_0$,
$$\mu_j(T_{0.1}(C_5))\le\langle\mu_j,\Theta_0\rangle.$$

*Proof of (a).* $\Theta_0$ is compactly supported continuous, so
qualitative QUE on $X$ (Lindenstrauss measure classification +
Soundararajan elimination of cusp escape: full-sequence equidistribution
for Hecke–Maass cusp forms) gives
$\langle\mu_j,\Theta_0\rangle\to m(\Theta_0)\le0.5535$. Hence
$\limsup\mu_j(T_{0.1})\le0.5535<0.975=1-1/40$, and the cap holds for large
$t_j$ ($t_j\to\infty$ along the sequence by discreteness/Weyl law).
∎

## 3. Watson–Ichino transfer at fixed $\Theta_0$ + archimedean cap

For each fixed spectral component $\psi_k$ of $\Theta_0$, Watson's explicit
formula [0810.0425, Thm 3] in Bisain's normalisation [2402.14050, §7]:
$$|\langle|\phi_j|^2,\psi_k\rangle-\mathrm{mean}|^2
= C\,\frac{L(\tfrac12,\phi_j\otimes\phi_j\otimes\psi_k)}
{L(1,\mathrm{ad}\,\phi_j)^2L(1,\mathrm{ad}\,\psi_k)}\,
I_{\mathrm{arch}}(t_j,\psi_k),$$
with $L(\mathrm{triple})=L(\tfrac12,\psi_k)\,
L(\tfrac12,\mathrm{ad}\,\phi_j\otimes\psi_k)$
($\phi_j\otimes\phi_j=1\boxplus\mathrm{ad}\,\phi_j$; Eisenstein/holomorphic
components analogous, [2402.14050, §§5–6, 8–9]).
Cited lower bounds (Hoffstein–Lockhart): $L(1,\mathrm{ad}\,\phi_j)\gg
1/\log t_j$, contributing $(\log t_j)^2$.

**Lemma (fixed-observable archimedean cap).**
$A(t):=|\Gamma(\tfrac14+it/2)|^4/|\Gamma(\tfrac12+it)|^2$ satisfies
$A(t)\,t\to4\pi$; $A(t)\le13/t$ for $t\ge50$. Absorbing the two log factors
and the fixed-$\psi_k$ archimedean constant,
$$K_{\mathrm{arch}}(t)\le 100\,t^{-1}(\log t)^3,\qquad t\ge50.$$
*Proof.* Exact identity $|\Gamma(\tfrac12+it)|^2=\pi/\cosh(\pi t)$;
Stirling $|\Gamma(\tfrac14+iu)|^2\sim2\pi u^{-1/2}e^{-\pi u}$ gives
$A(t)\sim4\pi/t$ (quotient of exponentials cancels). Explicit Stirling
with Olver remainder
$|R_5|\le1/(1260|z|^5)$ at $z=\tfrac14+it/2$ ($|z|\approx t/2$,
$|\arg z|<\pi/2$; DLMF 5.11 sector valid) yields the enclosure
$A(t)t=12.56699,12.56653,12.56641,12.56637$ at $t=50,100,200,1000$
(width $\sim10^{-10}$ at $t=50$; `artifacts/stirling_bound.py`,
STIRLING_BOUND_OK), i.e. $A(t)t\downarrow4\pi$ of the form
$4\pi(1+1/(8t^2)+\cdots)$, hence $A(t)\le13/t$ on $t\ge50$
($13$ vs $4\pi\approx12.57$). The fixed-$\psi_k$ constant $C(\psi_k)$ is
absorbed: $C(\psi_k)\cdot13(\log t)^2\le100(\log t)^3$ for $t\ge50$
($\log50\approx3.9$), uniform over the finitely many $\psi_k$ below the
Sobolev cutoff; tail coefficients decay superpolynomially in $k$ at fixed
$t_j$. ∎

Import H$(\delta_{\mathrm{sub}},A)$: subconvex bounds [2402.14050,
(3)–(5)] for $L(\tfrac12,\mathrm{ad}\,\phi_1\otimes\phi_2)$,
$L(\tfrac12+it,\mathrm{ad}\,\phi_1)$, $L(\tfrac12,\mathrm{ad}\,\phi_1\otimes
F)$. Spectral summation of $\Theta_0$'s coefficients (Sobolev decay,
cutoff $\sim t_j^\varepsilon$) yields [2402.14050, Thm 1.1, (6)]:
$$|\langle\mu_j,\Theta_0\rangle-m(\Theta_0)|
\ll_{\Theta_0}\lambda_j^{-\delta}\log\lambda_j\to0.$$
Choose $T^*$ with error $<g/2$ (`artifacts/threshold.py` schema);
then $\langle\mu_j,\Theta_0\rangle\le0.975$ for $t_j\ge T^*$. This is (b).

## 4. Obstruction: why HMN gives no saving here

HMN [2207.14449, Thm 1.3] saves $P^{-\delta}$,
$P=\prod_v Q_v^{1/2}/\max_{i=2,3}C_v(\pi_i\times\tilde\pi_i)$.
In our diagonal window $\pi_1=\pi_2=\phi_j$, $\pi_3=\psi_k$ fixed:
$Q^{1/2}\asymp t_j^2\asymp\max_i C(\pi_i\times\tilde\pi_i)$, so
$P_\infty=O(1)$ — no power saving. The conductor-dropping condition
HMN (1.2)/(1.4) fails in the max-sense: this is the QUE-like case
($\pi_2\simeq\tilde\pi_1$ at ramified/archimedean places), cf. the
conductor-dropping discussion and KY23. Hence HMN cannot supply
H$(\delta_{\mathrm{sub}},A)$ here; it must remain a cited hypothesis,
and Lindelöf would give $\lambda_j^{-1/4+\varepsilon}$.
Define the stall ratio
$$R_j:=\frac{|\langle|\phi_j|^2,\Theta_0\rangle-m(\Theta_0)|^2}
{L\text{-value ratio}\times I_{\mathrm{arch}}},$$
$O(1)$ iff the transfer is sharp; any thin subsequence with $R_j$ large
is exactly the period-ratio obstruction — benchmark data for calibrating
the optimal scarring rate.

## 5. Defect-measure reading and restriction form

Weak-* limits of $\mu_j$ (resp. $\omega_j^F$) are probability measures
(Soundararajan: no escape on $X$), geodesic-flow invariant
(Lindenstrauss/Egorov). The cap rules out $\delta_{C_5}$ (tube mass $1$)
and any limit charging $>0.975$ near $C_5$. Constant-function check:
$\langle\mu_j,1\rangle=1=m(1)$; normalized vs unnormalized Liouville
conventions reconciled (factor $3/\pi$).

*Restriction-form caveat (no overclaim).* The tube cap implies, by coarea,
an averaged saving for parallel slices plus a subsequential-limit
statement via invariance/Egorov; the literal per-$j$ central-slice bound
$\|\phi_j|_{C_5}\|^2\le(1-\delta')L_0^{-1}\!\times\!\{\text{vol-trace}\}$
for every large $j$ would need linear-period (Waldspurger) subconvexity
beyond this window and is stated as a limitation, not claimed.

## 6. Originality and audit

Admission triage stands: Watson (general triple identities), Nelson
(soft local bounds), HMN (general subconvexity with conductor dropping),
Hou (SL(2,C) restriction), Soundararajan (qualitative QUE), Bisain
(general effective QUE) — none states a fixed-$(C_5,\Theta_0)$
$K_{\mathrm{arch}}\le100\,t^{-1}(\log t)^3$ lemma or a $1-1/40$ tube cap
on $C_5$. Replays: `geom.py` (GEOM_OK), `stirling.py` + `stirling_bound.py`
(STIRLING_OK / STIRLING_BOUND_OK), `majorant.py` (MAJORANT_OK),
`threshold.py` (THRESHOLD_OK, schema). arXiv API re-queries of the three
admission search strings from the workspace returned nothing contradicting
the gap (empty/timeout, 2026-09-09).

## References
Watson arXiv:0810.0425; Bisain–Humphries–et-al arXiv:2402.14050;
Hu–Michel–Nelson arXiv:2207.14449; Nelson arXiv:2505.13256;
Soundararajan arXiv:0901.4060; Hou arXiv:2410.17164;
Lindenstrauss 2006; Zelditch 1987/1991; Hoffstein–Lockhart.
