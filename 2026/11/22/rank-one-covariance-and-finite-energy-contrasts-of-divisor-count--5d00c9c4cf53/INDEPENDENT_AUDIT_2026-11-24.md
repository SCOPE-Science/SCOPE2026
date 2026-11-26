# Independent mathematical audit

## correctness

PASS

Reconstructed the finite-period normalization: the joint divisibility mean is 1/lcm(d,e), so expanding gcd(d,e) as a sum of totients gives the exact second moment Σ_{r≤By} φ(r)G(r/y)²/r². The first moment is v+O(1/y) by harmonic sums, with no rational-endpoint requirement. Summatory φ and partial summation give κ log x+O(1) for total weight and log(v/u) times κ as the limiting weight of each interval (u,v] away from zero. Finitely many floor jumps on any truncated interval allow integration against the limit. G(t)=v+O(t); for nonzero v the replacement by v² in the second moment costs O(1), since φ(r)/r²≤1/r. For zero v the contribution r≤εy is O(ε²) uniformly, giving exactly the stated finite integral after subtracting the vanishing squared mean. Polarization supplies the rank-one covariance matrix. Direct finite-X pair discrepancies sum to O(y²/X), and the corresponding means cost O(y/X). For the balanced dyadic difference G=−1 on (2,4), proving strict positivity. An independent step-sum calculation with x=4/t and cut at x=400000 gives 0.50821852788883831499…; the omitted positive tail is bounded by 5×10^(−9) using |G(t)|≤10t near zero. Replay: python3 /workspace/branches/f2242719-5199-4216-880c-d47ecbdc3d65/dyadic_constant_decimal_check.py (also dyadic_constant_independent.py). Ford's presence estimate transfers to period sampling by taking X an arbitrarily large multiple of L_y for each fixed y, so each dyadic presence probability tends to zero. The union bound gives convergence in probability to zero for the difference, while its squared mean tends to zero and its second moment does not. Frozen verify.py inspected, not executed; numerical computation supports only the displayed decimal.

## originality

PASS

Credit the classical gcd–totient identity, summatory totient asymptotic, and prior divisor-presence and frequency theory. On bounded evidence the joint proportional-window covariance law and the necessary-and-sufficient contrast criterion with its exact limiting energy are distinct. No priority is claimed for the vanishing presence probability.

## value

PASS

The natural fixed-window vector has a single logarithmically diverging direction and a complete finite-energy criterion for contrasts orthogonal to it. The positive contrast for disjoint adjacent dyadic windows shows what leading correlation and convergence in probability both miss. The exact integral, not just the numerical constant, makes the classification reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
