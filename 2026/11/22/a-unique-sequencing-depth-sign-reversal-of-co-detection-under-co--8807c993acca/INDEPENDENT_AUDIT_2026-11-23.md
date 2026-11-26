# Independent mathematical audit

## correctness

PASS

At an occupied site the one-detection probabilities are 1-u^n and 1-v^n, and the negative conditional covariance is w^n-(uv)^n. The covariance of the two conditional means is p(1-p)(1-u^n)(1-v^n). Adding these contributions with the conditional covariance weighted by p gives the exact positive-prefactor times (1-p-Theta(n)) factorization. Since uv-w=(1-u)(1-v)>0, the log derivative of Theta(t) after multiplying by (uv)^(-t) is delta/(exp(delta*t)-1) minus alpha/(1-exp(-alpha*t)) and beta/(1-exp(-beta*t)), with positive alpha=-log u, beta=-log v, delta=log(uv/w). The first term is below 1/t and each subtracted one above 1/t, giving strict decay. Theta(1)=1 and Theta tends to zero, so the threshold is unique, strictly increases from 1 with p, and diverges as p approaches 1. Dividing by (uv)^t gives a factor tending to 1; taking the logarithm yields the claimed additive o(1) error. The n=2 factorization gives p cutoff 2/[(1+u)(1+v)]; with u=2/3, v=1/2, w=1/6, p=4/5, exact arithmetic gives -8/75, 0 and positive for n=1, 2 and n>=3 respectively. Independent Poisson thinning makes conditional covariance zero and leaves strictly positive covariance of conditional means. The fixed-versus-Poisson comparison does not hold for arbitrary random depths; for instance equal probabilities of depth 1 and 2 in the witness give covariance -2/45. This is consistent with the explicit scope, which excludes other random-depth laws. The source checker and verification notes were inspected, not executed; the proof is analytic and real depth is only interpolation.

## originality

PASS

Best of current knowledge: the known multinomial indicator covariance and shared-occupancy mixture mechanism are starting points. The distinct contribution is the sharp all-depth negative-to-positive one-crossing law under this coupling, with an exact threshold, prevalence asymptotic and a scoped Poisson contrast. Closely related indexed sign-switch statements are not equivalent or broader coverage; direct full-text coverage of the cited eDNA model remains an access risk.

## value

PASS

A fixed read-budget artifact can produce a negative observed association even under perfect positive coupling. A unique, prevalence-dependent cutoff gives precise conditions under which observed covariance changes its qualitative interpretation, and the Poisson comparison separates two sampling designs. This is useful as an idealized benchmark or counterexample, not a field depth recommendation, causal inference, or a finite-sample guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
