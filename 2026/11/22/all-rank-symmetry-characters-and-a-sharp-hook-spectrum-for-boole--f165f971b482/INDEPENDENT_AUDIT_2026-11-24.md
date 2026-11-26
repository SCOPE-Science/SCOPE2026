# Independent mathematical audit

## correctness

PASS

Kitajima's definition and Corollary 4.19 apply to precisely the proper Boolean rank-span complex and concentrate its reduced homology in degree k. A fixed simplex cannot permute vertices of different ranks, so it has trace +1. Its fixed vertices are whole-cycle unions. For a nonempty set J of cycles between the two endpoints the remaining cycles give 2^(c-|J|)-2 valid endpoint assignments, and the alternating sum over ordered nonempty increments is (-1)^|J| by the falling-factorial identity. Together with the reduced augmentation this gives the stated cycle product with the stated sign. Independently, cover by rank-selected windows W_i=[i,i+k], i=1,...,n-k-1. Each new window meets the previous union precisely in the rank-selected complex on [i,i+k-1], since any face in it already has rank at least i and the previous union has upper ranks at most i+k-1. Reduced Mayer–Vietoris and concentration of rank-selected Boolean homology show that the top module is the sum, up to rational isomorphism, of the ribbon modules of the windows (k+1 ranks) and the successive intersections (k ranks, i=2,...,n-k-1). Equivalently the signs in the equivariant reduced Euler characteristic give positive contributions for both. The standard exact-descent-set rule for these ribbons gives one hook per permitted descent set of the prescribed cardinality, since a standard tableau of hook leg r is uniquely specified by its r descents. This yields n-k-1 copies at leg k+1 and n-k-2 at leg k, and none for the trivial hook. This independently checks the endpoint case k=n-2, when only the full-rank sign module remains, and includes k=1. In the quotient, the rank span condition gives a rank complex in which the leftmost vertex link is a cone on its successor, confirming contractibility. The frozen code was inspected, not executed.

## originality

PASS

Credit the previously known span-two character, nonequivariant persistence, Kitajima's window union and concentration, and the rank-selected ribbon representation theorem. Importantly, these last two primary papers together already give a direct route to the representation and the hook numbers via equivariant gluing. The distinct contribution supported here is the evaluated, uniform cycle-type trace formula for the whole range, with an explicit evaluation of the hook spectrum. It is not a new concentration, ribbon, or quotient theorem, and I do not credit the broader assertion that prior equivariant rank-selection theory cannot compute these filtered representations.

## value

PASS

A short cycle-type formula gives trace values at every permutation in every moving-window stage without decomposing ribbon modules or enumerating fixed chains. It determines the rational action, not just dimensions or persistence. The evaluated two-hook support makes the representation-theoretic effect of the rank-span cutoff explicit, including the unique terminal appearance of sign. The value is in these natural evaluated invariants, not the mere substitution of rank sets into the known ribbon theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
