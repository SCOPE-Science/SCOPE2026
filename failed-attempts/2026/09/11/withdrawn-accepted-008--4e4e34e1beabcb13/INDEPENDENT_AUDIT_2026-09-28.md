# Independent Audit — 2026/09/11/008

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `6b4fcfdf67914a442cee990204f392f75ecbc0e7`  
**Audited current source tree:** `6b4fcfdf67914a442cee990204f392f75ecbc0e7`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS AS GEOMETRY. The elementary unfolding proof is sound: any path from a tetrahedron vertex to the opposite-face centroid must first meet the boundary of that face; the chord lower bound reduces the boundary minimization to an edge profile whose minimum is attained at an edge midpoint, and unfolding the adjacent side face and opposite face produces a minimizing segment of length 2/sqrt(3). Threefold symmetry gives the three edge-midpoint realizations. The Dirac embedding x↦delta_x is isometric for W2, so each base minimizing geodesic gives a W2 geodesic. Thus the mathematical construction itself is correct.

## Originality

FAIL. The central base-space claim is already covered by earlier literature. Itoh--Rouyer--Vilcu (2019, arXiv:1906.11965) states for the unit regular tetrahedron that the intrinsic diameter is 2/sqrt(3), realized between any vertex and the center of the opposite face, and its cut-locus lemmas identify the vertex cut locus as a Y-tree with geodesic multiplicity determined by the cut-locus branching. The same paper cites Rouyer (2003) for antipodes on the regular tetrahedron. Consequently the exact vertex-to-opposite-centroid distance and the three minimizing branches are not an original finding. The W2 statement for Dirac masses is then the immediate isometric Dirac lift, not an independent novelty rescue.

## Scientific value

FAIL AS A VALIDATED NEW RESEARCH FINDING. The argument is a clear self-contained rederivation and could be useful pedagogically, but the headline geometry is prior art and the Wasserstein lift is automatic once the base geodesics are known. The remaining midpoint-separation bounds are elementary refinements and are not enough to support the record's original novelty/value framing.

## Independent checks

- current main record tree SHA equals the assigned source-tree SHA
- independent edge-profile/unfolding derivation confirms distance 2/sqrt(3)
- open-access Itoh--Rouyer--Vilcu 2019 full text directly states the same antipodal vertex/opposite-face-center distance and supplies the cut-locus multiplicity framework

## Limitations

- I read the lawful open-access full text of Itoh--Rouyer--Vilcu (2019); I did not obtain the full text of Rouyer (2003) and rely only on its bibliographic/abstract-level role.
- The failure is an originality/value failure, not a claim that the submitted geometric proof is mathematically wrong.
- The audit does not attempt a complete historical priority survey beyond the decisive covering source.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/11/008
- https://arxiv.org/abs/1906.11965
- https://doi.org/10.1007/s00022-003-1617-y
- https://arxiv.org/abs/1508.03546

This audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
