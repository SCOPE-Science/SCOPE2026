# Independent mathematical audit

## correctness

PASS

For PSD A with real Gaussian probes, exact MSE is (T-sum_i mu_i)^2+(2/m)sum_i mu_i^2, with real compressions characterized precisely by Cauchy/Fan–Pall intervals lambda_(i+n-r)<=mu_i<=lambda_i plus descending order. Strictly convex optimization on the larger product box gives mu_i=clip(tau,I_i) with unique positive root sum clip(tau,I_i)+2tau/m=T. Monotone interval endpoints preserve descending order, so Fan–Pall ensures real attainability. Corner KKT gives the top-space criterion. Explicit A=diag(10,2,0),r=2,m=3 has optimum mu=(6,2), MSE=128/3 vs principal 208/3; independently recomputed.

## originality

PASS

Classical Gaussian variance, Fan–Pall interlacing, Hutch++, and fixed-basis truncated infHutch supply ingredients; no inspected accessible theorem solves the exact deterministic rank-r oracle subspace MSE minimization with unique clipped Ritz spectrum and sharp top-subspace boundary. The most plausible 2026 primary source was inaccessible; originality explicitly qualified rather than incorrectly failed.

## value

PASS

The optimum gives a sharp benchmark for bias–variance subspace selection and a concrete failure of the naive rule to retain top eigenvectors, even for rank<=r. Precisely quantifies when deliberate projection bias is beneficial; relevant independent finite-dimensional design fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
