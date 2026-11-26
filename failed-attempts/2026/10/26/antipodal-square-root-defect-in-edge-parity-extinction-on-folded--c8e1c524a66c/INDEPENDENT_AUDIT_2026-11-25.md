# Independent mathematical audit

## correctness

PASS

Over F2 the incidence factorization is exactly F=B^T B, including the zero diagonal. The connected graph gives im B=J (the even-sum hyperplane) and ker B^T=<u> with u in J, so rank F=2^d-2. BB^T is multiplication by q=e2+...+ed in the square-zero group algebra; q^2=0 gives F^3=0. The off-diagonal-one alternating matrix of e2 has corank zero or one. After pairing variables, removing a degree-k term uses replacements of partner variables by degree-(k-1) corrections; cross terms start at degree 2k-2>k and the linear part remains invertible. Each pair contributes homology dimension two, and an unpaired variable contributes a factor of two. Thus rank q=2^(d-1)-2^floor((d-1)/2). Restriction to J removes exactly one rank since q has degree two and qJ has minimum degree three; B^T removes one more since q times the product t3...td is the top monomial u, with d>=3. The claimed Jordan counts and extinction histogram follow by ranks of iterates. At d=3 the square vanishes but F has rank 6, so the last step is exactly two; the counts 1, 1023, 64512, 0 and density 63/64 agree. At d>=4 the square has strictly positive rank. The unaugmented comparison also follows by writing its vertex element as a nonzero linear form, with rank 2^(d-1), and making the same two rank cuts.

## originality

FAIL

A distinct indexed result for higher-distance vertex parity already gives, in its proof, the decisive rank rule for arbitrary higher jets above the maximal-rank odd-dimensional alternating quadratic part. The entire new-looking square-root defect follows mechanically from that rule, using a dummy variable in even dimension and the same two incidence rank cuts exhibited by the separate unaugmented line-graph record. The exact augmented graph is not stated in either, but applying their results yields the exact claimed ranks and hence the entire transient law. This is verified deductive coverage, not a determination of which of the same-day records came first.

## value

FAIL

The graph and the edge-extinction invariant are well motivated, and the formula is useful as a worked application. As a standalone exact-invariant finding, however, the claimed square-root term is the already available quadratic-jet rank with the incidence correction; the remaining multiplicities and densities are just the same ranks translated into other statistics. The claimed exact fact is mechanically implied rather than an independently needed new computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
