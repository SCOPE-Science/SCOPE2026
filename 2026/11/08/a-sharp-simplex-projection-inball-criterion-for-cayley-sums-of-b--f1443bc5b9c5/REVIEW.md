# Scientific review

## Correctness (C): PASS

The theorem concerns the standard Euclidean metric on the explicitly normalized \(m+d\) coordinate realization. Orthogonal projection onto the simplex gives the sharp universal upper bound \(\rho_d\) and forces the unique simplex incenter at equality. The norm \(H_i\) of each upper fiber inequality is computed directly, and exact ball-in-halfspace containment gives independent lower and upper bounds on each center coordinate. Nonempty intervals are equivalent to the row criterion. The all-positive corollary follows from containment of \(\Delta_d\times[0,1]^m\); the sharp sparse-family exception follows from an explicit nonnegative rationalized square difference. Every quantifier includes \(d,m\ge1\), nonnegative real matrices with nonzero rows, and the separate integral subfamilies. The proof does not rely on finite enumeration. The independent optimization implementation checks 1,120 small-matrix instances, and the sparse radical identities were evaluated for 3,751 parameter triples; 19,865 assertions passed. The principal limitation is that nonsaturating general matrices do not receive an exact inradius.

## Originality (O): PASS, subject to historical priority review

Ferroni's inspected 15-page manuscript (arXiv:2609.10513v2) identifies the exact Cayley box fibers and the sparse matrices, but develops triangulations, smoothness, Ehrhart counts, and counterexamples rather than Euclidean inballs or optimal-center geometry. The general Nakajima/chimney theory cited there concerns triangulations. Search queries combining Cayley box sums, Nakajima polytopes, Euclidean inradius, center boxes, and saturation produced no matched statement. Related mathematical-record results describe center loci for different families and thus do not imply this row-by-row criterion. An accessible historical ledger was checked for the Cayley box object, metric claim, projection saturation, and related formulations; its closest records were Ehrhart-theoretic, not the new claim. No claim of proof of global uniqueness is made. The relevant chimney-polytope portion of the Haase–Paffenholz–Piechnik–Santos manuscript was also inspected; unindexed or unrelated metric-geometric work remains a residual risk.

## Mathematical value (V): PASS

This resolves a natural extremal geometry problem for the full box-Cayley construction introduced in recent work on smooth/IDP polytopes. The sharp iff criterion distinguishes exact saturation from strict undersaturation for arbitrary nonnegative matrices, and the complete center-locus description yields an explicit affine-dimension and facet-contact classification. In particular, all entrywise-positive integral examples have the *same* inscribed-ball radius regardless of the number and dimensions of the boxes, while Ferroni's sparse family has an isolated point-to-cube rigidity transition. This is a structural all-parameter result, not a numerical re-evaluation of an Ehrhart table or an arbitrarily selected finite instance.

## Limits and priority

The affine coordinate metric is essential; the result does not classify ellipsoids, nor the sub-saturation inradius. Historical priority is provisional and requires independent review. The computations are corroboration rather than an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
