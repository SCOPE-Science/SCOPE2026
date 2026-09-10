# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified seed fragment (NOT a claim): one replayed Csorgo-type loop of order 128

**Status: fragment only — NO_RESULT. This draft documents a verified construction;
it does NOT assert the target K_C census, the fallback exact-N1 census, or any new isomorphism type.**

## 1. Seed (G0, Z0) — from-scratch presentation
- Points: `{0,...,127}`, encoding `elem = u | (c << 3)`, `u in F2^3` (low 3 bits), `c in F2^4` (high 4 bits).
- Group law: `(u1,c1)(u2,c2) = (u1+u2, c1+c2+theta(u1,u2))`,
  `theta(u,v) = ((u0 v1), (u0 v2), (u1 v2), 0)` (upper-triangular bilinear cocycle, bits of `c`).
- `Z0 = {0, 64}` (extra central direction `f0`, bit 6). `M = Z(G0) = {u=0}` (order 16).
- `G0' = {u=0, c3=0}` (order 8); generators `e1=1,e2=2,e3=4` with
  `[e1,e2]=8=c1, [e1,e3]=16=c2, [e2,e3]=32=c3`.
- `K = G0/Z0`: order 64, `K' = G0'Z0/Z0` order 8 `= Z(K)`, both elementary abelian,
  `K/K'` order 8 elementary abelian — i.e. (7.1) of Drapal–Vojtechovsky.
- Verified: identity/inverses, full `128^3` associativity, `|G0'|=8`, `|Z(G0)|=16`, class 2.

## 2. Deformation datum (delta, mu), trilinear log
- `delta` (bit-valued, central value = bit `<< 6`):
  `dM(m,u) = (m1·u2) ^ (m2·u1) ^ (m3·u0)` where `m1,m2,m3` are the low-3 `c`-bits
  (D = anti-identity matrix `[[0,0,1],[0,1,0],[1,0,0]]`), `delta(a,b) = dM(a,u(b)) ^ dM(b,u(a))`,
  free transversal parameters `delta_T = 0`.
- `mu(a,b) = dM(a,u(b))` (Lemma-5.2-style trivial-`tau` choice).
- Verified: (B1)(B2) by construction; (B3) exhaustive over `G'`-adjacent triples;
  (B4) full `128^3` replay; `g(e1,e2,e3) = d([e1,e2],e3)d([e2,e3],e1)d([e3,e1],e2) = 1` (nontrivial);
  `Rad2(delta) = {0,64} = Z0`; `mu` satisfies (A1) fully and (A2)(A3) on `M`-adjacent triples.
- Loop: `x*y = (x·y) ^ (mu(x,y)<<6)`.

## 3. Loop replay (machine-checked by `artifacts/verify.py`, `VERIFY_OK` ~9 s)
- Loop axioms: two-sided identity 0; all 128 rows and 128 columns are permutations (Latin).
- Inner maps: `L(x,y) = L_{x*y}^{-1} L_x L_y`, `R(x,y) = R_{x*y}^{-1} R_y R_x`, `T(x) = R_x^{-1} L_x`:
  all fix 0; 64 distinct permutations; **zero non-commuting pairs** (abelian Inn);
  element orders `1×1, 2×63`; generated group order 64, i.e. `Inn ≅ (Z2)^6` (elementary abelian).
- Class 3: `Z(Q) = {0,64)` order 2; `Q/Z(Q)` nonabelian (witness `(1,2): 11 vs 3`);
  second center lift has 8 cosets (`|Z2| = 16`); associator witness `(1,2,4)`: `(1*2)*4 = 127`
  vs `1*(2*4) = 63`. Hence class exactly 3 (center order 2, nonabelian class-2 quotient).
- Trilinear log: `g` is the determinant on `G/M ≅ F2^3` (nontrivial alternating form).

## 4. Deliberately NOT claimed
- **Not** the full `K_C` census (would need all 125/106/10 setup groups, all parameters, isomorphism classification).
- **Not** the fallback exact-`N1` count: the `delta_T` free-bit transversal (`~2^21` scale) and `mu`-`tau`
  parameters were **not** exhaustively examined, and cross-transversal isomorphism collapse was not computed,
  so the binary coverage criterion fails. A 512-matrix `D`-screen found the anti-identity (`n=84`) as the
  unique survivor, but only on a generator-plus-central sample screen — a fragment, not coverage.
- **Not** a new non-elementary-abelian-`Inn` type: this `Q0` has `Inn ≅ (Z2)^6`, the previously known
  elementary-abelian kind (cf. prior constructions), so it changes no boundary.

## 5. Reproduction
- `output/artifacts/seed_Q0.json` (parameters), `group_table.json`, `loop_table.json`,
  `verify.py` (independent checker; rerun: `python3 output/artifacts/verify.py` → `VERIFY_OK`).
- Scratch scripts in `work/` (`build.py`, `delta.py`, `census.py`, `class3.py`, `transversal.py`, `finalize.py`).
