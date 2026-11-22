# Scientific assessment: exact nodal walls and bielliptic canonical model

## Correctness — PASS

The proof gives a complete gradient elimination over the affine chart and a separate exhaustive infinity analysis. All putative additional singularities are nondegenerate by exact Hessian determinants. The six base points are transverse and have analytic normal form \(u^3+sv^2=0\). Bézout excludes factorization of a sextic with at most four nodes and six unibranch cusps; the genus and Tjurina formulas then follow. The quadric-cubic model is obtained by reversible homogeneous identities, its generic smoothness follows from equality of arithmetic and geometric genus, and the quotient cubic is checked smooth away from the same walls. Exact symbolic checks in `check.py` passed. The proof does not cover the excluded parameter lines.

## Originality — PASS, qualified

Oka–Pho's classification already contains the exact singularity *baskets* \(6A_2+A_1\), \(6A_2+3A_1\) and \(6A_2+4A_1\); those baskets are expressly prior art. The additional statements are the exact parameter-wall arrangement and four-node collision in the specified symmetric two-parameter pencil, the all-fiber integrality on the stated open base, and the explicit smooth canonical bielliptic normalization on its complementary open subset. The 2026 Dimca–Sticlaru paper treats Tjurina/Betti formulas but not the exact symmetric pencil; the Cogolludo-Agustín–Elduque generic-fiber result is likewise not a special-fiber classification. Searches of published mathematical records and accessible prior claims found no direct or stronger equivalent description. Risk remains that a differently parameterized classical normal form encodes the same information.

## Value — PASS

The family is a geometrically natural symmetric \((2,3)\)-torus pencil with six persistent cusps. The classification identifies every parameter at which its geometric genus and Tjurina scheme jump, including a transverse four-node crossing that forces rational normalization. The canonical quadric-cubic equations identify a bielliptic structure on the generic genus-four normalization, providing a useful bridge from singular plane models to smooth canonical curves. This is more structural than an isolated basket example, and the exact walls are not implied merely by the known existence of those baskets.

## Limits of review

Only the new statements were assessed. The main remaining originality risk is an equivalent published parameterization not found by the inspected source sections, semantic record comparisons, or exact-formula web searches. The excluded parameter loci are not classified. The checker supplements, rather than replaces, the mathematical proof. No external audit was performed.

Self-review: passed. Independent audit: not yet performed.
