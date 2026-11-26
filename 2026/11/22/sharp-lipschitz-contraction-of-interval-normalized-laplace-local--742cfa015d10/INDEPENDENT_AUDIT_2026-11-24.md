# Independent mathematical audit

## correctness

PASS

For x<x' the log density ratio is a constant plus lambda(|y-x|-|y-x'|), nondecreasing in y. Equal row mass then gives stochastic order, and the ordered quantile coupling gives W1 equal to the difference of means, which the identity function realizes. Subtracting the normalizer score from the left/right kernel scores (-lambda,+lambda) gives (-2lambda B,+2lambda A), where A,B are the two masses. The conditional means x-H(u), x+H(v) thus give m'=2lambda AB(H(u)+H(v)). The two factors are maximized at the midpoint: AB<=1/4, and H'' has the opposite sign of h(r)=(r-2)e^r+r+2, where h(0)=h'(0)=0,h''(r)=re^r>0. Strict concavity therefore gives H(u)+H(v)<=2H((b-a)/2), with equality only there. The result is 1-z/(exp(z)-1) in (0,1). Integrating the continuous interior derivative shows any distinct-pair quotient is strictly less than the optimum; location pairs coalescing at the midpoint approach it. This distinguishes optimizer among functions (the identity witnesses the seminorm) from non-attainment among distinct pairs. Kernel symmetry gives detailed balance with stationary density proportional to Z; iterating the contraction and integrating against this law gives the displayed supremum bound, including k=0. Integrating against any other stationary law then shows equality on all Lipschitz tests, hence uniqueness on the compact interval. This does not claim a sharp k-step norm for k>=2. Independently ran `python3 /workspace/review_checks.py 4` (SciPy): twelve finite-difference gains from direct quadrature at noncentered endpoints and several rates. The finite checks corroborate the argument and do not certify the unique global maximum on their own; the frozen checker was inspected, not executed.

## originality

PASS

Neither normalized localization nor the bounded Laplace kernel is claimed as new. The supported addition is the sharp W1/Lipschitz coefficient and unique maximizing derivative location for the Lebesgue interval model. Reversibility from the symmetric base kernel and mixing from one-step contraction are standard consequences, not independent novelty claims. The closest truncated-mechanism literature was available only in part, so priority is qualified.

## value

PASS

The precise norm measures how bounded support changes a translation-invariant family into a strict contraction and gives a rate from the two physical parameters. Identifying the uniquely worst infinitesimal location matters for sharp robustness; the exact coefficient adds information beyond a qualitative contraction or a loose mixing estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
