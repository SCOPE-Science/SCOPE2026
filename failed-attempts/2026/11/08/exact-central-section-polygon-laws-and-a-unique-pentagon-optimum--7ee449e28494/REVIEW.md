# Independent mathematical audit

## correctness

PASS

In a right equilateral prism with half-height/circumradius H>0, generic central-plane polygon sides are counted by the sign changes across six base and three vertical edges. The three projected corner dot products sum to zero, so ordering their absolute values reduces all cases to 3,4,5 sides; conditional |U_z| is uniform and gives P(t<b)=b/sqrt(H^2+b^2). Integrating over a sextant yields p3=1-(6/pi)asin(1/(2sqrt(1+H^2))), p5=(6/pi)[2asin(sqrt3/(2sqrt(1+H^2)))-asin(1/(2sqrt(1+H^2)))-asin(1/sqrt(1+H^2))], p4 complementary. Direct derivative of J(H)=sqrt3 H/sqrt(H^2+1/4)-H/(2sqrt(H^2+3/4)) is positive for H>0, with J(0)=0 and J(infty)>1; unique pentagon optimum H*=0.531469551... and p5≈0.3851558057. p3 is strictly increasing and invertible. The included direct-edge Monte Carlo is supporting evidence only; analytic cases/integrals prove continuum. Independently compared exact formula against older arccos law at H=.2,.531469551,.9,2 with differences under 1e-12.

## originality

FAIL

Published November 1, 2026 primary findings already give the complete three-type central-section Haar distribution for the same right equilateral triangular prism at every height, the exact unique optimal pentagon frequency at H=0.531469551..., and explicit inverse height recovery from triangle frequency. The earlier arccos form is algebraically equivalent to the submitted arcsines. The full earlier mathematical proof was inspected; no novel implication remains.

## value

FAIL

This is a natural and potentially useful stereology distribution, but the entire all-ratio central triangular-prism law, unique pentagon optimum and triangle inverse observable were already explicitly proved in earlier primary findings. A distinct derivation or software implementation without any mathematically independent invariant supplies no new scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
