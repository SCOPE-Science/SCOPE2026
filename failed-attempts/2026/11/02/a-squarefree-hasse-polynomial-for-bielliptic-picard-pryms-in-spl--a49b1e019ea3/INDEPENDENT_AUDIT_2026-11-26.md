# Independent mathematical audit

## correctness

PASS

In the regular differential basis (dx/y, dx/y², x dx/y²), parity and the two cubic characters make the Cartier matrix diagonal for p=6m+1. The first two basis vectors are anti-invariant and the third is invariant. Expanding around z=−a/2 and using Lucas gives D^m dividing B and F, where D=a²−4b; degree and specialization at b=0 give F. B is also divisible by b^m, coprime to D^m. Substitution of B=b^mD^m Q into its coefficient ODE makes the Q' multiplier (4m−1)a and the Q multiplier −3m² mod p, exactly the equation for H. The leading indicial factor −(d−m)(d−3m) is nonzero for degrees d<m, proving quotient uniqueness and the stated leading-coefficient ratio. At b=1 the boundary evaluations are nonzero. A repeated root elsewhere of order r would give leading ODE term (4−a₀²)r(r−1) times a nonzero coefficient, impossible for 2≤r≤m<p. The elliptic Cartier scalar is a unit on the smooth locus. The degree-four isogeny separates the p-divisible groups, so simultaneous vanishing of the two Prym entries gives a=2 (superspecial) and simultaneous nonvanishing gives ordinary. Normalization leaves a sign action; the root at zero is present exactly for odd m. Independent exact polynomial-multiplication and gcd checks at p=7,13,19,37,97 replay with python3 /workspace/review-evidence/reproduce.py 3 (SymPy). These are finite corroboration; the supplied checker was inspected, not executed.

## originality

FAIL

The normalized polynomial, its m simple smooth roots, both exact Cartier coefficient identities, and the Jacobian strata are already present in Resultary 6da8625d9e59 (also compare 3204a085956d and 1c2ce1c55b2f). Weighted scaling restores arbitrary nonzero b; the prime-to-p Prym–elliptic decomposition and the sign quotient recover the Prym statement and exact marked count without a new mathematical result. This failure is based on direct equivalent coverage and explicit reductions, not on inaccessible primary literature or dates alone.

## value

FAIL

The explicit reduced divisor, its factorization and the split Prym strata are worthwhile questions, but the exact core is already solved in available records. Remaining differences are transporting the normalized formulas by weighted scaling, using the known prime-to-p factorization, and counting pairs under the established sign action. These routine deductions do not leave a distinct valuable result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
