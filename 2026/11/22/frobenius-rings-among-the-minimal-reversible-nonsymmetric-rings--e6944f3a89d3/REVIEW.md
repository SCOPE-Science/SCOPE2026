# Independent mathematical audit

## correctness

PASS

Theorem A of arXiv:2611.19962v1 verifies the hypotheses and complete coverage: 186 local classes with residue field F2 and exactly two nonduo rings. Appendix A gives 1–6 and 21–78 of type (1,2,2,2,1), 8–19 and 79–186 of type (1,3,3,1), and 7,20 of type (1,2,3,2). Its relations agree with the frozen inputs: the common two-generator initial relations include x²+y² and x²+xy+yx, with x²y²=0 (equivalent to x⁴=0 given x²=y²) and degree five truncated. For the three-generator cases the degree-leading relations are those from the characteristic-two presentations and the four characteristic-four A–D families; the latter split 44+44+10+10. The listed initial relations surject onto the associated graded algebra, and equality of dimension (eight) upgrades the surjection to an isomorphism; this is important because taking initial forms of generators alone need not give the whole initial ideal. The independent Python 3 replay /workspace/branches/socles256_audit.py reads only the transcribed literals, closes the ideal under prepending and appending generators, tests all vectors in each pairing radical, and checks all 256 elements for each of the 19 characteristic-two socle computations. G has ranks (2,2,2), each three-generator presentation has (3,3), and the A–D matrices match. Any element in a radical degree below the top has a nonzero product with a complementary positive radical degree, on either side, or is a unit in degree zero. Reversibility also equates the two socles. The top has order two in the 184 cases; in 7 and 20 the top has order four and sits in each socle. For a finite local ring with residue F2, every nonzero left ideal meets the left socle, and each socle additive line is a simple left ideal. An additive character extending the nontrivial character of a size-two socle separates all nonzero left ideals; for a larger elementary-abelian socle any character kills a nonzero line. The injection r ↦ [x ↦ χ(xr)] in the source is on left modules with (a·φ)(x)=φ(xa), not right modules as labeled; this sidedness slip does not affect the criterion or the claim. The census depends on the published completeness theorem, and no exact socle size for 20 beyond the lower bound is inferred.

## originality

PASS

The 186-class census of isomorphism types, duo split, and presentations belong to Grau Ribas–Oller-Marcén. The new classification is by generating-character/Frobenius status. The primary source gives presentations, not the socle or complementary-pairing classification, and neither the duo split alone nor a one-dimensional terminal radical layer decides the missing direction. No equivalent census was identified in the inspected material.

## value

PASS

Simple socle and Frobenius duality are natural ring invariants, particularly for a full classification at the minimal order where reversibility and symmetry diverge. The nondegenerate top pairings explain why 184 mixed- or equal-characteristic rings have a simple socle, and the two larger terminal layers explain the precise exceptions. This is a structural refinement of the existing classification, not a new claim about that classification itself or an arbitrary selection of rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
