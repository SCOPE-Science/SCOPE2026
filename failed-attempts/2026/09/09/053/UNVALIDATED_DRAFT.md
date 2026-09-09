# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Section covariance bound for the isotropic cross-polytope along Eldan localization

## Claim (fallback: exact statement)

Let $K=B_1^n$ in isotropic position with $n\ge 4$ even, $\mu$ the uniform
probability on $K$, and $(\mu_t)_{t\ge 0}$ Eldan stochastic localization
with identity driving matrix ($C_t\equiv I$). For every 2-dimensional
coordinate section $E=\mathrm{span}\{e_i,e_j\}$ ($i<j$),

$$\sup_{t\ge 0}\mathbb E\,\|\mathrm{Cov}(\mu_t|_E)\|_{\mathrm{op}}
  \le 8\,L_K^2,$$

where $L_K$ is the isotropic constant of $K$. In fact the proof gives
$2L_K^2$.

## Preliminaries (checked, not original)

1. **Eldan $C_t\equiv I$ setup** (Eldan 2013, eqs. (4)--(5) and Lemma 2).
   With $a_t=\mathrm{bary}(\mu_t)$, $A_t=\mathrm{Cov}(\mu_t)$,
   $$da_t = A_t\,dW_t,\qquad dA_t = -A_t^2\,dt + M^{(3)}_t\,dW_t,$$
   where the drift $-A_t^2\,dt$ is the finite-variation part and
   $M^{(3)}_t\,dW_t$ is a matrix-valued martingale built from third
   cumulants. This is the $C_t=I$ case of Eldan's general SDE; only the
   drift part and the martingale property (zero mean increment) are used.
2. **Positivity.** Each $A_t\succeq 0$ a.s.; principal submatrices of PSD
   matrices are PSD; hence with $P_E$ the coordinate projection,
   $S_t:=\mathrm{Cov}(\mu_t|_E)=P_EA_tP_E^\top\succeq 0$ a.s.
3. **Operator norm vs trace.** For $M\succeq 0$, $\|M\|_{\mathrm{op}}
   \le\mathrm{Tr}(M)$.
4. **Unconditional symmetry is used only at $t=0$.** By coordinate
   symmetries of $B_1^n$, $\mathrm{Cov}(\mu_0)$ is a multiple of $I$;
   in isotropic position $\mathrm{Cov}(\mu_0)=L_K^2I_n$, so
   $S_0=L_K^2I_2$ and $\mathrm{Tr}(S_0)=2L_K^2$.

## Lemma (expected-covariance decay; the localization step)

$$\mathbb E[A_t]\preceq A_0\qquad\forall\,t\ge 0,$$
i.e. $t\mapsto\mathbb E[A_t]$ is nonincreasing in PSD order.

*Proof via the law of total covariance (self-contained; no third-moment
drift needed).* In Eldan's construction with $C_t\equiv I$, the
localization posterior satisfies $\mu_t=\mathrm{Law}(X\mid\mathcal F_t)$
for $X\sim\mu_0=\mu$, with $a_t=\mathbb E[X\mid\mathcal F_t]$ and
$A_t=\mathrm{Cov}(X\mid\mathcal F_t)$ (Eldan 2013, Section 2: the tilt
$\theta_t$ generates $\mathcal F_t$ and $\mu_{t,\theta}$ is the Bayesian
posterior). Since $\mu$ is compactly supported, $\mathbb E|X|^2<\infty$.
The law of total covariance gives, entrywise by linearity / tower property,
$$\mathrm{Cov}(X)=\mathbb E[\mathrm{Cov}(X\mid\mathcal F_t)]
  +\mathrm{Cov}(\mathbb E[X\mid\mathcal F_t]),$$
i.e. $A_0=\mathbb E[A_t]+\mathrm{Cov}(a_t)$. As $\mathrm{Cov}(a_t)\succeq 0$,
$$\mathbb E[A_t]=A_0-\mathrm{Cov}(a_t)\preceq A_0.$$
Equivalently, $d\mathbb E[a_ta_t^\top]/dt=\mathbb E[A_t^2]$ via It\^o isometry
from $da_t=A_t\,dW_t$ is the differential form of the same identity; we use
only the integrated covariance decomposition, which needs no integrability
beyond $\mathbb E|X|^2<\infty$. ∎

## Theorem (section bound, constant 2 hence 8)

For every coordinate pair $i<j$ and every $t\ge 0$,
$$\mathbb E\,\|S_t\|_{\mathrm{op}}\le 2L_K^2\le 8L_K^2.$$

*Proof.* Chain of inequalities, each justified:
$$\mathbb E\|S_t\|_{\mathrm{op}}
  \overset{(a)}{\le} \mathbb E\,\mathrm{Tr}(S_t)
  \overset{(b)}{=} \mathrm{Tr}(\mathbb E[S_t])
  \overset{(c)}{\le} \mathrm{Tr}(S_0)
  = 2L_K^2.$$
(a) pointwise PSD fact $\|\cdot\|_{\mathrm{op}}\le\mathrm{Tr}(\cdot)$
on $S_t\succeq 0$, then monotonicity of expectation;
(b) linearity of expectation and trace (finite-dimensional);
(c) compress the Lemma: $S_t=P_EA_tP_E^\top$,
$\mathbb E[S_t]=P_E\mathbb E[A_t]P_E^\top\preceq P_EA_0P_E^\top=S_0$,
and $X\preceq Y\Rightarrow\mathrm{Tr}(X)\le\mathrm{Tr}(Y)$.
At $t=0$, $\mathrm{Tr}(S_0)=2L_K^2$ by the unconditional-symmetry
normalization above. The bound is uniform in $t$ and in the pair
$(i,j)$ by coordinate symmetry. Since $2\le 8$, the claimed constant 8
holds with slack factor 4. ∎

*Scope check.* $n\ge 4$ even is assumed as stated; the argument uses no
upper bound on $n$ and no parity beyond the hypothesis. The constant is
explicit (2 proved, 8 claimed). All pairs $i<j$ are covered identically.

## What this does and does not show

- Proves the exact fallback inequality (uniform-in-time expected
  section-covariance bound, constant 8) for the isotropic cross-polytope.
- Does NOT prove the full dimension-free KLS bound (target): it is the
  $t=0$-anchored localization-to-covariance base-case lemma the target
  route needs, with transfer value to Orlicz-ball attackers as stated in
  the admission record. No claim is made about $\psi_K\ge c(A)$.
- Numerical replay (`output/artifacts/fallback_corroborate.py`, stdlib
  only, lgamma-stable) corroborates the $t=0$ anchor
  ($\sigma^2=2/((n+1)(n+2))$, $L_K^2=V^{-2/n}\sigma^2$,
  section op-norm $=L_K^2$) and the PSD lemma on 5000 random witnesses;
  it does not substitute for the proof above.

## Statement-level prior comparison (no recomputation)

- Eldan 2013: general thin-shell$\Rightarrow$spectral-gap transfer with
  polylog loss; no named-body section estimate.
- Chen--Eldan annealing: reduction to truncated Gaussians, not
  cross-polytope sections.
- Cattiaux--Guillin 2018: unconditional Poincar\'e $O(\log^2 n)$, no
  localization-trajectory bound.
- Klartag 2023 / Klartag--Lehec 2024: general $\sqrt{\log n}$ KLS and
  slicing resolution; neither states a uniform-in-time covariance bound
  for $B_1^n$ coordinate sections.
