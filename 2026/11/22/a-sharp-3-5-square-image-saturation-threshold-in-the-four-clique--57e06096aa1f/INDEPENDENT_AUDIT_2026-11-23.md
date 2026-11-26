# Independent mathematical audit

## correctness

PASS

The frozen proof correctly factors the square map through J_4-I_4, whose determinant is -3, and uses coordinatewise square counts when invertible. In characteristic three its image is the sum-zero hyperplane, and the affine fiber s_i=t-y_i gives the root-count product. The uniform character bound in the frozen proof works at q>=729: exclusion costs at most 28+4, and the sum of Weil coefficients is at most 17. The supplied small-field algorithm and output were inspected, not executed. Separate enumeration by generating all translated subsets of the inclusive reflected square set reproduced the deficits at 3, 9, 27 and 81. At q=243 an analytic check suffices: for four distinct entries each pair sum is exactly -1 (substitute (t-a)/(t-b) over t!=b); four triples and the quartic cost at most 11√q, giving the positive bound q-38-11√q for q>=243; smaller supports extend to a four-set. The revised package instead proves the exact F27 statement. Here X^3-X+1 is an irreducible cubic by a root test; the new script constructs all translated d-subsets of the inclusive reflected square set for d=3,4 and was executed via python3 check_deficit_27.py in the revised package. It reproduced all 2,925 triples, 16,146 covered quartets, and 1,404 missing quartets, of which 52 have sum zero. Every four-support has exactly one sum-zero translate since 4=1 in the field; smaller supports extend to covered triples. The ordered deficit is 24*52, and subtracting it from 27^3 gives 18,435. This is a finite exact classification, not a fiber histogram or a field-size claim.

## originality

PASS

For the frozen record, the claimed sharp-threshold emphasis overlaps substantially with Paley common-neighbor results: strict existence at 243 is already implied by both a compiled domination table and the rank-five Paley-tournament theorem, and the dated-matching Paley-81 orbit classification determines the 81 obstruction and even its deficit by checking three representatives. Same-date corpus overlap does not establish who was first. This is not a pass for the frozen threshold novelty. The delivered replacement centers the exact deficit over F27 and drops the other field sizes and saturation threshold as contributions. Under the sign/zero conventions of the actual sources, no inspected earlier statement supplies the F27 all-positive closed-support count. The known triple coverage is credited, not counted as a separate new theorem.

## value

PASS

The repaired exact F27 invariant is worthwhile on its own: in this naturally occurring resonant field every three-point support is covered but coverage fails at four, so the known linear rank and the known three-point property substantially overstate the nonlinear image. An exact count is useful for distinguishing a property failure from its prevalence: the 52 uncovered supports modulo common translation and their ordered-target weight determine the entire image size. The repair does not rely for value on a known saturation statement, a change of vocabulary, or merely replaying a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
