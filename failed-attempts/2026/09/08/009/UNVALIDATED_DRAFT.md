# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Integral homology census of flag 2-skeleta on 7 vertices via Smith normal form, with a minimal 6-vertex RP2 torsion witness and collapse certificate

## Claim (data theorem; fully computed and cross-checked)

Let $G$ range over the 1044 unlabelled graphs on 7 vertices
(`networkx.graph_atlas_g()`, node count 7; atlas indices 209–1252).
For each $G$ let $X(G)$ be its flag 2-skeleton: 7 vertices, the edges of $G$,
and one 2-face per 3-clique of $G$, with fixed sorted orientations.
With $d_1: C_1 \to C_0$, $d_2: C_2 \to C_1$ the integral boundary maps and
$r_i = \mathrm{rank}(d_i)$ read from the Smith normal form:

1. **Zero torsion everywhere in the flag stratum.** For all 1044 complexes,
   $H_1(X(G))$ is free; the SNF diagonal of $d_2$ never contains an entry with
   $|\cdot|>1$. Hence every $H_1$ is $\mathbb{Z}^{b_1}$ and every $H_2$ is
   $\mathbb{Z}^{b_2}$ ($H_2=\ker d_2$ is always free).
2. **Complete Betti distribution** (58 occupied $(b_0,b_1,b_2)$ types, all torsion-free):
   - connected ($b_0=1$): 411 cases, of which 267 have $b_1=0$ (195 with $b_2>0$),
     65 have $b_1=1$, 132 have $b_1=2$, 32 $b_1=3$, 9 $b_1=4$, and $(b_1,b_2)$ up to
     $(5,0)\times1$, $(6,0)\times1$;
   - $b_0=2$: 130 cases; $b_0=3$: 31; $b_0=4$: 9; $b_0=5$: 3; $b_0=6$: 1; $b_0=7$: 1 (empty graph).
   - Extremes: the 7-vertex 2-sphere boundary data occur (e.g. $b_2=20$ for $K_7$,
     whose flag 2-skeleton is the 2-skeleton of the 6-simplex); the largest $b_1$ is 6.
   - Full 1044-row table with $(n_{\rm edges}, n_{\rm tri}, b_0,b_1,b_2, r_1,r_2,$
     both SNF diagonals, greedy-collapse core) is `artifacts/census.csv`.
3. **Minimal torsion threshold.** The 53 atlas graphs on $\le 5$ vertices carry no
   $H_1$ torsion either (`artifacts/small_vertices.txt`). Torsion first appears at
   6 vertices — but necessarily outside the flag stratum: the witness below is a
   general (non-flag) 2-complex.
4. **Minimal witness (general 2-complex, not flag).** On vertex set $\{0,\dots,5\}$
   the 10 facets
   `012, 013, 024, 035, 045, 125, 134, 145, 234, 235`
   form a closed connected 2-manifold with $\chi = 6-15+10 = 1$ in which every edge
   lies in exactly 2 triangles and every vertex link is a 5-cycle. Its integral
   homology, certified by SNF diagonals
   $d_1: (-1^5, 0)$, $d_2: (\pm 1^9, -2)$ (ranks 5, 10), is
   $$H_1 \cong \mathbb{Z}/2,\quad H_2 = 0,\quad H_0 \cong \mathbb{Z},$$
   i.e. a 6-vertex triangulation of $\mathbb{R}P^2$. Note its 1-skeleton is $K_6$,
   so its flag completion is the 5-simplex (contractible): the triangulation must be
   read as a general, non-flag 2-complex, exactly the flag-vs-general contrast of
   the topic.
5. **Collapse certificate.** The witness admits no elementary collapse at all:
   every edge lies in 2 triangles and every vertex in 5 triangles, so there is no
   free face; greedy lex-first collapse takes 0 steps with core $(6,15,10)$, and
   exhaustive DFS over collapse sequences visits exactly 1 state and certifies that
   no sequence reaches a point (`artifacts/collapse_log.txt`,
   `artifacts/collapse_exhaustive.txt`).
6. **Collapsibility census data.** Greedy lex-first collapse was also logged for all
   1044 flag cases (core sizes in `census.csv`): 184 reach a point $(1,0,0)$; the
   remaining 860 stick at non-trivial cores (commonest: $(4,4,0)\times125$,
   $(4,6,4)\times75$). This is reported as raw replay data, not as a theorem about
   collapsibility (greedy is one deterministic rule; see limitations).

## Method (replayable in seconds)

- Enumerate `graph_atlas_g()` (1253 graphs; assert 1044 on 7 vertices, indices 209–1252).
- Per graph: sorted edges, 3-cliques via adjacency check, oriented $d_1$ ($n_0\times n_1$),
  $d_2$ ($n_1\times n_2$); SNF via `sympy.matrices.normalforms.smith_normal_form`;
  $b_0=n_0-r_1$, $b_1=n_1-r_1-r_2$, $b_2=n_2-r_2$; $H_1$ torsion = SNF($d_2$) entries
  with $|\cdot|>1$ (valid because $H_2=\ker d_2$ is free, so torsion of
  $C_1/\mathrm{im}\,d_2$ injects into $H_1$ — $C_0$ is free).
- Cross-checks: Euler identity $n_0-n_1+n_2=b_0-b_1+b_2$ asserted on all 1044+53 cases;
  independent $\mathbb{Q}$-rank of $d_2$ recomputed on 10 spot cases; K7/K6 sanity
  rows; determinism by sorted ordering (no randomness).
- Witness: deterministic lex-first backtracking for 10 triangles on 6 vertices with
  every edge in exactly 2 triangles; manifold/link/connectivity checks in code;
  SNF certificate; greedy + exhaustive collapse audit.
- Replay: `output/artifacts/run.sh` (needs python3 + sympy + networkx); elapsed
  0.9 s in the lane environment.

## Relation to prior work (no overclaim)

- The 6-vertex $\mathbb{R}P^2$ triangulation itself is classical (Kühnel-type minimal
  triangulation); our contribution for the witness is the auditable SNF diagonal
  certificate plus the machine-checked no-collapse proof, not the triangulation.
- Adamaszek ("Small flag complexes with torsion", arXiv:1208.3892) classifies flag
  complexes up to 12 vertices carrying $H_1$ torsion by computer search; our zero-torsion
  finding is consistent with it (torsion needs more vertices / non-2-skeleton cells)
  and our delta is the complete public 1044-row integral Betti-plus-SNF table with
  replay script. Chong–Nevo-type inequalities are field-coefficient and theoretical;
  ours is integral and enumerative. Chessboard/matching-complex torsion work concerns
  different infinite families.

## Limitations / uncertainty

- The "no torsion in flag 7-vertex 2-skeleta" theorem is a verified computation
  (SNF over $\mathbb{Z}$ via sympy), not a structural proof; it depends on sympy's SNF
  and networkx's atlas correctness, mitigated by Euler + $\mathbb{Q}$-rank + spot checks.
- Greedy-collapse cores are rule-dependent data, not collapsibility decisions; only the
  witness's non-collapsibility is proved (exhaustively: no free face exists at all).
- Minimality claim "torsion first at 6 vertices" is proved only within the scanned
  range ($n\le 5$ flag 2-skeleta torsion-free) plus the 6-vertex witness; 6-vertex flag
  2-skeleta were not separately censused (and the witness itself is non-flag).
- The audit-plan item "no flag 2-complex on $\le 5$ vertices carries torsion" is
  established; the stronger phrase "minimality theorem" for the collapse part is not
  claimed beyond the logged failure.
