# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified per-block maximal-gap census to 2,000,000 with merit and an admissible prime-constellation witness

## 1. Claim (packaging, not a world record)
We produce a complete, byte-reproducible audit bundle for primes ≤ 2,000,000:
(a) every prime (148,933) from a logged segmented Eratosthenes sieve (base primes ≤ 1409, segment size 32,768, 62 segments);
(b) all 148,932 gaps `g = q − p`;
(c) per 100k-block table (20 blocks): prime count `n_k`, maximal gap `g_max(k)` over gaps with left endpoint in the block, least first-occurrence pair, merit `m = g/ln p`, achiever multiplicity;
(d) global first-occurrence list (61 gap values);
(e) deterministic Miller–Rabin (bases 2,7,61) certificates for every prime / every gap endpoint, with stored residues for all 148 endpoints of interest;
(f) certified constellation witnesses: quadruplet (5,7,11,13) and diameter-16 sextuplet (7,11,13,17,19,23) with offsets, sieve window, certificates;
(g) independent replay (different sieve code, bases 2,3,5,7,11) that byte-reproduces both CSVs and re-verifies all primality claims, with SHA-256 hashes.
No new maximal-gap world record is claimed: the maximum gap 132 below 2M is long known. Novelty is the closed, replayable certificate bundle with merit analysis.

## 2. Method
**Sieve (`census.py`, stdlib only).** Simple sieve to ⌊√2M⌋ = 1414 gives 223 base primes (max 1409). Segmented marking over `[2, 2000000]` in steps of 32768 (62 segments, each logged). Result: π(2M) = 148,933, last prime 1,999,993. Gaps assigned to blocks `B_k = ((k−1)·10⁵, k·10⁵]` by left endpoint (B₁ = (0,10⁵] so includes 2).
**Miller–Rabin.** Deterministic for 32-bit integers with bases {2,7,61} (covers all n < 2,032,801²; every n ≤ 2M is far below the threshold, so the test is a proof, not heuristic). Applied to all 148,933 primes; full (base, residue, pass) residues archived for the 148 distinct endpoints appearing in block achievers, global first occurrences, and constellation members.
**Constellation scan.** Linear scan of the prime set for offsets (0,2,6,8), retaining the first; then patterns (0,4,6,10,12,16) and (0,2,6,8,12,18). Admissibility checked by residue coverage.
**Replay (`replay.py`, independent code).** Monolithic (non-segmented) sieve; trial division to 1000 plus MR bases {2,3,5,7,11}; re-reads `gaps.csv` (difference exactness, endpoint primality, index-adjacency = consecutiveness); proves interior compositeness of all 61 first-occurrence gaps by sieve-membership plus MR; regenerates both CSVs and asserts byte equality; re-checks constellation offsets/primality/admissibility and cross-verifies stored certificates.

## 3. Results
### 3.1 Block maxima
| k | interval | n_k | g_max | first (p,q) | merit g/ln p | #ach |
|---|---|---|---|---|---|---|
| 1 | (0,100000] | 9592 | 72 | (31397,31469) | 6.9535 | 1 |
| 2 | (100000,200000] | 8392 | 86 | (155921,156007) | 7.1924 | 1 |
| 3 | (200000,300000] | 8013 | 82 | (265621,265703) | 6.5653 | 1 |
| 4 | (300000,400000] | 7863 | 112 | (370261,370373) | 8.7350 | 1 |
| 5 | (400000,500000] | 7678 | 114 | (492113,492227) | 8.6980 | 1 |
| 6 | (500000,600000] | 7560 | 90 | (576791,576881) | 6.7847 | 1 |
| 7 | (600000,700000] | 7445 | 98 | (604073,604171) | 7.3621 | 1 |
| 8 | (700000,800000] | 7408 | 78 | (736279,736357) | 5.7738 | 3 |
| 9 | (800000,900000] | 7323 | 100 | (838249,838349) | 7.3319 | 1 |
| 10 | (900000,1000000] | 7224 | 92 | (927869,927961) | 6.6955 | 1 |
| 11 | (1000000,1100000] | 7216 | 106 | (1098847,1098953) | 7.6205 | 1 |
| 12 | (1100000,1200000] | 7224 | 98 | (1139993,1140091) | 7.0268 | 1 |
| 13 | (1200000,1300000] | 7083 | 96 | (1242643,1242739) | 6.8411 | 1 |
| 14 | (1300000,1400000] | 7105 | 132 | (1357201,1357333) | 9.3478 | 1 |
| 15 | (1400000,1500000] | 7029 | 110 | (1468277,1468387) | 7.7467 | 1 |
| 16 | (1500000,1600000] | 6972 | 132 | (1561919,1562051) | 9.2557 | 1 |
| 17 | (1600000,1700000] | 7014 | 126 | (1671781,1671907) | 8.7931 | 1 |
| 18 | (1700000,1800000] | 6931 | 102 | (1761187,1761289) | 7.0924 | 2 |
| 19 | (1800000,1900000] | 6957 | 126 | (1889831,1889957) | 8.7185 | 1 |
| 20 | (1900000,2000000] | 6904 | 96 | (1904311,1904407) | 6.6392 | 1 |

Multi-achiever blocks: B₈ g=78 at (736279,736357), (794249,794327), (795349,795427); B₁₈ g=102 at (1761187,1761289), (1775069,1775171). Full lists in `block_achievers.json`. Σn_k = 148,933 ✓.
Global maximum gap ≤ 2M is **132** (blocks 14 and 16). Merits peak at 9.35 — below Cramér's (ln 2M)² ≈ 211 and consistent with merit-vs-log scatter (no anomaly claimed).

### 3.2 Global first occurrences (gap → least (p,q), merit)
1→(2,3)1.4427; 2→(3,5)1.8205; 4→(7,11)2.0556; 6→(23,29)1.9136; 8→(89,97)1.7823; 10→(139,149)2.0266; 12→(199,211)2.2670; 14→(113,127)2.9615; 16→(1831,1847)2.1298; 18→(523,541)2.8756; 20→(887,907)2.9464; 22→(1129,1151)3.1299; 24→(1669,1693)3.2345; 26→(2477,2503)3.3270; 28→(2971,2999)3.5015; 30→(4297,4327)3.5861; 32→(5591,5623)3.7085; 34→(1327,1361)4.7283; 36→(9551,9587)3.9282; 38→(30593,30631)3.6791; 40→(19333,19373)4.0529; 42→(16141,16183)4.3348; 44→(15683,15727)4.5547; 46→(81463,81509)4.0680; 48→(28229,28277)4.6838; 50→(31907,31957)4.8213; 52→(19609,19661)5.2612; 54→(35617,35671)5.1524; 56→(82073,82129)4.9490; 58→(44293,44351)5.4213; 60→(43331,43391)5.6198; 62→(34061,34123)5.9410; 64→(89689,89753)5.6120; 66→(162143,162209)5.5017; 68→(134513,134581)5.7581; 70→(173359,173429)5.8028; 72→(31397,31469)6.9535; 74→(404597,404671)5.7317; 76→(212701,212777)6.1952; 78→(188029,188107)6.4227; 80→(542603,542683)6.0587; 82→(265621,265703)6.5653; 84→(461717,461801)6.4404; 86→(155921,156007)7.1924; 88→(544279,544367)6.6630; 90→(404851,404941)6.9707; 92→(927869,927961)6.6955; 94→(1100977,1101071)6.7569; 96→(360653,360749)7.5025; 98→(604073,604171)7.3621; 100→(396733,396833)7.7573; 102→(1444309,1444411)7.1916; 104→(1388483,1388587)7.3531; 106→(1098847,1098953)7.6205; 110→(1468277,1468387)7.7467; 112→(370261,370373)8.7350; 114→(492113,492227)8.6980; 118→(1349533,1349651)8.3597; 120→(1895359,1895479)8.3017; 126→(1671781,1671907)8.7931; 132→(1357201,1357333)9.3478.
(61 values; gaps 108, 116, 124, 128, 130 never occur ≤ 2M.)

### 3.3 Constellation witnesses
- **Quadruplet** (offsets 0,2,6,8): **(5, 7, 11, 13)** — the least prime quadruplet; all four certified prime by MR(2,7,61) with stored residues and by replay TD+MR(2,3,5,7,11). Sieve window [2,33]: primes {2,3,5,7,11,13,17,19,23,29,31}, composites else (full per-integer dump in `constellation.json`).
- **Sextuplet** (pattern 0,4,6,10,12,16): **(7, 11, 13, 17, 19, 23)** — likewise dual-certified. Both patterns verified admissible (no prime's residues fully covered).
- Note: these least witnesses are classical (5–13 and 7–23); the contribution is their machine-checkable certificates inside the bundle, not discovery.

## 4. Verification summary
- `census.py` ≈ 0.9 s; `replay.py` ≈ 2.3 s; single core, stdlib only, runtime gate (<10 min) met by two orders of magnitude.
- Replay asserts: π(2M)=148933 with last prime 1999993; all 148,932 CSV gaps exact/prime/consecutive; all 61 first-occurrence interiors composite (sieve-membership + MR); regenerated `block_maxima.csv` and `first_occurrences.csv` byte-identical (MATCH/MATCH); constellation offsets, primality, admissibility re-proved; 148 stored MR details cross-verified under different bases.
- SHA-256 (`SHA256SUMS.txt`): gaps.csv 087446f3…; block_maxima.csv e43d17eb…; first_occurrences.csv 2a90969a…; mr_certificates.json 108f95b8…; constellation.json 89c259da…; sieve.log 3b2a00af…; block_achievers.json ec393e02…; replay.log fe48fe17…. (Pre-replay sieve.log hash 87edc4af… was superseded by the appended-hash final log; both recorded in WORKLOG chain. Final file hashes above govern.)

## 5. Limitations, conjecture vs proof, and prior art
- **Proof:** everything inside [2, 2M] (counts, gaps, maxima, first occurrences, witness primality) is proved by the two agreeing computations; MR determinism below 2,032,801² makes each primality verdict unconditional.
- **Not claimed:** any new world-record gap (132 ≪ published records 806/906 at 10¹⁵); any merit extremality beyond the stated table; any theorem about gaps above 2M or Cramér's model (merit column is descriptive data).
- **Bug encountered:** replay's first interior-compositeness check used trial division only to 1000 and false-flagged 1444363 = 1181×1223 as prime; repaired by using sieve-membership + independent MR. No census data changed; the incident shows why the dual method matters.
- **Prior art:** exhaustive gap tables (Nicely, Kourbatov, Visser, Prime Pages) already cover 2M; first-occurrence/minimal-constellation theory is classical. Originality is strictly the closed per-block + merit + dual-MR + byte-replay bundle, and the report disavows record novelty.
- **Reproducibility:** rerun `python3 census.py && python3 replay.py` (stdlib, CPython 3.12 tested); compare SHA-256 against §4. `gaps.csv` (2.7 MB) dominates size; all other artifacts are kilobytes.

## 6. Artifacts
`output/artifacts/gaps.csv`, `block_maxima.csv`, `first_occurrences.csv`, `block_achievers.json`, `mr_certificates.json`, `constellation.json`, `sieve.log`, `replay.log`, `SHA256SUMS.txt`; scripts `census.py`, `replay.py` at workspace root.
