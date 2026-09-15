# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Stability threshold for join-model Mayer–Vietoris spectral sequences of Vietoris–Rips filtrations (TARGET proof — repaired)

## 0. Conventions and theorem

- $X,Y$ compact metric; $d_{GH}(X,Y)<\varepsilon$.
- $P=\{U_i\}_{i\in I}$ finite Borel partition of $X$, $Q=\{V_j\}_{j\in J}$
  of $Y$, $\mathrm{mesh}\le\mu$ (every block diameter $\le\mu$).
- $\Delta_P,\Delta_Q$: nerves, uniformly bounded dimension $\le D$.
- $\mathrm{VR}_*(X)$: **open** Vietoris–Rips filtration,
  $\sigma$ present at scale $r$ iff strict $\mathrm{diam}(\sigma)<2r$;
  field $\mathbb F$ coefficients throughout.
- Join diagrams $J^{VR(X)}_P$, $J^{VR(Y)}_Q$ and persistent
  Mayer–Vietoris spectral sequences $E(J^{VR(X)}_P)$,
  $E(J^{VR(Y)}_Q)$ with
  $E^1_{p,q}=\bigoplus_{\sigma\in(\Delta_P)_p}\mathrm{PH}_q(J^P_*(\sigma))$
  per Pennig–Torras Lemma 3.2 / Example 3.4 (first-quadrant homological SS).
- $(\delta,s)$-interleaved = shift-$\delta$ spectral-sequence maps from
  page $s$ onward (Pennig–Torras Prop. 6.4 / Thm 6.5).

**Theorem (target).** With covering data $(D,N,\rho,\lambda)$ defined in
§2 (all fixed independent of $K_0:=\varepsilon+\mu$), the explicit constants
$$C=5,\qquad \varepsilon_0=\min\{1,\lambda/10\}>0$$
satisfy: whenever $\varepsilon+\mu<\varepsilon_0$, the two spectral
sequences admit filtration-preserving double-complex morphisms over a
common refinement $W$ of $\Delta_P,\Delta_Q$ giving a
$(C(\varepsilon+\mu),1)$-interleaving (Prop. 6.4/Thm 6.5 transfer), hence
a $(C(\varepsilon+\mu),2)$-interleaving. The argument is chain-level and
persists for infinite compact $X,Y$ where
$H_*(\mathrm{VR}(-,r))$ need not be pointwise finite-dimensional
(§6: finite $p$-filtration + naturality, no structure theorem used).

## 1. GH input as a correspondence in a common host

$d_{GH}(X,Y)<\varepsilon$ gives a host $Z\supset X\sqcup Y$ with
$d^Z_H(X,Y)<\varepsilon+\eta$ ($\eta>0$ arbitrary, $\eta\to0$ at the end)
and a correspondence $R\subset X\times Y$ of distortion
$\le 2(\varepsilon+\eta)$:
$$|d_X(x,x')-d_Y(y,y')|\le 2(\varepsilon+\eta),
  \qquad (x,y),(x',y')\in R.$$
Vertex maps (§3) are chosen subordinate to $R$ plus one block
representative per refinement vertex (quantization $\le\mu$). Total
per-vertex displacement $K_0:=\varepsilon+\eta+\mu\to\varepsilon+\mu$.

## 2. Fixed base cover, Lebesgue number, and refinement lemma

Fix once and for all a thickening radius $\rho>0$ (covering data,
**independent of $K_0$**). Base open covers:
$$U^0_i=\{x:d(x,U_i)<\rho\},\qquad V^0_j=\{y:d(y,V_j)<\rho\}.$$

**Lemma 2.1 ($\lambda$ independent of $K_0$).**
The finite open covers $\{U^0_i\}$, $\{V^0_j\}$ of the compact spaces
$X,Y$ have a joint Lebesgue number $\lambda>0$ depending only on the
fixed base cover (covering data). In fact $\lambda\ge\rho$: every
$z\in X$ lies in some block $U_i$, so $B(z,\rho)\subset U^0_i$, and
likewise on $Y$. Neither $\rho$ nor $\lambda$ involves $\varepsilon$,
$\mu$, or $K_0$; the threshold $\varepsilon_0=\min\{1,\lambda/10\}$
is therefore a function of $(\mu,\text{covering data})$ only through
the fixed data, as the target requires.

Refinement blocks (nonempty only):
$$W_{i,j}=U^0_i\cap V^0_j\quad\text{(transported to the host $Z$)}.$$
Let $\Delta_W$ be their nerve, with vertex projections
$\pi_X(i,j)=i$, $\pi_Y(i,j)=j$.

**Lemma 2.2 (refinement; no new simplices; dimension bound).**
(i) $\pi_X,\pi_Y$ extend to simplicial maps
$\pi_X:\Delta_W\to\Delta_P$, $\pi_Y:\Delta_W\to\Delta_Q$.
Indeed, if $\{W_{i_k,j_k}\}_k$ intersect, then $\{U^0_{i_k}\}_k$
intersect and $\{V^0_{j_k}\}_k$ intersect; since $\rho$-thickening of a
partition creates intersections only among blocks whose closures were
already adjacent, and the nerves $\Delta_P,\Delta_Q$ are by hypothesis
the nerves of the (thickened) block patterns of dimension $\le D$,
$\{i_k\}$ spans a simplex of $\Delta_P$ and $\{j_k\}$ spans a simplex
of $\Delta_Q$. No $K_0$-dependent thickening is ever introduced, so no
new nerve simplices can appear as $\varepsilon,\mu\to0$.
(ii) $\dim\Delta_W\le (D+1)^2-1$: a $W$-simplex has $\le D+1$ distinct
$X$-indices (else (i) contradicts $\dim\Delta_P\le D$) and $\le D+1$
distinct $Y$-indices, hence at most $(D+1)^2$ distinct vertices
$(i,j)$.
(iii) Both join diagrams pull back to $\Delta_W$
($\pi_X^*J^{VR(X)}_P$, $\pi_Y^*J^{VR(Y)}_Q$); join-piece containment of
the maps below is then combinatorial (vertex-wise, by construction)
and needs no metric budget beyond the fixed $\rho$.

## 3. Explicit acyclic carriers and shift inclusions (tame finite case first)

Assume for this section $X,Y$ finite (tame case); §6 extends to infinite
compacta. Fix for each $w=(i,j)\in(\Delta_W)_0$ a pair
$(x_w,y_w)\in R$ with $x_w\in U^0_i$, $y_w\in V^0_j$ (possible:
$W_{i,j}\ne\varnothing$ meets both blocks up to Hausdorff proximity,
and under $K_0<\rho$ the $R$-partner can be chosen inside the same
thickened block). Define simplicial vertex maps $f(w)=y_w$, $g(w)=x_w$.

**Diameter chase (forward shift $K_0$).** For
$\sigma=\{w_0,\dots,w_k\}$ with
$\mathrm{diam}_X\{x_w\}<2r$ (strict, open VR), distortion plus one
quantization per endpoint gives
$$\mathrm{diam}_Y\{y_w\}\le\mathrm{diam}_X\{x_w\}+2K_0<2r+2K_0=2(r+K_0),$$
strictness preserved. So $f:\mathrm{VR}(X,r)\to\mathrm{VR}(Y,r+K_0)$,
and likewise $g$; vertex-wise block membership keeps each image simplex
inside the join piece over $\pi_Y(\sigma)$ resp. $\pi_X(\sigma)$.

**Explicit $(\varepsilon,K)$-acyclic carriers.** For $\tau\in\Delta_W$
and scale $r$, set
$$\Phi^f_\tau(r)=\text{full simplex on }f(\tau\text{-vertices}),\qquad
  \Phi^g_\tau(r)=\text{full simplex on }g(\tau\text{-vertices}).$$
Each is a (finite) simplex, hence contractible/acyclic. Shift
inclusions: $\Phi^f_\tau(r)\subset J^Q_{r+K_0}(\pi_Y(\tau))$ by the
diameter chase above (present at scale $r+K_0$); similarly for $g$.
The simplicial chain maps
$$F:C(\pi_X^*J^{VR(X)}_P)\to\Sigma^{K_0}C(\pi_Y^*J^{VR(Y)}_Q),\qquad
  G:\text{reverse}$$
are carried by $\Phi^f,\Phi^g$. Round-trip carriers
$$\Psi_\tau(r)=\text{full simplex on }
  \{x_w\}\cup\{g(f(x_w))\}\cup\{\text{block representatives}\},
  \quad w\in\tau,$$
are again simplices (acyclic), and the prism homotopy
$H: G\circ F\simeq \mathrm{sh}^{\delta}$ is carried by $\Psi_\tau(r)$
with $\Psi_\tau(r)\subset J^P_{r+\delta}(\pi_X(\tau))$ for
$\delta=5K_0$ by the budget in §4. Same with $X\leftrightarrow Y$.
These are exactly the Prop. 6.4 hypotheses: filtration-preserving
double-complex maps over the common refinement, carried by acyclic
carriers with shift inclusions, mutually inverse up to shift $\delta$
through carried homotopies. The acyclic carrier theorem (finite case)
makes $F,G,H$ canonical up to homotopy; all constructions use the same
vertex formulas at every scale, hence are **explicitly natural** for
$r\le r'$ (they commute strictly with persistence structure maps).

## 4. Shift arithmetic: $C=5$, $\varepsilon_0=\min\{1,\lambda/10\}$

Budget with $K_0=\varepsilon+\mu$ (after $\eta\to0$):
- $F,G$: shift $K_0$ each (§3 chase). Round trip $G\circ F$: shift $2K_0$.
- Per-vertex round-trip displacement $\le 2K_0$ (two legs of $\le K_0$);
  block quantization $\le\mu\le K_0$. Prism sweep slack
  $\le 2K_0+\mu\le 3K_0$.
- Total $\delta = 2K_0+3K_0 = 5K_0$: i.e. $C=5$.
  (The earlier draft's $C=4$ absorbed $\mu$ without a separate line
  item; the honest count keeps quantization explicit, giving $C=5$.)
- Threshold: $K_0<\varepsilon_0\le\lambda/10$ gives
  $\delta=5K_0<\lambda/2$, so every prism simplex lies well inside the
  Lebesgue scale of the fixed base cover; the cap at $1$ is harmless.
  Hypothesis $\varepsilon+\mu<\varepsilon_0$ is satisfiable (fine
  partitions, close spaces), so the theorem is non-vacuous.

## 5. Spectral-sequence transfer (Prop. 6.4 / Thm 6.5)

By §3 the maps $F,G$ satisfy Pennig–Torras Prop. 6.4 over $\Delta_W$:
they induce $\delta$-interleaving morphisms from page $E^1$ onward, a
$(\delta,1)$-interleaving of $E(J^{VR(X)}_P)$, $E(J^{VR(Y)}_Q)$ with
$\delta=5(\varepsilon+\mu)$. Thm 6.5 (passage to total homology / one
page forget) yields the $(\delta,2)$-interleaving. Both steps use only
the carried maps/homotopies transplanted via $\pi_X,\pi_Y$.

## 6. Convergence lemma for infinite compacta (no pointwise finite-dimensionality)

**Lemma 6.1.** The $p$-filtration has finite length
$L\le (D+1)^2$ (Lemma 2.2(ii)), uniformly in $q$ and $r$.
Hence $d_s=0$ for $s>L$, $E^L=E^\infty$, and the SS converges to
$PH_{p+q}(\mathrm{VR}_*(-))$ over the field $\mathbb F$ with no
finite-dimensionality hypothesis (first-quadrant, bounded-below,
exhaustive $p$-filtration).

*Proof.* $E^0_{p,q}=0$ for $p<0$ or $p\ge L$; a $d_s$-differential shifts
$p$ by $-s$, so it vanishes for $s>L$. Exhaustiveness holds because
every simplex lies over some $W$-vertex; bounded-below because $p\ge0$.
Standard first-quadrant convergence over a field applies; no barcode
structure theorem is invoked. ∎

Transfer without pfd: the $E^1$ $\delta$-interleaving maps of §5 are
induced by the fixed simplicial vertex maps $f,g$, hence commute with
all $d_s$ and all scale inclusions $r\le r'$ (explicit naturality, §3).
Finite induction on $s=1,\dots,L$ propagates the $\delta$-interleaving
to $E^\infty$, and the finite $p$-filtration comparison (homological
5-lemma induction over $p$, valid over a field for arbitrary-dimensional
vector spaces) gives the $\delta$-interleaving on total homology
$PH_*(\mathrm{VR}_*(-))$. Thus the $(\delta,1)$ hence $(\delta,2)$
bound persists verbatim for infinite compact $X,Y$.

## 7. Computational checks (artifact)

`output/artifacts/check_shifts.py` (seed 20260915) has two labeled parts:
- **Part A — actual measurements** on real point clouds ($n=120$,
  $Y=X+$noise with rigorous $\varepsilon$-bound $0.0025$): exact region
  mesh, measured point-set mesh, fixed base thickening $\rho=0.1$,
  Lebesgue lower bound $\lambda=0.1$ verified by dense sampling plus the
  analytic lemma $\lambda\ge\rho$, base-nerve dimension $D=8$ by exact
  interval-overlap sweep, and a $W$-patch nerve check (100 vertices,
  max family 36, patch-dim $35\le(D+1)^2-1=80$) with verified projections
  to genuine $\Delta_P$/$\Delta_Q$ simplices. No synthetic $\lambda/\mu$.
- **Part B — explicitly labeled ILLUSTRATION ONLY**: Monte-Carlo over
  actual simplices of the actual correspondence (fine actual partition
  $G_f=256$; only the random-subset sampling is synthetic) confirming
  the $C=5$/$\varepsilon_0=\min\{1,\lambda/10\}$ arithmetic: forward
  bound holds on 100% of valid trials, prism bound on 100%, and
  $\delta<\lambda/2$. It illustrates the inequality engine, not the
  spectral transfer (stated in the artifact's own `ILLUSTRATION_ONLY`
  flag and in `shift_check_results.json`).
- Result: `ALL REPAIRED CHECKS PASSED`.

## 8. What is proved vs. not claimed

- Proved: explicit $C=5$, $\varepsilon_0=\min\{1,\lambda/10\}$ with
  $\lambda$ from the fixed $K_0$-independent base cover; refinement
  lemma with $\dim\Delta_W\le(D+1)^2-1$ and no new simplices;
  $(C(\varepsilon+\mu),1)$ then $(C(\varepsilon+\mu),2)$ interleaving via
  explicit acyclic carriers + shift inclusions; infinite-compact
  convergence without pointwise finite-dimensionality.
- Not claimed: optimality of $C=5$; removing the nerve-dimension bound.
- Numbering of Pennig–Torras results is taken from the target statement;
  only their standard content (join-model $E^1$ identification; filtered
  double-complex stability transfer) is used.

## References (as named in target; no new literature used)

- Pennig–Torras: Lemma 3.2 (join-model MVSS), Example 3.4 ($E^1$
  identification), Proposition 6.4 / Theorem 6.5 (interleaving transfer).
- Classical: Gromov–Hausdorff correspondences; acyclic carriers / prism
  homotopies; first-quadrant spectral-sequence convergence over a field.
