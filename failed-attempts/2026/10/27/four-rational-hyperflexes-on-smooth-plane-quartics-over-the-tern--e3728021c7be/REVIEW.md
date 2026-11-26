# Independent mathematical audit

## correctness

PASS

In flag coordinates (u,v,w), the four vanishing coefficients in F(u,v,0) and the nonzero u³w coefficient exactly express order-four tangency at a smooth point when F has no line component, which is automatic for a geometrically smooth projective quartic. Allowing a zero v⁴ coefficient before geometric screening is harmless. The independent replay /tmp/opencode/quartic_review.py fixes u³w=1 in the flag basis, enumerates the other ten free ternary coordinates for each of 52 flags, then transforms back and normalizes. It reproduced every positive flag count in the frozen table, with 9,997 forms having ≥5 flags and none rationally nonsingular. Of the 87,750 four-flag forms, 52,884 have no rational Jacobian zero. Euler's identity applies because 4=1 in F3. Generator closure on that candidate set gives 18 orbits; chart-wise Jacobian Gröbner bases leave exactly three geometrically smooth orbits, matching the literal F_A,F_B,F_C in sizes 1872,234,234. Thus stabilizer orders are 5616 divided by the respective sizes, and 2,340 equations attain equality. Independent substitution at rational points gave point counts 5,4,4 and hyperflex sets on Y=0 for A, on X=Y for C, and with all triple determinants nonzero for B. The no-rational-singularity test alone was used only to discard candidates, not to certify geometric smoothness. Frozen programs were inspected but not executed.

## originality

FAIL

The distinct October 18 Resultary record 1af4ae8246e7 gives the full joint spectrum, including maximum hyperflex count four and exactly 2,340 equations in three orbits at that count. Its complete orbit table gives the very same representatives (matching numerical polynomial codes), orbit sizes and rational-point counts. Rational hyperflex line count is exactly rational hyperflex point count here: Frobenius fixes the unique geometric contact point of a rational line meeting the curve in 4P, and the tangent to a rational smooth point is rational. A second distinct October 18 record states the same hyperflex marginal for rational points explicitly. This is demonstrated exact coverage, not a speculative priority concern or an inference from matching titles.

## value

FAIL

The invariant is natural, but the exact extremal cut-off and equality representatives are already present in a strictly richer same-field census. Re-enumeration corroborates those tables; it does not produce a distinct scientific result. The extra incidence labels follow from elementary tests on the already catalogued representatives and do not support a new general bound, classification or nonmechanical residual claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
