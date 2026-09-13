# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Heegaard distance at least four over the finite high-dilatation magic census (vacuous resolution)

## Claim (TARGET route)
Let $N$ be the magic manifold (complement of the 3-chain link, 3-cusped
hyperbolic). Let $F$ be the finite set of closed manifolds obtained by filling
all three cusps along slopes $p_i/q_i$ in lowest terms with $0<|q_i|\le 5$ and
$|p_i|\le 8$, excluding the Martelli–Petronio exceptional (non-hyperbolic)
list, satisfying minimum normalized slope length $L>6$, and such that the
filled manifold fibers over the circle with closed genus-2 fiber and
pseudo-Anosov monodromy of dilatation $2.30<\lambda\le 2.90$.
Then $F$ is **empty**. In particular the universal statement "every $M\in F$
is hyperbolic and satisfies Hempel distance $d(M)\ge 4$" holds vacuously, and
no distance-shorting certificate ($d(M)\le 3$) is required of any member.

## What is proved
We prove that **no** triple filling in the stated slope box with $L>6$ fibers
with closed genus-2 fiber — hence $F=\varnothing$ before the
Martelli–Petronio exclusion, hyperbolicity, dilatation-window, and Heegaard
filters are even applied (each of which can only shrink $F$ further).

## Proof
The argument is a finite computation with exact integer steps except for the
slope-length classification, whose margins ($0.10$ and $0.33$ at the $L=6$
boundary vs.\ floating-point error $\sim 10^{-9}$) are recorded in the
artifacts.

### 1. The manifold and its framings
The magic manifold is the exterior of the circular 3-chain link: three
unknots pairwise forming Hopf links (verified in SnapPy: link `L6a5` has three
unknotted components whose pairwise sublinks are 2-crossing Hopf links with
linking number $1$; exterior volume $5.3334895669$, $H_1=\mathbb Z^3$).
Its exterior is isometric (SnapPy `is_isometric_to`, common isometry signature
`svLvLQLAzQMMQdifhjmlknlopnqpqrrroaaaaaaoaaaaaaoaaao`) to the census manifold
`s776` and the link exterior `6^3_1`. These models carry *different*
peripheral framings (cusp shapes $+1.5+1.32i$, $-1.5+1.32i$, $+0.5+1.32i$,
differing by integer shears; two-cusp fill homology fingerprints differ), so
slope coordinates $(p,q)$ mean different curves in each model. To make the
conclusion framing-independent we run the full pipeline in **all three**
models; $F$ is empty in each.

### 2. Slope-length classification
For each model, maximal disjoint embedded cusp neighborhoods are obtained from
SnapPy (`cusp_areas`, `cusp_translations`), and the normalized length of
$p\,m+q\,\ell$ on the unit-area cusp is $|pm+q\ell|/\sqrt{A}$.
All three cusps are symmetric (length functions agree to $<10^{-6}$).
Over the integer box $0<|q|\le 5$, $|p|\le 8$, $\gcd(p,q)=1$:
- s776-model: 44 signed / 22 unsigned slopes pass $L>6$; min passing
  $6.3296$, max failing $5.8968$.
- `6^3_1`-model: 52 signed / 26 unsigned; min passing $6.3296$, max failing
  $5.8968$.
- `L6a5`-model: 52 signed / 26 unsigned; min passing $6.3296$, max failing
  $5.8968$.
No slope lies within $0.10$ of the $L=6$ boundary, so the passing sets are
robust to floating-point error.

### 3. Homology screen (exact)
Closed fibered $M$ has $b_1(M)\ge 1$. Filling all ordered triples of unsigned
passing slopes (cusps labeled) and computing $H_1$ exactly (SnapPy/Smith
normal form):
- s776: $22^3=10648$ triples, of which $6$ have $b_1\ge 1$ (2 unordered
  classes, $H_1=\mathbb Z/8+\mathbb Z$ and $\mathbb Z/5+\mathbb Z$).
- `6^3_1`: $26^3=17576$ triples, of which $57$ have $b_1\ge 1$ (14 unordered
  classes; $39\times\mathbb Z$, $9\times\mathbb Z/3+\mathbb Z$,
  $6\times\mathbb Z/2+\mathbb Z$, $3\times\mathbb Z/5+\mathbb Z$).
- `L6a5`: $26^3=17576$ triples, $57$ with $b_1\ge 1$ (same distribution).
Every survivor has $b_1$ **exactly** $1$ (abelianized-relator nullspace is
1-dimensional in each class).

### 4. Alexander-degree obstruction (exact)
Let $M$ be closed, fibered with closed genus-$g$ fiber $F$ and $b_1(M)=1$.
The infinite cyclic cover is $F\times\mathbb R$, so the Alexander module is
$H_1(F;\mathbb Z)\cong\mathbb Z^{2g}$ with $t$ acting by the monodromy, and
$\Delta_M(t)=\det(tI-f_*)$ has degree exactly $2g$ (and
$\Delta_M(1)=\pm|\mathrm{Tors}\,H_1(M)|$). For genus $2$ this forces
$\deg\Delta_M=4$.
For each survivor class we compute $\Delta_M$ exactly by Fox calculus on the
SnapPy presentation (integer-exponent arithmetic; code validated to reproduce
$\Delta=t^2-t+1$ for the trefoil, $t^4-t^3+t^2-t+1$ for $T(2,5)$, and
$\pm(t^2-3t+1)$ for the figure-8 from SnapPy presentations). Results:
- s776 classes: $\Delta$ of degrees $8$ and $6$ (both non-monic, leading
  coefficient $2$ — independently nonfibered).
- `6^3_1` classes: 14 polynomials, degrees $\{8,10,12,14,16,18,20\}$.
- `L6a5` classes: 14 polynomials, degrees $\{8,10,12,14,16,18,20\}$.
Every polynomial satisfies $\Delta(1)=\pm|\mathrm{Tors}\,H_1|$ (28/28 and
$2/2$ checks) and reciprocal symmetry $\Delta(t)=\pm t^{\deg}\Delta(t^{-1})$
as required for closed orientable manifolds. **No survivor has degree $4$.**
Hence no $L>6$ filling in the box fibers with closed genus-2 fiber, in any
framing. The Martelli–Petronio exclusion, hyperbolicity verification,
dilatation window, and Heegaard-distance estimates are moot: $F=\varnothing$.

### 5. Conclusion
$F$ is empty, so "every $M\in F$ is hyperbolic with $d(M)\ge 4$" holds
vacuously. This is a complete TARGET resolution (finite-census universal with
empty census), not a fallback or emergent finding.

## Evidence summary
- `output/artifacts/slope_lengths.json` — s776 cusp data, 44 passing slopes,
  boundary margins.
- `output/artifacts/homology_scan.json` — s776 full $10648$-triple scan, 6
  survivors.
- `output/artifacts/alexander.json` — s776 survivor Alexander data
  (non-monic, degrees 8 and 6).
- `output/artifacts/linkbasis_scan.json` — `6^3_1` full $17576$-triple scan,
  57 survivors in 14 classes.
- `output/artifacts/linkbasis_alexander.json` — `6^3_1` Alexander degrees
  8–20.
- `output/artifacts/L6a5_scan.json`, `output/artifacts/L6a5_alexander.json` —
  same for the `L6a5` chain-link framing.
- `work/*.py`, `work/fox.py` — reproducible pipeline and validated
  Fox-calculus code.

## Limitations and uncertainties
- Slope lengths use floating-point maximal-cusp geometry; the classification
  is rigorous only via the recorded margins (nearest slope to $L=6$ is
  $0.10$ away; SnapPy numerical error is $\sim 10^{-9}$). No interval
  arithmetic certificate (e.g.\ SnapPy `verified=True` inside Sage) was
  available in this environment.
- The Alexander-degree theorem ($\deg\Delta=2g$ for closed fibered,
  $b_1=1$) is standard (mapping-torus/infinite-cyclic-cover argument
  sketched above); we do not re-prove the Thurston-norm/fibration background.
- The identification "magic manifold = circular 3-chain exterior" rests on
  SnapPy isometry plus the component/sublink diagnostics recorded above and
  the Martelli–Petronio description; a fully framing-certified comparison
  against MP's printed slope tables was not needed since all framings give
  the empty census.
- Hyperbolicity, dilatation, and Heegaard-distance computations were not
  performed for any member because the census is empty; the $L>6$ theorem,
  train-track dilatations, and subsurface-projection machinery are
  inapplicable to the vacuous universal.
