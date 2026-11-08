# Tagged-block size and partition diversity have an exact negative covariance across the two-parameter sampling family

## Finding
For every integer \(n\ge2\), parameters \(0\le\alpha<1\) and \(\theta> -\alpha\) (requiring \(\theta>0\) when \(\alpha=0\)), let \(S_n\) be the number of customers seated at the first table and \(K_n\) be the number of occupied tables in the two-parameter Chinese restaurant process. Equivalently \(S_n\) is the size of the block containing label 1 in its exchangeable partition. Define the ordinary rising factorial by \((x)_0=1\) and \((x)_r=\prod_{j=0}^{r-1}(x+j)\) for \(r\ge1\). Then
\[
\boxed{\operatorname{Cov}(S_n,K_n)=-\frac{(1-\alpha)(\theta+\alpha)(n-1)}{\theta+1}\,\frac{(\theta+2+\alpha)_{n-2}}{(\theta+1)_{n-1}}<0.}
\]
In particular, at zero discount this reduces to \(\operatorname{Cov}(S_n,K_n)=-\theta(n-1)/(\theta+1)^2\).

For fixed \(0<\alpha<1\), put
\[
 v_S=\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)^2(\theta+2)},\quad
 A_1=\frac{\Gamma(\theta+1)}{\Gamma(\theta+\alpha)},\quad
 A_2=\frac{(\theta+\alpha)\Gamma(\theta+1)}{\Gamma(\theta+2\alpha)},
\]
\[
 v_K=\frac{A_2-A_1^2}{\alpha^2},\quad
 c=\frac{(1-\alpha)(\theta+\alpha)\Gamma(\theta+1)}{(\theta+1)\Gamma(\theta+2+\alpha)}.
\]
Both variances are strictly positive and
\[
 \operatorname{Corr}(S_n,K_n)\longrightarrow-\frac{c}{\sqrt{v_Sv_K}}<0.
\]
At \(\alpha=0\) and \(\theta>0\), the limiting correlation is instead zero, with the precise decay law
\[
 \sqrt{\log n}\,\operatorname{Corr}(S_n,K_n)\longrightarrow-\frac{\sqrt{\theta+2}}{\theta+1}.
\]

## Assumptions and scope
The first customer sits alone. Conditional on \(j\ge1\) customers, \(K_j=k\), and current table sizes \(s_1,\ldots,s_k\), customer \(j+1\) joins table \(i\) with probability \((s_i-\alpha)/(j+\theta)\), or opens a new table with probability \((\theta+\alpha k)/(j+\theta)\). The claim is about this exchangeable random partition for every admissible real parameter pair, not a deterministic conditioned block count, a Dirichlet-process mixture with overlapping atoms, nor a ranked frequency statistic. No limit assertion is made with parameters changing with sample size.

## Proof
Let \(X_j=S_j-\alpha\), \(Y_j=\theta+\alpha K_j\), and \(t_j=\theta+j>0\). Define the mutually exclusive indicator variables \(I_j\) for joining table 1 and \(J_j\) for opening a new table. Their conditional means are \(X_j/t_j\) and \(Y_j/t_j\), respectively, and \(I_jJ_j=0\). We have \(S_{j+1}=S_j+I_j\), \(K_{j+1}=K_j+J_j\), hence
\[
 u_{j+1}:=\mathbb E X_{j+1}=u_j(1+1/t_j),\qquad
 v_{j+1}:=\mathbb E Y_{j+1}=v_j(1+\alpha/t_j).
\]
The initial values \(u_1=1-\alpha\), \(v_1=\theta+\alpha\) give
\[
 u_j=\frac{(1-\alpha)(\theta+j)}{\theta+1},\qquad
 v_j=\frac{(\theta+\alpha)(\theta+1+\alpha)_{j-1}}{(\theta+1)_{j-1}}.
\]
Writing \(C_j=\operatorname{Cov}(S_j,K_j)\), bilinearity and the disjoint events imply
\[
 \operatorname{Cov}(I_j,J_j)=-\frac{u_jv_j}{t_j^2},\quad
 \operatorname{Cov}(S_j,J_j)=\frac{\alpha}{t_j}C_j,\quad
 \operatorname{Cov}(I_j,K_j)=\frac1{t_j}C_j.
\]
Consequently
\[
 C_{j+1}=\left(1+\frac{1+\alpha}{\theta+j}\right)C_j-\frac{u_jv_j}{(\theta+j)^2},\qquad C_1=0.
\]
Substituting the displayed expressions for \(u_j,v_j\) into this first-order recurrence and inducting on \(j\) yields the boxed identity. Its denominator and all rising factorial factors are positive in the stated domain; so is \((1-\alpha)(\theta+\alpha)(n-1)\), proving strict negativity.

For completeness, the table-1 size is beta-binomial: conditional on \(P\sim\operatorname{Beta}(1-\alpha,\theta+\alpha)\), the remaining \(n-1\) customers independently join its block with probability \(P\). Thus
\[
 \operatorname{Var}(S_n)=\frac{(n-1)(1-\alpha)(\theta+\alpha)(n+\theta)}{(\theta+1)^2(\theta+2)},\qquad \operatorname{Var}(S_n)/n^2\to v_S.
\]
For \(\alpha>0\), the conditional increment \(Y_{j+1}=Y_j+\alpha J_j\) gives the second factorial-moment recurrence
\[
 \mathbb E[Y_{j+1}(Y_{j+1}+\alpha)]=\left(1+\frac{2\alpha}{\theta+j}\right)\mathbb E[Y_j(Y_j+\alpha)].
\]
Therefore
\[
 \mathbb EY_n=\frac{(\theta+\alpha)(\theta+1+\alpha)_{n-1}}{(\theta+1)_{n-1}},\qquad
 \mathbb E[Y_n(Y_n+\alpha)]=\frac{(\theta+\alpha)(\theta+2\alpha)(\theta+1+2\alpha)_{n-1}}{(\theta+1)_{n-1}}.
\]
Since \(K_n=(Y_n-\theta)/\alpha\), Gamma-ratio asymptotics show \(\operatorname{Var}(K_n)/n^{2\alpha}\to v_K\). This limit is positive: the normalized process \(Y_j/v_j\) is a square-integrable martingale with nonzero conditional variance already on its first nontrivial increment, and its variance is nondecreasing to a finite limit (the displayed second moments bound it). The covariance formula likewise gives \(\operatorname{Cov}(S_n,K_n)/n^{1+\alpha}\to-c\). Dividing establishes the positive-discount correlation limit.

At \(\alpha=0\), new-table indicators are independent Bernoulli variables of probabilities \(\theta/(\theta+j)\), as their conditional probabilities do not depend on the current partition. Hence
\[
 \operatorname{Var}(K_n)=\sum_{j=1}^{n-1}\frac{\theta j}{(\theta+j)^2}\sim\theta\log n.
\]
Together with \(\operatorname{Var}(S_n)\sim\theta n^2/((\theta+1)^2(\theta+2))\) and the exact covariance above, this yields the zero-discount correlation asymptotic.

## Verification
The standalone standard-library file `verify.py` constructs the exact joint rational law of \((S_n,K_n)\) recursively, independently of the analytic recurrence, and compares its five moments (two means, two variances, covariance) and covariance signs against the closed formula. Running `python3 verify.py` passed 1392 exact comparisons for eight valid rational parameter choices and every \(2\le n\le30\). These checks cannot prove the all-integer result or continuum of parameters; the proof above does.

## Relationship to prior work
The two-parameter Chinese restaurant transition and its exchangeable partition probabilities are classical, represented by Pitman and Yor's technical report (1995), notably its Section 9.2, Proposition 49, and Pitman's 2002 lecture notes. Those works describe the partition law, size-biased frequencies, and species-diversity growth; the finite mixed tagged-block/diversity covariance and the contrasting limiting correlations are not explicitly stated in the inspected passages. The displayed identity requires evaluating a mixed statistic and a nontrivial cancellation of simultaneous seating events; it is not an assertion of novelty of the process, beta-binomial marginal, or block-count marginal.

## Limitations
The result concerns an existing family of exchangeable partitions and follows from classical transition rules. The existence of a broader earlier generating function or uninspected calculation explicitly implying the mixed identity remains a historical-priority risk. No independent audit has been performed. Numerical checks are finite only. The limiting correlation statement holds for fixed admissible parameters, not simultaneous approaches to \(\alpha=0\) as \(n\to\infty\).

## References
1. Pitman, J. and Yor, M. (1995), *The two-parameter Poisson–Dirichlet distribution derived from a stable subordinator*, Berkeley Technical Report 433, dated August 25, 1995; especially Section 9.2 and Proposition 49. https://statistics.berkeley.edu/sites/default/files/tech-reports/433.pdf
2. Pitman, J. (2002), *Combinatorial Stochastic Processes*, Berkeley Technical Report 621, dated August 2002; random partition and Chinese restaurant construction. https://statistics.berkeley.edu/sites/default/files/tech-reports/621.pdf
3. Teh, Y. W. (2005), *A hierarchical Bayesian language model based on Pitman–Yor processes*, transition description, Equation (2). https://homepages.inf.ed.ac.uk/sgwater/papers/nips05.pdf
