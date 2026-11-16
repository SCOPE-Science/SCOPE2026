# Self-review

## Correctness — PASS
The exact coefficient formula is obtained by reindexing the published two-index sum. The interpolation tent functions are piecewise quadratic, so a global composite trapezoid error of order \(O_k(m^{-2})\) follows; the integral coefficients factor into the stated universal polynomial. Quantitative Rouché, strict unit-circle nonvanishing, and reciprocal-conjugate pairing establish eventual simplicity and one inside/outside pair per boundary point. The published lower positivity bound gives the matching lower order \(m^{-1}\). `CHECK.py` passed finite tests; it is not used to infer an infinite theorem.

## Originality — PASS relative to inspected evidence
Edholm and Mathew prove the rational Hartogs numerator and its reciprocal symmetry and **already explicitly calculate gap-one and gap-two root limits**. The published gap-three record gives a stronger constant for that special gap. Deng and Fu prove nonvanishing on the unit circle and exactly \(k\) interior roots for all gaps. They do not state the fixed-\(k\ge4\) limiting factorization or sharp-order pointwise matching, as checked in the accessed full HTML sections. The new claim adds the universal coefficient limit and quantitative geometry and excludes previously handled small gaps. Residual risk: undetected equivalent results in older quotient-domain or spline literature; publication priority has no independent verification.

## Mathematical value — PASS
The new theorem describes the geometry of diagonal Bergman-kernel zeros when rational Hartogs exponents tend to the zero-free classical threshold. It distinguishes one isolated interior scalar limit from a regular boundary root cloud, gives sharp order of approach, and proves eventual simplicity. This geometric information is not implied by existing global zero counts.

## Scope and limitations
Only fixed \(k\ge4\) with coprime \(m,k\) and sufficiently large \(m\) is covered. The rate constants are not optimized, and no directional limiting constants or results for growing gaps and general off-diagonal zeros are asserted.

Self-review: passed. Independent audit: not yet performed.
