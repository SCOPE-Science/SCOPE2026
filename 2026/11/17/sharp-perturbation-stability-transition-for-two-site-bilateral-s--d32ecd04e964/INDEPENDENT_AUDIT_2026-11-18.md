# Independent mathematical audit

## correctness

PASS

Exact averaging/contrast reduction gives F_w(m,d)=(m,phi(d)) with phi(d)=d(1-w(|d|))/(1+w(|d|)). Monotonicity of w ensures phi is odd and increasing; ||phi||Lip<=1 iff H(s)=s*w/(1+w) nondecreasing. Every two-input quotient in coordinate ℓq equals the swap-symmetric matrix A_theta with eigendirections common mean and contrast; induced ℓq norm is max(1,theta). For inverse powers direct differentiation in z=(s/sigma)^p yields derivative peak z=(1+c)(p+1)/(p-1) only if p>1, giving 1+c(p-1)^2/(2p(1+c)); p<=1 sup=1 at infinity only. Gaussian stationary equation 2u(1-v)=3(1+v) has a unique root because the bracket decreases; substitution gives 1+2v(2+v)/(1-v^2). Finite distinct secants cannot equal isolated derivative maxima. Independently recomputed power-law peaks for c=0.1,0.7,1 and p=0.4,1,1.5,3 and Gaussian roots at c=0.1 and 1.

## originality

PASS

Pianykh and the original bilateral-filter papers concern range weighting and one-input variance/edge preservation, while the current quantitative question is worst-case differences of two filtered inputs in arbitrary ℓq norms. Search found no prior full two-pixel contrast criterion or sharp power/Gaussian amplification constants; full historical priority remains qualified where original literature was not read exhaustively.

## value

PASS

The two-site system is the minimal nontrivial bilateral-filter model and exactly separates one-input smoothing from two-input instability; p=1 is an interpretable tail-decay threshold, with quantitatively sharp worst-case response for standard rational and Gaussian kernels. This precise stability boundary is useful even though it does not generalize automatically to full images.

The dated certificate retains the supplied scientific assessment, sources and limitations.
