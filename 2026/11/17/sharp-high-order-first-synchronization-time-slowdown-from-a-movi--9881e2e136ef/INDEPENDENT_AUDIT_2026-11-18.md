# Independent mathematical audit

## correctness

PASS

For g_d(u)=P(s-u)+Hu^(d-1)(1-u), differentiating yields g_d'=-P+H[(d-1)u^(d-2)(1-u)-u^(d-1)]<0, since (d-1)u^(d-2)(1-u)<=1 and H<P; g_d(s)>0 and g_d(1)<0 give a unique stable equilibrium u_d. Its root equation and maximum of u^(d-1)(1-u) first bound u_d-s=O(1/d), then O(q^(d-1)) for fixed q in (s,1), permitting asymptotic (u_d-s)/s^(d-1)→H(1-s)/P. Taylor expanding the moving squared-radius level yields its shift. Reciprocal velocity subtraction is pointwise positive for each d, with endpoint integral from u0 to fixed t giving D t^(d-1)/(d-1); the moving interval has length of order s^(d-1) and contributes C s^(d-1), dominating because t<s. The constants were checked against F0(t)=Pt(s-t), and boundary assumptions ensure positive target/denominators. Universal claims are rigorous real-variable asymptotics.

## originality

PASS

Biswas–Patra–Banerjee arxiv:2604.07707 derives this very Ott–Antonsen reduced equation, moving steady-state FST quadrature and qualitative numerical high-order slowdown: those ingredients and observations are prior, not new. Examined primary source does not give the signed large-d coefficient, the separate fixed-target acceleration rate, or their exponential-scale comparison. Pairwise stochastic synchronization-time literature is different.

## value

PASS

A precise asymptotic law resolves the physically motivated confusion that faster pointwise flow can yield slower arrival to an endogenous moving target, identifying both competing rates and crossover. The distinction is useful for comparing interaction order and synchronization metrics, not a generic unmotivated exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
