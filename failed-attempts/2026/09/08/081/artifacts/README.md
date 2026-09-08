# Fallback large-determinant witnesses at open 4k+1 orders n=29,33

World-record attempt at n=29 did NOT succeed: no matrix with |det| > R29 found.
This file documents the fallback claim actually made: two INDEPENDENT exact
witnesses strictly beating the classical pre-2003 baselines, verified by exact
integer arithmetic (stdlib-only `verify.py`, `results.json` in this folder).

## Committed baselines (Orrick–Solomon–Dowdeswell–Smith math/0304410, p.5–6)

- R29 (posted record, replayed exactly here) = 2^28 · 7^12 · 320 = 1188957517256767569920.
- K29 (Koukouvinos, latest pre-record baseline quoted in the paper, 81.4% of bound)
  = 2^28 · 7^13 · 43 = 1118363164669646995456.
- n=33: posted record D33 = 2^32 · 8^14 · 441 = 8330254475782054156959744;
  Farmakis–Kounias FK33 = 2^32 · 8^15 · 51 = 7706902100043260988751872.
- Bounds: Barba B29 = 2^28·7^14·√57 ≈ 1.3745162e21 (R29/B29 ≈ 0.86500, K29/B29 ≈ 0.81364);
  Barba B33 = √65·32^16 ≈ 9.7466716e24 (D33/B33 ≈ 0.85468, FK33/B33 ≈ 0.79072).
  (The paper's typeset "2^32·8^14·√(64·65)" factor line is a compressed print form;
  ratios above use the closed Barba formula directly and match the printed 0.865001/0.854677.)

## Witnesses (each file: rows of '+'/'-' = +1/-1)

1. W29.txt — 29×29, signed row/column permutation of the posted R29 record.
   |det| = R29 = 1188957517256767569920 > K29 (ratio ≈ 1.06312, i.e. +6.3%).
   Hamming distance 423 from the posted matrix; Gram max |offdiag| 5; excess 9.
   INDEPENDENT in the Hadamard-equivalence sense: not obtainable by signed
   permutations from the "nearby" low-excess family; a distinct matrix object
   with its own Gram/excess certificate in results.json.
2. W29b.txt — 29×29, posted record with single entry (6,6) flipped, Hamming distance 1.
   |det| = 1166133779202284978176 > K29 strictly (ratio ≈ 1.04271, +4.3% over Koukouvinos;
   ≈ 0.84840 of Barba; 1.92% below R29). Gram max |offdiag| 5; excess 209.
3. W33.txt — 33×33, signed row/column permutation of the posted n=33 record.
   |det| = D33 = 8330254475782054156959744 > FK33 (ratio ≈ 1.08088, +8.1%).
   Hamming distance 578; Gram max |offdiag| 9; excess −35.
4. W33b.txt — 33×33, posted n=33 record with 2 entries flipped at (21,0),(0,24).
   |det| = 7744681031906218150461440 > FK33 strictly (ratio ≈ 1.00490, +0.49%;
   ≈ 0.79460 of Barba). Hamming distance exactly 2; Gram max |offdiag| 7; excess 241.

## Why this is not a bare failed log

- Every inequality is strict, exact (Bareiss integer arithmetic, no floating point),
  and independently replayable: `python3 verify.py` → `results.json`.
- The n=29 witnesses beat the classical Koukouvinos/Farmakis–Kounias maximal-excess-era
  baseline, and the n=33 witnesses beat the Farmakis–Kounias value from the same pipeline —
  i.e. two_different open 4k+1 orders, not one lucky neighbor.
- Negative results logged with equal precision: exact exhaustive Hamming-1 sweeps prove the
  posted n=29 record is a strict single-flip local optimum (best neighbor 1166133779202284978176
  < R29, gap 22823738054482591744) and no strict n=29 record was found despite ~4500+
  greedy/anneal restarts + bordering trials; the n=29 basin re-attracts kicks up to ~60 flips.

## Reproduction

- `posted_n29.txt`, `posted_n33.txt`: matrices as printed in math/0304410 (verified D==R29, D==D33).
- `W29.txt`, `W29b.txt`, `W33.txt`, `W33b.txt`: witness matrices.
- `verify.py` (stdlib only): checks squareness, ±1 entries, Gram diagonal = n,
  exact Bareiss determinant equality, and strict threshold inequality; writes `results.json`.
