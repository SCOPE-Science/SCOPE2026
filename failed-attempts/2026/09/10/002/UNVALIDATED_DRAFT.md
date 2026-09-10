# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-490 (NO_RESULT): auditable obstruction to the admitted CP* route

## 1. Target restated
Show: every Cutting Planes refutation of T(G, τ_odd) with |coeff| ≤ 60³ needs length ≥ 4096 = 2¹²,
chaining (i) certified expansion of the 60-vertex graph, (ii) a logged Delayer strategy forcing
Resolution width ≥ 9, (iii) a stated lifting + feasible-interpolation conversion with explicit
constants. A CP* refutation with ≤ 4095 lines would be a tightness witness.

## 2. What was verified (replay: `python3 output/artifacts/verify.py` → `VERIFY_OK`)
- Concrete 60-vertex 3-regular simple symmetric instance (`graph.json`): 90 edges; recomputed
  spectrum λ* = 2.732051 ≤ 2√2 = 2.828427 (margin 0.0964, tr A² = 180.0, max eig residual 1.8e-15);
  non-bipartite via certified 9-cycle; diameter 7; girth 4.
- Tseitin instance: 90 variables, 240 clauses of width exactly 3, odd charge τ(0) = 1.
- Exact small-set edge-boundaries by exhaustive enumeration: (k=1)→3, (k=2)→4, (k=3)→5, (k=4)→4.
- Naive bridge-avoidance Delayer R (sound: never falsifies a clause; defer non-bridges, answer
  forced bridges) scores 31–50 on long prover orders — but this is not a lower bound over all orders.

## 3. Obstruction (why the admitted route fails)
**Trap prover.** For any edge e = (u,v): query the two other incident edges of u and the two other
incident edges of v with values rigged so the two endpoints demand opposite values on e, then query
e. All four setup queries are non-bridges of the unqueried-edge graph (removing ≤ 4 edges from a
3-connected Ramanujan graph cannot isolate u or v), so R defers on all four (4 points); e is then
forced and falsifies a vertex clause. Verified uniformly: score exactly 4 on all 90/90 edges, every
deferral legality-checked, every game ending in a genuinely falsified width-3 clause.

Consequences:
- The constructed Delayer R does **not** satisfy the fallback criterion (score ≥ 9 against every
  prover order): the explicit 5-query trap order holds it to 4 < 9. No alternative ≥9-strategy was
  certified in the remaining time, so the preset fallback is not claimed.
- Even width 9 would not convert: Ben-Sasson–Wigderson at V = 90 gives size ≥ exp(36/1440) ≈ 1.025;
  2⁹ = 512 < 4096; reaching 4096 via BSW needs width ≥ ~112. Link (iii) has no standard constants.

## 4. What is NOT claimed
- No upper bound on the true Resolution width or CP* length of the instance: the trap defeats one
  explicit Delayer R, not the game value; optimal-Prover/optimal-Delayer analysis was not done.
- No claim that the instance is "easy" or that a ≤ 4095-line CP* refutation exists.
- The textbook-identity caveat: the direct LPS(2,5) quaternion recipe yields det-2 matrices and
  (2/5) = −1, so the canonical LPS object needs a quotient choice; the tested object is a certified
  3-regular Ramanujan Cayley graph on PSL(2,5) (60 vertices). A future attempt must pin the literal
  graph definition first.

## 5. Artifacts (verification-critical only)
- `output/artifacts/graph.json` — fixed 60-vertex adjacency list + spectrum.
- `output/artifacts/delayer_strategy.py` — Delayer R + simulator with soundness argument.
- `output/artifacts/verify.py` — stdlib+numpy replay verifier (checks [1]–[5], prints VERIFY_OK).
- `output/WORKLOG.md` — working notes incl. EMERGENT_CANDIDATE assessment.

## 6. Status
NO_RESULT on TARGET; fallback not met; obstruction evidence preserved and replayable.
