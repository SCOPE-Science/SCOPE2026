# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Dimension-free joint Poincaré bound for heavy-tail entropic couplings: DISPROOF

## Target question
For symmetric Student-type laws with
$V(x)=\frac{n+\nu}{2}\log(1+|x|^2/\nu)+W(x)$, $\nu>2$, $W$ $\kappa_0$-convex
($\kappa_0\ge 0$ allowed zero), and quadratic entropic coupling $\pi_\varepsilon$,
does an explicit threshold $\nu_0(\varepsilon,\kappa_0)$, independent of $n$,
exist above which $C_P(\pi_\varepsilon)\le P(\varepsilon,\kappa_0,\nu)$ with $P$
independent of $n$? **Answer: No.** The bound fails for *every* $\nu>2$,
*every* $n\ge 1$, *every* $\varepsilon>0$ — no threshold and no finite $P$ exist.

## Theorem
Let $\mu=\nu=t_{n,\nu}$ be the centred multivariate Student-$t$ law on
$\mathbb{R}^n$ ($W\equiv 0$, admissible since $0$-convex), density proportional to
$(1+|x|^2/\nu)^{-(n+\nu)/2}$, $\nu>2$. Let $\pi_\varepsilon\in\Pi(\mu,\mu)$ be any
coupling with exact marginals $\mu$ (in particular the quadratic entropic
coupling for any $\varepsilon>0$). Then
$$C_P(\mu)=C_P(\pi_\varepsilon)=+\infty.$$
More precisely, with $\gamma=(\nu+1)/2$,
$f_R(t)=\min(\max(t,0)^\gamma,R^\gamma)$, $G_R(x,y)=f_R(x_1)$ (bounded Lipschitz
on $\mathbb{R}^{2n}$), there are explicit $0<K(\nu),\bar D(\nu)<\infty$,
independent of $n$ and $\varepsilon$, with
$$\frac{\operatorname{Var}_{\pi_\varepsilon}(G_R)}
{\int |\nabla G_R|^2\,d\pi_\varepsilon}
\ge \frac{K(\nu)}{2\bar D(\nu)}\,R \xrightarrow[R\to\infty]{}\infty.$$
Hence any claimed finite (even $n$-dependent) constant $\bar P$ is violated by
$R>2\bar D(\nu)\bar P/K(\nu)$.

## Proof
**Step 1 — Reduction to marginals.** If $\pi$ satisfies Poincaré with constant
$C$, so does each exact marginal with the same $C$: for $g$ on $\mathbb{R}^n$,
$\operatorname{Var}_\mu(g)=\operatorname{Var}_\pi(g\circ\mathrm{proj})
\le C\int|\nabla_x g|^2d\pi=C\int|\nabla g|^2d\mu$.
Thus $C_P(\pi_\varepsilon)\ge C_P(\mu)$; it suffices to kill $C_P(\mu)$.

**Step 2 — First-coordinate marginal.** Write $x=(t,y)$, $t=x_1$. Then
$$p_1(t)=Z^{-1}\int_{\mathbb{R}^{n-1}}
\Bigl(1+\frac{t^2+|y|^2}{\nu}\Bigr)^{-\frac{n+\nu}{2}}dy.$$
With $y=\sqrt{\nu+t^2}\,z$,
$p_1(t)=Z^{-1}\nu^{\frac{n+\nu}{2}}(\nu+t^2)^{-\frac{\nu+1}{2}}
\int(1+|z|^2)^{-\frac{n+\nu}{2}}dz$,
i.e. the univariate $t_\nu$ density
$p_1(t)=c_\nu(1+t^2/\nu)^{-(\nu+1)/2}$
($c_\nu>0$; exact value unneeded). It is even, so $P(X_1\le 0)=1/2$, and
$$p_1(t)\le c_\nu\min\bigl(1,\nu^{(\nu+1)/2}|t|^{-(\nu+1)}\bigr)\quad\forall t.$$

**Step 3 — Dirichlet upper bound.** $f_R$ is bounded Lipschitz,
$f_R'(t)=\gamma t^{\gamma-1}\mathbf 1_{(0,R)}$ a.e., $2\gamma-2=\nu-1$. Hence
$$E_\mu[(f_R'(X_1))^2]=\gamma^2\!\int_0^R\!t^{\nu-1}p_1(t)dt
\le \gamma^2c_\nu\Bigl(\int_0^1 t^{\nu-1}dt
+\nu^{\frac{\nu+1}{2}}\!\int_1^R t^{-2}dt\Bigr)
\le \underbrace{\gamma^2c_\nu\bigl(\nu^{-1}+\nu^{(\nu+1)/2}\bigr)}_{=:\bar D(\nu)},$$
uniformly in $R$ (used $t^{\nu-1}t^{-(\nu+1)}=t^{-2}$).

**Step 4 — Variance lower bound.** $f_R=0$ on $(-\infty,0]$,
$f_R=R^\gamma$ on $[R,\infty)$. For i.i.d. copies,
$\operatorname{Var}(f)=\tfrac12E[(f-f')^2]
\ge P_0P_1R^{2\gamma}$ with $P_0=P(X_1\le0)=1/2$,
$P_1=P(X_1\ge R)$. For $R\ge1$, on $[R,2R]$,
$1+t^2/\nu\le R^2(1+4/\nu)$ (using $1\le R^2$), so
$p_1(t)\ge c_\nu(1+4/\nu)^{-(\nu+1)/2}R^{-(\nu+1)}$ and
$$P_1\ge \underbrace{c_\nu(1+4/\nu)^{-(\nu+1)/2}}_{=:K(\nu)}R^{-\nu}.$$
Since $2\gamma-\nu=1$,
$\operatorname{Var}_\mu(f_R)\ge \tfrac{K(\nu)}2R$.

**Step 5 — Conclusion.** The ratio is $\ge K(\nu)R/(2\bar D(\nu))\to\infty$.
For $\pi_\varepsilon$, $\operatorname{Var}_{\pi_\varepsilon}(G_R)
=\operatorname{Var}_\mu(f_R)$ and
$\int|\nabla G_R|^2d\pi_\varepsilon=E_\mu[(f_R')^2]$, same ratio. Thus
$C_P(\pi_\varepsilon)=\infty$ for all $\nu>2$, $n$, $\varepsilon>0$.
Explicit witness: any $R\ge1$ with $R>2\bar D(\nu)\bar P/K(\nu)$ defeats a
claimed bound $\bar P$. E.g. $\nu=3$: ratio $\ge R/406$ roughly
($K= c_3(7/3)^{-2}$, $\bar D=4c_3(1/3+9)$), so $\bar P=10$ falls at $R\approx4061$.

**Step 6 — Admissibility.** $W\equiv0$ is $0$-uniformly convex, hence admitted
($\kappa_0=0$ allowed); $\mu$ is symmetric. Non-log-concavity:
$\nabla^2V=\frac{2a}{\nu(1+s)}I-\frac{4a}{\nu^2(1+s)^2}xx^\top$
($a=(n+\nu)/2$, $s=|x|^2/\nu$) has radial eigenvalue
$\frac{2a}{\nu}\frac{1-s}{(1+s)^2}<0$ for $|x|^2>\nu$.
The same polynomial tail $P(X_1\ge R)\ge KR^{-\nu}$ contradicts exponential
tails forced by Poincaré, so $\mu$ is not a bounded oscillation of any
uniformly convex potential either (Bakry–Émery + Holley–Stroock would give
Poincaré). In particular the target's parenthetical premise ("each marginal
satisfies Poincaré") is false for $W=0$, and the proposed $\Gamma$-calculus
route — which needs finite marginal + conditional Poincaré inputs — has no
valid marginal input. The failure occurs at *every* $\nu>2$, not only as
$\nu\to2$: the "threshold" cannot exist.

## Numerical confirmation (`output/artifacts/witness_check.py`, numpy only)
Univariate-$t_3$ quadrature with $\beta=(2\nu+1)/4$:
$R=5,20,100,1000$ give Var/Dir $\approx 2.7, 9.0, 26.0, 93.5$ (growing);
Monte-Carlo in the marginal direction ($n=5$, $4\times10^5$ draws) gives
$2.7, 9.3, 26.7$ at $R=5,20,100$, matching quadrature. Hessian radial
eigenvalues at $r^2=0.5,2.9,3.0,3.1,20$ ($n=5,\nu=3$):
$+1.63,+0.023,0,-0.0215,-0.257$, confirming sign change (non-log-concavity).

## Remarks
The argument uses only that $\pi_\varepsilon$ is a genuine coupling (exact
marginals), hence covers every $\varepsilon>0$ and the unregularized case.
The constants $K,\bar D$ depend only on $\nu$ (via elementary bounds), never
on $n$: the violation is already visible in one fixed coordinate direction.
