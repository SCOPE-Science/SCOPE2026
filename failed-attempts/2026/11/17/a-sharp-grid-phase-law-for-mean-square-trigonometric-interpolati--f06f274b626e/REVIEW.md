# Independent mathematical audit

## correctness

PASS

The discrete Fourier coefficient from exact nodal geometric differentiation is (i pi/N) exp[-2pi i(a-1/2)k/N]/sin(pi k/N) for 0<|k|<=n, while the Fourier coefficient of G is i/k. Parseval decomposes the squared interpolation error into constant-mode O(N^-2), retained-mode aliasing difference, and tail 2 sum_{k>n}1/k^2; multiplying by N yields 4 plus the stated integral by a uniform phase Riemann sum with smooth removable t=0 singularity. Aliasing of h is O(N^-2) per retained Fourier coefficient, h tail has squared L2 O(N^-3), and a Cauchy cross term with G is O(N^-2), giving a uniform scaled O(1/N) remainder. The integrand differs by the strictly positive contribution proportional to 1-cos(2pi(a-1/2)t) for all a!=1/2, proving unique strict half-cell minimization. Changing one aligned sample from G(0)=0 to pi shifts every Fourier coefficient by pi/N; the corresponding cotangent Parseval integral is strictly larger by the identity (1/t-pi cot(pi t))-(pi csc(pi t)-1/t)=2/t-pi cot(pi t/2)>0. Independent numerical quadrature gave F(0)=15.00253187698, F(.25)=7.156996623005, F(.5)=4.334096272882, F(.75)=7.156996623005. The finite N diagnostics are not the analytic uniform asymptotic proof.

## originality

FAIL

Decisive prior full-text coverage: Arnak Poghosyan, On a pointwise convergence of trigonometric interpolations with shifted nodes (Armenian J. Math. 5(2), 2013, pp.105–122), Theorem 11, formulas (69)–(74), p.117–118, gives an exact normalized L2 phase-response integral a(q,sigma) for shifted (2N+1)-point trigonometric interpolation. The text expressly states immediately after Table 3 that Theorem 11 also holds for q=0, the CLASSICAL UNCORRECTED trigonometric interpolant of a function with a jump A0!=0. Under period rescaling, sigma=2a-1 and F(a)=[2*pi*a(0,sigma)]^2: at sigma=0, the classic partial fractions identity sum_{s in Z}(-1)^s/(x+2s)=pi/(2*sin(pi*x/2)) transforms the prior a(0,0) into exactly F(1/2). The general phase sum likewise coincides with the Fourier-alias expression for F(a). The previous theorem therefore entails the central exact phase functional and its parameter optimization; its strictly minimal half-cell positioning follows from positivity of the phase-dependent cross term. An O(N^-1) remainder under a Fourier-decay assumption and a comparison with one altered aligned point are extras, not a new independent central result. Originality FAIL despite the current proof being correct; this is direct old mathematical implication, not search failure.

## value

FAIL

The governing precise mean-square phase-response and grid optimization are already established in Poghosyan Theorem 11 for q=0, based on even earlier [8],[9] L2 work. The new aligned-node midpoint value calculation is a short exact Parseval corollary and slight regularity/rate refinement, not a separately motivated structural question of the required value. Hence the covered final theorem lacks independent mathematical new value. Correctness of its formulas and finite verification cannot rescue covered originality/value; no repair attempted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
