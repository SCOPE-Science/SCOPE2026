# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Mean-regime extremal process of the two-speed branching random walk

## Theorem (target claim)

Fix $t\in(0,1)$, $t_n=\lfloor tn\rfloor$, $s_n=n-t_n$.
Let $(V^{(n)}(u):|u|\le n)$ be the two-speed branching random walk (BRW)
with reproduction law $\mathcal L_1$ in generations $1,\dots,t_n$ and
$\mathcal L_2$ in generations $t_n+1,\dots,n$. Assume a.s.\ survival,
supercriticality, both $\mathcal L_i$ non-lattice, and a common
$\theta=\theta_1^*=\theta_2^*>0$ such that each $\mathcal L_i$ satisfies

$$\kappa_i(\theta)<\infty,\qquad
\theta\kappa_i'(\theta)=\kappa_i(\theta),\qquad
0<\mathbb E\Bigl[\sum_{\ell\in\mathcal L_i}
(\ell-\kappa_i'(\theta))^2e^{\theta\ell-\kappa_i(\theta)}\Bigr]<\infty,$$

plus
$\mathbb E[X_i(\log^+X_i)^2]+\mathbb E[\tilde X_i\log^+\tilde X_i]<\infty$
with $X_i=\sum e^{\theta\ell-\kappa_i(\theta)}$,
$\tilde X_i=\sum(\kappa_i'(\theta)-\ell)_+e^{\theta\ell-\kappa_i(\theta)}$.
Put $v_i=\kappa_i'(\theta)$ and

$$m_n \;=\; v_1t_n+v_2s_n-\frac{3}{2\theta}\log n,\qquad
\mathcal E_n=\sum_{|u|=n}\delta_{V^{(n)}(u)-m_n}.$$

Then, as $n\to\infty$, $\mathcal E_n$ converges in law for the vague
topology to a randomly shifted decorated Poisson point process

$$\mathcal E_n \;\Rightarrow\;
\mathrm{SDPPP}\bigl(C_m Z^{(1)}\,\theta e^{-\theta y}\,dy,\,
\mathcal D^{(2)}\bigr)$$

for some constant $C_m>0$, where $Z^{(1)}$ is the derivative-martingale
limit of the first-phase walk and $\mathcal D^{(2)}$ is the homogeneous
decoration of $\mathcal L_2$ at $\theta$. In particular, with
$M_n^{(n)}=\max_{|u|=n}V^{(n)}(u)$,

$$\lim_{n\to\infty}\mathbb P(M_n^{(n)}-m_n\le y)
=\mathbb E\bigl[\exp(-C_m Z^{(1)}e^{-\theta y})\bigr],
\qquad y\in\mathbb R.$$

## 1. Notation and spine setup

Write $\mathcal F_{t_n}$ for the $\sigma$-field of the first $t_n$
generations. For $|u|=t_n$ put the centred height
$a_u=V^{(n)}(u)-v_1t_n$.
Conditional on $\mathcal F_{t_n}$, the subtrees rooted at distinct $u$
are i.i.d.\ homogeneous $\mathcal L_2$-BRWs of length $s_n$ started from
$V^{(n)}(u)$, independent across $u$.

Phase-1 derivative martingale (critical tilt at $\theta$):

$$Z^{(1)}_{t_n}=\sum_{|u|=t_n}(-a_u)\,e^{\theta a_u-t_n(\theta v_1-\kappa_1(\theta))}
=\sum_{|u|=t_n}(-a_u)e^{\theta a_u},$$

since $\theta v_1=\kappa_1(\theta)$. Under the stated integrability
(Bigggins–Kyprianou / Aïdékon–Chen conditions),
$Z^{(1)}_{t_n}\to Z^{(1)}$ a.s.\ with $\mathbb E[Z^{(1)}]=\infty$-truncated
positivity: $Z^{(1)}>0$ a.s.\ on the survival event, hence a.s.\ here.

Homogeneous phase-2 centering:
$\tilde m_{s}=v_2s-\frac{3}{2\theta}\log s$.
Since $s_n/n\to1-t$,

$$m_n-v_1t_n-\tilde m_{s_n}
=-\frac{3}{2\theta}\log\frac{n}{s_n}
\;\longrightarrow\; d_t:=\frac{3}{2\theta}\log(1-t)<0.
\tag{1}$$

Write $c_n=m_n-v_1t_n-\tilde m_{s_n}\to d_t$.

## 2. Homogeneous inputs (lemmas)

We use the following standard homogeneous-BRW facts for $\mathcal L_2$
at critical $\theta$ (Aïdékon 2013 tail; Aïdékon–Berestycki–Brunet–Shi 2013
/ Madaule 2017 extremal process; Tikhomirov–Madaule ballot/localisation).

**Lemma A (tail with linear prefactor).** Let $M_s$ be the max of a
homogeneous $\mathcal L_2$-BRW of length $s$ started at $0$,
$m_s=v_2s-\frac{3}{2\theta}\log s$. There is $C_2^*>0$ such that for
$z\to\infty$ with $z=o(\sqrt s)$,
$\mathbb P(M_s-m_s>z)=(1+o(1))\,C_2^*\,z\,e^{-\theta z}$,
and the uniform upper bound
$\mathbb P_x(M_s-m_s>y)\le C(1+((y-x)\vee0))e^{-\theta(y-x)}$
holds for all $x,y,s$.

**Lemma B (cluster Laplace asymptotics).** Let
$\mathcal E_s=\sum_{|w|=s}\delta_{V(w)-\tilde m_s}$ for the homogeneous
$\mathcal L_2$-walk. For $\phi\in C_c^+(\mathbb R)$ there is a continuous
functional $\Psi(\phi)\ge0$ (the decoration functional of
$\mathcal D^{(2)}$, with
$\Psi(\phi)=C_2^*\int(1-\mathbb E e^{-\langle\mathcal D^{(2)},
\phi(\cdot+y)\rangle})\theta e^{-\theta y}dy$)
such that, uniformly for $a$ in compacts, with
$h_s(a)=1-\mathbb E[\exp(-\langle\mathcal E_s,\phi(\cdot+a-c)\rangle)]$
($c$ fixed shift),

$$h_s(a)=(1+o(1))\,\Psi(\phi)\,(-a+c')\,e^{\theta(a-c)},
\qquad s\to\infty,$$

in the regime $a\le K$ fixed; precisely what is needed is: for
$a\in[-K,K]$, $h_{s_n}(a-c_n)=(1+o(1))\Psi(\phi)e^{\theta c_n}
(-a)e^{\theta a}$ up to the harmless fixed shift, and the global bound
$h_s(a)\le C_\phi(1+(a_+-a))e^{\theta a}$.

**Lemma C (phase-1 extremes drift to $-\infty$).**
$M^{(1)}_{t_n}-v_1t_n+\frac{3}{2\theta}\log t_n$ is tight, hence
$\max_{|u|=t_n}a_u\to-\infty$ in probability (indeed a.s.).
So for every fixed $K$, eventually all $a_u\le K$ w.h.p.

**Lemma D (uniform integrability).** Under the $X(\log X)^2$ conditions,
$\{\sum_{|u|=t_n}e^{\theta a_u}\}$ is UI-adjacent and, crucially,
$\lim_{K\to\infty}\limsup_n\mathbb E[\sum_{a_u<-K}e^{\theta a_u}]=0$
after the standard truncation; deep particles are negligible in first
moment.

## 3. Laplace functional given $\mathcal F_{t_n}$

Fix $\phi\in C_c^+(\mathbb R)$, $\mathrm{supp}\,\phi\subset[-K_0,K_1]$.
Points of $\mathcal E_n$ are, for $v\ge u$ ($|u|=t_n$, $|v|=n$),
$V(v)-m_n=(V^{(u)}(w)-\tilde m_{s_n})+a_u-c_n$,
$w$ in the phase-2 subtree. Hence, conditional on $\mathcal F_{t_n}$,

$$\mathbb E[e^{-\langle\mathcal E_n,\phi\rangle}\mid\mathcal F_{t_n}]
=\prod_{|u|=t_n}\bigl(1-h_{s_n}(a_u)\bigr),
\qquad h_{s_n}(a)=1-\mathbb E e^{-\langle\mathcal E_{s_n},
\phi(\cdot+a-c_n)\rangle}.$$

Take logs. The proof reduces to

$$\sum_{|u|=t_n} h_{s_n}(a_u)
\;\xrightarrow[n\to\infty]{\mathbb P}\;
\Psi(\phi)\,e^{\theta d_t}\,Z^{(1)}
=: \Psi_m(\phi)\,Z^{(1)}.
\tag{2}$$

Indeed (2) gives
$\mathbb E e^{-\langle\mathcal E_n,\phi\rangle}
\to\mathbb E\exp(-\Psi_m(\phi)Z^{(1)})$,
the Laplace functional of
$\mathrm{SDPPP}(C_mZ^{(1)}\theta e^{-\theta y}dy,\mathcal D^{(2)})$
with $C_m=(1-t)^{3/2}C_2^*$ (see §5); $\phi\equiv0$ above level $y$
gives the max law.

## 4. Truncation: leaders and deep particles

Write $S_n=\sum_u h_{s_n}(a_u)$, split at levels $K$ and $-K$.

*High particles ($a_u>K$).* By Lemma C,
$\mathbb P(\exists u:a_u>K)\to0$ as $n\to\infty$ then $K$ fixed large?
More precisely: for fixed $K$, $\mathbb P(\max a_u>K)\to0$ since
$\max a_u\asymp -\log t_n\to-\infty$. So the $a_u>K$ block is empty w.h.p.

*Deep particles ($a_u<-K$).* Using Lemma B's global bound and that
$\phi$ is supported above $-K_0$, only $a_u$ with
$a_u-c_n\ge -K_0-K_1$-range matter; crudely
$h_{s_n}(a)\le C_\phi e^{\theta a}$ for $a\le K$. Hence

$$\mathbb E\Bigl[\sum_{a_u<-K}h_{s_n}(a_u)\Bigr]
\le C_\phi\,\mathbb E\Bigl[\sum_{a_u<-K}e^{\theta a_u}\Bigr]
\;\xrightarrow[K\to\infty]{}\;0
\quad\text{uniformly in }n,$$

by Lemma D (first-moment/UI estimate under the tilted measure; the
tilted walk has mean $v_1$ and the sum is the additive martingale tail).

*Bulk ($-K\le a_u\le K$).* Here Lemma B applies uniformly:
$h_{s_n}(a_u)=(1+o(1))\Psi(\phi)e^{\theta c_n}(-a_u)e^{\theta a_u}$
(the factor $(-a_u)$ dominates the fixed shift for large $-a_u$; on the
compact window the $o(1)$ is uniform and boundary terms vanish as the
window edge contributions are made small by first choosing $K$ large).
Therefore

$$\sum_{-K\le a_u\le K}h_{s_n}(a_u)
=(1+o(1))\Psi(\phi)e^{\theta c_n}
\sum_{-K\le a_u\le K}(-a_u)e^{\theta a_u}.$$

The truncated sum converges: as $n\to\infty$,
$\sum_{-K\le a_u\le K}(-a_u)e^{\theta a_u}\to Z^{(1)}-R_K$ in
probability, where the remainder $R_K$ (deep tail of $Z$) satisfies
$\lim_{K\to\infty}\mathbb P(|R_K|>\varepsilon)=0$ by the a.s.\
convergence $Z^{(1)}_{t_n}\to Z^{(1)}$ plus UI of the truncated
derivative martingale (Aïdékon–Chen). Sending $n\to\infty$ then
$K\to\infty$ yields (2), using $e^{\theta c_n}\to e^{\theta d_t}
=(1-t)^{3/2}$.

The $\log(1+ x)\approx x$ passage from $\prod(1-h)$ to $\exp(-\sum h)$
is justified since $\max_u h_{s_n}(a_u)\to0$ in probability
($h\le C e^{\theta K}$-bounded on bulk and bulk terms individually
$\to0$; high block empty w.h.p.).

## 5. Identification of the limit and the constant

From (2),

$$\mathbb E e^{-\langle\mathcal E_n,\phi\rangle}
\longrightarrow
\mathbb E\exp\!\bigl(-Z^{(1)}\Psi_m(\phi)\bigr),\qquad
\Psi_m(\phi)=e^{\theta d_t}\Psi(\phi).$$

With $\Psi$ from Lemma B,
$\Psi_m(\phi)=C_m\int(1-\mathbb Ee^{-\langle\mathcal D^{(2)},
\phi(\cdot+y)\rangle})\theta e^{-\theta y}dy$,
$C_m=e^{\theta d_t}C_2^*=(1-t)^{3/2}C_2^*>0$.
This is exactly the Laplace functional of
$\mathrm{SDPPP}(C_mZ^{(1)}\theta e^{-\theta y}dy,\mathcal D^{(2)})$
(see e.g.\ Maillard–Zeitouni characterisation). Taking
$\phi=\lambda\mathbf1_{[y,\infty)}$ (approximated by $C_c^+$) gives

$$\mathbb P(M_n^{(n)}-m_n\le y\mid\mathcal F_{t_n})
\to\exp(-C_mZ^{(1)}e^{-\theta y}),$$

and dominated convergence gives the announced mixture law. The shift
is carried solely by phase 1 ($Z^{(1)}$); clusters from distinct
phase-1 ancestors separate (their relative offsets $|a_u-a_{u'}|$
diverge or their phase-2 clouds are asymptotically independent given
$\mathcal F_{t_n}$), each converging to $\mathcal D^{(2)}$ — the
mean-regime phenomenon: extremes are recruited from bulk typical
ancestors, not from phase-1 leaders (who drift to $-\infty$ on the
centred scale).

## 6. Computational check (illustration, not proof)

`output/artifacts/sim_two_speed.py` simulates the binary-Gaussian case
($\mathcal L_1$: 2 children $N(0,1)$; $\mathcal L_2$: 2 children
$N(1,1)$; common $\theta^*=\sqrt{2\log2}$, $t=0.5$). Findings
(`summary.json`): $M_n-m_n$ tight (mean $\approx0.4$–$1.0$, sd
$\approx1.5$–$1.7$ across $n=8,\dots,16$); $Z^{(1)}_{t_n}>0$ in
$\ge95\%$ of trials; single-parameter Gumbel-mixture fit
$F(y)=\mathbb E\exp(-C_mZ^{(1)}e^{-\theta y})$ matches the empirical max
cdf to KS $\le0.07$ with $C_m\approx2$ stable; top-two leaves share a
phase-1 ancestor in only $15$–$28\%$ of trials (decreasing in $n$),
consistent with Poissonian (decorated) separation of extremes. This
supports — but does not substitute for — the proof above.

## References (inputs used as lemmas)

Aïdékon (2013) tail $C^*ze^{-\theta z}$; Aïdékon–Berestycki–Brunet–Shi
(2013) / Madaule (2017) homogeneous extremal process and decoration;
Bovier–Hartung (2014) variable-speed maxima and ballot method;
Aïdékon–Chen / Biggins–Kyprianou derivative-martingale convergence;
Madaule–Mallein–Zeitouni / Chen–Madaule–Mallein two-speed/mean-regime
analysis.
