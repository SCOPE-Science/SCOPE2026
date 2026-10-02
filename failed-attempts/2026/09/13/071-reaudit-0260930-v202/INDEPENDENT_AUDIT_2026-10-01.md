# Independent mathematical audit — SCOPE-20260913-071

Audit date: 2026-10-01 (UTC) UTC

Disposition: **failed**

## Final claim assessed

For the De Laet \(t=1\) quotient, the reduced \(V_3\) scheme is six smooth rational curves with incidence graph \(K_{3,3}\) minus a perfect matching, and the stated intersection point is singular with tangent dimension two.

## Correctness: PASS

The multilinearized quadratic relations force the triple locus to the six components \(C_i=L_i\times\{q_i\}\times L_i\) and \(D_i=\{q_i\}\times L_i\times\{q_i\}\). Restricting the two cubic relations gives one smooth bidegree-\((1,1)\) equation on each \(C_i\) and vanishes identically on each \(D_i\), yielding six rational curves. Direct component incidence gives \(E_i\cap D_j\neq\varnothing\) exactly when \(i\neq j\). At the stated point, the independent Jacobian rows have rank four in six affine variables, so the tangent dimension is two while the local component dimension is one. The inspected zero-dependency verifier encodes these same relation-level checks.

## Originality: FAIL

De Laet's primary Theorem 5.6 already classifies the point modules of the same \(T_t\) family for nonzero finite \(t\) by six lines and gives the shift dynamics by analyzing exactly the same consecutive triples and cubic relations. At \(t=1\), the audited \(V_3\) six-curve picture and its intersections are a finite graph-of-shift unpacking of that published classification rather than an implication-independent theorem.

### Originality comparisons

**equivalent_formulations.** The finite \(V_3\) presentation is the first three-coordinate graph of the already classified point sequences; its six components are therefore an equivalent finite manifestation of the published six-line parameter space.

Searches: Resultary: Heisenberg quotient degenerate Sklyanin truncated point scheme V3 T1 connected six rational curves; De Laet arXiv:1510.04024 full text, Section 5.2

Evidence: Resultary returned the audited record as the exact SCOPE match.; De Laet Theorem 5.6 states that point modules of \(T_t\), \(t\neq0,\infty\), are parametrized by six lines and describes the shift through the same triple relations.

**broader_coverage.** A published all-\(t\) classification dominates the fixed-\(t\), low-truncation component description.

Searches: De Laet Theorem 5.6 and proof; Walton degenerate Sklyanin point-scheme literature

Evidence: Theorem 5.6 covers every nonzero finite \(t\), hence strictly broader parameter coverage than the fixed \(t=1\) record.; Its proof explicitly treats subtriples, intersection points and the cubic-relation constraint governing the shift.

**exact_database_or_table.** Database comparison is inapplicable because the claimed object is an algebraic scheme; the exact prior coverage is theorem-level.

Searches: De Laet Section 5.2 relation-level classification; Resultary exact record search

Evidence: The relevant prior is a theorem rather than a numerical table.

**claim_vs_prior_implication.** Specializing those published formulas to \(t=1\) and taking the finite graph yields the same component/intersection mechanism. The Jacobian singularity is a routine local consequence at an intersection of two smooth branches and does not restore originality of the final combined claim.

Searches: https://arxiv.org/abs/1510.04024 full text around Theorem 5.6

Evidence: The proof states the allowed consecutive triples, including the relation \(\delta\alpha=-t\gamma\beta\), and concludes that the shift squared preserves each line and fixes intersection points.

### Primary source inspections

- **Quotients of degenerate Sklyanin algebras** (https://arxiv.org/abs/1510.04024): COVERING at broader parameter level. Material read: full ar5iv Section 5.2, especially Theorem 5.6 and proof lines describing six lines, subtriples, intersection points and shift dynamics. Evidence: Theorem 5.6 classifies point modules of \(T_t\) for all nonzero finite \(t\) by six lines and derives the shift from the same cubic relation analysis.


Checked sources: https://arxiv.org/abs/1510.04024; https://arxiv.org/abs/0812.0609; Resultary semantic search


Residual originality risks: The published theorem is phrased for infinite point modules rather than with the exact symbol \(V_3\); the coverage judgment rests on the explicit consecutive-triple/shift formulas in its proof, not title matching.

## Scientific value: FAIL

Once De Laet's broader point-module classification and shift formulas are taken into account, the fixed \(t=1\), \(d=3\) connectedness and singular-intersection certificate are a low-level unpacking of known geometry rather than a motivated new boundary or classification. The local Jacobian rank calculation is correct but does not supply enough independent mathematical content to meet the value bar.

## Limitations

The relation calculation is correct for the reduced \(d=3\), \(t=1\) truncated scheme, but the scientific claim is rejected because broader prior point-module/shift theory covers the same mechanism.
