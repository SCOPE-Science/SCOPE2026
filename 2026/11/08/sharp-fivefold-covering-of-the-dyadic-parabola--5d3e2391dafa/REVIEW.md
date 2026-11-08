# Scientific self-review

## Correctness — PASS
The proof is reconstructed from the elementary parity obstruction, a mixed-parity base at modulus four, and two top-bit operations that independently control the linear and quadratic sums. The second operation changes the square sum by exactly the highest binary bit because its two entries have opposite parity. The obstruction for four terms reduces to modulus eight. Boundary exponents \(k=1,2\) are covered separately, and the finite checker tests the complete small-modulus spectra and the lifting moves. No computational sample is used as an infinite proof.

## Originality — PASS
The archival source Tóth (2014) counts solutions of single quadratic congruences, not simultaneous prescribed first and second moments. Hickman–Wright (2018) concerns analytic restriction over modular rings. A published fourth-moment result for the same dyadic graph computes energy and sharp analytic constants, which do not imply a fivefold covering theorem. General finite-group sum-cover work addresses a different optimization problem. Targeted searches for equivalently phrased two-moment systems, fivefold dyadic parabola sums and local additivity found no covering statement. Older local quadratic-form and additive-basis literature remains a historical-priority risk; a small-group sum-cover paper was inspected only at abstract level.

## Mathematical value — PASS
The exact sharp covering order of a natural polynomial graph is classified over every dyadic ring. Five summands suffice for *every* parity-allowed prescribed pair of the first two power sums, and the sharp obstruction is structurally explained modulo eight. This resolves a local existence invariant rather than merely recomputing a table. No formula for representation counts, odd-prime extension or independent originality certification is claimed.

## Verification and limitations
`checker.py` enumerated all sumset sizes for exponents one through seven, confirming the sharp values. It also independently checked mixed-parity witnesses and the two lifts at exponents two through four. These tests are finite corroboration; the argument above proves the general theorem. The proof and scope are self-contained, but bibliographic completeness cannot be guaranteed.

Self-review: passed. Independent audit: not yet performed.
