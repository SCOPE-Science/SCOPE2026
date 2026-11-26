# Independent mathematical audit

## correctness

PASS

For uniform one-line permutations conditioned on an ordinary fixed point, deleting and standardizing that entry leaves the other upper records unchanged. It adds one record precisely when the remaining prefix consists of the smallest i−1 labels, in which case the prefix and suffix record counts add and their orders are independent. This yields the conditional PGF. Adjacent subtraction gives (z−1)(n−2i)P_{i−1}P_{n−i−1}/(n−1)!; telescoping gives all the tail gaps with the stated sign, and reflection and central equality include n=2. Summing the gaps gives W1. The zero-extended product coefficients are unimodal by real-rootedness and Newton's inequalities, so the variation of their first difference is twice their maximum. Differentiation at one gives the moments and the four positive sites for n≥5. A separately authored exact replay (branches/2b412c8e-80b8-44e8-87eb-fd6b59489e63/replay.py) checked 313 assertions across 46,232 permutations of sizes 2–8; the finite check supports rather than replaces the proof. Frozen checker inspected, not executed.

## originality

FAIL

The preceding 2026/10/26 local pinning record gives the same ordinary-fixed-position conditional PGF, symmetry, individual moments/covariances and aggregate covariance. The central new-looking stochastic claim is an immediate rising-factorial subtraction and coefficient telescope from that PGF; the two exact distances are its mechanical consequences via standard one-dimensional transport and unimodal first differences. The separate notation and explicit distance values do not supply a distinct finding under the implication check. The original mathematics is not false.

## value

FAIL

The positional comparison is natural and the formulas are useful expositions of the known family. As a distinct contribution, however, the proposed remainder simply unfolds the known PGF with a coefficient telescope, standard W1 and standard unimodal variation. The record supplies no independent quantitative problem, structural extension or further use that makes these mechanical consequences a substantive surviving finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
