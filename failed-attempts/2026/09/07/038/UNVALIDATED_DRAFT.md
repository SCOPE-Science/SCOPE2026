# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified optimal-distance witnesses for binary linear [n,k] codes, n=20–24, k=7–12

> Attribution first: the optimal distances below are **not new**. They coincide with the Brouwer/Grassl tables (`codetables.de/BKLC`, live-retrieved 2026-09-07, LB=UB in all 30 cells). This note's contribution is an **independent, machine-checkable certificate bundle**: one explicit full-support systematic generator per cell attaining d*, its exact minimum distance and full weight enumerator proved by exhaustive 2^k enumeration, derivation-containment checks against three verified parents, recomputed Griesmer bounds (self-contained optimality for 15/30 cells), and a stdlib-only replay script (30/30 PASS). No distance record beyond Grassl is claimed.

## 1. Theorem (verification, not discovery)

**Theorem.** For each (n,k) with n in {20,…,24}, k in {7,…,12}, the systematic matrix G(n,k) listed in §7 generates a binary linear [n,k,d*] code with d* equal to the Grassl BKLC optimum, and with the weight enumerator W(n,k) listed in §2. Distances and enumerators were established by exhaustive enumeration of all 2^k codewords (k ≤ 12, at most 4096 words per code; 16384 for the [23,14,5] parent) and independently replayed by `artifacts/verify.py` (separate int-bitmask implementation plus H=[Pᵀ|I] syndrome check): 30/30 PASS. Derivation edges (shortening / puncturing / subcode / parity-extension) from three verified parents were checked by codeword-set containment: ALL OK.

*Proof object.* `artifacts/codes.json` (witnesses + enumerators), `artifacts/verify.py`, `artifacts/replay_log.txt`, `artifacts/containment_log.txt`, `artifacts/bound_log.csv`, `artifacts/pruning_log.txt`, `artifacts/grassl_chains.json`. Run `python3 artifacts/verify.py artifacts` to replay. ∎ (machine proof; human-readable method in §§3–6.)

## 2. Distance and weight-enumerator table

| n | k | d* (Grassl) | achieved d | weight enumerator {w: count} |
|---|---|---|---|---|
| 20 | 7 | 8 | 8 | 0:1, 8:62, 12:64, 16:1 |
| 20 | 8 | 8 | 8 | 0:1, 8:130, 12:120, 16:5 |
| 20 | 9 | 7 | 7 | 0:1, 7:80, 8:130, 11:160, 12:120, 15:16, 16:5 |
| 20 | 10 | 6 | 6 | 0:1, 6:96, 8:233, 10:357, 12:254, 14:74, 16:8, 18:1 |
| 20 | 11 | 5 | 5 | 0:1, 5:39, 6:96, 7:139, 8:233, 9:336, 10:357, 11:326, 12:254, 13:151, 14:74, 15:31, 16:8, 17:2, 18:1 |
| 20 | 12 | 4 | 4 | 0:1, 4:12, 5:78, 6:167, 7:278, 8:482, 9:672, 10:715, 11:652, 12:508, 13:302, 14:141, 15:62, 16:21, 17:4, 18:1 |
| 21 | 7 | 8 | 8 | 0:1, 8:48, 12:76, 16:3 |
| 21 | 8 | 8 | 8 | 0:1, 8:102, 12:144, 16:9 |
| 21 | 9 | 8 | 8 | 0:1, 8:210, 12:280, 16:21 |
| 21 | 10 | 7 | 7 | 0:1, 7:120, 8:210, 11:336, 12:280, 15:56, 16:21 |
| 21 | 11 | 6 | 6 | 0:1, 6:135, 8:372, 10:693, 12:580, 14:225, 16:39, 18:3 |
| 21 | 12 | 5 | 5 | 0:1, 5:51, 6:135, 7:210, 8:372, 9:585, 10:693, 11:684, 12:580, 13:405, 14:225, 15:98, 16:39, 17:15, 18:3 |
| 22 | 7 | 8 | 8 | 0:1, 8:42, 12:72, 16:13 |
| 22 | 8 | 8 | 8 | 0:1, 8:78, 12:160, 16:17 |
| 22 | 9 | 8 | 8 | 0:1, 8:162, 12:312, 16:37 |
| 22 | 10 | 8 | 8 | 0:1, 8:330, 12:616, 16:77 |
| 22 | 11 | 7 | 7 | 0:1, 7:176, 8:330, 11:672, 12:616, 15:176, 16:77 |
| 22 | 12 | 6 | 6 | 0:1, 6:186, 8:582, 10:1278, 12:1264, 14:630, 16:137, 18:18 |
| 23 | 7 | 9 | 9 | 0:1, 9:18, 10:32, 11:26, 12:14, 13:10, 14:14, 15:6, 16:1, 17:4, 18:2 |
| 23 | 8 | 8 | 8 | 0:1, 8:62, 12:160, 16:33 |
| 23 | 9 | 8 | 8 | 0:1, 8:122, 12:328, 16:61 |
| 23 | 10 | 8 | 8 | 0:1, 8:250, 12:648, 16:125 |
| 23 | 11 | 8 | 8 | 0:1, 8:506, 12:1288, 16:253 |
| 23 | 12 | 7 | 7 | 0:1, 7:253, 8:506, 11:1288, 12:1288, 15:506, 16:253, 23:1 |
| 24 | 7 | 10 | 10 | 0:1, 10:50, 12:40, 14:24, 16:7, 18:6 |
| 24 | 8 | 8 | 8 | 0:1, 8:50, 12:152, 16:53 |
| 24 | 9 | 8 | 8 | 0:1, 8:90, 12:328, 16:93 |
| 24 | 10 | 8 | 8 | 0:1, 8:202, 12:616, 16:205 |
| 24 | 11 | 8 | 8 | 0:1, 8:375, 12:1296, 16:375, 24:1 |
| 24 | 12 | 8 | 8 | 0:1, 8:759, 12:2576, 16:759, 24:1 |

All enumerators sum to 2^k; minimum nonzero support weight equals d* in every row (checked by the verifier).

## 3. Upper bounds: what is proved here vs cited

**Griesmer bound (recomputed, self-contained).** For binary [n,k,d], n ≥ G(k,d) := Σ_{i=0}^{k-1} ⌈d/2^i⌉. Hence d ≤ max{d : G(k,d) ≤ n}. We recomputed G(k,d) exactly for every cell (see `bound_log.csv`, `pruning_log.txt`):

| n | k | d* | G(k,d*) | G(k,d*+1) | Griesmer UB | tight? |
|---|---|---|---|---|---|---|
| 20 | 7 | 8 | 18 | 22 | 8 | yes |
| 20 | 8 | 8 | 19 | 23 | 8 | yes |
| 20 | 9 | 7 | 19 | 20 | 8 | no |
| 20 | 10 | 6 | 18 | 20 | 7 | no |
| 20 | 11 | 5 | 18 | 19 | 6 | no |
| 20 | 12 | 4 | 16 | 19 | 6 | no |
| 21 | 7 | 8 | 18 | 22 | 8 | yes |
| 21 | 8 | 8 | 19 | 23 | 8 | yes |
| 21 | 9 | 8 | 20 | 24 | 8 | yes |
| 21 | 10 | 7 | 20 | 21 | 8 | no |
| 21 | 11 | 6 | 19 | 21 | 7 | no |
| 21 | 12 | 5 | 19 | 20 | 6 | no |
| 22 | 7 | 8 | 18 | 22 | 9 | no |
| 22 | 8 | 8 | 19 | 23 | 8 | yes |
| 22 | 9 | 8 | 20 | 24 | 8 | yes |
| 22 | 10 | 8 | 21 | 25 | 8 | yes |
| 22 | 11 | 7 | 21 | 22 | 8 | no |
| 22 | 12 | 6 | 20 | 22 | 7 | no |
| 23 | 7 | 9 | 22 | 23 | 10 | no |
| 23 | 8 | 8 | 19 | 23 | 9 | no |
| 23 | 9 | 8 | 20 | 24 | 8 | yes |
| 23 | 10 | 8 | 21 | 25 | 8 | yes |
| 23 | 11 | 8 | 22 | 26 | 8 | yes |
| 23 | 12 | 7 | 22 | 23 | 8 | no |
| 24 | 7 | 10 | 23 | 25 | 10 | yes |
| 24 | 8 | 8 | 19 | 23 | 10 | no |
| 24 | 9 | 8 | 20 | 24 | 9 | no |
| 24 | 10 | 8 | 21 | 25 | 8 | yes |
| 24 | 11 | 8 | 22 | 26 | 8 | yes |
| 24 | 12 | 8 | 23 | 27 | 8 | yes |

15/30 cells are Griesmer-tight, so their optimality is proved from scratch (Griesmer theorem + our exhibited code). The remaining 15 cells have d* strictly below the Griesmer UB; their upper bounds are deeper Brouwer results (one-step Griesmer / shortening / parity arguments). We do **not** re-derive those 15 UB proofs; we cite them verbatim from the live Grassl pages (full texts in `artifacts/grassl_chains.json`, Brouwer table 2007-02-13). Optimality for those cells is therefore conditional on Brouwer's UBs; our verified contribution there is the matching lower bound (explicit code with d=d*). Plotkin's bound was also recomputed per cell and is never binding in this band (all d* ≤ n/2), consistent with the audit trail.

## 4. Constructions (three verified parents + elementary ops)

- **P1 — extended Golay [24,12,8].** Systematic [I₁₂|A] with the 12×12 A in §7 (QR/circulant literature form). Verified d=8 with the Golay enumerator {0:1, 8:759, 12:2576, 16:759, 24:1}.
- **P2 — Wagner [23,14,5]** (Grassl `Wa` stored matrix, IEEE Trans. Inf. Theory 1965). Transcribed and verified d=5. Parity extension gives [24,14,6] (verified d=6).
- **P3 — Hashim–Pozdniakov [23,7,9]** (Grassl `HP` stored matrix, Electron. Lett. 1976). Transcribed and verified d=9. Parity extension gives [24,7,10] (verified d=10, Griesmer-tight).
- **Ops.** puncture (delete coordinate, d drops ≤1); shorten at S (subcode vanishing on S, delete S: [n,k,d]→[n−|S|,k−rank,≥d]); subcode (any subspace: d nondecreasing); parity extension (append overall parity). Monotonicity gives d(lower-bound) for each child; equality d=d* follows from the UB (Griesmer or Brouwer). Every edge was audited by codeword-set containment (shortenings are exact equalities): ALL OK.

Derivation per cell (0-based positions; 1-based in Grassl prose):

| cell | route |
|---|---|---|
| [20,7] | subcode of [20,8] (resample) |
| [20,8] | shorten P1 at {21,22,23,24} |
| [20,9] | shorten [23,12,7] at {21,22,23} |
| [20,10] | shorten [24,14,6] at {21,22,23,24} |
| [20,11] | shorten P2 at {21,22,23} |
| [20,12] | puncture [21,12,5] at {21} |
| [21,7] | subcode of [21,9] (resample) |
| [21,8] | subcode of [21,9] (resample) |
| [21,9] | shorten P1 at {22,23,24} |
| [21,10] | shorten [23,12,7] at {22,23} |
| [21,11] | shorten [24,14,6] at {22,23,24} |
| [21,12] | shorten P2 at {22,23} |
| [22,7] | subcode of [22,10] (resample) |
| [22,8] | subcode of [22,10] (resample) |
| [22,9] | subcode of [22,10] (resample) |
| [22,10] | shorten P1 at {23,24} |
| [22,11] | shorten [23,12,7] at {23} |
| [22,12] | shorten [24,14,6](P2+parity) at {23,24} |
| [23,7] | P3 base |
| [23,8] | subcode of [23,11] (resample) |
| [23,9] | subcode of [23,11] (resample) |
| [23,10] | subcode of [23,11] (resample) |
| [23,11] | shorten P1 at {24} |
| [23,12] | puncture P1 at {24} |
| [24,7] | parity extension of P3 |
| [24,8] | subcode of [24,12] (resample) |
| [24,9] | subcode of [24,12] (resample) |
| [24,10] | subcode of [24,12] (resample) |
| [24,11] | subcode of [24,12] (full-support resample) |
| [24,12] | P1 base |

All witnesses were converted to systematic [I_k|P] form by column permutation (a monomial equivalence, distance-preserving) and resampled subcodes use seed 20260907; no witness has an all-zero coordinate.

## 5. Replay instructions

```
python3 artifacts/verify.py artifacts   # expect 30/30 PASS, exit 0
```
The verifier re-enumerates all 2^k codewords per cell with an independent implementation, checks ΣW=2^k, min-weight=d, systematic form, H·Gᵀ=0 with rank(H)=n−k, Griesmer admissibility, and equality with the stored Grassl LB/UB. See `replay_log.txt` for the reference output.

## 6. Limitations and honest scope

1. No new optimal distances: every d* equals the published Grassl/Brouwer value (checked live 2026-09-07). 2. No exhaustive search over monomial-equivalence classes was performed — it is infeasible (thousands of column types for k=12); the audit-plan search was replaced by targeted derivation, disclosed here. 3. For the 15 non-Griesmer cells, optimality relies on Brouwer's UB proofs, cited not reproduced. 4. Parent matrices P2/P3 are transcriptions of Grassl stored matrices (their distances re-verified here, but provenance is Grassl/MAGMA). 5. Weight enumerators are for our specific representatives, not canonical invariants of the (n,k) cell (non-equivalent optima may differ).

## 7. Witnesses and parents

### Parent A (Golay [24,12,8], [I|A] right half, rows given as 12-bit strings)
- `011111111111`
- `111011100010`
- `110111000101`
- `101110001011`
- `111100010110`
- `111000101101`
- `110001011011`
- `100010110111`
- `100101101110`
- `101011011100`
- `110110111000`
- `101101110001`

### Parent P2 (Wagner [23,14,5], Grassl stored matrix, 14x23) and P3 (HP [23,7,9], 7x23)
Transcribed from the Grassl BKLC pages for [23,14] and [23,7] (URLs in `grassl_chains.json`); distances re-verified (d=5, d=9).
- P2 `10000000000010000101101`
- P2 `01000000000010001010101`
- P2 `00100000000010010010111`
- P2 `00010000000010001100001`
- P2 `00001000000010001111110`
- P2 `00000100000010011111101`
- P2 `00000010000000001011010`
- P2 `00000001000000011110011`
- P2 `00000000100010010001011`
- P2 `00000000010000010001110`
- P2 `00000000001010011000110`
- P2 `00000000000110011101000`
- P2 `00000000000001000110111`
- P2 `00000000000000101000111`
- P3 `10000000100110101001111`
- P3 `01000001101011010110001`
- P3 `00100001100100001110011`
- P3 `00010001011001010011100`
- P3 `00001001110001100111111`
- P3 `00000100110100110110100`
- P3 `00000011011000101101001`

### All 30 systematic witnesses G(n,k)=[I_k|P] (rows as bitstrings, length n)

#### [20,7] d*=8
-`10000001001000101111`
-`01000000110011010101`
-`00100000011100011101`
-`00010001010010011110`
-`00001001000111001101`
-`00000101111010001001`
-`00000011010011100011`

#### [20,8] d*=8
-`10000000100101011110`
-`01000000110011010101`
-`00100000011100011101`
-`00010000111111101111`
-`00001000101010111100`
-`00000100010111111000`
-`00000010111110010010`
-`00000001101101110001`

#### [20,9] d*=7
-`10000000010011101001`
-`01000000011011010101`
-`00100000001110101010`
-`00010000011101011000`
-`00001000010110111100`
-`00000100001001001111`
-`00000010011100100101`
-`00000001010111000110`
-`00000000100010110111`

#### [20,10] d*=6
-`10000000001110001100`
-`01000000001110000011`
-`00100000000010111010`
-`00010000000100111100`
-`00001000000100010111`
-`00000100001111111000`
-`00000010001100101010`
-`00000001001011100001`
-`00000000100111100111`
-`00000000010010011101`

#### [20,11] d*=5
-`10000000000111001100`
-`01000000000111000011`
-`00100000000001111010`
-`00010000000010111100`
-`00001000000010010111`
-`00000100000111010110`
-`00000010000110101010`
-`00000001000101001111`
-`00000000100011001001`
-`00000000010001011101`
-`00000000001000101110`

#### [20,12] d*=4
-`10000000000010110101`
-`01000000000010111010`
-`00100000000001111010`
-`00010000000010111100`
-`00001000000010010111`
-`00000100000010101111`
-`00000010000011010011`
-`00000001000000110110`
-`00000000100001111001`
-`00000000010011001001`
-`00000000001001011101`
-`00000000000100101110`

#### [21,7] d*=8
-`100000010000111101001`
-`010000010101011111111`
-`001000011100011011000`
-`000100001111111011110`
-`000010010001110011010`
-`000001011100010100101`
-`000000101111100100100`

#### [21,8] d*=8
-`100000000101010111100`
-`010000000110110101010`
-`001000001100100011110`
-`000100001000011111010`
-`000010000100011001111`
-`000001000011111110000`
-`000000100101101010101`
-`000000010000110110111`

#### [21,9] d*=8
-`100000000101010111100`
-`010000000110110101010`
-`001000000011110001101`
-`000100000111001101001`
-`000010000100011001111`
-`000001000011111110000`
-`000000100111010010011`
-`000000010101101010101`
-`000000001000110110111`

#### [21,10] d*=7
-`100000000010111010010`
-`010000000011110101010`
-`001000000001011100011`
-`000100000011100000111`
-`000010000010011001111`
-`000001000001010011110`
-`000000100011111111101`
-`000000010010000111011`
-`000000001000110110111`
-`000000000100101101110`

#### [21,11] d*=6
-`100000000001010110111`
-`010000000001010101001`
-`001000000000101110100`
-`000100000001001111000`
-`000010000001000101110`
-`000001000001001011111`
-`000000100001111111011`
-`000000010000001101101`
-`000000001000110101111`
-`000000000101111001110`
-`000000000010100111010`

#### [21,12] d*=5
-`100000000000101101011`
-`010000000000101110101`
-`001000000000011110100`
-`000100000000101111000`
-`000010000000100101110`
-`000001000000101011111`
-`000000100000110100111`
-`000000010000001101101`
-`000000001000011110011`
-`000000000100110010010`
-`000000000010010111010`
-`000000000001001011100`

#### [22,7] d*=8
-`1000000101000101100101`
-`0100000101010111111110`
-`0010000001110001110100`
-`0001000011111110111100`
-`0000100100011100110100`
-`0000010111101000100100`
-`0000001011010100100110`

#### [22,8] d*=8
-`1000000010001111010010`
-`0100000010011101001001`
-`0010000011001100000111`
-`0001000001110100001011`
-`0000100001101011110000`
-`0000010011100010010011`
-`0000001010000100111011`
-`0000000100001010110111`

#### [22,9] d*=8
-`1000000001111000010110`
-`0100000001000111100011`
-`0010000000010110101101`
-`0001000001011001100101`
-`0000100001000110011110`
-`0000010000111000111001`
-`0000001001011110010001`
-`0000000101011010101010`
-`0000000010001010110111`

#### [22,10] d*=8
-`1000000000110101111000`
-`0100000000100111100011`
-`0010000000010110101101`
-`0001000000111001100101`
-`0000100000100110011110`
-`0000010000010101010111`
-`0000001000111110010001`
-`0000000100111010101010`
-`0000000010001010110111`
-`0000000001001101101110`

#### [22,11] d*=7
-`1000000000011110100100`
-`0100000000010111100011`
-`0010000000001101110001`
-`0001000000010010111001`
-`0000100000010110011110`
-`0000010000001110001011`
-`0000001000010101001101`
-`0000000100010001110110`
-`0000000010001010110111`
-`0000000001001101101110`
-`0000000000101011011100`

#### [22,12] d*=6
-`1000000000001100001101`
-`0100000000001100110001`
-`0010000000001011101000`
-`0001000000001010010011`
-`0000100000001000111111`
-`0000010000001011011101`
-`0000001000000110010101`
-`0000000100000011011010`
-`0000000010001101011110`
-`0000000001000111111111`
-`0000000000101001100011`
-`0000000000011001110100`

#### [23,7] d*=9
-`10000000100110101001111`
-`01000001101011010110001`
-`00100001100100001110011`
-`00010001011001010011100`
-`00001001110001100111111`
-`00000100110100110110100`
-`00000011011000101101001`

#### [23,8] d*=8
-`10000000100010111010010`
-`01000000111111101010110`
-`00100000111001101111101`
-`00010000111000001011010`
-`00001000000011110001011`
-`00000100100000100111011`
-`00000010000100111100011`
-`00000001000010010110111`

#### [23,9] d*=8
-`10000000010101100101001`
-`01000000000011101110001`
-`00100000001110110000110`
-`00010000000100001111101`
-`00001000010001011100101`
-`00000100011100100011100`
-`00000010010111011111011`
-`00000001011101001010001`
-`00000000101001001101011`

#### [23,10] d*=8
-`10000000001100010011011`
-`01000000001000110101101`
-`00100000001110110000110`
-`00010000001111010100001`
-`00001000001000101010111`
-`00000100000101010101110`
-`00000010000101110010101`
-`00000001000100111100011`
-`00000000101001001101011`
-`00000000010010101101110`

#### [23,11] d*=8
-`10000000000111001000111`
-`01000000000011101110001`
-`00100000000101101011010`
-`00010000000100001111101`
-`00001000000011110001011`
-`00000100000101010101110`
-`00000010000101110010101`
-`00000001000100111100011`
-`00000000100010010110111`
-`00000000010010101101110`
-`00000000001011011011100`

#### [23,12] d*=7
-`10000000000001111111111`
-`01000000000011101110001`
-`00100000000011011100010`
-`00010000000010111000101`
-`00001000000011110001011`
-`00000100000011100010110`
-`00000010000011000101101`
-`00000001000010001011011`
-`00000000100010010110111`
-`00000000010010101101110`
-`00000000001011011011100`
-`00000000000110110111000`

#### [24,7] d*=10
-`100000001001101010011110`
-`010000011010110101100010`
-`001000011001000011100111`
-`000100010110010100111001`
-`000010011100011001111110`
-`000001001101001101101001`
-`000000110110001011010011`

#### [24,8] d*=8
-`100000001100010001001101`
-`010000000000111011100010`
-`001000001001111111011010`
-`000100000000101110001011`
-`000010001101011111010101`
-`000001001000011101000011`
-`000000101101010010011000`
-`000000011010110001100001`

#### [24,9] d*=8
-`100000000000011111111111`
-`010000000011100000101011`
-`001000000011101100001100`
-`000100000011110101000010`
-`000010000000111100010110`
-`000001000101111110000000`
-`000000100111000001001110`
-`000000010011111001111110`
-`000000001100001110110010`

#### [24,10] d*=8
-`100000000001101001000111`
-`010000000000111011100010`
-`001000000001000001111101`
-`000100000011110011101111`
-`000010000010010111001010`
-`000001000011100101001001`
-`000000100011101100111111`
-`000000010010001001101011`
-`000000001001010011010110`
-`000000000100101101110001`

#### [24,11] d*=8
-`100000000000011111111111`
-`010000000000111011100010`
-`001000000000110111000101`
-`000100000000101110001011`
-`000010000001011001111000`
-`000001000001011101000011`
-`000000100000110001011011`
-`000000010001000111011001`
-`000000001000101011011100`
-`000000000100110110111000`
-`000000000010101101110001`

#### [24,12] d*=8
-`100000000000011111111111`
-`010000000000111011100010`
-`001000000000110111000101`
-`000100000000101110001011`
-`000010000000111100010110`
-`000001000000111000101101`
-`000000100000110001011011`
-`000000010000100010110111`
-`000000001000100101101110`
-`000000000100101011011100`
-`000000000010110110111000`
-`000000000001101101110001`

## References

- M. Grassl, Bounds on the minimum distance of linear codes, `codetables.de/BKLC` (Brouwer table 2007-02-13; per-cell pages + LB/UB retrieved 2026-09-07, archived in `grassl_chains.json`).
- A. E. Brouwer, bounds tables for binary codes (upper bounds cited via Grassl).
- T. J. Wagner, remark on binary group codes, IEEE Trans. Inf. Theory 11 (1965) 458 (parent [23,14,5]).
- A. A. Hashim & V. S. Pozdniakov, computerized search for linear binary codes, Electron. Lett. 12 (1976) 350–351 (parent [23,7,9]).
- F. J. MacWilliams & N. J. A. Sloane, Theory of Error-Correcting Codes (Griesmer bound, shortening/puncturing monotonicity).
