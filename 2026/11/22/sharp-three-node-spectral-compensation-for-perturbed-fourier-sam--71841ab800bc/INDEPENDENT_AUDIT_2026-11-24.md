# Independent mathematical audit

## correctness

PASS

Conjugating the derivative by the normalized Fourier matrix gives the node term i[C,diag(ε)] with C=F*diag(0,1,2)F, and the weight term 3diag(ζ). The displayed diagonal phase makes the node term B(u)/√3 with the three positive off-diagonal entries u/√3, 1/√3, (1−u)/√3. At zero jitter the Gram norm defect is max|3v_j−1|. The uniform candidate has O(t) error, the expansion in the weight simplex is uniform, and the fixed trace bounds the norm by twice the half-spread. Thus all first-order near-minimizers have bounded scaled weight offsets; compactness and strictly positive realizations of each fixed tangent justify minimizing after reduction. The uniform Rayleigh quotient of the rescaled matrix is 4/3, and equality in operator norm forces the uniform vector to be an eigenvector. The unique balanced diagonal then gives the two remaining eigenvalues −2/3±√(1−3u(1−u)); the negative extreme reaches the norm bound at the two stated closed endpoints. Coercivity excludes another limiting attainment outside the interval. At u=1/2 reflection averaging reduces half-spread to diagonals (a,−2a,a); the minimum is at the crossing a=1/4 of the odd eigenvalue with the lower even eigenvalue. This gives the displayed half-spread and the opposite tangent, without needing to classify nonsymmetric minimizers. The unweighted and two optimized spectra give the three squared Frobenius values. At two nodes, the node derivative is off-diagonal in the Fourier basis and a traceless diagonal adjustment changes the two eigenvalues to ±√(a²+|b|²), so does not help either objective; one node is trivial. The three-node strict improvement witness is therefore minimal. The bundled verify.py was inspected, not executed.

## originality

PASS

The supported contribution is the minimal three-node witness, sharp operator-norm equality window and exact difference of operator and half-spread optima in the symmetric example. The general possibility of improving half-spread at the expense of Frobenius error is credited to the four-node precedent. The closest indexed results and attributed literature statements do not establish prior coverage of the narrower finding; the decisive full-text access limits are retained below.

## value

PASS

Minimal dimension and a closed sharp equality window are informative for deciding when normalized positive reweighting improves a perturbed sampling design. The opposite corrections at symmetric motion give an exact warning that optimizing distance to identity, first-order conditioning, or Frobenius defect leads to genuinely different choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
