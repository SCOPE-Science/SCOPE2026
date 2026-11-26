# Independent mathematical audit

## correctness

PASS

On Z=1 and the torus, t=-x^{n-1}y gives x^N=f(t)=(-1)^{n+1}t^n/(1-t) with the stated inverse y. The reciprocal polynomial is Eisenstein at t=1, so this dense torus part is integral geometrically, and no missing coordinate axis is a component. The three boundary coordinate vertices have nonzero linear terms. In the torus the change to x,t is étale, x^N has zero derivative, and f' has a unique simple zero at n/(n-1) since p∤n(n-1). The equation at that t has precisely M geometric roots. There p is odd, u=x^M-x_0^M is a transverse ambient coordinate and f-f(t_0) is a square of a formal change of parameter over the algebraic closure; the completed germ is v²=u^{p^e}. Its normalization k[[s]] via u=s², v=s^{p^e} has quotient dimension (p^e-1)/2 by the missing odd exponents below p^e (the delta invariant). In K=F_p(x,t), set w=x^{p^e}; in L=F_p(t,w) the valuation of w above t=1 is -1. Therefore K/L has degree p^e, and L=K^{p^e} since that Frobenius subfield has the same index and is contained in L. Frobenius identifies the two smooth models over F_p, not necessarily the coordinate projections identically. The valuations n,-1,1-n are all prime to M; tame Riemann–Hurwitz gives (M-1)/2, including M=1. The normalization is Frobenius-equivariant and bijective on geometric points by the computed single branches, so each extension point set and the zeta functions agree. Independent replay: python3 /workspace/branches/review_checks.py 3, seven prime-field direct plane-gradient checks and counts against the tame model, with cases e>1 and M>1. Frozen code and its recorded output were inspected, not executed.

## originality

FAIL

The earlier exact Klein/Hurwitz record 027b54346512 treats the same equation for all degrees and bad primes, with the full completed cusp types, count, delta and normalization genus, even adding the total Jacobian length. The passage of the classical explicit Kummer model to the tame model follows by the standard power-subfield operation and a monomial change, while the all-extension zeta equality follows immediately from the prior geometrically unibranch classification. These are genuine known coverage and direct implications, not negative evidence from an inaccessible paper.

## value

FAIL

A first classification of these singularities through arbitrary wild exponents would be mathematically useful; that classification already exists with even more local data. Applying standard Frobenius to the known Kummer equation and deducing point-count invariance from the known single branches adds no independent substantial invariant here. No new zeta numerator for M>1, arithmetic structure beyond the immediate bijection, or other substantively different theorem is proved in this frozen record, so no repair is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
