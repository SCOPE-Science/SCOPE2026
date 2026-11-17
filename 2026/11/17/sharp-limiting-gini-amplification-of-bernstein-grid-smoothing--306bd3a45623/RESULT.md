# Sharp limiting Gini amplification of Bernstein grid smoothing

## Finding
For each integer \(n\ge 1\), let \(B_n\) be the \((n+1)\)-site Bernstein collocation operator
\[
 (B_n f)_k=\sum_{j=0}^n\binom nj\left(\frac{k}{n}\right)^j\left(1-\frac{k}{n}\right)^{n-j}f_j,\qquad 0\le k\le n,
\]
with endpoint conventions given by the binomial distribution at parameters zero and one. Let
\[
 G_n(f)=\sum_{0\le i<j\le n}|f_i-f_j|,\qquad
 \Lambda_n=\sup_{G_n(f)>0}\frac{G_n(B_nf)}{G_n(f)}.
\]
Then \(\Lambda_1=\Lambda_2=1\), but \(\Lambda_n>1\) for **every** \(n\ge3\). For \(n\ge2\), put
\[
 u_{n,k}=\left(1-\frac{k}{n}\right)^n,\quad
 U_n=\sum_{k=0}^n u_{n,k},\quad
 R_n=\sum_{k=0}^n\left(1-\frac{2k}{n}\right)u_{n,k}.
\]
The exact, reproducible all-dimensional bounds are
\[
 R_n\le\Lambda_n\le U_n,\qquad
 0\le U_n-\Lambda_n\le \frac{2}{n}\sum_{k=0}^n k u_{n,k}
 \le\frac{2e^{-1}}{n(1-e^{-1})^2}.
\]
In particular, the **sharp asymptotic operator norm** is
\[
 \boxed{\lim_{n\to\infty}\Lambda_n=\frac{1}{1-e^{-1}}=\frac{e}{e-1}.}
\]
The endpoint impulse \(f=(1,0,\ldots,0)\) gives the exact ratio \(R_n\), and is asymptotically norming. For the first amplifying degree, \(\Lambda_3=88/81\), as confirmed by the exhaustive four-site cut computation in the proof.

## Assumptions and scope
All signals are real, with \(n+1\) equally weighted values at the nodes \(0,1/n,\ldots,1\). The matrix is row-stochastic but not, in general, column-stochastic. The unnormalized complete-pair Gini seminorm is translation-invariant; its kernel is exactly the constant vectors. All operator norms refer to the induced quotient norm, not to \(\ell^1\), ordinary adjacent total variation, or oscillation.

## Proof
**1. A weighted Gini comparison.** Let \(N\ge2\), and let \(q=(q_j)_{j=1}^N\) be any probability vector with \(q_*=\max_j q_j\). Then
\[
 N^2\sum_{i<j}q_iq_j|f_i-f_j|\le Nq_*\sum_{i<j}|f_i-f_j|.
\]
To prove this, decompose any real vector into a constant plus nonnegative multiples of superlevel-set indicators, and use the triangle inequality on both sides. For an indicator of a nonempty proper set \(S\) of size \(s\), its weighted pair-difference is \(q(S)(1-q(S))\), while its unweighted pair-difference is \(s(N-s)\). If \(q(S)\ge s/N\), then \(1-q(S)\le(N-s)/N\) and \(q(S)\le s q_*\). If \(q(S)<s/N\), exchange \(S\) with its complement. In either case \(N^2q(S)(1-q(S))\le Nq_*s(N-s)\). This proves the comparison for all real vectors.

**2. Stochastic averaging controlled by column sums.** Suppose \(P\) is a nonnegative row-stochastic \(N\)-by-\(N\) matrix. Define \(q_j=N^{-1}\sum_kP_{kj}\). For each ordered pair of output indices \(k,\ell\), draw **independent** inputs \(I\sim P_{k,\cdot}\) and \(J\sim P_{\ell,\cdot}\), using independent copies even when \(k=\ell\). Jensen's inequality for distinct output indices, followed by adding the nonnegative same-index terms, yields
\[
 \sum_{k<\ell}|(Pf)_k-(Pf)_\ell|
 \le\frac12\sum_{k,\ell}\mathbb E_{I\sim P_{k,\cdot},\,J\sim P_{\ell,\cdot}}|f_I-f_J|
 =N^2\sum_{i<j}q_iq_j|f_i-f_j|
 \le\left(\max_j\sum_kP_{kj}\right)G_n(f).
\]
The middle equality uses independent draws even for identical output row indices, and thus legitimately includes positive same-index contributions in the upper bound, though the original same-index output differences vanish.

**3. Exact maximal column mass of the Bernstein matrix.** Let \(b_j(t)=\binom njt^j(1-t)^{n-j}\), and \(s_j=\sum_{k=0}^n b_j(k/n)\). The two endpoint columns have the same mass, namely \(s_0=s_n=U_n\). For \(1\le j\le n-1\), the function \(b_j\) is nonnegative and unimodal, with integral \(\int_0^1b_j(t)\,dt=1/(n+1)\). For **any** nonnegative unimodal function \(b\), the set \(\{t:b(t)>h\}\) is an interval (possibly empty), containing at most \(n\) times its length plus one grid nodes. Integrating this count in \(h\) gives
\[
 \sum_{k=0}^n b(k/n)\le n\int_0^1 b(t)\,dt+\sup b.
\]
For the Bernstein basis, \(h_j=\sup b_j=b_j(j/n)\). The identity
\[
 \frac{h_{j+1}}{h_j}=\frac{(1+1/j)^j}{(1+1/(n-j-1))^{n-j-1}}
\]
shows that \(h_j\) decreases for \(1\le j\le\lfloor(n-1)/2\rfloor\), since \((1+1/r)^r\) is increasing in positive integers \(r\); symmetry supplies the other half. Consequently \(h_j\le h_1=(1-1/n)^{n-1}\). Hence every interior column obeys
\[
 s_j\le\frac{n}{n+1}+\left(1-\frac1n\right)^{n-1}
 <1+\left(1-\frac1n\right)^n\le U_n.
\]
For the strict inequality, subtract the two sides and use \((1-1/n)^{n-1}<n/(n+1)\). Thus \(\max_j s_j=U_n\), proving \(\Lambda_n\le U_n\).

**4. Endpoint lower bound and dimension threshold.** For \(f=e_0\), the output values are \(u_{n,k}\), decreasing in \(k\), while \(G_n(e_0)=n\). Therefore
\[
 \frac{G_n(B_ne_0)}{G_n(e_0)}
 =\frac1n\sum_{k=0}^n(n-2k)u_{n,k}=R_n
 =U_n-\frac2n\sum_{k=0}^n k u_{n,k}.
\]
For \(n\ge3\), pair the \(k\)-term and the \((n-k)\)-term of the weighted sum and isolate the \(k=0\) contribution. Then
\[
 R_n=1+\frac1n\sum_{1\le k<n/2}(n-2k)
 \left[\left(1-\frac{k}{n}\right)^n-\left(\frac{k}{n}\right)^n\right]>1.
\]
For \(n=1\), the collocation map is the identity. For \(n=2\), three-site complete-pair Gini variation is twice the oscillation, which a row-stochastic matrix cannot increase, and the preserved endpoint values provide equality. To check \(\Lambda_3\) exactly, the positive-matrix layer-cake argument reduces the maximum to nontrivial binary cuts. Up to complement and reflection, their ratios are \(88/81\), \(14/27\), \(47/54\), \(41/54\), and \(2/3\); therefore \(\Lambda_3=88/81\).

**5. Compatibility with classical adjacent variation.** Interpolate any sampled vector linearly between successive grid nodes to obtain a continuous function whose interval total variation is exactly \(\sum_{j=0}^{n-1}|f_{j+1}-f_j|\). Its Bernstein polynomial is the one used by \(B_n\). Classical Bernstein total-variation diminution, together with the fact that restricting a continuous function to a grid cannot increase its variation, gives \(\sum_{k=0}^{n-1}|(B_nf)_{k+1}-(B_nf)_k|\le\sum_{j=0}^{n-1}|f_{j+1}-f_j|\). This explains why the strict Gini amplification above is a genuinely different stability phenomenon.

**6. Sharp limit.** The elementary bound \(0\le u_{n,k}\le e^{-k}\), with \(u_{n,k}=0\) for \(k>n\), and pointwise convergence \(u_{n,k}\to e^{-k}\) give by dominated convergence
\[
 U_n\longrightarrow\sum_{k=0}^{\infty}e^{-k}=\frac{1}{1-e^{-1}}.
\]
Moreover \(0\le U_n-R_n=(2/n)\sum k u_{n,k}\le(2/n)\sum_{k\ge0}ke^{-k}\). The geometric-derivative sum equals \(e^{-1}/(1-e^{-1})^2\), yielding the stated \(O(n^{-1})\) sandwich and identical sharp limit for \(\Lambda_n\).

## Verification
The self-contained standard-library Python script `checker.py` constructs exact rational Bernstein matrices, exhausts every nontrivial binary cut in dimensions \(n+1=3,\ldots,9\), confirms explicit ratios and column bounds, and checks endpoint witnesses in a larger finite range. Its finite computations corroborate the identities; the proof above establishes the unrestricted statements. Invoke `python3 checker.py` from the extracted directory.

## Relationship to prior work
Heitzinger, Hössinger and Selberherr (available online January 18, 2004) give the classical Bernstein polynomial definition and discuss preservation of ordinary interval total variation in Theorem 2.7. That is adjacent-path variation rather than complete-pair Gini variation of the collocation matrix; its bound does not imply the present amplification or the sharp limiting coefficient. Kozyra and Rychlik (online April 11, 2016) use Bernstein basis polynomials for sharp Gini-scaled bounds on expectations of i.i.d. order-statistic combinations, not the deterministic grid-to-grid operator norm. Results on the same Bernstein collocation matrix's singular-value energy concern Hilbert-space spectral quantities and do not imply the complete-pair variation norm. The present limit relies on a distinct column-mass concentration bound and an asymptotically saturating endpoint impulse.

## Limitations
No exact formula for the finite-degree sharp coefficient \(\Lambda_n\) is asserted for all \(n\ge4\). Although finite computations indicate endpoint impulses are maximizers in tested dimensions, that stronger global assertion is **not proved**. The theorem applies only to the classical equispaced Bernstein collocation matrix on real samples, one application, and unweighted complete-pair Gini variation. Historical priority remains provisional; indexes and searches cannot establish uniqueness.

## References
1. C. Heitzinger, A. Hössinger, S. Selberherr, *An algorithm for smoothing three-dimensional Monte Carlo ion implantation simulation results*, Mathematics and Computers in Simulation 66 (2004), 219–230, available online January 18, 2004, DOI: 10.1016/j.matcom.2003.11.010. Relevant material: Definition 2.1 and Theorems 2.7–2.8. Author-hosted PDF: https://www.iue.tuwien.ac.at/pdf/ib_2004/JB2004_Heitzinger_3.pdf.
2. P. M. Kozyra, T. Rychlik, *Sharp bounds on the expectations of L-statistics expressed in the Gini mean difference units*, Communications in Statistics—Theory and Methods 46 (2017), 2921–2941; available online April 11, 2016, DOI: 10.1080/03610926.2015.1053937. Author-hosted PDF: https://www.math.us.edu.pl/pkozyra/papers/Sharp%20bounds%20on%20the%20expectations%20of%20L%20statistics.pdf.
3. Classical finite-dimensional Gini mean difference: \(\sum_{i<j}|f_i-f_j|\), the unweighted pairwise-difference dispersion functional.
