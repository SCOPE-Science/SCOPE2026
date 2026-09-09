# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Chermak–Delgado fragments at orders 64 and 81, with calibration and one CD-minimal witness

## 1. What is proved and computed (self-contained)

**Definition.** For a finite group $G$ and $H\le G$ the CD-measure is
$m(H)=|H|\cdot|C_G(H)|$. Let $m(G)=\max_H m(H)$; the Chermak–Delgado lattice is
$\mathrm{CD}(G)=\{H:m(H)=m(G)\}$. Its least member is the CD-subgroup
(the **Chermak–Delgado subgroup**). Width = size of the largest antichain.
A group is **CD-minimal** if $|\mathrm{CD}(G)|=2$ (McCulloch 2017: then
$\mathrm{CD}(G)=\{1,G\}$, forcing $G$ non-nilpotent non-abelian).

**Lemma (abelian case, proof).** If $G$ is abelian, $C_G(H)=G$ for all $H$, so
$m(H)=|H||G|$ is strictly increasing in $|H|$; hence $m(G)=|G|^2$ and
$\mathrm{CD}(G)=\{G\}$, width 1.
*Used for:* C64, C8×C8, C81, C9×C9 as machine-checked theorem instances
(tables additionally asserted abelian elementwise before applying it, and the
general pipeline independently recomputed the same values).

**Method (exact, stdlib-only).** Each group is a committed explicit
multiplication table on $\{0,\dots,n-1\}$ (cyclic, $\mathbb F_p^k$ vector,
dihedral / generalized-quaternion / semidihedral / $C_q\rtimes C_p$ product
formulas, $Q_8$ signed units, $S_3/S_4/A_4$ permutation tables, direct
products). Before any invariant is computed, the script brute-force verifies
associativity ($n^3$ triples), identity, and inverses. The subgroup lattice is
enumerated by single-element adjunction (complete: every $H$ is reached by
adjoining its elements one at a time), centralizers by brute force, $m(G)$ and
$\mathrm{CD}(G)$ by exhaustive scan, width by exact matching-based
Dilworth computation with brute-force antichain re-verification in
`verify.py`. An independent verifier using a *different* lattice route
(cyclic-join closure to fixpoint) reproduces every entry: **VERIFY_OK**.

## 2. Results table (all machine-verified, VERIFY_OK)

| group | $|\mathrm{Sub}|$ | $m(G)$ | $|\mathrm{CD}|$ | width | type | CD member orders |
|---|---|---|---|---|---|---|
| S3 (calib) | 6 | 9 | 1 | 1 | chain | [3] |
| D8 (calib) | 10 | 16 | 5 | 3 | quasi-antichain M_3 | [2,4,4,4,8] |
| Q8 (calib) | 6 | 16 | 5 | 3 | quasi-antichain M_3 | [2,4,4,4,8] |
| A4 (calib) | 10 | 16 | 1 | 1 | chain | [4] |
| **S4 (CD-minimal witness)** | 30 | 24 | **2** | 1 | chain {1,S4} | [1,24] |
| C64 | 7 | 4096 | 1 | 1 | chain | [64] |
| C8×C8 | 37 | 4096 | 1 | 1 | chain | [64] |
| D64 | 69 | 1024 | 1 | 1 | chain | [32] |
| Q64 | 37 | 1024 | 1 | 1 | chain | [32] |
| SD64 | 53 | 1024 | 1 | 1 | chain | [32] |
| D8×C8 (ord 64, max-width QA here) | 89 | 1024 | 5 | 3 | quasi-antichain M_3 | [16,32,32,32,64] |
| C81 | 5 | 6561 | 1 | 1 | chain | [81] |
| C9×C9 | 23 | 6561 | 1 | 1 | chain | [81] |
| C3^4 (ord 81) | 212 | 6561 | 1 | 1 | chain ({G}); subgroup-lattice ranks [1,40,130,40,1], width 130 | [81] |
| C9⋊C3, $a:x\mapsto 4x$ | 10 | 81 | 6 | 4 | quasi-antichain M_4 | [3,9,9,9,9,27] |
| C27⋊C3, $a:x\mapsto 10x$ (max-width QA here) | 14 | 729 | 6 | 4 | quasi-antichain M_4 | [9,27,27,27,27,81] |

**Calibration.** D8 and Q8 both yield the textbook quasi-antichain $M_3$
($m=16$, orders [2,4,4,4,8], width 3) of Brewster–Hauck–Wilcox; S3 yields
$\mathrm{CD}=\{A_3\}$ ($m=9$, $G\notin\mathrm{CD}$); all agree with the
literature and validate the pipeline. Widths 3 ($=1+2^1$) and 4 ($=1+3^1$)
conform to An's theorem that quasi-antichain widths are $1+p^a$.

## 3. Claims (precise scope — what is and is not claimed)

- **Claim A (certified CD-minimal witness).** The committed $S_4$ table
  (order 24) has exactly 30 subgroups, $m(S_4)=24$, and
  $\mathrm{CD}(S_4)=\{1,S_4\}$ — a CD-minimal group. Verified by two
  independent lattice routes. (Outside the 64/81 window; offered as the
  fallback's certified CD-minimal witness, not as a 64/81 extremal.)
- **Claim B (exact CD data for 12 named groups of orders 64/81).**
  The per-group rows above (orders 64: C64, C8×C8, D64, Q64, SD64, D8×C8;
  orders 81: C81, C9×C9, C3^4, two semidirects) are exact for the committed
  tables; replay with `python3 verify.py` prints VERIFY_OK.
- **Claim C (maximal-width quasi-antichain witnesses *within the computed set*).**
  Among computed order-64 groups the widest quasi-antichain is D8×C8 ($M_3$,
  width 3); among computed order-81 groups the widest is C27⋊C3 ($M_4$,
  width 4). **Not** claimed maximal over all 267/15 groups.
- **Claim D (C3^4 subgroup-lattice width).** $C_3^4$ has 212 subspaces with
  rank sizes [1,40,130,40,1] (Gaussian binomials) and subgroup-lattice width
  130 (Sperner middle rank, explicit witness stored, pairwise
  incomparability machine-checked). Its CD lattice is $\{G\}$ (width 1).
- Explicitly **not** claimed: the full 267+15 census, CD-minimality inside
  orders 64/81, or global maximal-width status. Those need GAP/SmallGroups,
  unavailable here (no GAP binary, no root). The fallback "complete table"
  is therefore downgraded to the 12-group exact table above.

## 4. Reproduction

```
cd output/artifacts
python3 cd_compute.py S3        # one group; ALL = all non-vspace (excl. C2x6)
python3 vspace.py C3x4          # 212-subspace enumeration (~40 s)
python3 verify.py               # independent replay -> VERIFY_OK (see verify.log)
```

## 5. Files

- `output/artifacts/tables.py` — committed mult tables (re-checked in-script).
- `output/artifacts/cd_compute.py` — primary enumeration.
- `output/artifacts/vspace.py` — C3^4 subspace enumeration.
- `output/artifacts/fix_c34.py` — relabels C3x4 CD fields per abelian lemma.
- `output/artifacts/verify.py` — independent cyclic-join replay + width recheck.
- `output/artifacts/verify.log` — VERIFY_OK transcript.
- `output/artifacts/results/*.json` — 16 per-group certificates.
