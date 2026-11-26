# Independent mathematical audit

## correctness

PASS

Independently expand N_t^2 into its mean, (1+2lambda t) times M_t=N_t-lambda t, and C_t=M_t^2-N_t. These degrees are orthogonal across times, with covariance kernels lambda min(s,t) and 2lambda^2 min(s,t)^2. Conditioning on N_x projects these degrees onto M_x and C_x with respective factors r and r^2, where r=min(t/x,1). Integration gives coefficients D=1-x/2+lambda(1-x^2/3) and A=1-2x/3, recovering the conditional estimator and explained variance lambda*x*D^2+2(lambda*x)^2*A^2. Integrating the two covariance kernels with the degree coefficients gives Var(Q)=lambda/3+7lambda^2/6+8lambda^3/15. Both endpoint count conventions agree with the limit of this expression for explained variance. Independent expansion gives the claimed quartic derivative factor and positive Bernstein coefficients for P1 on [0,2/3]; all terms have negative derivative on the root bracket and the signs exclude extrema beyond it. At a root, differentiating in lambda gives numerator lambda P2-P0/lambda>0, so the root increases. The simple roots of P0 at 2/3 and P2 at sqrt(3/5) give the stated endpoint expansions. The compact-domain leading coefficient of the risk is minimized at sqrt(3/5), giving 0.03759146501878 versus 0.04956561499771 and a 24.1581789704% leading-coefficient reduction. Replay independent symbolic computations with python /workspace/branches/independent-algebra.py (item 1); universal optimality follows from signs, not a root grid.

## originality

PASS

Credit the classical linear one-site optimum, Poisson-bridge conditioning, and the ordinary conditional-mean projection principle. The distinct result is the exact known-rate quadratic-target optimum and its strictly moving, uniformly bracketed root with quantified risk comparison. The closest inspected results optimize other targets or use different information; none entails this classification.

## value

PASS

An observation budget of one count is natural, and time-integrated squared occupancy penalizes concentrated load in a way the known linear functional does not. The exact optimum quantifies a systematic failure of the standard 2/3 rule for this target and gives a substantial leading-order risk improvement at high intensity. This is not a claim for unknown intensity, noisy or adaptive observations, or other powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
