# Independent mathematical audit

## correctness

FAIL

The exact RK4 interval and q=13 switch check out, but the Finding (RESULT.md line 29) additionally asserts strict improvement over forward Euler for every allowed d,q. At q=2 the graph has degree d, Θ=2d and the proved sharp horizon H_{d,2}=H3=1/d equals the forward-Euler horizon. For example H(3,2) has both endpoints 1/3. This falsifies the stated universal strict inequality; equality occurs for all q=2 and the strict comparison holds for q≥3. For the main interval I rebuilt the off-diagonal coefficients independently from signed moments of the commuting clique spectral projectors. The distance-two coefficients after homogenization on [0,H3] are positive; for distance one all but the last are positive and its sign at d=3 is the sign of 64−5q, with a positive-coefficient certificate when d≥4. Descartes on the transformed polynomial gives the unique exceptional zero, and the distance-three entry is strictly negative for every h>H3. The diagonal is positive by the scalar fourth-order Taylor remainder and spectral resolution; distances above four are structural zeros, not active boundary zeros. For the strict Euler comparison in the exceptional q≥13 case, the adjacency coefficient of A is positive at Euler's horizon and the other coefficients are nonnegative (the A³ coefficient is zero there, not strictly positive as claimed in the proof). The scaled limiting cubic and the example roots agree. Replay exact shell and sign checks with python /workspace/branches/math_checks.py 1; the frozen checker and notes were inspected, not run. This is a completed-step result, not stage positivity.

## originality

FAIL

The substantive 12-to-13 transition and the full endpoint for d≥3,q≥3 are exactly covered in a distinct Resultary Hamming diffusion record. The omitted binary slice is a direct specialization of the separately indexed exact bipartite-network theorem and requires only elementary walk counts. The example and asymptotic root are evaluations of the same exact Hamming polynomial. Catalogue dates do not show historical priority: both covering records have later path dates than the frozen record. The verdict is about demonstrable equivalent and stronger coverage in the audited corpus, not who first obtained the result.

## value

FAIL

An exact stochastic timestep and active entry obstruction on a categorical product graph are worthwhile. The substantial switch, complete interval and no-reentry fact are already under exact equivalent or stronger coverage, however. After correcting the false strict Euler comparison at q=2, the additional comparison and large-q limit are short consequences of those same laws, not an independently useful new sharp result. No scientifically distinct repaired claim remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
