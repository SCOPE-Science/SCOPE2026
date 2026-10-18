# Independent mathematical audit

## correctness

FAIL

The claimed equality to the actual Li et al. q-FedAvg algorithm is false whenever curvature a != 1. Original Algorithm 1 (source PDF page 5, source page index 4) defines UNscaled Delta_w=x-bar_x and h_i=(q/L) F_i^(q-1)*Delta_w_i^2+F_i^q, whereas the package verifier sets Delta_w_i=L(x-bar_x), then uses h_i=q F_i^(q-1)*Delta_w_i^2+L F_i^q. With eta=1/a, L=a, exact client update bar_x_i=+/-b makes the real Delta_w_i=x-/+b, not a(x-/+b). Algebra gives the REAL source map T_src(x)=x-[sum_i d_i |d_i|^(2q)]/[(1+2q/a^2) sum_i|d_i|^(2q)], d_i=x-b,x+b, while RESULT states denominator factor (1+2q). At a=2,b=1,q=1/2,x=1/2, client losses are 1/4 and 9/4, source numerator=2, denominator=5/2, so x_new=1/2-4/5=-3/10, not 0. Thus unique one-round deadbeat q=1/2 for every a>0 is false; the claimed Newton equivalence and cubic local convergence are also false (true linear derivative is 1-(1+2q)/(1+2q/a^2), nonzero for a != 1). This is a falsifying admissible explicit counterexample, not a numerical approximation or verifier timeout.

## originality

FAIL

The main claimed dynamical phenomenon is not a true statement about the source algorithm; no new correct theorem as stated survives to be assessed as an original mathematical result. Independent model-code novelty is irrelevant to validity.

## value

FAIL

Identifying exact communication-round dynamics is a motivated question, but this final claim asserts a source-algorithm exact Newton identification that fails for a=2, so the advertised unique fairness-exponent deadbeat and cubic phenomenon do not constitute a valid mathematical finding. A different rescaled algorithm with a=1 could be studied separately; that does not salvage the false universal a>0 claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
