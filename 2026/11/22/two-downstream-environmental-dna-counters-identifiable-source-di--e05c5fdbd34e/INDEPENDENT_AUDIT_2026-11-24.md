# Independent mathematical audit

## correctness

PASS

For g a calibrated positive mixture, H is the tilted mean attenuation rate and H' is minus the strictly positive tilted variance; the log mean ratio therefore increases strictly to the claimed unattainable limit. The Poisson split conditional on total T is binomial with downstream probability p=g(x+h)/(g(x)+g(x+h)). Reparameterizing the nuisance Q by the free total mean E[T] removes the total-score contribution to source distance. Here p'=p(1-p)(H(x)-H(x+h)); the binomial information E[T](p')^2/[p(1-p)] gives the stated formula independently of a Schur complement. It is positive for h>0 and tends to zero at both ends. Write b=c2/c1, a=a1, delta=a2-a1. The expansions g(u)=c1 exp(-au)(1+O(exp(-delta u))) and H(u)=a+delta b exp(-delta u)+o(exp(-delta u)) yield the proposed profile after extracting Q c1(delta b)^2 exp(-(a+2delta)x); two h-derivatives of the scaled information converge on compact h intervals by the finite exponential expansions and denominators bounded away from zero once the leading factors are extracted. Uniformly for u>=x both H(u)-a and |H'(u)| are O(exp(-delta x)); with the Poisson prefactor this bounds scaled information at small h by C h^2 and at large h by C' exp(-ah). These exclude escaping maxima. The limiting log derivative decreases strictly from +infinity to -a, so the maximum is unique and strictly nondegenerate. Compact convergence plus local strict concavity of the scaled information gives eventual uniqueness, not just subsequential convergence. Exact check: at x=h=log(2) for rates 1,2 and weights 1,1 with Q=16, the conditional downstream probability is 5/17, total mean is 17, and hazard difference is 2/15, giving 16/255. For an uncalibrated mixture a shift x to x' is exactly absorbed in each source amplitude by multiplication by exp(a_j(x'-x)); a one-pool model is an alias even with known shape.

## originality

PASS

The supported distinct claim is the general distant-source efficient-information profile and eventual unique two-rate optimal gap under calibrated shape, together with the source-distance identifiability boundary. Log convexity and the Fisher calculation are standard. A distinct same-day optimization record exactly overlaps the equal-gap/equal-weight example at the level of objective shape, but has a different parameter, criterion, general objective and asymptotic regime. Neither the matching example nor same-day order is claimed as priority evidence.

## value

PASS

The model gives a useful exact benchmark: an unknown scale still permits localization if a mixture shape is calibrated, but without calibration even noiseless full downstream data can alias all distances. The two-rate Fisher gap and the faster loss of localization information than of mean counts quantify distinct design consequences that identifiability alone cannot reveal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
