# Independent mathematical audit

## correctness

PASS

Represent an exact-degree-two spherical harmonic on S^(2m-1) (m>=2) by a complex symmetric trace-free matrix. The decomposition into scalar |x|^2-|y|^2 (dimension 1), x-traceless and y-traceless (each (m-1)(m+2)/2), and mixed bilinear (dimension m^2) diagonalizes the normalized ambient-to-product-sphere Gram ratio. Direct fourth-moment contractions give squared singular values 4(m+1)(t-1/2)^2, 4(m+1)t^2/(m+2), 4(m+1)(1-t)^2/(m+2), and 4(m+1)t(1-t)/m. At t=1/2 exactly the scalar mode vanishes. On 0<t<1/2 the smallest band is min(lambda_Z,lambda_X), crossing once at t0=sqrt(m+2)/[2(1+sqrt(m+2))]; all competing max/min ratios decrease before and increase after that crossing. Thus kappa_min=1+2/sqrt(m+2), only at t0 and 1-t0, with maximal min eigenvalue (m+1)/(1+sqrt(m+2))^2 at those t. Independent numerical evaluation checked spectral ordering and kappa for m=2,3,4,9, including m=2 t=1/3 and kappa=2. The supplied checker is based on degree-four-exact rational cubature and its implementation was read; analytic invariance and inequalities establish all dimensions.

## originality

PASS

The earlier Clifford torus paper studies the balanced torus t=1/2 in S^3, a harmonic degree cutoff, its Fourier-diamond trace range and inverse instability; that trace is in fact singular on exact degree-two input. It neither quantifies the t-dependent four-sector spectrum for arbitrary m nor the two optimum imbalanced radii. General full-sphere random harmonic sampling and spherical low-coherence matrices do not yield this restricted continuous product-hypersurface optimization. Historical isoparametric-product-sphere literature could contain equivalent spectral decompositions; no complete priority guarantee is possible.

## value

PASS

Restrictions of harmonics to codimension-one product spheres are canonical sampling/trace operators. Their exact singular values locate a rank-loss singular hypersurface and give a sharp globally best conditioning and least-eigenvalue design among all radii for every m>=2. The optimum is a precise reusable stability constant and geometric design parameter, not just a finite check or a textbook normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
