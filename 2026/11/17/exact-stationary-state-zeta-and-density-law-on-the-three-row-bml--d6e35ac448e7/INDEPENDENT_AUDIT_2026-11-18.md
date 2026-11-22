# Independent mathematical audit

## correctness

PASS

PASS: In a full-step fixed state, an east car moving into a previously empty site cannot be replaced by a north car as an east-labelled occupant; so there are no east movements, then no north movements. Thus the exact local east and north blocking predicates characterize fixedness in both directions. Vertically legal columns are exactly 18 of 27 ternary triples; the cross-column east predicate builds an 18x18 weighted adjacency with a bijection between labelled configurations and length-n closed walks. The trace/log-det identity yields the whole bivariate law for arbitrary n. I independently enumerated all 18 columns and computed the exact integer characteristic polynomial t^10 times the two claimed quartics and traces n=3..9=1686,19988,237828,2829334,33652161,400231244,4759942476. Rouché on |t|=11 singles out the first quartic root in (11,12); the second quartic roots have modulus<=10 by Cauchy, establishing unique spectral dominance. Numerical perturbation of the weighted matrix independently reproduced species means ~1.28838 and ~1.29490 per column, giving the stated occupied fraction. The finite transfer matrix is an exact all-n reduction, unlike a sample-based extrapolation.

## originality

PASS

PASS (qualified): The full original Biham–Middleton–Levine 1992 model paper and accessible subsequent jamming studies concern traffic-flow phases, random initial states and threshold criteria; they do not count labelled 3-by-n fixed states by both species. A published exact two-row BML result gives a seven-column transfer with a cubic growth base 5.278..., which does not imply the 18-column three-row zeta or two quartics because the vertical blocking alphabet changes. Other Rule184 and 3-row majority fixed-state enumerators concern different local rules. No covering same-object n-family formula was found; an unindexed classical strip-transfer census remains a residual bibliographic risk.

## value

PASS

PASS: The complete two-species fixed-state count for the first nontrivial non-aliased three-row BML strip is a natural invariant of deterministic traffic jamming. The all-n bivariate generating function determines every east/north density sector, and the two-quartic reduction yields exact frozen-state entropy and a nonobvious high-density conditional occupation law. The result does not confuse stationary microstate count with random-initial jamming likelihood.

The dated certificate retains the supplied scientific assessment, sources and limitations.
