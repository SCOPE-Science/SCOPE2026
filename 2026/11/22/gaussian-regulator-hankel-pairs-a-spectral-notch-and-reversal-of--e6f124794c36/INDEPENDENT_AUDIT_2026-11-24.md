# Independent mathematical audit

## correctness

PASS

The Hankel outputs for distinct monomials have distinct angular frequencies. Gaussian radial moments give A_n, and analytic projection takes only the coefficient at degree n±m, vanishing for the minus symbol when n<m. This gives exactly B_{n,±} and the squared singular channels by Pythagoras. At finite β the residuals are nonzero because their radial factor is not the analytic monomial factor. Both are bounded, with a polynomial times exponentially decaying channel majorant; the binomial generating function and the reindexing n=m+k for the minus projection sum yield the stated common Hilbert–Schmidt square. With u=nβ→u_0>0, β^m A_n→u_0^m exp(-2u_0). The plus loss logarithm is (n+m+1)d_β, d_β=log(1+β²/(1+2β)); divided by β it tends to u_0. The minus loss logarithm adds the factorial term m²/n+O_m(n^-2) and subtracts m log(1+2β), so after division by β its limit is u_0+m²/u_0-2m=(u_0-m)²/u_0, including at the notch. The loss is 1-exp(-log loss) in each channel, where log loss denotes the nonnegative negative log of B/A. The envelope with v=β(n+1) bounds the minus spectrum by a constant times (v^(m-1)+v^(m+1))exp(-cv), and the plus by v^(m+1)exp(-cv). This follows from 1-exp(-x)≤x and the factorial logarithm bound O_m(1/(n-m+1)), treating n<m directly. It gives zero endpoints at u=0 except minus m=1: there fixed n gives 1 directly, and when n→∞, nβ→0 implies n times the minus logarithm tends to 1 and A_n/n→1. These sequential limits give compact-uniform convergence on the grid; the exponential bounds control Riemann-sum tails for every fixed p>0 and the suprema. For m=1 the two trace integrals are 1 and 2/e and the maxima 1/e and 1, giving the strict reversal. The frozen numerical checker was inspected, not executed.

## originality

PASS

Credit existing Fock Hankel ideal criteria, the known equality of Hilbert–Schmidt norms for this Lebesgue-square-integrable symbol, and prior diagonal methods. The supported distinct result is the sharp paired Gaussian-regulator profiles and their contrasting Schatten/maximum consequences, not ideal membership or equality at p=2.

## value

PASS

A Gaussian regulator turns a natural unbounded monomial pair into bounded all-Schatten test symbols. The exact notch and norm-ranking reversal exhibit how conjugation redistributes singular mass while preserving its Hilbert–Schmidt total. Sharp profiles across every fixed p and at the maximum make this a useful quantitative example beyond qualitative membership or constant-factor comparison; it is not a general solution of Berger–Coburn questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
