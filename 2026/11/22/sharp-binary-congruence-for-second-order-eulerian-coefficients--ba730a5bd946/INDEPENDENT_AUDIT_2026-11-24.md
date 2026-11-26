# Independent mathematical audit

## correctness

PASS

Use internal ascents, excluding sentinels. Inserting nn in one of the ascent gaps or at the beginning leaves the ascent count unchanged and all other gaps add one; the empty word initializes column zero. For k=2j>0 the two old coefficients share divisor 2^j and the multipliers are odd. For k=2j+1 the old same-column term has divisor 2^(j+1) and an even multiplier, while the incoming column has divisor 2^j and multiplier 2(n-j-1). This proves integrality and yields the printed parity recurrences, including the zero boundary. An independent induction on the proposed binomial parity works directly: in even columns the two older binomials combine by Pascal with upper index n-1-j, and in odd columns (u-2j)binom(u,2j)=(2j+1)binom(u,2j+1) with u=n-j-1. The first 1 is at n=k+ceil(k/2); summing the shifted binomial coefficients gives the stated formal series (also for k=0). Lucas yields the bit test for fixed k>=1; among residues modulo 2^r, r the bit length of k, exactly 2^(r-s_2(k)) qualify. Any eventual period is a period of the residue pattern, and the least must divide 2^r; a half-period flips the highest required bit at u=k, so the least is 2^r. Independent literal Stirling-word enumeration by open and closed pairs through n=7 in python3 /workspace/review_evidence/recompute_arithmetic.py confirmed the normalization and parity. This finite reproduction is diagnostic, not the universal proof.

## originality

PASS

Best of current knowledge: the recurrence, raw triangle, and its one-column aliases are established. The exact bit-level result after division by 2^ceil(k/2), and its uniform sharpness classification, are not stated by the inspected sources. Lucas and the period/density deductions are standard once the nontrivial normalized parity is known.

## value

PASS

For a standard triangle the result identifies the exact minimum column valuation and all rows attaining it by a low-cost binary test, with exact onset, period and density. This is a natural unbounded arithmetic classification, not a small table recomputation or a reindexing of standard Stirling numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
