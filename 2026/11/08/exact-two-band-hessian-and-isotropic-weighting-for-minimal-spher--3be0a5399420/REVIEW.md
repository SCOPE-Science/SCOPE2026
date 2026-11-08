# Self-review

## Correctness: PASS

The proof specifies the exact configuration space, two loss weights, Euclidean and Frobenius normalizations, and product-sphere Hessian convention. The global zeros are exactly regular simplices by a rank-and-Gram argument. The tangent decomposition into skew-symmetric rotations and traceless symmetric deformations has the correct total dimension, is injective, and is orthogonal; the further split into the \(d\)-dimensional vertex sector and its complement gives every Hessian eigenvalue and multiplicity. The two Jacobian norm ratios derive the asserted positive bands, so no additional zero eigenvalue is possible. Their difference factors as a nonzero scalar times \(a-4b/d\), proving the unique ratio. The separately formulated numerical Hessian implementation and symbolic checker completed 130 assertions. The proof, rather than the finite tests, establishes all integer dimensions \(d\ge3\).

## Originality: PASS, historical priority provisional

The standard facts about regular simplices and spherical two-designs are **not** claimed as new. Sloan and Womersley (2009) develop variational design criteria. Xiao and Zhuang (arXiv first posted 2023-03-09) develop general derivative/Hessian machinery for spherical-design optimization, but the accessible abstract contains no exact all-dimensional simplex spectrum or optimal relative weighting. The complete manuscript was not accessible through the attempted public routes, so its absence of an equivalent result was **not** verified; this remains the principal priority risk. Fu, Wang, and Yan (2022), checked through open full-text sections and proofs, optimize a different functional, \(\max_{v\in S^{d-1}}\sum_i |x_i\cdot v|\), which does not give the present weighted centroid-and-covariance Hessian. Scientific-semantic searches of related published mathematical results found no direct two-band or perfect-isotropy claim. An implicit older equivalent calculation remains possible and needs human literature confirmation before a publication-priority statement.

## Mathematical value: PASS

A minimal equal-weight spherical two-design is a fundamental quadrature configuration. Numerical design construction relies on minimizing nonlinear discrepancies, for which rotational zero modes and poor transverse conditioning are central. This result isolates **all** nonrotational stiffness modes, gives exact sharp local constants, and identifies the unique balance of degree-one and degree-two moment penalties that achieves the minimum possible transverse condition number, exactly one, in every dimension \(d\ge3\). The natural equal-weight choice exhibits a sharp dimension-four crossover. This is a motivated optimization property, not merely a different notation for the simplex design condition. It does not imply global convergence or conditioning for a different loss.

## Principal references and limitations

- Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365; DOI: 10.1137/22M1542362 (abstract and publisher metadata examined; complete text inaccessible).
- I. H. Sloan and R. S. Womersley, *A variational characterisation of spherical designs*, DOI: 10.1016/j.jat.2009.02.014 (abstract and bibliographic record examined).
- W. Fu, G. Wang, and J. Yan, *On the minimax spherical designs*, DOI: 10.1002/rsa.21087 (open full text, energy definition, theorem statements, and relevant proof sections inspected).

Self-review: passed. Independent audit: not yet performed.
