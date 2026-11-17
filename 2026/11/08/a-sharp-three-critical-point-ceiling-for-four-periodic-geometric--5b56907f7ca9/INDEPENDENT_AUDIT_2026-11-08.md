# Independent mathematical audit

## correctness

PASS

Differentiating F gives F’=G/[2sqrt(z)(1-dz^4)^2], with G correct; h_j derivatives strictly positive for 0<z<=1/3, so no earlier root. Reconstructed Q(v)=(1+v)^8 G(v/(1+v)): all 9 coefficients independently computed with SymPy, B0-B2>0, B7-B8<0; the exact inequality B4-(26/7)B3=-9+7d-648a/7-318b/7<-2 excludes the only potential 5-sign-change pattern. Descartes gives at most 3 positive roots counted with multiplicity; endpoint derivative signs imply an odd total, hence 1 or 3. Exact-rational independent substitutions at z=1/2,3/5,3/4,9/10 give +,-,+,-, forcing 3 distinct simple roots and exactly 2 local maxima. This is a universal algebraic proof, not extrapolation of the witness.

## originality

PASS

Best-of-knowledge PASS for sharp all-parameter upper bound, not for previously published 3-root witness or restricted-family uniqueness. Published full same-function cone result supplies only b>=sqrt(d) unimodality and >=3 roots somewhere; it cannot exclude a fourth/fifth outside that cone. No broader exact root-count theorem identified, but broader variation-diminishing results remain a priority risk.

## value

PASS

An exact, sharp global count of candidate optimizers is a meaningful structural boundary for the natural geometric-vector lower bound. It reduces continuous optimization to at most 2 local maxima even when the known uniqueness cone fails; it is not merely a sampled example or a claim about the true operator numerical radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
