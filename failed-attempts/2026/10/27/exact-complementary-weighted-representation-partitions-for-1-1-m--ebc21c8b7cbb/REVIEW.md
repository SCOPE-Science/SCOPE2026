# Independent mathematical audit

## correctness

PASS

The mathematical finding is true. Summing over residues forces size h=m/2, and at nonzero characters the complement negates the indicator transform. At even frequencies the h-multiplied frequency is zero; at odd frequencies it is h. Hence either the parity coefficient vanishes or all odd coefficients vanish, the latter exactly equivalent to half-turn invariance. The first alternative and the half-turn pairing each force h even. For the labeled intersection, the half-turn pairs are parity homogeneous when h is even, and parity balance requires choosing m/8 pairs of each parity. For Burnside, a translation with gcd(s,m)=g fixes precisely the subsets lifted from residues modulo g; a size-h lift requires g even, and then parity balance requires g divisible by 4. Jointly imposing the half-turn replaces g by gcd(s,h), with twice the totient multiplicity. This recovers all three sums, including the identity and half-turn shifts and the small modulus edge cases. RESULT.md line 50 has a false redundant aside about even orbit lengths (e.g., s=2 modulo 8 has orbit length 4); the direct gcd reasoning there proves the claim without it. The finite evidence in VERIFICATION.md is recorded corroboration only; verify.py was inspected, not executed.

## originality

FAIL

The complete classification is a direct instance of Qu's stronger cyclotomic criterion, and its existence assertion is covered by his explicit existence theorem. No literal copy of the numerical formulas was found, but the labeled sum is immediate binomial inclusion–exclusion, and the translation sum is the ordinary fixed-content cyclic orbit count on the two already-determined families and their intersection. The record does not establish a distinct mathematical contribution beyond those deductions.

## value

FAIL

The representation problem and translation action are natural, but the proposed invariant adds no distinct structural step to Qu's characterization in this specialization: the orbits are counted by reducing to fixed-content choices on cyclic quotients with a parity filter. The orbit count alone, although explicit, is a routine Burnside deduction here and does not support a stand-alone repaired claim under the scientific standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
