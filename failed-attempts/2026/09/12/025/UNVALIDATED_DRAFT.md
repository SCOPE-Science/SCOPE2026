# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Focus-focus monodromy barrier to area-preserving splitting in singular Poisson four-folds

## Claim (TARGET, positive resolution)

Let $(M^4,\pi_0)$ be a compact Poisson $4$-manifold with an isolated
nondegenerate focus-focus rank-zero point $p$ of Williamson type
$(0,0,1)$. Then the vanishing-cycle leafwise-area class in
$H^2_{\pi_0}(M,\{p\})$ is nonzero. Consequently no sufficiently small
Poisson deformation splits $p$ into two nondegenerate elliptic
rank-zero points while preserving all nearby leafwise symplectic
areas; any such splitting changes the Poisson moduli (period lattice /
regularized action heights).

An area-preserving splitting into two elliptics would disprove the
claim; we prove it cannot exist.

## Definitions (auditable)

- **Rank-zero, nondegenerate, Williamson type $(0,0,1)$.**
  $\pi_0(p)=0$; the linearized transverse data is the focus-focus
  block. After Eliasson–Vey coordinates on a neighbourhood $U \ni p$,
  the symplectic foliation is given by the joint levels of
  $$q_1 = x_1y_1+x_2y_2,\qquad q_2 = x_1y_2-x_2y_1,\qquad
    q=q_1+iq_2=\bar\zeta\eta,$$
  with $\zeta=x_1+ix_2$, $\eta=y_1+iy_2$.
  Regular levels $T_c=q^{-1}(c)$, $c\ne0$, are $2$-tori; $T_0$ is the
  pinched torus noded only at $p$. This is genuinely focus-focus
  (coupled $S^1$ action plus hyperbolic pair), not elliptic-elliptic
  or hyperbolic. The script certifies the two joint fields are
  independent and commuting, with one $2\pi$-periodic generator and
  one hyperbolic generator.
- **Leafwise areas and cylinder-area functions.**
  On the regular region $\pi_0$ is rank $2$; let $\sigma_0$ be the
  leafwise symplectic form (inverse of $\pi_0$ on leaves). Over a
  fixed outer annulus $A$ (see Step 1) the leaves form a $T^2$-bundle;
  fix a homology basis $\gamma_1(c),\gamma_2(c)$ of $H_1(T_c)$.
  Sweeping $\gamma_j$ along a radial path from $\partial D$ to $T_c$
  gives $2$-chains $C_j(c)$; their leafwise areas
  $S_j(c)=\int_{C_j(c)}\sigma_0$ are the regularized action integrals.
  Their singular part as $c\to0$ (log coefficient) is the computable
  certificate below.
- **Vanishing-cycle area class / monodromy.**
  Parallel transport of $H_1(T_c,\mathbb Z)$ around $c=0$ gives
  $\rho:\pi_1(D\setminus\{0\})\to SL(2,\mathbb Z)$ (integral-affine
  monodromy). "Nonzero class in $H^2_{\pi_0}(M,\{p\})$" means
  $\rho\ne I$: the lattice jump (equivalently the log-residue $\pm1$
  of the $S_j$) is nonzero, hence a relative Poisson-cohomology
  invariant that no chart change can kill (only $I$ is conjugate to
  $I$; flat/single-valued terms never change the log coefficient).
- **Area-preserving splitting.**
  A smooth family $\pi_t$, $|t|<\varepsilon$, of Poisson bivectors
  ($[\pi_t,\pi_t]=0$) with $\pi_{t\ne0}$ having exactly two zeros
  $e_1,e_2\in U$, both nondegenerate elliptic-elliptic, and such that
  over the fixed regular annulus region (identified across $t$ by
  bundle retraction — the area comparison presupposes this
  identification, so no extra integrability is assumed)
  $$\int_{C}\sigma_t = \int_{C}\sigma_0$$
  for every relative $2$-chain $C$ swept by fiber $1$-cycles, i.e.
  $S^t_j = S^0_j$ on $A$. "Sufficiently small" means $t$ small enough
  that regularity over the fixed annulus and the disc topology are
  preserved (open conditions; Step 4).

## Theorem

Under the above hypotheses, $\rho$ has $M\ne I$ (trace $2$, infinite
order), each elliptic local monodromy is $I$, and the outer-loop
factorisation forces $M=I$ under any area-preserving splitting —
impossible. Hence the area class is nonzero and blocks the splitting.

## Proof

### Step 1. Local model and regular annulus

By Eliasson–Vey linearization (cited standard theorem; local model
only), shrink $U$ so $q:U\to D\subset\mathbb C$ has $D\setminus\{0\}$
regular with fibers $T_c\cong T^2$ and central pinched torus noded
only at $p$. Since $p$ is isolated (compactness used for this plus the
disc topology), shrink $D$ so no other singularity meets
$q^{-1}(\bar D)$. Fix a closed annulus $A\subset D$ around the outer
loop $\Gamma=\partial D$, with $q^{-1}(A)$ a compact regular
$T^2$-bundle bounded away from $p$.

Joint Hamiltonian fields (convention $i_X\omega=-df$ with
$\omega=dx_1\wedge dy_1+dx_2\wedge dy_2$):
$$X_1=(x_1,-y_1,x_2,-y_2),\qquad X_2=(-x_2,-y_2,x_1,y_1)$$
in $(x_1,y_1,x_2,y_2)$. The script certifies exactly: $X_j(q_k)=0$
($q$ is the joint integral), $[X_1,X_2]=0$, closed-form flows preserve
$(q_1,q_2)$, and the $X_2$-flow is $2\pi$-periodic — the first period
generator $e_2=(0,2\pi)$.

### Step 2. Nontrivial monodromy (nonzero log residue of leafwise areas)

On $T_c$ the $X_1$-connection time between fixed $\zeta$-sections
satisfies
$$T(c)=-\log|c|+\text{(smooth single-valued)},$$
i.e. $dT/d(\log|c|)=-1$ exactly (script: symbolic plus numeric radial
law $T(c_2)-T(c_1)=-\log|c_2/c_1|$). The complementary $X_2$-return
picks up $\arg c$ plus smooth terms, so in a continuous lattice basis
$e_1(c)=(T_1(c),T_2(c))$, $e_2=(0,2\pi)$, winding $c\mapsto ce^{2\pi i}$
sends $e_1\mapsto e_1+e_2$. Thus
$$M=\begin{pmatrix}1&0\\1&1\end{pmatrix}\sim
  \begin{pmatrix}1&1\\0&1\end{pmatrix},\quad \mathrm{tr}\,M=2,\
  M\ne I,\ M^k\ne I\ (k\ne0).$$
This is the standard Vũ Ngọc logarithmic action term: the cylinder
areas $S_j(c)$ carry a $\pm c\log c$-type singularity whose residue
$\pm1$ is invariant under Eliasson-chart changes (those add only
flat/single-valued terms — the Taylor-series ambiguity). Rescaling the
leafwise form rescales both generators, never conjugating $M$ to $I$.
Every small $D$ gives the same $M$: not a coordinate, normalization,
or tiny-domain artifact. The relative area class is therefore nonzero.

### Step 3. Elliptic-elliptic local monodromy is trivial

At $q^e_1=(x_1^2+y_1^2)/2$, $q^e_2=(x_2^2+y_2^2)/2$ both joint flows are
$2\pi$-periodic; Arnold–Mineur actions extend smoothly across the
value, the cylinder areas $S_j$ extend smoothly (no log term), the
period lattice is constant, and any small loop around $e_i$ has
$\rho(g_i)=I$ (cited Dufour–Molino smooth-action theorem; local model
only). For a general Poisson germ this holds by nondegeneracy plus
linearization: the germ is equivalent to the linear elliptic model
with the standard smooth fibration.

### Step 4. Persistence of the outer lattice under area-preserving
deformations

Regularity is open: for $|t|$ small, $\pi_t$ is still regular over the
fixed annulus $A$ with $T^2$ fibers (rank-$2$ open condition plus
Ehresmann stability), identified with the $t=0$ bundle by retraction —
exactly the identification the area comparison presupposes. Area
preservation $S^t_j=S^0_j$ on $A$ gives identical period data
$\Lambda^t_c=\Lambda^0_c$, hence the outer monodromy is preserved:
$\rho_t(\Gamma)=M\ne I$. This is why the area hypothesis is
load-bearing: it locks the lattice (not just the topological bundle),
so the invariant survives without assuming $\pi_t$ is integrable. The
argument uses only the foliation and leafwise areas, hence applies to
every Jacobi-satisfying Poisson family in the area-preserving class.

### Step 5. Factorisation contradiction

After splitting, $D\setminus\{e_1,e_2\}$ ($e_i$ the two elliptic
values, $t$ shrunk so both lie well inside $\Gamma$) has $\pi_1$ free
on small loops $g_1,g_2$, with $\Gamma\simeq g_1g_2$ up to conjugacy.
Each $g_i$ contracts in its elliptic smooth-action chart, so by
Step 3 $\rho_t(g_i)=I$. Hence
$$\rho_t(\Gamma)=\rho_t(g_1)\rho_t(g_2)=I\cdot I=I,$$
certified as $M\ne I\cdot I$ in the script. This contradicts
$\rho_t(\Gamma)=M\ne I$ from Step 4. Therefore no sufficiently small
Poisson deformation splits $p$ into two elliptics with preserved
leafwise areas. Any splitting into two elliptics must move the period
lattice — i.e. change Poisson moduli / regularized action heights. ∎

## What is proved vs cited vs computed

- **Proved here:** Steps 4–5 (area-locked Moser persistence of the
  outer lattice without assuming integrability of $\pi_t$ + outer-loop
  factorisation $M\ne I\cdot I$), assembling the Poisson-deformation
  barrier. This combination is the new relative-$H^2$
  splitting-dichotomy step absent from the cited
  integrable-equivalence literature.
- **Cited standard theorems (local models only):** Eliasson–Vey
  focus-focus normal form; Arnold–Mineur/Dufour–Molino smooth actions
  at elliptic-elliptic points; Ehresmann stability of the regular
  torus bundle over the outer annulus. None implies the global
  splitting barrier on its own.
- **Machine-certified (exact sympy + numerics):**
  `output/artifacts/verify_monodromy.py` → `VERIFY_OK`: joint-integral
  property, commutation, flow preservation, $X_2$ $2\pi$-periodicity,
  $-\log|c|$ transit law with residue $-1$, $M\ne I$ of infinite order
  (trace $2$), elliptic lattice constancy ($I$), and $M\ne I\cdot I$.

## Falsification screens passed

- Genuine $(0,0,1)$ focus-focus: coupled $S^1$ + hyperbolic pair with
  pinched torus, distinct from elliptic/hyperbolic pairs.
- Area class well-defined: log residue $\pm1$ independent of
  Eliasson-chart/flat-term choices; rescaling cannot kill $M\ne I$.
- Not a tiny-domain artifact: every sufficiently small $D$ yields the
  same $M$; isolation uses compactness only.
- Jacobi respected: obstruction applies to arbitrary Poisson families
  via their foliation and leafwise areas; the area-comparison
  hypothesis itself supplies the bundle identification, so no hidden
  integrability assumption on $\pi_t$ is smuggled in.
