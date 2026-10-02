# Explicit length-6 maximal green sequence for the non-minimal triple-arrow rank-4 quiver Q_T3D121C

## Context

Per-member maximal green sequence (MGS) existence for mutation-infinite quivers
is nontrivial: Muller proved MGS existence is not invariant under quiver
mutation, and the Lawson–Mills theorem (every minimal-mutation-infinite quiver
of rank ≥ 4 is Louise and has an MGS) applies only under minimal-infiniteness.
No general theorem supplies an explicit MGS word for non-minimal triple-arrow
rank-4 classes. This record certifies one such word with a full replayable
c-matrix log.

## Definitions

- Quiver / exchange matrix: a rank-4 skew-symmetric integer matrix
  B = (b_{ij}); b_{ij} > 0 means b_{ij} arrows i → j.
- Framed seed: the pair (B, C) with C = I_4 initially.
- C-matrix mutation (FZ extended rule), mutating at k:
  B'_{ij} = -B_{ij} if i = k or j = k, else
  B'_{ij} = B_{ij} + [B_{ik}]_+ [B_{kj}]_+ − [−B_{ik}]_+ [−B_{kj}]_+;
  C'_{ij} = −C_{ij} if j = k, else
  C'_{ij} = C_{ij} + [C_{ik}]_+ [B_{kj}]_+ − [−C_{ik}]_+ [−B_{kj}]_+.
- Green / red: column j of C is green if it is nonzero and entrywise ≥ 0;
  red if nonzero and entrywise ≤ 0. Statuses presuppose sign-coherence
  (no mixed-sign column).
- Maximal green sequence: a mutation word in which every mutated vertex is
  green at mutation time and the terminal C-matrix is all-red.

## Result

Let

    B_T = [[0,3,0,-1],[-3,0,1,0],[0,-1,0,2],[1,0,-2,0]]

(3 arrows 1 → 2, 1 arrow 2 → 3, 2 arrows 3 → 4, 1 arrow 4 → 1;
QMD Q.n4.16518fcc0c6931a9).

From the framed seed (B_T, C = I_4), the word

    w = (2, 4, 3, 1, 2, 4)

is a maximal green sequence of length 6 (≤ 10). Every mutated vertex is green
at mutation time, every intermediate C-matrix is sign-coherent, and the
terminal C-matrix has columns (−e_4, −e_3, −e_2, −e_1), hence all-red.

## Proof / evidence (per-step certificate)

Statuses list columns 1–4 as G (green) / R (red).

- t=0: C = I_4, status (G,G,G,G).
- Mutate 2: B = [[0,-3,3,-1],[3,0,-1,0],[-3,1,0,2],[1,0,-2,0]],
  C = [[1,0,0,0],[0,-1,1,0],[0,0,1,0],[0,0,0,1]], status (G,R,G,G).
  Vertex 2 was green.
- Mutate 4: B = [[0,-3,1,1],[3,0,-1,0],[-1,1,0,-2],[-1,0,2,0]],
  C = [[1,0,0,0],[0,-1,1,0],[0,0,1,0],[1,0,0,-1]], status (G,R,G,R).
  Vertex 4 was green.
- Mutate 3: B = [[0,-2,-1,1],[2,0,1,-2],[1,-1,0,2],[-1,2,-2,0]],
  C = [[1,0,0,0],[0,0,-1,0],[0,1,-1,0],[1,0,0,-1]], status (G,G,R,R).
  Vertex 3 was green.
- Mutate 1: B = [[0,2,1,-1],[-2,0,1,0],[-1,-1,0,3],[1,0,-3,0]],
  C = [[-1,0,0,1],[0,0,-1,0],[0,1,-1,0],[-1,0,0,0]], status (R,G,R,G).
  Vertex 1 was green.
- Mutate 2: B = [[0,-2,3,-1],[2,0,-1,0],[-3,1,0,3],[1,0,-3,0]],
  C = [[-1,0,0,1],[0,0,-1,0],[0,-1,0,0],[-1,0,0,0]], status (R,R,R,G).
  Vertex 2 was green.
- Mutate 4: B = [[0,-2,0,1],[2,0,-1,0],[0,1,0,-3],[-1,0,3,0]],
  C = [[0,0,0,-1],[0,0,-1,0],[0,-1,0,0],[-1,0,0,0]], status (R,R,R,R).
  Vertex 4 was green. All-red termination.

All C-matrices above are sign-coherent, so green/red statuses are well defined.
The terminal C-matrix is a permutation matrix with all signs negative
(det = +1), hence all-red. Length 6 satisfies the admitted bound ≤ 10.

The certificate was verified by two independent implementations:
`output/artifacts/verify_mgs.py` (flat-list routine, prints VERIFY_OK) and a
from-scratch audit replay; both reproduce every (B, C) entry exactly.

## Limitations

- Per-member / per-seed existence only: one MGS word for this quiver from the
  framed seed. By Muller non-invariance, nothing is claimed about
  mutation-equivalent quivers.
- Mutation-infiniteness and non-minimality (deletions of 3 or 4 retain the
  3-arrow Kronecker pair, infinite by Derksen–Owen for rank ≥ 3) are assumed
  background, not proved here.
- No Louise / Banff cover is claimed or proved here.
- A secondary depth-≤ 5 DFS (214 nodes, no all-red terminal) suggests length 6
  is minimal, but the headline claim requires only length ≤ 10.

## Reproducibility

Run `python3 output/artifacts/verify_mgs.py` (Python stdlib only).
Expected output: per-step (B, C) log as above, then
`LENGTH 6 <= 10 OK`, `TERMINAL all-red OK`, `VERIFY_OK`.

## References

- J. W. Lawson, M. R. Mills, Properties of minimal mutation-infinite quivers,
  arXiv:1610.08333 — minimal-infinite Louise + MGS theorem (scope explicitly
  minimal; does not cover this non-minimal quiver).
- G. Muller, The Existence of a Maximal Green Sequence is not Invariant under
  Quiver Mutation, Electron. J. Combin. 23(2) (2016), doi:10.37236/5412 —
  per-member nontriviality.
- Quiver Mutation Database (QMD), https://quivermutationdb.org — exact lookup
  Q.n4.16518fcc0c6931a9 (found, max_edge 3, explored false, mc_id null);
  wiki definitions of census, Derksen–Owen settlement, and Banff/Louise logic.
