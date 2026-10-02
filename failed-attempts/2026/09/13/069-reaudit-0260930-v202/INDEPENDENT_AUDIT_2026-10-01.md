# Independent mathematical audit — SCOPE-20260913-069

Audit date: 2026-10-01 (UTC) UTC

Disposition: **failed**

## Final claim assessed

For the explicitly specified shear-perturbed toral family, the fixed point \(p_2=(1/2,0,1/2)\) has a simple unit multiplier at \(t_*=(\sqrt3-1)/(4\pi)\), so the family is not Anosov at \(t_*\) and the threshold satisfies \(t_c\leq t_*\); the continued weak multiplier has derivative \(-2\pi\sqrt3\) there.

## Correctness: PASS

A fresh symbolic reconstruction gives \(\det(Df_t(p_2)-I)=s^2+2s-2\) for \(s=4\pi t\). At \(s=\sqrt3-1\) the characteristic polynomial factors as \(-(\lambda-1)(\lambda^2-4\lambda-1)\), so the unit multiplier is simple and the other multipliers are \(2\pm\sqrt5\). Implicit differentiation gives \(d\mu/ds=-\sqrt3/2\), hence \(d\mu/dt=-2\pi\sqrt3\). A periodic point with a unit-modulus multiplier is incompatible with Anosov hyperbolicity, so the stated upper bound follows exactly.

## Originality: PASS

No prior source was found for this exact matrix/shear family and parameter value. The proof uses standard periodic-point hyperbolicity, but the exact algebraic crossing is a best-of-knowledge new instance.

### Originality comparisons

**equivalent_formulations.** Equivalent formulations would give the same fixed point, unit-multiplier equation, or identical threshold bound; none was found.

Searches: Resultary semantic search for the exact toral family and neutral fixed point; web exact-expression search for the matrix and \(\sqrt3-1\) threshold

Evidence: Resultary returned the audited record as the only exact match.; The exact-expression web search returned no relevant mathematical source.

**broader_coverage.** The general theorem supplies the obstruction principle, not the exact parameter.

Searches: Anosov perturbation neutral periodic point threshold torus; standard structural-stability and periodic-point criteria

Evidence: General Anosov theory says periodic points are hyperbolic but does not compute this family-specific crossing.

**exact_database_or_table.** The result is an elementary exact calculation, not a database lookup.

Searches: Resultary exact family search

Evidence: No external table of this parameterized family was found.

**claim_vs_prior_implication.** That general implication does not determine where this specific family acquires a unit multiplier; the matrix calculation is still instance-specific.

Searches: exact matrix/shear formula search; generic Anosov bifurcation literature search

Evidence: Only the standard implication 'Anosov implies hyperbolic periodic points' applies generally.


Checked sources: Resultary semantic search; web exact-expression search; standard Anosov periodic-point criterion


Residual originality risks: Absence of an exact web hit is not novelty proof; the PASS is best-of-knowledge for the instance only.

## Scientific value: FAIL

The final claim is an elementary fixed-point eigenvalue calculation for one ad hoc matrix/shear family. It neither identifies the actual Anosov threshold nor supplies a natural extremal boundary, classification, general mechanism with reusable hypotheses, or downstream invariant. The exact parameter is selected by solving a single determinant equation, so correctness and instance-level novelty do not make the result scientifically substantial under the stated value bar.

## Limitations

Only the displayed upper bound and neutral fixed-point crossing are proved; equality with the true Anosov threshold and any mixing-rate conclusion remain unproved.
