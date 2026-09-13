# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A first-order versus finite rigid-foldability gap in a generic flat-foldable degree-8 vertex

## 1. Result

**Theorem.** There exists a generic flat-foldable degree-8 single-vertex crease pattern and a
combinatorially flat-foldable mountain--valley assignment with $|M-V|=2$ that is first-order
flexibly rigid-foldable but admits no finite continuous rigid folding motion from the flat
state. Concretely:

- Sector angles (cyclic order, radians)
  $$\theta=(0.62,\ 0.97,\ 0.58,\ 1.02,\ 0.71,\ 0.88,\ 1.231592653589793,\ 0.27159265358979295),$$
  with $\sum\theta_k=2\pi$ and alternating sum $0$.
- Assignment $s=(--+++++-)$: creases $3,4,5,6,7$ mountain; $1,2,8$ valley.
- Infinitesimal rigid folding velocity (unit vector, $Jr=0$, signs $s$)
  $$r\approx(-0.099719,-0.099719,0.637618,0.099719,0.099719,0.099719,0.730603,-0.099719).$$
- No $C^1$ path $\rho(t)\to0$, $\rho(t)\ne0$, with all fold angles nonzero of signs $s$,
  satisfies exact rigid closure for $0<|\rho(t)|<2\delta_z$ with $\delta_z=8.4\times10^{-4}$.

So the first alternative of the admitted dichotomy holds: a second-order-locked gap witness exists.

## 2. Model and notation

Parametrize folded states near the flat state by fold angles $\rho\in\mathbb R^8$.
With $Z(\cdot)$ rotation about $z$ and $X(\cdot)$ rotation about $x$, the vertex closure is
$$F(\rho)=A_1(\rho_1)\cdots A_8(\rho_8),\qquad A_k(\rho_k)=Z(\theta_k)X(\rho_k).$$
Rigid foldability is $F(\rho)=I$. Write $f(\rho)\in\mathbb R^3$ for the rotation vector of
$F(\rho)$ (so $f(\rho)=0\iff F(\rho)=I$ near $0$), split as $f=(G_1,g_2)$ with $G_1$ the two
in-plane components and $g_2$ the out-of-plane scalar $(\,F_{21}-F_{12}\,)/2$.

Let $a_k=\theta_1+\cdots+\theta_k$ be the crease-axis directions in the flat state.
A generator computation gives the rigidity Jacobian and the true Hessian of $g_2$:

- $Df(0)$ has columns $(\cos a_k,\sin a_k,0)$; i.e. with the $2\times8$ matrix
  $J_{jk}=(\cos a_k,\sin a_k)$, the linearized in-plane constraint is $Jw=0$.
- $g_2$ has vanishing linear part; its Hessian is $B$ with $B_{kk}=0$ and, for $k<l$,
  $$B_{k\ell}=\tfrac14\sin(a_\ell-a_k)\quad\text{(symmetric extension).}$$
  The associated quadratic obstruction is $Q(w)=w'Bw$.
- The in-plane quadratic part vanishes identically (Lemma 4 below).

The derivation is as follows. Write $J_x,J_y,J_z$ for the infinitesimal rotation generators.
$A_k(0)=Z(\theta_k)$ and $F(0)=Z(\sum\theta_k)=Z(2\pi)=I$. Moreover
$$\frac{\partial F}{\partial\rho_k}(0)=(Z_1\cdots Z_k)J_x(Z_1\cdots Z_k)^{-1}
=:X_k=[u_k\times],\qquad u_k=(\cos a_k,\sin a_k,0).$$
Hence the Jacobian columns are the in-plane axes above. For the second order, with
$F=I+hL_1+h^2L_2+\cdots$ along $\rho=hw$,
$$L_2=\sum_{k<\ell}w_kw_\ell X_kX_\ell+\text{(block-diagonal symmetric terms)}.$$
Now $[u_k\times][u_\ell\times]=u_\ell u_k^T-(u_k\!\cdot\! u_\ell)I$, whose skew part is
$\tfrac12(u_\ell u_k^T-u_ku_\ell^T)=-\tfrac12[(u_k\times u_\ell)\times]$, and
$u_k\times u_\ell=\sin(a_\ell-a_k)e_z$. The diagonal second derivatives vanish exactly:
$F(te_k)=C_kX(t)C_k^{-1}$ is a rotation about the in-plane axis $u_k$, so its rotation
vector is $\sin(t)u_k$, exactly in-plane; thus $g_2(te_k)\equiv0$ and $B_{kk}=0$.
The pairwise fits of Section 5 confirm $c_{k\ell}=+\sin(a_\ell-a_k)/2$ for
$g_2(h(e_k+e_\ell))/h^2=2B_{k\ell}$, i.e. $B_{k\ell}=\sin(a_\ell-a_k)/4$ for $k<\ell$.

**Remark on normalization.** An early notebook stencil
$(g_{++}-g_{+-}-g_{-+}+g_{--})/4h^2$ equals $2B_{k\ell}$, not $B_{k\ell}$; survey code that
compared against $S_{k\ell}=\sin(a_\ell-a_k)/2$ therefore tabulated $2Q$. Signs and uniformity
are unaffected; the certified value below uses the corrected $B$ and direct path fits.

## 3. Certificate data (machine-verified, interval arithmetic)

All claims below are verified by the self-contained interval-arithmetic script
`certify.py`/`assemble_cert.py`/`qfix.py` (no external dependencies), with results stored in
`output/artifacts/certificate.json`:

1. **Rank.** $J$ has rank $2$: the $2\times2$ minor on columns $(0,1)$ lies in
   $[0.8248857133384452,\,0.8248857133384551]\not\ni0$. Hence $\ker J$ is $6$-dimensional.
2. **Cone = ray.** For the closed sign cone $C=\{w:Jw=0,\ s_iw_i\ge0\}$ with $s=(--+++++-)$:
   the section $\{w\in C:\sum s_iw_i=1\}$ (equivalently $s_iw_i=1$ vertex enumeration over all
   $\binom 86=28$ six-active-bound systems) has exactly one feasible vertex
   ($w^\star\approx(-1,-1,6.394,1,1,1,7.327,-1)$, $\det=-0.6442\ne0$), and every one of the $8$
   facet sections $\{w\in C:w_f=0\}$ (capped polytope, $35+21$ systems each) is $\{0\}$.
   Every interval pivot excluded $0$ (smallest $|\det|$ is $0.048$ for section systems and
   $0.0083$ for facet systems, versus interval widths $\sim10^{-14}$). Hence
   $C=\mathbb R_+\{r\}$ with $r$ above, and $s_ir_i\ge0.0997>0$ strictly.
3. **Obstruction value.** Point-interval evaluation of the corrected form gives
   $$Q(r)\in[0.025585331905838633,\ 0.02558533190586059],\qquad m:=0.0255853319>0.$$
   (Direct path fit: $g_2(hr)/h^2\to0.0255853$, stable over $h\in[2.5\times10^{-3},2\times10^{-2}]$.)
4. **Genericity.** $\theta_k\in(0,\pi)$, pairwise distinct (min gap $0.04$), no two consecutive
   summing to $\pi$ (margin $\ge1.03$), $\sum\theta_k=2\pi$ and alternating sum $0$ (intervals
   of width $<10^{-13}$), crease axes distinct mod $\pi$ (min distance $0.0484$). The proof uses
   only these listed open conditions plus strict inequalities, so it persists on an open
   neighborhood in angle space, which contains fully generic points.

## 4. No-branch proof (Lyapunov--Schmidt with explicit constants)

Write $\rho=Py+Nz$ with $P=J^T(JJ^T)^{-1}$ ($8\times2$ right inverse, $|P|_2=0.5335$) and $N$ a
null basis ($8\times6$). The in-plane equation is
$$G_1(y,z)=y+R_1(y,z)=0,$$
with no linear term in $z$ and no quadratic term in $z$ (Lemma: in-plane Hessian is zero).
The remainder bounds use the rotation-geometry lemma: every partial derivative of $F$ inserts a
unit-norm generator into a product of rotations, so with $s_1=\sum|\rho_i|\le\sqrt8\,|\rho|$,
$$|R_1|\le C|\rho|^3,\qquad |R_2|\le C|\rho|^3,\qquad C=\tfrac{8\sqrt2}{3}<3.78,$$
for the in-plane and out-of-plane remainders. The constant was cross-checked numerically:
directional third derivatives satisfy $\max|d^3f_c|\le5.64\ll22.6=(\sqrt8)^3$ over $60$ random
directions, and the in-plane symmetrized second derivatives vanish to solver precision.

Fixed point: for $|\rho|\le r_0=0.249$ (with an extra safety halving),
$|y|\le C|\rho|^3$ and hence $|\rho|\le2|z|$. Sign consistency: $Nz/\,|z|\to r$ while
$|Py|\le8pC|z|^3$ with $\min s_ir_i=0.0997$, so for $|z|\le r_1=0.0031$ the null component $Nz$
(and hence $\rho$) carries the strict signs $s$, i.e. $z/|z|$ lies in the cone $C=\mathbb R_+r$
and $Q(z)\ge m|z|^2$. Therefore
$$g_2(\rho)\ \ge\ m|z|^2-8C|z|^3\ >\ 0\qquad\text{for }0<|z|<\frac{m}{8C}=8.46\times10^{-4}.$$
So $g_2$ cannot vanish on any sign-$s$ path with $0<|\rho|<2\delta_z$, $\delta_z=m/8C$.
This covers all $C^1$ motions including higher-order tangencies: by compactness,
$\rho(t)/|\rho(t)|$ has a subsequential limit $d\ne0$ in the closed cone, hence $d$ is a positive
multiple of $r$, and $g_2/|\rho|^2\to Q(d)>0$, contradicting $g_2\equiv0$ along a motion.

Since $Jr=0$ with strict signs $s$, the assignment is first-order flexibly rigid-foldable;
since no finite branch exists, it is a genuine second-order-locked gap witness. This proves the
first alternative of the target dichotomy.

## 5. Computational survey (context, not part of the proof)

- Exact vertex-enumeration LP over all $56$ assignments with $|M-V|=2$ (5 mountains): $52$ are
  first-order feasible.
- Complete extreme-ray enumeration of every full cone $\{Jw=0,s\cdot w\ge0\}$ (all
  $\binom85+\binom86$ active-bound systems; completeness holds because every $5$-combo system
  has full rank $7$): cones range from rays to $62$ extreme rays.
- The obstruction $Q$ (corrected normalization) is sign-uniform exactly on the certified ray
  cone above (plus heuristic interior-uniformity signals on several multi-ray cones, not claimed).
- The obstruction analysis initially used the doubled form $2Q$ due to the stencil factor in
  Section 2's remark; this was caught by the direct path fit ($0.0255853=Q(r)$ vs tabulated
  $0.0512$) and corrected before certification. The certificate and gap radius use the true $B$.

## 6. Limitations and uncertainty

- The "no further algebraic relation" part of genericity is handled by openness: the certificate
  is stable under small perturbations, so fully generic angle vectors nearby inherit the witness;
  the exhibited decimals themselves satisfy every listed genericity clause.
- The remainder constant $C=8\sqrt2/3$ is an analytic operator-norm bound (Lemma in Section 4);
  numerics suggest it is loose by a factor $\approx4$, so the gap radius $8.4\times10^{-4}$ is
  conservative.
- The interval arithmetic (`I`, `isin`/`icos` with Taylor order $25$ and Lipschitz widening) is
  implemented from scratch in `certify.py`; all pivot-nondegeneracy assertions passed, and
  interval widths at the solution are $\sim10^{-12}$, versus the certified margins
  ($Q\ge0.0256$, sign margin $0.0997$).

## 7. Reproduction

```
python3 assemble_cert.py   # section uniqueness + facet-kill (interval)
python3 qfix.py            # corrected symmetric Q interval [0.025585331905838633, ...86059]
python3 gapradius.py       # explicit constants and gap radius 8.4e-4
python3 verifyM3.py        # third-derivative and in-plane-quadratic checks
```
Artifacts: `output/artifacts/certificate.json` (interval certificate),
`output/artifacts/fullcone.pkl` (extreme rays of all 52 feasible cones),
`output/artifacts/theta.npy`, `output/artifacts/Bsym.npy` (raw doubled-Hessian table; divide by 2).
