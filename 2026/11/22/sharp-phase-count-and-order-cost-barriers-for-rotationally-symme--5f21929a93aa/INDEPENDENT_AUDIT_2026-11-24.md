# Independent mathematical audit

## correctness

PASS

For fixed p, roots-of-unity averaging deletes every Taylor term except positive degrees congruent to p modulo n (the zero degree was subtracted). If n>=p, the analytic Taylor remainder after filtering is O(|sigma X|^(p+1)) within a smaller holomorphic disk. Gaussian tails and global boundedness control its complement in L2 even with the factor sigma^(-p). Thus the limit is u^(p)(0) H_p(X) X^p/p!. For n<p the shared radial cutoff leaves exactly the two aliased monomials in RESULT.md:55–69. After rescaling by sigma^(p-m), the sample converges in L2 to H_p(X) X^m/m!, whose mean is zero by Gaussian integration by parts. Evaluating the Hermite product against X^(2m) gives the stated strictly positive C_(p,m) and the special value (2p+1)p!. For m=p, the mean is one and the second moment yields the binomial sum. In the Legendre integral at 3, put S=3+2 sqrt(2); near theta=0 the integrand base is S-sqrt(2) theta^2+O(theta^4). The half-Gaussian factor and central binomial coefficient give exactly (1+sqrt(2))/(pi 2^(5/4)) and growth base 2S. Probe averaging gives V_p/K in the fixed-order zero-radius limit, not in an arbitrary joint limit. Variance on the general complex class can be read as E|Y-EY|^2; the radial witnesses are real without any extra condition outside the disk. Independent replay: python3 /workspace/review_checks.py 1, 77 exact direct polynomial moment comparisons; the finite tests do not establish the limiting claims. The frozen checker was inspected, not executed.

## originality

PASS

Credit the published sufficient phase count, root filter and fixed-order Gaussian moment structure to Fang et al. The distinct contribution supported by this comparison is necessity on the same bounded locally holomorphic class with exact bad-phase rates, plus identification of the sharp sequential sampling cost for these admissible RSSE witnesses. Neither the special functions nor their asymptotics are new in isolation.

## value

PASS

Variance stability as smoothing vanishes is distinct from affordability as derivative order rises. A normalized admissible family pinpoints the necessary phase budget and demonstrates why additional phases cannot reduce independent-probe cost on that family. This is a specific estimator diagnostic, not an estimator-independent lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
