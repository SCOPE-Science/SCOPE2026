# Independent mathematical audit

## correctness

PASS

For g_c(t)=(t-c)e^(-beta t^2) at ab=1/2, Zak-frame criterion reduces frame positivity to noncoincident zeros of two theta entries; theta function has one simple zero per period parallelogram and a ratio difference elliptic function with two simple zeros only at u=0,1/2, at which P/F=0. Hence simultaneous fibre zero iff c=0 for every width and rectangular aspect ratio, including pure-Gaussian endpoint. At beta=pi,a=1/2,b=1 the Hessian of the unique zero fibre is nondegenerate; minimizing the quadratic Taylor form yields C_R=Delta^2/||u||^2, C_I=Delta^2/||v||^2. Reflection g_(-c)(-t)=-g_c(t) makes optimal A(c) even and real analytic near zero, so odd total degrees vanish and remainder is O(|c|^4). Direct independent Gaussian tail summation gave C_R=1.999916096270648 and C_I=.4881512351938045. Infinite conclusion uses theta argument principle and implicit function theorem, not finite sampling. Source tree, RESULT.md and CHECK.py inspected.

## originality

FAIL

Two published records already cover every substantive claim: one classifies all Gaussian–first-Hermite mixtures at ab=1/2 and arbitrary widths/rectangular lattices; another gives phase-anisotropic sharp lower-frame-bound expansion for the *Fourier-dual* rectangle (a,b)=(1,1/2). Under unitary Fourier transform, g_c maps to -i(t-i c)e^(-pi t^2) and lattice (.5,1) maps to (1,.5) with unchanged optimal bounds. Its published coefficients 2 K_nu(pi)=1.999916096..., 2 K_x(pi)=.488151235..., exactly agree after exchanging Re and Im. Improvement of the error from O(|c|^3) to O(|c|^4) follows from routine analytic parity, not a new mathematically motivated invariant.

## value

FAIL

Qualitative existence, the natural exact quadratic onset invariant, both directional constants and their anisotropy already follow from accessible earlier same-family findings after unitary Fourier duality. The O(|c|^4) parity sharpening is a routine unmotivated error-term refinement rather than an independently useful new boundary classification. Correct calculations cannot supply new scientific value when the final claim is covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
