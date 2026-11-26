# Independent mathematical audit

## correctness

PASS

Substitution in F(n) gives G_0(t)=t(3t−1)^2(3t−2)/4 and G_2(t)=t(3t+2)(3t+1)^2/4, reducing as polynomials to unit-slope t and −t. Their divided differences are units, so each contributes exactly one input per target modulo every 3^k. For n=3t+1, G_1=−3φ(t)^2/4 with φ=t√(1−9t²) using the square root congruent to 1 mod 3. The difference of two such roots is in 9(t−s)Z_3 by the difference of squares and unit sum, so φ is an isometry and permutes every finite level. For 3|y, the lower-depth square equation has three lifts per root (also k=1); otherwise none. For minimality, the mod-three sequence has a period of nine but not three, so an arbitrary period is divisible by nine (periods of the cyclic word are a subgroup). Evaluating at that period T gives v_3(F(T))=v_3(T)−1. The square-root classification by unit and even valuation gives the histogram, including the single zero target, and the critical image measure is (3/8)/3=1/8. The regular branches give total valuation density 4/3^(j+2); the critical branch gives 2/3^(r+2) at j=2r+1, with natural density by periodic cylinders. Fresh direct evaluation through k=8 matched all target counts and proper-divisor obstructions; replay /workspace/branches/f1125559-1aa8-4894-9018-c28d623d7353/record3_direct_check.py and record3_direct_check.out in the same directory. Those checks are finite; the isometry proof and least-period obstruction cover all levels. No uploaded code was executed.

## originality

PASS

The supported distinct claim is the all-target least-period fiber law for the ordinary third Narayana column and its associated singular image and index-density law. Earlier Narayana divisibility and integer-square or perfect-power statements do not establish it. Fourth-binomial/pentatope fibers have the same square-root spectrum after an affine relabeling of targets, but on a different polynomial and with different actual target values. The analogous spectrum alone is not originality evidence. No independently matching targetwise law was established in the checked sources.

## value

PASS

A complete target-by-target count and sharp index period for a natural fixed column distinguish genuine singular concentration from prime divisibility or integer squares. The globally bijective coordinate yields the precise critical support and nonuniformity at every depth. The value is the evaluated law for this column, not the general use of Hensel lifting or an isolated valuation at an individual input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
