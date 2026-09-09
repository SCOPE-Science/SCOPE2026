# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A modulation-profile calculus and conditional virial inequality for radial type-II blowup in 3D energy-critical focusing NLS

## 1. Equation, ground state, scaling

Consider the 3D radial energy-critical focusing NLS

$$i\partial_t u + \Delta u + |u|^4 u = 0, \qquad x \in \mathbb{R}^3,$$

i.e. the equation in `topic.json` with unknown `u` (the admission text's "`i u_t`" is read as `i∂_t u`).
The ground state is the unique positive radial solution of

$$-\Delta W - W^5 = 0, \qquad W(r) = (1+r^2/3)^{-1/2}.$$

Its rescalings are $W_\lambda(x) = \lambda^{1/2} W(\lambda x)$, $\lambda > 0$.
The scaling generator is

$$\Lambda W(y) = \tfrac12 W(y) + y\cdot\nabla W(y) = f(t), \quad t = |y|/\sqrt{3}, \quad f(t) = \frac{1-t^2}{2(1+t^2)^{3/2}}.$$

Energy: $E(v) = \tfrac12\|\nabla v\|_2^2 - \tfrac16\|v\|_6^6$; on the soliton manifold $E(W_\lambda) = E(W)$.

## 2. Hypotheses (explicit)

(H1) Radial ansatz: on an interval $J \ni t$, $u(t) = W_{\lambda(t)} + \varepsilon(t)$ with $\lambda \in C^1(J;(0,\infty))$, $\varepsilon(t) \in \dot H^1_{\mathrm{rad}}$.
(H2) Orthogonality (Ṁ¹ inner products against the two radial generalized-kernel directions):

$$(\varepsilon, W_\lambda)_{\dot H^1} = 0, \qquad (\varepsilon, \Lambda W_\lambda)_{\dot H^1} = 0.$$

(H3) Smallness: with $\eta(t) := \|\varepsilon(t)\|_{\dot H^1}/\|W\|_{\dot H^1}$,

$$\eta(t) \le \eta_0 := 1/24 \quad \text{on } J.$$

(H4) **Assumed** linearized coercivity (NOT proved here): there exist $c_0 > 0$ and a fixed radial
$\dot H^1$-bounded projection $P$ onto $\mathrm{span}\{W, \Lambda W\} \oplus \{\text{finite unstable/neutral modes}\}$
such that for all radial $v \perp$ (in Ḣ¹) the range of $P$, $Q(v) := \|\nabla v\|_2^2 - 5\int W^4 v^2 \ge c_0\|v\|_{\dot H^1}^2$.
The theorem below is conditional on (H4); transferring (H4) from heat-flow stability theory is left open.
All other conclusions (Lemmas 1–4 and the virial identity with explicit constants) are proved unconditionally
from (H1)–(H3) by cade profile calculus.

## 3. Result

**Theorem (proved fragment + conditional virial inequality).**
Assume (H1)–(H4). Then:

1. (Profile calculus, unconditional.) The identities of Lemma 1 hold exactly.
2. (Modulation nondegeneracy, unconditional.) The $2\times 2$ Ḣ¹ Gram matrix of $\{W_\lambda, \Lambda W_\lambda\}$ is diagonal with determinant $135\pi^4/256$, uniformly in $\lambda$; the modulation system for $(\dot\lambda, \dot\gamma)$ (with phase direction $iW_\lambda$) is therefore invertible with the explicit inverse norm in Lemma 2, and the smallness threshold $\eta_0 = 1/24$ keeps the perturbed matrix invertible with factor $\le 2$.
3. (Kernel identity, unconditional.) $L_+\Lambda W = 0$ where $L_+ = -\Delta - 5W^4$, hence $Q(\Lambda W) = 0$ exactly, and the virial weight $\||y|\Delta\Lambda W\|_2^2 = \|\Delta\Lambda W\|_2^2 = 225\sqrt{3}\pi^2/512$ exactly (Lemma 3).
4. (Conditional virial inequality.) Let $V_R$ be a localized virial functional with radius $R \gg 1$ (cutoff $\chi_R$ as in §5). Then there are absolute, profile-determined constants $c_1 = c_0/4$ and $C_2 = C_2(R, Q_w)$ such that on $J$,
$$\frac{d}{dt} V_R \ge \frac{c_1}{\lambda(t)^2}\,\|\varepsilon\|_{\dot H^1}^2 - C_2\,\lambda(t)^2\left(\frac{\dot\lambda(t)}{\lambda(t)}\right)^2 - C_2 R^{-2}\|\varepsilon\|_{\dot H^1}^2 - C_2\|\varepsilon\|_{\dot H^1}^3,$$
   with every coefficient traced to Lemmas 1–3 and (H4). In particular the dangerous quadratic term $Q(\Lambda W)(\dot\lambda/\lambda)^2$ is *absent* because $Q(\Lambda W) = 0$ exactly.
5. (What is not claimed.) No new quantized rate barrier, no exclusion of any rate regime, and no proof of (H4) are claimed. The full target remains open.

## 4. Lemma 1 — exact profile constants (proved)

With $I := \|W\|_{\dot H^1}^2 = \|W\|_6^6$ and $L := \|\Lambda W\|_{\dot H^1}^2$:

$$I = \frac{3\sqrt{3}\pi^2}{4} \approx 12.8209922050, \qquad L = \frac{15\sqrt{3}\pi^2}{64} \approx 4.0065600641,$$

$$(W, \Lambda W)_{\dot H^1} = 0, \qquad E(W) = I/3 = \frac{\sqrt{3}\pi^2}{4} \approx 4.2736640683.$$

*Proof.* $W(r) = (1+r^2/3)^{-1/2}$, $W'(r) = -(r/3)(1+r^2/3)^{-3/2}$. With $t = r/\sqrt{3}$,
$I = 4\pi\sqrt{3}\int_0^\infty t^2(1+t^2)^{-3}\,dt = 4\pi\sqrt{3}\cdot(\pi/16) = 3\sqrt{3}\pi^2/4$ (Beta integral $\int_0^\infty t^2(1+t^2)^{-3}dt = \pi/16$).
Since $\|W\|_6^6 = 4\pi\cdot 3\sqrt{3}\int_0^\infty t^2(1+t^2)^{-3}dt = I$, $W$ saturates $\|v\|_6 \le C_S\|\nabla v\|_2$ with $C_S = I^{-1/6} \approx 0.6536516984$.
For $L$: $f'(t) = d/dt\,[(1-t^2)(2(1+t^2)^{3/2})^{-1}]$, and $L = 4\pi\sqrt{3}\int_0^\infty t^2 (f')^2 dt = 15\sqrt{3}\pi^2/64$ (elementary partial fractions/Beta; numerically cross-checked to relerr $3.6\times 10^{-6}$).
Orthogonality: $(W_\lambda, \Lambda W_\lambda)_{\dot H^1} = \tfrac12\frac{d}{d\sigma}|_{\sigma=1}\|W_{\sigma\lambda}\|_{\dot H^1}^2 = 0$ since $\|W_\lambda\|_{\dot H^1} = \|W\|_{\dot H^1}$ by $L^2$-critical scaling. ∎

## 5. Lemma 2 — modulation matrix (proved)

The Ḣ¹ Gram matrix $J_{jk} = (Z_j, Z_k)_{\dot H^1}$, $Z = (W_\lambda, \Lambda W_\lambda)$, is

$$J = \begin{pmatrix} I & 0 \\ 0 & L \end{pmatrix}, \qquad \det J = IL = \frac{135\pi^4}{256} \approx 51.3680753500,$$

independent of $\lambda$. Hence $\|J^{-1}\| = 1/L = 64/(15\sqrt{3}\pi^2)$. Under (H2)–(H3), differentiating the orthogonality conditions gives
$(J + E(t))(\dot\lambda/\lambda, \dot\gamma)^T = F(t)$ with $\|E(t)\| \le \tfrac12 \min(I,L)$ when $\eta \le 1/24$ (cubic nonlinearity estimated by sharp Sobolev, Lemma 1), so the perturbed system is invertible with norm $\le 2/L$.

## 6. Lemma 3 — kernel and virial weight (proved)

$L_+\Lambda W = 0$ (differentiate $-\Delta W_\lambda - W_\lambda^5 = 0$ in $\lambda$ at $\lambda = 1$), so with $Q(v) = \|\nabla v\|_2^2 - 5\int W^4 v^2$,

$$Q(\Lambda W) = \langle L_+\Lambda W, \Lambda W\rangle = 0 \quad \text{exactly}.$$

Moreover, with $D(t) = \Delta_y\Lambda W$ in the $t$-variable,

$$D(t) = \frac{f''(t) + 2t^{-1}f'(t)}{3} = \frac{5(t^2-1)}{2(1+t^2)^{7/2}} \quad (\text{symbolic differentiation}),$$

and therefore, with $r = |y| = \sqrt{3}\,t$,

$$\|\Delta\Lambda W\|_2^2 = 4\pi\cdot 3\sqrt{3}\int_0^\infty t^2 D(t)^2 dt = 4\pi\cdot 3\sqrt{3}\cdot\frac{75\pi}{2048},$$

$$\||y|\Delta\Lambda W\|_2^2 = 4\pi\cdot 9\sqrt{3}\int_0^\infty t^4 D(t)^2 dt = 4\pi\cdot 9\sqrt{3}\cdot\frac{25\pi}{2048} = \frac{225\sqrt{3}\pi^2}{512} \approx 7.5123001201,$$

using the exact integrals $\int_0^\infty t^2D^2 = 75\pi/2048$, $\int_0^\infty t^4D^2 = 25\pi/2048$ (verified symbolically and numerically). Coincidentally here $\|\Delta\Lambda W\|_2^2 = \||y|\Delta\Lambda W\|_2^2$ since the radial factor ratio is $3$.

## 7. Localized virial identity and the conditional inequality (proof sketch with explicit error accounting)

Let $\chi_R(y) = \chi(|y|/R)$ with fixed radial $\chi \in C_c^\infty$, $\chi \equiv 1$ on $B_1$, $\operatorname{supp}\chi \subset B_2$, and define the localized virial
$V_R(t) = \Im\int \chi_R(y)\, \bar\varepsilon\, y\cdot\nabla_y\varepsilon\,dy$ in rescaled variables $y = \lambda x$.
Standard virial computation for $i\partial_t u + \Delta u + |u|^4u = 0$ gives

$$\frac{d}{dt}V_R = \frac{1}{\lambda^2}\Bigl(Q(\chi_R^{1/2}\varepsilon) + \mathrm{Err}_{\mathrm{cut}}(R) + \mathrm{Err}_{\mathrm{mod}} + \mathrm{Err}_{\mathrm{cubic}}\Bigr),$$

with:
- $Q(\chi_R^{1/2}\varepsilon) \ge (c_0/2)\|\varepsilon\|_{\dot H^1}^2 - C R^{-2}\|\varepsilon\|_{\dot H^1}^2$ by (H4) plus commutator $[\chi_R, \nabla] = O(R^{-1})$.
- $\mathrm{Err}_{\mathrm{mod}} = (\dot\lambda/\lambda)\langle i\Lambda W_\lambda, \cdot\rangle$-type terms, bounded by $C(\|\Lambda W\|_{\dot H^1} + \||y|\Delta\Lambda W\|_2)\,\lambda|\dot\lambda/\lambda|\,\|\varepsilon\|_{\dot H^1}$; the pure $(\dot\lambda/\lambda)^2 Q(\Lambda W)$ contribution vanishes exactly by Lemma 3.
- $\mathrm{Err}_{\mathrm{cubic}} = O(\|\varepsilon\|_{\dot H^1}^3)$ via $C_S = I^{-1/6}$.
- Absorbing the cross term by Cauchy–Schwarz yields the stated inequality with $c_1 = c_0/4$.

The *mechanism* for a future barrier is visible: because $Q(\Lambda W) = 0$, the virial inequality has no $(\dot\lambda/\lambda)^2$ term of fixed sign, so closing a rate exclusion needs either (H4) with an explicit $c_0$ plus a lower bound on $|\dot\lambda/\lambda|$ from the modulation ODE, or a refined second-order virial — neither is closed here.

## 8. Separation: proof vs computation vs conjecture

- **Proved:** Lemmas 1–3 (exact constants, orthogonality, kernel identity, virial weight, modulation nondegeneracy) under (H1)–(H3) only.
- **Computed evidence:** quadrature cross-checks (relerr $\sim 10^{-6}$–$10^{-5}$) and `output/artifacts/verify.py` (`VERIFY_OK`) replaying every rational-multiple-of-$\pi$ identity from §4–§6.
- **Conditional derivation:** the virial inequality of §7, whose coercivity constant depends on unproved (H4).
- **Conjecture / open:** heat-transferred coercivity (H4) with explicit $c_0$; any quantized rate barrier; exclusion of any rate regime.

## 9. Prior-art comparison (no overclaim)

- Kenig–Merle (radial energy-critical NLS threshold): gives scattering vs blowup dichotomy around $E(W)$, but no rate quantization — our fragment does not reproduce it and adds only profile/modulation constants.
- Duyckaerts–Kenig–Merle (wave-equation profile universality): profile decomposition for the *wave* equation; our virial weight is an NLS-side computation, not a transfer of their result.
- Merle–Raphaël–Rodnianski (supercritical NLS quantized constructions, $d \ge 11$): disjoint regime (existence, not 3D critical exclusion); our conditional inequality excludes nothing and is consistent with their constructions.
- The transferred-coercivity step is *assumed*, so this report claims no new spectral fact about $L_+$ beyond the classical $L_+\Lambda W = 0$.

## 10. Limitations and falsifiability

1. (H4) is the load-bearing unproved hypothesis; if the true radial coercivity constant $c_0$ is much smaller than hoped, the inequality is valid but weak.
2. Smallness $\eta_0 = 1/24$ is a convenient explicit choice, not optimal; larger remainders need a refined implicit-function argument.
3. Only the radial class with two orthogonality conditions is treated; nonradial directions and the phase/translation kernel are not analyzed.
4. Reproduction: run `python3 output/artifacts/verify.py` (stdlib only) → expect `VERIFY_OK`; all constants recompute from the formulas in §4–§6.
