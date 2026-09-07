# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Extremal subgroup-lattice size and non-abelian class-number maximum among the 231 groups of order 96

## Claim (exact, computationally certified)

Let `G_i = SmallGroup(96,i)`, `i=1..231` (Besche–Eick–O'Brien library),
`s(G)` = total number of subgroups, `k(G)` = number of conjugacy classes.
Computed exhaustively in GAP 4.12.1 / SmallGrp 1.5.3:

**(a) Global subgroup maximum.** `S_max = max_i s(G_i) = 1362`, attained
uniquely by `i_s = 230`, `G_230 ≅ C2 × C2 × C2 × C2 × S3`
(order `16·6=96`), with `k(G_230)=48`, non-abelian, and subgroup-by-order
profile

```
1:1|2:63|3:1|4:395|6:31|8:435|12:155|16:91|24:155|32:3|48:31|96:1
```

(sum = 1362). The runner-up is the abelian `G_231 ≅ C6×C2^4` with 748
subgroups, then `G_207 ≅ C2×C2×D24` with 578. Full ranking is in
`artifacts/census96.csv`.

**(b) Non-abelian class-number maximum.** The unrestricted maximum of `k`
is the trivial abelian value 96 (attained by exactly the 7 abelian groups
`i ∈ {2,46,59,161,176,220,231}`, as `p(5)·p(1)=7` predicts). Restricted to
non-abelian groups,

```
K_max = max_{i non-abelian} k(G_i) = 60,
```

attained by exactly 15 IDs:

```
45, 47, 48, 55, 60, 162, 163, 164, 165, 166, 177, 178, 221, 222, 223
```

with structure descriptions and `s`-profiles tabulated below. No
non-abelian group of order 96 has `k > 60`; the non-abelian `k`-range is
10–60 and the `s`-range over all groups is 12–1362.

Top-5 by `s(G)`:

| i | StructureDescription | s | k | abelian | profile |
|---|---|---|---|---|---|
| 230 | C2 x C2 x C2 x C2 x S3 | 1362 | 48 | false | 1:1\|2:63\|3:1\|4:395\|6:31\|8:435\|12:155\|16:91\|24:155\|32:3\|48:31\|96:1 |
| 231 | C6 x C2 x C2 x C2 x C2 | 748 | 96 | true | 1:1\|2:31\|3:1\|4:155\|6:31\|8:155\|12:155\|16:31\|24:155\|32:1\|48:31\|96:1 |
| 207 | C2 x C2 x D24 | 578 | 36 | false | 1:1\|2:55\|3:1\|4:179\|6:23\|8:139\|12:67\|16:43\|24:51\|32:3\|48:15\|96:1 |
| 209 | C2 x D8 x S3 | 562 | 30 | false | 1:1\|2:47\|3:1\|4:171\|6:23\|8:139\|12:67\|16:43\|24:51\|32:3\|48:15\|96:1 |
| 219 | C2 x C2 x ((C6 x C2) : C2) | 498 | 36 | false | 1:1\|2:39\|3:1\|4:131\|6:23\|8:123\|12:67\|16:43\|24:51\|32:3\|48:15\|96:1 |

All 15 `k=60` non-abelian attainers (`s`, profile from the CSV):

| i | StructureDescription | s | profile |
|---|---|---|---|
| 45 | C3 x ((C4 x C2) : C4) | 100 | 1:1\|2:7\|3:1\|4:19\|6:7\|8:19\|12:19\|16:3\|24:19\|32:1\|48:3\|96:1 |
| 47 | C3 x (C8 : C4) | 44 | 1:1\|2:3\|3:1\|4:7\|6:3\|8:7\|12:7\|16:3\|24:7\|32:1\|48:3\|96:1 |
| 48 | C3 x ((C8 x C2) : C2) | 68 | 1:1\|2:7\|3:1\|4:11\|6:7\|8:11\|12:11\|16:3\|24:11\|32:1\|48:3\|96:1 |
| 55 | C3 x (C4 : C8) | 44 | 1:1\|2:3\|3:1\|4:7\|6:3\|8:7\|12:7\|16:3\|24:7\|32:1\|48:3\|96:1 |
| 60 | C3 x (C16 : C2) | 28 | 1:1\|2:3\|3:1\|4:3\|6:3\|8:3\|12:3\|16:3\|24:3\|32:1\|48:3\|96:1 |
| 162 | C6 x ((C4 x C2) : C2) | 188 | 1:1\|2:15\|3:1\|4:43\|6:15\|8:27\|12:43\|16:7\|24:27\|32:1\|48:7\|96:1 |
| 163 | C6 x (C4 : C4) | 108 | 1:1\|2:7\|3:1\|4:19\|6:7\|8:19\|12:19\|16:7\|24:19\|32:1\|48:7\|96:1 |
| 164 | C3 x ((C4 x C4) : C2) | 92 | 1:1\|2:7\|3:1\|4:19\|6:7\|8:11\|12:19\|16:7\|24:11\|32:1\|48:7\|96:1 |
| 165 | C12 x D8 | 124 | 1:1\|2:11\|3:1\|4:23\|6:11\|8:19\|12:23\|16:7\|24:19\|32:1\|48:7\|96:1 |
| 166 | C12 x Q8 | 76 | 1:1\|2:3\|3:1\|4:15\|6:3\|8:11\|12:15\|16:7\|24:11\|32:1\|48:7\|96:1 |
| 177 | C6 x (C8 : C2) | 76 | 1:1\|2:7\|3:1\|4:11\|6:7\|8:11\|12:11\|16:7\|24:11\|32:1\|48:7\|96:1 |
| 178 | C3 x ((C8 x C2) : C2) | 68 | 1:1\|2:7\|3:1\|4:7\|6:7\|8:11\|12:7\|16:7\|24:11\|32:1\|48:7\|96:1 |
| 221 | C2 x C6 x D8 | 316 | 1:1\|2:23\|3:1\|4:67\|6:23\|8:51\|12:67\|16:15\|24:51\|32:1\|48:15\|96:1 |
| 222 | C2 x C6 x Q8 | 156 | 1:1\|2:7\|3:1\|4:19\|6:7\|8:35\|12:19\|16:15\|24:35\|32:1\|48:15\|96:1 |
| 223 | C6 x ((C4 x C2) : C2) | 188 | 1:1\|2:15\|3:1\|4:27\|6:15\|8:35\|12:27\|16:15\|24:35\|32:1\|48:15\|96:1 |

(Commas in GAP `StructureDescription` output replaced by `;` in raw CSV;
rendered here with `x`/spaces as GAP prints. Full machine-readable rows,
including `k` and abelian flag, are in `artifacts/census96.csv`.)

## Method (auditable, rerunnable in minutes)

For each `i=1..231`, `G:=SmallGroup(96,i)`:
`s(G)=Sum(ConjugacyClassesSubgroups(LatticeSubgroups(G)),Size)`,
`k(G)=Length(ConjugacyClasses(G))`, plus `IsAbelian`, `StructureDescription`
(with `IdGroup` fallback, never triggered), and the per-order profile from
conjugacy-class representatives. Sorting the 231 rows gives the two maxima
above. No lattice stalled (order 96 is small; full run ≈ seconds–minutes).

Fp-presentation certificates for the union of the `s` top-5 and all `k=60`
IDs were produced by `IsomorphismFpGroup` / `SimplifiedFpGroup` with
`Order` checks (see `artifacts/fp_certs.log`); e.g. `G_230` has a
6-generator 21-relator pc-presentation simplifying within the logged data
(all relators explicitly listed in the log).

Independent cross-checks (`artifacts/crosscheck.log`):
`s` for the top-10 by `s` recomputed via `AllSubgroups` (exact agreement
on all 10, including 1362 vs 1362 at `i=230`);
`k` for the top-10 plus all 15 `k=60` IDs recomputed via
`NrConjugacyClasses(CharacterTable(G))` and `Length(Irr(G))`
(exact agreement, all `k=60` confirmed);
plus a fresh from-scratch global rescan reproducing
`Smax=1362 Sids=[230]` and `Kmax(nonab)=60` with the same 15 IDs.

## Rerun

Stock GAP suffices (no custom code):

```
sudo apt install gap gap-smallgrp gap-character-tables gap-transgrp gap-primgrp gap-gapdoc
gap -q output/artifacts/census96_clean.g   # → output/artifacts/census96.csv + log
gap -q output/artifacts/crosscheck.g       # → independent verification
gap -q output/artifacts/fp_certs.g         # → presentations
```

Expected: `census96.csv` has header + 231 rows, `S_max=1362` at row 230,
`K_max(nonab)=60` at exactly the 15 IDs above. Scripts set
`SizeScreen([10000,24])` so the CSV has no wrapped lines.

Recorded versions: GAP 4.12.1, SmallGrp 1.5.3, TransGrp 3.6.5,
PrimGrp 3.4.4; `NumberSmallGroups(96)=231`; run 2026-09-07 (see
`census96_clean.log`, `rerun_timestamp.txt`).

## Proof vs computation vs conjecture (honest separation)

- **Proved (machine-checked exhaustive enumeration):** the two extremal
values, attainer lists, profiles, and per-group `(s,k)` table, conditional
on correctness of the GAP SmallGroups library (completeness of the 231
groups of order 96) and of GAP's `LatticeSubgroups`,
`ConjugacyClassesSubgroups`, `ConjugacyClasses`, `AllSubgroups`,
`CharacterTable`/`Irr` implementations. Cross-validation between two
independent subgroup-count routes and two independent class-number routes
removes single-function risk but not whole-system risk.
- **Computed evidence:** the CSV, full logs, and Fp relators.
- **Conjecture / not claimed:** any human-readable theoretical explanation
of why `C2^4×S3` maximizes subgroups or why 60 is the non-abelian class
ceiling; minimality of the Fp presentations.
- **Uncertainty:** general-web triage (GroupNames etc.) was attempted but
network-blocked at solve time; the originality claim rests on the
assignment's prior scan plus absence of any extremal table in the local
SmallGrp documentation. If a hidden web table already lists these maxima,
the contribution reduces to an independently rerunnable certificate
(which is still the citable artifact).

## Limitations

- Trusts the SmallGroups library and GAP lattice/class machinery.
- Fp presentations are computer-generated (`IsomorphismFpGroup`), not
hand-minimized; `SimplifiedFpGroup` output is recorded verbatim.
- Scope is exactly order 96; no asymptotic or general-`n` claim is made.
