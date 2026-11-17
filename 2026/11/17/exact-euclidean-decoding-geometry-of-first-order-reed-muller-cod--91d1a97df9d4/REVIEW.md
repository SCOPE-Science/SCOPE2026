# Self-review

## Correctness — PASS

The exact identity \(P_m=\mathbf1/2-HB_1^n/2\) and orthogonality \(H^{\mathsf T}H=nI\) reduce the claimed projection to Euclidean projection onto the unit \(\ell_1\) ball. The soft-threshold KKT conditions give a unique optimum for every real input, and the residual norm gives the stated squared-distance formula. At binary inputs Parseval and Cauchy–Schwarz yield the cube-wide bound; explicit quadratic bent functions saturate it for every even \(m\). Equality forces Walsh flatness, while distinct bent vertices have distinct projection residuals, excluding nonvertex maxima. The facet claim uses strict positivity of every thresholded Walsh coordinate in bent cases. The exact checker exhausts 16, 256, and 65,536 binary input tables and independently confirms KKT conditions. The only unproved extension is the exact odd-\(m\) Hausdorff maximum, which is explicitly excluded.

## Originality — PASS (priority provisional)

Searches covered affine-codeword and Hadamard cross-polytopes, Euclidean nearest convex mixtures, Walsh thresholds, cubical deep holes, bent functions, and both current published records and accessible same-family claims. Ziegler's known cross-polytope realization is explicitly credited; Oblaukhov addresses discrete Hamming metric complements; Potapov addresses Walsh spectra and bent counts. The closest published affine-codebook random-access theorem has a coordinatewise worst-success objective. It coincides with the Euclidean projection mixture on bent inputs, but does not supply the projection formula or residual/nearest-face classification for all real inputs. No exact convex Euclidean decoding formula or entire-cube Hausdorff/extremizer classification was located. The ingredients are classical, so an equivalent result under alternative terminology remains a concrete priority risk.

## Mathematical value — PASS

The Euclidean distance from the full cube to a canonical, full-dimensional error-correcting-code polytope measures the loss incurred by convexifying discrete codewords. The theorem computes that invariant for an infinite family; moreover it supplies the exact nearest-face map for every received real vector and a sharp geometric characterization of deep holes as bent vertices projecting onto facets. It separates convex Euclidean decoding from known Hamming covering-radius statements and identifies the face dimension of all maximizers. This is a natural geometric invariant and complete projection law, not a renamed Hamming covering radius or an arbitrary finite slice.

## Closest literature and limitations

Oblaukhov (2019 preprint), Potapov (2023 preprint), Ziegler (2001 Hadamard-polytope geometry), and published affine random-access record 7628acdda7d2 were compared at the level of objectives and mathematical implications. Earlier equivalent convex-geometric work is possible. The exact Hausdorff value for odd Boolean dimensions is not established. Independent priority and proof validation remain desirable.

Self-review: passed. Independent audit: not yet performed.
