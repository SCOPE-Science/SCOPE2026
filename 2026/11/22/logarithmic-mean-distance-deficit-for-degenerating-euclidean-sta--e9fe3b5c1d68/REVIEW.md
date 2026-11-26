# Independent mathematical audit

## correctness

PASS

Re-audited the corrected proof and both stated asymptotics under arclength sampling, with ordered pairs and normalization Q=N/P³. For straight-side length L and each end-piece mass m, the projected reference distance integral is A(m)=4L³/3+4mL²+2m²L, with A(m)−P³/6=−2m²L−4m³/3. The rectangle's flat ends project exactly. The stadium's outward horizontal first moment is 2r² per cap by integration of r cos θ against r dθ. With both orders and straight-side total length 2L, this adds 16Lr²; cap-cap collapse costs only O(r³). Independently expanding the two square-root powers and asinh in the exact opposite-side integral gives J_L(a)−J_L(0)=La²(log(2L/a)−1/2)+O(a³+a⁴/L) for a≤L/5. The two ordered copies with a=2r therefore add 8Lr² log(L/r)−4Lr²+O(r³). For end-side pairs integrate min(2r,2r²/s) at horizontal distance s, obtaining O(r²[1+log(L/r)]) on a straight side and O(r³[1+log(L/r)]) after the cap-length factor; end-end corrections are O(r³). Thus the stadium nonlog term before normalization is (12−2π²)Lr² and the rectangle's is −12Lr². Dividing by each P³ gives, respectively, 3/2−π²/4 and −3/2, with uniform remainder O(η³[1+log(1/η)]) for 0<η≤1/10, since the relative denominator correction is O(η). Subtracting at equal width and straight-side length gives the claimed limit 3−π²/4>0. The original numerical quadrature was inspected but not run; it is not a certificate for either coefficient or the asymptotic error.

## originality

PASS

The validated claim is the nonlogarithmic quadratic coefficient for semicircular caps, its smaller uniform remainder, and the resulting quantitative difference from flat ends. Shared leading logarithmic behavior is covered at the frozen precision and is not claimed as a distinct contribution in the repair.

## value

PASS

The shared logarithmic term alone cannot distinguish a sharp rectangular degeneration from a C¹,¹ rounded one. The revised theorem quantifies the first rounding-sensitive term with a strict positive comparison at a physically natural fixed width and straight-side length. This identifies exactly where the cap first moment enters; it is not merely better error bookkeeping on a known leading term and does not assert extremality over other caps or convex bodies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
