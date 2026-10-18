# Independent mathematical audit

## correctness

PASS

The source Proposition 4.3 upper bound K(r)<=2r-1 follows by monotonicity of separated penalty model, source feasibility [G(y)]+<=2*iota*nu/gamma, and the bound on difference at candidate. For X=[-2,2], f(x)=-x, G(x)=2(1+x), y=0, iota=nu=gamma=1, exact affine model on [-1,1] is psi_r=2r+(2r-1)x, giving source residual V_1=1 and transferred residual V_r=2r-1. Feasibility saturates at G(0)=2, Slater G(-2)<0. Penalized constrained optimum x*=-1, phi_1=1+|x+1| with exact global quadratic growth modulus 2/3 on compact X by |x+1|<=3. Every r>=1 is attained, including r=1. Thus the mathematical sharpness with these regularities is valid.

## originality

FAIL

FAIL: an actually published Resultary 2026-10-04 record titled The Penalty W-certificate transfer constant is sharp was returned by targeted Resultary search and its complete RESULT.md was read from Git blob 16570f83ffa2db59f6c47081b49ae581ddab1acf. It proves the same exact transfer factor 2*r-1 under the same Definition 3 with a one-dimensional affine constrained witness, saturated Wolfe residual and feasibility, for all r>1. Its witness f(x)=-rho*x/2, G(x)=x, candidate y=iota, is equivalent by affine change of coordinates/scaling to this witness. Slater feasibility already holds for x<0 there; adding a compact interval supplies the quadratic-growth property automatically for this V-shaped penalty without a new mechanism. The current strengthening does not isolate a new essential mathematical phenomenon; it is a covered corollary/variant of the already published sharpness result.

## value

FAIL

FAIL: the same sharp coefficient and underlying equality phenomenon were previously exhibited explicitly in the identical optimization certificate setup. The compact-bound and quadratic-growth observations are routine modifications of a scalar affine witness; no independently needed new invariant, threshold, classification or mechanism survives. Correctness and reproducibility alone do not establish value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
