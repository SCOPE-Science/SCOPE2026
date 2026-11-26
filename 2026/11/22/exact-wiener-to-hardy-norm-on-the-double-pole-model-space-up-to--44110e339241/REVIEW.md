# Independent mathematical audit

## correctness

PASS

The Taylor coefficients are c_0=a and c_k=r^(k-1)[(2ra+b)+(k-1)(ra+b)] for k>=1. Summation bounds their absolute total by the three covectors v_0,v_1,v_2 in the record, with equality when the two tail combinations point along the same ray. Summing squares/cross-products of the two numerator columns gives equal Hardy Gram diagonals (1+r^2)/(1-r^2)^3 and off-diagonal 2r/(1-r^2)^3; its determinant is (1-r^2)^(-4) and inversion gives the displayed matrix. The squared majorant norm is the maximum inverse-Gram norm squared of the sum of three unimodularly phased covectors by duality and Hilbert Cauchy–Schwarz. After fixing the first phase and optimizing the last, the off-diagonal objective becomes At+sqrt(B^2+C^2-2BCt) with A,B,C as in (69)–(72). Here A,B,C>0 and C/B>=2 on the positive stated interval; the objective is strictly concave. Its right derivative at t=-1 is A-BC/(B+C)<=0 by the factorization involving (1-2r)(1+2r); strict concavity gives the unique maximum even when the endpoint derivative vanishes at r=1/2. The last phase then must be -1 as well. Multiplying v_0-v_1-v_2 by the inverse Gram yields (1-r^2)(1+2r^2,-1-4r), and pairing gives the squared constant. Both tail combinations for that vector have strictly negative real sign after rescaling, so the majorant is exact and all extremizers arise from that unique phase choice and the Hilbert equality condition. At r=0 two coefficient magnitudes give the elementary equality criterion; at r=1/2 the unscaled extremizer has Wiener norm 9 and Hardy norm squared 12, consistent with 3sqrt(3)/2.

## originality

PASS

The exact full-subspace norm and equality vectors on 0<r<=1/2 were not established by the inspected general rational Wiener–Hardy inequalities or asymptotic lower-test results. The repeated model space itself is classical, r=0 is elementary, and the sharp endpoint vector is proportional to a published test function at n=2, rather than a new test function in isolation. The new assertion is the global exact norm and uniqueness at that endpoint and across the positive range, best of current knowledge.

## value

PASS

A repeated pole is the first nontrivial coalesced-zero model for the rational Wiener/Hardy embedding, and its exact sharp constant and uniqueness are information not delivered by the large-degree rate. The range is motivated by an explicit global phase criterion, not by an arbitrary numeric sample; the half-radius case includes a prior test function but answering whether that test is a global optimizer is a distinct exact question. The result gives a reusable finite-degree benchmark for extensions to larger radii or distinct poles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
