# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Extremal-process convergence for two-speed BRW in the mean regime — full proof
*(repaired truncation core: explicit H1' range, subcritical-tilt I3 control,
bounded-$d_n$ additive-martingale term, $p_m$-based max law)*

## Notation and setting

Fix $t\in(0,1)$, $k=k_n=\lfloor tn\rfloor$, $m=m_n=n-k\sim(1-t)n$.
$L_1,L_2$ non-lattice supercritical reproduction point processes satisfying
Luo (1.11)--(1.13); $\theta_1^*=\theta_2^*=:\theta$.

$\kappa_i(\vartheta)=\log E_{L_i}[\sum_{|u|=1}e^{\vartheta X_u}]$,
$v_i=\kappa_i'(\theta)$, boundary case $\kappa_i(\theta)=\theta v_i$.
Two-speed BRW $V^{(n)}$: $L_1$ for generations $1..k$, $L_2$ after.
Centering $m_n=v_1k+v_2m-\frac{3}{2\theta}\log n$.
Homogeneous $L_2$ BRW $V_2$, centering $m^{(2)}_m=v_2m-\frac{3}{2\theta}\log m$.
Put $d_n=\frac{3}{2\theta}\log(n/m)\to c_t:=-\frac{3}{2\theta}\log(1-t)$,
a **finite** constant, so $e^{\theta d_n}=(n/m)^{3/2}\to(1-t)^{-3/2}$.

Condition on ${\cal F}_k$ (first phase). Given ${\cal F}_k$, for each
$|w|=k$ at $x_w=V_1(w)$, the descendant subtree of depth $m$ is an
independent homogeneous $L_2$ BRW rooted at $x_w$. Write
$s_w=x_w-v_1k$, $b_w=-s_w=v_1k-x_w$, $z_w=b_w-d_n$.
For descendant $x_w+X_u$ ($X_u$ homogeneous $L_2$ displacement from 0),

$$x_w+X_u-m_n = s_w+d_n+(X_u-m^{(2)}_m),\qquad
  m_n-m^{(2)}_m = v_1k-d_n.$$

Hence with $E^{(2)}_m=\sum_{|u|=m}\delta_{X_u-m^{(2)}_m}$ (i.i.d. copies
$E^{(2),w}_m$ per $w$), conditional on ${\cal F}_k$,

$${\cal E}_n:=\sum_{|u|=n}\delta_{V^{(n)}(u)-m_n}
   =\sum_{|w|=k}\theta_{\,s_w+d_n}E^{(2),w}_m
   =\sum_{|w|=k}\theta_{-z_w}E^{(2),w}_m\tag{1}$$
($\theta_a$ = shift by $a$). The relevant homogeneous upper-tail level is
$z_w=b_w-d_n=-s_w-d_n$: cluster $E^{(2)}_m$ must reach $\approx z_w$.

Derivative and additive martingales of phase 1:
$$D_k=\sum_{|w|=k} b_w e^{-\theta b_w}
   =\sum_{|w|=k}(-s_w)e^{\theta s_w},\qquad
  W_k=\sum_{|w|=k}e^{\theta s_w}.$$
Under Luo (1.11)--(1.13) ($X\log X$-type + exponential moments),
$D_k\to Z^{(1)}\ge 0$ a.s. with $Z^{(1)}$ nondegenerate,
$W_k\to 0$ a.s. (Biggins--Kyprianou; Lyons' change-of-measure
conditions, implied by Luo), and
$\{Z^{(1)}>0\}=\{\text{survival of }L_1\}$ a.s. up to null sets;
$Z^{(1)}=0$ on extinction, where ${\cal E}_n$ is empty for large $n$
(finite total progeny; empty sums below are $0$, empty products $1$,
and $\max\varnothing:=-\infty$ by convention).
Since $d_n\to c_t$ is **bounded**,
$$d_nW_k\longrightarrow 0\quad\text{a.s.},\qquad
  e^{\theta d_n}(D_k-d_nW_k)\longrightarrow(1-t)^{-3/2}Z^{(1)}
  \quad\text{a.s.}\tag{2}$$
using only $W_k\to0$ a.s.
*Remark (Seneta--Heyde, not needed).* The quantitative norming
$\sqrt{k}\,W_k\to c_0Z^{(1)}$ in probability on survival is
A\"id\'ekon--Shi, "The Seneta--Heyde scaling for the branching random
walk", Ann. Probab. 42(3), 2014, Theorem 1.1 (see also Chen's revisited
proof under optimal $X\log X$ assumptions). It is recorded here only as
context; (2) uses boundedness of $d_n$, not SH tightness.

Fix once and for all an explicit intermediate scale
$$r_m:=m^{1/4}\quad(\,r_m\to\infty,\ r_m=o(\sqrt m)\,),$$
and put $T_n:=d_n+r_m\to\infty$.

## Homogeneous inputs (spine + ballot black boxes)

Let $\phi\ge 0$ continuous with compact support, $\phi\not\equiv0$,
$\mathrm{supp}\,\phi\subset(-\infty,K]$. For homogeneous $L_2$ depth $m$ set
$$F_m(z)=E\big[e^{-\langle\theta_zE^{(2)}_m,\phi\rangle}\big],\quad
  g_m(z)=1-F_m(z),$$
and $p_m(a)=P(\max E^{(2)}_m\ge a)$.

**Lemma H1$'$ (uniform Laplace/maximum tail on the exact range used).**
There is $C_*>0$ (homogeneous maximum constant) and for each $\phi$ a
constant
$$C(\phi)=C_*\int_{-\infty}^{\infty}
  \big(1-E[e^{-\langle{\cal D}^{(2)},\theta_y\phi\rangle}]\big)\,
  \theta e^{-\theta y}\,dy\ \ge 0,$$
(${\cal D}^{(2)}$ the decoration law, $\max{\cal D}^{(2)}=0$ a.s.),
strictly $>0$ if $\phi\not\equiv0$, such that: for every fixed $A$,
$$\sup_{z\in[A,\,r_m]}
  \Big|\frac{g_m(z)}{z\,e^{-\theta z}}-C(\phi)\Big|\longrightarrow 0,
  \qquad
  \sup_{a\in[A,\,r_m]}
  \Big|\frac{p_m(a)}{a\,e^{-\theta a}}-C_*\Big|\longrightarrow 0.
  \tag{H1$'$}$$
More generally the convergence holds uniformly on $[A,\rho_m]$ for any
$\rho_m\to\infty$ with $\rho_m=o(\sqrt m)$; we use only $\rho_m=r_m
=m^{1/4}$. *Citations.* Maximum version: A\"id\'ekon, "Convergence in
law of the minimum of a branching random walk", Ann. Probab. 41(3),
2013 (doi:10.1214/12-aop750), Theorem 1.1 and the ballot/local-limit
machinery of Sections 3--4 (uniformity on sub-ballistic
$o(\sqrt m)$ ranges via Stone's local limit under non-lattice).
Laplace/decoration version: Madaule, "Convergence in law for the BRW
seen from its tip", J. Theoret. Probab. 30, 2017
(doi:10.1007/s10959-015-0636-6), Theorem 1.1; genealogy/decoration
formulation in Mallein, ALEA 15, 2018 (doi:10.30757/alea.v15-39).
Non-lattice removes periodic oscillation (Stone LLT continuity), giving
uniformity without lattice subsequences. The $o(\sqrt m)$ restriction is
exactly the ballot regime where the spine local limit applies; choosing
the explicit $r_m=m^{1/4}$ reconciles the earlier "$o(\sqrt m)$ vs fixed
$\delta\sqrt m$" mismatch: no uniformity up to $O(\sqrt m)$ is claimed
or used.

**Lemma H2 (global upper bound).** For some $C(\phi)$,
$$0\le g_m(z)\le C\,(1+(z_+))\,e^{-\theta z}\quad\forall\,m,z,$$
and $g_m\le1$; similarly $0\le p_m(a)\le C(1+a_+)e^{-\theta a}$.
*Provenance:* same ballot/spine references; the bound is the standard
many-to-one + ballot upper estimate, valid for all $z$ including
$z\gg\sqrt m$.

**Lemma H3 (phase-1 barrier; ballot).** Let
$\bar s_k=\max_{|w|=k}s_w+\frac{3}{2\theta}\log k$.
$\{\bar s_k\}$ is tight above: $\forall\varepsilon\,\exists L$,
$P(\bar s_k\ge L)<\varepsilon$ for large $k$ (A\"id\'ekon 2013 upper
envelope; also Bramson-type ballot bounds). Put
$G_k(L)=\{\bar s_k\le L\}$ (on extinction, with no particles, $G_k$
holds vacuously with $\min\varnothing:=+\infty$). On $G_k(L)$,
$$\min_w z_w\ \ge\ \frac{3}{2\theta}\log k-L-d_n
  =\frac{3}{2\theta}\log(km/n)-L+c\,o(1)\longrightarrow+\infty,$$
since $km/n\sim t(1-t)n\to\infty$. So for any fixed $A$,
$\{w:z_w<A\}=\varnothing$ on $G_k(L)$ eventually, and with
$A_n:=\min_w z_w\to\infty$ in probability,
$\max_w g_m(z_w)\le C(1+A_n)e^{-\theta A_n}\to0$ in probability by H2.

**Lemma T (in-probability far-tail control; replaces the false $L^1$
claim).** Assume Luo (1.11) so $\kappa_1(\vartheta)<\infty$ in a
neighbourhood of $\theta$. Pick $\theta_0<\theta$ close with
$\kappa_1(\theta_0)<\infty$ and set $\eta=\theta-\theta_0>0$,
$W_k(\theta_0)=\sum_{|w|=k}e^{\theta_0s_w}$. Then for every $T>0$,
$$\sum_{|w|=k}(1+b_{w,+})e^{-\theta b_w}{\bf1}_{\{b_w>T\}}
   \ \le\ C_\eta\,e^{-\eta T/2}\,W_k(\theta_0),\tag{T1}$$
with $C_\eta=\sup_{u\ge0}(1+u)e^{-\eta u/2}<\infty$, and with
$\varphi(\vartheta)=\kappa_1(\vartheta)-\vartheta v_1$,
$$E[W_k(\theta_0)]=e^{k\varphi(\theta_0)},\qquad
  \varphi(\theta_0)<0,\tag{T2}$$
so for $T_n\to\infty$ (in particular $T_n=d_n+r_m$),
$$e^{\theta d_n}\sum_{b_w>T_n}(1+b_w)e^{-\theta b_w}
   \xrightarrow{P} 0,\qquad
  e^{\theta d_n}\sum_{b_w>T_n}b_we^{-\theta b_w}
   \xrightarrow{P} 0.\tag{T3}$$
*Proof.* For $b_w>T>0$, $s_w=-b_w<-T$ and
$(1+b_w)e^{-\theta b_w}=(1+|s_w|)e^{\theta s_w}
=(1+u)e^{-\eta u}e^{\theta_0s_w}$ with $u=|s_w|>T$.
Since $(1+u)e^{-\eta u}\le C_\eta e^{-\eta u/2}\le C_\eta e^{-\eta T/2}$,
summing gives (T1) (for $b_w>T\ge0$, $b_{w,+}=b_w$).
Many-to-one gives
$E[\sum_w e^{\theta_0s_w}]
=e^{-\theta_0v_1k}E[\sum_w e^{\theta_0x_w}]
=e^{-\theta_0v_1k}e^{k\kappa_1(\theta_0)}=e^{k\varphi(\theta_0)}$.
Boundary case: $\varphi(\theta)=0$, $\varphi'(\theta)
=\kappa_1'(\theta)-v_1=0$, $\varphi''=\kappa_1''>0$ near $\theta$
(non-degenerate tilted increments under supercritical non-lattice Luo
hypotheses), hence $\varphi(\theta_0)<0$ for $\theta_0\ne\theta$ close.
Then $E$ of the left side of (T1) times bounded $e^{\theta d_n}$ is
$\le C_\eta e^{\theta d_n}e^{-\eta T_n/2}e^{k\varphi(\theta_0)}\to0$
($T_n\to\infty$ and $k\varphi(\theta_0)\to-\infty$ exponentially), so
Markov yields (T3). No claim $E[\sum(1+|s_w|)e^{\theta s_w}]<\infty$
is made or needed; the tilts $\theta_0<\theta$ make the expectation
finite and exponentially small. ∎

*Method sketch (spine/ballot).* Tilt by $\theta$: many-to-one with
centred (mean $v$) spine walk $S$. $D_k,W_k$ are spine martingales;
$D_k\to Z$ via Biggins--Kyprianou $X\log X$ (implied by Luo). Ballot
estimates for $S$ (Stone local limit, non-lattice) give H1$'$--H2.
Full homogeneous proofs are in the cited works; we use only the
statements H1$'$, H2, H3, T. The two-speed novelty is the combination
below.

The decoration ${\cal D}^{(2)}$ is by hypothesis the weak limit of
$\sum_{|u|=m}\delta_{X_u-\max V_2}$ given $\{\max V_2\ge v_2m\}$
(homogeneous tip-cluster limit); we use its law only through $C(\phi)$.

## Conditional Laplace functional

Fix $\phi$ as above. Conditional on ${\cal F}_k$, by independence (1),
$$\Psi_n:=E\big[e^{-\langle{\cal E}_n,\phi\rangle}\mid{\cal F}_k\big]
   =\prod_{|w|=k}F_m(z_w)=\prod_w(1-g_m(z_w)).\tag{2}$$
On $G_k(L)$ all $z_w\ge A_n\to\infty$, so $\max_w g_m(z_w)\to0$ in
probability (H2--H3). On $\{\max_w g_m\le1/2\}$,
$|\sum_w\log(1-g_m(z_w))+S_n|\le S_n\max_w g_m$ with
$S_n:=\sum_w g_m(z_w)$, using $|\log(1-x)+x|\le x^2$, $x\in[0,1/2]$.
Hence it suffices to prove
$$S_n:=\sum_{|w|=k}g_m(z_w)\ \xrightarrow{\;P\;}\ C(\phi)(1-t)^{-3/2}Z^{(1)}.
\tag{3}$$

Split with fixed $A$ and the explicit $r_m=m^{1/4}$:
$I_1=\{z_w<A\}$, $I_2=\{A\le z_w\le r_m\}$, $I_3=\{z_w>r_m\}$.

*I1.* On $G_k(L)$, $I_1=\varnothing$ eventually (H3, $\min z_w\to\infty$);
$P(G_k(L)^c)<\varepsilon$ arbitrary. Contribution $0$ w.h.p.

*I3.* Here $z_w>r_m$ i.e. $b_w>T_n=d_n+r_m$. By H2 (all $z_w>0$
eventually since $r_m>0$) and $d_n>0$,
$$0\le\sum_{I_3}g_m(z_w)\le C\sum_{I_3}(1+z_w)e^{-\theta z_w}
  \le C\,e^{\theta d_n}\!\!\sum_{b_w>T_n}(1+b_w)e^{-\theta b_w}
  \xrightarrow{P}0$$
by Lemma T, (T3). No $L^1$ bound on
$\sum(1+|s_w|)e^{\theta s_w}$ is used.

*I2 (main term).* H1$'$ applies exactly on $[A,r_m]$:
$g_m(z_w)=C(\phi)z_we^{-\theta z_w}(1+e_{m}(z_w))$ with
$\sup_{[A,r_m]}|e_m|\to0$. Thus
$$\sum_{I_2}g_m = C(\phi)e^{\theta d_n}
   \sum_{|w|=k}(b_w-d_n)e^{-\theta b_w}{\bf1}_{I_2}\,(1+o(1)),$$
$o(1)$ deterministic (uniform relative error).
Now $e^{\theta d_n}\sum_{{\rm all}\,w}(b_w-d_n)e^{-\theta b_w}
=e^{\theta d_n}(D_k-d_nW_k)\to(1-t)^{-3/2}Z^{(1)}$ a.s. by (2).
The restriction ${\bf1}_{I_2}$ removes $I_1$ (empty w.h.p. on $G_k$)
and $I_3$; the $I_3$ part of the $b$-weighted sum satisfies
$e^{\theta d_n}\sum_{I_3}(b_w-d_n)e^{-\theta b_w}
\le e^{\theta d_n}\sum_{b_w>T_n}b_we^{-\theta b_w}\to_P0$ by (T3),
and the $I_1$ part is $0$ w.h.p. Hence
$\sum_{I_2}(b_w-d_n)e^{-\theta b_w}=D_k-d_nW_k+o_P(1)$, giving (3).

Therefore $\Psi_n=\exp(-S_n+o_P(1))\to_P
\exp(-C(\phi)(1-t)^{-3/2}Z^{(1)})$ (on extinction $S_n=0$, $\Psi_n=1$,
same formula with $Z^{(1)}=0$). Bounded convergence gives
$$E[e^{-\langle{\cal E}_n,\phi\rangle}]
   \longrightarrow E\big[e^{-C(\phi)(1-t)^{-3/2}Z^{(1)}}\big].\tag{4}$$

## Identification of the limit (SDPPP)

For a Cox intensity $\Lambda(dy)=C_mZ^{(1)}\theta e^{-\theta y}dy$ with
i.i.d. decorations ${\cal D}^{(2)}_j$ attached to Poisson atoms $y_j$,
the Laplace functional at $\phi$ is exactly
$E[\exp(-C_mZ^{(1)}\!\int(1-Ee^{-\langle{\cal D}^{(2)},\theta_y\phi\rangle})
\theta e^{-\theta y}dy)]$.
Comparing with (4) and $C(\phi)=C_*\int(1-Ee^{-\langle{\cal D}^{(2)},
\theta_y\phi\rangle})\theta e^{-\theta y}dy$ gives
$$C_m = C_*(1-t)^{-3/2}>0,$$
independent of $\phi$. Since (4) holds for all $\phi\ge0$,
$C_c$, Kallenberg's theorem yields vague convergence in law
${\cal E}_n\Rightarrow{\cal E}$, ${\cal E}$ the SDPPP with Cox
intensity $C_mZ^{(1)}\theta e^{-\theta y}dy$ and decorations
${\cal D}^{(2)}$. On $\{Z^{(1)}=0\}$ the Cox intensity is $0$,
i.e. ${\cal E}=\varnothing$, consistent with ${\cal E}_n=\varnothing$.

## Maximum law via the $p_m$ version of (3) (no indicator approximation)

Fix $y\in\mathbb R$. Conditional on ${\cal F}_k$,
$$P(\max{\cal E}_n\le y\mid{\cal F}_k)
   =\prod_{|w|=k}\big(1-p_m(z_w+y)\big),\tag{5}$$
since cluster $w$ exceeds $y$ iff $E^{(2),w}_m$ reaches $z_w+y$
($\max{\cal D}^{(2)}=0$ a.s. is not needed for (5), only for the limit
identification). Set $S^y_n=\sum_w p_m(z_w+y)$ and
$M^y_n=\max_w p_m(z_w+y)$. On $G_k(L)$, $z_w+y\ge A_n+y\to\infty$,
so eventually all $z_w+y\ge A$ and $M^y_n\le C(1+A_n)e^{-\theta A_n}
\to0$ in probability by H2. Splitting $\{z_w+y<A\}$,
$\{A\le z_w+y\le r_m\}$, $\{z_w+y>r_m\}$ exactly as above, H1$'$
(maximum part) gives uniformly on the middle piece
$p_m(z_w+y)=C_*(z_w+y)e^{-\theta(z_w+y)}(1+o(1))$, whence
$$S^y_n = C_*e^{-\theta y}e^{\theta d_n}
   \sum_{I^y_2}(b_w-d_n+y)e^{-\theta b_w}(1+o(1))
   \xrightarrow{P} C_*e^{-\theta y}(1-t)^{-3/2}Z^{(1)},\tag{6}$$
because $e^{\theta d_n}\sum_{{\rm all}}(b_w-d_n+y)e^{-\theta b_w}
=e^{\theta d_n}(D_k+(y-d_n)W_k)\to(1-t)^{-3/2}Z^{(1)}$ a.s. by (2)
($yW_k\to0$ a.s. as well), while the $I^y_1$ piece is empty w.h.p. and
the $I^y_3$ piece ($b_w>d_n+y+r_m$) is $o_P(1)$ by H2+Lemma T
($T_n$ shifted by fixed $y$; (T3) applies verbatim).
Explicit product-to-exponential error: on $\{M^y_n\le1/2\}$,
$$0\le e^{-S^y_n}-\prod_w(1-p_m(z_w+y))
   \le e^{-S^y_n}\big(e^{M^y_nS^y_n}-1\big),\tag{7}$$
since $|\log(1-x)+x|\le x^2$ gives
$|\sum\log(1-p_i)+S^y_n|\le M^y_nS^y_n$.
$S^y_n$ is tight (converges in prob.) and $M^y_n\to_P0$, so the right
side of (7) $\to_P0$. With (5)--(6), on $G_k(L)$ and off it
($P(G_k^c)<\varepsilon$ arbitrary),
$$P(\max{\cal E}_n\le y\mid{\cal F}_k)\xrightarrow{P}
  \exp\!\big(-C_*(1-t)^{-3/2}Z^{(1)}e^{-\theta y}\big),$$
and bounded convergence gives
$$P(\max{\cal E}_n\le y)\longrightarrow
  E\big[\exp(-C_mZ^{(1)}e^{-\theta y})\big],\qquad
  C_m=C_*(1-t)^{-3/2},$$
for every fixed $y$. (On extinction both sides equal $1$:
empty product $=1$, $Z^{(1)}=0$.) This is the stated
Gumbel-with-random-shift law. ∎

## Remarks on hypotheses

- $\theta_1^*=\theta_2^*$ (mean regime) is exactly what makes both tilts
  use the same $\theta$, so $e^{\theta d_n}=(n/m)^{3/2}$ is the only
  cross-phase factor; in the anomalous regimes ($\theta_1^*\ne\theta_2^*$)
  the logarithmic correction and limit structure differ (cf. Luo).
- Non-lattice gives uniformity/continuity in H1$'$ (Stone LLT, no
  subsequence oscillation); supercriticality + Luo (1.11)--(1.13) give
  $X\log X$, exponential moments (used for $\theta_0$ in Lemma T and
  strict convexity $\varphi(\theta_0)<0$), $C_*>0$, and nondegenerate
  $Z^{(1)}$.
- The $(1-t)^{-3/2}$ factor is the $m^{3/2}/n^{3/2}$ ballot-ratio from the
  second phase sharing the $-\frac{3}{2\theta}\log n$ (rather than
  $-\frac{3}{2\theta}\log m$) centering.
- Finiteness of $d_n\to c_t$ is why $d_nW_k\to0$ needs only $W_k\to0$
  a.s.; no Seneta--Heyde norming is invoked in the proof.

## Numerical check (artifact `artifacts/sim_twospeed.py`)

Binary Gaussian two-speed BRW ($\sigma=1$,
$\theta^*=\sqrt{2\log2}$ shared): centered maxima stay tight across $n$
(mean $\approx0$, stable quantiles), and maxima are stochastically larger
when phase-1 $Z_k$ is above median (shift $\approx+1.2$ at $n=16$,
$+2.2$ at $n=20$, Spearman$(Z,\max)=0.76$), consistent with
the $Z^{(1)}$ random-shift SDPPP representation. See
`artifacts/sim_log.txt`, `artifacts/sim_log2.txt`,
`artifacts/sim_summary.json`.
