# Independent mathematical audit

## correctness

PASS

The primary arXiv:2611.11635v1 p. 2, equations (1)–(4) and Theorem 1.1 do state the given sharp variational reduction and absolute directional inequality for every unit u, and identify the projected-volume constant. Scaling the affine profile removes one endpoint; r=∞ correctly represents the zero left endpoint. Independently integrating by the formula I_j=1/(j+1)+2(r-1)/(j+2)+(r-1)^2/(j+3) gives the displayed F(r). Differentiation yields -3Q/(20 A^2 B^2), with a strictly positive denominator on r>=0. One sign change and Q(0)<0<Q(1) give one positive zero and strictly increasing then decreasing F, including strict comparison to the two endpoint values 3/20 and 1/20. The exact resultant is 1769472000 times the displayed sextic in z. In /workspace/branches/check_centroid.py, polynomial powering and Euclidean GCDs modulo 113 give gcd(f,z^(113^i)-z)=1 for i=2 and 3 (and likewise for Q). This excludes all irreducible factors of degrees 1,2,3, hence proves irreducibility at degree six with unchanged leading degree. For the value sextic the actual remainders for i=2,3 are 13z^5-56z^4+2z^3+z^2+14z-42 and 4z^5+19z^4-23z^3+16z^2-48z+19. The replay also certifies the printed decimal prefixes with rational brackets and exact root counts. For the sharpness polytopes the cross-section volume is 4ε^4 tℓ(t)^2, yielding I2/I1; the bottom and top face densities are constant multiples of ℓ(t)^2 and total order ε^2, whereas lateral and end faces contribute O(ε^3) and O(ε^4). Thus their boundary first-coordinate centroid tends to I1/I0. Width is one, diameter tends to one and the ratio is sharp. Uniqueness is of the normalized affine optimizer only.

## originality

PASS

Credit the full geometric inequality, common constant, already-computed one-parameter objective in general dimension, and the exact family K_ε with unspecified maximizing profile to the primary papers. Neither decisive source passage supplies the evaluated maximum in dimension four. The supported distinct result is specifically the evaluation and proof of its algebraic degree and unique normalized optimizer, not the variational characterization or polytope construction principle. Substitution into the prior formula supplies an unevaluated rational optimization, not the new exact facts about its maximizer and arithmetic degree.

## value

PASS

D4 is a natural unknown sharp coefficient shared by two established centroid inequalities, in the first dimension beyond the explicitly solved three-dimensional case. The useful outputs beyond a substituted objective are the first exact four-dimensional threshold with a certified algebraic degree, and the unique taper ratio to instantiate known extremizing bodies. An exact algebraic specification permits rigorous comparisons rather than reliance on approximate optimization, and the degree-six certificate establishes that a lower-degree algebraic equation cannot suffice. The incremental value is this evaluated invariant and the isolated profile, not new geometry or a general dimension formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
