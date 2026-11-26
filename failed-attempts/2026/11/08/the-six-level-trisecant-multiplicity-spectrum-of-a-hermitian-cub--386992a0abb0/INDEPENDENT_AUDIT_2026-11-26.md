# Independent mathematical audit

## correctness

PASS

The homogeneous partials prove smoothness. Over F4 the affine counts are two for each x, and infinity adds one, so both F4-Frobenius eigenvalues equal -2 and their cubes give 81 curve points over F64. The tangent polynomial h^2(h+a+a^4) at an affine curve point shows that a flex has a in F4; its y also lies in F4 since the two solutions of y^2+y=a^3 already lie there. Infinity is a flex as well. The 72 nonflex tangents each have one distinct rational residual point, and every two-point line is such a tangent because the third intersection after two rational points is rational. Counting pairs yields 1056 trisecants. Directly reproduced the exhaustive finite census by an independent pair-join method, replay python3 /workspace/check_secants.py. The implementation uses the reciprocal modulus u^6+u^5+1 (inversion of the residue generator gives the specified field presentation), checks inverses, forms each distinct secant by normalizing a projective cross product of two of the 81 enumerated points, and recognizes trisecants by exactly three unordered pairs sharing that join. It walks each trisecant's 65 points by affine slope or vertical parameter and includes points at infinity. It returned exterior counts 11:72,14:648,16:2052,17:864,18:432,26:12, interior 39:72,40:9, line counts 1080,1953,72,1056, and exact set equality of the 26-locus with the exterior subplane calculated by u^4=u. The test of the 40-locus also matched the nine subplane curve points. This is exhaustive in the fixed plane only; the uploaded verifier's two methods were inspected but not executed.

## originality

FAIL

A distinct indexed record, 93d11627de18, states the same complete exterior table and the same marked twelve-point locus for the same cubic and field. Projection fibers are simply the pencil's line sections, so the alternate terminology changes no invariant. The ancillary line and on-curve counts do not provide a separately meaningful new finding.

## value

FAIL

The number of trisecants is a natural and motivated refinement of arc completeness, and the exact max locus is mathematically useful. But both facts and the complete census are already known in the distinct indexed record. An independent computation confirms them without adding new mathematics; flux through the remaining line classes is a routine incidence deduction. No repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
