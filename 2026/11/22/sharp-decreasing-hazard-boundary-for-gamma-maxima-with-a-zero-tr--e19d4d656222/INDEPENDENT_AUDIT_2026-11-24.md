# Independent mathematical audit

## correctness

PASS

With t=beta*z, the conditional Poisson generating function gives survival (1-exp(-lambda*Q))/(1-exp(-lambda)) and hazard beta*lambda*f/expm1(lambda*Q). Using Q'=-f and f'/f=(alpha-1)/t-1, direct logarithmic differentiation gives (f/Q)[V(lambda*Q)-1-m']; the sign is unchanged on changing from t to z. The integral m=integral_0^infinity exp(-y)(1+y/t)^(alpha-1)dy has strictly negative derivative for alpha>1, zero for alpha=1, and strictly positive derivative for alpha<1. Differentiation is dominated on compact positive t intervals. For alpha>=1, V>1 gives strict increase. Otherwise V is strictly increasing onto (1,infinity), so its inverse defines the unique pointwise intensity at derivative zero. Put a=1-alpha: at zero m~Gamma(alpha)t^a, and m'=-1+m(1+a/t)~a*Gamma(alpha)t^(-alpha). At infinity t^2*m'=a*integral exp(-y)y(1+y/t)^(-a-1)dy -> a, and Q~f. Since V(u)-1~u/2 at zero and V(u)~u at infinity, the age-dependent critical intensity diverges at both endpoints. It is continuous and positive inside, so attains a positive finite minimum. Below it the derivative is everywhere negative; at equality it is nonpositive with no constant interval by analyticity and the negative endpoint signs. Above it there is a positive derivative at a minimizing age and negative derivatives on both sides sufficiently far away. Minimizing and maximizing on intervals bracketed by the derivative signs gives an interior minimum and a later maximum; no uniqueness follows or is claimed. Replay python3 -B /workspace/reproductions/4.py uses half-integer survival formulas and finite differences (12 sign checks, illustrative half-shape crossing about 1.65543269); neither that grid nor the frozen script certifies a global minimum.

## originality

PASS

The 2023 distribution, hazard and alpha=1 increasing result are prior. The distinct mathematical claim is the sharp global phase classification, particularly the attained, positive finite iff threshold for subunit shape and the strict boundary/turning-point behavior. The closest prior calculation gives the same model but works with a different derivative and stops short of that classification. This is a bounded comparison, not an assertion of historical priority for the model.

## value

PASS

The model is established in reliability analysis; being able to decide strict DFR globally rather than read off plots or a sufficient shape diagnostic resolves a real ambiguity. The rate-free scalar threshold includes the critical case and explains why a large sampling intensity adds an intermediate increasing interval without changing the endpoint signs. This goes beyond recovering the distribution or differentiating at individual ages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
