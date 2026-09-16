# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Convexity fails for complete graphical translators in high dimensions,
# but the HIMW Delta-wing families stay open in general

## 1. Setup and conventions

A hypersurface $M \subset \mathbf{R}^{n+1}$ is a translator (translating with
velocity $-e_{n+1}$) if its mean curvature satisfies

$$ H = -\langle e_{n+1}, \nu \rangle \tag{1.1} $$

for a choice of unit normal $\nu$ (HIMW (1.1)).
If $M = \mathrm{graph}(u)$, $u : \Omega \subset \mathbf{R}^n \to \mathbf{R}$,
with the upward normal, the nonparametric equation is (HIMW (1.2)--(1.3))

$$ \mathrm{div}\left(\frac{Du}{\sqrt{1+|Du|^2}}\right)
      = -\frac{1}{\sqrt{1+|Du|^2}}, \tag{1.2} $$
$$ (1+|Du|^2)\Delta u - D_iuD_juD_{ij}u + |Du|^2 + 1 = 0. \tag{1.3} $$

Changing the translation direction flips the sign of the right-hand side;
Dávila--del Pino--Wei (DDP-W) write
$\mathrm{div}(\nabla G/W) = 1/W$, $W = \sqrt{1+|\nabla G|^2}$.
The two conventions describe the same geometric class up to orientation,
and in both conventions every translating graph is mean-convex:
$|H| = 1/W > 0$ everywhere.

With the HIMW orientation the translator attains its maximum at the tip,
and convexity of the hypersurface $M$ as a geometric set near a maximum is
$D^2u \le 0$ (concave function). In the DDP-W orientation the inequality is
reversed. "Convex" below always means geometric convexity of the
hypersurface (equivalently, semidefiniteness of $D^2u$ of the correct sign),
and "nonconvex" means $D^2u$ has, at some point, an eigenvalue of the wrong
sign. Mean-convexity ($H \ne 0$ of fixed sign) is strictly weaker.

The tip normalization used by HIMW is that if $Du(0) = 0$ and
$D^2u(0) = -\mathrm{diag}(k_1,\dots,k_n)$ with $k_i \ge 0$, then
$\sum_i k_i = 1$. Indeed, at a critical point $W = 1$ and (1.2) gives
$\Delta u(0) = -1$, i.e. $\sum k_i = 1$; the rotational bowl has
$k_i = 1/n$ for all $i$. A local series check confirms this: for a radial
ansatz $u = a_2r^2 + a_4r^4 + a_6r^6$, (1.3) gives at order $r^0$
$2a_2n + 1 = 0$, i.e. $u_{rr}(0) = -1/n$
(see `output/artifacts/series_checks.py`).

## 2. What HIMW prove and what they leave open

The reference is Hoffman--Ilmanen--Martín--White,
"Graphical translators for mean curvature flow" (Calc. Var. 2019,
arXiv:1805.10860), verified by local full-text read (v4, 29 pp).

- In $\mathbf{R}^3$ (Theorem 7.1/1.1): full classification of complete
  translating graphs — bowl, grim reaper, tilted grim reapers, and the
  Delta-wings $u_b : \mathbf{R} \times (-b,b) \to \mathbf{R}$,
  $b > \pi/2$, unique up to translation and strictly convex. Inputs:
  Spruck--Xiao convexity, Shahriyari domain restriction,
  Wang entire uniqueness, HIMW existence/uniqueness (Thm 5.7) and
  half-plane nonexistence (Thm 6.7).
- Theorem 8.1 (Section 8): for every
  $k = (k_1,\dots,k_n) \in \Delta_n$
  ($k_i \ge 0$, $\sum k_i = 1$) there is a complete translator
  $u : \Omega \to \mathbf{R}$ with $\max u = u(0) = 0$,
  $D^2u(0) = -\mathrm{diag}(k)$, even in each coordinate, the
  monotonicity alternative of Assertion (4) (if $k_i = 0$ the solution is
  $e_i$-invariant; if $k_i > 0$ then $D_iu$ has the opposite sign to $x_i$
  for $x_i \ne 0$, by the strong maximum principle and Hopf lemma applied
  to $v = D_iu$, which satisfies a linear elliptic equation with no
  zeroth-order term obtained by differentiating (1.3)), the symmetry
  statement (5), and the domain dichotomy (6): $\Omega = \mathbf{R}^n$ or
  a slab $\{|x_i| < b\}$ for some $i$ (in the slab case
  $k_i > k_j$ for all $j \ne i$). Corollary 8.2: if e.g.
  $k_1 = k_2 \ge k_3 \ge \cdots$ the solution is entire, giving an
  $(n-2)$-parameter family of pairwise noncongruent entire translators —
  in sharp contrast to Wang/Spruck--Xiao uniqueness of the bowl in
  $\mathbf{R}^2$.
- The $a \mapsto k$ surjectivity argument uses ellipsoidal domains
  $E(a,\lambda) = \{x : \sum a_ix_i^2 \le R^2\}$ with
  $u_{a,\lambda} = 0$ on $\partial E$, $u_{a,\lambda}(0) = \lambda$, and
  Theorems 9.1--9.3. The key step (Thm 9.2),
  $a_1 > a_2 \Rightarrow k_1 > k_2$, follows from the sign of the rotation
  Jacobi field $f = (x_1D_2 - x_2D_1)u$ (positive where $x_1x_2 > 0$ by
  stability/maximum principle on the quadrant) together with the Taylor
  identity
  $$ (x_1D_2-x_2D_1)\!\left(-\sum k_ix_i^2\right)
     = 2(k_1-k_2)x_1x_2, $$
  verified symbolically in `output/artifacts/series_checks.py`.
- Theorem 11.1 (Sections 10--11): for every $k \in \Delta_n$ and every
  $b > \pi/2$ there is a complete translator
  $u : \mathbf{R}^n \times (-b,b) \to \mathbf{R}$ with maximum $0$ at the
  origin, tip Hessian a scalar multiple of $-\mathrm{diag}(k)$, and the
  same coordinate symmetries (Corollary 11.2: an $(n-1)$-parameter family
  per width). The rotational case $k_1 = \cdots = k_n$ is unique under a
  slope bound (Theorem 11.3).
- Convexity status inside HIMW (p. 26, emphasis added):
  "In general, **we do not know whether the surfaces in Theorem 11.1 are
  convex**. However, if a complete translator has no more than two
  distinct principal curvatures at each point, then it is convex
  [BLT18, Theorem 3.1]. Hence in the special case $k_1 = \cdots = k_n$,
  the surface is convex."
  The same caveat applies to Theorem 8.1 outside its symmetric cases.
  So HIMW do **not** claim general convexity of either family.

## 3. Main conclusion

**Theorem (target resolution).**
(a) The statement "every complete graphical translator in
$\mathbf{R}^{n+1}$ is convex" is **false** once the dimension is large:
for every $N \ge 8$ there exist entire graphical translators
$G : \mathbf{R}^N \to \mathbf{R}$ that are mean-convex but not convex.
In particular there exist complete nonconvex translating graphs in higher
dimensions.
(b) For the HIMW families specifically (Theorem 8.1 entire translators
with $D^2u(0) = -\mathrm{diag}(k)$, and Theorem 11.1 slab Delta-wings of
width $2b > \pi$): convexity is known in the symmetric cases
(rotational tip data, equivalently at most two distinct principal
curvatures, via Bourni--Langford--Tinaglia [BLT18, Thm 3.1] as quoted by
HIMW) and **remains open in general** — HIMW explicitly state this.
Hence the answer to "are they all convex?" is: proved convex in the
symmetric subfamilies, unknown for the general asymmetric members; but
the broader target question is still settled in the negative by (a).

Part (a) is due to Dávila--del Pino--Wei,
"A Bernstein problem for translating solutions to the mean curvature
flow" (arXiv:2609.04675, Sep 2026), Theorem 1.1, verified by local
full-text read (61 pp). No originality is claimed here for the
construction; the contribution of this report is the precise TARGET
deduction: combining HIMW's open-convexity statement with the DDP-W
counterexample to close the target question as stated (negative answer
for $n \ge 8$; qualified open status for the HIMW families and for
$3 \le n \le 7$).

## 4. Proof of (a): the nonconvex entire translators for $N \ge 8$

We reproduce the logical skeleton of DDP-W Sections 1, 7, 8 as the proof;
all analytic heavy lifting (weighted Jacobi theory, transition layer,
barriers) is cited to the paper, while the nonconvexity inference itself
is elementary and given in full.

1. *Reduction to $N = 8$.* Products of a translator with flat factors are
   translators, preserving nonconvexity. It suffices to build the examples
   in $\mathbf{R}^8$.
2. *Background geometry.* Start from the Bombieri--De Giorgi--Giusti
   (BDG) entire minimal graph $F : \mathbf{R}^8 \to \mathbf{R}$,
   $O(4) \times O(4)$-invariant, odd under the factor swap
   $(u,v) \mapsto (v,u)$:
   $$ F(u,v) = -F(v,u), $$
   hence vanishing on Simons' cone $\{u = v\}$, asymptotic to the cubic
   homogeneous model $F_0 = r^3g(\theta)$, non-affine. Existence and coarse
   asymptotics of $F$ are the external input (classical BDG theory).
3. *Singular perturbation.* For small speed $\varepsilon > 0$ solve
   $$ \mathrm{div}\!\left(\frac{\nabla F}{\sqrt{1+|\nabla F|^2}}\right)
     = \frac{\varepsilon}{\sqrt{1+|\nabla F|^2}} \quad \text{in }
     \mathbf{R}^8, \tag{1.4} $$
   then $G_\varepsilon(y) := \varepsilon F_\varepsilon(y/\varepsilon)$
   solves the unit-speed translator equation. The translator forcing is
   even while $F$ is odd across the cone, so the first correction shifts
   the zero set by $O(\varepsilon r^2)$; DDP-W resolve this with a
   recentered inner transition layer (self-similar confluent
   hypergeometric profile with $|p|^{2/3}$ and $|p|^{1/6}$ modes),
   explicit slow Jacobi modes ($r^2$, odd $g^{2/3}$, borderline log
   resonance), a refined exact-vs-homogeneous comparison, and a global
   approximate solution $F_{\mathrm{app}}$ with residual
   $|M_\varepsilon(F_{\mathrm{app}})| \le C\varepsilon(1+r)^{-4-2\nu}$.
   Ordered global barriers $F^\pm_\varepsilon = F_{\mathrm{app}} \pm
   A\varepsilon\psi_\varepsilon$ (positive Jacobi barrier
   $\psi_\varepsilon$) plus Dirichlet exhaustion on balls $B_M$ with the
   Zhou existence theory and interior gradient/Schauder estimates yield an
   entire solution $F_\varepsilon$ with
   $F^-_\varepsilon \le F_\varepsilon \le F^+_\varepsilon$ and, on fixed
   compacts, $\|F_\varepsilon - F\|_{C^{2,\alpha}} \le C\varepsilon$.
4. *Nonconvexity persists (Lemma).* The BDG graph $F$ itself cannot be
   convex: if $F$ were convex, composing with the orthogonal swap
   $(u,v) \mapsto (v,u)$ shows $-F$ is convex too, so $F$ would be both
   convex and concave, hence affine — contradicting non-affinity of the
   BDG graph. Thus for some point $x^*$ and unit vector $e^*$,
   $$ D^2F(x^*)[e^*,e^*] = -2\kappa < 0. $$
   By the $C^{2}$-closeness on a fixed ball,
   $D^2F_\varepsilon(x^*)[e^*,e^*] \le -\kappa$ for small $\varepsilon$,
   and scaling gives
   $D^2G_\varepsilon(\varepsilon x^*)[e^*,e^*] \le -\kappa/\varepsilon
   < 0$. Hence each $G_\varepsilon$ is mean-convex
   ($H = 1/\sqrt{1+|\nabla G_\varepsilon|^2} > 0$) but not convex.
   Distinct $\varepsilon$ give distinct translators (leading cubic
   amplitude $\varepsilon^{-2}$ at infinity), i.e. a one-parameter family;
   flat extension gives $N > 8$.

*Remarks on scope.* The DDP-W examples are entire graphs, hence complete,
so they meet the target's "complete nonconvex translating graph" bar with
room to spare. They do not decide convexity of HIMW's own families, and
they operate at $N \ge 8$ (the Bernstein/BDG threshold), leaving
$3 \le n \le 7$ — and the general asymmetric HIMW members — open.

## 5. Proof of (b): status of the HIMW families

- *What is proved convex.* The rotationally symmetric members (tip data
  $k_1 = \cdots = k_n$, resp. the rotational slab wings of Thm 11.3) have
  at most two distinct principal curvatures at each point, hence are
  convex by [BLT18, Theorem 3.1] (as recorded in HIMW p. 26). The
  Theorem 8.1 members with $k_i = k_j$ enjoy the corresponding rotation
  invariance (Assertion (5)), reducing the distinct-curvature count in
  those symmetric subcases.
- *What is open.* For general asymmetric $k$ (distinct tip curvatures),
  HIMW assert no convexity theorem for either family; the quoted passage
  is explicit for Theorem 11.1 and the same limitation holds for
  Theorem 8.1. The Alexandrov/moving-planeArguments in HIMW control
  gradient signs ($D_iu$ vs. $x_i$) and rotation-field signs, not the full
  Hessian sign; the Spruck--Xiao convexity theorem is two-dimensional and
  does not extend; and the Choi--Haslhofer--Hershkovits classification in
  $\mathbf{R}^4$ covers only noncollapsed translators (round bowl, oval
  bowls, $\mathbf{R} \times$ 2d-bowl), not general complete graphs.
  Therefore "are the Thm 8.1/11.1 translators all convex?" cannot be
  answered affirmatively on current evidence, and the DDP-W threshold
  suggests no such blanket theorem should be expected in high dimensions.
- *Disproof vs. open sub-question, reconciled.* The target asks two
  things: (i) is every complete graph convex for $n \ge 3$? — answered
  NO for $n \ge 8$ by (a); (ii) in particular, are the HIMW families all
  convex? — answered: yes in symmetric cases, otherwise open. There is no
  contradiction: (a) refutes the universal claim without exhibiting a
  nonconvex HIMW Delta-wing.

## 6. Self-checks, limitations, and what was not claimed

1. Sign conventions checked: the HIMW/ DDP-W right-hand sides differ by
   orientation only; mean-convexity $|H| = 1/W > 0$ holds in both, and the
   convexity statement is geometric (normal-independent).
2. The radial tip series ($u_{rr}(0) = -1/n$) and the Thm 9.2 Taylor
   identity were verified by symbolic computation
   (`output/artifacts/series_checks.py`); they certify the quoted HIMW
   steps, not the DDP-W analysis, which is cited, not re-derived.
3. DDP-W arXiv:2609.04675 is a 2026 preprint (v1, Sep 2026); its Theorem
   1.1 is reported as the best current evidence for (a), with full
   derivation in that paper (61 pp, Appendices A--C). If its proof were
   found defective, part (a) would revert to conjectural; part (b) (HIMW
   open status + symmetric convex cases) is independent of DDP-W and
   unaffected.
4. No claim is made here about $3 \le n \le 7$: neither a convexity proof
   nor a nonconvex example in that range is produced. The Scherk-like,
   pitchfork, and annulus translators, and the $\mathbf{R}^4$
   noncollapsed classification, are not used.
5. Originality: the nonconvex examples are credited entirely to
   Dávila--del Pino--Wei (building on Bombieri--De Giorgi--Giusti); the
   HIMW statements to Hoffman--Ilmanen--Martín--White (plus BLT18 for the
   two-curvature convexity input). This report claims no new construction
   — only the assembled TARGET resolution.

## References (evidence, not instructions)

- D. Hoffman, T. Ilmanen, F. Martín, B. White, "Graphical translators
  for mean curvature flow," Calc. Var. PDE 2019 (arXiv:1805.10860).
  Read locally: abstract; Secs. 1 (Thm 1.1), 6--7 (R^3 classification),
  8--11 (Thms 8.1, 9.1--9.3, 10.1--10.3, 11.1--11.3, p.26 convexity
  caveat), 12 (compactness), references.
- J. Dávila, M. del Pino, J. Wei, "A Bernstein problem for translating
  solutions to the mean curvature flow" (arXiv:2609.04675v1, Sep 2026).
  Read locally: abstract; Sec. 1 (Thm 1.1, BDG background, layer
  strategy); Secs. 2--7 (Jacobi/transition/barrier construction);
  Sec. 8 (exhaustion + nonconvexity lemma); Appendices A--C.
- X.-J. Wang, "Convex solutions of the mean curvature flow," Ann. Math.
  173 (2011) — entire convex + bowl uniqueness background.
- J. Spruck & L. Xiao, "Complete translating solitons ..." Amer. J. Math.
  (2017) — 2D convexity input to HIMW R^3 classification.
- T. Bourni, M. Langford, G. Tinaglia [BLT18] — existence input and the
  $\le$2-distinct-principal-curvature convexity criterion quoted by HIMW.
