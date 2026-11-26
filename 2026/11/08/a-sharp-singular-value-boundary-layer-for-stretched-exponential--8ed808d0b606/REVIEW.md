# Independent mathematical audit

## correctness

PASS

Polar action of the shift sends e_j to e_(j+1); the log-weight update is convolution by the two-point law (1-t,t), so n steps give the claimed binomial expectation. Compactness and strict monotonicity in j give precisely the ordered list and its norm. Bounded convergence for (1+X_n)/n proves the logarithmic norm asymptotic. For alpha>1, the integrated derivative is >=alpha*j and for fixed j its n^(alpha-1)-scaled value tends to alpha*j*t^(alpha-1). This gives both relative vanishing and summable domination for any fixed p>0. Alpha=1 is exactly geometric. For 0<alpha<1, on j<=A n^(1-alpha) the rescaled derivative is uniformly convergent in mean to alpha*t^(alpha-1): binomial concentration bounds the lower tail (where the negative power is at worst polynomial) by exponential probability, and on the central interval the mean is uniformly continuous in the rescaled variables. Integrate and use floor error O(n^(alpha-1)). The infinite sum needs more than the local limit: using X_n<=n gives D_n(j)>=alpha*j*(2n+1)^(alpha-1) for j<=n, hence after scaling a geometric tail O(exp(-const*A)); for n<j<2n the concavity lower bound (n+1+j)^alpha-(n+1)^alpha is >=const*n^alpha, and j>=2n gives >=const*j^alpha, since (n+1)/j<=3/4 for n>=2. Both latter tails vanish after normalization. Integrating the local profile to power p gives t^(1-alpha)/(pc alpha). A fresh finite diagnostic used binomial coefficient propagation from [1] by convolution, t=.3,c=.7,p=1.2 and j=0..399; at alpha=.5 the ratios to the predicted mass were 1.266251,1.130181,1.062390 at n=100,400,1600; this truncated diagnostic is not the infinite proof. At alpha=2, D_n(j)=j^2+2j(1+nt) exactly. Packaged checker inspected, not executed.

## originality

PASS

Best of knowledge for the normalized trichotomy and stretched-exponent profile only. The exact singular list follows directly from known binomial geometric weight iteration and is correctly excluded from the novelty claim. The comparison below checks whether prior results dominate the normalized statement, not just whether they mention weighted shifts.

## value

PASS

When every unnormalized singular value tends to zero, the mass carried by the leading one can still have three qualitatively distinct behaviors. The parameter boundary, exact effective spectral count, and shape of the near-leading spectrum distinguish these regimes sharply for a canonical decay family; the uniform tail argument makes the result a statement about all ranks, not a finite-mode calculation. Scope is fixed parameters and the specified compact unilateral shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
