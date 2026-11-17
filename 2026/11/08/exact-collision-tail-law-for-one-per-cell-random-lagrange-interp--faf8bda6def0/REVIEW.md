# Independent mathematical audit

## correctness

PASS

Each adjacent pair of independently uniform one-per-cell nodes approaches its shared boundary b_i with two independent one-sided gaps u,v; P(u+v<δ)=m²δ²/2. Non-adjacent node separations are bounded below, and successive tiny gaps cannot coexist, bounding W_m(z) by B_m/min_i gap_i. Near one collision, L_i and L_(i+1) have residues ±C_i(z,Y)/(u+v), with all other scaled coefficients vanishing; the Euclidean norm has leading √2|C_i|/(u+v). Integrating over the small triangle and over independent other nodes gives K_m(z)=m²Σ E C_i², with negligible O(t^−4) simultaneous non-adjacent faces, and dominated convergence yields t²P(W>t)→K_m. Each factor positive, so K>0 for m≥3 all fixed z, except m=2 z=1/2 where convex weights bounded. Tail integration gives moments iff p<2 when K>0. Independent symbolic integration verifies m=3 z=1/2: K=9/16−log(2)/2=0.2159264097200273. This is fixed m,z asymptotic, not uniform in m.

## originality

PASS

PASS best-of-knowledge: an earlier general Vandermonde-repulsion interpolation theorem treats exchangeable nodes with joint density proportional to product |xi−xj|^θ, especially iid uniform θ=0, where single interior collisions give threshold p<1. It does NOT encompass exactly one node per adjacent full cell (disjoint labelled supports and two-sided boundary collision codimension 2), nor its exact t^−2 coefficient. Dell’Accio–Sommariva–Vianello 2023 prove almost-sure interpolation unisolvency, which does not imply finiteness/divergence of moments. Random mesh and deterministic stability sources do not supply this stratified sharp constant. Existing near-collision methods are prior tools; unindexed special cases remain priority risk.

## value

PASS

The precise coefficient of the heavy tail and the sharp second-moment threshold quantify a real failure mode of a standard stratified exact-interpolation design: despite a.s. nonsingularity and one node in each cell, independent observation noise has infinite unconditional variance for any fixed degree ≥2 except the two-point midpoint. This is a natural, operationally meaningful invariant; the m=3 midpoint irrational constant is not a routine parameter substitution from iid collision laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
