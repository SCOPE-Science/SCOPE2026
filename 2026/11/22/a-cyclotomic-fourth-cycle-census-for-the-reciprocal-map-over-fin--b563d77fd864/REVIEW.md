# Independent mathematical audit

## correctness

PASS

The coprimality-of-values induction applies over every field, and D₄=∏_{j=0}^3 Nⱼ ensures each of the first four inputs is nonzero for a root of N₄−XD₄. Independently expanded the return equation and verified its exact factors P=2X²+1, A, B. Their discriminants are −8, 2048, 324000000 and the pairwise resultants Res(P,A), Res(P,B), Res(A,B) are 4,25,81. Thus all fourteen geometric return roots are simple and disjoint in the stated range; no lower periods except two can divide four. Moreover f²(X)+X=A(X)/[X(X²+1)], so A describes exactly the anti-return f²(x)=−x; oddness makes this subset invariant, and B is invariant as the remaining primitive period-four set. Evaluating in the actual cyclotomic quotient rings gives the stated roots, stabilizers {1,7} and {1}, and orbit sizes 4 and 8; these imply the characteristic-zero irreducibilities. The rational denominator for the quartic parametrization is a unit away from 2 since its square is 2. The factor identities therefore specialize at a primitive root of unity for every p≥7, and separability preserves the sizes of the distinct root sets. The action of q-Frobenius on indices is multiplication by q, with constant stabilizer on each orbit because the groups are abelian. It fixes all or none of each invariant root set; dividing the rational point counts by four gives the claimed indicators. Reviewer-written exact replay `python /workspace/review_checks/1.py` uses SymPy over integer/rational polynomial rings and finite-field arithmetic for 248 prime fields and six quadratic extensions; these finite checks are not the proof of all extensions. Frozen verifier inspected only.

## originality

PASS

Best-of-knowledge pass limited to the primitive period-four splitting and count. A directly inspected earlier finite-field census covers periods at most three; the actual originating reciprocal-sum paper is now accessible and its substantive finite-field discussion concerns preimages of zero, not these returns. No absolute priority claim.

## value

PASS

Period four is the next natural census after the already studied periods two and three. The exact separation into two cyclotomic splitting criteria, coexistence of all four counts 0 through 3, and extension-field uniformity give reusable orbit data rather than a finite lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
