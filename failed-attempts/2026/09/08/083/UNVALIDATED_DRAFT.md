# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified crosscap cog for the Conway / Kinoshita–Terasaka mutant pair

## Status
Partial theorem (fallback scope): certified two-sided crosscap bounds and explicit
nonorientable spanning-surface witnesses for the canonical Jones-equal mutant pair
K11n34 (Conway) and K11n42 (Kinoshita–Terasaka). Exact values and mutant separation
remain open; what is proved is a replayable, machine-checked cog.

## Objects (committed data)
`output/artifacts/diagrams.json` transcribes, for K11n34 and K11n42, the KnotAtlas
PD, Gauss, and DT codes (retrieved 2026-09-08), e.g.

- K11n34 Gauss: `1,-4,2,-1,3,-7,4,-2,-5,11,-6,-3,7,10,-8,5,-9,6,-10,8,-11,9`
- K11n42 Gauss: `1,-4,2,-1,3,-7,4,-2,-5,8,-6,-3,7,10,-8,11,-9,5,-10,6,-11,9`

External data used only as cited lemmas, not as computed results: both knots are
hyperbolic of volume 11.2191, nontrivial, nontorus, signature 0, determinant 1,
unknotting number 1 (KnotAtlas pages fetched during this run).

## Definitions used
For a knot diagram with `c` crossings, a Kauffman state (choice of smoothing at each
crossing) with `s` state circles spans a state surface `F` with
`chi(F) = s - c`, hence first Betti number `b1(F) = c - s + 1`. The state graph
(vertices = state circles, edges = crossings joining the two incident circles, a loop
when both smoothings at a crossing lie on one circle) is bipartite iff `F` is
orientable; a loop or odd cycle certifies nonorientability. A nonorientable spanning
surface with `b1 = n` gives crosscap number `C(K) <= n`. `C(K) = 1` iff `K` is a
`(2,q)` torus knot (classical: Neuwirth/Fox; see e.g. Clark, *Crosscaps and knots*,
and Jaco–Rubinstein–Spreer–Tillmann arXiv:2108.07599 for the modern normal-surface
framework).

## Theorem (certified cog)
Let K in {K11n34, K11n42} with the committed diagram above. Then:

1. (Full state census, computed.) Over all 2^11 = 2048 Kauffman states, the b1
   distribution is, for EACH of the two knots,
   `{5:2, 6:30, 7:169, 8:472, 9:698, 10:522, 11:155}`.
2. (Explicit witnesses, computed.) The Seifert (all-oriented-smoothing) state has
   `s = 4`, `b1 = 8`. The states with masks 1707 (K11n34) and 1435 (K11n42) have
   `s = 7`, `b1 = 5`, and nonbipartite state graphs (explicit odd-cycle witnesses
   recorded in the worklog), hence span NONORIENTABLE surfaces with `b1 = 5`.
   Therefore `C(K) <= 5` for both knots, by an explicit in-run surface.
3. (Floor, cited.) Both knots are hyperbolic, hence nontrivial and nontorus, so
   `C(K) >= 2` for both. Hence `C(K) in {2,3,4,5}` for both knots.
4. (Tightened ceiling, cited lemma.) A crossing change alters crosscap number by at
   most 2 (Clark 1978), and both knots have unknotting number 1, so `C(K) <= 3` for
   both. Hence `C(K) in {2,3}` for both knots.

## Proof / replay
Run `python3 output/artifacts/verify.py` (stdlib only, seconds). It re-derives from
`diagrams.json`: Gauss validity, the full census of (1), the Seifert values and the
witness values/nonorientability of (2), and checks minimality of `b1 = 5` among
nonorientable state surfaces. Items (3)–(4) are short deductions from cited classical
facts recorded above. Output ends with `VERIFY_OK`.

## Mutant-separation status (honest)
No separation: every computed state-surface datum coincides for the two mutants
(identical census; same minima). The exact values `C(11n34)`, `C(11n42)` in `{2,3}`
and whether crosscap number distinguishes the pair are NOT decided here — that needs
either a `b1 <= 3` nonorientable spanning surface (below every state surface of the
committed diagrams, whose minimum nonorientable b1 is 5) or a `C >= 3` obstruction
(Goeritz/Clark–Murakami–Yasuhara signature bound or normal-surface enumeration à la
Jaco et al., unavailable in this stdlib-only environment: no Regina/SnapPy).

## What is new vs prior work
Alternating tables (Bahena–Kindred–Parsley) exclude this nonalternating pair;
2-bridge formulas (Cohen et al.) exclude bridge-index-3 mutants; Jaco et al. Table 1
new 11n values omit 11n34/11n42. The full Kauffman-state b1 census with explicit
minimal-nonorientable-state witnesses for these two diagrams is computed in-run from
committed codes, not transcribed. The interval `{2,3}` with this certificate is, to our
knowledge, the first replayable crosscap cog for the Conway/KT pair.

## Limitations
- Upper bound `C <= 5` is machine-certified from committed diagrams; `C <= 3` uses the
  external unknotting-number-1 datum + Clark's lemma (not recomputed in-run).
- Floor `C >= 2` uses external hyperbolicity (KnotAtlas volume) + the classical
  torus-knot characterization of `C = 1`.
- A Kauffman-bracket Jones computation attempted for an independent in-run unknotting
  check produced polynomials disagreeing with the tabulated Jones under all sign
  vectors (convention bug in bracket weights, parked in worklog); it is NOT used.
- No claim of exact crosscap values or mutant separation; no Regina normal-surface
  enumeration was possible in this environment.
