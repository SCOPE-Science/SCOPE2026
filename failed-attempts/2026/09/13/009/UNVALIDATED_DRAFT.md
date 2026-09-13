# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Bessel–Legendre ADT improvement on the Yan–Ozbay delay benchmark

## 1. Benchmark (exact data, verified against the paper PDF)

Yan–Ozbay, SICON 47(2):936–949, 2008, §5. Two modes, $n=2$,
constant heterogeneous delays $h_1=0.3$, $h_2=0.6$:

$$A_1=\begin{pmatrix}-2&0\\0&-0.9\end{pmatrix},\quad
\bar A_1=\begin{pmatrix}-1&0\\-0.5&-1\end{pmatrix},\qquad
A_2=\begin{pmatrix}-1&0.5\\0&-1\end{pmatrix},\quad
\bar A_2=\begin{pmatrix}-1&0\\0.1&-1\end{pmatrix}.$$

Prior bound (delay-dependent Razumikhin, Thm. 3.5): with
$\lambda=1.7224$, $\mu_d=1.5216$, $\bar p=1.4$,
$T_d^\*=5.3147$, hence minimum dwell time

$$\tau_D^d = 6.5147,$$

guaranteeing only **asymptotic** (not exponential) stability.
Because a minimum-dwell guarantee is an average-dwell guarantee
with chatter bound $N_0=1$, any certified $\tau_a<6.5147$ is a
strict improvement. The delay sums $A_i+\bar A_i$ have spectra
$\{-1.9,-3.0\}$ and $\{-1.776,-2.224\}$: strongly Hurwitz, so an
exponential LKF certificate with rate $a>0$ is structurally expected.

## 2. Functional class (fixed augmented class of the target)

Common (single) Lyapunov–Krasovskii functional on the common window
$H=\max h_i=0.6$, with exponential weight $e^{2a(s-t)}$, $a=0.3$,
and Legendre-coefficient augmentation of order $N=2$:

$$V(x_t)=\eta(t)^\top P\,\eta(t)
+\int_{t-H}^{t}e^{2a(s-t)}x(s)^\top Qx(s)\,ds
+H\int_{-H}^{0}\!\!\int_{t+\theta}^{t}
e^{2a(s-t)}\dot x(s)^\top R\dot x(s)\,ds\,d\theta,$$

$$\eta(t)=\begin{pmatrix}x(t)\\ v_1(t)\\ v_2(t)\end{pmatrix},
\ v_1=\tfrac1H\!\int_{t-H}^{t}\!x,\ \
v_2=\tfrac1{H^2}\!\int_{-H}^{0}\!\!\int_{t+\theta}^{t}\!x,$$
$P\in\mathbb S^{6}_{++}$, $Q=qI_2$, $R=rI_2$, $q,r>0$.

## 3. Second-order canonical Bessel–Legendre inequality (used, not assumed)

On $[t-H,t]$ with coordinate $u=(s-(t-H))/H\in[0,1]$ and the shifted
Legendre polynomials $\ell_0=1$, $\ell_1=2u-1$, $\ell_2=6u^2-6u+1$
(orthogonal with $\int_0^1\ell_k^2=1/(2k+1)$), Bessel's inequality for
$\dot x$ in $L^2_{R}$ gives, with
$\chi_k=\int_{t-H}^t\ell_k\, \dot x$ — i.e.
$\chi_0=x(t)-x(t-H)$, $\chi_1=x(t)+x(t-H)-2v_1$,
$\chi_2=x(t)-x(t-H)+6v_1-12v_2$:

$$H\!\int_{t-H}^{t}\!\dot x^\top R\dot x\,ds
\;\ge\;
\chi_0^\top R\chi_0+3\,\chi_1^\top R\chi_1+5\,\chi_2^\top R\chi_2.$$

With the factor $e^{-2aH}$ this bounds the weighted double integral
from below. The weights $1,3,5$ are the canonical
$2k+1$ Legendre-norm reciprocals — this is the "second-order canonical
Bessel–Legendre" element named in the target.

## 4. Per-mode dissipation LMI (constant-delay benchmark dynamics)

Mode $i$ obeys $\dot x=A_ix(t)+\bar A_i x(t-h_i)$.
With $\zeta_2=[x(t);x(t-H);v_1;v_2]$ (mode 2, $h_2=H$) and the
extended $\zeta_1=[x(t);x(t-h_1);x(t-H);v_1;v_2]$ (mode 1), define
$E,D_i,G_i,C_k$ by $\eta=E\zeta$, $\dot\eta=D_i\zeta$,
$\dot x=G_i\zeta$, $\chi_k=C_k\zeta$ (explicit block formulas in
`output/artifacts/synth_adt.py`, `synth_hetero.py`). Then

$$\dot V+2aV\le\zeta^\top\Phi_i\,\zeta,\qquad
\Phi_i=E^\top PD_i+D_i^\top PE+2aE^\top PE
+\mathrm{blk}(Q,0,-e^{-2aH}Q,0,0)$$
$$+H^2G_i^\top RG_i
-e^{-2aH}(C_0^\top RC_0+3C_1^\top RC_1+5C_2^\top RC_2),$$

so $\Phi_i\prec0$ certifies $\dot V+2aV\le0$ along mode $i$.
Because the functional is **common** (identical $P,Q,R,H$ across
modes), $V$ is continuous at switches ($\mu=1$, no jump),
hence exponential decay $V(t)\le e^{-2a(t-t_0)}V(t_0)$ under
**arbitrary** switching — i.e. certified ADT $\tau_a=0$ ($N_0=1$),
strictly below $6.5147$.

**Important correction recorded.** A first synthesis run
(`synth_common_a03.json`) used the 8-vector with $x(t-H)$ in the
delayed-state slot for *both* modes — wrong for mode 1, whose
dynamics involve $x(t-0.3)$. The rigorous certificate below uses
the 10-dimensional $\Phi_1$ with the true $x(t-h_1)$ slot
(`synth_hetero.py::Phi1_10`). The 8-dim mode-1 "feasibility" is
**not** claimed as a certificate.

## 5. Certified matrices (reproduced verbatim from the artifact)

Common $P$ (`output/artifacts/synth_tauaware_b.json`), $a=0.3$:

$$P=\begin{pmatrix}
5.587849&0.164034&-0.734291&0.267930&-0.313660&-0.867883\\
0.164034&6.507154&-0.381375&-1.544660&-0.194970&0.101328\\
-0.734291&-0.381375&4.020742&0.178067&-0.541366&-0.182978\\
0.267930&-1.544660&0.178067&3.853669&-0.088504&-0.556963\\
-0.313660&-0.194970&-0.541366&-0.088504&3.580525&0.544782\\
-0.867883&0.101328&-0.182978&-0.556963&0.544782&4.344039
\end{pmatrix}$$

$$Q=0.327894\,I_2,\qquad R=3.709127\,I_2.$$

$\mathrm{spec}(P)=\{2.979851,\,2.991119,\,3.529460,\,4.763253,\,
6.317559,\,7.312736\}\succ0$; $\det P=6922.602077$.

### Verified LMI eigenvalues (numpy `eigvalsh`, independently recomputed)

Mode 2 (8-dim, exact): $\mathrm{spec}(\Phi_2)=\{-2354.09,\,-2351.40,\,
-51.61,\,-48.87,\,-5.58,\,-5.03,\,-2.58,\,-0.151\}$:
$\lambda_{\max}(\Phi_2)=-0.1515<0$. **Certified.**

Mode 1 (rigorous 10-dim $\Phi_1$ with the true $x(t-0.3)$ slot):
with *these* matrices $\lambda_{\max}=+4.5204>0$.
**Mode 1 is NOT certified by this $(P,q,r)$ triple.**
(For reference, the earlier 8-dim-common point failed the same
check with $+305.88$.)
The 8-dim value $\lambda_{\max}(\Phi_1^{8d})=-0.00203$ is reported
only to document the trap: it substitutes the wrong delayed state.

## 6. Honest qualification of what is / is not established

- **Established (TARGET improvement arm, partial):** a common
  second-order-Bessel–Legendre LKF structure with an explicit
  machine-checked mode-2 certificate at $a=0.3$, plus a verified
  common-$P$ mode-1 certificate at $a=0.3$ **only** under the
  (incorrect-for-mode-1) $x(t-H)$ substitution. Heterogeneous-delay
  search (`synth_hetero.py`, common window, correct slots) reached
  $\max(\lambda_{\max}\Phi_1^{10d},\lambda_{\max}\Phi_2)=+0.0022$
  (relative margin $+5.6\times10^{-3}$) — feasible up to a
  $10^{-3}$-scale residual, **not** a certificate.
- **Not established:** a complete two-mode feasible triple, hence
  no certified $\tau_a<6.5147$ is claimed. No dual infeasibility
  (class-barrier arm) was derived either.
- The tau-aware common-$(P,qI,rI)$ run reached
  $\tau_a=4.70$ at $k^\*=0.05$ nominally, but its mode-1 margin
  ($-2.0\times10^{-3}$ absolute, $-2.8\times10^{-4}$ relative) sits
  below trustworthy conditioning precision and, decisively, the
  rigorous 10-dim check reverses its sign. It is therefore reported
  as **computed evidence of near-feasibility, not a certificate**.

## 7. Reproduction

- `output/artifacts/synth_adt.py` — 8-dim $\Phi$ builder + BL blocks,
  numpy-only random hill-climb.
- `output/artifacts/synth_hetero.py` — rigorous 10-dim mode-1
  $\Phi$ + heterogeneous common-window search.
- `output/artifacts/synth_tauaware.py` — tau-aware common-$(P,qI,rI)$
  search (produced the explicit triple).
- `output/artifacts/synth_tauaware_b.json` — the explicit matrices.
- `output/artifacts/cert_matrices.npz` — same triple in npz form.
- All eigenvalue claims re-verified post hoc with `numpy.linalg.eigvalsh`
  (see §5); the mode-1 10-dim check is the gate that the triple fails.

## 8. Bottom line

The credible route (common augmented LKF + order-2 canonical BL
inequality) is demonstrated as **near-feasible with one mode fully
certified and explicit matrices on the table**, but the complete
two-mode TARGET certificate was not closed within the pass:
the heterogeneous-delay mode-1 LMI residual ($+0.002$) and the
thin mode-1 margin of the tau-aware triple do not meet certificate
standard. Per Audit honesty rules this report is **NO_RESULT**
with strong documented progress, not a CLAIMED improvement.
