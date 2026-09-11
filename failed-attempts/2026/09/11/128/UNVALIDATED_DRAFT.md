# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Single-mode BGK DMS ledger at unit wavevector — DRAFT (self-contained)

## Claim

Fix the 2pi torus $T^3=(\mathbb R/2\pi\mathbb Z)^3$ and Fourier mode $k=e_1$,
$|k|=1$. Let $\mu(v)=(2\pi)^{-3/2}e^{-|v|^2/2}$,
$H=L^2(\mu\,dv)$ fiber, $Vh=v_1h$ (so fiber transport is $T=ikV=iV$),
$\Pi$ the $L^2(\mu)$-orthogonal projection onto
$\mathrm{span}\{\phi_0,\phi_1,\phi_2,\phi_3,\phi_4\}$ with
$\phi_0=1$, $\phi_i=v_i$, $\phi_4=(|v|^2-3)/\sqrt6$,
and BGK collision $L=\Pi-I$ (so $-L=(I-\Pi)$, gap $1$ on micro).
With the DMS operator
$$A=(I+(T\Pi)^*(T\Pi))^{-1}(T\Pi)^*,\qquad B=(I+S)^{-1},\ S=\Pi T^*T\Pi,$$
and twisting $\varepsilon=1/8$, the functional
$H_k[h]=\|h\|^2+\varepsilon\,\mathrm{Re}\langle Ah,h\rangle$ satisfies,
for all complex fiber data $h$ (no global-mean restriction needed at fixed
nonzero mode):
$$0.9\|h\|^2\le H_k[h]\le 1.1\|h\|^2,\qquad
\frac{d}{dt}H_k[S_k(t)h]\le -\frac1{120}\,\|(I-\Pi)h\|^2,$$
where $S_k$ is the fiber semigroup of $L-T$.
The proved micro strength is $-1/60$ on $\|(I-\Pi)h\|^2$ minus certified
positive macro/cross remainders, hence $1/120$ holds with slack.

## Proof

**Step 1 — Exact fiber matrices.** All overlaps are integer moments of
$N(0,I_3)$. With $F_{ab}=\langle\phi_a,V\phi_b\rangle$,
$S_{ab}=\langle\phi_a,V^2\phi_b\rangle$:
$$F=\begin{pmatrix}0&1&0&0&0\\1&0&0&0&\sqrt{2/3}\\
0&0&0&0&0\\0&0&0&0&0\\0&\sqrt{2/3}&0&0&0\end{pmatrix},
\quad S=\begin{pmatrix}1&0&0&0&\sqrt{2/3}\\0&3&0&0&0\\
0&0&1&0&0\\0&0&0&1&0\\\sqrt{2/3}&0&0&0&7/3\end{pmatrix}.$$
$P=S-F^2$ has spectrum $\{0,1,1,4/3,5/3\}$, so with
$q(m)=\Pi(Vm)$, $\|q\|^2\le \frac53\|m\|^2$.
$\|A\|\le 1/2$ (AM–GM on $\sqrt{\lambda}/(1+\lambda)$), $\|TA\|\le1$
(DMS lemma); hence $|\varepsilon\mathrm{Re}\langle Ah,h\rangle|
\le\frac1{16}\|h\|^2$, i.e. equivalence in $[0.9375,1.0625]\subset[0.9,1.1]$.
$R_{mm}=\hat E M^{-1}\hat E-M^{-1}S$ (macro–macro block) is negative
definite (eigenvalues $-0.514,-0.5,-0.5,-0.194,-0.180$); the transverse
modes $a=2,3$ decouple with margin $-1/2$.

**Step 2 — Finite-rank reduction.** Write $h=M+m$, $M=\Pi h$, $m=(I-\Pi)h$.
Since $T=iV$ and $A$ are built from $\Pi,V$, every micro dependence of
$D=\frac{dH_k}{dt}$-defect enters through the 9-vector
$z=(q,r)$, $q_a=\langle u_a,m\rangle$ ($a=1..4$, $u_a=(I-\Pi)V\phi_a$),
$r_a=\langle w_a,m\rangle$ ($w_a=(I-\Pi)V^2\phi_a$), with exact-moment
joint Gram $J\succeq0$ (9x9) and constraint $z^*J^{-1}z\le\|m\|^2$.
Put $z=J^{1/2}y$; then $\|m\|^2\ge|y|^2$ controls everything.

**Step 3 — Complex-field LMI.** Splitting $h=u+iv$ (real operators),
$G=D-\kappa H$-defect ($\kappa=1/120$) is the stacked form
$[[G_d,K],[K^*,G_d]]$ on $(M,y)_u\oplus(M,y)_v$ (28x28), with
$K$ ($\|K\|\approx0.033$) the skew $D$-term plus $\kappa H$-cross block.
All blocks are explicit rational/monomial functions of $F,S,B,J^{1/2}$
above. The certificate matrix $G_{28}$ has float minimum eigenvalue
$0.00779$; with float eigvec matrix $V$, $S=V^*G_{28}V$ has off-diagonal
radii $\sim10^{-15}$ and orthogonality error $\sim10^{-15}$, certifying
$\lambda_{\min}(G_{28})\ge 0.007787>0$. Hence $G\ge0$, i.e. the claimed
differential inequality, for all complex $h$. The $1/120$ is not sharp:
the margin $0.0078$ is $\approx 65\%$ of $\kappa$.

## What this does and does not show

Proves the full per-mode DMS ledger (equivalence + dissipation) for the
BGK fiber at $k=e_1$ with the admitted pair $(1/8,1/120)$.
It does NOT prove the cutoff hard-sphere target: the only
session-available explicit HS gap (Baranger–Mouhot, $\ge0.0281$) leaves a
$12\times$ micro-budget shortfall against the $\varepsilon=1/8$ cross
terms, and HS needs weighted $\nu$-moment $AL$ bounds with no
session-available explicit constants (crude caps fail by $10^1$–$10^2$).

## Reproduction

`output/artifacts/verify_bgk_complex_lmi.py` rebuilds $F,S,B,J$ from exact
Gaussian moments, assembles $G_{28}$, prints min-eig $0.00779$ and the
orthogonality-residual certificate. `Gmat_bgk_complex.csv` is the matrix.
stdlib+numpy only.
