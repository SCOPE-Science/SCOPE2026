# Independent mathematical audit

## correctness

PASS

Deleting a specified set of singleton labels preserves cyclic noncrossing and is bijective, so the sign expansion gives the Catalan transform for the counting kernel with multiplicities. For m=n-w>=1, shifting the Catalan moment measure gives the even semicircle weight times y^w(2+y)^(m-1). Pairing opposite y gives positive integrals except for odd w at m=1; at m=0 the arcsine moments give (-1)^n binom(n,floor(n/2)). The weight difference identity Lambda(n,w)-Lambda(n,w+1)=2 Lambda(n-1,w) on the pre-top shells and the semicircle moments give the stated exact gap, including n=1 and n=2 where the top shell ties. At odd n=2m+1, the top magnitude equals (2m+1) C_m, and at even n=2m it equals (4m-2) C_(m-1). At even order the missing layer is the n weight-(n-1) modes. Multiplication by the top character identifies their projection with the first-level projection. The convolution kernel of the complementary projection has norm 1+(n/2^n)(binom(n,n/2)-2) at either endpoint, using (n-2j) binom(n,j) = n[binom(n-1,j)-binom(n-1,j-1)] and symmetry. Averaging over translations preserves the range and fixes it pointwise, so no projection improves this norm. Stirling gives its asymptotic. Independent Python replay at branches/89ef1d1d-16b9-470c-a660-23f930f7fc07/check_record3.py verified every enumerated coefficient through n=8, exact formulas through n=80 and endpoint norms through n=8. The frozen script was inspected, not run. Unweighted distinct profiles are demonstrably different: at n=4 they have six zero masks, not the four in this theorem.

## originality

PASS

The supported distinct part is the all-order recovery classification and exact positive gap for the multiplicity-weighted noncrossing singleton profile, identifying the precise lost layer and hence its optimal endpoint recovery cost. Catalan enumeration, the semicircle moments, and translation-averaging optimality are standard inputs. In particular, the endpoint norm is the complement of the usual first-level projection norm conjugated by a Walsh character; it is not credited as a new general projection principle. No verified distinct source was found that gives the complete signed-shell classification for the stated kernel.

## value

PASS

This determines not only exact recovery and the smallest nonzero singular value but also the precise missing Walsh layer. The latter produces an exact and useful contrast: the lost fraction goes to zero exponentially while the optimally achievable endpoint projection norm diverges like sqrt(2n/pi), even if arbitrary linear recovery projections are allowed. The result is about a natural multiplicity-weighted observable and distinguishes Hilbert stability from endpoint recovery cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
