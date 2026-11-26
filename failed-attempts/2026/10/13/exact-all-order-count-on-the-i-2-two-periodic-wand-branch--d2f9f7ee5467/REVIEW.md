# Independent mathematical audit

## correctness

PASS

The positive diagonal fixed point is unique because h is strictly decreasing with the required endpoint limits. For z>t put r=(z/t)^(1/k)>1. Dividing the original equations gives r=(1+1/t)/(1+1/z); substituting z=r^k*t gives t=(1-r^(1-k))/(r-1)=sum_{j=1}^{k-1}r^(-j) and then z=r^k*t. Substitution back gives the stated rational activity and is reversible. For r=e^(2s), the exponential factors cancel in the sinh quotient; its log derivative equals sum_{j=1}^{k-2}(H_s(j+1)-H_s(j))-k*(H_s(k)-H_s(k-1)), negative since H_s is increasing and strictly convex (differentiate u*coth(us)). The limits are lambda_cr and 0, so there is a unique swapped pair only below lambda_cr. Expansion of log(sinh(us)/(us)) at zero gives ((k+1)(k-1)^2-1-k^3)/6=-k(k+1)/6 as the s^2 coefficient of log(lambda). Since log(z/t)=2ks exactly, inversion gives the stated onset coefficient and the O((lambda_cr-lambda)^(3/2)) error. This check applies only to the positive reduced I_2 system; no completeness outside I_2 or extremality follows. Inspected RESULT.md, VERIFICATION.md and verify.py; the analytic proof did not require executing the supplied script.

## originality

FAIL

The headline all-order solution count is already implied exactly by the ordinary two-state hard-core model's parity-periodic theorem. For the wand variables set mu=2^k/lambda, a=1/(mu*z), b=1/(mu*t); then a=(1+mu*b)^(-k), b=(1+mu*a)^(-k), reversibly for each positive activity. This is precisely (2.10) of arXiv:2111.11163; its Theorem 2.6 gives the exact one-versus-three count for all k>=2, including equality, and attributes it to Suhov–Rozikov (2004). The change of variables maps the threshold to the displayed wand threshold, reverses the activity inequality, and preserves diagonal solutions and the swapped pair. The wand source's weaker count is not the relevant prior upper bound. The separate formulas for the parameter and onset are correct; the checked general theorem need not state them in wand coordinates.

## value

FAIL

For the stated scope the phase count is a change of variables of a known exact count. The ratio substitution and convexity argument illustrate the recursion, but the remaining closed form is obtained directly from the known two equations and the log-ratio coefficient is its elementary quadratic Taylor expansion. No distinct physical boundary, extremality result, or mathematical gap that needs this particular coordinate coefficient was established. The remaining presentation is useful exposition, not a standalone repair of the claimed classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
