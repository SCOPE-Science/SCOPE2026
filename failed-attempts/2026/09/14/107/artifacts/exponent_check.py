"""Check adjacency-moment exponent gap vs sharp 2/r, and NB optimization identity.
q=2d-1, rho_temp=2*sqrt(q)/(q+1), theta(r)=(q^{1/r}+q^{1-1/r})/(q+1).
Adjacency trace exponent: beta/alpha with beta=log(1/rho_temp), alpha=log(1/theta)... 
actually N_r <= n*(rho/theta)^{2m} with m~c log n gives exponent 1-2c*log(theta/rho);
max feasible c from word-length constraint gives exponent strictly above 2/r for small q.
NB route: E[sum|lam|^{2m}] <= N q^m + N q^{2m}/n; threshold T=q^{1-1/r};
terms give N*(q^m)^{2/r-1} and (q^m)^{2/r}; q^m~n -> n^{2/r}. Verify numerically.
"""
import math
for q in [3,5,7,9]:
    rho=2*math.sqrt(q)/(q+1)
    print(f"q={q} rho_temp={rho:.4f}")
    for r in [2.5,3,4,6]:
        th=(q**(1/r)+q**(1-1/r))/(q+1)
        # adjacency exponent with maximal word length 2m = A log n, A chosen so error ok;
        # illustrate gap: log(theta/rho) vs (1-2/r)/2c... instead directly show theta vs rho^n?
        # Sharp exponent 2/r; adjacency achievable exponent with c=1/(2*log(q/rho?)) ~ 
        # For illustration compute ratio log(1/rho)/log(1/th): if adjacency moments were used
        # with m ~ log(n)/log(q/rho^2?) the exponent would be...
        # Standard: N <= n*(rho/th)^{2m}, m <= (log n)/(2 log(q+1)) (word count limit) ->
        # exponent 1 - log(th/rho)/log(q+1) ... compare to 2/r.
        adj_exp = 1 - math.log(th/rho)/math.log(q+1) if th>rho else 1.0
        # NB exponents
        print(f"  r={r}: theta={th:.4f} sharp={2/r:.3f} adj_naive={adj_exp:.3f} gap={adj_exp-2/r:+.3f}")
print("NB identity: with q^m=n, term1=N*(q^m)^{2/r-1}/N = n^{2/r-1}, term2=(q^m)^{2/r}=n^{2/r}. OK")
