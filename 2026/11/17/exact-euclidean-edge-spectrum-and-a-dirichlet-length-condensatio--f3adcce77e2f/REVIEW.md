# Scientific review: exact Euclidean edge spectrum of Loday associahedra

## Correctness — PASS
The exact domain is the unscaled canonical embedding with N>=3 ordered leaves. All edges correspond to uniquely oriented Tamari right rotations. The local coordinate difference consists of (+ac,-ac), a known fact verified independently from the coordinates. Catalan tree contexts prove the exact joint outer-size multiplicity, and the differentiated Catalan generating series yields the exact summed length. A pointwise probability limit of total mass one proves the microscopic product-Catalan law. A uniform Stirling estimate plus boundary-strip bound establishes the macroscopic Dirichlet weak limit without assuming boundary mass is negligible. The included Python checker enumerates every such edge for 3 through 8 leaves and verifies all discrete formulas. All-dimensional claims depend on the written analytic proof, not the finite checks.

## Originality — PASS, priority provisional
Loday's original Section 2.10 **already proves the local edge-length formula and maximum**; these are used and credited, not newly claimed. The aggregate integer sequence matches OEIS A000531, so the numerical values alone are not novel. The new assessed statement is the complete two-parameter multiplicity formula and its two contrasting edge-sampling laws, including the length-biased Dirichlet limit. The 2023 survey and inspected related realization literature provide the polytope, coordinate and combinatorial context, without stating that joint distributional result. A publicly indexed graph-associahedron braid-wall theorem has a different graph-distance pair count. Residual historical risks include unindexed Catalan rotation fringe laws and related work not exhaustively inspected.

## Mathematical value — PASS
The two canonical sampling procedures on the same geometric 1-skeleton have radically different scales: typical edges remain microscopically short in distribution, while total edge length is carried by macroscopic rotations and has an explicit three-part limiting density. This is a natural, reproducible complete metric spectrum and a motivated sampling phenomenon, rather than a cosmetic generalization of an existing local formula or the recognition of a pre-existing integer sequence.

## Sources and limits
Primary geometric sources: Loday, *Realization of the Stasheff polytope*, arXiv:math/0212126, §§1,2.9–2.10; Pilaud, Santos and Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471v1; Padrol et al., *Associahedra for finite-type cluster algebras and minimal relations between g-vectors*, DOI:10.1112/plms.12543. Numerical sequence: OEIS A000531/A143019. All sampling and metric assertions refer to one fixed canonical Euclidean realization. Historical priority remains provisional, finite enumeration does not replace proof, and no external independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
