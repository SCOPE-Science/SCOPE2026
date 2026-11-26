# Independent mathematical audit

## correctness

PASS

Independently cut the replaced bond in J=2 Re(T), with p its bulk weight, v the other weight and S=a+b. Exterior eigenvalues satisfy c^2=Q_m P, the product of the left and right inverse endpoint resolvents. Both are positive and increasing for lambda>S, and their product tends to infinity. For lambda^2=S^2+4ab sinh^2(kappa), the right decaying continuation gives P=p lambda/(p+v exp(-2 kappa))=p+2D kappa+O(kappa^2). At lambda=S the left Dirichlet solution is L_i=sum_{q=-1}^{i-1} 1/w_q with fictitious w_{-1}=b and alternating w_q, so Q_m(S)=p+1/L_m. L_m is (m(a+b)+2a)/(2ab) when m is even and (m+1)(a+b)/(2ab) when odd. This gives both exact thresholds and their stated second coefficients. Differentiating the finite inverse-resolvent recurrence Q_i=lambda-w_{i-1}^2/Q_{i-1} gives Q_m'(lambda)=sum_{i=0}^m (L_i(lambda)/L_m(lambda))^2 <=m+1: the positive Dirichlet solution is increasing because w_i(L_{i+1}-L_i)=(lambda-S)L_i+w_{i-1}(L_i-L_{i-1}). Thus Q_m(lambda)-Q_m(S)=O(m kappa^2). Taking the square root of Q_m P gives the needed uniform linear term (D+O(m^-1)) kappa and O(m kappa^2) error. Monotone bracketing gives m^2 kappa -> (xi-B_j)/D above threshold and o(1) at equality if an outlier exists; below threshold there is none. Since w-E=D kappa^2+O(kappa^4), the constants and factor of two are correct. On the right the two-cell multiplier is exp(-2 kappa) and the within-cell ratio tends to one. The largest left amplitude is bounded by lambda/c times the first right amplitude by the recurrence at m+1. Therefore left mass is O(m) times the squared boundary amplitude whereas right mass is asymptotic to that squared amplitude divided by 2 kappa. This proves the stated normalization, and a fixed exponential upper bound in the rescaled variable gives strong L2 convergence. A bounded independent high-precision inverse-impedance check with a=1,b=2 and xi=-13/18 found no even outlier at 80,160,320 and odd rescaled gaps 0.00292,0.00371,0.00415 at 81,161,321, consistent with 1/216, not a proof of the limit.

## originality

PASS

The novelty that survives is the quartic gap coefficient and strong normalized eigenmode in the joint depth/coupling window for unequal period-two weights. The finite thresholds, their Taylor coefficients and the strict above/below-threshold parity selection follow from prior work and are not original contributions.

## value

PASS

A sharp threshold does not give the energy or the distance over which the bound state is spread. This fine window yields a quantitative parity-selective onset and a normalized mode at an emergent m^2 scale, resolving the spectral response exactly where fixed-c asymptotics and the coarse m-scale window need not resolve it. The scaling is dictated by the leading threshold correction and quadratic band-edge dispersion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
