# Independent mathematical audit

## correctness

PASS

With u=sqrt(d), independent symbolic differentiation confirms 2sqrt(z)(1-u²z⁴)²F'(z)=Σ_{k=0}^3 a_k G_k(z). The strictly increasing h(z)=z/(1-z)-1/2-4u²z⁴/(1-u²z⁴) orders the four G_k zero crossings. The polynomial Wronskians -W(G0+uG2,G3), -W(G1,G3), -W(G2,G3) factor as stated; Q13,Q23 have positive u=1 lower bounds, and Q_A is strictly concave in u with positive endpoint bounds. For b≥u, -W(G0+aG1+bG2,G3)>0, hence H/G3 decreases from +infinity to -infinity on (0,r3), producing exactly one zero and hence a strict interior maximum. Four independent exact rational derivative-sign checks at z=1/2,3/5,3/4,9/10 give +,-,+,- for (d,a,b,c)=(49/50,1/1000,1/1000,73/100), hence at least three distinct critical points. The universal proof is analytic; the symbolic checks only corroborate identities.

## originality

PASS

The effective new statement is the free-middle-coefficient sufficient cone b>=sqrt(d), not previously known uniqueness for b=sqrt(d), together with analytically demonstrated non-unimodality when unconstrained. A published all-four-parameter three-zero ceiling reuses the same positive witness and removes novelty from that particular witness, but does not imply that all b>=sqrt(d) produce exactly one critical point. No inspected earlier covering theorem for the cone was found. This is best-of-knowledge, with a possible general total-positivity criterion remaining a risk.

## value

PASS

The geometric trial bound is a natural computable proxy for the numerical radius of a compact four-block shift. A nontrivial explicit sufficient uniqueness cone and a strictly positive counterexample outside it delimit optimizer geometry and rule out universal unimodality. It does not claim a sharp boundary or the operator numerical radius, but the analytic transition and obstruction have substantive standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
