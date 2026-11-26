# Independent mathematical audit

## correctness

PASS

Restrict any coupling to the equality contour and fold each coordinate. The supported folded graph is v=g(u), with endpoints having no marginal atoms. Its first marginal is dominated both by 2 du and by 2|g'(u)| du (pulling back the second marginal constraint through the interior graph bijection). These inequalities hold also for singular couplings. Taking the pointwise minimum saturates the mass bound. Independent fair signs split each folded density among two symmetric preimages and produce dominated unfurled marginals; the product of residual marginals divided by their common mass completes a copula, with no extra mass on the area-zero contour, or no residual needed at mass one. At any maximum the first folded contour submeasure must equal the pointwise minimum, since its difference is nonnegative with integral zero. For p≠1 the monotone absolute slope crosses one at u=a^q/(a^q+b^q)^(1/p), v=b^q/(a^q+b^q)^(1/p), with u+v=(a^q+b^q)^(1/q). For p>1 the integrated minimum is a+b-u-v; for p<1 it is u+v. With the factor two these are exactly the given branches. The p=1 constant slope gives 2 min(a,b), including the unequal-axis case. The strict comparison follows from the signed powers; substituting equal axes and differentiating gives the circle, diamond and one-sided slopes. An independent quadrature using the contour parameter t=(u/a)^p matches 18 cases: `python /workspace/audit-replay.py 3`.

## originality

PASS

The supported distinct claim is the explicit arbitrary-axis all-exponent boundary evaluation, the strict diamond transition and the optimizer description for this contour family. The general capacity problem, closed-set duality and measure-overlap principle are not new. This is a bounded originality finding, not a historical-priority certification.

## value

PASS

The optimal equality-event mass is not obtained by considering the projection lengths of the filled set. This explicit family shows exactly when that tempting bound succeeds, with a quantitative gap for every other exponent, and gives both an attaining construction and a forced distribution for its contour mass. That is a meaningful contour-specific dependence result, not just application of a numerical capacity test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
