# Independent mathematical audit

## correctness

PASS

Slicing at integer height j gives the product of a triangle lattice count and a segment lattice count. Independently summing its cubic in j against the four power sums yields the displayed quartic; the Ehrhart-series binomial transform gives the stated numerator. Exact symbolic recomputation reproduced both discriminants and all coefficients. For c≥1, h* has positive leading cubic coefficient and takes the signs negative, positive, negative, positive at −∞, −1, −1/(c+1), 0 respectively; the two finite negative-argument values are 4c²+c−2 and −(c+2)²/[2(c+1)]. This independently proves three simple negative roots. The quadratic Ehrhart factor has discriminant c²(c²−12c−12); for integer c≥13 its two roots have positive product and sum between zero and one, so each is in (0,1). For integers 1≤c≤12 it is nonreal, and c=0 reduces to (t+1)³(t+2)/2 with h*=1+7u+4u². The two ordinary coefficient crossings fall strictly in (9,10) and (11,12). The endpoint fibers establish the vertex and facet counts, and the primitive fiber directions together with the linking edge of unit height form a lattice basis at each vertex. Replay: python3 /workspace/evidence/bounded_checks.py 2, using SymPy. The packaged exact checker was inspected, not executed; the conclusions are for the stated integer family, not all smooth four-polytopes.

## originality

PASS

Credit the prior polytope and full slice-count formula, which give the coefficient signs and ordinary root transition by routine algebra. The supported distinct claim is strict negative real-rootedness of the numerator uniformly for this positive-parameter family, yielding its coexistence with positive Ehrhart roots in a natural smooth family. Neither the identified broader theorems nor a same-day related Cayley result covers that claim. This is not a claim of priority for the family, the count, c=0 numerator real-rootedness or the published c=12 negative coefficients.

## value

PASS

The family was introduced to test Ehrhart positivity in a small-facet smooth setting. Showing its entire numerator spectrum stays simple, real and negative despite a separate onset of positive roots of the counting polynomial gives a precise separation between two common positivity and root questions. The ordinary cutoffs alone would be a routine expansion of the known count; the uniform contrast of spectra is the useful fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
