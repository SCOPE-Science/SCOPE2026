# Independent mathematical audit

## correctness

FAIL

The numerical Finding reproduces from the primary data, but the frozen claim that the supplied certificate is in source order is false. I parsed all 620 aligned entries from Xarles's public ListCurvesGenus4p2.txt, checked the independent mirror gave identical parsed rows, and classified the primary rows directly. The eight bin counts are indeed 99/230/112/1/68/29/60/21 and the gonality totals are 264/526/253/1. The packed-table comparison localized a difference to line 26. At zero-based index 514, whose full counts are (5,5,5,21), the primary projection is 551000 but the frozen row says 551001. At index 515, whose counts are (5,5,8,17), the primary projection is 551001 but the frozen row says 551000. This transposition is invisible to the aggregate check, but contradicts the asserted source-indexed provenance and would fail the optional ordered comparison. Separately, the text's 'minus a moving residual point' is incorrect for a degree-three pencil: by Riemann–Roch a trigonal fibre spans a line, and the quadric contains that line because its intersection has length at least three. This supplies the ruling argument; the cone vertex is avoided by smoothness. For a nonsplit curve the Riemann–Roch complement of a degree-two effective divisor gives a degree-four pencil, which has no removable fixed part because the gonality is at least four, and the absence of such a divisor forces gonality five by the finite-field bound. Independent field enumeration and affine-chart Jacobian checks confirmed the explicit witness equations and point counts 1/5/10/17; the hyperelliptic infinity chart u=1/x, w=u⁵y is smooth with its single point above u=0. Neither the table's numerical counts nor the witness is shown false by the certificate defect.

## originality

FAIL

The incidence table was not located as an earlier printed table with the same labels. Nevertheless it is an evaluated coarsening mechanically covered by the exact published isogeny-grouped census and the already published gonality criteria: every relevant row field is given, and the target is obtained by a fixed Boolean relabelling and histogram, without any new evaluation of gonalities from equations or further mathematical classification. The existence of a triple-gonality class is itself already implied by Xarles's examples with a hyperelliptic representative and all three quadric types (the example with rational points ensures the nonsplit gonality is four). The supplied explicit triple is not a new existence conclusion.

## value

FAIL

Failure of gonality to be an isogeny invariant is a well-motivated question, and an incidence histogram may be a convenient reference. Here the exact finite refinement is a straightforward coarsening of a complete stronger table with already known class-by-class criteria. Its new numbers supply no further mathematical classification beyond evaluating that histogram, and the concrete triple recertifies a phenomenon already forced by known examples. The narrow-exact-invariant standard excludes this mechanical table recomputation. Fixing the two ordered certificate entries or the explanatory error would not provide a surviving distinct valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
