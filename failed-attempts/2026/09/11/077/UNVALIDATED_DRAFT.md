# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact diameter 8 and eccentricity census of the full supersingular 2-isogeny graph at p = 1009

## Claim

Let `p = 1009` and `F = Fp[s]/(s^2 - 11)` (11 is the least quadratic nonresidue mod 1009).
Let `G` be the full supersingular 2-isogeny graph over `F`: vertices are the supersingular
j-invariants in `F`, and `j ~ j'` iff `Phi_2(j, j') = 0`, where `Phi_2` is the classical
modular polynomial

    Phi_2(X,Y) = X^3+Y^3-X^2Y^2+1488(X^2Y+XY^2)-162000(X^2+Y^2)
                 +40773375 XY+8748000000(X+Y)-157464000000000.

`Phi_2` is symmetric, so adjacency is undirected (2-isogenies pair with their duals).
Then:

- `G` is connected with **84 vertices** (all of `F`, listed in `output/artifacts/ledger.json`),
  it is **simple and 3-regular** (no loops, no multiple edges; 126 edges),
  because neither `j = 0` (supersingular iff `p = 2 mod 3`) nor `j = 1728`
  (supersingular iff `p = 3 mod 4`) is supersingular at `p = 1009 = 1 mod 12`.
  Hence no loop/multiplicity convention choice affects any distance.
- The **exact diameter is D = 8**, radius 7.
- The **eccentricity histogram** is `{7: 61, 8: 23}`.
- There are **30 unordered diametral pairs**. The committed witness pair
  (ledger indices 11, 59) is `j_a = (752, 965)`, `j_b = (972, 306)`
  (coordinates are `(a, b)` = `a + b*s` in `F`).
- A shortest `j_a -> j_b` path of length 8, with every link satisfying `Phi_2 = 0`, is

  | step | j |
  |------|---|
  | 0 | (752, 965) |
  | 1 | (815, 366) |
  | 2 | (529, 0) |
  | 3 | (155, 0) |
  | 4 | (635, 421) |
  | 5 | (524, 482) |
  | 6 | (643, 156) |
  | 7 | (258, 294) |
  | 8 | (972, 306) |

- Each of the 8 links is realized by an explicit rational 2-isogeny over `F`
  (translated Velu quotient by an `F`-rational order-2 kernel point), in **both**
  directions; the full chains are logged below and in `output/artifacts/velu_chains.json`.

Ledger SHA-256: `f08040927748263c528ae0981726da1cf7653d264b1575dad16ee673c77b6293`
Replay: `python3 output/artifacts/verify.py` prints `VERIFY_OK`
(stdlib only apart from numpy for the vectorized scan; seconds-to-minutes).

## Method (reproducible)

1. **Phi_2 self-test over Z** (exact integer arithmetic, in `compute_graph.py`):
   `Phi_2(0, Y) = (Y - 54000)^3` and `Phi_2(1728, Y) = (Y - 1728)(Y - 287496)^2`,
   plus symmetry `Phi_2(a,b) = Phi_2(b,a)` on 20 random integer pairs. All pass.
2. **Supersingular seed over Fp.** `y^2 = x^3 + x + 7` over F_1009 has
   `#E(Fp) = 1010 = p + 1` (direct point count; trace 0, hence supersingular),
   with `j = 155`. Since `|t| <= 2*sqrt(1009) < 1009`, trace 0 is the only
   supersingular trace with `#E = p+1` reachable by naive search, and one seed
   suffices by connectivity (verified a posteriori: closure has 84 vertices,
   matching the theory count `floor(1009/12) = 84` for `p = 1 mod 12`).
3. **Neighbor enumeration over all of F_{p^2}.** For each `j`, `Phi_2(j, Y)` is a
   cubic in `Y` over `F`; all `p^2 = 1018081` values of `Y` are tested by a
   vectorized Horner evaluation. BFS closure from the seed reaches 84 vertices.
4. **Symmetry/regularity check.** Every recorded edge is reciprocal
   (`i in adj[k]` whenever `k in adj[i]`); every vertex has simple-degree 3,
   no loops. So `G` is a connected simple 3-regular graph on 84 vertices.
5. **All-pairs BFS.** BFS from every vertex gives eccentricities, `D = 8`,
   histogram `{7: 61, 8: 23}`, radius 7, and 30 unordered diametral pairs.
6. **Velu chains.** Along the diametral j-path, at each step a short-Weierstrass
   model over `F` is maintained; the three roots of `x^3 + a x + b` (all three
   are `F`-rational at every step of both chains) give the three order-2
   subgroups; the kernel whose translated-Velu codomain has the target
   j-invariant is selected and its domain/kernel/codomain logged. The backward
   chain replays the reversed j-path from the canonical model of `j_b`.
   Every step's codomain formula `a' = Bp - 3t^2`, `b' = 2t^3 - t*Bp`
   (`A = 3x_0`, `B = 3x_0^2 + a`, `A' = -2A`, `B' = A^2 - 4B`, `t = A'/3`)
   is re-verified by the independent checker.

## Velu chains

Curves are `y^2 = x^3 + a x + b` with `a, b` in `F` written `[u, v] = u + v*s`.
`ker` is the x-coordinate of the order-2 kernel generator `(ker, 0)`.

### Forward chain (j_a -> j_b), 8 steps

| # | domain (a, b) | ker x | codomain (a, b) | j_in -> j_out |
|---|---------------|-------|-----------------|---------------|
| 0 | ([279,376],[186,587]) | [728,881] | ([804,95],[664,303]) | (752,965)->(815,366) |
| 1 | ([804,95],[664,303]) | [324,600] | ([50,649],[600,43]) | (815,366)->(529,0) |
| 2 | ([50,649],[600,43]) | [461,292] | ([352,89],[828,806]) | (529,0)->(155,0) |
| 3 | ([352,89],[828,806]) | [316,367] | ([675,525],[652,244]) | (155,0)->(635,421) |
| 4 | ([675,525],[652,244]) | [658,265] | ([22,483],[1004,398]) | (635,421)->(524,482) |
| 5 | ([22,483],[1004,398]) | [379,866] | ([532,497],[839,974]) | (524,482)->(643,156) |
| 6 | ([532,497],[839,974]) | [310,714] | ([205,59],[267,419]) | (643,156)->(258,294) |
| 7 | ([205,59],[267,419]) | [725,39] | ([416,83],[207,581]) | (258,294)->(972,306) |

### Backward chain (j_b -> j_a), 8 steps

| # | domain (a, b) | ker x | codomain (a, b) | j_in -> j_out |
|---|---------------|-------|-----------------|---------------|
| 0 | ([2,987],[674,658]) | [966,337] | ([772,948],[939,832]) | (972,306)->(258,294) |
| 1 | ([772,948],[939,832]) | [248,672] | ([877,159],[494,434]) | (258,294)->(643,156) |
| 2 | ([877,159],[494,434]) | [663,859] | ([419,260],[340,872]) | (643,156)->(524,482) |
| 3 | ([419,260],[340,872]) | [784,355] | ([91,853],[756,175]) | (524,482)->(635,421) |
| 4 | ([91,853],[756,175]) | [995,66] | ([400,92],[369,457]) | (635,421)->(155,0) |
| 5 | ([400,92],[369,457]) | [426,407] | ([267,576],[311,634]) | (155,0)->(529,0) |
| 6 | ([267,576],[311,634]) | [453,639] | ([248,167],[263,513]) | (529,0)->(815,366) |
| 7 | ([248,167],[263,513]) | [683,287] | ([442,163],[189,375]) | (815,366)->(752,965) |

(The forward and backward chains use different intermediate curve models, as
expected: each direction builds its own models from its own start. What agrees
is the j-path, reversed exactly.)

## Independent verification

`output/artifacts/verify.py` (stdlib + numpy) checks, from the committed
`ledger.json` / `velu_chains.json` only:

- ledger SHA-256 match;
- 84 distinct vertices; adjacency symmetric, simple 3-regular, 126 edges, no loops;
- a **fresh independent re-implementation** of the Phi_2 neighbor scan reproduces
  the full committed adjacency table (3/3 roots in-set at every vertex);
- count `84 = floor(1009/12)` and correct absence of `j = 0, 1728`;
- all-pairs BFS: connected, `D = 8`, histogram `{7: 61, 8: 23}`, radius 7,
  30 unordered diametral pairs, committed path of length 8 between indices 11, 59;
- `Phi_2 = 0` on all 8 path links (independent Fp2 evaluator);
- seed curve `#E(Fp) = 1010` by direct count; seed `j = 155` sits on the path;
- all 16 Velu steps replay: kernel on curve, translated-Velu formulas reproduce
  the codomain, domain/codomain j-invariants match the path links.

Output ends with `VERIFY_OK n=84 D=8 hist=[[7,61],[8,23]] pairs=30 sha256=f080...6293`.

## Limitations / scope notes

- The graph-construction rule is the standard one: adjacency via `Phi_2 = 0`
  (2-isogeny up to isomorphism, dual edges identified). At `p = 1009` there are
  no loops or multi-edges, so symmetrization conventions cannot shift the result.
- Vertex completeness rests on BFS closure from a certified supersingular seed
  plus the match `84 = floor(1009/12)`; the independent verifier additionally
  rebuilds every adjacency row from `Phi_2` and confirms closure (all roots in-set).
- The Velu chains certify the 8-step diametral path geometrically; the diameter
  upper bound `D <= 8` comes from exhaustive all-pairs BFS over the verified
  adjacency table (recomputed by the auditor script), and `D >= 8` from the path.
- The remaining 29 diametral pairs are counted but their paths are not individually
  logged; any of them can be extracted from the committed adjacency table by BFS.
