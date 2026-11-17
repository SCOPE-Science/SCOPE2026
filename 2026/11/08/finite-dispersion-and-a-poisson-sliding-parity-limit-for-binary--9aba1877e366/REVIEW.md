# Independent mathematical audit

## correctness

PASS

Deleting a contiguous fixed-length b-block at positions i and j gives identical descendants iff all x_t=x_{t+b} for i<=t<j, implying B_b(x)=1+sum_{i=0}^{n-b-1}1{x_i!=x_{i+b}}. Independent flip signs eta_j=(-1)^xi_j yield E Z_i=a^b, E Z_i Z_{i+h}=a^{2h} if h<b or a^{2b} otherwise; summing covariance proves stated exact mean and variance for n>=2, 1<=b<=n, p in [0,1], including N=0. For p_n=lambda/n and b_n/n->alpha in (0,1), sparse flips give Poisson point-process convergence; sliding-window parity Riemann approximation yields L=integral_0^(1-alpha) 1{Pi((t,t+alpha]) odd}dt, with mean, integrated variance, non-Gaussian atom and one-point density. Independent exhaustive deletion-output direct count over 1536 finite (n,b,word) cases and exact Bernoulli flip moments on small cases corroborated, rather than proving the limit.

## originality

PASS

Against full submitted theorem and inspected sources: Natural specific formula distinct from checked prior claims, with clear residual priority risks. The natural distinct-output count of a one-burst deletion channel under a correlated binary source admits exact finite dispersion and a non-Gaussian macroscopic-burst sparse-flip limit; the occupation/variance and atom a

## value

PASS

The natural distinct-output count of a one-burst deletion channel under a correlated binary source admits exact finite dispersion and a non-Gaussian macroscopic-burst sparse-flip limit; the occupation/variance and atom are useful for typical channel ambiguity and represent a meaningful scaling boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
