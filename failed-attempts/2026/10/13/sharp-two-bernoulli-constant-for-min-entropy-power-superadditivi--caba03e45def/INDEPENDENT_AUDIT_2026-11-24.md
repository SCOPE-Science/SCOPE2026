# Independent mathematical audit

## correctness

PASS

Let f,g be the two mass functions. For any integer z, the convolution at z is an average of f(z-y) against g(y), so it is at most M(B_1), and symmetrically at most M(B_2). Since m→m^(-2)-1 is decreasing, the sum deficit is at least the maximum of the two individual deficits and hence their average. Equality in the average bound requires both deficits equal and the summed maximum atom equal to each individual maximum atom. If one variable is deterministic, equal deficits force the other to be deterministic. Otherwise each Bernoulli gives positive weight to 0 and 1, so equality in the convolution average forces f(z)=f(z-1)=M(B_1) at a maximizing z and symmetrically for g. Thus z=1 and both Bernoulli variables are fair. The fair sum has masses (1/4,1/2,1/4), each of the three deficits is 3, and the ratio is 1/2. The frozen modal-orientation formulas give the same contraction, and their r,s in [0,1] bounds include all degenerate and tied modes. The independent exact replay `python3 /workspace/branches/frozen_math_checks.py` checked 441 parameter pairs on mesh 1/20 and found the four fully deterministic ordered pairs and one fair pair as the only equalities on that grid. The averaging argument proves the full result.

## originality

FAIL

The sharp lower inequality is a direct and strictly weaker corollary of classical Young convolution contraction for any pair of independent integer-valued inputs, not a new two-Bernoulli resolution. Madiman–Melbourne–Roberto already give the fair-pair upper obstruction. The equality classification is exactly equality in the same weighted-average bound with two positive summands, checked directly in the correctness assessment. No separate original remainder is established. This is affirmative mathematical implication, not a failure of retrieval or a claim that the exact Bernoulli wording is reproduced verbatim in a source.

## value

FAIL

The many-summand sharp-constant gap is meaningful, but for a pair the presented coefficient is the immediate comparison of a maximum with an arithmetic mean after ordinary convolution contraction. The Bernoulli equality check needs only the support of the elementary weighted average, and the sharpness obstruction is prior. This is a routine example, not a new benchmark obstruction or progress on the many-input lower constant. No scientifically valuable distinct remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
