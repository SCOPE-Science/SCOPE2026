# Independent mathematical audit

## correctness

PASS

A maximum-index update is precisely an endpoint maximum in the enlarged window; on the circle each index's winning starts lie in one contiguous arc within the k starts containing it. Since n>k, there is more than one winner, so the number of cyclic runs equals the number of distinct winners and the number of transitions. For a separate local check, condition on the largest among the k+d+1 sites for 1<=d<=k. If it is at either outer endpoint, the other interval contributes an endpoint with probability 2/(k+1) by rank symmetry; there are two such placements. A union maximum at a shared site can contribute only when the shared site is an endpoint of both enlarged windows, i.e. d=k, giving an extra 1/(2k+1). Disjoint intervals are independent. This gives both signs and the exact harmonic variance after summing each of the two orientations of lags 1 through k. Jensen on the k denominators k+2 through 2k+1 has strict average reciprocal greater than 2/[3(k+1)], which yields the stated lower bound; k times the explicit variance tends to 8 log(2)-5. The nondegenerate bounded stationary k-dependent CLT applies at each fixed k, and the cyclic sum differs from an appropriate linear sum by at most k terms. The frozen exact-enumeration checker was read, not executed.

## originality

FAIL

The principal claim is mechanically recoverable from the published all-length linear count distribution already cited by the record. For fixed k let M_N be the linear count of distinct k-window maxima, m=N-k, and U_m=Var(M_{k+m}). A linear winning index never reappears after its contiguous run, so M_{k+m}=1+sum of the m stationary update indicators. Writing c_d for the linear lag covariance gives 2c_d=U_{d+1}-2U_d+U_{d-1}. This exact inversion is available from the *family* of prior scalar laws; the claim that a scalar law does not determine individual lags applies only at a single sample size. Moreover it gives the precise closed formulas by two y-derivatives of Austin et al.'s published generating recurrence. In the accessible mathematical restatement Eq. (1), v_x=yv^2+(1-y)P, where P=sum_{j=1}^{k-1} j x^(j-1), v(0,y)=1, and v(x,1)=1/(1-x). Put A=(1-x)^2 v_y(x,1), B=(1-x)^2 v_yy(x,1). Then A=x^k[1-(k-1)x/(k+1)] and B'=4A/(1-x)+2A^2/(1-x)^2. The exact means are 1+2m/(k+1), so the variance second difference gives c_d=(1/2)[x^(k+d+1)]B-(2/(k+1))^2. For 1<=d<=k the coefficient equals (8/(k+1)+2*1_{d=k})/(k+d+1) immediately from B'; this is exactly the frozen rational kernel, including its sign reversal. These linear covariances are the cyclic local covariances up to wrap reversal under the stated n bound. For the aggregate itself, rotate the global maximum to a fixed site and delete it: windows containing it all choose it, and every other window is in the remaining n-1 consecutive sites, which have uniform relative ranks. Thus the cyclic total has exactly the prior linear count law at N=n-1 plus one, stronger than just inherited first and second moments. No available primary body is claimed to state these reductions, but the explicit implication needs only the verified restatement of the prior theorem. The new proof is a transparent local explanation, not a distinct uncovered invariant.

## value

FAIL

The negative-to-positive transition is an informative way to explain dependence, and the short local proof has pedagogical value. But the exact invariant is an elementary extraction of the earlier count generating theorem, the aggregate circular law reduces directly to it, and the fixed-width CLT is standard. The frozen package does not isolate a surviving unknown structural claim beyond that extraction. No repair is justified for this record without a substantively different result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
