# Independent mathematical audit

## correctness

PASS

With kappa=u+v, Pi=I+A/kappa is a projection and A vanishes on its range and equals −kappa on the complementary range. The Caputo series with zero initial slope is Pi+f(I−Pi), f=E_alpha(−(kappa^(1/alpha)t)^alpha), by scalar Caputo differentiation of the series. Its diagonal numerators are v+uf and u+vf, the off-diagonals have the sign of 1−f, both column sums equal one, and the determinant is f. For 1<alpha<2 the even scalar function is the Fourier transform of the stated density: take twice the real part of z^(alpha−1)/(1+z^alpha) at z=iω, with the standard inversion normalization. With y=|ω|^alpha and theta=πα/2, its mass is 2 sin(theta)/(πα) times the integral of 1/(1+2y cos(theta)+y²) on the positive half-line, hence 2theta/(πα)=1. The independently checked neutral-diffusion Fourier pair also verifies this step. Positivity off zero frequency makes |f(s)|<1 for s>0 by equality in the triangle inequality and integrability of the density gives f(s)→0. Negativity also follows independently of the cited tail expansion: the Laplace transform tends to zero as z decreases to zero, impossible if f is everywhere nonnegative since f(0)=1 and f is continuous; the Laplace identity follows first for z>1 from the series and then by analytic continuation on the right half-plane using |f|<=1. Negativity and decay give an attained global minimum −c_alpha in (−1,0), and the entry conditions give the exact sharp interval including equality at a minimizing time. Scheffé applied to the densities gives uniform convergence of the Fourier transforms to e^(−|s|) as alpha decreases to 1, so c_alpha→0. Near 2 the series at s=π admits a summable majorant on alpha in [3/2,2] and tends to cos(π)=−1, so c_alpha→1; at alpha=2 all times are nonnegative only for u=v. The negative determinant at some finite time rules out any locally integrable generator via Liouville, not arbitrary stochastic processes with the given initial-time marginals.

## originality

PASS

The matrix solution and the scalar characteristic-function law are established prior results, and the generic distinction from a Markov propagator is not itself the originality claim. The supported contribution is the exact all-time two-state positivity boundary for strictly positive rates with zero initial velocity, its order limits, and the explicit separation in the admissible regime. No inspected primary statement gives the two-state rate classification; access limits do not supply negative evidence.

## value

PASS

This gives a sharp boundary for the minimal finite-state example in a genuine fractional-dynamics question: some high-order solutions stay inside the probability simplex for every time even though none of them can be integrable-rate two-state Markov propagators. The cutoff guarantees or rules out nonnegativity for every positive rate pair, includes exact boundary times of vanishing entries, and compares the neighborhoods of the classical orders 1 and 2 without assuming monotonicity in alpha.

The dated certificate retains the supplied scientific assessment, sources and limitations.
