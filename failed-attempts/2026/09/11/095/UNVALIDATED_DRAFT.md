# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Calibration rigidity at θ=π/4: explicit slicing competitor with certified area defect

## 1. Setup

Let $c=s=\sqrt2/2$, $u=1-c$, $\delta_0=\sqrt{2-2c}=\sqrt{2-\sqrt2}\approx0.7654$.
In $\mathbb R^4$ with standard basis $e_1,\dots,e_4$ put

$$P_0=\operatorname{span}(e_1,e_2),\qquad
P_1=\operatorname{span}(ce_1+se_3,\;ce_2+se_4).$$

Both are 2-planes through the origin; $P_1$ is the diagonal graph rotation of
$P_0$ by $\pi/4$. Its principal angles with $P_0$ are $(\pi/4,\pi/4)$.
(The single-rotation normalization $\operatorname{span}(ce_1+se_3,e_2)$
satisfies the same pointwise estimates below, so the proof covers it too.)
Let $C=P_0\cup P_1$ and $B^4$ be the closed unit ball.
$C\cap B^4$ is two unit discs, so with $\mathcal H^2$ area,

$$\mathcal H^2(C\cap B^4)=2\pi\approx6.283.$$

**Theorem (competitor disjunct of the target).**
There is an explicit compact Lipschitz 2-chain $S\subset B^4$ with the same
boundary link as $C\cap B^4$ (the two outer unit circles) satisfying

$$\mathcal H^2(C\cap B^4)-\mathcal H^2(S)\ge 0.351>0.02.$$

Hence the target disjunction is decided on the competitor side, with all
constants recomputable from the ledger below.

## 2. Competitor: drilled discs plus ruled bridge

Fix $\rho=1/2$. Let

$$A_0=\{x\in P_0:\rho\le|x|\le1\},\qquad
A_1=\{x\in P_1:\rho\le|x|\le1\}$$

be the two outer annuli (total area $2\pi(1-\rho^2)$).
Let $a(t)=\rho(\cos t,\sin t,0,0)\in P_0$ and
$b(t)=\rho(c\cos t,c\sin t,s\cos t,s\sin t)\in P_1$ be the phase-aligned
inner circles of radius $\rho$, and

$$F(t,\lambda)=(1-\lambda)a(t)+\lambda b(t),\qquad
(t,\lambda)\in S^1\times[0,1],$$

$$B=F(S^1\times[0,1]),\qquad S=A_0\cup A_1\cup B.$$

Write $R(\lambda)=\rho(1-\lambda u)$, $S(\lambda)=\rho\lambda s$ and
$\omega(t)=(\cos t,\sin t)$. Then

$$F(t,\lambda)=(R(\lambda)\omega(t),\,S(\lambda)\omega(t)).\tag{1}$$

### 2a. Containment in the unit ball

Since $s=c$ and $2c^2=1$,

$$u^2+s^2=(1-c)^2+c^2=1-2c+2c^2=2-2c=2u.\tag{2}$$

Hence

$$R(\lambda)^2+S(\lambda)^2
=\rho^2\big[(1-\lambda u)^2+\lambda^2s^2\big]
=\rho^2\big[1-2\lambda u+2\lambda^2u\big]
=\rho^2\big[1-2\lambda u(1-\lambda)\big]\le\rho^2\le1.$$

So $B\subset B^4$; $A_0,A_1\subset B^4$; thus $S\subset B^4$.

### 2b. Area of the bridge

From (1),

$$\partial_tF=\rho(-R\sin t,R\cos t,-S\sin t,S\cos t)/\rho\text{-scaled},$$

i.e. $|\partial_tF|^2=R^2+S^2\le\rho^2$ by §2a, and

$$\partial_\lambda F=\rho(-u\cos t,-u\sin t,s\cos t,s\sin t),$$

so by (2), $|\partial_\lambda F|^2=\rho^2(u^2+s^2)=\rho^2\cdot2u=\rho^2\delta_0^2$.
The area integrand satisfies pointwise $|\partial_tF\wedge\partial_\lambda F|
\le|\partial_tF|\,|\partial_\lambda F|\le\rho^2\delta_0$. By Fubini,

$$\mathcal H^2(B)\le\int_0^{2\pi}\!\!\int_0^1\rho^2\delta_0\,d\lambda\,dt
=2\pi\delta_0\rho^2.\tag{3}$$

$F$ is smooth, so (3) is an ordinary integral estimate; no GMT beyond the
elementary wedge inequality is used.

### 2c. Embeddedness and boundary

$R(\lambda)=\rho(1-\lambda u)$ is strictly decreasing ($R>0$) and
$S(\lambda)=\rho\lambda s$ strictly increasing. If
$F(t,\lambda)=F(t',\lambda')$ then $(R,S)=(R',S')$ by taking norms of the two
$\mathbb R^2$ blocks, so $\lambda=\lambda'$, and then $\omega(t)=\omega(t')$
since $R>0$, so $t=t'\bmod2\pi$. Thus $F$ is injective on the compact
$S^1\times[0,1]$, hence an embedding; $B$ is an embedded annulus meeting
$A_0,A_1$ exactly along the inner circles. $S$ is a compact Lipschitz
2-chain with boundary the two outer unit circles — the same link as
$C\cap B^4$. The interior gluing circles carry no area.

## 3. Defect ledger (integer arithmetic only)

Net saving over the cone:

$$\Delta:=\mathcal H^2(C\cap B^4)-\mathcal H^2(S)
\ge 2\pi\rho^2-2\pi\delta_0\rho^2
=2\pi(1-\delta_0)\rho^2
=\frac{\pi}{2}(1-\delta_0).\tag{4}$$

Bound $\delta_0$: $14142^2=199996164<2\cdot10^8<200024449=14143^2$, so
$1.4142<\sqrt2<1.4143$ and $\delta_0^2=2-\sqrt2<2-1.4142=0.5858$.
Since $0.5858\cdot10^{10}=5858000000<5867560000=766^2\cdot10^4$,
$0.5858<0.766^2$, hence

$$\delta_0<0.766.$$

Bound $\pi$: the inscribed regular hexagon has perimeter $6<2\pi$, so
$\pi>3$. From (4),

$$\Delta>\frac{3}{2}(1-0.766)=\frac32\cdot0.234=0.351>0.02.$$

True value $\Delta\approx(\pi/2)(1-0.76537)\approx0.369$; the certificate
uses only the rational bounds above. Margin over the $0.02$ threshold: $17\times$.
Replay: `python3 output/artifacts/verify_defect.py` → `VERIFY_OK`.

## 4. Remarks

The Lawlor–Nance angle theorem (characterizing-angle sum $\pi/2<\pi$ here)
predicts $C$ is not minimizing, motivating the competitor side; the proof
above is self-contained and does not invoke it. No calibration is claimed.
The radius $\rho=1/2$ is not optimized; any $\rho\in(0,1)$ gives a defect
$2\pi(1-\delta_0)\rho^2$. No claim is made about adjacent angles, the full
Lawlor–Nance boundary, or uniqueness of tangent cones.
