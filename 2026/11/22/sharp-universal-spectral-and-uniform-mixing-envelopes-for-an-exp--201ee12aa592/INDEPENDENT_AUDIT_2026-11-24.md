# Independent mathematical audit

## correctness

PASS

Writing c=delta*alpha², differentiation gives 1+c*g(u)*g(v). The score is centered, its range is symmetric, and it takes both values ±M. The copula boundary values are the required ones; nonnegativity is sufficient by integrating over rectangles and necessary by continuity (even a negative boundary value forces nearby negative interior values). The derivative is exp(alpha*u*(1-u)) times [alpha*(1-2u)²-2]. Hence M=1 for alpha<=2, and M=sqrt(2/alpha)*exp(alpha/4-1/2) for alpha>2, with the two interior maximizers of |g| as stated. At alpha=0 the model is independence for all finite delta. The centered transition operator is c times the rank-one form g⊗g, so its nth power has coefficient c^n*J^(n-1), and its norm |cJ|^n is the HGR supremum, attained by the normalized score. The essential uniform lag error is |c|^n*J^(n-1)*M² (continuous attainment extends to essential sup). At any nonzero alpha both objectives strictly maximize at the two admissible delta endpoints; the endpoint objectives are B(alpha)^n and B(alpha)^(n-1), with B=J/M². For alpha<=2, x=|1-2u| gives B as the integral of x² exp(alpha*(1-x²)/2), strictly increasing in alpha and agreeing with the other formula at 2. For alpha>2, s=sqrt(alpha/2) yields B=e*int_0^s t² exp(-t²)dt/s. Its derivative has the sign of D=s³ exp(-s²)-int_0^s t² exp(-t²)dt; D'(s)=2s² exp(-s²)(1-s²)<0. D(1)>e^(-1)-1/3>0 and its limit is -sqrt(pi)/4. Thus the shape optimum is unique, B(s*)=s*² exp(1-s*²)<1, and all claimed equality cases follow. At lag one density optimality holds at every nonzero-alpha boundary, whereas HGR still selects alpha*. Independently ran `python audit_checks/independent_replays.py 3`: 50-digit quadrature of the untransformed score objective and numerical derivative/root, direct checks at extremal points and a two-step convolution reproduce alpha*=4.5675630499780930652…, m=0.6325798050619892679…, and |delta*|=0.0303211885502754231…. Bounded numerical checks corroborate, not prove, the monotonicity and all-lag theorem. The submitted checker was inspected but not executed; its recorded replay is separate from the source's expert, independent-audit and formal statuses.

## originality

PASS

The exact family and admissible ranges are prior, and the lag and HGR formulas are direct specializations of established rank-one spectral theory. The supported distinct result is the exact shape-constrained global optimization and equality classification, with one root-defined base simultaneously sharp for the two all-lag envelopes. No matching family optimization was established in the checked statements; this is a qualified judgment, not universal priority.

## value

PASS

The originating family was introduced to enlarge achievable dependence; maximal nonlinear correlation and persistence under stationary Markov iteration answer a natural question not answered by its rank correlations. The exact family maximum is attained, yields a sharp uniform density convergence base at all lags even at the admissibility boundary, and identifies the unique most persistent shape and the two signs of the coupling. The nontrivial value is this global classification, not recomputation of the generic rank-one spectrum or a bound for all copulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
