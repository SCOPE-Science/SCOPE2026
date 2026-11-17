# Independent mathematical audit

## correctness

PASS

For F(n)=binom(n,5), Vandermonde with h=2^(k+2) shows each difference binom(h,j) divisible by 2^k for 1<=j<=5; at n=1 a half-period h/2 has valuation k-1, giving least period P_k=2^(k+2). On each residue input branch n=r+8t, r=0..7, exact polynomial expansion has depth d_r=(3,1,2,1,3,1,2,1), odd normalized linear coefficient and all higher coefficients with at least one extra power of 2. Consequently normalized branch t->u_rt+2H_r(t) is an exact bijective 2-adic isometry and maps onto F(r)+2^d_r Z2. Summing eight Haar pushforwards gives w(y)=1/2+(1/2)1_{2|y}+2 1_{8|y}. Integration over y+2^k Z2 and multiplying by minimal-period length gives c_k(y)=2+2 1_{2|y}+8 1_{8|y}, k>=3, plus (6,2),(8,2,4,2) at k1,k2. Direct 2-adic branch comparisons of columns1–4 yield at most two density levels, with three first at column5. A new independent complete least-period enumeration corroborated c_k for k=1..9, with levels {2,4,12} at every k>=3; finite checking is not an infinite proof.

## originality

PASS

The least period 2^(k+2) is already in OEIS A349593/A385557 and fixed-column 2-adic surjectivity is Sun–Zhang Corollary 1.2; both credited. Barat–Grabner proves bivariate triangular-index asymptotic distribution rather than the exact vertical column n choose 5. The indexed cubic-column dyadic law has two rather than three levels. The exact three-level fifth-column multiplicities and Haar density were not covered by the inspected earlier results. Residual risk is a preexisting unindexed exact fifth-column distribution.

## value

PASS

Sun–Zhang’s universal-image problem makes fixed binomial columns natural arithmetic objects. Exact count of each output residue through the true minimal period is a useful finer invariant not implied by coverage or period tables. The fifth column exhibits the first three-stratum 2-adic image density among initial lower indices, with a complete infinite-level structural branch proof and exact 2/4/12 multiplicities. This is a motivated local-distribution classification rather than an arbitrary small finite modulus table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
