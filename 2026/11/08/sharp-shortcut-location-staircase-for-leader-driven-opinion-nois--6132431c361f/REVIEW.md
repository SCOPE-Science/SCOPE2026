# Independent mathematical audit

## correctness

PASS

For follower grounded unit path L0, the exact inverse Green matrix G(i,k)=min(i,k) is verified by boundary and interior finite differences. A new edge of conductance omega from leader 0 to follower j yields L=L0+omega e_j e_j^T, so Sherman–Morrison yields exact inverse-trace gain Delta=omega S_n(j)/(1+omega j), S_n(j)=sum_i min(i,j)^2=n j^2-(2/3)j^3+(1/2)j^2+j/6. The sign of adjacent gain Delta(j+1)-Delta(j) is the sign of A=(n-j)(2j+1)+(omega j(j+1)/6)(6n-8j-1). Before j0=ceil((6n-1)/8), A>0; after j0 it crosses once at positive omega_{n,j}=6(n-j)(2j+1)/(j(j+1)(8j+1-6n)), strictly decreasing with j. Thus all maximizing sites, adjacent-only ties and monotone staircase follow. For omega fixed, j_opt/n→3/4 from threshold estimates, gain/n²→3/8, total trace/n²→1/2, residual fraction→1/4. For n omega_n→c>0, uniform objective convergence yields F_c(u)=c(u²−2u³/3)/(1+cu) and its unique root u_c in (3/4,1). Exact independent inversion of augmented Laplacians for n≤10 and threshold checks at small n supplement, not replace, the all-size proof; Brownian convention gives stationary covariance L^{-1}/2.

## originality

PASS

The exact finite-conductance rank-one gain formula for noisy leaders is established by Xu–Zhang (2023) and expressly credited. The new theorem derives closed form and complete all-n, all-conductance staircase and scaling on the unit rooted path. Inspected broader greedy edge algorithms do not logically assert these sharp closed-form site thresholds, while spectral-eigenvalue optimality and perfectly pinned leader selection are different objectives. A 2026 grounded-path resistance preprint was only accessible descriptively and remains a concrete priority risk.

## value

PASS

The one-added-link intervention in noisy social networks is a natural optimization problem. This theorem gives all finite-size rational switching weights, every unique/tied optimal site, and the exact 3/4 placement and 75% variance-removal limit, illustrating a non-obvious strength-dependent location effect. It provides a meaningful closed-form benchmark for graph-design algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
