# Independent mathematical audit

## correctness

PASS

In scaled position y and unit reset rate, the equations on (−β/q,β) are u''−u+u(−qy)=−1 and p''−p+p(−qy)=0. To the left the reset gives zero future time and jump-capture payoff one, so both outer equations have right side −1, and boundedness gives the same Robin condition F'(−β/q)=F(−β/q)−1. Matching the factorial-series odd homogeneous and negative even particular solutions with F(β)=0 reproduces both formulas and gives 0<p(0)<1. Piecewise C¹ matching does not create a local-time term. The uniform block capture bound is valid also for q=1 and identifies the bounded solutions as the expectations. Independently, the first-reset renewal equation has kernel (exp(−|x−y|)−exp(x+y−2β))/2 in pre-reset position y<β. It restricts continuing starts to [−qβ,β], on which Brownian capture before reset has probability bounded below by exp(−(q+1)β); this gives a contraction and an alternative uniqueness check. Integrating this kernel with piecewise linear interpolation reproduced (u,p)=(1.2462091261,0.1144004837) at q=1/2,β=1 on a 640-panel grid, within 1.3e−6 of the reference; at q=1,β=2.5 both values were within 2.1e−5 of the elementary expressions. For fixed q<1 the normalized odd and even factorial weights escape to large indices, giving the coefficient-product limits and two equal leading contributions d_q exp(β)/2 to u(0). The bounds by sinh and cosh with multiplicative factors between 1 and the limiting odd coefficient, which tends to 1 as q↓0, are uniform at β/q and give the other rare-jump limit. At q=1 the even series terminates and the odd series is elementary, proving the finite mean limit and positive limiting jump fraction.

## originality

PASS

The closest inspected works share the sign-reversing mechanism but expressly count only exact visits. The half-line stopping event instead has a positive jump channel, which changes the outer boundary-value problem and the resulting mean. Other inspected overshoot work studies a different random walk and reset mechanism. The distinct supported claim is the pair of explicit half-line capture laws with their limiting regimes, not the resetting process or pantograph method in isolation.

## value

PASS

A detector that records leapovers measures a genuinely different first-passage law from exact-point detection. The exact channel fraction quantifies when reset captures matter, and the two strong-reset regimes show an important boundary effect: abolishing contraction at q=1 changes a mean growing exponentially in β to a finite Brownian-scale mean and restores a positive limiting fraction of reset captures. This is more than a change of convention or computation of one sample rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
