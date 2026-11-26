# Independent mathematical audit

## correctness

PASS

For the Euclidean projector in R^(d+1), with coordinate maximum norm measuring perturbations, differentiation in the middle region gives scalar row sum (1+||u||_1)/2. The spatial rows maximize as s/||x|| approaches 1 from below; Cauchy–Schwarz on the other d−1 entries gives the stated g_d, and g_d''<0 with opposite derivative signs at 1/2 and 1/sqrt(2). Evaluating g_d at 1/sqrt(2) proves spatial dominance for d=2,3,4 (the test margin decreases up to d=4 and is still positive there). At d=5 the stated quadratic majorant gives g_5 <= (9+4sqrt(2))/12 < 11/9 < sqrt(5)−1, and g_d(a)−sqrt(d)+1 decreases pointwise thereafter. On a segment the two cone boundaries have finitely many crossings unless the defining quadratic vanishes identically; in that case split at any change in sign of the scalar coordinate, on each piece of which the projector is identity or zero. Integration and interior row-sign perturbations give global sharpness, including the one-dimensional spatial case. Independent bisection gave 1.361178997924584, 1.463035638120580 and 1.541623172494264 for the three exceptional constants. The supplied verifier was inspected, not executed; the numerical replay is not the all-d proof.

## originality

FAIL

A distinct published Resultary record expressly states the identical Euclidean-projector/coordinate-norm problem, all sharp constants, the same optimizing equation, and the exact dimension-five switch. The tighter bracket on the same unique root is a direct endpoint sign check, not an independent finding. This decision concerns demonstrated equivalent coverage; the two path dates do not settle historical priority or how the records relate.

## value

FAIL

The amplification factor and switch of the worst output coordinate answer a natural robustness question, but the record adds no substantive claim beyond the equivalent published classification. A narrower bracket for the same optimizer and more displayed decimal digits are routine refinements, not a worthwhile surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
