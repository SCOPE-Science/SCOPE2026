# Independent mathematical audit

## correctness

PASS

Independently differentiated the copula, checked the scale a=3λ1, b=5λ2/4 and reconstructed the two inequalities on density and minors. Dividing the small-rectangle TP2 minor by the two side lengths and taking the limit gives D=c c_xy−c_x c_y≥0 even at a density zero; continuity takes this to the boundary. Nonnegativity at corners and (1,0) gives |a|≤1+4b, −1/4≤b≤1/2, and D(0,0) forces a≥0. D at the appropriate corner requires b>−1/16 and a(1+16b)≥36|b|. For b<0 combining with a≤1+4b gives the stated radical cutoff. For b>1/8 the edge x=1 bounds a by 2√(6b(1−2b)); its incompatibility with the corner condition follows from the factor 24b(8b−1)^3, also covering b=1/2 by the limiting edge bound. For sufficiency fix t=|xy| and use 2t≤x²+y²≤1+t² to minimize the density bound, giving a≤1+4b and strict positivity inside, including on the axes. For negative b the worst D occurs at the corner; for nonnegative b the bound follows from the monotonicity of t/[1+b(1+3t)^2], whose derivative has numerator 1+b−9bt²≥0 in range. Integrating D/c² proves interior TP2, then continuity handles every boundary rectangle. Spearman is a/3 by integration; the admissible segment b=0 followed by the upper boundary a=1+4b for 0≤b≤1/8 realizes the full range, with unique a=3/2 at b=1/8. Independent symbolic replay: python3 /workspace/branches/legendre_algebra.py passed the density transform, D, feasibility identities, monotonicity numerator and rank integral. This is algebra corroboration; the continuous inequalities above prove the universal claim. The frozen checker was inspected, not executed.

## originality

PASS

Credit the established family, rho identity, full copula-validity region and general dependence criteria. The supported distinct result is the closed density-TP2 coefficient region and its restricted rank envelope, not any of those antecedents. No exact or dominating covering result was established by the inspected comparisons.

## value

PASS

A sharp structural condition for positive likelihood-ratio dependence in a previously studied two-parameter model is useful beyond basic validity. It settles admissible negative and positive second-mode limits, handles exact zero-density boundary cases, and gives an attainable Spearman ceiling of 1/2 rather than the one-mode limit 1/3 or the unrestricted two-mode ceiling. No claim about more modes or all copulas is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
