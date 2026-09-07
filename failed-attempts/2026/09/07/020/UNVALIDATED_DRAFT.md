# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Complete h*-vector census with extremal witness for hollow and once-punctured lattice tetrahedra of normalized volume 20

## Abstract
We close the normalized-volume-20 stratum for lattice 3-simplices (tetrahedra)
with at most one interior lattice point. Up to unimodular equivalence there are
exactly 24 Ehrhart h*-vectors with h3 in {0,1}: 16 hollow (h3=0) and 8
once-punctured (h3=1), listed in Theorem 1 with explicit Hermite-normal-form
(HNF) representatives, dual lattice-point certificates (L1,L2,L3, boundary,
interior), Ehrhart-series identities and certified lattice widths. Stratum
maxima are max-h1 = 19 attained by (1,19,0,0) and max lattice width = 2
(318 of 597 h01 tetrahedra attain it). The census is exhaustive over all 1085
HNF types (ordered-diagonal count verified) with two independent exact-integer
counting routes agreeing on every case, plus Ehrhart reciprocity, White
empty-tetrahedron consistency and a one-command replay script.

## 1. Objects and normal form

Let T = conv{0,v1,v2,v3} subset R^3 with vi in Z^3 linearly independent.
Normalized volume V(T) = |det[v1 v2 v3]| (6x Euclidean volume).
Write M = [v1 v2 v3] (3x3, columns = vertices). Unimodular equivalence fixing
the origin is M -> U M, U in GL(3,Z).

**HNF fact (Cohen, Course in Computational Algebraic Number Theory,
Algorithms 2.4.5/2.4.8; SymPy normalforms implementation).**
Every full-rank integer M is left-equivalent U M = H to a unique
lower-triangular H = [[d1,0,0],[a21,d2,0],[a31,a32,d3]] with
di >= 1, 0 <= a21 < d1, 0 <= a31 < d1, 0 <= a32 < d2.
Indeed H^T is the (right) HNF of M^T (upper-triangular, row-bounded), transposed.
Hence, fixing an ordering of the three non-zero vertices, every class contains
exactly one such H; varying the ordering only duplicates coverage, harmless for
a census of values. Conversely every such H defines a tetrahedron with columns
as vertices: 0, (d1,a21,a31), (0,d2,a32), (0,0,d3), of volume d1 d2 d3.

For V=20 the ordered diagonal types d1 d2 d3 = 20 are 18 in number
(2^2*5 exponent distributions: 6 ways for 2^2 times 3 ways for 5).
Per type the count is d1^2 d2 (choices of a21,a31,a32). Summing gives

  sum_{d1 d2 d3=20} d1^2 d2 = 1085,

verified by the logged generator (also equals sum d2 d3^2 by reversal symmetry).
The artefact `hnf_list.csv` enumerates all 1085 with columns-as-vertices
coordinates. This is a covering (indeed canonical-up-to-ordering) set: for any
T = conv{0,w1,w2,w3}, form W=[w1 w2 w3], take its left-HNF H=U W; then
conv{0, columns of H} = U(T). So every unimodular class meets the list.

*Pitfall documented:* interpreting rows (instead of columns) as vertices with
the same matrix set gives a different, non-canonical family (12 h01 vectors
only). The correct columns interpretation reproduces the full stratum and is
used throughout. Both routes below use columns.

## 2. Ehrhart counts and h*

For a 3-simplex, Ehrhart function L_T(t)=|tT cap Z^3| is a cubic polynomial
with L_T(0)=1, and Ehrhart series sum_{t>=0} L_T(t) x^t
= (h0+h1 x+h2 x^2+h3 x^3)/(1-x)^4. With V=sum hi and

  L(t) = sum_i hi C(t+3-i,3),

evaluating at t=1,2,3 gives (h0=1)

  h1 = L1-4,
  h2 = L2-10-4 h1,
  h3 = L3-20-10 h1-4 h2,

and h3 equals the number of interior lattice points of T (Stanley reciprocity).
Boundary = L1 - interior.

**Counting.** Fix H and t in {1,2,3}. Vertices of tT:
0, t(d1,a21,a31), t(0,d2,a32), t(0,0,d3).
Bounding box: 0<=x<=t d1, 0<=y<=t max(a21,d2), 0<=z<=t max(a31,a32,d3)
(tight; max box at t=3 is 61x? with <=976 points for column bounds -- tiny,
so brute force is exact and fast).

Route A (barycentric, integer numerators): write p=(x,y,z)=c1 t v1'+... with
v1'=(d1,a21,a31) etc. (unscaled). Then c1=x/(t d1),
M2=y d1 - x a21, c2=M2/(t d1 d2),
M3=z d1 d2 - x a31 d2 - M2 a32, c3=M3/(t d1 d2 d3),
NS=x d2 d3 + M2 d3 + M3. Membership: M2>=0, M2+x d2<=t d1 d2, M3>=0,
NS<=t d1 d2 d3. Strict versions (>0, <bound) for interior. All integer ops.

Route B (facets, independent): four facet planes via 3x3 integer determinants.
Reference signs from centroid C=v1+v2+v3 (=4x barycenter, scaled to integers).
Point p inside iff all four det(q-p,r-p,p-p)... have reference sign or zero;
interior iff none zero. Entirely different arithmetic (determinants vs
barycentric solve), same boxes.

Both routes use only Python integers (arbitrary precision, no floating).
Agreement is required on every (HNF,t); any mismatch aborts.

**Checks on every HNF:** nonnegativity hi>=0, sum hi=20 (=V, determinant check),
h3 == directly counted strict interior int1, and Ehrhart reciprocity
L(-1)=-int1 where L(-1) is exact-Fraction cubic interpolation through
L0=1,L1,L2,L3 evaluated at -1 (all 1085 pass).

## 3. Theorem (volume-20 hollow + once-punctured census)

**Theorem 1.** Over lattice tetrahedra of normalized volume 20, the set of
h*-vectors with h3 in {0,1} is exactly the following 24 vectors
(16 with h3=0, 8 with h3=1):

hollow (h3=0):
(1,0,19,0),(1,1,18,0),(1,2,17,0),(1,3,16,0),(1,4,15,0),(1,5,14,0),
(1,6,13,0),(1,7,12,0),(1,9,10,0),(1,10,9,0),(1,11,8,0),(1,12,7,0),
(1,13,6,0),(1,14,5,0),(1,15,4,0),(1,19,0,0);

once-punctured (h3=1):
(1,1,17,1),(1,3,15,1),(1,4,14,1),(1,5,13,1),
(1,6,12,1),(1,7,11,1),(1,8,10,1),(1,9,9,1).

Each occurs; no other h3 in {0,1} vector occurs at volume 20.

*Proof (computer).* Exhaust the 1085 HNF matrices. Dual counts give
(L1,L2,L3) and hence h* per above; all consistency identities hold.
Filtering h3 in {0,1} (597 tetrahedra: 351 hollow + 246 once-punctured) and
deduplicating yields exactly the 24 listed; the verifier asserts set equality
with the hardcoded list. Full per-simplex log: `hnf_census_full.csv`
(1085 rows, both routes agreed, 0 mismatches). Distinct table with one HNF
representative + (L1,L2,L3,boundary,interior) certificate per h*:
`distinct_hstar_h01.csv`. One-command replay: `python3 output/artifacts/verify.py`
(~40-70s, stdlib only) regenerates the HNF list, dual recounts, all identities
and asserts the identical 24-set. ∎

Representative certificates (first occurrence in HNF order; H=(d1,a21,d2,a31,a32,d3),
vertices columns; L=(L1,L2,L3); W=width, u=witness):

| h* | H | L | int/bdry | W(u) |
|---|---|---|---|---|
| (1,0,19,0) | (20,1,1,1,0,1) | (4,29,96) | 0/4 | 1 (0,-1,0) |
| (1,1,17,1) | (20,3,1,7,0,1) | (5,31,99) | 1/4 | 2 (-1,2,2) |
| (1,1,18,0) | (10,1,1,1,0,2) | (5,32,102) | 0/5 | 1 (0,-1,0) |
| (1,2,17,0) | (10,1,1,2,0,2) | (6,35,108) | 0/6 | 1 (0,-1,0) |
| (1,3,15,1) | (5,1,2,0,1,2) | (7,37,111) | 1/6 | 2 (0,-1,0) |
| (1,3,16,0) | (5,1,1,1,0,4) | (7,38,114) | 0/7 | 1 (0,-1,0) |
| (1,4,14,1) | (4,1,5,0,2,1) | (8,40,117) | 1/7 | 2 (0,0,-1) |
| (1,4,15,0) | (4,1,1,1,0,5) | (8,41,120) | 0/8 | 1 (0,-1,0) |
| (1,5,13,1) | (4,0,5,2,2,1) | (9,43,123) | 1/8 | 2 (0,0,-1) |
| (1,5,14,0) | (2,1,5,0,1,2) | (9,44,126) | 0/9 | 2 (-1,0,-1) |
| (1,6,12,1) | (4,0,5,0,2,1) | (10,46,129) | 1/9 | 2 (0,0,-1) |
| (1,6,13,0) | (2,0,5,1,3,2) | (10,47,132) | 0/10 | 2 (-1,0,0) |
| (1,7,11,1) | (2,1,5,0,4,2) | (11,49,135) | 1/10 | 2 (-1,0,0) |
| (1,7,12,0) | (2,0,5,0,1,2) | (11,50,138) | 0/11 | 2 (-1,0,-1) |
| (1,8,10,1) | (2,1,2,0,1,5) | (12,52,141) | 1/11 | 2 (-1,0,0) |
| (1,9,9,1) | (2,1,2,0,0,5) | (13,55,147) | 1/12 | 2 (-1,0,0) |
| (1,9,10,0) | (2,1,1,1,0,10) | (13,56,150) | 0/13 | 1 (0,-1,0) |
| (1,10,9,0) | (1,0,10,0,1,2) | (14,59,156) | 0/14 | 1 (-1,0,0) |
| (1,11,8,0) | (1,0,5,0,1,4) | (15,62,162) | 0/15 | 1 (-1,0,0) |
| (1,12,7,0) | (1,0,4,0,2,5) | (16,65,168) | 0/16 | 1 (-1,0,0) |
| (1,13,6,0) | (1,0,4,0,0,5) | (17,68,174) | 0/17 | 1 (-1,0,0) |
| (1,14,5,0) | (1,0,2,0,1,10) | (18,71,180) | 0/18 | 1 (-1,0,0) |
| (1,15,4,0) | (1,0,2,0,0,10) | (19,74,186) | 0/19 | 1 (-1,0,0) |
| (1,19,0,0) | (1,0,1,0,0,20) | (23,86,210) | 0/23 | 1 (-1,-1,0) |

Frequencies (HNF count per h*): 21,6,24,12,48,24,24,12,48,18,24,24,24,18,48,24,6,54,60,24,24,12,12,6 (sum 597). Full distribution h3: 0:351, 1:246, 2:246, 3:114, 4:109, 5:15, 6:4 (total 1085). All 39 distinct h* overall (24 h01 + 15 with h3>=2) satisfy sum 20, h1>=h3 (Hibi-type), L(-1)=-h3.

## 4. Extremal witnesses

Lattice width in primitive u: max_{T} u.x - min_{T} u.x (integer; vertices integral).
For columns tetrahedron, y_i=u.vi, y=(M^T)u with M=[v1 v2 v3]. Width<w implies
|y_i|<=w-1 (interval length w-1 containing 0). Hence |u|_inf <= ||(M^T)^{-1}||_{inf->inf}(w-1),
with (M^T)^{-1} entries n11=1/d1, n22=1/d2, n33=1/d3, n12=-a21/(d1d2),
n23=-a32/(d2d3), n13=(a21a32-a31d2)/(d1d2d3) (exact Fractions). So for candidate
minimum w* the search bound Bcert=ceil(rmax(w*-1)) (0 if w*=1) is certified:
any better direction would lie in the searched box. Search increasing boxes of
primitive u; Bcert<=1 throughout the h01 stratum, so certification is a tiny
exhaustive check (<=27 directions) plus, for w*=1, the integer-dot argument
(width>=1 for any nonzero u since vertices affinely span R^3).

**Stratum maxima (h3 in {0,1}, 597 tetrahedra, all widths certified):**
- Max h1 = 19, uniquely (up to HNF duplicates, 6x) vector (1,19,0,0),
  e.g. H=(1,0,1,0,0,20), verts 0,(1,0,0),(0,1,0),(0,0,20), L=(23,86,210), width 1.
- Max width = 2, attained by 318/597 tetrahedra, e.g. H=(2,1,2,0,1,5),
  verts 0,(2,1,0),(0,2,1),(0,0,5), h*=(1,8,10,1), L=(12,52,141),
  witness u=(-1,0,0) giving dots {0,-2,0,0} range 2, Bcert=1 (check 26 neighbours).
  No h01 tetrahedron has width >=3 (exhaustive; verifier re-checks all 597).

Context: width 3 does occur at volume 20 outside the stratum, e.g.
H=(4,0,5,2,4,1), h*=(1,6,11,2) (h3=2), width 3 witness (-1,-1,1), Bcert=2,
proving the h01 max-2 bound is nontrivial.

## 5. Consistency: White, Hibi, reciprocity

- *Ehrhart reciprocity:* L(-1)=-interior holds with exact Fractions for all 1085.
- *Hibi-type:* h1>=h3 holds for all 1085 (in particular all 24).
- *White (consistency only, not used as proof):* White classifies *empty*
  (L1=4) tetrahedra as T(a,b,q). Our census has exactly one empty h*
  (1,0,19,0), L1=4, e.g. H=(20,1,1,1,0,1), verts (20,1,1),(0,1,0),(0,0,1),
  mapped by permutation U=[[0,1,0],[0,0,1],[1,0,0]] (det 1) to White T(1,1,20).
  The remaining 15 hollow vectors have L1>4 (hollow-with-boundary, not White-empty),
  as expected beyond White; no claim of White classification for them.

## 6. What is proved vs computed vs uncertain

- *Proved (mathematical):* HNF existence/uniqueness covering argument (cited),
  Ehrhart h* inversion formulas, width certificate bound (M^T)^{-1} argument,
  White implication for the single empty case (explicit U).
- *Computed evidence (exact, replayable):* dual integer counts agreeing on all
  1085x3 cases; derived h* set equality; reciprocity/sum/nonnegativity/Hibi
  checks; exhaustive width scan certifying max 2. No floating point, no sampling,
  no heuristics in the final pipeline. Independent rerun via `verify.py`
  reproduces the identical 24-set (tested).
- *Uncertainty / limits:* correctness relies on (i) cited HNF theorem for the
  column convention, (ii) correct implementation of two independent counters
  (mitigated by their mutual agreement + facet/barycentric diversity + tiny boxes
  auditable by hand), (iii) Python integer/determinant arithmetic (standard).
  No claim about h3>=2 completeness beyond the logged 15 vectors (provided for
  context, same pipeline). No claim of unimodular uniqueness of representatives
  (only h* completeness). No originality claim over White/multi-width/point-count
  theories; delta is the compiled V=20 joint census + replayable pipeline.

## 7. Reproducibility

Artefacts (all under `output/artifacts/`):
`hnf_list.csv` (1085 HNF + vertex coordinates),
`hnf_census_full.csv` (1085 rows: H,L1,L2,L3,int1-3,h*,L(-1)),
`distinct_hstar_h01.csv` (24 rows: h*,L, representative H, boundary/interior, freq),
`witnesses.json` (per-rep widths/witnesses/Bcert, stratum maxima, White U, width-3 outside note),
`summary.json`, `verify.py` (stdlib-only, `python3 output/artifacts/verify.py` => VERIFY PASS).

## References (for context, not claimed)

White's empty-tetrahedron theorem (exposition arXiv:1610.01981); width-1
multi-width classification (arXiv:2304.03627); lattice 3-polytopes with few
points (Blanco-Santos et al., arXiv:1409.6701); GRDB Fano tables (grdb.co.uk);
Cohen, A Course in Computational Algebraic Number Theory, Alg. 2.4.5/2.4.8
(HNF); Normaliz documentation (alternative counter capability).
