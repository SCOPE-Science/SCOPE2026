# Independent mathematical audit

## correctness

PASS

Tensor integration gives Var(J_d)=3^−d, Cov(J_d,Y_x)=∏a(x_i), a(u)=u(1−u/2), and Var(Y_x)=v+η, v=∏x_i. Gaussian conditioning minimizes squared error over all measurable estimators, with explained variance F=∏a(x_i)²/(v+η). At v=0 it is zero even at η=0, by F≤v. An independent diagonal reduction: at fixed v>0, put l_i=log x_i; the sum l_i is fixed and log(1−e^l/2) has second derivative −2e^l/(2−e^l)²<0. Strict Jensen therefore selects x_i=v^(1/d) uniquely, including the trivial v=1 case. On this diagonal the log-information derivative divided by d/r is 4(1−r)/(2−r)−r^d/(r^d+η); the endpoint 1 has negative derivative for every finite η. The only interior root is r=2/3 if η=0; otherwise r^d(3r−2)/(1−r)=4η has a strictly increasing left side from zero to infinity on (2/3,1). For fixed r in that interval the left side strictly decreases in d, establishing both monotonicities in the claim. At zero noise h(r)^d, h=r(1−r/2)², gives I=(8/27)^d and fraction (8/9)^d. For fixed η>0, let z=d(1−r). The exact root gives z e^z≤d/(4η), hence z=O(log d). Logarithms then give z+log z=log(d/(4η))+O((log d)²/d); the derivative of the inverse comparison map is bounded by one. Thus the Lambert error in 1−r has order (log d)²/d². In I=4^−d(1−(1−r)²)^(2d)/(r^d+η), the correction tends to one and r^d→0 by the root equation. For η_d=c(2/3)^d/d, write y_d=d(r−2/3). The exact monotone relation is c=(9/4)y_d(1+3y_d/(2d))^d/(1−3y_d/d). Its locally uniform limit yields y e^(3y/2)=4c/9 by bracketing, with c=0 exact. At r=2/3, (log h)'=0 and (log h)''=−27/8, while η_d/r^d=c exp(−3y/2)/d+o(1/d); substituting gives both terms of the asserted log-information coefficient. Replay: RESULT.md proof steps 1–4 or the Jensen reduction above. A separate high-precision log-domain bisection at d=100,1000,10000 confirmed convergence for η=1/5 and c=7/3; for example at d=10000 the fixed-noise information ratio to 4^−d/η was 0.98610315 and the crossover coefficient error was −4.15×10^−5. These are spot checks, not proofs. The original verify.py was inspected, not executed.

## originality

PASS

On the evidence inspected, the defensible contribution is the unrestricted one-site noisy optimizer with its sharp dimension/noise crossover, especially the coefficient after the small-noise scaling. The conditioning formula, tensor integration, noiseless rule and ordinary one-dimensional noisy specialization are excluded from the novelty finding. No inspected prior result supplies the competing fixed-noise and vanishing-noise dimensional laws or the crossover coefficient; historical noisy-information literature remains a priority risk.

## value

PASS

The same sensing budget gives two different exponential explained-variance rates depending on whether noise is exactly zero or fixed positive. The result identifies the movement of the global design that accompanies this change and locates the exponentially small noise scale at which it first moves by order 1/d, with a quantitative information loss at that scale. This is a structural calibration law for one observation, not merely a table of single-dimension roots. No consequence for multiple, adaptive, or heteroscedastic observations follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
