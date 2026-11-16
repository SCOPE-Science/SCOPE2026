# Mathematical review: sharp first-band Fourier hole radius

## Correctness — PASS
The claim covers every positive Borel probability measure on the two-torus annihilating the eight nonconstant characters of the first rectangular Fourier band. Compactness ensures a deepest-hole center exists. The witness \(H=\cos(2\pi x)\cos(2\pi y)+\tfrac12(\cos(2\pi x)+\cos(2\pi y))\) has exactly zero mean under the stated Fourier assumptions. Its complement-of-square sign estimate follows from two linear endpoint optimizations and has exactly three cosine-pair equality cases. Positivity then reduces an arbitrary measure to at most five explicit contact sites. First-harmonic sine, cosine and mass equations uniquely determine all their weights; the mixed moment of the resulting measure vanishes exactly. The same reasoning excludes any hole larger than the stated one. This is an infinite-dimensional proof, not a finite search.

A dependency-free checker independently evaluates the nine complex moment identities using exact arithmetic in \(\mathbb Q(i\sqrt2)\) and checks the contact formulas and endpoint inequalities. The finite checker does not substitute for the support argument.

## Originality — PASS relative to inspected primary sources
The first-band theorem supplies an exact **largest empty square** constant and determines every extremizing *measure*, even allowing arbitrary support size. Kunis (arXiv:2608.11915, August 12, 2026), especially Theorem 3.3 and Remark 3.4, establishes general degree-dependent upper bounds using sign-localized polynomials but does not determine this sharp first-band extremal configuration. Noskov–Schmid (2002) treats minimal node counts for a different, total-degree trigonometric exactness requirement. An equation with the present \(\arccos(-1/3)\) constant, the five-atom weights and a covering-radius rigidity conclusion was not found in the inspected literature; negative search alone has not been treated as proof of priority.

Risks remain from older multivariate moment-space, positive cubature and covering literature, including results indexed under alternative terminology. The present assessment does not assert independent verification or a definitive priority certificate.

## Mathematical value — PASS
The problem is the smallest genuinely multivariate case of a current positive-quadrature covering-radius question: how large may a spatial hole be while all prescribed low Fourier moments remain exact? The solution gives a sharp universal constant, an explicit attainable rule, and full structural rigidity across continuous and atomic measures. In contrast with a single numerical example or arbitrary cutoff, these three statements close a natural small-band extremal problem and expose a contact-polynomial mechanism potentially useful for larger spectra.

## Scope and limitations
The metric is wrap-around \(\ell^\infty\); the exactness set is the nine frequencies \(\{-1,0,1\}^2\). Neither Euclidean covering nor higher bands are treated. The five-node statement is rigidity among maximizers, not a minimum-node theorem for all exact rules. Results do not extend to signed weights by the present argument. Full bibliographic priority and mathematical validation by an independent party remain open.

Self-review: passed. Independent audit: not yet performed.
