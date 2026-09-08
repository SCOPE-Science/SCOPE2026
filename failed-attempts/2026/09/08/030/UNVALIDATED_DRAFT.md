# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Residual audit of the open binary-linear entry [48,12]: structure theorem, moment system, and validated pipeline

**Lane 123 — partial-theorem report (fallback consolidation).**
**Status: full nonexistence of `[48,12,18]` is NOT proved; the result below is the strongest verified partial theorem.**

## 1. Gap source (re-pinned live, 2026-09-08)

- Grassl BKLC `[48,12]` over GF(2): lower 17 / upper 18 — **open**.
  Lower `[48,12,17]` via Goppa `[55,16,19]` → B2 `[49,13,17]` → shortening;
  upper 18 via one-step Griesmer from `Ub(29,11)=9 (Ja)`.
  URL: `https://www.codetables.de/BKLC/BKLC.php?q=2&n=48&k=12`
- Grassl BKLC `[29,11]`: 9/9 closed, `Ub(29,11)=9 (Ja)`.
  URL: `https://www.codetables.de/BKLC/BKLC.php?q=2&n=29&k=11`
- Grassl BKLC `[30,11]`: 10/10 closed, `Ub` via one-step Griesmer from `Ub(19,10)=5`.
  URL: `https://www.codetables.de/BKLC/BKLC.php?q=2&n=30&k=11`
- No recorded proof of nonexistence of `[48,12,18]` was found (admission arXiv phrase searches empty); Jaffe `Ja` covers `[29,11]=9`, not `[48,12]`.

## 2. Theorem (verified partial / residual-structure result)

Assume a binary linear `[48,12,18]` code `C` exists. Let `z` be its number of zero coordinates. Then:

1. **Cascade (reproduces the table upper bound as a residual argument).**
   A putative `[48,12,19]` has a weight-19 residual of length 29, dimension exactly 11,
   and distance `≥ ceil(19/2) = 10`, contradicting `Ub(29,11)=9`. Hence `Ub(48,12) ≤ 18`.
2. **Residual stratum.** For any weight-18 word `c ∈ C`, the residual `Res(C;c)` is a
   binary linear `[30,11,d']` code with `9 ≤ d' ≤ 10`:
   length `48−18=30`, dimension exactly `12−1=11` (residual lemma),
   `d' ≥ ceil(18/2)=9` and `d' ≤ Ub(30,11)=10` (re-pinned closed entry).
3. **Weight-18 overlap bound.** Any two distinct weight-18 codewords intersect
   (as supports) in `s ≤ 9` positions. The case `s=18` forces equality.
   Proof: for `wt(x)=wt(c)=18` with overlap `s`, `wt(x+c)=36−2s ∈ {0} ∪ [18,∞)`;
   the projection `wt` `18−s ∈ {0} ∪ [9,∞)`. Both force `s ≤ 9` or `s=18`.
   Exhaustively checked over integers `0..18` in `verify_residual.py`.
4. **Degeneracy bound.** Effective length `48−z ≥ G(12,18)=44`, so `z ≤ 4`.
5. **Exact Pless/Krawtchouk moment system.** With `M=4096`, `A_i` the weight distribution,
   `K_1(i)=48−2i`, `K_2(i)=2i²−96i+1128` (machine-verified polynomial identities),
   dual distances `B_j = M⁻¹∑_i A_i K_j(i)` satisfy `B_1=z`, i.e.
   `S_1 := ∑ iA_i = 2048(48−z)`, and `2S_2 − 96S_1 + 1128M = M·B_2` with integer `B_2 ≥ 0`,
   i.e. in the nondegenerate case `z=0`: `S_1=98304`, `S_2=2408448+2048·B_2`.
6. **Order-2 non-elimination (LP-weakness witness, exact rational).**
   The formal distribution `A_0=1, A_18=2018/3, A_24=8237/3, A_30=2030/3`
   (all other `A_i=0`) is nonnegative rational, sums to 4096, has minimum weight 18,
   and satisfies the MacWilliams identities for `j=0,1,2` with `B_1=B_2=0`.
   Hence second-order moments alone **cannot** rule out `[48,12,18]`;
   any completion must use higher Krawtchouk orders or the residual constraints (2)–(3).
7. **Reusable pipeline.** `output/artifacts/verify_residual.py` (stdlib only,
   `Fractions`+`comb`) implements: exact Griesmer numbers, Krawtchouk matrix,
   dual-distribution and moment checks, and the residual constructor
   (puncture support of a min-weight word + project). It is validated end-to-end on
   Hamming `[7,4,3]` → `[4,3,2]` residual with dimension exactly `k−1` and distance
   attaining `ceil(3/2)`.

### What is PROVED vs COMPUTED vs CONJECTURED vs UNCERTAIN

- **Proved (by hand, standard lemmas):** residual lemma statement, cascade (1),
  overlap bound (3) given the cited `Ub` values, degeneracy bound (4) given Griesmer,
  moment identities (5) given MacWilliams/Krawtchouk definitions.
- **Computed evidence (exact rational, replayable):** all Griesmer numbers
  (`G(12,18)=44, G(12,19)=46, G(12,17)=43, G(11,9)=26, G(11,10)=27, G(11,11)=29`);
  `K_1,K_2` polynomial identities; witness sums `S_1=98304, S_2=2408448, B_1=B_2=0`;
  overlap-integer sweep; Hamming `[7,4,3]` pipeline test. See `output/artifacts/results.json`.
- **Conjectured (NOT claimed):** that no `[48,12,18]` exists (`d*(48,12)=17`).
- **Uncertainty / dependence:** (2)–(3) depend on the live-table values
  `Ub(29,11)=9` (Jaffe, unpublished) and `Ub(30,11)=10` taken as provenance, not re-proved;
  a projected-gradient search for a fully Delsarte-feasible (`all 48` inequalities)
  formal `[48,12,18]` enumerator was inconclusive within budget and is **not** claimed;
  no exhaustive integer-enumerator classification is claimed.

## 3. Proof sketches

**Residual lemma (standard; e.g. Hill, Huffman–Pless).**
Let `C=[n,k,d]`, `c` weight `d`. Puncture `supp(c)` and project: codewords vanishing on
`supp(c)` would have weight `< d` unless zero (since `c` has full support on those coords
after suitable coordinate view), so the projection kernel is exactly `{0,c}`;
dimension drops by exactly 1; any nonzero projected word lifts to two preimages whose
weights sum to `≥ d` on complementary parts, forcing projected weight `≥ ceil(d/2)`.

**Griesmer numbers.** `G(k,d)=∑_{i=0}^{k−1}⌈d/2^i⌉`. Direct summation gives the table above;
e.g. `G(12,18)=18+9+5+3+2+1·7=44`. Verified in `verify_residual.py`.

**Overlap.** As in (3) above; `36−2s` and `18−s` arithmetic is exact integer casework.

**Moments.** From `B_j = 2^{−k}∑_i A_i K_j(i)` with verified closed forms for `K_1,K_2`;
`B_1=z` because weight-1 dual words are exactly the zero coordinates.

**Witness check.** `∑A = 1+(2018+8237+2030)/3 = 4096`;
`S_1=(18·2018+24·8237+30·2030)/3=294912/3=98304`;
`S_2=(324·2018+576·8237+900·2030)/3=7225344/3=2408448`;
`B_1=(1/M)∑A_i(48−2i)=0`, `B_2=(1/M)∑A_i K_2(i)=0` by exact `Fraction` arithmetic.

## 4. How to replay

```
python3 output/artifacts/verify_residual.py
```

Stdlib only. Exits nonzero on any failure; writes `output/artifacts/results.json`.
Live-table provenance re-checked 2026-09-08 at the three BKLC URLs above.

## 5. Limitations (explicit)

- Full nonexistence of `[48,12,18]` remains **open**; this report closes nothing.
- No complete MacWilliams-feasible enumerator shortlist is produced (topic fallback
  envisioned one); only the exact moment system + one order-2 feasible witness.
- Higher Krawtchouk constraints (`j≥3`) and integrality (`A_i,B_j ∈ ℤ≥0`) are not resolved.
- Depends on external `Ub(29,11)=9`, `Ub(30,11)=10` as cited bounds, not re-derived.
- Gradient LP search for full Delsarte feasibility was inconclusive; removed from artifacts.

## 6. References

- Brouwer–Verhoeff, updated table of minimum-distance bounds for binary linear codes (1993).
- Jaffe, Binary linear codes: new results on nonexistence (1996, `code.ps.gz`) — via BKLC `Ja` citations.
- Gijswijt–Mittelmann–Schrijver, SDP bounds based on quadruple distances (2012) — benchmark context only.
- Grassl BKLC live entries `[48,12]`, `[29,11]`, `[30,11]` (re-pinned 2026-09-08).
