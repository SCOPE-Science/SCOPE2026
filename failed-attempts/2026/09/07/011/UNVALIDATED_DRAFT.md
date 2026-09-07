# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Jones collisions among braid-closure knots and links: a verified partial census with no separable pair found

## What was done
We studied Jones-collision classes in an explicit, computationally frozen
sub-universe of the audit target: **closures of braid words** (2–6 strands,
length ≤ 12, no immediate σᵢσᵢ⁻¹), rather than the full Hoste–Thistlethwaite
alternating tables (which were unreachable offline: no SnapPy/Sage/network).
Every number below is recomputed from the frozen braid words by exact
integer arithmetic in pure Python + sympy (`output/artifacts/braid_toolkit.py`).

## Methods (exact, self-contained)
- **Jones polynomial** via Kauffman bracket state sum (2ᵐ states, union-find
  circle counting) with writhe normalization; t = A⁻⁴.
- **Alexander polynomial** (knots) via Wirtinger presentation + abelianized Fox
  Jacobian minor (sympy determinant), normalized symmetric with Δ(1) = 1.
- **Linking number** for 2-component closures by signed inter-component count.
- **Screens**: knot/link component count by braid permutation; alternation by
  component traversal over/under check; reduced/minimality by Jones span = m
  (Kauffman–Murasugi–Thistlethwaite); diagram-primeness by brute-force
  no-2-edge-cut test (Menasco); split links excluded by shadow connectivity.
- **Separation logic**: distinct Alexander polynomials force distinct
  HOMFLY-PT polynomials (both specialize from HOMFLY-PT; Freyd–Yetter,
  Lickorish–Millett); distinct linking numbers force distinct Conway, hence
  distinct HOMFLY-PT, polynomials. Either would close a collision class under
  audit predicate (a) and simultaneously certify a non-mutant pair (Conway
  mutants share HOMFLY-PT).

## Validation (all pass, see `output/artifacts/verify.py`)
- Jones/Alexander match published values for unknot, trefoil (t+t³−t⁴),
  figure-8 (symmetric span 4), cinquefoil, Hopf link; RII/RIII bracket invariance.
- 360/360 independent determinant agreements |V(−1)| = |Δ(−1)| on sampled words
  (two fully independent implementations: bracket vs Fox calculus).

## Results
- **Knots**: 40,120 braid words → 11,981 knot closures → 219 Jones-collision
  classes. Of these, 26 classes contain ≥ 2 members passing all
  alternating/reduced/prime screens ("good" members); in **every** such class
  all good members share one Alexander polynomial (no HOMFLY separation).
- **Links**: 19,100 braid words → 10,717 non-split 2-component links → 141
  Jones-collision classes; 27 with ≥ 2 good members; in **every** such class all
  good members share one linking number (no HOMFLY separation).
- Hence **no closable non-mutant Jones-collision class was found** in this
  braid-closure sub-universe. Stored artifacts list every collision class with
  member braid words and Jones polynomials (`jones_collisions.json`,
  `jones_collisions_big.json`, `phase2/4/5_report.json`).

## Limitations (explicit)
1. Sub-universe only: braid words of length ≤ 12 on ≤ 6 strands; most
   ≤12-crossing alternating knots/links (higher braid index or minimal braid
   length > 12) are not covered. No full-U census is claimed.
2. No interval-certified volumes were computed (no SnapPy/HIKMOT available);
   classes whose members share Alexander/linking number (possible mutants or
   Kanenobu-type families) remain open and would need the volume branch.
3. DT codes were not cross-checked against SnapPy/Regina/KnotInfo (offline);
   diagrams here are braid words, not canonical HT codes.
4. Within-class Alexander/linking-number uniformity was checked on up to
   12–16 good members per class (caps); residual risk of a missed pair inside
   very large duplicate-heavy classes is documented, not excluded.

## Rerun
`python3 output/artifacts/verify.py` (minutes). Full search:
`search_phase1.py`, `search_phase3.py`, `search_phase5.py` (∼1–2 h total).
