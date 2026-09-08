# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact certified W1/W2 cost table with Kantorovich duality on 4x4 and 5x5 Manhattan grids

## Abstract
We compute and certify exact 1- and 2-Wasserstein costs for a fixed suite of
finitely supported probability measures (rational masses with denominator 8)
on 4x4 and 5x5 grids with Manhattan ground cost. The suite comprises 12 core
pairs (P01–P06 on 4x4, P07–P12 on 5x5), one strict mass-splitting extremal
(P05S), and one displacement-midpoint triple (M1/M2/M3), i.e. 16 certified
pairs total. Every pair carries: (i) an exact optimal transport permutation
(primal plan), (ii) an exact integer assignment-dual certificate with zero
duality gap, and (iii) for W1, an exact integer grid-level 1-Lipschitz
Kantorovich potential attaining the primal cost. All certificates are replayed
in exact integer arithmetic by a stdlib-only verifier. The splitting extremal
is proved optimal-only-by-splitting: both supply tokens at the doubled node
must separate, with explicit nonsplit gaps. The midpoint triple certifies cost
additivity W1(S,T) = W1(S,Mid) + W1(Mid,T) = 8/8 + 8/8 = 16/8.

## 1. Setup and conventions
- Grid: 4x4 nodes {(x,y): 0<=x,y<=3} or 5x5 nodes {0<=x,y<=4}, ground cost
  d = Manhattan distance, W2 ground cost d^2.
- Measures: each measure is recorded as 8 tokens of mass 1/8 (a node with mass
  k/8 appears k times in the token list). Hence for token lists
  S=(s_1..s_8), T=(t_1..t_8):
  W1 = (1/8) min_perm sum_i d(s_i,t_perm(i)),
  W2^2 = (1/8) min_perm sum_i d(s_i,t_perm(i))^2.
  A transport plan is pi[i,j]=1/8 iff j=perm(i). Costs are reported as exact
  fractions W1_num8/8 and W2sq_num8/8 with integer numerators.
- Assignment dual: max sum u + sum v s.t. u[i]+v[j] <= c[i][j] (c = d or d^2),
  integer vectors. Zero gap sum(u)+sum(v) = perm cost certifies optimality.
- Grid Kantorovich potential (W1 only): integer phi on grid nodes with
  |phi(a)-phi(b)| <= 1 on every grid edge and
  sum_x phi(x)(mu(x)-nu(x)) = W1_num8, where mu,nu are token counts (sum 8).
  This certifies W1 at measure level (Kantorovich duality on the grid metric).

## 2. Certified cost table
W1 = value/8, W2sq = value/8. Grid is 4 or 5.

| id  | grid | description | W1 | W2^2 |
|-----|------|-------------|----|------|
| P01 | 4 | shift-east cols0-1 to cols1-2 | 8/8 = 1 | 8/8 = 1 |
| P02 | 4 | doubled corners to edge-midpoints | 8/8 = 1 | 8/8 = 1 |
| P03 | 4 | doubled main diagonal to anti-diagonal | 16/8 = 2 | 40/8 = 5 |
| P04 | 4 | concentration to (1,1) | 20/8 = 5/2 | 58/8 = 29/4 |
| P05 | 4 | near-identity with 2/8 at (1,1) | 2/8 = 1/4 | 2/8 = 1/4 |
| P06 | 4 | checkerboard black to white | 8/8 = 1 | 8/8 = 1 |
| P07 | 5 | shift-east cols0-1 to cols1-2 | 8/8 = 1 | 8/8 = 1 |
| P08 | 5 | doubled corners to center | 32/8 = 4 | 128/8 = 16 |
| P09 | 5 | middle row to middle column | 4/8 = 1/2 | 4/8 = 1/2 |
| P10 | 5 | diagonal+corners to anti-diagonal+corners | 4/8 = 1/2 | 8/8 = 1 |
| P11 | 5 | perimeter ring to inner ring | 10/8 = 5/4 | 16/8 = 2 |
| P12 | 5 | corners (0,0),(4,4) to (0,4),(4,0) | 32/8 = 4 | 128/8 = 16 |
| P05S | 4 | STRICT-SPLIT extremal (see §3) | 6/8 = 3/4 | 16/8 = 2 |
| M1 | 4 | full displacement S->T at speed 2 | 16/8 = 2 | 32/8 = 4 |
| M2 | 4 | first half S->MID | 8/8 = 1 | 8/8 = 1 |
| M3 | 4 | second half MID->T | 8/8 = 1 | 8/8 = 1 |

Token lists S,T, optimal perms, dual vectors (u,v), and grid potentials phi
are archived in output/artifacts/certificates.json and grid_phis.json.

Pair definitions (token lists, 8 entries):
- P05S: S = [(0,0),(0,3),(3,0),(2,0),(0,2),(3,2),(1,1),(1,1)],
  T = [(0,0),(0,3),(3,0),(2,0),(0,2),(1,2),(3,3),(3,3)].
  Shared background D (5 tokens) plus supply extras {(3,2),(1,1)x2} and demand
  extras {(1,2),(3,3)x2}. The only doubled demand node is (3,3).
- M1/M2/M3: S0 = left 4x2 block [(0,*),(1,*)], MID = middle block [(1,*),(2,*)],
  T0 = [(2,*),(3,*)] (rows 0..3). M1=(S0,T0), M2=(S0,MID), M3=(MID,T0).

## 3. Theorems (proved by exact replayable computation)
Theorem 1 (exact table). For each of the 16 pairs, the W1 and W2^2 values in
the table above are exact. Witnesses: the archived permutation attains the
claimed numerator; the archived integer (u,v) is feasible
(u[i]+v[j]<=c[i][j] for all i,j) with sum(u)+sum(v) equal to that numerator;
hence the permutation is optimal by LP strong duality. Verified in exact
integer arithmetic for all 16 pairs x 2 costs.
Theorem 2 (grid potentials). For each pair, the archived integer grid function
phi is 1-Lipschitz on grid edges and sum phi(mu-nu) equals W1_num8, hence is an
exact Kantorovich potential certifying W1 at measure level. Verified for all 16.
Theorem 3 (strict splitting extremal P05S). Every W1-optimal and every
W2-optimal plan for P05S splits the doubled supply node (1,1): the two tokens
at (1,1) go to different demand tokens. Proof: the only demand node holding >=2
tokens is (3,3) (token indices 6,7). The cheapest plan pinning both (1,1)-tokens
to (3,3)-tokens costs 10/8 (W1) resp. 36/8 (W2sq), by exhaustive 6x6 remainder
enumeration, strictly above the optima 6/8 resp. 16/8 (gaps 4/8 and 20/8).
Hence no optimal plan is nonsplit (non-Monge) for either cost.
Theorem 4 (midpoint). With S0,MID,T0 as above,
W1(S0,T0)=16/8=8/8+8/8=W1(S0,MID)+W1(MID,T0); legs have W2sq 8/8 each and the
full pair 32/8. Costs certified as in Theorem 1.

## 4. Methods (reproducible, stdlib-only)
- Primal: exhaustive 8! permutation enumeration in integers (brute force),
  cross-checked against an exact-integer Hungarian assignment solver that also
  emits the dual (u,v). Agreement required.
- Grid potentials: exact simplex (Fractions) for max bal.phi s.t.
  |phi_a-phi_b|<=1, then integrality observed and verified; stored as ints.
- Splitting: constrained enumeration — pin both doubled-supply tokens to the
  unique doubled-demand node, optimize the remaining 6x6 assignment by
  exhaustive 6! enumeration; compare against global optimum.
- Independent verifier output/artifacts/verify.py re-derives everything from
  the archived JSON only: marginal/token sanity, perm cost equality, dual
  feasibility + strong duality, phi Lipschitz + value, splitting gaps,
  midpoint additivity. Prints ALL VERIFIED.

## 5. What is proof vs computation vs conjecture
- Proof: Theorems 1–4 are proved in the certificate sense — finite exact
  integer checks with zero duality gap, replayable by verify.py. No floating
  point is used anywhere.
- Computed evidence: the optimal perms/duals/potentials themselves were found
  by the search programs (compute_table.py, finalize.py); their optimality is
  then proved by the replay checks above.
- Conjecture: none. No general claim beyond the fixed suite is made.
- Uncertainty: none about the stated equalities conditional on correct
  execution of the integer verifier; residual risk is limited to transcription
  of pair definitions, mitigated by the verifier re-reading the same JSON.

## 6. Limitations and scope
- Fixed suite only (denominator-8 masses, Manhattan cost, 4x4/5x5 grids);
  no general OT theorem is claimed.
- W2 certificates are assignment-dual (token-level LP), not grid-level
  potentials; W1 additionally has grid-level potentials.
- Originality claim is the archived artifact (paired primal plans + duals +
  grid potentials + splitting/midpoint witnesses with replay logs), not the
  general Kantorovich theory or bare distance values.

## 7. Reproduction
Run from the lane root:
  python3 output/artifacts/compute_table.py   # rebuilds 12-pair table
  python3 output/artifacts/finalize.py        # adds P05S/M1-M3 + exact grid phis
  python3 output/artifacts/verify.py          # independent exact replay
Regeneration is deterministic; verification uses only stdlib.
