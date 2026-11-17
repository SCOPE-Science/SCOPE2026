# Independent mathematical audit

## correctness

PASS

Exact two-state CTMC occupation solves p_t=pi_w+(p-pi_w)e^{-2kt cosh(beta(E-w)/2)} and net jump difference equals X_0-X_t. On 0<w<Phi_p, factorization W_t=w[p-(1-p)e^x]e^{-x/2}(1-e^{-scosh(x/2)})/(2cosh(x/2)) has strictly negative second log derivative: A(y)=1-y/(e^y-1) and A'(y)>0 imply strict concavity of kernel, plus log w. Endpoints vanish (also w->infty for p=1), proving global unique optimum. At w=E, log derivative equals 1/E-beta/[2(2p-1)]; implicit differentiation gives w*(t) increasing when beta E>2(2p-1), decreasing when beta E<2(2p-1), and constant w*=E at equality. For p=1, short-time 2/beta, infinite-horizon [1+W_0(exp(beta E-1))]/beta. I independently checked the signs and boundary through the displayed analytic derivatives; bounded original verify_load.py inspected (not treated as proof).

## originality

FAIL

The identical strict log-concavity, all-horizon fixed-load optimization and occupation threshold had already been published in a November 2 Resultary primary record, where p_crit=1/2+beta E/4 is algebraically identical to beta E=2(2p-1). Its full mathematical RESULT.md was read. The newer p=1 endpoint is a straightforward limit of the prior formulas plus Lambert W algebra, not a sufficiently separate surviving original theorem. Earlier active-matter work gives physical rate conventions, not the priority comparison. Rejection is scientific coverage, not merely a failed search.

## value

PASS

Sharp thermodynamic parameter boundary and load-versus-time reversal are useful exact optimization results for a well-defined two-state stochastic model. This content is valuable mathematically but already covered by the stronger prior publication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
