# Independent mathematical audit

## correctness

PASS

Verified independently of the symmetry witness table by enumerating every tour with the least vertex fixed first, retaining both orientations and counting the closing edge. Using d=popcount(i xor j), there were 16,064 orders over 247 subsets. For every subset, the minimum of B=sum d(d+1)/2 among tours with A=sum d≤8 was at most 12. It equaled 12 exactly for labels 07, 16, 25, 34, 0356, 1247. Analytically, set T=2^(p*/2)>3, with 3^(p*/2)=2T. For step counts (a,b,c), put w=b+2c. The certificate gives a+3w≤12 and w≤4, yielding cost a+Tw≤12+(T−3)w≤4T at p*. A witness with B<12 gives a strict bound there. The same tour has cost at most 8 at p=2; Hölder interpolation gives the bound 4·2^(p/2) between 2 and p*, and each d≤3 gives the upper bound 2·3^(p/2) for p≥p*. Strictness for every other subset propagates to p>2. Parity tetrahedra and antipodal pairs have constant distances per tour and attain their stated cost at every p; their exact comparison gives the tie and equality regimes. No equality classification at p=2 is inferred as part of this decision.

## originality

PASS

The supported distinct contribution is the exact vertex-subset envelope for all real p≥2 and its extremizer switch, not the parity-tetrahedron witness or a standalone p=3 cube result. A same-date indexed prism result gives exact overlap at t=1, p=3, but varies aspect ratio at a fixed power rather than varying power. Its unattributed statement that the power-exponent cube classification is already known raises a priority risk; the only exact indexed match located for that description was this assigned record. Neither that sentence nor the primary sources it cites establishes distinct coverage of the full envelope.

## value

PASS

The first nontrivial three-dimensional vertex domain is a natural exact test of the geometric tour problem. It distinguishes a four-point geometry from the two-point diameter geometry, including their crossover and tie, instead of just confirming a few exponents. The simultaneous two-weight certificate is what makes the classification apply over the entire continuum of powers; the finite result can serve as an exact benchmark without being a solution in the continuous cube.

The dated certificate retains the supplied scientific assessment, sources and limitations.
