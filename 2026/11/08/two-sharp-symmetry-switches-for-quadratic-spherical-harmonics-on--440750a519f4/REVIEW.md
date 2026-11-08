# Scientific review

## Correctness — PASS

The claim concerns one precisely defined finite-dimensional concentration operator, and the proof spans its entire harmonic quadratic domain by five symmetry sectors (the even axial sector is a two-by-two block). Full-sphere orthogonality, beta moments for the axial radius, and angular moments through frequency four yield the asserted blocks with their multiplicities. The two extremal comparisons reduce to explicit signs, whose unique zeros are the claimed cosine thresholds. Strict positivity and the small-aperture condition-number constant follow without relying on numerical experiments. A separately implemented cubature checker constructs the **full generalized Gram problem** separately for 30 dimension/aperture combinations, obtains the eigenvalues without using the proposed blocks, and verifies both crossing multiplicities; it reports `LUNE_QUADRATIC_CUBATURE_CHECKS_PASS 656`. The calculation and the proof apply to the complex harmonic space because the underlying real-symmetric matrices also diagonalize its complexification.

## Originality — PASS (provisional)

Michel, Plattner and Seibert (arXiv:2103.14650, sections 3.1–3.3) formulate the general spherical Slepian matrix and provide commuting operators for **caps** in ordinary three-dimensional space. Aslam and Khalid (arXiv:2010.07266, sections II-D and III) analyze general-region spherical Slepian matrices and associated transforms on \(S^2\). These sources establish the general concentration framework; they do not state the exact spectrum of pure quadratic modes on a lune for arbitrary \(d\ge3\), nor the two distinct sharp maximizing/minimizing crossings. Thus the present closed classification is not presented as new Slepian machinery, but as explicit spectral and optimizer information not supplied by these statements. Searches for lune, wedge, intersection-of-hemispheres, and quadrupolar aliases found no decisive equivalent closed theorem. Roddy and McEwen (arXiv:2106.02023) was identified as relevant, but its full PDF could not be inspected; only the abstract and metadata were accessible. Earlier geometric or harmonic spectral literature may contain an implicit special case. Priority is therefore provisional rather than independently certified.

## Mathematical value — PASS

A spherical lune is a natural non-axisymmetric observation region, already relevant in regional harmonic reconstruction. The theorem determines all singular values and symmetry sectors exactly in every dimension, not merely a sampling or perturbative approximation. The two distinct angular thresholds show that the optimally observable and least observable quadratic modes switch in different ways; the condition-number asymptotic quantifies the sharp inverse-aperture stability loss. These features explain the behavior of a natural, complete small-degree reconstruction problem and are not just a relabeling of a standard eigenvalue bound.

## Limits and closest coverage

The source papers' general-region matrix formulas could be specialized to the current problem by a further calculation; no claim is made that regional concentration or its Gramian representation is new. No full-text comparison with every classical spherical-lune result has been established, and the uninspected Roddy–McEwen full text remains an access limitation. The proof concerns pure degree-two scalar harmonics, a continuous lune of aperture strictly between zero and \(\pi\), and exact measurements; it neither treats arbitrary cutouts nor finite noisy samples. Numerical checks are corroboration, not a proof for untested dimensions. Independent mathematical review has not occurred.

Self-review: passed. Independent audit: not yet performed.
