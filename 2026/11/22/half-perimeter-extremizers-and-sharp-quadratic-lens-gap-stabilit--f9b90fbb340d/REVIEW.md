# Independent mathematical audit

## correctness

PASS

Reconstructed the disk geometry and checked the bound independently. The farthest center changes at the rays bisecting consecutive opposite-center directions. In one such sector the corner at radius r satisfies r sin(alpha)=sin(q/m) and t+r cos(alpha)=cos(q/m), where alpha=pi/m and q=P/2. This gives t=sin((pi-q)/m)/sin(alpha), strictly decreasing from 1 to 0. Summing the corner polygon and the unit circular segments gives the stated area profile. With s=(P-pi)/pi, beta=pi/2, and k=m/(2 sin(alpha)), the gap is cos(beta s)-k[cos(alpha s)-cos(alpha)]. Its derivative with respect to q is positive on 0<q<pi/2 by strict increase of sin(alpha z)/sin(beta z) for 0<z<1 (x cot(x) decreases), and symmetry supplies the other half. For an independent check of the sharp envelope, regard the gap as a function of x=s^2. The second derivative of cos(a sqrt(x)) is a/(4 x^(3/2)) times the integral from 0 to a sqrt(x) of t sin(t) dt. Bounding sin(t) between 2t/pi and t gives the gap a strictly positive second derivative, since 2 beta^4/pi>k alpha^4 (the latter is at most pi^4/36). Its chord between x=0 and 1 is therefore a strict upper bound in between. This proves all equality cases; endpoint continuity forces the constant even on the open perimeter interval. Substitution gives G_m, the optimizing radius and the Reuleaux triangle; tan(x)/x gives the monotone limit. The frozen finite script is corroboration, not the proof, and was inspected rather than run.

## originality

PASS

Credit the exact area profiles, strict fixed-perimeter hierarchy, and lens lower bound. The supported distinct claim is the variable-perimeter maximizer and the sharp global upper envelope with its equality set; the available prior statements do not supply that quantitative upper optimization.

## value

PASS

The total gap between two canonical profiles has one optimizing perimeter for every disk count. The sharp estimate controls all perimeters at once and distinguishes global sharpness, which is forced by degenerate endpoints, from the local curvature at the interior maximizer. That is meaningful additional information beyond a known exact area formula or another finite comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
