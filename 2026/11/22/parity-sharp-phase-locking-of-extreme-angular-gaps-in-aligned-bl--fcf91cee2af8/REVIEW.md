# Independent mathematical audit

## correctness

PASS

For the prescribed normalization each factor equals 1 at z=1 and has Poisson-kernel angular derivative, so the lift F is odd and increases by 2πN per turn, with F(π)=Nπ. The summed speed is strictly decreasing on (0,π) as soon as a zero is positive. Thus the inverse speed is even, periodic and strictly increasing with circular distance from 0 up to Nπ. At c±π, 0<c<Nπ, the plus endpoint is farther from 0 even on the wrapped branch (compare 2Nπ−c−π with c−π); hence J′(c)>0. The interval centers form the coset φ+π modulo 2π in the phase circle. The least distance to 0 is π−d(φ,0); the greatest distance is Nπ minus the least distance to Nπ, giving (N−1)π+d(φ,Nπ). Strict monotonicity proves both unique optima and the parity rule; substitution gives the two gap sizes and Taylor expansion at the interior optimizing radii gives the positive cusp constants. This covers wraparound, repeated roots and N=2, and explains the all-zero exception. In the prediction example, reversed polynomials reduce optimality to matching moments through N−1 for evaluation at a. Orthogonality of the monic node polynomial to z,…,z^(N−1) under Poisson measure at a gives Q=z^(N−1)(z−a)−η(1−az), and its Lagrange interpolation weights at a simplify to the stated masses. An independently written inverse-phase checker evaluates the Blaschke product at the computed roots, checks both gap profiles in 390 list/phase cases, and checks both cusp sides for five lists including repeated positive zeros. Replay: python3 /workspace/reproductions/frozen_math_checks.py 2; output /workspace/reproductions/record-2.txt. The theorem is for co-radial zeros in the stated normalization, not arbitrary or signed-real arrays.

## originality

PASS

The supported distinct claim is the complete finite-degree ordering of the smallest and largest successive angular gaps with target phase for one fixed co-radial product, including their unique phases and exact cusps. The Poisson derivative, paraorthogonal fibre formulation and prediction optimization framework are prior tools. Known angular-speed extrema, asymptotic spacing and node/measure characterization are not this finite-degree optimization. Distinct same-day indexed records concern changing the zeros and optimizing variance of the angular speed, not changing the target phase of a fixed product. The conclusion is bounded by the inspected statements and is not a historical priority certificate.

## value

PASS

Minimum separation and largest unsampled arc are distinct and natural design criteria. Giving their entire finite-degree profiles identifies exactly when the best packing and covering phases agree and quantifies phase sensitivity with explicit strict linear coefficients. The result applies to a meaningful design family with continuous zero parameters, not an arbitrary isolated data point or a claim about known weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
