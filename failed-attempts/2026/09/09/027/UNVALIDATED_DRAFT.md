# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Paired LCD / one-dimensional-hull witnesses at five short cells with Gram-rank, tally, and MacWilliams certificates

## Statement (fallback-level theorem; proved by computation)

Let a binary $[n,k]$ code be given by a $k\times n$ generator $G$ over $\mathbf F_2$
(bit $c$ of each stored integer = coordinate $c$, LSB = coordinate 0).
Hull dimension is $h=k-\mathrm{rank}_{\mathbf F_2}(GG^T)$;
minimum distance is the minimum nonzero weight of the $2^k$ codewords.

At each of the five cells $(n,k)\in\{(16,5),(20,5),(20,6),(24,6),(24,7)\}$
there exist explicit generators $G^{LCD}_{n,k}$ and $G^{one}_{n,k}$ with:

| $[n,k]$ | LCD witness: $(d,h,\mathrm{rk}\,GG^T)$ | one-dim witness: $(d,h,\mathrm{rk}\,GG^T)$ | Griesmer UB | widths |
|---|---|---|---|---|
| $[16,5]$ | $d=6,h=0,\mathrm{rk}=5$ | $d=6,h=1,\mathrm{rk}=4$ | 8 | 2, 2 |
| $[20,5]$ | $d=9,h=0,\mathrm{rk}=5$ | $d=9,h=1,\mathrm{rk}=4$ | 9 | 0, 0 |
| $[20,6]$ | $d=8,h=0,\mathrm{rk}=6$ | $d=8,h=1,\mathrm{rk}=5$ | 8 | 0, 0 |
| $[24,6]$ | $d=10,h=0,\mathrm{rk}=6$ | $d=10,h=1,\mathrm{rk}=5$ | 11 | 1, 1 |
| $[24,7]$ | $d=9,h=0,\mathrm{rk}=7$ | $d=8,h=1,\mathrm{rk}=6$ | 10 | 1, 2 |

Consequences (all machine-checked):
- Both hull values $\{0,1\}$ are realized at every committed cell (hull spectrum contains $\{0,1\}$).
- Achieved LCD-vs-one-dim gaps $d_{LCD}-d_{one}$ are $0,0,0,0,1$; every cell has a
  two-sided interval of width $\le 2$ (achieved $d$ below, Griesmer UB above), so the
  true gap satisfies $|d_{LCD}-d_{one}|\le 2$ throughout.
- Monotonicity on achieved lower bounds holds along the chains: $6\le 9$ at $k=5$,
  $8\le 10$ at $k=6$ (consistent with Bouyuklieva shortening monotonicity, checked as an inequality on witnesses, not proved as a general theorem here).
- $[20,5]$ and $[20,6]$ witnesses are Griesmer-optimal codes (width 0).

## Witnesses (integers; bit $c$ = coordinate $c$)

- $[16,5]$ LCD: $[7873, 47202, 12708, 31976, 46224]$
- $[16,5]$ one-dim: $[40001, 46306, 35428, 23176, 26288]$
- $[20,5]$ LCD: $[62177, 726690, 449700, 812456, 212432]$
- $[20,5]$ one-dim: $[440289, 989282, 1040516, 225000, 712144]$
- $[20,6]$ LCD: $[1033025, 657346, 104324, 580872, 422288, 89312]$
- $[20,6]$ one-dim: $[1048321, 701058, 1023172, 745672, 129488, 815712]$
- $[24,6]$ LCD: $[4013825, 6528066, 9549124, 6150728, 9074320, 15201696]$
- $[24,6]$ one-dim: $[11519745, 10951298, 2337988, 13790600, 7742416, 6001568]$
- $[24,7]$ LCD: $[10238209, 914946, 16139012, 7385864, 5711376, 11663776, 11179200]$
- $[24,7]$ one-dim: $[3391873, 4630018, 12656132, 1918344, 10387984, 12342944, 13417920]$

(Canonical copy in `artifacts/witnesses.json`.)

## Proof / verification route (reproduced by `artifacts/verify.py`, stdlib only)

1. **Generator rank:** exact $\mathbf F_2$ elimination on $G$ gives rank $k$.
2. **Hull:** form $M=GG^T$ ($M_{ij}=$ parity of bitwise AND of rows $i,j$);
   exact elimination gives $\mathrm{rk}\,M$; $h=k-\mathrm{rk}\,M$ equals the claimed 0 or 1.
3. **Distance:** exhaustive $2^k\le 128$ codeword tally; minimum nonzero weight equals claimed $d$.
4. **MacWilliams replay:** dual basis from pivot/free-column elimination, full $2^{n-k}$
   dual tally, exact integer Krawtchouk identity
   $B_j = 2^{-k}\sum_i A_i K_j(i)$ at every $j$ — PASS at all 10 witnesses.
5. **Syndrome check ($n\le 20$):** all errors of weight $\le\lfloor(d-1)/2\rfloor$ have
   distinct syndromes — PASS at all 6 witnesses with $n\le 20$; at $n=24$ distance rests on
   (3)+(4).
6. **Upper side:** Griesmer bound $n\ge\sum_{i=0}^{k-1}\lceil d/2^i\rceil$ gives the UB column;
   widths $\le 2$ everywhere.

Run: `python3 artifacts/verify.py` $\to$ `VERIFY_OK` (10/10 cells OK).

## What is NOT claimed

- No exact $d_{LCD}(n,k)$/$d_{one}(n,k)$ pins except the two Griesmer-optimal cells
  $[20,5]$ ($d=9$) and $[20,6]$ ($d=8$), where achieved distance meets the Griesmer UB and is
  hence exactly optimal among *all* binary linear codes (a fortiori within the hull class).
  Elsewhere only the stated two-sided width-$\le 2$ intervals are proved.
- No building-up linkage between the LCD and one-dim witnesses is exhibited
  (audit-plan success criterion not met); witnesses were found by independent
  hull-constrained stochastic search, so no structural transformation claim is made.
- No claim that the bare distances are new vs Bouyuklieva $d_{LCD}$ tables or
  Li–Shi–Kim $d_{one}$ values; the new content is the *paired Gram-rank-certified bundle
  with replay logs and gap row* as one auditable unit.
- No statement about Li–Shi–Kim residue classes (Thm 6.15/6.16) is re-verified here.

## Relation to prior work

- Li–Shi–Kim 2211.02480 ($d_{one}$, $k=5$ partial), Kim et al. 2210.14549 (building-up hull
  census to $n\le 13$), Bouyuklieva 2010.13399 ($d_{LCD}$ tables to $n\le 40$ + monotonicity),
  Liu–Li 2406.02065 ($[n,6]$ LCD, $n\ge 51`) motivate the question; none publishes this
  paired Gram-rank + syndrome + MacWilliams bundle with gap row at these cells
  (per admission triage; triage was API/abstract-level, so stated as candidate-level gap).
