# Finite spikes decouple fixed-point counts from the Luce permuton

## Finding

Let \(m\geq1\) be fixed and let \(a_1,\ldots,a_m>0\). For each integer \(n>m\), take a Luce (Plackett--Luce) random permutation \(\sigma_n\) of the labels \(1,\ldots,n\): the ranking is produced by successive sampling without replacement with probabilities proportional to positive item weights. Give label \(i\le m\) weight \(na_i\) and every label \(i>m\) weight \(1\). Write \(\sigma_n(i)\) for the rank of label \(i\), and \(F_n=\#\{i:\sigma_n(i)=i\}\) for its fixed-point count.

Let \(U_1,\ldots,U_m\) be independent exponential variables of rates \(a_1,\ldots,a_m\), and let \(N(t)\), \(t\geq0\), be an independent unit-rate Poisson process. Define

\[
R_i=1+\#\{j\le m:j\ne i,\ U_j<U_i\}+N(U_i),\qquad
H_m=\sum_{i=1}^m\mathbf 1\{R_i=i\}.
\]

Then the empirical permuton of \(\sigma_n\) converges in probability to Lebesgue measure on \([0,1]^2\), while

\[
\boxed{F_n\ \Longrightarrow\ Z+H_m},
\]

where \(Z\) has the \(\operatorname{Poisson}(1)\) law and is independent of \(H_m\). Thus the fixed-point law is not Poisson even though the limiting permuton has the constant density \(1\). Its limiting mean is \(1+\mathbb EH_m>1\), not the integral \(1\) of that density along the diagonal.

The finite correction has an exact computable polynomial probability-generating function. For \(S\subseteq\{1,\ldots,m\}\), put \(A_S=\sum_{i\in S}a_i\), define \(P_{m+1,S}(z)=1\), and for \(r=m,m-1,\ldots,1\) recursively set

\[
P_{r,S}(z)=\frac{P_{r+1,S}(z)+\sum_{i\in S}a_i z^{\mathbf1\{i=r\}}P_{r+1,S\setminus\{i\}}(z)}{1+A_S}.
\]

Then \(\mathbb E z^{H_m}=P_{1,\{1,\ldots,m\}}(z)\). In particular, for \(m=1\) and \(a_1=a>0\),

\[
F_n\Longrightarrow Z+B_a,\qquad B_a\sim\operatorname{Bernoulli}\left(\frac{a}{1+a}\right),\qquad Z\perp B_a.
\]

For \(m=2\) and \(a_1=a_2=1\), the correction has generating polynomial \((10+5z+3z^2)/18\).

There is also a sharp scale classification for one exceptional label: if label \(1\) has arbitrary positive weight \(w_n\), all other weights equal \(1\), and \(w_n/n\to a\in[0,\infty]\), then \(F_n\Longrightarrow Z+B_a\), independently summed, with Bernoulli success parameter \(a/(1+a)\) at finite \(a\) (interpreted as \(0\) at \(a=0\) and \(1\) at \(a=\infty\)). Its permuton remains uniform in every case.

## Assumptions and scope

The number \(m\) of exceptional labels is fixed as \(n\to\infty\). Their labels are exactly the initial \(m\) integers; their rates \(a_i\) are fixed and strictly positive. The ordinary labels \(m+1,\ldots,n\) have exchangeable weight \(1\). The one-exception corollary permits any positive sequence \(w_n\) with a limit of \(w_n/n\) in the extended interval \([0,\infty]\). The ranking maps each label to its draw position; fixed points are the same under inversion of a permutation, so this convention is immaterial for the count. Ties of exponential clocks have probability zero.

## Proof

**1. Exponential-race coupling.** The Luce ranking is the increasing order of independent exponential clocks whose rates equal the item weights. For the exceptional labels set \(U_i=nE_i\), where \(E_i\) has rate \(na_i\); hence each \(U_i\) has rate \(a_i\) for every \(n\). For ordinary labels, the rescaled clocks \(nE_j\) form a binomial point process of \(n-m\) points with interval intensities converging to Lebesgue measure. On each bounded interval this point process converges to a unit-rate Poisson process, independently of \((U_i)\). Because the \(U_i\)'s are almost surely distinct and avoid Poisson points, the ranks of the exceptional labels jointly converge to \((R_i)_{1\leq i\leq m}\). Therefore the number \(H_n=\sum_{i\le m}\mathbf1\{\sigma_n(i)=i\}\) converges in distribution to \(H_m\).

**2. Uniform conditional law of ordinary labels.** Conditional on the entire vector of exceptional ranks (and their relative order), exchangeability of the ordinary exponential clocks makes their labels uniformly distributed over the remaining \(M=n-m\) rank positions. Write \(O_n=F_n-H_n\). Let \(h\) count positions that are both available to ordinary labels and belong to \(\{m+1,\ldots,n\}\). Since only \(m\) positions are excluded, \(M-m\leq h\leq M\) for every exceptional-rank configuration. For each fixed integer \(k\ge0\), the exact conditional falling-factorial moment is

\[
\mathbb E\big[(O_n)_k\mid\text{exceptional ranks}\big]
=\frac{(h)_k}{(M)_k},
\]

with the usual zero interpretation for \(k>h\). Here \((x)_k=x(x-1)\cdots(x-k+1)\). Equivalently, its conditional generating function is

\[
\mathbb E[z^{O_n}\mid\text{exceptional ranks}]
=\sum_{k=0}^{h}\frac{(h)_k}{(M)_k}\frac{(z-1)^k}{k!}.
\]

For each fixed \(k\), the coefficient ratio tends uniformly to \(1\), and every ratio lies in \([0,1]\). The series is dominated by \(\sum_k|z-1|^k/k!\). Thus for each fixed complex \(z\), the conditional generating function converges uniformly over all exceptional-rank configurations to \(\exp(z-1)\). In particular \(O_n\Longrightarrow Z\sim\operatorname{Poisson}(1)\), jointly and asymptotically independently of all exceptional-rank observables. Combining with Step 1 gives \(F_n\Longrightarrow Z+H_m\). This calculation also gives uniform integrability of every fixed falling-factorial moment, hence convergence of the mean.

**3. Finite-state law of the exceptional correction.** In the limiting merged time line, the ordinary arrivals form a Poisson process of instantaneous rate \(1\), while the as-yet-unseen exceptional labels have independent exponential arrival rates \(a_i\). At draw position \(r\), conditional on the remaining exceptional-label set \(S\), the next arrival is ordinary with probability \(1/(1+A_S)\) or is exceptional label \(i\in S\) with probability \(a_i/(1+A_S)\). An exceptional arrival contributes one fixed point precisely when \(i=r\). Positions beyond \(m\) cannot be fixed by exceptional labels, which proves the displayed backward recurrence and its terminal value. For \(m=1\), the probability that the exceptional label is first is \(a/(1+a)\). For two unit-rate exceptional labels, evaluating two recursion steps gives \((10+5z+3z^2)/18\).

**4. Uniform permuton.** Conditional on the exceptional ranks, all other labels form a uniform matching of \(M=n-m\) labels with \(M\) positions. For any fixed rectangular region \([0,x]\times[0,y]\), the count of matched ordinary labels in its rescaled rectangle is hypergeometric: its conditional mean is \(nxy+O(m+1)\) and its conditional variance is \(O(n)\), uniformly over exceptional ranks. Exceptional labels contribute at most \(m\) points. Division by \(n\), followed by a finite-grid approximation, proves weak convergence in probability of the empirical permuton to the uniform permuton.

**5. One-spike scale boundary.** For arbitrary positive \(w_n\), the exceptional label is first with exact probability \(p_n=w_n/(w_n+n-1)\). Independently of the value of \(w_n\), Step 2 with \(m=1\) gives a conditional \(\operatorname{Poisson}(1)\) limit uniformly in the exceptional rank. Thus the Bernoulli correction has success probability converging to \(a/(1+a)\), including its endpoints. Step 4 applies unchanged. For finite positive \(a\), the law has generating function \(\exp(z-1)(1+a z)/(1+a)\), not the generating function of a Poisson random variable.

## Verification

The standalone file `verify.py` uses only the Python standard library. It exactly enumerates Luce permutation probabilities for small \(n\), compares the resulting heavy-label generating polynomials to the finite-sampling recursion, checks conditional ordinary-label factorial moments for every exceptional-rank state, and checks convergence of the exact finite recurrence to its limiting version. It also verifies the explicit two-spike polynomial. Execute `python verify.py` next to this file. The finite checks are not substituted for the infinite arguments in the proof.

## Relationship to prior work

Borga, Chatterjee, and Diaconis (2025), Section 5.2, explicitly ask for the fixed-point distribution of Luce permutations and discuss a Poisson heuristic derived from the diagonal of a limiting permuton density. The present finite-spike construction has the uniform permuton but a non-Poisson fixed-point limit, so the permuton density alone is not sufficient for that heuristic without additional uniformity assumptions. Their paper proves permuton, local-pattern, and inversion results, not this finite-spike fixed-point law.

Chatterjee, Diaconis, and Kim (2023) establish the exponential representation and finite top- and bottom-rank results of the Luce/Tsetlin model; these underlie the coupling but do not determine the limiting full fixed-point count here. Clay (2026), Section 8, separately highlights the Luce fixed-point problem. The classical Poisson limit for fixed points of a uniform permutation supplies the baseline, not the non-Poisson finite-spike correction. A distinct homogeneous finite-block Luce result with positive block proportions and fixed rates gives a Poisson limit; its assumptions exclude vanishing-proportion blocks with weights of order \(n\).

## Limitations

The general theorem treats a fixed number of exceptional labels placed at the beginning and a homogeneous background. It does not characterize arbitrary weight arrays, arbitrary moving locations of exceptional labels, a growing number of exceptions, or full cycle counts. The result is an internally checked mathematical argument rather than an independent mathematical audit, and historical-priority assessment may be incomplete. In particular, an inaccessible later revision of the most relevant source and broadly formulated rare-event approximation results remain comparison risks. The finite verifier alone does not establish the asymptotic result.

## References

1. J. Borga, S. Chatterjee, and P. Diaconis, *Permuton and local limits for the Luce model*, arXiv:2509.07729, first posted 2025-09-09. https://arxiv.org/abs/2509.07729
2. S. Chatterjee, P. Diaconis, and G. B. Kim, *Enumerative Theory for the Tsetlin Library*, arXiv:2306.16521, first posted 2023-06-28. https://arxiv.org/html/2306.16521v1
3. A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008, first posted 2026-03-09, Section 8. https://arxiv.org/html/2603.09008
4. P. Diaconis, J. Fulman, and R. Guralnick, *On fixed points of permutations*, J. Algebraic Combin. 28 (2008), 189--218, for the classical uniform-permutation context. https://arxiv.org/abs/0708.2643
