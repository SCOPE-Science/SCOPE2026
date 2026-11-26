# Independent mathematical audit

## correctness

PASS

On the invariant anti-diagonal, g(u)=(1-u)e^{-u}, u=s²>0, decreases from 1 to -e^{-2} at u=2 and increases to 0 from below, giving all 0/2/4 counts, including the exclusion of u=0 and the single radius at c=0. Differentiating the actual two-coordinate map yields the normal multiplier a e^{-u}(1-5u+2u²) and the tangent multiplier 1+2au(u-2)e^{-u}. At u=2 the tangent multiplier is 1; the outer branch is expanding. For a<e² the inner branch approaches a normal multiplier strictly inside (-1,1), and its tangent multiplier approaches 1 from below. For a≥e² the normal multiplier is at most -1 for 1≤u<2 since (5u-2u²-1)e^{-u} decreases there to e^{-2}; on 0<u≤3/20 it is at least e^{37/20}/4>1. On [3/20,1], u(2-u)e^{-u} has just one interior maximum and its two endpoint values exceed e^{-2}; hence the tangent multiplier is below -1. The fold curvature g''(2)=e^{-2} gives the stated splitting with coefficient 2e/√a. The half-difference outside M_a/(2|b|-1) grows geometrically in excess of that bound, proving an open escaping set in the same parameter interval as the two local sink basins. No nonlinear stability at (1,-1) or claim about all finite attractors follows. The frozen verify.py implements sampled radius/Jacobian diagnostics, not the continuum proof; it was inspected, not executed.

## originality

PASS

The identical map, numerical stability diagrams and an analytic escape region predate this result. The checked work does not furnish the exact all-coupling obstruction a≥e² or the inner-branch hyperbolic attainment and resulting coexistence for all a<e². Priority is assessed only against the inspected material.

## value

PASS

The precisely motivated invariant is the gain range for stable nonzero antiphase equilibria in the original full-plane map. It turns numerical evidence into a sharp obstruction across every coupling and proves that bounded attractors can persist on an entire open coupling interval where open sets escape. The critical (1,-1) linear spectrum marks where the near-fold sink mechanism ceases to work, without claiming a nonlinear codimension-two classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
