# Gaussian Voronoi boundary layers and Chernoff-sharp convergence for atomic Bernstein–Durrmeyer operators

## Finding
For an arbitrary fixed finite collection of distinct interior atoms, the Bernstein–Durrmeyer operator has a complete pointwise limit profile on the entire interval. It quantizes inputs according to Bernoulli Kullback–Leibler bisectors, with a universal Gaussian interface at every bisector. On its atomic support, its \(L^2\) error decays at the exact Chernoff exponent with the sharp \(n^{-1/2}\) polynomial factor:
\[
\|I-T_n\|_{L^2(\rho)\to L^2(\rho)}=\Theta\!\left(n^{-1/2}e^{-nC_*}\right).
\]
Here \(C_*\) is the smallest Chernoff information of adjacent Bernoulli atoms. The result includes any number \(r\ge2\) of atoms and any positive atomic weights.

## Assumptions and scope
Let \(r\ge2\), \(0<a_1<\cdots<a_r<1\), and \(w_i>0\). Define \(\rho=\sum_{i=1}^r w_i\delta_{a_i}\). For arbitrary real data \(f_i=f(a_i)\), write
\[
b_{n,k}(x)={n\choose k}x^k(1-x)^{n-k},\quad
(M_nf)(x)=\sum_{k=0}^n b_{n,k}(x)
\frac{\sum_j w_jb_{n,k}(a_j)f_j}{\sum_jw_jb_{n,k}(a_j)}.
\]
The denominator is positive for every index because the sites lie strictly inside \((0,1)\). The notation \(T_n\) means restriction of this polynomial to the \(r\) sites, acting on \(L^2(\rho)\cong\mathbb R^r\).

Set \(\ell_i(t)=t\log a_i+(1-t)\log(1-a_i)\). For \(1\le i<r\), let \(c_i\) be the unique point where \(\ell_i(c_i)=\ell_{i+1}(c_i)\):
\[
c_i=\frac{\log[(1-a_i)/(1-a_{i+1})]}{\log[a_{i+1}(1-a_i)/(a_i(1-a_{i+1}))]},\quad a_i<c_i<a_{i+1}.
\]
Put \(c_0=0\), \(c_r=1\). Define \(D(t\|a)=t\log(t/a)+(1-t)\log[(1-t)/(1-a)]\), \(C_i=D(c_i\|a_i)=D(c_i\|a_{i+1})\), and \(C_*=\min_iC_i>0\). Let \(\Phi\) denote the standard-normal distribution function.

For every fixed \(x\in(c_{i-1},c_i)\), \(M_nf(x)\to f_i\). For \(1\le i<r\), \(M_nf(c_i)\to (f_i+f_{i+1})/2\). In fact, for each fixed real \(h\),
\[
\lim_{n\to\infty}(M_nf)(c_i+h/\sqrt n)=
\Phi\!\left(-\frac h{\sqrt{c_i(1-c_i)}}\right)f_i+
\Phi\!\left(\frac h{\sqrt{c_i(1-c_i)}}\right)f_{i+1}.
\]
The weights do not enter these limiting interface coefficients. On every compact subset of \([0,1]\setminus\{c_1,\ldots,c_{r-1}\}\), convergence to the indicated step function is uniform with an error bounded by \(Ae^{-\eta n}\), with constants depending on the compact set, sites, and weights. Finally, for sufficiently large \(n\) there are fixed \(0<A\le B<\infty\) such that
\[
A n^{-1/2}e^{-nC_*}\le\|I-T_n\|_{2\to2}\le B n^{-1/2}e^{-nC_*}.
\]

## Proof
**1. Ordered logarithmic-likelihood envelopes.** Each \(\ell_i\) is affine with slope \(\log[a_i/(1-a_i)]\), strictly increasing with the site. Moreover, \(\ell_i(t)\) is the log-likelihood of Bernoulli parameter \(a_i\), up to a term independent of the site; for a fixed \(t\) it is strictly increasing in the parameter for \(a_i<t\) and decreasing for \(a_i>t\). Therefore its upper envelope is attained uniquely at site \(i\) whenever \(c_{i-1}<t<c_i\), and only the two sites \(i,i+1\) tie at \(c_i\). The crossing \(c_i\) lies strictly between the two adjacent sites, so the crossings are ordered. Write \(Q_{n,k}=\sum_j w_jb_{n,k}(a_j)\). The posterior coefficients \(p_{j,n}(k)=w_jb_{n,k}(a_j)/Q_{n,k}\) obey \(p_{j,n}(k)\to1\) exponentially fast when \(k/n\) remains in a compact subinterval on which \(\ell_j\) alone maximizes the envelope. If \(K\sim\operatorname{Bin}(n,x)\), then \(M_nf(x)=\mathbb E\sum_jp_{j,n}(K)f_j\). Binomial concentration proves the claimed pointwise and locally uniform exponential convergence away from crossings (including the endpoints).

**2. Normal interfaces.** Let \(x_n=c_i+h/\sqrt n\) and \(K_n\sim\operatorname{Bin}(n,x_n)\). The triangular-array binomial central limit theorem gives \((K_n-nc_i)/\sqrt n\Rightarrow N(h,c_i(1-c_i))\). For \(k\) near \(nc_i\), the posterior mass outside \(\{i,i+1\}\) is exponentially negligible. Since \(\ell_{i+1}(t)-\ell_i(t)\) is a positive-slope affine function vanishing at \(c_i\), \(p_{i+1,n}(k)\to1\) if \(k-nc_i\to+\infty\), and it tends to zero if \(k-nc_i\to-\infty\). The number of trials in the strip \(|K_n-nc_i|\le n^{1/4}\) has probability tending to zero by the binomial local bound. Splitting at this strip and applying the central limit theorem yields the displayed \(\Phi\)-mixture. Any fixed log-weight ratio shifts the posterior crossing by only \(O(1)\) trials, hence does not affect the \(\sqrt n\) interface. Set \(h=0\) for the equal midpoint limit.

**3. Binomial-overlap lemma.** For any fixed \(0<a<b<1\) and weights \(u,v>0\), let \(c\) solve \(\ell_a(c)=\ell_b(c)\), and \(C=D(c\|a)=D(c\|b)\). Then
\[
\sum_{k=0}^n\min\{u b_{n,k}(a),v b_{n,k}(b)\}
=\Theta(n^{-1/2}e^{-nC}).
\]
Indeed, the ratio of the two summands is a strictly increasing exponential in \(k\), with crossover index \(nc+O(1)\). At the crossover, Stirling's formula gives each binomial mass \(\Theta(n^{-1/2}e^{-nC})\). To the right of that index the smaller (the \(a\)-binomial) is a geometric tail because \(c>a\); to the left the smaller (the \(b\)-binomial) is a geometric tail because \(c<b\). Their fixed geometric ratios are bounded strictly below one near the crossover, so the entire sum is at most a constant times the central term, while that term supplies the matching lower bound. For nonadjacent sites, their pair Chernoff information is no smaller than \(C_*\): for fixed \(a\), this information strictly increases as the other Bernoulli parameter moves farther away on either side. This follows, for example, from the characterization \(C(a,b)=\min_{t\in[a,b]}\max\{D(t\|a),D(t\|b)\}\) and monotonicity of Bernoulli relative entropy in its second argument away from \(t\).

**4. Exact exponential norm scale.** The restricted matrix is
\[
P_{ij}^{(n)}=\sum_{k=0}^n b_{n,k}(a_i)\frac{w_jb_{n,k}(a_j)}{Q_{n,k}}.
\]
It is row stochastic and reversible: \(w_iP_{ij}^{(n)}=w_jP_{ji}^{(n)}\). Its quadratic form is nonnegative,
\[
\langle f,T_nf\rangle_{L^2(\rho)}
=\sum_{k=0}^n\frac{\left(\sum_i w_i b_{n,k}(a_i)f_i\right)^2}{Q_{n,k}}\ge0.
\]
A self-adjoint Markov contraction with nonnegative quadratic form has spectrum in \([0,1]\); therefore \(I-T_n\) is positive semidefinite. Moreover,
\[
w_iP_{ij}^{(n)}\le\sum_{k=0}^n\min\{w_i b_{n,k}(a_i),w_jb_{n,k}(a_j)\}
=O(n^{-1/2}e^{-nC_*}),\quad i\ne j.
\]
For adjacent sites attaining \(C_*\), the summand at the nearest integer to \(nc_i\) has size \(\Omega(n^{-1/2}e^{-nC_*})\); all other sites have exponentially smaller likelihoods there, so its denominator is comparable to the sum of the two adjacent likelihoods. Consequently the corresponding \(P_{i,i+1}^{(n)}\) has a matching lower bound. The positive-semidefinite trace estimate gives \(\|I-T_n\|_{2\to2}\le\operatorname{tr}(I-T_n)=\sum_{i\ne j}P_{ij}^{(n)}\), while the unit coordinate Rayleigh quotient at such an adjacent site is at least \(P_{i,i+1}^{(n)}\). This proves the sharp two-sided order and logarithmic limit. By norm equivalence on fixed finite support, the same exponential and polynomial order also holds in each fixed \(L^q(\rho)\) operator norm, \(1\le q\le\infty\); only the \(L^2\) formulation is used for the spectral argument.

## Verification
A standalone Python checker uses exact rational arithmetic for the stochastic identities, detailed balance, and principal-minor positivity on three rational interior atoms for degrees one through 21. It independently tests adjacent KL-bisector identities, six Gaussian boundary profiles at degree 1000, and rescaled off-diagonal sums for degrees 100, 200, 400, and 800. The checker is supplementary evidence; the proofs of all infinite and universal assertions are the four steps above. Run `python3 verify_atomic_durrmeyer.py` from the package directory.

## Relationship to prior work
Berdysheva (2012) established uniform approximation for arbitrary measures with full simplex support and identified questions concerning convergence for incomplete supports. Berdysheva (2014) proved pointwise recovery at support points under general conditions. Berdysheva and Li (2014) obtained \(L^p\) convergence with general \(n^{-1/2}\)-scale estimates in terms of a \(K\)-functional. Those claims do not specify the Gaussian interface at points outside finite supports or the sharp Chernoff exponential rate for operator recovery *on* the support. The earlier weighted-kernel spectral framework of Berdysheva and Jetter (2010) imposes a positivity condition excluding finite atomic support, and its Jacobi spectral formulas address continuous measures. Standard binary hypothesis-testing large deviations motivate the exponential comparison, but the full operator formulation and the uniform Gaussian boundary-layer classification require the indicated connection to the Bernstein–Durrmeyer kernel.

## Limitations
The classification assumes finitely many strictly interior atoms with fixed positive masses. It does not cover infinite atomic supports, atoms at endpoints, continuous or singular-continuous measures, higher-dimensional simplices, or measures varying with degree. The norm estimate is sharp to exponential and polynomial order; no constant-level asymptotic (which may exhibit lattice effects) is claimed. The literature search cannot exclude an unindexed equivalent treatment, and the complete text of the 2014 pointwise-convergence paper was not accessible for inspection.

## References
1. E. E. Berdysheva, *Uniform convergence of Bernstein–Durrmeyer operators with respect to arbitrary measure*, J. Math. Anal. Appl. 394 (2012), 324–336. DOI: 10.1016/j.jmaa.2012.03.004.
2. E. E. Berdysheva, *Bernstein–Durrmeyer operators with respect to arbitrary measure, II: Pointwise convergence*, J. Math. Anal. Appl. 418 (2014), 734–752. DOI: 10.1016/j.jmaa.2014.04.006.
3. E. E. Berdysheva and B.-Z. Li, *On \(L^p\)-convergence of Bernstein–Durrmeyer operators with respect to arbitrary measure*, Publ. Inst. Math. 96 (2014), 23–29. DOI: 10.2298/PIM1410023B.
4. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, J. Approx. Theory 162 (2010), 576–598. DOI: 10.1016/j.jat.2009.11.005.
