# Independent mathematical audit

## correctness

PASS

At b>0, a>2sqrt(b), r=(a-sqrt(a²-4b))/2>0 is the lower equilibrium with ar=r²+b and a>2r; det of the Jacobian at (r,r²) is eps*r*(2r-a)<0. The backward left stable branch stays in 0<x<r,mu>r² since xdot>0 and mudot=-eps(mu+b-ax)<0 there; it cannot blow up at finite backward time and reaches every higher horizontal section exactly once. Inverse graph ODE bounds 0<=mu_eps(eta)-r²<=a eps/r log(r/eta). Along fixed section, log derivative gives -eps log x(mu0) as integral of (mu-x²)/(mu+b-ax), whose difference from mu/(mu+b) is O(eta) uniformly on x<=eta; first eps->0 then eta->0 gives action integral [mu-r²-b log((mu+b)/(r²+b))]. Subtracting two fixed-section limits cancels the lower endpoint and a-dependent r, giving independent-of-a attenuation. Independent numerical stable-branch integrations at eps=.12,.05,.02 show convergence of action at mu=2,5 for a=3,b=2; only analytical argument proves limit.

## originality

PASS

Best-of-knowledge PASS for explicit fixed-section exponent and feedback-independent relative section rate of this adaptive pitchfork. The same-model prior article constructs exponential singular basin funnels but does not state this exact closed action and section ratio, based on reading the main text and supplement; general entry-exit integrals are method precedent, not the displayed model-specific law.

## value

PASS

For the actual positive-saddle basin boundary of an adaptive pitchfork, the logarithmic action is an exact, parameter-resolved natural observable quantifying exponential funnel sensitivity. The section-to-section a-independence is a meaningful structural cancellation; the stable-branch existence and order of limits distinguish it from a trivial one-line linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
