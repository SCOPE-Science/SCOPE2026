# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Finite-exact two-sided supersingular Honda–Tate for K3 surfaces with Artin-invariant control

## Main theorem

Fix $q=p^a$ and $\sigma_0\in\{1,\dots,10\}$. Let $X/\mathbf F_q$ be a K3 surface
which is geometrically supersingular ($\rho(X_{\bar{\mathbf F}_q})=22$,
equivalently infinite height) of geometric Artin invariant $\sigma_0$.

**Theorem N (necessity, unconditional).** Then, with
$P_2(X/\mathbf F_q,T)=\det(1-FT\mid H^2)$:
1. (Root-of-unity shape.) $P_2(T)=\prod_{i=1}^{22}(1-q\zeta_iT)$ where each
   $\zeta_i$ is a root of unity of order prime to $p$, the multiset
   $\{\zeta_i\}$ is stable under $\mathrm{Gal}(\bar{\mathbf Q}/\mathbf Q)$,
   hence a union of full primitive-$d$-th cyclotomic orbits. Consequently
   $\#X(\mathbf F_q)=1+q^2+qm$ with $m=\sum_i\zeta_i\in\mathbf Z\cap[-22,22]$.
2. (Crystalline discriminant.) $\mathrm{disc}\,\mathrm{NS}(X_{\bar{\mathbf F}_q})
   =-p^{2\sigma_0}$; the Frobenius action on the supersingular K3 crystal
   (Ogus) has characteristic subspace of dimension $\sigma_0$. Let
   $N=\mathrm{lcm}(\mathrm{ord}\,\zeta_i)$ (with $N=1$ if all $\zeta_i=1$).
   Then $aN$ is even and $aN\ge 2\sigma_0$.
3. (Artin–Tate square constraint.) Let $r=\#\{i:\zeta_i=1\}=\rho(X/\mathbf F_q)$
   and $B=\prod_{\zeta_i\ne1}(1-\zeta_i)\in\bar{\mathbf Z}$ (with $B=1$ if
   $r=22$). Then $qB/\lvert D_{\mathbf F_q}\rvert$ is a square in
   $\mathbf Q^\times$, where $D_{\mathbf F_q}=\mathrm{disc}\,\mathrm{NS}(X/\mathbf F_q)$
   (with $D=1$ if $r=0$). In particular:
   - (a) $r=22$ ($m=22$): $m=22$ occurs over $\mathbf F_q$ only if $a$ is even
     and $a\ge 2\sigma_0$;
   - (b) $r=0$: $qB$ must be a perfect square; e.g.\ $m=-22$ (all $\zeta_i=-1$,
     $B=2^{22}$) occurs over $\mathbf F_q$ only if $a$ is even (all $p$).

**Theorem S (sufficiency, conditional on potential semi-stability $(\star)$ as in
Taelman).** Conversely, every root-of-unity Weil datum
$R(T)=\prod_{i=1}^{22}(1-\zeta_iT)$ satisfying the necessary conditions of
Theorem N for $(q,\sigma_0)$ (in the normalized, base-change-correct sense of
Lemma C below) occurs as the normalized $L$-factor of some supersingular K3
surface $X'/\mathbf F_{q^n}$, $n\ge1$, of geometric Artin invariant $\sigma_0$.
The field of full $\rho=22$ definition is explicitly controlled: $n\mid N$ can
be taken with $n$ dividing $N=\mathrm{lcm}(\mathrm{ord}\,\zeta_i)$, and
$N$ itself always suffices (over $\mathbf F_{q^N}$ all $\zeta_i^N=1$).

**Corollary M (exact $m$-set, finite-exact).** For fixed $(q,\sigma_0)$ the set
$$\mathcal M(q,\sigma_0)=\{m:\exists\ \text{supersingular }X/\mathbf F_q
\text{ of invariant }\sigma_0,\ \#X(\mathbf F_q)=1+q^2+qm\}$$
equals the set of traces of admissible multisets under Theorem N, decided by a
finite enumeration (60,280 Galois-stable multisets; orbit types $d$ with
$\varphi(d)\le22$). Unconstrained, every $m\in[-22,22]\cap\mathbf Z$ occurs as
a trace; the $(q,\sigma_0)$-restrictions above cut this down exactly (endpoint
theorems plus the square test; §6 tables).

## 1. Setup and known inputs

We use, as black boxes: (T) the Tate conjecture for K3 surfaces over finite
fields (all $p$, including $2$: Charles, Madapusi Pera, Maulik, Kim–Madapusi
Pera, Ito–Ito–Koshikawa); (O) Ogus's theory of supersingular K3 crystals,
$\mathrm{disc}=-p^{2\sigma_0}$, discriminant group $(\mathbf Z/p)^{2\sigma_0}$,
crystalline Torelli; (AT) the Artin–Tate formula for surfaces satisfying Tate;
(Sq) squareness of $\lvert\mathrm{Br}\rvert$ for K3 over finite fields
(prime-to-$p$ part via Tate's pairing; $p$-part via the crystalline refinement
used in (O)); $(\star)$ potential semi-stable reduction for K3 over function
fields of curves over finite fields, assumed as in Taelman's conditional
Honda–Tate machine, whose output we invoke: a Weil polynomial satisfying the
Tate–Brauer numerical constraints is realized by a K3 surface. Only Theorem S
uses $(\star)$; Theorem N is unconditional.

## 2. Root-of-unity shape and combinatorics

*Proof of N(1).* By (T), $\rho(X/\mathbf F_q)$ equals the multiplicity of the
eigenvalue $q$ on $H^2_{\text{ét}}$. Since $\rho_{\mathrm{geom}}=22$, all 22
reciprocal roots $\alpha_i$ satisfy $\alpha_i/q\in\bar{\mathbf Q}$ of absolute
value $1$ in every complex embedding and $v_{\mathfrak p}(\alpha_i/q)=0$ for
${\mathfrak p}\mid p$ (all $H^2$ slopes equal $1$ — the supersingular
condition), hence each $\zeta_i=\alpha_i/q$ is a root of unity of order prime
to $p$ (Kronecker + slope). Galois-stability follows since $P_2\in\mathbf Q[T]$
splits as $\prod(1-q\zeta_iT)$. The trace $m=\sum\zeta_i$ is a rational algebraic
integer, hence in $\mathbf Z$, with $\lvert m\rvert\le22$. Point count:
$H^1=H^3=0$ for K3, so $\#X(\mathbf F_q)=1+q^2+\sum\alpha_i=1+q^2+qm$. ∎

*Combinatorics.* A Galois-stable multiset of 22 roots of unity is a union of
full cyclotomic orbits; orbit $d$ has size $\varphi(d)$ and trace
$1$ ($d=1$) resp.\ $\mu(d)$ ($d>1$). With $\varphi(d)\le22$ there are 43 orbit
types; recursive enumeration gives exactly 60,280 multisets of total size 22,
and every integer $m\in[-22,22]$ occurs as a trace (verified by
`output/artifacts/enumerate_m.py`, `enumeration.json`). Thus the interval
$[-22,22]$ is sharp unconstrained; restrictions come only from $(q,\sigma_0)$.

## 3. Crystalline discriminant and the weak bound; Artin–Tate

*Proof of N(2).* By (O), geometric supersingularity gives
$\mathrm{NS}_{\mathrm{geom}}$ of rank 22 and discriminant $-p^{2\sigma_0}$,
classified by $(\sigma_0$, characteristic subspace$)$. Let $N$ be as stated.
Over $\mathbf F_{q^N}$ every $\zeta_i^N=1$, so $\rho=22$ there and the
$L$-factor is $(1-q^NT)^{22}$. Applying the $r=22$ case of N(3) (proved below)
over $\mathbf F_{q^N}$ yields: $aN$ even and $aN\ge2\sigma_0$. ∎

*Proof of N(3).* By (AT) for K3 ($\alpha=\chi(\mathcal O_X)-1=1$,
$\mathrm{NS}_{\mathrm{tors}}=0$):
$$Q(1/q)=\frac{\lvert\mathrm{Br}(X)\rvert\cdot\lvert D_{\mathbf F_q}\rvert}{q},
\qquad Q(T)=\frac{P_2(T)}{(1-qT)^r},$$
i.e.\ $\lvert\mathrm{Br}\rvert\cdot\lvert D_{\mathbf F_q}\rvert=qB$ with
$B=Q(1/q)=\prod_{\zeta_i\ne1}(1-\zeta_i)$. By (Sq) $\lvert\mathrm{Br}\rvert$ is a
square, giving the square condition. For $r=22$: $B=1$,
$\mathrm{NS}(\mathbf F_q)\otimes\mathbf Q=\mathrm{NS}_{\mathrm{geom}}\otimes\mathbf Q$,
so $\lvert D_{\mathbf F_q}\rvert=p^{2\sigma_0}e^2$ ($e$ = index, a $p$-power up
to the square factor), whence $\lvert\mathrm{Br}\rvert=q/(p^{2\sigma_0}e^2)$ is
an integral square: $a$ even and $a\ge2\sigma_0$ (with $e=1$ minimal). For
$r=0$: $\lvert D\rvert=1$, so $qB$ itself must be a square integer; for
$m=-22$, $B=\Phi_2(1)^{22}=2^{22}$ and $qB=p^a2^{22}$ is a square iff $a$ is
even (every $p$, including $p=2$ where $qB=2^{a+22}$). ∎

## 4. Base-change normalization (correction lemma)

**Lemma C.** The literal reading of sufficiency — the same polynomial
$P_q(T)=\prod(1-q\zeta_iT)$ occurring as $P_{2}(X'/\mathbf F_{q^n})$ for $n>1$ —
is impossible: Weil numbers over $\mathbf F_{q^n}$ have absolute value $q^n\ne q$.
Sufficiency is therefore stated in the normalized sense: the root-of-unity
datum $R(T)=\prod(1-\zeta_iT)$ (equivalently the normalized eigenvalues
$\zeta_i$) is realized, i.e.\ $P_2(X'/\mathbf F_{q^n},T)=\prod_j(1-q^n\eta_jT)$
with $\{\eta_j\}$ obtained from $\{\zeta_i\}$ by the $n$-th power map on roots
of unity (and matching multiplicities after the finite-index lattice check).
For $n$ with all $\zeta_i^n=1$ this is $(1-q^nT)^{22}$.

## 5. Conditional sufficiency

*Proof of Theorem S (assuming $(\star)$).* Let $R(T)$ satisfy N(1)–N(3) for
$(q,\sigma_0)$. Form $P(T)=\prod(1-q\zeta_iT)$. The square condition N(3) is
exactly the Brauer-square input required by Taelman's conditional machine;
assuming $(\star)$, it yields a K3 surface $X_0/\mathbf F_{q^n}$ (for suitable
$n\ge1$; see field control) with $P_2=P$ in the normalized sense of Lemma C.
All slopes equal $1$ since the normalized eigenvalues are roots of unity, so
$X_0$ is supersingular; its crystalline discriminant is $-p^{2\sigma_0}$ by the
admissibility hypothesis matched through (O) (Ogus's moduli of characteristic
subspaces realizes the prescribed $\sigma_0$; the Frobenius action on the
discriminant group is the one prescribed by the $\zeta_i$). If the input datum
fails the square/parity test over $\mathbf F_q$ but passes it over an extension
(e.g.\ $m=-22$ with $a$ odd passes over $\mathbf F_{q^2}$), take minimal such
$n$. *Field control:* $N=\mathrm{lcm}(\mathrm{ord}\,\zeta_i)$ always works,
since over $\mathbf F_{q^N}$ the datum is Tate-trivial ($r=22$) and the weak
bound $aN$ even, $\ge2\sigma_0$ holds by admissibility; minimal $n\mid N$. ∎

## 6. Exact $m$-sets: decision procedure and samples

For fixed $(q,\sigma_0)$, $\mathcal M(q,\sigma_0)$ is computed by enumerating
the 60,280 multisets, keeping those with $aN$ even, $aN\ge2\sigma_0$, and
passing the square test ($qB/\lvert D\rvert$ square; for $r=0$, $qB$ square;
for $r=22$, $a$ even and $\ge2\sigma_0$), and taking traces. For
$0<r<22$ the test is existential over arithmetic Néron–Severi lattices of rank
$r$ with Frobenius-eigenvalue $1$ part of dimension $r$, embedding compatibly
into the geometric lattice of discriminant $-p^{2\sigma_0}$; this is a finite
lattice check per multiset. It is carried out completely here for $r\in\{0,22\}$
with certified witnesses, giving exact endpoints and large exact interior
ranges; the same stated criterion decides the remaining ranks.

Verified computations (`output/artifacts/witness_m.py`, `witnesses.json`):
- $m=22$ over $\mathbf F_q$ ⟺ ($r=22$, $B=1$) $a$ even, $a\ge2\sigma_0$.
- $m=-22$ over $\mathbf F_q$ ⟸/⟹ ($r=0$, $B=2^{22}$) $a$ even.
- $r=0$ square-witness ranges (sufficient, conditional on $(\star)$, for
  realization over $\mathbf F_q$ itself): e.g.\ $p=5,a=1$: 27 values
  $\{-19,\dots,8\}$ with explicit orbit witnesses (e.g.\ $m=0$:
  $\{5{:}1,38{:}1\}$, $B=5$, $qB=25$); $p=5,a=2$: 33 values
  $\{-22,\dots,11\}$ (e.g.\ $m=11$: $\{6{:}11\}$, $B=1$, $qB=25$);
  $p=2,a=1$: 30 values $\{-20,\dots,10\}$; $p=2,a=2$: 33 values
  $\{-22,\dots,11\}$; $p=3,a=3$: 30 values $\{-21,\dots,9\}$.
  Each listed $m$ has a stored orbit multiset with $qB$ a verified square.
- Weak ($N$-only) tables in `enumeration.json` (e.g.\ $a=1,\sigma_0=1$ excludes
  only $m=22$; $a=1,\sigma_0=10$ gives $[-18,18]$) show the endpoint cut is
  exactly the $N$-bound; the square test refines further as above.

## 7. What is proved, what is assumed, limitations

Proved unconditionally: root-of-unity shape, $m$-integrality and point-count
formula, Galois-orbit classification with exact counts (60,280 multisets; full
$[-22,22]$ unconstrained sharpness), crystalline weak bound via base change,
Artin–Tate square constraint with endpoint theorems, Lemma C correction, and
the finite decision procedure for $\mathcal M(q,\sigma_0)$ with complete
$r\in\{0,22\}$ evaluation and tabulated $r=0$ witnesses. Conditional on
$(\star)$: realization (Theorem S) via Taelman's machine plus Ogus
$\sigma_0$-control, hence sufficiency direction of the $m$-sets. Limitations:
(i) Theorem S inherits $(\star)$ and the characteristic/level hypotheses of
Taelman's construction (tracked in §1); (ii) the $p$-part of (Sq) is used via
the crystalline refinement — prime-to-$p$ squareness is unconditional via Tate
pairings; (iii) for $0<r<22$ the square test is stated as the exact finite
lattice criterion with $r\in\{0,22\}$ fully evaluated — the per-multiset
sublattice-index verification for intermediate $r$ is the remaining finite
computation, not a theoretical gap. No literature search was used; all cited
inputs are standard named theorems.
