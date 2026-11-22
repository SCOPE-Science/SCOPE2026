# Independent mathematical audit

## correctness

PASS

Forward positivity is a real hypothesis since the full quadrant is not invariant. The prey satisfies x_{n+1}<R x_n exp(-x_n), so x_n decreases to zero and alpha x_n->0 makes y_n super-geometric. For R<1 the convergent sums x_n,y_n give a nonzero limit C=x_n/R^n and tail O(R^n); summing the product of x_k/(CR^k) proves positive finite D and the exact Gaussian exponent n(n-1)/2. At R=1, eventual multiplier e^{-x_n}-y_n>=1/2 yields x_n>=c 2^{-n}, whereas y_n=O(q^n) for arbitrary q<1, so y_n/x_n^m decays exponentially for every fixed m. With u_n=1/x_n, the exact update u_{n+1}=u_n e^{1/u_n}/(1-y_n e^{1/u_n}) expands as u_{n+1}-u_n=1+1/(2u_n)+O(u_n^{-2})+O(rho^n). Summability gives u_n=n+0.5 log n+H+O(log n/n). The difference of V_n=log(y_n Gamma(n)/alpha^n)+0.25 log^2 n+H log n is O(log^2 n/n^2), so V_n converges and D>0. Verified that nlogn limit follows from Stirling, not from numerical fitting. The described positive invariant open set x_0<min(1,1/alpha), y_0<R exp(-x_0) indeed decreases both coordinates and retains positivity.

## originality

PASS

The exact same-model Hamada/El-Azab/El-Metwally published paper establishes a subcritical global extinction region and neutral linear multiplier, not the two exact extinction clocks, particularly the universal critical exp[-(log n)^2/4]. An earlier Gaussian herbivore claim in a different strong-Allee Ricker model and neutral Leslie–Gower results are not the same coupled recurrence. The simple subcritical Gaussian mechanism is credited rather than asserted unique.

## value

PASS

The distinction between geometric prey extinction and neutral 1/n prey decay induces genuinely different predator time scales, with a non-obvious universal log-squared prefactor from summing the parabolic prey correction. This is a motivated boundary asymptotic for a published ecological recurrence, not merely a Jacobian check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
