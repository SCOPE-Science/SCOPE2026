# Review: singular geometry of a truncated Grassmannian

## Correctness — PASS

The local chart is proved by a direct change of Plücker coordinates, not a tangent-cone approximation: after four explicitly recoverable free coordinates are removed, the remaining ring is the prime ring of \(2\times2\) minors of a \(2\times4\) matrix. The six minors vanish symbolically and their vanishing ideal is the closure of the parametrization \(y=cx\). Group transitivity covers the full singular stratum. Outside the degree-two-coordinate charts the Plücker quadratic equations give a regular inverse to projection. The multiplicity follows from the Segre Hilbert series; the degree follows from the blow-up intersection formula. The provided exact-arithmetic verifier rechecks the nonstandard coordinate identities. Risks: the global smoothness argument depends on standard Plücker line classification and the fact that quadrics generate the Grassmannian ideal; both are used with explicit hypotheses.

## Originality — PASS, provisional historical assessment

The primary motivating article by Feigin–Makhlin and Feigin's earlier full-text article introduce these truncated varieties and their general coordinate rings and resolutions, but do not state the exact singular locus or transverse local type of this projected ninefold. The closest same-shape record involves a three-camera multiview fourfold rather than this Grassmannian, so neither its geometry nor its multiplicity implies the claim. The 2025 quantum-chemistry paper lists degree \(41\) for a different tenfold; it is not the claimed ninefold. The 2020 Grassmannian-projection paper studies centers disjoint from the Grassmannian, unlike the present base point. Exact research-record and literature searches did not reveal an equivalent result. General determinantal facts are credited. Residual risk: unpublished or implicit treatment in classical projection literature.

## Value — PASS

The projected ninefold is the smallest nontrivial intermediate truncated Grassmannian in the balanced three-by-three setting. The complete singular-stratum identification, uniform Zariski transverse model, and local multiplicity distinguish its intrinsic singular geometry from the combinatorial coordinate-ring descriptions, and provide natural input for its resolution and intersection-theoretic study. This is a classification of a canonical object, not an arbitrary finite slice or solely a computation of an already named invariant.

## Boundaries and sources

The result is limited to complex dimension parameters \((d,n,r)=(3,6,2)\). It does not compute other truncations, global intersection cohomology, or full syzygies. Primary sources: arXiv:2610.40891v1 and arXiv:2604.00751v2. Contrasts: arXiv:2004.10070 and Faulstich–Sturmfels–Sverrisdóttir, DOI 10.1007/s10208-024-09657-8. Determinantal normality and Cohen–Macaulayness are classical.

Self-review: passed. Independent audit: not yet performed.
