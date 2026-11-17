# Scientific review

## Correctness — PASS

The proof specifies the four knots, positive mesh ratio, exact natural second-derivative conditions, discrete and continuous variation, and the supremum over all nonconstant real data. Decomposition into three jump vectors is exact and attains the operator norm. Curvature solves a positive-determinant two-by-two system; sign analysis separates the two jump types, computes every interior cubic extremum, and gives exact expressions for the two norm branches. Strict monotonicity of opposite branches and limiting values prove existence and uniqueness of the minimax mesh. The supplied rational interval checker certifies a narrow optimum bracket; separate finite-data tests corroborate but do not replace the proof.

## Originality — PASS, qualified

Beatson–Chacko (1990 report, 1992 article) is the strongest directly inspected comparator: its natural-spline study uses sup-norm operator/first-derived projector norms and pointwise errors rather than the input-discrete-variation to output-continuous-variation norm and optimal symmetric four-knot spacing. Kobza (2002) optimizes squared-derivative and coefficient norms with boundary parameters instead of minimizing the sharp data-dependent variation gain over a mesh parameter. Hall (1973) treats approximation error. The published three-knot natural-spline positivity-defect result has a different number of knots and cannot imply the four-knot competition between central and outer jumps without an additional new calculation. An earlier four-node global cubic Lagrange variation minimax result uses a single cubic polynomial rather than a natural cubic spline, while the cardinal cubic result uses a bi-infinite uniform grid; neither is the present finite natural-boundary spline operator. Indexed database and prior-ledger searches did not reveal an equivalent or stronger theorem. Limitations: broad archival indexing is incomplete, and the three-knot published full text was not accessible in the attempted route; priority should be independently checked.

## Mathematical value — PASS

The theorem resolves a concrete interpolation-design problem on the smallest symmetric natural cubic mesh with two coupled interior curvatures, where an outer and a central jump generate different instability branches. It establishes a unique nonuniform optimum and a quantitative approximately thirteen-percent improvement over the usual uniform choice; this is a structural extremal result, not an isolated numeric sample, and is useful when variation stability rather than approximation order governs knot selection. It does not optimize unrestricted meshes or other end conditions.

Self-review: passed. Independent audit: not yet performed.
