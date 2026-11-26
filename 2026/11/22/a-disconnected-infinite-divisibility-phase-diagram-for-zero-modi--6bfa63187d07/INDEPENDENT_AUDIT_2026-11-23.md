# Independent mathematical audit

## correctness

PASS

Summing the masses with t=theta+1 and c=theta²/t gives F(z)=c(t+1-z)/(t-z)² and G=pi+(1-pi)F. For p_0>0 the Taylor coefficients are (2 t^(-n)-sum r_j^(-n))/n, where r_j are the finite numerator roots. When 0<pi<1, the quadratic in s=t-z is pi s²+(1-pi)c(s+1); both roots have negative real part, so the corresponding z roots have modulus >t. At pi=0 the single root is t+1; pi=1 gives the point mass. In the negative branch set q=(1-pi)c/(-pi); the positive root of s²-q(s+1)=0 rises strictly from t to infinity, putting one z root rho down from zero through -t, and the other eta stays >t. The equation at rho=-t is q=4t²/(2t+1), giving the displayed pi_* and its strictly positive distance from pi_min. For rho<=-t even coefficients are bounded below by (t^(-n)-eta^(-n))/n>0 and odds are positive as well. For -t<rho<0, negative even coefficients eventually dominate. Real iid roots with p_0>0 cannot have a negative part (all copies could be negative); they must have an atom at 0 and then lie on the integer lattice, since the other copies can all be zero. At truncation, the shifted PGF has a single numerator zero t(theta+3)/(theta+2)>t, so its log coefficients are positive and summable and G=zH gives explicit fractional-shift real roots. Integer roots at truncation cannot exist for order m>1 since the minimal possible summed integer count would be m times the least supported count, not 1. The boundary coefficients remain strictly positive at every fixed degree, so continuity at fixed positive p_0 provides the arbitrarily late obstruction; no finite enumeration is needed. For theta=1 the right-hand boundary roots are -2 and 14/5, and at pi=-1/3 I get p_0=1/6, p_1=1/3, p_2=5/24 and lambda_2=-3/4. The first two raw moments are 2 and 22/3, so the overdispersion example also checks. Frozen checker read, not executed; the mass recurrence it uses follows from G'=G(log G)' and is independent as a finite coefficient computation.

## originality

PASS

The phase classification for this exact zero-modified family, especially the conjunction of a sharp deflation cutoff with an isolated shifted endpoint, survives the comparisons. The model, standard lattice compound-Poisson criterion, and expansion of rational logarithms are not contributions. Earlier work on the isolated endpoint specifically remains a priority risk.

## value

PASS

For an established model whose defining flexibility is zero inflation and deflation, the two notions of divisibility give genuinely different phase diagrams, and the isolated ordinary-ID law cannot be read from the coefficient test for positive zero mass. The result both supplies the exact admissible region for a jump interpretation and explains why finite coefficient screening or overdispersion can falsely suggest it. No empirical jump mechanism or inference guarantee follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
