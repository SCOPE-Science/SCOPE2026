# Independent mathematical audit

## correctness

PASS

The scale products satisfy r_n~C n^-3 since the logarithmic drift remainder is summable. Finite-interval gambler's ruin followed by the upper endpoint tending to infinity gives h(n)=S_n/S_0, so h(1)<1 and the chain is transient. A separate occupation check proves the conditional divergence: for the original chain killed at zero, reversible weights with w_0=1 are w_n=1/(p_n r_n), and its Green function satisfies G(1,n)=w_n h(n). Indeed q_1 G(1,1)=h(1), and for n>=1 the chance to reach 1 is h(n)/h(1); apply reversibility. Conditioning multiplies G(1,n) by h(n)/h(1). Hence E_1[H_0 | H_0<infinity] is the sum of w_n h(n)^2/h(1), whose summands are asymptotic to a positive constant times 1/n. The deterministic first step from zero adds one. This confirms the frozen transformed-drift and telescoping proof without relying on the finite example.

## originality

FAIL

Lo–Menshikov–Wade's strict-inequality theorem does exclude this boundary, but an existing stronger exact first-return law covers the frozen nearest-neighbor claim by direct substitution after conditioning. For the Doob chain reset to step from 0 to 1, h(n)=S_n/S_0~c n^-2 and the transformed scale product is r_n^h=r_n h(0)h(1)/(h(n)h(n+1))~c' n. Its drift is -1/(2n)+o(1/n), it is recurrent by the conditioning identity, and uniform ellipticity follows from its transition limits 1/2 and strict positivity at the finitely many small states. Thus Alexander's Bessel-like hypotheses hold with delta=1, kappa=1. Equation (2.5) gives a positive finite limit for L(n) from r_n^h~c'n. Theorem 2.1, equation (2.7), yields the stronger conditional return tail ~c''/n, which immediately implies the claimed infinite conditional mean. This is verified coverage via a reduction, not an accusation about historical priority.

## value

FAIL

The general strong-transience equality is a meaningful problem, and the nearest-neighbor scale proof is pedagogically useful. The frozen first-moment assertion nonetheless gives only the divergent-mean consequence of a stronger known first-return theorem in exactly the transformed class. It leaves no new boundary behavior beyond a standard exact nearest-neighbor reduction and harmonic-series divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
