# Scientific review: rare spherical obtuse triangles

## Correctness — PASS

The theorem explicitly fixes independent surface-area sampling and Euclidean chordal angles, and the proof verifies the sphere coordinate density and obtains the exact cap integral using the condition \((Y-X)\cdot(Z-X)<0\). The integration-by-parts cap bound, the strict unique saddle \(T=1/3\), Stirling's gamma ratio, and a localized Laplace expansion yield the stated constant \(27\sqrt6/(16\sqrt\pi)\) with relative \(O(d^{-1})\) error. The same localized density proves the conditional Gaussian law; the conditional spherical azimuth variance and endpoint concentration prove the limiting three dot products. Checks from the actual package include exact symbolic saddle identities, numerical quadrature, dimension-three and dimension-five exact benchmarks, conditional mean/variance trends and direct sphere simulations. Finite checks are diagnostics only; the analytical proof carries the quantifiers.

## Originality — PASS, with identified priority risk

The 2025 sphere-sampling study gives an exact beta-cap probability integral, which is acknowledged as the starting point, but its displayed high-dimensional treatment freezes the pair angle at its typical value and does not derive the rare-event saddle, its sharp prefactor, the conditional central limit theorem, or the limiting right-isosceles geometry. Obtaining these requires nonuniform large-deviation localization; the earlier integral alone is not a stated stronger asymptotic or conditional theorem. The 2013 sphere-angle study concerns pairwise central angles, and the 2015/1996 Gaussian triangle studies use a different point law. Search and statement comparisons did not identify matching published research records. Residual risk: the full 1996 publication was inaccessible, so historical exclusion is not absolute, and any exact integral can in principle be asymptotically analyzed.

## Mathematical value — PASS

The result identifies an exponentially rare geometric configuration whose conditional shape is sharply different from typical high-dimensional spherical triples. Both the rate \((16/27)^{d/2}\) and the conditional saddle \(1/3\) are needed: direct substitution of typical nearly orthogonal coordinates gives a different exponential scale. The probability prefactor, conditional Gaussian scale and full limiting side-length ratios provide falsifiable quantitative predictions and geometric explanation, rather than just a routine fixed-dimensional evaluation.

## Limits

The claims exclude volume-uniform and Gaussian point laws, do not cover growing samples, and give no explicit finite-dimensional error constant. Originality is a literature-based determination, not independent certification; the older plausible primary item was not available in full text.

Self-review: passed. Independent audit: not yet performed.
