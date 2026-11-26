# Independent mathematical audit

## correctness

PASS

Nondegenerate trace pairing over every field identifies a rank-one map with R(X)=tr(VX)U, up to reciprocal scaling. Take Z with tr(VZ)=1. Applying the identity first to (Z,Z) gives U²=λU, then to (Z,Y) and (X,Z) gives VU=aV and UV=bV with a+b=λ. Consequently a²=λa and b²=λb. If λ=0 both scalars vanish; otherwise exactly one is λ, in characteristic two as well. Normalizing U/λ gives the unique nonzero idempotent on the image line. Substitution proves sufficiency. Cyclicity of trace gives tr(VU)=0 in either normalized case, hence R²=0. For square-zero U of matrix rank r, choose image, containing kernel, and the quotient-to-image isomorphism; the valid V form Hom(Kⁿ/im U, ker U), and nonzero pairs are counted modulo a free scalar action. For idempotents, image and complementary kernel give the stated Gaussian factor times q^{r(n−r)}; the two disjoint nonzero rectangular-block families supply the remaining factor. An independent exhaust of (U,V) tested the original identity on ordered pairs of matrix units, deduplicated by full basis actions and checked R²=0. It found 3+12=15, 8+48=56 and 315+336=651 for (n,q)=(2,2),(2,3),(3,2); pair counts were 15,112,651. Replay: /workspace/branches/fdf27dce-93cb-489b-91d6-eb6659975d0e/independent_check.py. The frozen verify.py was inspected, not executed. The finite replay does not prove unrestricted n or extension-field cases.

## originality

FAIL

The distinct indexed November 2 Resultary record gives the same unrestricted-field normal forms, uniqueness, square-zero composition, and all-size labelled counts, including the n=2 boundary. Its added asymptotic is not part of this frozen claim. The exact overlap precludes accepting this version as a distinct finding; it does not establish that the other version preceded this one, or resolve priority, dependence, or attribution. The explicit n=2 simplification is an algebraic specialization of the overlapping formulas.

## value

PASS

The underlying mathematical problem is substantive: a complete normal form on all full matrix algebras for a natural nontrivial operator stratum distinguishes vanishing multiplication from idempotent images and gives field-uniform counts not available from M2 orbit lists. This is valuable as a classification and an enumerator, irrespective of whether this version adds anything to the existing equivalent record; there is no such distinct addition here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
