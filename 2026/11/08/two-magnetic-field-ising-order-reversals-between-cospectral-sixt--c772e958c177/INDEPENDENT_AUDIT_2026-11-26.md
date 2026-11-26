# Independent mathematical audit

## correctness

PASS

Independent replay /workspace/branches/replay_1.py, run with python3, directly summed crossing indicators over the 48 unordered edges of each graph on each of 65,536 binary profiles; it imports no source code and uses neither the supplied row-mask nor edge-increment recurrence. It checked all subset-size totals, every coefficient difference (35 nonzero, all others zero), and the degree and common-neighbor conditions. The latter give A²=4I+2J_16 and the shared spectrum 6,2^(6),−2^(9); the unequal counts of K4 subgraphs (8 vs. 0) certify nonisomorphism. After dividing the parenthetical factor by z^4 the sign is that of g(s)=s²−4q⁶s+6q⁸−2 on s≥2. For q≠1, g(2)=2(q²−1)²(3q⁴+2q²+1)>0; for q<1 the vertex lies left of 2, and for q>1 it lies right of 2 with negative value −2(q⁴−1)²(2q⁴+1). This gives exactly the stated strict intervals; q=1 makes the full difference zero. In the Ising normalization the common prefactor is exp(−48βJ+16βh), q=exp(2βJ), z=exp(−2βh); s=2cosh(4βh) sweeps [2,∞) strictly monotonically for h≥0. Rationalizing the smaller root gives s_−∼(3/2)q², while s_+∼4q⁶, proving the two limits J and 3J at fixed J>0. Spin reversal gives the negative-field comparisons. The uploaded finite certificate was inspected, not executed; the independent replay covers only these two labeled finite graphs.

## originality

PASS

The general bivariate cut-polynomial representation, the exact zero-field specialization, and the same pair's zero-temperature field behavior are known. Neither the strongest matching exact records nor the inspected primary formulas give the complete joint difference in cut size and occupancy or its two distinct positive-temperature reversals. The supported distinct claim is that joint identity and finite-temperature sign diagram, not an independent priority claim for zero field or zero temperature.

## value

PASS

The rook–Shrikhande pair is a natural fixed spectral indistinguishability test, and the field-resolved Ising partition function is motivated independently of the enumeration. The exact factorization shows that turning on field can reverse, then restore, the strict all-coupling zero-field ordering at every positive temperature. That precise behavior is not a routine corollary of nonisomorphism, graph spectra, or the pair's ground-state thresholds. The crossing is a finite-system comparison, not a claim of a thermodynamic singularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
