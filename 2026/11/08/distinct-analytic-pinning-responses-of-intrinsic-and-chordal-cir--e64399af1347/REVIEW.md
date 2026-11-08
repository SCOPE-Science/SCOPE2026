# Self-review

## Correctness — PASS

The claim is confined to two explicitly defined maps on circular Voronoi cells, with fixed von Mises mean direction and ordered angular lifts. At zero concentration the exact Jacobian is \(J_0=I/2+(S+S^{-1})/4\). On reflection-odd perturbations the constant rotation mode disappears, making \(I-J_0\) invertible; the analytic implicit-function theorem gives locally unique pinned fixed branches and attraction within that subspace. Direct integral differentiation gives the intrinsic coefficient \((\sin L/L-\cos L)/\sin^2 L\) and chordal coefficient \((L-\sin L\cos L)/(2\sin^3 L)\). The strict ordering has an explicit positive second-derivative proof. The exact paired-weight identity makes every regular polygon nonfixed for positive concentration. The supplied standard-library checker corroborates representative cases; the proof, not numerical sampling, handles all integers \(n\ge3\) and positive concentrations in the nonfixed conclusion.

## Originality — PASS (best available source comparison)

The 2026-02-12 paper arXiv:2602.11926v1 already gives the general nonuniform intrinsic centroid condition, a chordal Lloyd algorithm and numerical seven-point von Mises comparisons. The 2026-05-28 dynamics paper arXiv:2605.29451v1 already gives a circular Lloyd map and Fourier linearization, while treating equally spaced polygons as fixed at positive concentration. This result is **not** an uncredited rediscovery of different centroid definitions or qualitative codepoint deformation: it provides two all-finite-\(n\) analytic near-uniform pinned fixed branches, their explicit different response coefficients and a global-in-concentration regular-polygon obstruction. The relevant primary sections and appendices were examined for these exact conclusions; targeted equivalent-formulation and stronger-coverage searches yielded no matching theorem. Search absence is not a uniqueness proof, and historical priority remains provisional.

## Mathematical value — PASS

A recent discrete dynamical analysis makes stability assertions at regularly spaced von Mises codebooks, while another study supplies only implicit optimality conditions and numerical metric comparisons. This proof separates the two update conventions and replaces the assumed nonuniform fixed polygon by a rigorously constructed pinned branch. The exact response and strict metric ordering hold for **every finite number of cells**, beyond high-resolution asymptotics, and provide a computable starting configuration for stability analysis. The result is a structural dynamical correction, not a routine arbitrary numerical instance.

## Closest literature and limitations

- Saha–Jha–Roychowdhury, arXiv:2602.11926v1, sections on geodesic centroids, chordal centroid conditions, and numerical von Mises seven-point codebooks: qualitative metric differences already known; all-finite-\(n\) first-order coefficients not provided in inspected text.
- Saha–Jha–Roychowdhury, arXiv:2605.29451v1, Definition 2.8, Proposition 3.4, sections 4–5: motivates Lloyd dynamical stability, but its equally spaced assumption with fixed nonuniform weight is not valid beyond the reference cell.
- Roychowdhury, *Mathematics* 14 (2026), 63: broader spherical quantization background; no matching finite-\(n\) von Mises response.

Only local reflection-symmetric branch attraction is proved. The nonfixed regular-polygon result has no small-concentration restriction. Global optimality and full-space stability remain unproved. Further historical-source comparison and independent scientific review remain necessary.

Self-review: passed. Independent audit: not yet performed.
