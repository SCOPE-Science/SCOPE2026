# Independent mathematical audit

## correctness

PASS

A new leaf replaces an old one unless a uniform branch selects a nonleaf; hence the increment is Bernoulli with parameter (j/n)^beta(1-L/j). Centering by the exact mean gives damping a_{n,j}=1-n^{-1}(j/n)^{beta-1} and a bounded martingale difference. The ODE has an integrable second derivative at zero for every fixed beta>0, so summed local Euler errors and the one-leaf initial discrepancy give an O_beta(1) unscaled centering bound. Summation by parts against the monotone damping weights bounds the supremum by twice the martingale supremum, giving summable Azuma tails under every cross-row coupling. The martingale brackets converge uniformly by the fluid law away from zero and a bounded initial-interval estimate; the drift measures have vanishing mesh atoms and converge uniformly in cumulative mass to t^beta/beta. Thus the centered recursion converges to the stated linear diffusion, including 0<beta<1. The same bracket and squared product weights give convergence of endpoint variance. The variance is positive since 0<p_beta(s)<1 in the interior. The beta=0 and beta=1 formulas follow from the limiting kernel s/t and x_1(t)=t-1+exp(-t), respectively. The density comparison follows from the positive drift difference (q_1-q_2)(1-x_2/t). The variance bound 1/(beta+1) gives its zero limit, and its beta=1 value exceeds 1/12. Even a literal eventual-decrease interpretation holds: writing e=1/beta and u=s^beta gives x_beta(s)/s=e*u*J(e,u), with J(e,u)=integral_0^1 w^e exp(-e*u*(1-w)) dw. The variance divided by e is the integral of exp(-2e(1-u))*u^e*(1-e*u*J)*(1-u+e*u^2*J); dominated differentiation using integrable logarithms shows a C^1 extension with value 1/2 at e=0. Thus dv_beta/d beta is eventually negative. The frozen finite checker was inspected, not executed, and its reported cases are not the proof.

## originality

PASS

The aggregation model and metric scaling are prior work, as are the classical benchmark constants. The supported increment is the specific time-inhomogeneous growing leaf-count law, diffusion and explicit nonmonotone variance profile for the polynomial triangular array. The strongest inspected comparators do not state or mechanically imply that combination.

## value

PASS

Leaf counts are local statistics uncontrolled by the natural metric-measure scaling theorem. The result identifies the entire Gaussian trajectory, supplies the terminal variance and separates a strictly decreasing density from a genuinely nonmonotone variance across the natural profile family. The integrable singular drift at the initial time and the arbitrary-coupling almost-sure law are useful features, not rephrasings of the benchmark constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
