# Independent mathematical audit

## correctness

PASS

The heat observation rows have modal factors (1,1) and (q,q^4); with two rows and independent noise, det I=(det M)^2/σ^4. Taking absolute cosines s,t gives the exact global reduction to (1-s²)(1-t²)(s+kt)², with equality for opposite signs at nonzero s,t. The unit edges and origin cannot maximize; along each remaining zero edge the inward first derivative is positive. Strict concavity of the log in the interior gives unique maximizing magnitudes. The stationarity identities 2s²+kst=1 and st+2kt²=k imply s²=(1-2w)/(2-3w), k²=w/[(1-2w)(2-3w)] with w=t². The increasing branch w∈(0,1/3) gives the stated quadratic root and exactly two reflected designs. Since s²-w=(1-w)(1-3w)/(2-3w)>0, the canonical pair has sum below one and the reflected pair has sum above one. Substitution yields the stated determinant. The sign of dw/dk gives both migration directions, w=2k²-14k⁴+O(k⁶) gives the large-time expansions, and dw/dk=1/6 at k=1 gives the equal short-time site velocities. At k=0 the reduced objective is 1/4 at the limit optimizer and 4/27 at the static equal-time pair, giving ratio 27/16. An independent bounded comparison at k=0.8, 0.2 and 0.001 evaluated the physical rows on the grid (i/160,j/160), 0≤i,j≤160, using q=k^(1/3); no grid value exceeded the formula and reflection agreed to floating-point precision. At q=10^(-4) the independently evaluated ratio was 1.6874999999966254. The frozen checker was inspected, not executed; the grid is only corroboration.

## originality

PASS

The supported contribution is the specific globally sharp two-time likelihood design: the closed parameter curve, exhaustion of equality cases, strict symmetry breaking, and time-dependent determinant and placement laws. Neither general D-optimality nor the standard two-by-two information identity is new. The closest inspected polynomial-design, heat-sampling and PDE-design results differ in their design spaces or objectives and do not imply the solved pair.

## value

PASS

One observation at each fixed time underlies a natural minimal identifiable heat-reconstruction design. The precise optimizer tests and rejects the natural reflected-site constraint for every finite separation, gives the migration of both sites, and quantifies the asymptotic information cost of reusing the equal-time design. The value is the complete optimizer and quantitative comparison, not routine computation of the Fisher determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
