# Independent mathematical audit

## correctness

PASS

The first-order relaxation with known baseline discretely switched to a common positive contrast yields d_i/lambda_i = integral of Delta*1_[a,b](s) times exp(-lambda_i*s). Two distinct positive pulses differ on a set of positive measure and have at most two sign transitions ignoring zeros: nested intervals can have a +-+ pattern, and disjoint or crossing intervals have at most one. Endpoint conventions do not affect integrals. Any nonzero combination of k distinct exponentials has at most k-1 real zeros counted with multiplicity by division by one exponential and Rolle induction. Imposing zeros at the transition locations therefore produces a sign-matching test function from the first r+1 exponentials for r transitions. Its integral against the difference is strictly positive, contradicting equality of all three Laplace samples. With two distinct rates, every sufficiently small perturbation of L=b-a preserves feasibility after solving a=(log((1-exp(-lambda2*L))/(1-exp(-lambda1*L)))-log(d2/d1))/(lambda2-lambda1), then setting Delta=d1*exp(lambda1*a)/(1-exp(-lambda1*L)); duplicated readings add no information. For harmonic rates, division by d1 gives R=u+v and S=u^2+uv+v^2, hence K=(u-v)^2 and the stated open inequalities characterize exactly the feasible data. In the Jacobian in (Delta,u,v), remove Delta and -Delta from columns two and three, replace column two by its difference from column three, and subtract (u-v) times column three from column one. The resulting columns yield (u-v)^4 before multiplying back -Delta^2. The logarithmic change of variables contributes gamma^2*u*v, and u-v is asymptotic to u*gamma*(b-a) for fixed a and gamma, giving the displayed quartic decay at fixed positive contrast. The exact scope does not establish noise robustness or empirical validity of the shared contrast.

## originality

FAIL

The arbitrary-rate injectivity claimed as the mathematical addition is directly covered by the classical Laplace sign-variation bound, explicitly stated in Bhaskar and Song (2014), Theorem 4, adapted there from Jameson. For these pulses, a nonzero difference has at most two sign changes and its compactly supported Laplace transform would have three distinct positive zeros if the data matched. This is precisely the prior theorem's conclusion with at most two zeros, not a mere analogy or a method requiring new theory. Necessity of three locally identifying readings is also immediate from the open three-dimensional parameter domain and invariance of domain (pad a map into R^2 by a zero coordinate), with the frozen proof giving an explicit fiber. The isotope interpretation is useful but does not change the mathematical inverse problem. Harmonic inversion is expressly illustrative and substantially overlaps explicit catalogue formulas. The failure is based on demonstrated prior mathematical implication, not on inaccessible ecology papers or a same-day priority assumption.

## value

PASS

The exact three-versus-two measurement threshold has a concrete interpretation for sampling a temporary dietary excursion with a common unknown contrast, and the harmonic determinant marks a degeneracy at short durations. These are useful model-design facts when the assumptions hold. That usefulness does not establish a distinct mathematical contribution given the direct prior implication, nor does it validate the assumptions in real tissues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
