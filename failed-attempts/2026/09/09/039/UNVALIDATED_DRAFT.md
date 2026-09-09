# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified one-level distortion bound for an SL_3 Cayley quotient into L^4,
# with exact diamond rigidity and sharpness

## Abstract

Fix `S = {E_{ij}(±1)}` (12 elementary transvections) and
`G_5 = Cay(SL_3(F_5), S)`, `|G_5| = 372000`, degree 12. We prove

```
c_{L^4}(G_5) ≥ 2^{1/4} ≥ 1.1892,
```

i.e. the admission fallback bound `c ≥ 1 + η` with `η = 2^{1/4} − 1 > 0.1892`,
plus a certified sharpness statement: the diamond (4-point) method used is best
possible, since `c_{L^4}(C_4) = 2^{1/4}` exactly. We also certify
`girth(G_5) = 4`. Every numerical assertion replays via
`artifacts/verify_diamond.py` (stdlib only) printing `VERIFY_OK`.
We do NOT prove any `(log N)^δ` growth rate; see §6 for the honest boundary.

## 1. Objects and conventions

- `E_{ij}(a) = I + a e_{ij}` (i ≠ j), `S = {E_{ij}(±1) : i≠j}`, `I` = identity.
- `G_5 = Cay(SL_3(F_5), S)` with right multiplication, S-labels; undirected
  because S is symmetric. Distortion `c_Y(X)` = inf `L/l` over injective
  `f : X → Y` with `l·d_X ≤ ‖f − f‖_Y ≤ L·d_X`; injective maps of finite spaces
  have `l > 0`.
- `C_4` = unweighted 4-cycle with graph metric (sides 1, diagonals 2).
- `L^4` denotes real `L^4[0,1]` (any fixed atomless model); only its pointwise
  4-point inequality is used, so the same proof works for `ℓ^4` and any
  `L^4(μ)`.

## 2. Exact diamond rigidity in L^4 (elementary proof)

**Lemma 1 (sharp L^4 diamond inequality).** For all real a,b,c,d,

```
(a−b)^4 + (b−c)^4 + (c−d)^4 + (d−a)^4 ≥ ((a−c)^4 + (b−d)^4)/4,   (*)
```

with equality e.g. at a=c or in the rhombus configuration below.

*Proof.* Put `t = (a+c−b−d)/2`, `u = (a−c)/2`, `v = (b−d)/2`. Then
`a−b = t+u−v`, `b−c = u−t+v`, `c−d = u−t−v`, `d−a = t−u−v` up to signs
irrelevant after 4th powers. Let S be the left side and T the bracket on the
right without the 1/4. The verifier checks the exact polynomial identity

```
2(4S − T) = 2(2t)^4 + 12(2t)^2(2u)^2 + 12(2t)^2(2v)^2 + 12(2u)^2(2v)^2
```

coefficient-by-coefficient over the 22 degree-4 monomials in (a,b,c,d), i.e.

```
4S − T = 16(t^4 + 6t^2u^2 + 6t^2v^2 + 6u^2v^2) ≥ 0.
```

∎

**Corollary 2 (exact distortion of C_4).** `c_{L^4}(C_4) = 2^{1/4}.`

*Proof.* Lower bound: let f map the cyclic vertices to A,B,C,D ∈ L^4 with
constants l,L. Pointwise application of Lemma 1 and integration gives,
with `S = ‖A−B‖^4 + ‖B−C‖^4 + ‖C−D‖^4 + ‖D−A‖^4 ≤ 4L^4` (four sides of
length 1) and `T = ‖A−C‖^4 + ‖B−D‖^4 ≥ 2(2l)^4 = 32l^4` (two diagonals of
length 2): `4S − T ≥ 0` yields `16L^4 ≥ 32l^4`, i.e. `(L/l)^4 ≥ 2`.
Upper bound (sharpness): the rhombus `(1,0),(0,1),(−1,0),(0,−1)` in `ℓ^4_2`
has side `2^{1/4}` (side^4 = 1+1 = 2) and diagonal distance 2. Rescaling by
`2^{−1/4}` gives sides 1 and diagonals `2^{3/4}`, i.e. an embedding of C_4
with `L = 1`, `l = 2^{3/4}/2 = 2^{−1/4}` and distortion exactly `2^{1/4}`. ∎

*Remark.* This is the classical Clarkson/Enflo uniform-convexity rigidity for
the diamond; we claim no originality for the inequality — only for the
certified tower-level instance in §4 and the exact replay packaging.

## 3. Graph certificate: girth 4 and an isometric C_4 in G_5

Take `E12 = E_{12}(1)`, `E13 = E_{13}(1)` (both in S).

**Lemma 3.** `E12 E13 = E13 E12` (both equal the matrix with row 1 =
(1,1,1)). Hence `I, E12, E12·E13, E13` is a 4-cycle with steps
`E12, E13, E12^{−1}, E13^{−1} ∈ S`, all verified by exact mod-5 arithmetic.

**Lemma 4 (isometric).** The two diagonal differences are
`E12·E13` and `E12^{−1}·E13`, neither of which lies in `S ∪ {I}`
(checked explicitly). So both diagonals have Cayley distance exactly 2:
the 4-cycle is an isometric copy of C_4.

**Lemma 5 (girth).** No product of three generators is I (all 12³ = 1728
triples checked exactly), and S contains no involution or loop, so G_5 has
no triangles; with Lemma 3, `girth(G_5) = 4`.

**Group data.** `|SL_3(F_5)| = (125−1)(125−5)(125−25)/4 = 124·120·100/4
= 372000`; S has 12 distinct determinant-1 matrices, is symmetric
(`E_{ij}(a)^{−1} = E_{ij}(−a)`), loop-free. So G_5 is 12-regular on 372000
vertices.

## 4. Main bound (fallback claim) and transfer lemma

**Lemma 6 (isometric transfer).** If H embeds isometrically in G then
`c_Y(G) ≥ c_Y(H)` for every target Y (restrict the embedding).

**Theorem 7.** `c_{L^4}(G_5) ≥ 2^{1/4} ≥ 1.1892`; i.e. with `η = 2^{1/4}−1`,
`c_{L^4}(G_5) ≥ 1 + η` with `η > 0.1892` certified by the integer enclosure
`11892^4 = 19999521365872896 < 2·10^16 < 20006249265015601 = 11893^4`.

*Proof.* Lemma 4 + Corollary 2 + Lemma 6. ∎

**Sharpness obstruction (fallback second disjunct).** Corollary 2's rhombus
shows the constant `2^{1/4}` is best possible for the diamond method: no
improvement of Theorem 7 is obtainable from C_4-isometric-subgraph rigidity
alone. Any stronger tower bound must use larger witnesses (e.g. iterated
diamonds / Laakso graphs / spectral methods), not the single C_4.

**Tower remark (transferable).** The matrices E12, E13 commute over Z, and the
diagonal words `E12E13`, `E12^{−1}E13` avoid `S ∪ {I}` as words over Z
(they equal `I + e_{12} + e_{13}`-type matrices ≠ any single transvection),
hence the same 4-tuple is an isometric C_4 in `Cay(SL_3(Z/mZ), S)` for every
`m ≥ 2` (for m = 2 signs coincide but the four vertices remain distinct;
distinctness/diagonal assertions are polynomial identities over Z).
Consequently `c_{L^4}(G_m) ≥ 2^{1/4}` uniformly in m — a flat floor, not growth.

## 5. Replay log

```
$ python3 artifacts/verify_diamond.py
V1_OK: |S|=12, det=1, symmetric, no loops/involutions, degree=12
V2_OK: |SL_3(F_5)| = 372000
V3_OK: commuting 4-cycle vertices distinct; ...
V4_OK: isometric C4; ...
V5_OK: 1728/1728 triples nonzero -> ... girth(G_5)=4 ...
V6_OK: symbolic identity ... over 22 monomials; ... >= 0, sharp
V7_OK: rhombus side^4=2, diag=2 -> distortion upper bound 2^{1/4}
V8_OK: 11892^4=... < 2e16=... < 11893^4=... i.e. 1.1892 < 2^{1/4} < 1.1893
V9_OK: T>=32 l^4, S<=4 L^4, T<=4S => D^4>=2 => D>=2^{1/4}>=1.1892
VERIFY_OK
```

Stdlib only; exact integer/mod-5 arithmetic throughout. No floating point,
no eigenvalue computation, no external gap citations.

## 6. Limitations and honest boundary (read before citing)

1. **No distortion growth proved.** The target `(log N)^δ` rate is untouched:
   Theorem 7 is a uniform constant floor from a single C_4. Proving
   `δ_p > 0` needs nonlinear spectral-gap bootstrapping with certified
   constants, which we do not attempt.
2. **Blocked route documented.** Reducing an L² spectral gap to an L^p (p>2)
   nonlinear Poincaré inequality by naïve Hölder goes the wrong way on finite
   measure (it weakens, not strengthens, the gap); a correct chain needs the
   Mendel–Naor nonlinear spectral calculus or Banach property (T) constants
   plus a certified linear gap of the 372000-vertex graph — out of scope here.
3. **Originality boundary.** Lemma 1/Corollary 2 are classical uniform
   convexity (Clarkson/Enflo); the contribution is the certified exact
   instance: isometric diamond + girth certificate in the canonical Margulis
   level G_5 with a machine-checked inequality log and a sharpness witness.
4. **Generators fixed.** All claims are for the stated 12-element elementary
   transvection set S; other generating sets need their own certificates
   (the commuting-pair argument adapts whenever two generators commute).
