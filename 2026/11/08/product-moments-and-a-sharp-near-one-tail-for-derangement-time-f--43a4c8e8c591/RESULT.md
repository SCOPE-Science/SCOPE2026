# Product moments and a sharp near-one tail for derangement-time fractions in Ewens growth

## Finding

Fix an Ewens Chinese restaurant process with parameter \(\theta>0\). For an integer \(k\geq1\), let \(C_i(m)\) be its number of cycles of size \(i\) after \(m\) customers, and define the chronological no-small-cycle fraction
\[
A_{n,k}=\frac1n\sum_{m=1}^{n}\mathbf1\{C_1(m)=\cdots=C_k(m)=0\}.
\]
Define
\[
H_k=\sum_{i=1}^k\frac1i,\quad
\phi_k(r)=\sum_{\ell=1}^k(-1)^{\ell+1}\binom{k}{\ell}\frac{1-r^\ell}{\ell},\quad
q_j(\theta,k)=j\int_0^1r^{j-1}e^{-\theta\phi_k(r)}\,dr.
\]
Then \(A_{n,k}\Rightarrow L_{\theta,k}\) for a random variable in \([0,1]\), uniquely characterized by the **product moment law**
\[
\boxed{\mathbb E L_{\theta,k}^{s}=e^{-\theta H_k}\prod_{j=1}^{s-1}q_j(\theta,k)\qquad(s=1,2,\ldots).}
\]
The empty product is one. The following strictly positive, finite constant exists, where \(\gamma\) is Euler's constant:
\[
C_{\theta,k}=e^{-\theta(H_k+\gamma)}\prod_{j=1}^{\infty}\bigl(q_j(\theta,k)e^{\theta/j}\bigr)\in(0,\infty).
\]
The resulting **sharp upper-endpoint law** is
\[
\boxed{\Pr\{L_{\theta,k}>1-\varepsilon\}\sim
\frac{C_{\theta,k}}{\Gamma(1+\theta)}\varepsilon^\theta
\quad(\varepsilon\downarrow0).}
\]
Thus the upper-tail exponent is \(\theta\) for every fixed cutoff \(k\); the multiplicative constant depends on the cutoff. For derangements (\(k=1\)),
\[
\mathbb E L_{\theta,1}=e^{-\theta},\qquad
\operatorname{Var}(L_{\theta,1})=e^{-2\theta}\left(\frac{e^\theta-1}{\theta}-1\right)>0.
\]
In particular, at \(\theta=1\) the limiting variance is \(e^{-2}(e-2)\).

## Assumptions and scope

The seating rule is: at size \(m\), the next customer creates a new singleton with probability \(\theta/(\theta+m)\), or joins an existing cycle of size \(i\) with aggregate probability \(iC_i(m)/(\theta+m)\), increasing that cycle's size by one. Every \(\theta>0\), finite integer cutoff \(k\geq1\), and every positive integer moment order \(s\) are covered. The limit \(n\to\infty\) precedes the endpoint limit \(\varepsilon\downarrow0\). No assertion concerns an almost-sure chronological-average limit or an exact finite-size tail.

## Proof

**1. Logarithmic-time limit.** The established finite-vector functional limit for Ewens cycle counts (Gnedin--Stark, Theorem 6; see also Galganov--Ilienko, Section 4.2) gives, on every compact subinterval \([\delta,1]\) of \((0,1]\), convergence of \((C_i(\lfloor nt\rfloor))_{1\leq i\leq k}\) to the stationary tandem infinite-server queue observed at logarithmic time \(\log t\). The limiting queue has Poisson arrivals at rate \(\theta\), with independent sequential stage durations of exponential rates \(1,2,\ldots,k\). Let \(Y_{\theta,k}(u)\) be the total number of customers in the first \(k\) stages at time \(u\), in the stationary bi-infinite version. Since the stationary process has locally finitely many jumps, its zero-set indicator is Riemann integrable on compact intervals; thus the continuous mapping theorem and the bound on the missing interval, at most \(\delta\), yield
\[
A_{n,k}\Rightarrow L_{\theta,k}:=\int_0^1\mathbf1\{Y_{\theta,k}(\log t)=0\}\,dt.
\]
The convergence mechanism itself is from the cited functional limits; the explicit moment and endpoint laws below are the claims derived here.

**2. One-customer service and multitime void formula.** The total time \(S_k\) a customer remains in stages \(1,\ldots,k\) is the sum of independent exponential variables with rates \(1,2,\ldots,k\). By the Rényi exponential-order-statistics representation, \(S_k\) has the same law as the maximum of \(k\) independent mean-one exponentials. Consequently,
\[
\Pr(S_k>v)=1-(1-e^{-v})^k,\qquad
\mathbb E S_k=H_k,\qquad
\int_0^d\Pr(S_k>v)\,dv=\phi_k(e^{-d}).
\]
The stationary system is a Poisson process of arrival times, each marked with an independent service duration. For ordered observation times \(u_1<\cdots<u_s\), all queues are empty at those times precisely when no marked interval covers any observation time. The intensity of the union of the forbidden arrival-and-service sets is
\[
\theta H_k+\theta\sum_{i=2}^s\int_0^{u_i-u_{i-1}}\Pr(S_k>v)\,dv.
\]
To see this, start with the forbidden intervals for \(u_1\), of intensity \(\theta\mathbb ES_k\); the *additional* forbidden intervals when adding \(u_i\) are exactly those arriving after \(u_{i-1}\) and surviving to \(u_i\). Indeed, any arrival before \(u_{i-1}\) that survives until \(u_i\) necessarily covers \(u_{i-1}\), which was already excluded. Independent thinning of the marked Poisson process therefore gives
\[
\Pr\{Y(u_1)=\cdots=Y(u_s)=0\}
=e^{-\theta H_k}\prod_{i=2}^se^{-\theta\phi_k(e^{-(u_i-u_{i-1})})}.
\]
All terms are finite because \(\mathbb ES_k=H_k\).

**3. Exact factorization of all moments.** By Fubini and ordering \(s\) independent integration coordinates,
\[
\mathbb EL_{\theta,k}^s=s!e^{-\theta H_k}
\int_{0<t_1<\cdots<t_s<1}
\prod_{i=2}^s e^{-\theta\phi_k(t_{i-1}/t_i)}\,dt_1\cdots dt_s.
\]
Set \(r_j=t_j/t_{j+1}\) for \(j=1,\ldots,s-1\) and \(u=t_s\). The Jacobian is
\[
dt_1\cdots dt_s=u^{s-1}\prod_{j=1}^{s-1}r_j^{j-1}\,du\,dr_1\cdots dr_{s-1}.
\]
Since \(\int_0^1u^{s-1}du=1/s\) and \(s!/s=(s-1)!=\prod_{j=1}^{s-1}j\), the multidimensional integral separates into the asserted \(q_j\) product. Compact support in \([0,1]\) makes these moments determine the distribution uniquely (Hausdorff moment determinacy).

**4. Positivity, product convergence and endpoint exponent.** The polynomial \(\phi_k\) satisfies
\[
\phi_k(1)=0,\qquad \phi_k'(r)=-\frac{1-(1-r)^k}{r},\qquad \phi_k'(1)=-1.
\]
The value at \(r=0\) is understood by polynomial continuation. Thus \(\phi_k(r)=(1-r)+O_k((1-r)^2)\) as \(r\uparrow1\). If \(B_j\) has density \(jr^{j-1}\) on \([0,1]\), then \(q_j=\mathbb E e^{-\theta\phi_k(B_j)}\). The beta moments \(\mathbb E(1-B_j)=1/(j+1)\) and \(\mathbb E(1-B_j)^2=2/((j+1)(j+2))\) imply
\[
q_j=1-\frac\theta j+O_{\theta,k}(j^{-2}),\qquad
\log q_j+\frac\theta j=O_{\theta,k}(j^{-2}).
\]
Every \(q_j\) is positive, so the infinite product defining \(C_{\theta,k}\) converges to a finite positive number. Using \(H_{s-1}=\log s+\gamma+o(1)\),
\[
\mathbb E L_{\theta,k}^{s}
=e^{-\theta H_k-\theta H_{s-1}}
\prod_{j=1}^{s-1}(q_je^{\theta/j})
\sim C_{\theta,k}s^{-\theta}.
\]
This moment asymptotic extends from integer to arbitrary real \(s\to\infty\) by monotonicity between consecutive integer powers. With \(W=-\log L_{\theta,k}\in[0,\infty]\), and the convention \(e^{-s\infty}=0\), it says \(\mathbb E e^{-sW}\sim C_{\theta,k}s^{-\theta}\). The Laplace--Stieltjes Tauberian theorem at the origin (for a nonnegative measure, \(\theta>0\)) yields
\[
\Pr(W\leq x)\sim\frac{C_{\theta,k}}{\Gamma(1+\theta)}x^\theta\quad(x\downarrow0).
\]
Replacing \(x\) by \(-\log(1-\varepsilon)\sim\varepsilon\), with continuity bracketing to handle a strict inequality, proves the endpoint formula.

**5. Derangement variance.** For \(k=1\), \(\phi_1(r)=1-r\) and \(q_1=(1-e^{-\theta})/\theta\). The first two moment formulas immediately give the stated variance. The factor \((e^\theta-1)/\theta-1\) is strictly positive for every \(\theta>0\).

## Verification

The standalone \(check.py\) uses exact-rational finite CRP recurrences, symbolic polynomial identities, and numerical quadrature to check independent instances of the moment product. Running \(python check.py\) gives 101 successful assertions, including the limiting derangement variance \(0.09720887469821693\ldots\). Finite tests do not prove the infinite law: the proof relies on the explicitly cited functional limit, the marked-Poisson void computation, moment factorization, and the Tauberian implication.

## Relationship to prior work

Gnedin and Stark establish the Ewens CRP transition law, the absence of an almost-sure discrete chronological time-average, a stationary queue representation, and a logarithmic-time functional limit; in particular, their discussion leaves a nonvanishing variance calculation to readers. The paper does not provide the product law for all moments of the chronological zero-small-cycle fraction or its sharp near-one tail. Galganov and Ilienko prove a stronger small-block point-process limit and describe count processes, providing a second foundation for the limiting process; their described results are not the explicit moment product or endpoint asymptotic. The contribution here is the explicit distributional fingerprint and the universal endpoint exponent, **not** the stationary queue construction or functional convergence per se. The product and tail formulas are consequences of additional void-event integration and Tauberian analysis beyond the cited functional limits.

## Limitations

The result applies to the classical Ewens CRP, fixed finite cutoff \(k\), and fixed \(\theta>0\); no joint growing-cutoff limit or optimal finite-size convergence rate is established. The endpoint law is for the *limiting random fraction*, not a uniform-in-\(n\) estimate. Because the dynamic functional limit is known, independent historical-priority review should specifically check whether the integrated void-product and sharp endpoint law have been derived elsewhere in queueing or random-partition literature.

## References

1. A. Gnedin and D. Stark, *Random Permutations and Queues*, arXiv:2209.12781v1, first public 2022-09-26; Sections 3, 5, 8, and Theorem 6 in Section 10. https://arxiv.org/abs/2209.12781
2. P. Galganov and A. Ilienko, *Scaling limit for small blocks in the Chinese restaurant process*, arXiv:2502.05578v1, first public 2025-02-08; Sections 2 and 4, especially Section 4.2. https://arxiv.org/abs/2502.05578
3. P. H. da Silva, A. Jamshidpey, and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1, 2020; static derangement context distinct from chronological occupation laws. https://arxiv.org/abs/2006.04840
4. Karamata's Laplace--Stieltjes Tauberian theorem for regularly varying measures; used in its standard nonnegative-measure form.
