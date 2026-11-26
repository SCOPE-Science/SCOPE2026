# Independent mathematical audit

## correctness

PASS

The geometric and first-moment series independently give w(r)=theta^2 q^(m-3)q^(-r)(r+b)/(q^m-1), q=1+theta, b=theta+2+m/(q^m-1). Neighbor ratios strictly decrease, and their difference from 1 has the sign of H_m-r. With A=theta sum(q^k), strict AM–GM gives m^2 q^(m-1)/A^2 < theta^(-2), so H'_m<-1. Expanding the finite sum gives H_m(0+)=(m-5)/2, not attained, while H_m(infinity)=-infinity. Therefore the only nonnegative integer thresholds are j<(m-5)/2. This handles m=2 (vacuous interior concavity), m=5 (endpoint limit 0 but no tie), and m=6 (first positive threshold). In all cases H_m<m-1, so there is no missing overflow sector; every claimed unique mode occurs on an interval and any tie is exactly adjacent. For m=6 clearing theta A and removing theta^2 yields the stated sextic. For the large-m transition, A/m increases strictly in m at fixed theta; t_m increases toward t_*=sqrt(2)-1 by pointwise convergence of H_m. Its positive lower bound t_6 and the mean-value theorem give t_*-t_m=O(m(1+t_6)^(-m)), so ((1+t_m)/sqrt(2))^m tends to one. The derivative of 1/t-t-2 then gives the stated limiting coefficient 1/(4+2sqrt(2)).

## originality

PASS

Pass for the WPL-specific all-resolution threshold classification, six-sector cutoff and sharp first-threshold asymptotic, not for the underlying PMF, recurrence or the general method of comparing ratios. The strongest available analogous result concerns WDLE, with materially different cutoff and upper sector. The identical catalog entry is not evidence of earlier coverage.

## value

PASS

The result explains exactly what angular discretization is required for a moving modal sector in an existing circular distribution, and how the first transition approaches its unwrapped threshold. The unique global phase transitions, including the low-resolution obstruction, are not just plots or a numerical rerun of the PMF.

The dated certificate retains the supplied scientific assessment, sources and limitations.
