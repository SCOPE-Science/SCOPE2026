# Independent mathematical audit

## correctness

PASS

For fixed L and interior u=x/L, subtract C from 1-u to obtain homogeneous Dirichlet heat evolution of 1-u. The killed heat kernel is positive and the first sine coefficient is 2/π; the higher modes decay strictly faster, giving the claimed strict stationary bound and leading exponential. With F=erf(x/sqrt(2t)) and H=F(t,L), the shortcut's heat residual is FH'/H²<0. Duhamel gives strict undershoot: the initial term started at positive ε tends to zero by boundedness and dominated convergence against the heat kernel as ε↓0, so the incompatible initial corner does not supply an extra term. Positivity of the shortcut follows from 0<F<H, and its difference from C is strictly smaller than its difference from stationarity. I independently checked the expansion of erf(uy)/erf(y) through order y² with y=L/sqrt(2t), and the cubic's Poisson equation and boundary values, in symbolic arithmetic. The O(t^-2) tail error is integrable, and termwise time integration of the exact sine series has an absolutely summable n^-3 bound. These are continuum equal-time relaxation integrals, not autocorrelation times. The frozen verifier was inspected, not executed; its toleranced sign tests are finite corroboration only.

## originality

FAIL

A distinct indexed result, 58ae94a45462, materially covers the strict signed bias, the exponential versus algebraic deficits, the finite exact cubic integral and the logarithmic shortcut integral with the same coefficient. The strict error envelope follows immediately by subtracting its strict exact stationary bound. There is no supported distinct scientific remainder in the frozen finding relative to that match. The indexed work's chronology and derivation are not established by its displayed catalog date. The primary paper by Henkel already gives the exact correlation and the normalized shortcut, but recognition of a crossover discrepancy is weaker than the results under audit and is not the basis of the fail.

## value

PASS

The gap between bounded-domain exponential relaxation and a positive 1/t deficit is consequential for an integral observable: integrating the shortcut outside its useful time regime produces a false logarithm, not merely an inaccurate coefficient. The exact finite area and the coefficient of the false logarithm make the diagnostic reusable. This is not a claim that the shortcut is poor everywhere or that stationary lag correlations diverge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
