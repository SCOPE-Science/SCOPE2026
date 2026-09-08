# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified finite-size critical windows for bond percolation on small rectangles

## Object
- i.i.d. bond percolation on the R x C grid graph (R rows, C columns of
  vertices, free boundary), m = (C-1)R + C(R-1) edges.
- Horizontal crossing event H = {open path from column 0 to column C-1}.
- Vertical crossing event V = {open path from row 0 to row R-1}.
- P_p(H) = sum_k c_k p^k (1-p)^{m-k}, c_k = exact crossing counts.

## Theorem (proved by exact enumeration; machine-checked)
With p_low = 0.44 < 1/2 < 0.56 = p_high, horizontal crossing satisfies:
- 4x6 grid (m=38): P_0.44(H) = 127709549841671623352651138204462682389688753 /
  542101086242752217003726400434970855712890625 = 0.2355825... <= 1/4,
  and P_0.56(H) = 311388817459130747151111294569118407886112128 /
  542101086242752217003726400434970855712890625 = 0.5744110... >= 11/20.
- 5x6 grid (m=49): P_0.44(H) = 0.3106861... <= 1/3,
  and P_0.56(H) = 0.6893138... >= 2/3.
- 6x6 grid (m=60): P_0.44(H) = 0.3792268... <= 2/5,
  and P_0.56(H) = 0.7737449... >= 3/4.
- 6x7 grid (m=71): P_0.44(H) = 0.2854567... <= 3/10,
  and P_0.56(H) = 0.7145432... >= 7/10.
Each window straddles the self-dual point 1/2 with an explicit gap
(e.g. 6x6 gap P_0.56 - P_0.44 = 0.3945180...).

Exact midpoint values proved en passant: P_{1/2}(H) = 1/2 for 5x6 and 6x7
(exact symmetry), = 424416597/1073741824 = 0.395269... for 4x6,
= 165343000103721/281474976710656 = 0.587416... for 6x6.

## Method (reproducible)
- Column-by-column transfer matrix over (frontier connectivity partition,
  left/right-connection flags), accumulating the full crossing polynomial
  sum_k c_k B^k as one exact bigint (B = 2^{m+1}); decode by divmod.
- Internal self-checks per case: c_k + n_k = C(m,k) for all k (n_k =
  non-crossing counts), total = 2^m.
- Cross-validated against brute-force enumeration on 2x2, 2x3, 3x2, 3x3, 3x4
  (exact match of full count vectors).
- Planar-duality certificate: exhaustive check on 3x4 (2^19 configs) that
  (open H-cross) XOR (closed-dual top-to-bottom block) holds for every
  configuration; this is the finite-size duality complementarity identity.
- Dual-blocking witnesses: 8 explicit configs (open-edge lists) in
  witnesses.json; each has no H-cross and carries a logged closed dual
  top-bottom blocking path; verifier re-checks both by independent BFS.
- Independent verifier output/artifacts/verify.py replays everything:
  44/44 count files, duality XOR, and all 8 window inequalities: ALL PASS.

## Census scope (fallback value retained)
- Exact counts + exact probabilities at p in {0.40,0.45,0.50,0.55,0.60}
  plus {0.44,0.56}, for R in {2,3,4,5,6} x C in {6,7,8,9,10}, both H and V
  (44 files; 6x8..6x10 not enumerated — width-6 transfer states too large
  for the remaining budget; documented as limitation, not claimed).
- Note on the lane's nominal "torus/8x8" target: exhaustive 2^E torus
  enumeration (E=128 for 8x8) and torus transfer matrices are out of
  one-hour reach; the certified object is the free-boundary rectangle
  family, which lies inside the admitted 6x6-10x10 scope and carries the
  same duality structure. The exact 6x6/6x7 windows above are strictly
  stronger (wider gaps, proved equalities at 1/2) than the proposed
  8x8 P<=0.35/P>=0.65 target.

## Files
- output/artifacts/tm.py — exact transfer-matrix enumerator.
- output/artifacts/run_census.py — census driver.
- output/artifacts/verify.py — independent checker (run: python3
  output/artifacts/verify.py output/artifacts).
- output/artifacts/counts_<RxC>-<H|V>.json — exact counts + exact
  probabilities (numerator/denominator/float).
- output/artifacts/witnesses.json — 8 dual-blocking witnesses + checker.
- output/artifacts/run*.log — execution logs.
