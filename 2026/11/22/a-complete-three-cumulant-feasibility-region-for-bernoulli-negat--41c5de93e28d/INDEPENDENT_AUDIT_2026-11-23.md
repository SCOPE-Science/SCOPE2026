# Independent mathematical audit

## correctness

PASS

The pgf about 1 factors as (1+pz)(1-az)^(-nu), a=theta/(1-theta). Its log yields m=p+nu*a, v=-p^2+nu*a^2, and t=kappa_[3]/2=p^3+nu*a^3. For fixed m,v the positivity of A=m-p and B=v+p^2 together with 0<p<1 is equivalent to max(0,sqrt(max(0,-v)))<p<min(1,m); this interval is nonempty exactly under the two stated strict prerequisites. Positivity gives the unique inverse a=B/A, nu=A^2/B. The third-coordinate function F=p^3+B^2/A has derivative 3p^2+4pB/A+B^2/A^2>0. At p=0 (v>=0) or p=sqrt(-v) (v<0) its limiting values are v^2/m and (-v)^(3/2). At the upper end m<=1 there is a genuine divergence since v+m^2>0, including m=1; for m>1 the limit is 1+(v+1)^2/(m-1). This proves strict necessity and sufficiency and uniqueness; the implicit function theorem with positive F' yields smoothness also at v=0 or m=1 at interior parameter points. For feasible negative v, approaching p=sqrt(-v) gives a->0, nu*a->m-sqrt(-v)>0, so the negative-binomial term tends to a Poisson term by its pgf and t tends to the unattained lower limit. Bin(N,q) has t/(-v)^(3/2)=1/sqrt(N), proving the stated incompatibility. The rational match has (m,v,t)=(1/2,-1/8,61/800), versus t=1/32 for Bin(2,1/4). Scope: population factorial cumulants of the strictly interior independent convolution, not a sample or boundary-model theorem.

## originality

PASS

Best-of-knowledge pass for the explicit image and unique smooth three-cumulant inversion with the sharp binomial obstruction, not for the count law, its PGF, or standard component cumulant calculus.

## value

PASS

For a specifically proposed count model, the attainable set determines whether a three-moment fit exists and whether its parameters are unique, including near the underdispersed boundary. The sharp obstruction distinguishes the family from multi-trial binomials even when the first two moments can match. This is a useful complete feasibility result, not merely the standard log-PGF derivative calculation or a claim about estimation from finite samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
