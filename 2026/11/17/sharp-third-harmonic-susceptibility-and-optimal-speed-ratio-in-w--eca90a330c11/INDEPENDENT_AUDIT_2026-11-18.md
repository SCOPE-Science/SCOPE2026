# Independent mathematical audit

## correctness

PASS

The rotating-frame equilibrium has separation r=sqrt(1-n²)>0 and stable variational matrix [[0,1],[-1,-n/r]], making periodic perturbation differentiable for fixed 0<n<1. Linearizing D/|D| gives a constant plus second-frequency forcing. Solving the complex-amplitude equations (2iA=B-n/2, 2iB=-A-(n/r)B-(n²/(2r))+in/2) yields A+iB=in/(3-2in/r); multiplication by e^{it} gives the displayed third harmonic. The global attracting orbit existence is imported explicitly from Yoshihara, not independently established here. Differentiating S²=x(1-x)/(4(9-5x)) has sign (5x-3)(x-3), proving the interior unique maximum; endpoints limit to zero. Independent scipy Poincare shooting/quadrature at n=.3,.5,sqrt(.6),.9 and eps=.002,.004 reproduced coefficient errors <6.3e-7; these finite tests do not establish the smooth all-n theorem or uniformity at endpoints.

## originality

PASS

Global existence and Floquet stability in Yoshihara are prior and are not recertified as novel. The new mathematically separate derivative of the phase-locked third spatial Fourier coefficient and its 1/10 sharp speed maximum were not present in the examined primary orbit results or indexed close analogues. This is best-of-knowledge, with unindexed classical pursuit references an explicit risk.

## value

PASS

A phase-resolved higher-harmonic response is a natural quantitative observable in elliptical pursuit; its exact nonmonotonic speed optimum is not supplied by general orbit-existence theory. The sharp coefficient and fixed-anomaly qualification allow precise comparison and bifurcation calibration without claiming geometric nonellipticity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
