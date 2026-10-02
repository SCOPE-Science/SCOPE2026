# Exact graded Betti tables, regularity, and projective dimension for seven committed edge ideals (8–10 vertices), including a one-edge regularity jump

## Context

Betti numbers, Castelnuovo–Mumford regularity, and projective dimension of edge
ideals are central to the Stanley–Reisner / Herzog–Hibi / Kalai–Meshulam and
regularity-bound programs. Katzman's bound states the induced-matching number
is a lower bound for regularity. Fröberg's theorem characterizes edge ideals
with 2-linear resolution as exactly chordal (complement chordal) graphs.
Beyond forests/cycles, selected circulants, and the linearity-defect ≤ 1
classification, exact per-ideal graded tables on 8–10 vertices with replayable
certificates are sparse. This record supplies seven such tables.

## Definitions

Work over **QQ**. For a simple graph G on vertices {0,…,n−1}, let
S = QQ[x_0,…,x_{n−1}] and I(G) = (x_a x_b : {a,b} ∈ E(G)) the edge ideal.
Recorded are the minimal graded Betti numbers β_{i,j}(S/I(G)) in homological
degree i and internal degree j. Regularity reg(S/I) = max{j−i : β_{i,j} ≠ 0},
reg(I) = reg(S/I)+1, projective dimension pdim = max{i : β_{i,j} ≠ 0}.
The induced-matching number im(G) is the maximum size of a set of pairwise
disjoint edges with no edge of G joining distinct members.

## Objects (0-indexed, verbatim)

- **G1** (C5 blow-up, n=10): parts {0,1},{2,3},{4,5},{6,7},{8,9}; all 4 edges
  between consecutive parts cyclically. 20 edges:
  02,03,12,13,24,25,34,35,46,47,56,57,68,69,78,79,80,81,90,91.
- **G2** (chordal, n=8): K5 on {0..4} plus 5–{0,1}, 6–{1,2}, 7–{2,3}. 16 edges.
- **G3** (partially whiskered C5, n=8): C5 01,12,23,34,40 plus pendants
  50,61,72. 8 edges.
- **G4** (9v intermediary, n=9): C5 on 0..4 plus 5–{0,1}, 6–{2,3}, 7–{0,3},
  8–{1,4}. 13 edges.
- **G5** (9v partial blow-up, n=9): parts {0,1},{2,3},{4,5},{6,7},{8}; all edges
  between consecutive parts cyclically. 16 edges.
- **H** (n=9): edges 01,12,23,34,40,50,51,61,62 (vertices 7,8 isolated).
  9 edges.
- **H+e** (n=9): H plus e={7,8} (a disjoint K2 component). 10 edges.

## Result (exact, over QQ)

Notation (i,j)^v means β_{i,j} = v.

- **G1**: (1,2)^20, (2,3)^60, (3,4)^65, (3,5)^32, (4,5)^30, (4,6)^80,
  (5,6)^5, (5,7)^80, (6,8)^40, (7,9)^10, (8,10)^1.
  reg(S/I)=2, reg(I)=3, pdim=8, im=1 (witness [0,2]). Exceeds im by 1.
- **G2**: (1,2)^16, (2,3)^46, (3,4)^59, (4,5)^40, (5,6)^14, (6,7)^2.
  reg(S/I)=1, reg(I)=2, pdim=6, im=1 (witness [0,1]). Linear resolution;
  attains im bound.
- **G3**: (1,2)^8, (2,3)^11, (2,4)^4, (3,4)^3, (3,5)^10, (4,6)^6, (5,7)^1.
  reg(S/I)=2, reg(I)=3, pdim=5, im=2 (witness {[2,3],[5,0]}). Attains im bound.
- **G4**: (1,2)^13, (2,3)^26, (2,4)^12, (3,4)^16, (3,5)^44, (4,5)^3,
  (4,6)^55, (5,7)^32, (6,8)^9, (7,9)^1.
  reg(S/I)=2, reg(I)=3, pdim=7, im=2 (witness {[0,1],[6,3]}).
- **G5**: (1,2)^16, (2,3)^42, (3,4)^39, (3,5)^16, (4,5)^15, (4,6)^32,
  (5,6)^2, (5,7)^24, (6,8)^8, (7,9)^1.
  reg(S/I)=2, reg(I)=3, pdim=7, im=1 (witness [0,2]). Exceeds im by 1.
- **H**: (1,2)^9, (2,3)^14, (2,4)^5, (3,4)^6, (3,5)^13, (4,5)^1, (4,6)^9,
  (5,7)^2. reg(S/I)=2, reg(I)=3, pdim=5, im=2 (witness {[2,3],[5,0]}).
- **H+e**: (1,2)^10, (2,3)^14, (2,4)^14, (3,4)^6, (3,5)^27, (3,6)^5,
  (4,5)^1, (4,6)^15, (4,7)^13, (5,7)^3, (5,8)^9, (6,9)^2.
  reg(S/I)=3, reg(I)=4, pdim=6, im=3 (witness {[2,3],[5,0],[7,8]}).

In particular **reg(H+e) = reg(H)+1** in both conventions (S/I: 3 vs 2;
ideal: 4 vs 3), and Katzman im ≤ reg(S/I) holds throughout:
1≤2, 1≤1, 2≤2, 2≤2, 1≤2, 2≤2, 3≤3.

## Proof / evidence

Hochster's formula over QQ:
β_{i,j}(S/I(G)) = Σ_{|W|=j} dim H̃_{j−i−1}(Ind(G[W])),
computed in exact rational arithmetic (stdlib `Fraction` Gaussian elimination
on simplicial boundary matrices over all 2^n subsets). By Hochster's theorem
this yields the minimal free-resolution Betti numbers. Independent checks:

1. **Euler/Hilbert identity**: Σ_{i,j}(−1)^i β_{i,j} t^j equals
   Σ_{F independent} t^{|F|}(1−t)^{n−|F|} exactly for all 7 ideals
   (euler_ok=True).
2. **Calibration**: C5 → (1,2)^5,(2,3)^5,(3,5)^1 reg 2; P3 → linear;
   chordal G2 → linear (Fröberg consistency).
3. **Induced matchings**: exact by branch-and-bound (conflict graph) and
   independently confirmed by brute-force subset enumeration; each witness
   checked induced (no cross edges).
4. **Audit recomputation**: all 7 tables re-executed from the above edge
   lists reproduced the claimed numbers byte-for-byte; reg/pdim read-offs
   (max j−i, max i) verified.

The certificate form is exact Hochster homology, not literal Buchberger
S-pair / Schreyer logs; equivalence to minimal Betti numbers rests on
Hochster's theorem.

## Limitations

- QQ coefficients only; no characteristic-p analysis.
- No Buchberger/Schreyer logs; no minimality-differential matrices.
- The H/H+e jump mechanism is disjoint-component additivity: vertices 7,8
  are isolated in H, so H+e adjoins a K2 component and regularity adds by the
  tensor-product (Künneth) formula. It does not demonstrate connected
  edge-addition monotonicity.
- G3 carries 3 pendants, not the full 5-pendant whiskered C5; any
  Cohen–Macaulay label is loose and not certified here.
- G4/G5/H edge lists are researcher-fixed intermediaries reported verbatim.
- No maximality-over-all-graphs claim; only the 7 listed ideals.

## Reproducibility

`verify_method.py` implements `betti_hochster`, `hilbert_check`,
`induced_matching`, all stdlib-only. Running its `__main__` block writes
G1–G5 tables; H/H+e are obtained by calling `show`/`betti_hochster` on the
edge lists above (e.g. H=[[0,1],[1,2],[2,3],[3,4],[4,0],[5,0],[5,1],[6,1],
[6,2]], H+e=H+[[7,8]]). `tables.json` stores the G1–G5 Betti tables,
K-vectors, and witnesses.

## References

- S. Jacques, Betti Numbers of Graph Ideals, PhD thesis, Sheffield, 2004.
  https://arxiv.org/abs/math/0410107 — Betti/pdim for forests and cycles.
- S. Anand, A. Roy, Graded Betti numbers of some circulant graphs, 2020.
  https://arxiv.org/abs/2007.02401 — three circulant families.
- H. D. Nguyen, T. Vu, Linearity defect of edge ideals and Fröberg's
  theorem, 2015. https://arxiv.org/abs/1506.05769 — defect ≤ 1
  classification (weakly chordal, im ≤ 2).
- T. Hibi et al., Dominating induced matchings and regularity of edge
  ideals, 2014. https://arxiv.org/abs/1412.3881 — im ≤ reg ≤ mmm bounds.
