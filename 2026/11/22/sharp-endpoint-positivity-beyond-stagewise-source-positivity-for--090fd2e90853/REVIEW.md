# Independent mathematical audit

## correctness

PASS

Ordinary matrix powers preserve the eigenbasis of a symmetric input, so this is exactly a scalar question on [0,1]. The scalar endpoints are fixed. For 0<x<1 let u=x² and a=1+h(1-u)>1. Substitution gives 2z_h(x)(1-u)/x=1+a²-u(1+a+a⁴-a³). The denominator minus the numerator in the resulting zero formula for u is a(a-1)²(a+1)>0, so the parametrization is reversible and covers all interior zeros at positive h. The crossing function is G(a)=a-1+(a²+1)/(a(a²-1)). Its derivative has the sign of a⁴-4a²+1 on a>1, so it has one minimum at sqrt(2+sqrt(3)). There a-1/a=sqrt(2) and (a²+1)/(a²-1)=sqrt(3), yielding G(a)=2sqrt(2)-1. Continuity from h=0 gives positivity below the first crossing and nonnegativity at it; uniqueness of the minimizing a yields the sole interior zero at equality. At fixed u the quartic coefficients in descending h have signs -,-,ambiguous,+,+, with any zero coefficient omitted. Descartes' rule and the negative leading coefficient give one positive root, with strict negativity thereafter. Applying it at the critical input proves the same witness for every h above the frontier. Independently y>=0 and y-1=(1-x)(hx(1+x)-1); the supremum of x(1+x) as x approaches 1 from below is 2, giving the universal source threshold 1/2 including equality. These arguments address all matrix dimensions without a numerical search.

## originality

PASS

The sharp completed-step threshold and fixed failure witness for the stated nonlinear PSD problem are distinct from the inspected positive-source and forward-Euler-based sufficient restrictions. The same Heun formula and cubic reaction have prior uses; the record appropriately makes no novelty claim on the method or reaction. Related SCOPE positivity results have different linear operators, conditions or algorithms. This is a bounded comparison; unavailable articles were not treated as negative evidence.

## value

PASS

The calculation answers a natural sharpness question about sufficient stagewise conditions for standard second-order time stepping. The substantial separation from 1/2, the exact interior extremizer, and the fixed failure witness quantify a practical and structural distinction that a sufficient SSP bound does not capture. It is not presented as an invariant-domain or general SSP theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
