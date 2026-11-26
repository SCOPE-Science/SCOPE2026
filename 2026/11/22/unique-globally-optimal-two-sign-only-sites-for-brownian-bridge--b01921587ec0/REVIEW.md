# Independent mathematical audit

## correctness

PASS

Integrated bridge covariance gives Var(J)=1/12 and Cov(J,B_s)=s(1-s)/2. With two interior distinct sites all sign atoms have positive probability, and global sign reversal makes the Bayes decoder odd; the odd functions on the sign square are exactly the span of the two signs. Thus the arcsine sign Gram matrix and the Gaussian mixed moment give the exact objective, not a restricted linear decoder. In logit coordinates, decomposing into sign sum and difference gives the two terms (1+h)w/(1+c) and h(w-1)/(1-c), divided by 4 pi(w+h)^2; this verifies the frozen rational expression. Its unconstrained w-critical point grows with c, and for rho>=1/3 the factor (1-rho)(1+rho)^2(3rho-1)/(8rho^2) and c<rho give strict merit loss for every w>1. For rho<=1/3 the Lipschitz bound for log cosh gives both amplitude ratios at least rho, allowing a strict upper bound by replacing c with 3rho/5. The sign of the resulting variance certificate reduces to 4(1-rho^2)^2(25-9rho^2)-3(5-rho^2)^2 = (5-rho^2)^2-(6rho^3-14rho)^2, the stated opposite-sign cubic factors with an overall minus sign. This bounds the low correlations strictly below 1/(6 pi), realized by the symmetric rho=1/2 design. For the reflected design the logarithmic derivative sign is Q(rho)-1; the positive term of Q'/Q is <1/(1-rho), showing strict decrease of Q from infinity to zero. Pinned and duplicate observations reduce to at most a single sign (variance explained at most 1/(8 pi)). For the real-valued benchmark, the conditional residual consists of independent bridges on three intervals, giving residual variance sum(length^3)/12, minimized uniquely at trisection by strict convexity. Independent double-precision bisection gives rho=0.5393616215470003, s=0.3503800627463755, and explained fraction 0.638028078245238. Replay: /workspace/reproductions/frozen-review-checks.js, record 2, Node.js. The frozen high-precision output and script were inspected, not independently executed or taken as the global proof.

## originality

PASS

The part supported as distinct is the exact all-pairs, fixed zero-threshold sign design for the linear signed integral of this pinned Gaussian process. Gaussian conditional-mean and sign-correlation formulas are inputs, and related binary quadrature results concern different targets or covariance. No matching global optimizer was identified in the bounded comparisons; historical priority is not certified.

## value

PASS

A bridge integral is a basic Gaussian quadrature target, and exact sign reports impose a natural one-bit measurement constraint. The global optimizer moves away from the full-value trisection design; precisely quantifying that movement and the retained variance, with asymmetric and boundary designs ruled out, answers a genuine design question rather than just recomputing a decoder or giving a numerical placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
