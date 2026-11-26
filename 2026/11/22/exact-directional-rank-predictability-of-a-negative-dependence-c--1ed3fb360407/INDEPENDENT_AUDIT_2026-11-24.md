# Independent mathematical audit

## correctness

PASS

Independently reconstruct the GBF ranks using X~Exp(1), Z~Exp(theta) independent, Y=exp(Z−X), b=theta/(1+theta), R=exp(−X)=1−U. Y's rank is b*y below y=1 and 1−(1−b)y^(−theta) above. Given R=r the survivor of V is 1 below br, (br/v)^theta from br to b, and (1+theta)(1−v)r^theta above b. Given V=v, R has CDF (r/w)^(1+theta) on [0,w], w=min(v/b,1), from the transformed exponential density. These conditional distributions have no boundary atoms. Integrating the squared forward CDF over r gives 2 theta v/(1+2 theta) below b and v²+theta²(1−v)²/(1+2 theta) above. The reverse squared CDF integrates to w*2(1+theta)²/[(2+theta)(3+2 theta)] and E[w]=1−b/2. Centering by the uniform margins gives exactly the claimed two directed formulas. Their difference is positive and has derivative with sign opposite to the strictly increasing 8 theta³+12 theta²−3; endpoint decay and independent 45-digit checks confirm the unique sharp maximum and both decimals. For two observations, |Delta X| is Exp(1), and the independent symmetric Laplace difference Delta Z gives conditional concordance exp(−theta*|Delta X|)/2. This proves tau=−theta/(1+theta) and the stated reparameterizations.

## originality

PASS

The supported distinct claim is the evaluation for the absolutely continuous GBF model. The two formulas as functions of |tau| already occur together, with reversed coordinate assignment, at the boundary of the Marshall–Olkin family; accordingly neither those bare rational functions nor their ensuing numerical gap maximum should be claimed model-independently as new. The boundary Marshall–Olkin copula has a singular component and is not GBF or its transpose/reflection. The inspected GBF primary source supplies the model, conditional laws and Kendall coefficient, not the pair of Chatterjee integrals in the passages read. Other materially close catalogue claims have different copulas or random reflection; the unread Ansari–Rockel table remains a specific risk, not negative evidence.

## value

PASS

GBF is an established asymmetric negative-dependence model; symmetric concordance alone does not say which response ranks are more predictable. These exact directional invariants answer that question at every model parameter, distinguish an order-theta from an order-theta² coefficient near independence, and calibrate the maximum asymmetry. They also allow a meaningful comparison with the same numerical profile in a singular copula, which could not be inferred from concordance alone. The value is the evaluation for the established continuous model, not a claim to a new general dependence measure or empirical prediction method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
