# Independent mathematical audit

## correctness

PASS

I reconstructed the U-statistic and studentizer. Deleting observation i changes f_1 to (n f_1-2g_i)/(n-2); the jackknife for sqrt(n) f_1 f_2 gives exactly the stated factor 4(n-1)/(n-2)^2. In the no-overlap cell, the counts give Q_n=AB[(A+B)/4-AB/n]/(n-1)^2. As the margins concentrate at np_n, this is asymptotic to np_n^3/2 on zero overlap, while f_1 is asymptotic to -p_n^2. Both half-signs are negative with probability tending to one below criticality. At criticality, fixed C_1=k>0 gives Q_n=k/4+o_P(1): the joint-one cells contribute this leading term, the O_P(sqrt(n)) singleton cells have squared deviations O_P(1/n), and the joint-zero terms contribute O_P(1/n). The sign in the second half is asymptotically nonzero on each fixed count since theta is noninteger. Tightness of the overlap counts reduces extended-real convergence to these conditional limits, including the signed divergence for C_1=0. The exceptional zero denominator has vanishing probability. For theta=1/2, the Gaussian threshold is strictly between the k=3 and k=4 positive values, giving the two stated Poisson rejection events and size 0.3685686509430986. In line 86, the exact first overlap term should be n C_r/(n-1), not C_r; the omitted C_r/(n-1) is o_P(1) and the preceding exact formula and subsequent limit are correct. I also rederived the Gaussian branch: W=(X-p)(Y-p) has variance p^2(1-p)^2 and Lyapunov ratio asymptotic to 1/(np^2). In both halves sqrt(n) f_r/[p(1-p)] is asymptotically standard normal since empirical-mean product error is O_P(p/n). In the first half 2(n-1)(g_i-f_1)/n is the centered vector of empirical-centered products (X_i-A/n)(Y_i-B/n). Replacing that vector by the population-centered products costs o_P(sqrt(n)p) in Euclidean norm by binomial mean concentration. The same fourth-moment ratio bounds the relative variance of the second moment, so the rescaled studentizer divided by p(1-p) tends to one. Independence and the limiting second-half sign preserve the standard normal limit.

## originality

PASS

Pass applies to the studentized magnitude and resulting sparse limits, not invention of cross-HSIC, the Gaussian branch, or the published critical Bernoulli Poisson-sign example. Prior sign information cannot determine the 5% size or either escaping tail mass without analysis of the studentizer. Primary-text scope beyond the reported comparison remains an access risk.

## value

PASS

Under exact independence, Gaussian calibration can reject with asymptotic probability one even though the two margins are each well populated. The diverging rate and critical magnitude law distinguish this effect from a modest normal-approximation error; the nominal 5% example quantifies an actual decision threshold. The result locates the failure in the cross-cell and the studentizer, rather than in independence itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
