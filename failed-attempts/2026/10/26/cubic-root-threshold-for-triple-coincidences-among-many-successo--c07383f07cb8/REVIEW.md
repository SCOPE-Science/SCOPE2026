# Independent mathematical audit

## correctness

FAIL

The claimed exact second factorial moment is false. For n=2,r=6, let K∼Bin(6,1/2) count orders in one direction. Y=binom(K,3)+binom(6−K,3), giving E[(Y)₂]=35 by exact enumeration of 64 equiprobable choices; the stated formula is 275/8. Distinct arcs with disjoint triples (s=0) need not coexist in a single order and all ordered distinct-arc pairs contribute. Writing M=n(n−1), the different-arc term should be M(M−1)a₀/n⁶ + M(n−1)(n−2)Σ_{s=1}³ a_s/[n^(6−s)(n−1)^s]; the same-arc term is unchanged. In the counterexample this restores 40/64. The mean is correct by one-arc contraction. The finite defect does not affect the critical factorial-moment proof: with fixed moment order, different arcs have bounded probability O(n⁻³ᵏ), while each repeated directed arc uses at least four distinct indices and loses a factor O(n⁻²ᐟ³); the disjoint arc/index configurations have the advertised limit. The isolation estimates and logical equivalence follow by contraction and counting. Supercritical existence also follows directly by keeping the first ⌊Cn^(1/3)⌋ orders and then sending C to infinity, regardless of the erroneous exact identity. This does not validate the full frozen Finding.

## originality

FAIL

The valid asymptotic and logical findings are covered by the indexed orientation-profile theorem and its counting estimates for the identical successor model. The false finite identity cannot supply a distinct valid claim, and fixing its zero-overlap term is an elementary two-event case split, not a valuable surviving finding. This is statement coverage, not a claim about which record was first or their relationship.

## value

PASS

The asymptotic transition and isolation would be worthwhile structural information in this model: they quantify when a growing family of relations first produces triple successor coincidences and show that critical witnesses do not interact. Those findings do not survive as a distinct contribution here. The proposed finite correction is routine accounting and is not needed for the transition or a new application; it does not merit a stand-alone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
