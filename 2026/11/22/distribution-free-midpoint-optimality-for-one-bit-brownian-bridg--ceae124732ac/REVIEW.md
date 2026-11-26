# Independent mathematical audit

## correctness

PASS

Symmetry makes the sign balanced with zero tie probability at each interior time, so the conditional mean is 1/2 + C(t)Y_t and the risk is 1/12 - C(t)^2 by the uniform occupation law. Conditional on a positive standardized bridge value z, the expected noisy sign at scale r is P(|N|<z/r) except on a Gaussian-null set, and equals 1 at r=0. This is nonincreasing in r and positive on a positive-measure tail for every finite r. Integrating it against the conditional Gaussian sign expectation gives a positive kernel for rho>0, strictly increasing on [0,1] in rho (it is zero at rho=0). In log-odds coordinates the correlation is exp(-|x-z|/2), and the time measure is an even logistic density strictly decreasing away from zero. Each centered-interval layer of the kernel gives a strictly decreasing shifted integral since w(z+v)<w(z-v) for z,v>0. Its nonzero positive mixture is also strictly decreasing. Applying the fixed scale r(1/2) to every candidate is an upper bound for C(t) because the standardized scale has a global midpoint minimum; this proves uniqueness even for atomic noise and discontinuous scales. For Gaussian noise the arcsine integrand follows from correlation attenuation. Integrating by parts with u=sqrt(s/(1-s)), then setting au=sin(theta) and taking tan(theta), gives the stated arctangent. At zero noise the two arcsine integrals give C(t)=(sqrt(t)+sqrt(1-t)-1)/2 and the risk and explained fraction follow exactly.

## originality

PASS

The supported distinct claim is a unique global one-bit placement law for arbitrary symmetric finite noise under the global standardized-scale condition. The bridge sign correlation, Lévy's occupation law and the directly obtained noiseless covariance are not new. The strongest same-day comparisons either change the process and restrict noise to Gaussian, or change the experiment to two noiseless signs; neither supplies the distribution-free noisy bridge theorem.

## value

PASS

This is a sharp decision result for a natural information-constrained experiment: one observed bit for a global path functional. Exact midpoint uniqueness robust to discrete, heavy-tailed or degenerate symmetric noise removes a noise-density assumption, and covers both constant absolute and constant relative amplitude. The explicit risks give a quantitative benchmark; neither numerical design tuning nor a noiseless formula alone would give this conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
