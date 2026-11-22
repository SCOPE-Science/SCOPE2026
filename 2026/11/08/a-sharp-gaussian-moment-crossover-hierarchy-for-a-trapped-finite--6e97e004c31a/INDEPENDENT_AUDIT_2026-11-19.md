# Independent mathematical audit

## correctness

PASS

For all R,T>0 the Markov generator for (X,S), S in {-1,0,1}, gives m_k=h_(k-1), (k-1+R)h_(k-1)=(k-1)u_(k-2), and (k+R+T)u_k=(k+T)m_k. At even k these imply m_(2j)/m_(2j-2)=(2j-1)(T+2j-2)/[(R+2j-1)(R+T+2j-2)], with m0=1 and m2=T/[(R+1)(R+T)]. Hence Q_n is exactly the stated product for every integer n>=2. Its log derivative is sum of d_R(T+2j-2)-d_R(T), where d_R(x)=R/[x(x+R)] strictly decreases, so Q_n strictly decreases. As T->0, Q_n~const*T^(1-n)->infinity; as T->infinity, Q_n tends to product_(j=2)^n (R+1)/(R+2j-1)<1. Thus a unique positive root exists with the claimed signs. The n=2 identity reduces to R^2+R-RT-T^2-2T=0 and the stated positive root. Gamma products yield m2n~[c Gamma((R+1)/2)Gamma(R/2)/(2sqrt(pi))]n^(-(R+1)) at T=c/n, while (2n-1)!!m2^n~sqrt(2)e^(-c/R)[2c/(eR(R+1))]^n. Uniformity for c in compact positive intervals brackets c_n=nT_n and the root expansion gives c_n=c_R[1-((R+1)log n-B_R)/n+O_R((log n)^2/n^2)]. This is for fixed R>0 only. Independently reconstructed an exact conditional-state generator solution and compared 60 rational moment cases through degree 30, simplified two symbolic fourth-cumulant/root identities, and solved 12 high-precision roots for R=0.2,1,3 and n=20,100,1000,10000. Their error behavior corroborates (not proves) the analytic asymptotic. The source tree was independently recomputed from its seven actual Git blob SHAs and matches the assigned tree.

## originality

PASS

Best-of-knowledge, narrow derived-theorem originality: the stationary law and all raw moments were already published, and a separate published theorem explicitly covers the n=2 fourth-cumulant crossing. The inspected primary papers and published mathematical results do not state the full simultaneous n>=2 uniqueness/sign classification or the double-scaling critical-rate law with explicit logarithmic correction. These nontrivial properties require extra monotonicity and uniform asymptotic arguments beyond writing the moment product. The pass does not assign originality to the model, moment recurrence, beta product, the known fourth-moment special case, or the full density.

## value

PASS

The stationary three-state harmonic particle is a natural physical stochastic model and variance-matched Gaussian excess is a natural nondimensional measure of high-order non-Gaussianity. Exactly one sign change for every even order n>=2 gives a full qualitative phase classification over a continuous two-rate family. The sharp nT_n limit and (log n)/n displacement identify a singular order-dependent boundary not available by a fixed-order kurtosis sign calculation; a researcher can use the exact boundary to distinguish long-rest intermittency at increasing moment sensitivity. The all-n asymptotic and exact uniqueness are substantive information rather than renaming a known table or merely enumerating small cases. This is a natural derived structural theorem, not an assertion of distributional dominance or novel raw moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
