# Independent mathematical audit

## correctness

PASS

PASS. Three IID hyperbolic arclength-uniform points on a geodesic circle of radius R in curvature −1 give anchored angular gaps (G1,G2,G3) uniform on the 2π-simplex with density 1/(2π²). The hyperbolic chord formula a_i=2asinh(sinh R sin(G_i/2)) and semiperimeter identity tanh²r=Πsinh(s−a_i)/sinh s lead to 4tanh²r=Π(1−u_i)/(1−Πu_i), u_i=e^{−2(s−a_i)}. For fixed gaps, r→r*=atanh(1/2); this alone cannot justify exchanging expectation and limit. Source proof constructs uniform deficit envelope C/(1+e^R G_min)^2, including double-gap corners, and analyzes each minimum-gap chart G_min=x e^{−R}, next gap b. For x>0,b∈(0,2π) it gives deficit profile δ(x)=0.5log[3(1+exp(−2asinh(x/4)))/(3−exp(−2asinh(x/4)))], independent of b. DCT yields e^R E[r*−r_R]→3I/π; change of variable gives I=π−4/sqrt(3) atanh(1/sqrt(3)), so constant 3−12/(πsqrt3)atanh(1/sqrt3)=1.547846114742869.... The Q_R density weighted by the nonnegative deficit converges pointwise in each of three charts to δ(x)/(6πI); its total mass is one, hence Scheffé proves total variation, yielding independent uniform minimum-gap index, density δ/I for scaled minimum x, and uniform next gap angle. Independently evaluated I by high-precision quadrature: 1.62090066098790054 agrees with closed form; constant 1.54784611474286907. Original check_inradius.py read, not its printed log treated as proof. Scope is mean-deficit size-bias, not typical e^{−2R} almost-sure deficit.

## originality

PASS

PASS best-of-knowledge with a decisive same-ensemble comparison. Another published result for exactly three arclength-uniform points on an expanding hyperbolic circle establishes the *typical* e^{2R} inradius deficit, its half-Pareto limiting tail and tail-conditioned mark. Its limiting variable has infinite mean, so its statements do not entail a finite-R e^{−R} expectation coefficient or the deficit-weighted Q_R total-variation law. The current result resolves precisely the loss of uniform integrability through a different e^{−R} angular boundary layer. Classical hyperbolic inradius identities are credited, not claimed. No exhaustive priority guarantee.

## value

PASS

PASS. Nonuniform integrability creates a mathematically meaningful discrepancy between typical e^{−2R} deficit and mean e^{−R}. The exact coefficient and total-variation law identify the angular near-collision source of the mean and its deficit-biased typical configurations, giving a quantitative answer not mechanically implied by the existing heavy-tail limit. This exact asymptotic can be used for future random hyperbolic polygon statistics and concentration comparisons; no paper-sized general theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
