# Independent mathematical audit

## correctness

PASS

The exact invariant yields squared speed Y_A(s)=int_0^s[1+alpha(A²-s+u)]e^{beta u}du, s=A²-x²; it is positive for 0<s<=A², proving smooth simple ovals and minimal physical period. The original-time quadrant density is proportional 1/(sqrt(1-s/A²)v_A(s)), v_A=sqrt(Y_A)/A; hence T_A=2D_A/A² and M_q=I_q/D_A with I_q=int v_A^(q-1)/sqrt(1-s/A²) ds. Endpoint bounds show D_A->pi/sqrt(alpha beta). For fixed q<1 dominated convergence gives gamma^q/sec reciprocal cos(πq/2); q=1 has I_1=2A² exactly; q>1 setting u=A²-s and dominated Laplace integral yields gamma^q A sqrt(2beta/[pi(q-1)])exp[beta(q-1)A²/2]. For q=1+lambda/A², s=A²t and A^-2 log v_A(A²t)->beta t/2, with common integrable t^-1/4(1-t)^-1/2 domination for lambda in compacts, yields 2sqrt(alpha beta)/pi times F_beta(lambda)=int_0^1exp(beta lambda(1-u²)/2)du. Algebraic prefactors and period normalization checked against exact formulas; verify.py finite quadratures only corroborate. No claim at alpha=0 or q varying faster than A^-2.

## originality

PASS

PASS: full same-equation published uniform period/turning-layer theorem covers physical period and TV of the finite turning-gap variable, but its TV law controls bounded observables and cannot imply exponential growth of |y/A|^q (unbounded with A), or the moving-order crossover. Published Cauchy velocity finding for xdot=v, vdot=-x(1-alpha v+beta v²) has a different speed feedback and fixed rather than normalized large speed, hence does not cover. Appis–Llibre classify global centers but lack physical-time moments. These distinctions are mathematical statements not title matching.

## value

PASS

High-order moments of a time-sampled velocity distinguish rare exponentially fast trajectory passages invisible to weak or TV turning-layer convergence. Sharp phase transition at order one and its finite A^-2 interpolation is an interpretable nontrivial asymptotic with useful normalization and independent oscillator/statistical relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
