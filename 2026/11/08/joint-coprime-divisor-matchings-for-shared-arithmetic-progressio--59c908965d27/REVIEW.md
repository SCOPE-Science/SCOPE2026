# Independent mathematical audit

## correctness

PASS

Uses the published Alekseyev–Beyer de Ryke matching criterion as a premise: for each p dividing n_i, at most tau(n_i)/(e_i+1) terms of the common progression may be divisible by p. For p not dividing b, a primitive pair determines one residue t0=-a b^(-1) mod p; the first pT_i positions contain T_i multiples, and the excess h_i=(e_i+1-p)_+ T_i forbids exactly min(p,h_i) initial residues. Across all n_i those forbidden sets are nested, yielding lambda_p=max_i min(p,h_i), not a product of marginal factors. Counting primitive nonzero residue-pairs gives factor 1-lambda_p/(p+1); CRT plus Möbius produces density 6/pi² times the finite local product and O_n(X log X). To get tuple averages, the subpopulation with e_i>=p but 0<h_i<p has zero density for fixed p because tau(cofactor)<p; union over p>P is bounded by sum p^-p. Hence regular inputs have obstruction p precisely when p^p divides some n_i and independence of divisibility mod finitely many prime powers gives J_k=prod_p[1+p(1-p^-p)^k]/(p+1). Strict J2>J1² follows from positive per-prime B-A²=p*p^(-2p)/(p+1)². Independently checked direct admissible progressions for (4,8) and (27,81) for a,b<=24; finite frequencies do not prove densities.

## originality

PASS

Earlier 2026 matching-criterion work and a separate single-input progression-density result cover the scalar marginal but not the all-tuple same-parameter local maximum, J_k law or J2 correlation in the inspected material. This is a new joint probability object rather than rediscovery of individual matchability.

## value

PASS

The same primitive progression is a genuinely shared arithmetic random input: nested obstructions produce a max rule and positive correlations instead of the naive product of single-set matching probabilities. An exact all-order joint Euler product and two explicit same-prime counterexamples are motivated dependence invariants useful beyond a single fixed-set census, while the deep matching criterion is acknowledged as prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
