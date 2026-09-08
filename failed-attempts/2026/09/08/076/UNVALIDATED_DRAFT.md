# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Verified systole census over smooth regular-polygon gluings (genus 2 and 3)

## Claim (fitted to evidence)

**Theorem (verified W-ball systole census with Bolza-type extremal witness).**
Let $P_n$ be the regular hyperbolic $n$-gon with interior angle $2\pi/n$
($n=8$: genus 2; $n=12$: genus 3). Among orientation-preserving side-pairings:

- $n=8$: 105 pairings total, exactly **21 smooth** (single vertex cycle).
- $n=12$: 10395 pairings total, exactly **1485 smooth**.

For every smooth gluing, explicit $SU(1,1)$ side-pairing generators are
constructed by midpoint-frame transport, the edge-loop vertex relation closes
to $\pm I$ (residuals $\le 1.1\times 10^{-13}$ genus 2, $\le 1.3\times 10^{-12}$
genus 3), and a reduced-word BFS certifies the $W$-ball systole minimum:

- **Genus 2 ($W=6$):** the opposite pairing
  $\{\{0,4\},\{1,5\},\{2,6\},\{3,7\}\}$ has $W$-ball minimum
  $2\,\mathrm{arcosh}(1+\sqrt2)=3.05714183896\ldots$ (50-digit mpmath
  enclosure agrees to all digits; trace $=2+2\sqrt2$ exactly up to
  $10^{-50}$-scale roundoff), uniquely maximal in the census; the other 20
  gluings all have $W$-ball minimum $2.2567679299\ldots$ (gap $0.8004$).
- **Genus 3 ($W=4$):** distribution $1214 \times 2.4718020467$,
  $264 \times 3.2510592692$, $7 \times 3.3257716488$; the opposite pairing
  $\{\{0,6\},\{1,7\},\{2,8\},\{3,9\},\{4,10\},\{5,11\}\}$ is one of the top-7
  attainers at $3.3257716488$ (gap $0.0747$ over runner-up tier).
- No reduced word in either census ball is elliptic or parabolic
  ($\mathrm{ell}=\mathrm{par}=0$ on all $21+1485$ rows), and collar-lemma
  half-widths / area data are tabulated as one-sided consistency checks.

## Status of "systole" vs "$W$-ball minimum" (honesty clause)

Each tabulated value is **rigorously an upper bound** on the true systole
(realized by the logged word) and **certified minimal within the stated
reduced-word ball** ($W=6$ genus 2, $W=4$ genus 3, plus $W=5$ spot rechecks on
9 genus-3 representatives with no change). Global minimality over all words
is **not** certified; it is conjectured (not claimed) that the $W$-ball
minima equal the true systoles. The extremal-witness lemma (Bolza value and
trace identity) is exact regardless.

## Method (replayable)

1. **Combinatorics (exact, stdlib):** enumerate all fixed-point-free
   involutions (105 / 10395); single-vertex-cycle filter by union-find,
   cross-checked by the permutation $\tau(v)=\pi(v)-1$ being a single
   $n$-cycle on all smooth rows.
2. **Geometry:** regular-polygon data from the exact right-triangle formula
   $\cosh d=\cot(\pi/n)$, $\cosh R=\cot^2(\pi/n)$; interior angle verified
   numerically ($\pi/4$ to $10^{-12}$ for $n=8$); side-pairing generators by
   midpoint-frame transport $g=\phi_i^{-1}R_\theta\phi_j$ with
   $\theta=\arg(-t_i)-\arg(t_j)$ (midpoint error $\le 1.1\times 10^{-15}$,
   $\det=1$ to $10^{-12}$, centers mapped strictly outside).
3. **Discreteness:** Poincar\u00e9 polygon theorem applies (all vertex angles
   $2\pi/n$ with one $n$-cycle give angle sum $2\pi$; side-pairings are
   hyperbolic/parabolic-free in-ball); the edge-loop relation residual to
   $\pm I$ is the machine-checkable certificate (max above).
4. **Spectrum:** BFS over reduced words in the free group on $n/2$ letters to
   cutoff $W$; length via $L=2\,\mathrm{arcosh}(|\mathrm{tr}|/2)$;
   cyclically non-reduced words skipped (they repeat shorter conjugacy
   classes); minimum + runner-up recorded per gluing with realizing words.
5. **Collar cross-check:** for each tier, $w=\mathrm{arsinh}(1/\sinh(L/2))$
   and area $4\pi(g-1)$ tabulated; no contradiction (positive widths,
   disjoint-collar area bound respected).

## Evidence

- `output/artifacts/census_n8_W6.json` — 21 rows (genus 2, $W=6$).
- `output/artifacts/census_n12_W4.json` — 1485 rows (genus 3, $W=4$).
- `output/artifacts/verify_audit.py` — independent replay: rebuilds
  generators from pairings, rechecks smoothness + relation + realizing-word
  length + $W$-ball minimality. Result:
  `census_n8_W6.json: VERIFY_OK (21 rows, 0 fails)`,
  `census_n12_W4.json: VERIFY_OK (1485 rows, 0 fails)`.

## Tables (head)

Genus 2 ($W=6$): 20 rows at $2.2567679299$, 1 row (opposite pairing) at
$3.0571418390$ with runner-up $4.8969$ (margin $1.8398$).

Genus 3 ($W=4$): $1214$ rows at $2.4718020467$, $264$ at $3.2510592692$,
$7$ at $3.3257716488$; top-7 indices/pairings/words:

| idx | pairing | $W$-min | word | runner-up |
|-----|---------|---------|------|-----------|
| 366 | [0,4],[1,5],[2,8],[3,9],[6,10],[7,11] | 3.3257716488 | (g0,g1^{-1}) | 3.6828 |
| 408 | [0,4],[1,7],[2,8],[3,11],[5,9],[6,10] | 3.3257716488 | (g0,g3) | 3.6828 |
| 729 | [0,6],[1,7],[2,8],[3,9],[4,10],[5,11] | 3.3257716488 | (g0,g1^{-1}) | 3.9833 |
| 740 | [0,6],[1,7],[2,10],[3,11],[4,8],[5,9] | 3.3257716488 | (g0,g1^{-1}) | 3.6828 |
| 776 | [0,6],[1,9],[2,10],[3,7],[4,8],[5,11] | 3.3257716488 | (g0,g5) | 3.6828 |
| 1023 | [0,8],[1,5],[2,6],[3,9],[4,10],[7,11] | 3.3257716488 | (g0,g5) | 3.6828 |
| 1074 | [0,8],[1,9],[2,6],[3,7],[4,10],[5,11] | 3.3257716488 | (g0,g1^{-1}) | 3.6828 |

## Limitations / uncertainty

- True-systole optimality beyond the word cutoff is **conjectural**; the
  fallback-grade claim actually proved is the $W$-ball census + realized-word
  upper bounds + one-sided collar consistency + exact Bolza trace witness.
- The Bolza value $2\,\mathrm{arcosh}(1+\sqrt2)$ itself is classical and is
  replayed as a witness, not claimed as a new inequality.
- Genus-3 top tier ($3.3257$, 7 gluings) is a $W$-ball maximum within this
  regular-polygon scope, not a new global genus-3 maximum claim.
- Interval arithmetic enclosures (e.g. directed-rounding certificates) were
  not produced; verification is double-precision replay + 50-digit mpmath
  witness for the Bolza trace, which is strong evidence but not a
  fully interval-certified proof.
