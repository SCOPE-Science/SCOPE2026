# Independent mathematical audit

## correctness

PASS

A tree resistance is a path sum, so the diameter is the sum of the two largest arm resistances R_i. At fixed R_i the least arm cost is s_i²/R_i, with unique equality at w_e=s_i/(R_i√p_e). For a fixed diameter limit D and a dominant index j, all other R_i are at most D−R_j, so the cost is at least s_j²/R_j+U/(D−R_j); its unique minimum gives the stated dominant formula and is feasible. For the balanced case put q_i=s_i²/C. Since q_i≤1/2, q is a convex combination of vectors (e_i+e_k)/2 (the vertices of the box slice 0≤q_i≤1/2, Σq_i=1). Thus Σq_iR_i≤D/2; Cauchy–Schwarz gives Σs_i²/R_i≥2C/D with equality only for equal R_i. Both minima saturate the budget, agree at the boundary, and give unique conductances. With two unequal arms the dominant formula becomes the ordinary path optimum (s_1+s_2)²/B. The finite independent replay checked edge reconstruction, competitors, and threshold and two-arm examples; the proof, not the replay, establishes the quantifiers.

## originality

FAIL

Demonstrably implied by earlier weighted-star results, not merely a similar threshold. For each arm use the single-spoke conductance g_i=1/R_i at effective price c_i=s_i². The attainable optimal budget/diameter pairs coincide in both directions, and the unique armwise Cauchy–Schwarz equality condition recovers all individual-edge conductances. This imports the whole threshold, both optimal values and uniqueness from the earlier arbitrary-price, arbitrary-budget star classification.

## value

FAIL

The explicit conductances are useful as a design recipe, but as a standalone claim this is the known weighted-star classification transported by ordinary series reduction and the equality case of Cauchy–Schwarz. The edge-level expansion and equal-price length statement leave no distinct structural result or nonroutine remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
