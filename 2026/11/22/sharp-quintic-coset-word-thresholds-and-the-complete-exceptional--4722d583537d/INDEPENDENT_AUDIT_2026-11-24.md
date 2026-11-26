# Independent mathematical audit

## correctness

PASS

On nonzero arguments, expansion of the three five-character projections gives the p−3 principal term. For s nonzero exponents the active polynomial has s distinct roots of multiplicities 1–4, so is not a fifth power and the order-five Weil estimate is (s−1)√p. Restoring the omitted x could affect at most 3−s nonvanishing terms. The support strata have 12, 48 and 64 terms, yielding 125N≥p−176√p−75. At 31126 the difference of squares (p−75)²−176²p is 5625 and p−176√p−75 increases thereafter. The finite run used a separate Python sieve and fifth-power-coset enumeration over all 836 eligible primes through 31126. It matched both printed exception lists (48 and 43) and all six boundary patterns. At 2311 the least generator is 3, with only (0,0,0) and (2,0,2) absent; the latter label is generator-specific. Changing generator multiplies labels by a unit modulo five and preserves the all-zero word. The C++ was inspected, not run. Independent replay and output are branches/c076698d-228a-4fbb-8203-95c042e35703/reproduce.py and census-full.txt (lines 1–9). The analytic bound covers the entire infinite tail, not sampled primes.

## originality

PASS

Credit applies to the full ordered length-three quintic coset census and sharp mixed-word threshold, not to the known all-residue obstruction at 3331, the character-sum method, or separate results for other orders. Existing accessible statements do not give the mixed-word list or imply its boundary at 2311/2341.

## value

PASS

The presence of local coset patterns is a natural arithmetic invariant, and the exact separation between the known all-residue obstruction and the last mixed obstruction answers a distinct question. The exact finite classification and boundaries are not predicted by the generic character-sum estimate or a neighbouring character order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
