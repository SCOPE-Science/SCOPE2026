# Independent mathematical audit

## correctness

PASS

Gaussian/Hermite STFT energy for radial binary masks integrates to λ_j=(1/j!)∫_E t^j exp(-t) dt with t=π|z|². For E,F unions of ≤m intervals, 1_E−1_F has ≤2m nonzero alternating sign-runs; a polynomial of degree ≤2m−1 with zeros between opposite runs has strictly signed weighted integral, contradicting equality of the 2m moments unless E=F. For exactly m intervals the endpoint derivative matrix is sign times weighted Vandermonde; determinant (-1)^m exp(-∑x_i)∏_(i<k)(x_k−x_i)/∏j! is nonzero. Dropping a row yields rank 2m−1 and analytic one-dimensional equal-moment fibers, proving necessity. Lagrange inversion gives the stated linear noise sensitivity, not a global noise guarantee. Independent m=2 endpoints (.3,1.1,2,3.7) determinant 0.00126476703225768 matches formula. Infinite uniqueness is the sign-change proof, not a finite test.

## originality

PASS

Best-of-knowledge original quantitative conclusion after matching exact objects, normalizations and implication checks. General piecewise D-finite moment inversion contains the problem class but not clearly the sharp fixed-sign minimal first-2m e^-t moments. The indicator sign-run argument derives uniqueness and exact local minimality with tied endpoint weights, not arbitrary weighted-spike inversion.

## value

PASS

Identifiability of binary radial Gabor masks from labelled Hermite-mode observations is a natural finite inverse spectral problem. The sharp 2m threshold, all-mask uniqueness, one-dimensional ambiguity below threshold and explicit local Jacobian quantify measurement burden and instability; broader weighted spike theory does not mechanically give these exact Hermite observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
