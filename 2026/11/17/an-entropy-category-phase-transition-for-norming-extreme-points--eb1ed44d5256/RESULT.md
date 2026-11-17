# An entropy–category phase transition for norming extreme points of bidual block averages

## Finding

For each real \(c>0\) there is an explicit norm-one operator \(T_c:c_0(\mathbb N;\mathbb R)\to c_0(\mathbb N;\mathbb R)\) such that neither \(T_c\) nor its first adjoint attains its norm, while its second adjoint has a dense \(G_\delta\) set of norming extreme points in the sign cube \(\{-1,1\}^{\mathbb N}\). This norming set has Hausdorff dimension one in the usual binary ultrametric, but its measure under an independently biased sign law exhibits a sharp transition.

Precisely, let \(p\in(0,1)\), \(q=\max\{p,1-p\}\), and let \(\mu_p\) give independent sign coordinates probability \(p\) of \(+1\). Define the binary relative entropy
\[
D_2(r\Vert q)=r\log_2\frac rq+(1-r)\log_2\frac{1-r}{1-q},\qquad q\le r\le1,
\]
using the continuous endpoint interpretation. Define \(c_*(q)=1/(-\log_2q)\), and define \(R(c,q)\) as follows: \(R(c,q)=1\) when \(c\le c_*(q)\); when \(c>c_*(q)\), it is the unique \(r\in(q,1)\) satisfying \(D_2(r\Vert q)=1/c\). For \(\mu_p\)-almost every sign vector \(\xi\),
\[
\operatorname{dist}_{\ell_\infty}(T_c^{**}\xi,c_0)
=\limsup_{n\to\infty}\left|(T_c^{**}\xi)_n\right|
=2R(c,q)-1.
\]
Consequently the set \(E_c=\{\xi\in\{-1,1\}^{\mathbb N}:\|T_c^{**}\xi\|_\infty=1\}\) is comeager and of full Hausdorff dimension for every \(c\), yet
\[
\mu_p(E_c)=\begin{cases}1,&c\le c_*(q),\\0,&c>c_*(q).\end{cases}
\]
The complementary, nonnorming sign set is also topologically dense for every \(c\). In particular, a fixed norm-attaining second adjoint can have a comeager, full-dimensional set of norming extreme points that is null for a full-support Bernoulli product measure.

## Assumptions and scope

Work over real scalars. Index rows by \(n\ge1\). Let \(m_n=\max\{1,\lceil c\log_2(n+1)\rceil\}\) and partition \(\mathbb N\) into consecutive disjoint blocks \(I_n\) with \(|I_n|=m_n\). Put \(\lambda_n=n/(n+1)\), and define
\[
(T_cx)_n=\frac{\lambda_n}{m_n}\sum_{j\in I_n}x_j.
\]
Since the blocks escape to infinity, this formula maps \(c_0\) to \(c_0\). Its canonical second-adjoint action on \(\ell_\infty=c_0^{**}\) has exactly the same row-average formula. The sign cube is the set of extreme points of the real \(\ell_\infty\) unit ball and carries the product topology and the ultrametric \(d(\xi,\eta)=2^{-k}\), with \(k\) the first differing coordinate. No claim is made about complex sign cubes, arbitrary operators, correlated coordinate laws, or full classes of block lengths.

## Proof

**Norms and failure of earlier attainment.** Every row of \(T_c\) has positive coefficients summing to \(\lambda_n<1\), so \(\|T_c\|\le1\). Testing the indicator of the finite block \(I_n\) yields \(\|T_c\|\ge\lambda_n\); hence \(\|T_c\|=1\). For any \(x\in c_0\), its row averages tend to zero, so its image norm is a maximum of finitely many row values, each strictly below one when \(\|x\|_\infty\le1\). Thus \(T_c\) does not attain its norm. Its first adjoint sends \(y\in\ell_1\) to a disjoint-block vector of norm \(\sum_n\lambda_n|y_n|<\|y\|_1\) for every nonzero \(y\), so \(T_c^*\) does not attain either. Finally \(T_c^{**}\mathbf1=(\lambda_n)_n\), which has norm one.

**Binomial large-deviation envelope.** Fix a bias \(p\). On each block choose the majority-probability sign, occurring with probability \(q\); let \(K_n\sim\operatorname{Bin}(m_n,q)\) be its count. The random variables \(K_n\) are independent because the blocks are disjoint. The absolute output before the factor \(\lambda_n\) is \(|2K_n/m_n-1|\). For \(q<r<1\), the usual binomial exponential estimate and one term of the binomial sum give
\[
\Pr(K_n/m_n\ge r)=2^{-m_nD_2(r\Vert q)+O(\log m_n)},
\]
where the lower bound follows directly from the binomial coefficient bound \(\binom m{\lceil rm\rceil}\ge 2^{m h_2(\lceil rm\rceil/m)}/(m+1)\), and the upper bound follows from exponential Markov optimization. Here \(h_2\) is binary entropy. For every \(r\ge1/2\), the minority-tail probability \(\Pr(K_n/m_n\le1-r)\) does not exceed \(\Pr(K_n/m_n\ge r)\), by reflecting \(k\) to \(m_n-k\) in the binomial mass function, since \(q\ge1/2\). Therefore the same exponential rate governs \(\Pr(|2K_n/m_n-1|\ge2r-1)\).

Because \(m_n=c\log_2(n+1)+O(1)\), these independent events have summable probabilities when \(cD_2(r\Vert q)>1\), and divergent probabilities when \(cD_2(r\Vert q)<1\). In the second case the elementary single-binomial-term bound gives a lower bound of order \((\log n)^{-1}n^{-cD_2(r\Vert q)}\), which is enough for divergence. Both Borel–Cantelli lemmas, followed by taking rational thresholds approaching the unique entropy boundary, yield
\[
\limsup_n|2K_n/m_n-1|=2R(c,q)-1
\]
almost surely. At the endpoint \(R=1\), the same conclusion follows by approaching one from below; alternatively, all-majority blocks occur infinitely often because \(\sum_n q^{m_n}=\infty\) whenever \(c(-\log_2q)\le1\). Since \(\lambda_n\to1\), multiplication by \(\lambda_n\) does not change the limsup. Finally \(\operatorname{dist}_{\ell_\infty}(z,c_0)=\limsup_n|z_n|\), proving the asserted quotient norm formula.

**Exact attainment transition.** If \(R=1\), the tail norm already equals one and \(\|T_c^{**}\xi\|=1\) almost surely. If \(R<1\), choose a strict bound \(\rho<1\) on all sufficiently late output coordinates, and note that the finitely many initial output coordinates are each bounded by their corresponding \(\lambda_n<1\). Hence the entire output norm is strictly below one almost surely. This proves the measure-zero/measure-one transition, including equality at the critical parameter.

**Category and dimension.** For \(k\ge2\), the set of sign vectors having an output coordinate of modulus greater than \(1-1/k\) is open and dense in the sign cube: after any prescribed finite coordinates, choose an entirely uniform, sufficiently late block, with \(\lambda_n>1-1/k\). Their countable intersection is exactly \(E_c\), a dense \(G_\delta\). Its complement is dense as well: after any finite prefix, fill subsequent blocks with as nearly equal numbers of the two signs as possible, making their averages tend to zero; all finitely many prefix rows have coefficient sum less than one.

For dimension, fix the sparse block subsequence \(n_j=2^{j^2}\) and require every sign on \(I_{n_j}\) to be \(+1\). All such vectors lie in \(E_c\). Through coordinate \(N\), the number \(f(N)\) of forced signs is \(o(N)\), since the \(j\)-th forced block has length \(O(j^2)\) but begins beyond coordinate \(2^{j^2}\). Give every other coordinate an independent fair sign. A length-\(N\) cylinder then has measure \(2^{-(N-f(N))}\), which is at most \(2^{-sN}\) for large \(N\) and any fixed \(s<1\). The mass-distribution bound gives Hausdorff dimension at least \(s\), hence one; the entire sign cube has dimension one, giving equality.

## Verification

The accompanying standalone `CHECKER.py` executed successfully, reporting 2,370 finite diagnostics. These test exact rational binomial mass identities, reflection inequalities, and numeric inversion of the entropy boundary. The infinite-dimensional norm and almost-sure assertions are proved above and are **not** inferred from finite computation. A reader can reproduce the diagnostics with `python CHECKER.py` using the Python standard library.

For the unbiased law \(p=1/2\), the critical block scale is \(c_*=1\). For \(c>1\), the almost-sure quotient output norm is strictly between zero and one, given uniquely by \(1-h_2((1+\rho)/2)=1/c\); at \(c\le1\), the quotient norm equals one almost surely.

## Relationship to prior work

Dantas, Jung, and Martín (2026) prove that every operator on real \(c_0\) has a norm-attaining second adjoint, and their Section 3.1 constructs witnesses from weak-star-null coordinate rows. The present result **does not claim that existence theorem as new**. Instead it calculates the full relative-entropy phase diagram for the product-measure prevalence of norming *extreme points* of one explicitly constructed operator, alongside its category and dimension properties.

The probability component is an elementary special case in the spirit of the classical Erdős–Rényi logarithmic-window law and uses standard binomial large deviations and Borel–Cantelli. The cited dynamical-systems versions concern maxima of moving averages, not the simultaneous category, quotient-norm, and bidual-attainment classification for this fixed operator. Earlier work on residuality of norm-attaining **operators** considers a different ambient variable from the norming points of a single operator. No independent publication-priority certification is claimed.

## Limitations

This is a specific real block-averaging family; it neither characterizes norming points for every operator on \(c_0\) nor improves the universal existence theorem. The entropy formula uses independent identically biased signs, and the quotient norm is an almost-sure assertion rather than a pointwise formula for all signs. The probabilistic step relies on classical theorems; any earlier operator-theoretic reformulation of those theorems would narrow the originality claim. The full texts of some peripheral related studies have not been inspected, so independent priority review remains appropriate.

## References

1. S. Dantas, M. Jung, M. Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794v1 (first submitted 2026-09-01), https://arxiv.org/abs/2609.00794. Relevant material: Section 3.1, especially the disjoint-support argument and Theorem 3.3.
2. Y. Kifer, *Erdös–Rényi law of large numbers in the averaging setup*, arXiv:1608.01858 (2016), https://arxiv.org/abs/1608.01858. Related logarithmic-window large-deviation framework, not an operator-attainment statement.
3. M. Jung, M. Martín, A. Rueda Zoca, *Residuality in the set of norm attaining operators between Banach spaces*, J. Funct. Anal. 284 (2023), 109746; arXiv:2203.04023, https://arxiv.org/abs/2203.04023. The ambient variable there is an operator, not a norming sign vector.
