# Independent mathematical audit

## correctness

PASS

For pure stationary circular complex Gaussian noise with compact bounded nonzero spectral density S, the accepted first-intensity identity gives rho=1+(log F)''/4pi=4pi Var_{mu_omega}X=m'(omega) with F=integral S(x)exp(-2pi(omega-x)^2)dx and exponentially tilted mean m. Essential compact endpoints imply m(+-infinity)=b,a, so exact total zero-intensity integral b-a and right tail b-m(R). For S(b-u)=u^alpha h(u)exp(-kappa/u^beta), saddle phase t u+kappa/u^beta, t=4piR, has unique minimizer u_t=(kappa beta/t)^{1/(beta+1)} with Gaussian variance scale u_t/((beta+1)t). Convergence of first two centered moments using convex phase and bounded prefactors establishes sharp rho(R)~u_t/((beta+1)R) and integrated tail~u_t; algebraic cutoff gives alpha+1/(4piR^2). Independent SciPy tilted-integral at beta=1,t=1000 yielded mean/u_t about 1.029 and var/sigma² about 1.064, corroborative only. Left edge follows reflection. Spectral intensity, not finite sample recovery, is identified.

## originality

PASS

Known Gaussian-spectrogram intensity formula and stationary Gaussian entire-function spectral theory are credited, as is the flat box-band limit. The distinguishing surviving contribution is the exact endpoint saddle-variance coefficient/exponent continuum for an infinitely flat compact cutoff and inverse recovery of beta/kappa. Closely related full primary general Gaussian analytic literature was not wholly accessible; best-of-knowledge qualification retained.

## value

PASS

Identifies a universal continuously varying zero-intensity tail exponent and exact constant for infinitely flat compact spectral cutoffs, together with integrated tail and edge-parameter recovery. This is a naturally motivated non-regular spectral boundary beyond standard algebraic endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
