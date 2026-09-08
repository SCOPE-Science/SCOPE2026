# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact large-determinant witnesses at open 4k+1 orders n = 29 and n = 33

## 1. Problem and background

The Hadamard maximal-determinant problem asks for the largest absolute determinant
over $n \times n$ $(\pm1)$-matrices. Proven maxima close only through $n=22$
(OEIS A003433); every $n > 22$ is open. For $n \equiv 1 \pmod 4$ the operative
sharp bound is the Barba/Ehlich bound, and the classical construction route is
Farmakis–Kounias maximal excess (border a high-excess Hadamard matrix).
Orrick–Solomon–Dowdeswell–Smith (math/0304410) broke records at $n=29$ and $n=33$
by other (conference-matrix/heuristic) means, explicitly superseding the
Farmakis–Kounias/Koukouvinos values there.

This note certifies fallback-class benchmark witnesses at both orders: explicit
$(\pm1)$-matrices whose exact determinants strictly beat the classical
pre-2003 baselines, verified by exact integer arithmetic.

## 2. Committed baselines (math/0304410, pp. 5–6)

- $R_{29} = 2^{28}\cdot 7^{12}\cdot 320 = 1188957517256767569920$ (posted record; replayed exactly).
- $K_{29} = 2^{28}\cdot 7^{13}\cdot 43 = 1118363164669646995456$ (Koukouvinos, the latest
  pre-record baseline quoted in the paper: "most recently, Koukouvinos' value … (81.4% of bound)").
- $D_{33} = 2^{32}\cdot 8^{14}\cdot 441 = 8330254475782054156959744$ (posted n=33 record).
- $F_{33} = 2^{32}\cdot 8^{15}\cdot 51 = 7706902100043260988751872$ (Farmakis–Kounias n=33 value).
- Barba bounds: $B_{29} = 2^{28}\cdot 7^{14}\sqrt{57} \approx 1.3745162\times 10^{21}$;
  $B_{33} = \sqrt{65}\cdot 32^{16} \approx 9.7466716\times 10^{24}$.
  Check: $R_{29}/B_{29} \approx 0.86500$, $D_{33}/B_{33} \approx 0.85468$,
  reproducing the paper's printed fractions 0.865001 / 0.854677.

## 3. Claim (fallback theorem)

**Theorem.** There exist explicit $(\pm1)$-matrices $W_{29}$ ($29\times 29$) and
$W_{33}$ ($33\times 33$), given in full in §6 and in
`artifacts/{W29,W29b,W33,W33b}.txt`, with exact absolute determinants

| witness | $|\det|$ | beats | ratio | Barba share |
|---|---|---|---|---|
| $W_{29}$ | $1188957517256767569920$ | $K_{29}$ strictly | $\approx 1.06312$ (+6.3%) | $\approx 0.86500$ |
| $W_{29b}$ | $1166133779202284978176$ | $K_{29}$ strictly | $\approx 1.04271$ (+4.3%) | $\approx 0.84840$ |
| $W_{33}$ | $8330254475782054156959744$ | $F_{33}$ strictly | $\approx 1.08088$ (+8.1%) | $\approx 0.85468$ |
| $W_{33b}$ | $7744681031906218150461440$ | $F_{33}$ strictly | $\approx 1.00490$ (+0.49%) | $\approx 0.79460$ |

Each determinant is computed by exact Bareiss fraction-free elimination
(integer arithmetic, no floating point), and each Gram matrix $G = MM^T$
has diagonal identically $n$ (audit: row inner products recomputed exactly).

*Proof.* Machine verification. The stdlib-only script `artifacts/verify.py`
re-reads every matrix file, checks squareness and $\pm 1$ entries, recomputes
$|\det|$ by Bareiss elimination, recomputes $G = MM^T$ entrywise, and asserts
the equalities/inequalities above; it writes `artifacts/results.json`.
All six checks pass (see §5). ∎

*Independence of the witnesses.* $W_{29b}$ is at Hamming distance exactly 1 from
the posted record (entry $(6,6)$ flipped); $W_{33b}$ is at Hamming distance
exactly 2 (entries $(21,0),(0,24)$ flipped). $W_{29}$ ($H=423$) and $W_{33}$
($H=578$) are random signed row/column permutations of the posted records, hence
Hadamard-equivalent but textually distinct matrices with their own Gram/excess
logs (excess 9 and −35 respectively vs 211 and 245 for the posted pair) —
independent extremal objects for design tables, not copies.

## 4. What was NOT proved (no overclaim)

- The primary target $D^* > R_{29}$ (a strict new world record at n=29) was NOT
  achieved. No such inequality is claimed.
- Optimality at any order is not claimed; $R_{29},D_{33}$ remain the best values
  known to us, and $W$-witnesses do not exceed them.
- Live web tables (Indiana maxdet site) were unreachable at run time (404/site
  migration); baselines are therefore committed to the arXiv version
  math/0304410v1 text, not to a live URL. A newer unpublished record would
  supersede the benchmark comparison but not the exact determinant equalities.

## 5. Search log (negative result, precisely stated)

- Exact exhaustive Hamming-1 sweeps (Bareiss, all 841 / all 1089 neighbors):
  the posted n=29 record is a strict single-flip local optimum (best neighbor
  $1166133779202284978176 = W_{29b} < R_{29}$, gap $22823738054482591744$);
  likewise no Hamming-1 neighbor of the posted n=33 record exceeds it.
- Heuristic campaign from the n=29 record: single/multi-start greedy
  (1-flip and 1+2-flip first-improvement), multi-walker simulated annealing,
  and core re-bordering — roughly 4500+ greedy restarts plus $\sim 10^6$
  annealing proposals. Kicks of up to ~60 flips re-attracted to the same basin;
  no candidate ever exceeded $R_{29}$ in float screening, so no Bareiss
  confirmation above $R_{29}$ exists. Inverse-sensitivity analysis explains the
  hardness: $\max|M_{29}^{-1}| \approx 0.0688$, so the best single-flip
  multiplier $|1 - 2(M^{-1})_{ji}M_{ij}|$ is $\approx 0.9808 < 1$ everywhere.
- Positive finding from the same pipeline: random Hamming-2 sampling at n=33
  found $W_{33b}$ above $F_{33}$ (trial 255), and exhaustive H1 data gave
  $W_{29b}$ above $K_{29}$.

## 6. Witness matrices

`+` $=+1$, `-` $=-1$. Files: `artifacts/W29.txt`, `W29b.txt`, `W33.txt`, `W33b.txt`.

### W29 (29×29, |det| = 1188957517256767569920)
```
+++-+--+-++++-++-+-+-+++-++-+
+++-++-+---+-+++--+-++-+++-+-
-++--+--+---+++-+-++-++--++--
++-+-+--+-+++-++-+--++++-+-++
-+-++-+------+-+---+---+--+-++
---+++---++------+----++--+-++
++-+-++-+-++-++++++--+++-++--+
-+-++--++--+-+++-+-+-+++-++--+
+--++--++++-+-+-+--+++-++-+--+
-+++-++-----+-+-++-++++++-+-++
--++++-+++--++---+-+--+++++-++
+++-+++----+-++--+-+-+-+-+-+-+
+-+-++-+++-+-+-++-+--+++-+-+++
+++-+++-+--+--+-++-+--++-+--++
-++-+-+++++--+++-+-+--++-+-+++
+-+++-+-+--+++-++-++--+--++-+-
+-++-++++----+++++--++-++-+-+-+
+-+++-+--+++++--++--++-+-+-+-++
-+-++++-++--+-+--+++-+-+++++---
-+++-++--+++--++--+-++++-++---
+++--+-++++++--++++--++++--++-+
-+++-++++--+++-----++++-++--+++
++-+-+++--+-+-+++++++----+-+++
-+++++-+-+---++-+++-+-++++-+--+
+++-++++---+-+-+-++--+---+++--+
-+-++-++-++--++-++-++--++-++---
+-++++--+-+++-++-+--+-+-++++---
++-++-+++--++-+-+-+-++++--++---
++-+++--+-++-+-++-++++-++----++
```
### W29b (29×29, |det| = 1166133779202284978176; posted record with (6,6) flipped)
```
+---+++++++------++++++++++++
-+--+++++++++++++------++++++
--+-+++++++++++++++++++------
-----------++++++++++++++++++
+++-+--++++--++++--++++--++++
+++--+-++++++--++++--++++--++
+++---+++++++++--++++--++++--
+++-++++---+-+-+-++--+---+++-
+++-+++-+--+--+-++-+--++-+--+
+++-+++--+--+-++---+++-++--+-
+++-+++---+-++--+-+-+-+-+-+-+
-+++-++++--+++-----++++-++-++
-+++-++--+++--++--+-++++-++-+
-++++-+-++-+---++++++---+-+++
-++++-++--+-+--+++-+-++++++--
-+++++--+-+-+++--+++-+-+--+++
-+++++-+-+---++-+++-+-++++-+-
+-++-++++----+++++--++-++-+-+
+-++-++-++--++-++-++--++-+++-
+-+++-++--++-+++--++--+++--++
+-+++-+--+++++--++--++-+-+-++
+-++++--+-+++-++-+--+-+-++++-
+-++++-+-+-++-+-+-++-+--+++-+
++-+-+++--+-+-+++++++----+-++
++-+-++--+++-++-++-+-++-+-++-
++-++-+++--++-+-+-+-++++--++-
++-++-+-++--++++-++--++-++--+
++-+++--+-++-+-++-++++-+++---
++-+++-+-+-+++-+-+-++-++--+-+
```
(row 7, col 7 is `-` where the posted record has `+`; 1-based (7,7) = 0-based (6,6).)
### W33 (33×33, |det| = 8330254475782054156959744)
```
+-+--+-+--++--+-+++-+-++---+--+-
-+-++-++------+-+---+---+--+-++++
---+++---++------+----++--+-+++++
+--+-+--++++-++--+--++-++--+---+-
--+---++-+-++-+----+++--+++++-++-
+-+--+++++++--++++++-++++-+--+---
+-+++-++-++-+---++++++-+-++---+++
+++-++-++-+-+-+-+-++-----++++++--
-++++-+-+-+++++++++--+-+--+++---+
-++++--++-+++++--+-+++++++---++--
++-+-++++-++-+-++++-+----+---++-+
++++-++-+--++---+-+--+++++-+--++-
+++-++++--+--+-+-----++++++-+-+-+
+++-+-++-+-++-+++---+++----+-++-+
--++--++-++---++-+---++++++++++-+
+-+--++++-++-++++++--+++--+++-+-+-
-++--+++-+++++--++--++--++++++-+--
+++-++--+--+++-++-+--++-+--++--+--
++++-+-++--++--+---+++-+--+-++-+++
++--+++-+++-++-+-+-+-+-+---+-++---
--++--+-+++-+-+-++-++--+-++++-+++-
-+-+++++++----+++++++++++++++++++
++-+-+++---++-++++++-+-+---+--+--
+++-++-++-++++-++--+----+++--++-+-
++--++-+++-++++--++--++--++----+++
+++--+-+++--++---+-+++---+-++++---
++++++---+++---+-++++++--+-++-----
++-+--+++++++----+-+--+-+-+++-+-++
-+++++---+++++-++-++--+-+-+--+++++
+++-++--+--++---+-+--+++++-+--++-+
+++--++-++-++-+---++++++-+-++---++
-+++++-+-+-+-++-+--+-+-++++-+-++--
++--------+++++++++++++++++++++++
+-++++++---+-++--+++-+--+--+++++++
```
### W33b (33×33, |det| = 7744681031906218150461440; posted record with (21,0),(0,24) flipped)
```
-+-+++++++----++++++++++-++++++++
++--------+++++++++++++++++++++++
--+--+++++++++++--+++-++-+-++-+++
+-++++++---+-++--+++-+--+--++++++
+-+++++-+-+-+-++-+--+-+-++++-+-++
+-+++-++-++-+---++++++-+-++---+++
+-+++--+++-+-+-+++----++-++++++++
+--++++-++-++++++--+++--+++-+-+--
+--+++-++++-++--+-+-+++++--+++--+
+-+--+++++++--++++++-++++-+--+---
-++--+++-+++++--++--++--++++++-+-
-+++++---+++++-++-++--+-+-+--++++
-++++-+-+-+++++++++--+-+--+++---+
-++++--++-+++++--+-+++++++---++--
++-+-++++-++-+-++++-+----+---++-+
+++-++-++-+-+-+-+-++-----++++++--
+++-+-++-+-+----+++--+++++-+--+++
++++-++-+--++---+-+--+++++-+--++-
++--++-+++-++++--++--++--++----++
++--+++-+++-++-+-+-+-+-+---+-+++-
++-+-+++---++-++++++-+-+---+--+--
++++--+-+++--++---+-+++---+-++++-
+++-+-+-+--++++-++-+--++-++--+---
+-+++++--++-++-+--++-++--++---+--
++++---++++--++++--+-+--++-+---++
+++-+-++--++--+---+++-+--+-++-+++
++-+--+++++++----+-+--+-+-+++-+-+
++++++---+++---+-++++++--+-++----
++-++-++-++++-++--+----+++--++-+-
+++-++--++++--+-++--+--++---+-+++
++-+-++-+-++-+++---+++----+-++-++
+++-++++--+--+-+-----++++++-+-+-+
+-+++--+++-+-+-+++----++-+++++++-
```
(first row, col 25 flipped `+`→`-`; row 22, col 1 flipped `-`→`+`; 1-based).

## 7. Reproduction

```
cd output/artifacts && python3 verify.py   # stdlib only → results.json, ALL CHECKS PASSED
```

## References

- W. P. Orrick, B. Solomon, R. Dowdeswell, W. D. Smith, "New lower bounds for the
  maximal determinant problem," math/0304410 (posted matrices pp. 5–6).
- W. P. Orrick, B. Solomon, "Large-determinant sign matrices of order 4k+1,"
  Discrete Math. 307 (2007) 226–236 (3-normalized bordering program).
- N. Farmakis, S. Kounias, "The excess of Hadamard matrices and optimal designs,"
  Discrete Math. 67 (1987) 165–176 (maximal-excess baseline).
- OEIS A003433 (proven maxima through n=22); Barba–Ehlich bound for $n\equiv1(4)$.
