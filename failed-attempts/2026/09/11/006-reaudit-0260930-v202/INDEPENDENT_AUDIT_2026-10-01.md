# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260911-006`

## Correctness — PASS

The square-with-center family calculation is internally consistent. The actual `artifacts/certify_isolation.py` was read completely: exact rational inequalities with a rigorous decimal enclosure for \(\sqrt2\) show positivity of the even block and reduce the odd block to positivity of an affine factor on \(\nuu\in[1/2,1]\). This gives transverse Morse index zero and nondegeneracy for \(\mu\in[1,2]\). The same interval also lies strictly below the independently published unique degeneracy mass, so the no-bifurcation conclusion on this interval is correct.

## Originality — FAIL

Meyer and Schmidt already analyze the same square-with-center four-equal-plus-central-mass family and identify its unique degeneracy at the exact mass \((13+11\sqrt2)/12\), with kite and trapezoid branches at that degeneracy and no nonsymmetric relative equilibria bifurcating from the square family. Since this mass is about \(2.38\), their result directly implies nondegeneracy and absence of bifurcation throughout \([1,2]\). The audited interval result is therefore a special-case corollary of stronger prior coverage.

### equivalent_formulations

Searches: square with center central configuration four equal masses central mass bifurcation; Meyer Schmidt square family degeneracy central mass

Evidence: The 1988 Meyer–Schmidt paper studies the same family and gives the exact unique degeneracy mass.

Reasoning: The audited parameterization is the standard square with four equal outer masses and a central mass, so the prior result is an equivalent formulation after normalization.

### broader_coverage

Searches: Meyer and Schmidt, Bifurcations of relative equilibria in the 4- and 5-body problem, 1988

Evidence: The paper gives the unique square-family degeneracy and the bifurcating kite/trapezoid branches.

Reasoning: A theorem locating the only degeneracy globally along this family is strictly broader than certifying positivity/no bifurcation on the subinterval \([1,2]\).

### exact_database_or_table

Searches: central-configuration square-family index/degeneracy tables

Evidence: No separate table is needed: the prior exact degeneracy formula already determines whether the audited interval contains a bifurcation.

Reasoning: The result is mechanically implied by the prior exact threshold rather than being a new database row.

### claim_vs_prior_implication

Searches: comparison of audited interval with Meyer–Schmidt threshold

Evidence: The exact prior threshold exceeds \(2\), so \([1,2]\) contains no degeneracy; the paper also states the corresponding branch behavior at the unique degeneracy.

Reasoning: The audited no-bifurcation claim follows directly as a corollary, even if the endpoint Morse-index wording is not copied verbatim.

### source_inspections
- **Bifurcations of relative equilibria in the 4- and 5-body problem** — https://doi.org/10.1017/S0143385700009433. Trigger: Same square-with-center mass family and bifurcation question. Material read: Accessible full-text passages containing the unique degeneracy mass and the square-family bifurcation statements. Method: Primary-source theorem/passage inspection. Assessment: DECISIVE COVERAGE: the unique degeneracy occurs above the audited interval, and the same paper describes the square-family branches. Evidence: The paper gives the exact mass \((13+11\sqrt2)/12\) and states the square-family bifurcation behavior.
- **Assigned isolation verifier** — artifacts/certify_isolation.py. Trigger: Correctness of the finite interval calculation. Material read: Complete source file. Method: Line-by-line exact-inequality inspection. Assessment: Confirms the interval calculation but cannot restore originality. Evidence: The odd-block determinant factor is positive on the entire \(\nuu\)-interval corresponding to \(\mu\in[1,2]\).

### checked_sources

- Meyer–Schmidt (1988), DOI 10.1017/S0143385700009433
- assigned RESULT.md and artifacts/certify_isolation.py
- Resultary semantic search

### residual_risks

- The prior paper uses relative-equilibrium language and its own normalization, but the square-plus-central-mass family and degeneracy parameter are the same mathematical object.

## Scientific value — FAIL

The interval isolation statement is mathematically correct, but as stated it is a routine subinterval consequence of a prior exact unique-degeneracy theorem for the same family. The new exact-Hessian certificate is useful reproducibility evidence, yet correctness and reproducibility alone do not make the already implied interval fact a new valuable mathematical finding.

## Limitations

- Scientific rejection is due to stronger prior coverage, not a correctness defect.
- The package's verifier is located at `artifacts/certify_isolation.py`, while RESULT/METADATA name an `output/artifacts` path.
- The audit does not reject the usefulness of the exact certificate as a regression check.

## Disposition

**FAILED — not a validated finding.**
