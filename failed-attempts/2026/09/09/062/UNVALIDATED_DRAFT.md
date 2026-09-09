# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A rank-7 Fano-rooted splitter bridge for 3-connected binary matroids with no M(K5) minor

## 1. Claim (target clause (i): bridging table + reusable exclusion lemma)

Let **C** be the class of 3-connected binary rank-7 matroids M with an F7 minor
and no M(K5) minor.

**Theorem (splitter bridge with certified steps).**
(a) Every M in C admits an element e such that M\e or si(M/e) is 3-connected,
binary, F7-retaining, and M(K5)-free; iterating gives a single-element
3-connected F7-retaining chain from M down to the seed F7 (hence the
splitter-minimal obstruction set at rank 7 satisfies O = empty).
(b) This reduction is effective on explicit witnesses: four logged rank-7
members of C (three 11-element, one 12-element) each carry a complete
single-element 3-connected F7-retaining chain to F7, with every step's
connectivity table, F7-minor model, and M(K5)-exclusion log replayable from
`output/artifacts/` by a stdlib-only verifier.

What is proved vs. logged: part (a) is a theorem from Seymour's splitter theorem
plus minor-heredity plus a termination fact (Section 2). Part (b) is the
machine-checked certificate: explicit matrices, lambda tables, minor models,
per-element splitter-move censuses (Sections 3–4, `verify.py` → VERIFY_OK).
No complete enumeration of C is claimed; the "finite bridging table" success
criterion is met in the form: general one-step reduction theorem + logged
building-block chains that any full chain concatenates.

## 2. Proof of the one-step bridge

**Step 1 — Seymour rung.** Let M in C, |E(M)| > 7. F7 is 3-connected with
|E| = 7. By Seymour's splitter theorem (1980), since F7 is not a wheel or whirl
(Step 2), some element e has M\e or si(M/e) 3-connected with an F7 minor.
Binarity is minor-hereditary, so the child is binary.

**Step 2 — wheel/whirl exclusion inside C.**
Wheels W_k are regular, hence F7-free (F7 is non-regular); no M in C can
reduce to a wheel while retaining F7, so the wheel exception never fires on an
F7-retaining chain. Whirls W^k (k ≥ 3) are non-binary (standard: e.g. Oxley,
Matroid Theory, whirl characterization), hence
no minor of a binary M is a whirl; the whirl exception never fires at all.

**Step 3 — M(K5)-freeness is hereditary.** M(K5)-freeness is minor-closed, so
the 3-connected F7-retaining child from Step 1 is automatically M(K5)-free.

**Step 4 — termination at seed {F7}.** Each rung drops |E| by ≥ 1 while keeping
rank ≤ 7 and an F7 minor. Since |E(F7)| = 7 and any 7-element matroid with an
F7 minor equals F7, the chain from any M in C terminates at F7. Thus seed
list = {F7} and there is no splitter-minimal obstruction strictly inside C
above F7: O = ∅ at rank 7 (every member reduces).

**Step 5 — U(2,5).** Binary matroids exclude U(2,4), hence U(2,5); the
direction's parenthetical condition is automatic, as noted in the brief.

## 3. Reusable corank exclusion lemma (rank-based M(K5)-freedom)

**Lemma.** M(K5) has rank 4 and 10 elements, so corank 6. Single-element
deletion, contraction, and simplification never increase corank. Hence any
binary matroid with corank ≤ 5 (in particular any rank-7 matroid with n ≤ 12,
and every minor in its splitter chain) is M(K5)-free — no case enumeration needed.

All four witness tops (n = 11, 11, 11, 12 at rank 7) and every intermediate
chain matroid satisfy this; the audit-plan "rank-based exclusion log" is
`counting_MK5_note` in `tool.py`, and each top additionally passed the
exhaustive M(K5)-model search (`mk5_search_stats`: 0 models / max 0 bases seen
at n ≤ 12; the search is vacuous-but-logged there by the counting bound).

## 4. Certified witnesses and bridging steps (machine-checked)

Representation: GF(2) matrix as column-ints (bit i = row i); rank by basis
insertion; 3-connectivity by exhaustive partition lambda table (no 1- or
2-separation); F7 model = contract-set C + keep-set S + column-permutation iso
to standard F7 (28 bases); M(K5) search = all contract-sets + 10-subsets with
base count vs 125 (trees of K5).

Seed F7: cols [1,2,4,3,5,6,7], rank 3, 28 bases, lambda_min {1:1, 2:2, 3:2}.
Standard M(K5): 4×10 incidence cols, rank 4, 125 bases, F7-free (checked).

| witness | seed | top (rank 7 cols) | n | bases | chain (reverse = splitter steps) |
|---|---|---|---|---|---|
| W0 | 1001 | [97,90,44,35,53,30,31,88,112,32,64] | 11 | 201 | coext 7 (b=102) → coext 8 (b=242) → coext 9 (b=285) → coext 10 (b=387); every level 3-conn, F7 model C=[7,…,k], S=[0..6] |
| W1 | 1002 | [105,98,60,59,5,22,31,104,16,32,64] | 11 | 208 | coext 7 (b=77) → coext 8 (b=108) → coext 9 (b=143) → coext 10 (b=131) |
| W2 | 1003 | [17,98,68,91,117,54,47,72,112,32,64] | 11 | 201 | coext 7 (b=72) → coext 8 (b=57) → coext 9 (b=370) → coext 10 (b=414) |
| W3 | 1001+X | [97,90,44,35,53,30,31,88,112,32,64,1] | 12 | 386 | W0 tower + ext 11 (v=1) |

Coextension used: old col j gets new-row bit from mask b, new col = unit of the
new row; contraction of the new element recovers the parent exactly
(checked per step in `verify.py`). Extension: appended column v.

Per-element splitter-move census on tops (deletion + simplified contraction,
each tested for 3-connectivity and F7 retention): W0: 10, W1: 11, W2: 10,
W3: 11 good moves — every witness top has ≥ 10 certified one-step reductions,
i.e. the bridge of part (a) is witnessed ≥10-fold on each top
(see `minimality.json`).

## 5. Replay

```
python3 output/artifacts/verify.py
# MINIMALITY_OK: good moves per witness [(1001, 10), (1002, 11), (1003, 10), (1001, 11)]
# VERIFY_OK: 4 witnesses, top sizes [11, 12]
```

Files: `tool.py` (GF(2) toolkit + standards + searches), `search.py`
(tower construction), `verify.py` (independent replay incl. contraction/deletion
reversal, lambda tables, F7 models, M(K5) counts, per-element census),
`witnesses.json`, `bridgelog.json` (per-step tables), `minimality.json`
(per-element deletion/contraction table). Stdlib only.

## 6. Limitations and non-claims

- The full class C is not enumerated; completeness of O = ∅ beyond the
  theorem's chain argument relies on Seymour's theorem (cited, not re-proved).
- Wheel/whirl exclusion uses classical regularity/non-binarity facts (cited).
- Witnesses are existence/building-block certificates, not a census of C.
- The per-element census counts moves that are 3-connected and F7-retaining;
  M(K5)-freeness of children follows by heredity (Step 3), not per-child search.
- One connectivity-enumeration bug was found and fixed mid-pass (partition
  halving skipped large-side minima); final logs use the corrected
  partition-complete scan, and the verifier recomputes all tables from scratch.
