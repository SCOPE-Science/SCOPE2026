# Independent mathematical audit

## correctness

PASS

At each prime the quotient valuation is the sum over powers p^j of max(0,N_{p,j}-1). A term can contribute only if two window terms share the power, hence p^j divides a nonzero difference (i-i')c and j<=v_p(c)+floor(log_p k). This gives the claimed period divisor c*lcm(1,...,k). CRT separates the means, and every odd-prime sum has odd numerator. For the binary mean m_t of a consecutive window, separating out even terms yields exactly (1): halving a window of u even terms costs u-1 in valuation. Both child pairs in the proof have one odd and one even numerator over a common power-of-two denominator, including the m_2,m_3,m_4 bases. This excludes equality and opposite unit values in adjacent pairs for u>=2. Thus only t=3 and its doublings give zero, and only powers of two give unit means, with m_{2^r}=(-1)^(r-1) for r>=1. For the arbitrary stride, the classes v_2(n)=j<e contribute the fixed sign (-1)^(kj) with weight 2^(-j-1), and the divisible class contributes 2^(-e)*(-1)^(ke)*m_{k+1}; its odd unit is a residue permutation. For even k and positive e the odd-length m has modulus<1, so the mixture is positive; for odd k its zero requires m=(1-(-2)^e)/3, namely 1 or -1 at e=1 or 2 and outside [-1,1] beyond. This proves all branches including k=1. Independently enumerated 190536 starts over complete periods for 128 (k,c) pairs via the telescoping identity G=product_i gcd(lcm of earlier terms, next term). Computing each gcd by lcm of pairwise gcds and evaluating Liouville by a sieve gives exactly the predicted finite zero set.

## originality

FAIL

The exact uniform classification follows from already indexed stronger ingredients, not merely from a known period or a table of special cases. The exact AP value-frequency law yields the mixed signed mean by a direct residue-class substitution and evaluation at -1; the same-day consecutive result supplies exact binary word sums strong enough to give both their zero set and all their unit extrema. Combining them gives all three frozen branches by a scalar geometric sum. This is demonstrable coverage by implication and does not infer priority or order from same-day dating.

## value

FAIL

Uniform sign balance is a natural question and the even-stride families are a useful way of presenting its answer. But as a distinct contribution the frozen result is a direct specialization and mixing of the available exact PGF and exact consecutive word-sum results. No separate useful invariant or bound beyond their evaluated arithmetic consequence is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
