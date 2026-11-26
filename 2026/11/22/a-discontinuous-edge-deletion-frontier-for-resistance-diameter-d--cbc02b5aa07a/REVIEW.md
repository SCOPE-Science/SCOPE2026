# Independent mathematical audit

## correctness

PASS

The endpoint benchmark holds with or without a positive ordinary path: the 0–m conductance is x+1/H with H=Σ1/a_i, or just x if the path is broken. It is at most x+Σa_i/m² by Cauchy–Schwarz. At c≥m² the bound is attained by the uniform open path; for c>m² endpoint equality forces x=0 and uniform saturated a_i. At c=m² a missing ordinary edge could tie the endpoint bound only if all ordinary conductances were zero, which disconnects the graph for m≥2. Otherwise equality forces uniform y. Independently, the grounded path Laplacian with ordinary weights y has inverse entries min(i,j)/y, and the closing edge adds x e_m e_m^T. The rank-one inverse formula gives R_k=k/y - x(k/y)^2/(1+xm/y); comparison to R_m gives (m-k)(kx/y-1)≤0. This yields exactly x∈[0,B/(m(2m-1))]. For c<m² the uniform open path perturbed by small x lowers R_m while all other pairs retain a strict gap, so no open path can be optimal. Connected support gives continuous pair resistances by a grounded inverse; a cut whose summed conductance tends to zero gives divergent cross-cut resistance by the unit-voltage energy bound. This proves the needed lower semicontinuity and existence. Normalize all saturated optimizers to the critical simplex. For ε=m²-c the rescaled objective there is (1-εx/B)Δ. Comparing the upper endpoint to the constant lower bound m²/B forces normalized x≥x_* and Δ→m²/B. Compactness and the critical classification then force every normalized limit to be the same upper endpoint; the rescaling tends to one. As an exact check at m=3,B=1, the critical endpoint has R_1=6, R_2=R_3=9; at c=8, x=1/15 and y=7/45 give Δ=135/16<9. Read the frozen result, audit, review, verification note, metadata, slogan and rational arc verifier without executing it. The proof and grounded inverse above give the all-parameter replay, not the packaged finite count. Below threshold this checks retention and the limit, not a closed optimizer formula or uniqueness.

## originality

PASS

The generic maximization over pair resistances is known as an objective, and close results optimize other graph families or optimize different functionals on exactly this cycle. The complete minimax critical segment and universal one-sided selection survive the statement comparisons. Priority is qualified by access and search limits.

## value

PASS

Worst-pair resistance is a natural robust design objective. The useful part is not just the simple sufficient price bound; it is the complete degenerate segment and proof that every sequence of optimal designs approaching from below selects its positive endpoint. That distinction matters when using a critical-cost optimum as a limit of perturbations and is not provided by a finite solver run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
