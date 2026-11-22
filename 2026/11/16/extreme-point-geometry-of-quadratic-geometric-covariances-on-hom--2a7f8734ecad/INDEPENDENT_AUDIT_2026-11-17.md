# Independent mathematical audit

## correctness

PASS

From the adjacency recurrence on the (q+1)-regular tree, resolvent F_r(A)=(1-r²)/(1+qr²-rA) has entries r^d; r d/dr and r²/2 d²/dr² give d r^d and binom(d,2)r^d, respectively. Read source N formula and independently used symbolic differentiation to verify N/D³ for arbitrary formal q,r,a,b, with degree <=2. The full adjacency spectrum and positive continuous spectral density justify pointwise N>=0 iff all finite-support quadratic forms PSD, and absence of spectral atoms at finitely many zeros justifies strict positive definiteness on finite distinct sites. Normalization ∫ N D^-3 dμ=1 and injectivity from d=1,2 give affine bijection onto all normalized quadratics. The extreme-point classification exhausts nonnegative quadratics with double internal or endpoint zeros, two endpoint simple zeros, and decomposable single-simple-edge zeros. Independent exact SymPy checks confirmed both q=4,r=1/4 rational notches: (285/164,225/164) yields 1215/41984 lambda²; (195/236,-225/236) yields 3375/60416(16-lambda²). No critical/supercritical r claim is made.

## originality

PASS

The published first-order r^d(1+a d) sharp positive interval is included as b=0, while this two-parameter degree-two affine moment cone and continuum of arbitrary spectral double notches cannot be deduced from its first-order slice. Vergara supplies the general positive-definite radial kernel criterion, but the studied exact affine family, sharp extreme polynomial classification, and strict finite-site boundary behavior are not stated in the inspected general treatment. Universal geometry of positive quadratics is classical, credited as machinery, not novelty by itself.

## value

PASS

Motivated by natural polynomially weighted radial covariance families on regular trees; gives a complete, computable PSD parameter domain, exact extreme spectral notch designs and the distinction between vanishing continuous-frequency multipliers and finite-site Gram singularity. The full two-parameter extremal geometry is useful in covariance design and harmonic analysis rather than an unmotivated isolated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
