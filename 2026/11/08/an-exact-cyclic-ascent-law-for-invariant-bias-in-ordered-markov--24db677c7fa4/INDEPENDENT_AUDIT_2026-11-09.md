# Independent mathematical audit

## correctness

PASS

For 0<u=1−exp(−h)<1, every ordered edge-exponential sweep is stochastic, irreducible and aperiodic. The pre-update mass at vertex i is pi_i+J*1_{r_{i−1}<r_i}; conservation gives constant flux J=u/(n−um), hence exact pi_i=(1−u*d_i)/(n−um). I independently checked a rational n=5 update-order example by multiplying its matrices and verifying stationarity. Summing absolute deviations yields TV=u*m*(n−m)/(n(n−u m)), with 1<=m<=n−1; one-variable calculus maximizes the envelope at t=m/n=1/(1+sqrt(1−u)), equal tanh(h/4). Cyclic conjugation of any sweep matrix yields a circulant doubly stochastic average and exact uniform invariance. The proof covers all n and h, whereas finite checker enumeration is corroboration.

## originality

PASS

The constant stationarity flux and exact cyclic ascent bias are not obtained by existing PDMP splitting error expansions, information metrics, or nearest published cycle positivity findings. Same-cost cyclic rotation correction is a distinct exact invariant statement; novelty qualified by specialized update-schedule literature.

## value

PASS

Ordered generator splitting changes the invariant measure even when every factor is exact and stochastic. The theorem's exact dependence on the cyclic ascent statistic, global sharp worst-order bias tanh(h/4), and cost-neutral random-rotation correction give actionable and conceptually distinct stochastic approximation insights; this is more than checking row stochasticity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
