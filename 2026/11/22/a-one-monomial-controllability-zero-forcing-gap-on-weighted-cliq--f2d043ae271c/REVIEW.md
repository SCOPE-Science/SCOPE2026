# Self-review

## Correctness — PASS

The claim covers every integer \(p,q\ge3\) and positive real \(a,b,t\). The proof constructs two interior clique-difference eigenspaces and one four-coordinate Jacobi quotient, explicitly factors the quotient characteristic polynomial at \(pa\) and \(qb\), and applies PBH to all eigenvalues. At \(pa=qb\) the exact compactly supported vector with two omitted nongateway values \(-1\) and both gateway values \(+1\) establishes the only extra obstruction. The selected-set classification and polynomial counting follow without limiting approximations. The packaged symbolic checker verifies the characteristic identities; the separate standard-library checker matches 3136 finite-field Krylov ranks to the theorem in varied resonant and nonresonant small networks. Finite checks are not substituted for the all-size proof.

## Originality — PASS with explicit publication-priority risk

The bridge-barbell zero-forcing polynomial and its \(p+q-3\) minimum are **known** and are not claimed as new. Those prior coefficients exactly match the resonant controllable-set polynomial. The new result identifies the full fixed-Laplacian actuator-set polynomial at all positive homogeneous clique and bridge conductances, the sharp spectral condition \(pa=qb\), and the unique one-monomial nonresonant correction. Yuan et al. give the general multiplicity/PBH framework, Monshizadeh et al. give the family-wide zero-forcing criterion, and Dai studies general undirected leader selection and explicit other graph classes. The closest indexed partial-matching-clique result assumes at least two cross-clique links, so its stated classification does not entail this single-bridge theorem. The exact older zero-forcing record and partial-matching record were accessible as indexed claims, not full manuscripts; those access limits and possible unpublished equivalences remain significant priority risks.

## Value — PASS

These densely connected two-community networks are a natural exact-control test family. The complete placement census shows a sharp one-actuator discontinuity across an explicit tunable spectral resonance, independent of the bridge strength, and identifies *exactly* when the much more robust graph zero-forcing test is also a necessary fixed-weight controllability test. The parameter law \(pa=qb\) explains why simply balancing clique sizes is not decisive when intracluster conductances differ; the four-vertex compact eigenvector provides a structural mechanism for the lost control direction. No control-energy improvements or applications beyond this exact setting are claimed.

## Closest literature and limitations

- Yuan et al., *Nature Communications* 4:2447 (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/ : full-text multiplicity/PBH criterion, not the present dedicated-input all-set census.
- Monshizadeh, Zhang and Camlibel, arXiv:1403.4868 (2014), https://arxiv.org/abs/1403.4868 : full six-page preprint, zero forcing equivalent to controllability throughout a qualitative matrix family, not equivalent to fixed Laplacian controllability.
- Dai, *IET Control Theory & Applications* (first public 2022), https://doi.org/10.1049/cth2.12385 : full text on minimum leader selection, not this parameter-dependent barbell census.
- *Zero forcing polynomial of bridge barbells* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-bridge-barbells--5431b532d7f2 : indexed exact formula acknowledged as prior; full text unavailable.
- *Exact minimum dedicated leader sets for cliques joined by a partial matching* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-minimum-dedicated-leader-sets-for-cliques-joined-by-a-part--7537ea98c09f : indexed scope has at least two matching bridges and equal clique sizes; full text unavailable.

The result says nothing about how much control energy is needed near resonance, nor about arbitrary intra-clique heterogeneity or additional bridges. A mathematically independent or exhaustive priority audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
