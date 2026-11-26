# Independent mathematical audit

## correctness

PASS

On the overlap the sum is 2 cos(a) cos(t); elsewhere no individual contribution exceeds the cap. The proposed clipping boundary u lies in the overlap by sin(2a)<=1, and clipping disappears exactly at and above pi/3. Integrating the overlap with the premium profile and subtracting the clipped excess gives the stated formula; the moving endpoints do not contribute because the excess vanishes there. In the clipped regime, U' has the sign of B_eta for a>0. Up to pi/4, B_eta>=sqrt(2)-pi/4>0; on [pi/4,pi/3), B_eta'<=-sqrt(2)+1/2<0 and its terminal value is -eta*pi/3. The uncapped branch decreases for eta>0, so the only root is the global maximum, including against both endpoints. At the root the coefficient of eta is negative, proving strict decrease by implicit differentiation. The root tends to pi/3 as eta falls to zero, 2u~eta*pi/3, and u^2~2sqrt(3)(pi/3-a), giving the stated quadratic coefficient. For eta=0, precisely the nonclipping plateau maximizes total output. The frozen checker was inspected, not executed; independent direct piecewise quadrature and a numerical derivative (`python /workspace/branches/review_recomputation.py`) give a*(1)=1.0254642013857601183 and full separation 117.50954156231511582 degrees, as diagnostics only.

## originality

PASS

The contribution is the exact unique optimizer and quadratic transition for the explicit clipped-price model, not the prior engineering observation that separated output peaks can reduce losses or that energy price can affect orientation. No distinct inspected source establishes the mathematical claim; incomplete access to two papers limits historical priority.

## value

PASS

The one-peak cap gives a natural boundary between clipping and no clipping. The theorem resolves which offset a small midday preference selects from a whole zero-premium plateau, on which side it lies, and the order and constant of the approach. This is substantive sensitivity information for the idealized capped design, not an installation recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
