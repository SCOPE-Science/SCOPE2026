# Independent mathematical audit

## correctness

PASS

For the normalized x''(t)=x(tau(t)) with nondecreasing tau<=t and tau(t)->infinity, the primary arXiv:2609.31732v1 source, Lemma 2.12 (equation 2.15), gives beta(a)=2a-2d+sqrt(2d^2+4/(rs)-2) on beta(a)>=2a. Because beta(0)=sqrt(2), this branch applies for all sufficiently small a>0. Its Corollary 2.8 defines positive analytic spectral roots r^2=exp(ar), s^2=exp(-as). Independently derived the principal Lambert-W expansions by Lagrange inversion and checked the defining spectral equations: d=1/s-1/r=a+a^3/6+2a^5/15+O(a^6), 1/(rs)=1-a^2/2-5a^4/24+O(a^6). Thus the exact radicand is 2-a^4/6+O(a^6) and beta(a)=sqrt(2)-a^3/3-(sqrt(2)/24)a^4+O(a^5) (also -4a^5/15). Vanishing first two right derivatives and third_right_derivative_beta_at_zero=-2 follow from real analyticity at zero. For b(a)=sqrt(2)-kappa*a^3+o(a^3), b-beta=(1/3-kappa)*a^3+o(a^3); fixed kappa<1/3 forbids eventually positive decreasing solutions by source Theorem 1.4, and fixed kappa>1/3 falls into a<=b<=beta(a) and source Theorem 2.15 constructs one tau for each sufficiently small a. No conclusion for equality kappa=1/3 from cubic term alone. These are local one-sided limits; source analytic branch and sharpness are used as assumptions rather than independently reproven.

## originality

FAIL

The same-object primary source arXiv:2609.31732v1 already supplies the complete exact analytic formula for beta(a) on a neighborhood of a=0 (Lemma 2.12, eq. 2.15), its Lambert-W spectral roots (Corollary 2.8), the necessary sharp bound (Theorem 1.4), and existence for all admissible (a,b) (Theorem 2.15). These stronger published statements directly imply the proposed endpoint Taylor coefficients by standard Lagrange-inversion/Taylor algebra and imply the fixed-kappa phase rule by sign comparison; the submitted proof uses precisely that deduction and introduces no new construction or theorem independent of it. The new explicit coefficient is not printed in the inspected source, but absence of matching wording or number does not establish novelty when the complete prior formula covers the entire local boundary. Search results (including Resultary self-match) found no separate predecessor but do not negate the decisive prior implication.

## value

PASS

The liminf-to-limsup sharp boundary is a mathematically motivated and operationally meaningful invariant; a=0 is its classical threshold corner. The cancellation of linear and quadratic terms gives an informative cubic scaling and coefficient 1/3 that supplies a quantitative sensitivity rule for nearby admissible delay data. This is a genuinely interpretable exact local fact, rather than an arbitrary parameter slice or mere negative type check, even though its deduction from a stronger published closed formula prevents a new originality claim. It does not purport to establish a new global sharp criterion, and no larger theorem is demanded for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
