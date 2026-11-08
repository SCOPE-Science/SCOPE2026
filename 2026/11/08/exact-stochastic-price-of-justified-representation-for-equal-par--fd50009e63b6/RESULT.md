# Exact stochastic price of justified representation for equal party lists

## Finding

Fix integers \(q\ge2\) and \(k\ge1\). There are \(k\) equally large disjoint voter blocs, \(q\) distinct candidates per bloc, and a committee of size \(k\). Every voter approves precisely the \(q\) candidates of their own bloc. Candidate qualities \(X_{ij}\), for \(1\le i\le k\) and \(1\le j\le q\), are independent samples from the same nonnegative, continuous probability distribution \(F\) with finite first moment. Let \(C_k\) denote the maximum total quality of a committee satisfying justified representation (JR), and let \(U_k\) denote the unconstrained maximum total quality. Write \(D_k=U_k-C_k\). On these profiles the JR, PJR and EJR constraints are equivalent: each bloc must receive exactly one seat. Therefore, with \(M_i=\max_{1\le j\le q}X_{ij}\),

\[
C_k=\sum_{i=1}^k M_i,\qquad U_k=\text{sum of the largest }k\text{ of the }kq\text{ qualities}.
\]

The finite-sample expectations are exactly

\[
\mathbb E C_k=k\int_0^\infty(1-F(x)^q)\,dx,
\]

\[
\mathbb E U_k=\int_0^\infty\sum_{r=0}^{kq}\min(k,r)\binom{kq}{r}\bigl(1-F(x)\bigr)^r F(x)^{kq-r}\,dx.
\]

Suppose additionally that \(F\) has a finite second moment, and its density is continuous and strictly positive in a neighborhood of its \((1-1/q)\)-quantile \(t\). Put \(X_1,\ldots,X_q\) for one independent quality block and \(M=\max_jX_j\). Define

\[
u=t+q\,\mathbb E(X_1-t)_+,\quad f=\mathbb E M,\quad d=u-f,\quad
\sigma^2=\operatorname{Var}\!\left(\sum_{j=1}^q(X_j-t)_+-M\right).
\]

Then, as \(k\to\infty\) with \(q\) fixed, under a single infinite array coupling,

\[
\frac{U_k}{k}\to u,\qquad \frac{C_k}{k}\to f,\qquad \frac{D_k}{k}\to d>0
\quad\text{almost surely},
\]

and

\[
\boxed{\frac{D_k-kd}{\sqrt{k}}\ \xrightarrow{\ d\ }\ N(0,\sigma^2).}
\]

In particular, \(C_k/U_k\to f/u\) almost surely. A joint central limit theorem also gives

\[
\sqrt{k}\left(\frac{C_k}{U_k}-\frac fu\right)\xrightarrow{\ d\ }N(0,\tau^2),\qquad\tau^2=\operatorname{Var}\!\left(\frac{M}{u}-\frac f{u^2}\sum_{j=1}^q(X_j-t)_+\right).
\]

These explicit variances account for dependence between the globally selected top candidates and the within-bloc winners.

For independent uniform qualities on \([0,1]\), these formulas simplify to the exact finite-sample identity

\[
\boxed{\mathbb E D_k=\frac{k(k-1)(q-1)}{2(kq+1)(q+1)}}
\]

and the sharp limits

\[
\boxed{\frac{D_k}{k}\to\frac{q-1}{2q(q+1)},\qquad
\frac{C_k}{U_k}\to\frac{2q^2}{(q+1)(2q-1)}.}
\]

Writing \(a=1-1/q\), the centered deficit's explicit Gaussian variance is

\[
\boxed{\sigma_q^2=\frac1{3q^2}-\frac1{4q^3}
+\frac{q}{(q+1)^2(q+2)}+\frac1{q^2(q+1)}
-2\left(\frac{1-a^{q+2}}{q+2}-a\frac{1-a^{q+1}}{q+1}\right).}
\]

For two candidates per bloc, \(\mathbb ED_k=k(k-1)/(6(2k+1))\), \(C_k/U_k\to8/9\), and \((D_k-k/12)/\sqrt{k}\Rightarrow N(0,1/72)\). Moreover, \(\sqrt{k}(C_k/U_k-8/9)\Rightarrow N(0,52/2187)\). The asymptotic fair-to-optimal ratio is at least \(8/9\) for **every** integer \(q\ge2\), with equality precisely at \(q=2\).

## Assumptions and scope

All candidates have different identities even if two have equal qualities; continuity makes quality ties probability zero. Every bloc contains the same positive number of voters, so with \(n\) total voters each bloc has \(n/k\) voters and its representation quota is exactly one. Every ballot consists of that bloc's complete list of \(q\) candidates, with no approval across blocs. JR and EJR are their usual approval-voting axioms; quality is a separate additive objective and does not change voter approvals. The general distribution is supported on nonnegative qualities, is atomless, and has a finite first moment. The additional local regularity and second-moment assumptions are required for the limit theorem. No independence between the optimized and fair total qualities is assumed. The asymptotic regime holds \(q\) fixed while the number of equally sized blocs/committee seats \(k\) grows. The uniform finite-expectation formula holds for all \(k\ge1\) without any limiting argument.

## Proof

**Representation reduction.** Each bloc's voters form a size-\(n/k\) cohesive group, approving their common \(q\) candidates. JR requires at least one elected candidate in its bloc. Since there are \(k\) blocs and exactly \(k\) seats, the only JR-feasible seat vector is one seat per bloc. Conversely, such a committee satisfies JR. For EJR, a cohesive group of level \(\ell\ge2\) would have to contain at least \(\ell n/k\) voters who all approve at least \(\ell\) candidates. Any group with a nonempty common approval intersection is contained in one bloc, whose cardinality is only \(n/k\); hence no such group exists. For level one, EJR is exactly JR. PJR is sandwiched between JR and EJR, so the three properties coincide. Maximizing total quality within the forced seat vector selects the maximum candidate of each bloc. Without a representation constraint, the optimum selects the globally highest \(k\) qualities.

**Exact finite expectations.** For a nonnegative random variable \(Y\), \(\mathbb E Y=\int_0^\infty\Pr(Y>x)\,dx\). Since \(\Pr(M\le x)=F(x)^q\), applying this to every bloc gives the first formula. For any nonnegative realized qualities, the sum of the largest \(k\) equals \(\int_0^\infty \min(k,N_x)\,dx\), where \(N_x\) counts qualities exceeding \(x\). Here \(N_x\) has distribution \(\operatorname{Binomial}(kq,1-F(x))\). Tonelli's theorem gives the second exact formula.

**Quantile variational representation.** Put \(N=kq\) and \(L_k(s)=ks+\sum_{i=1}^k\sum_{j=1}^q(X_{ij}-s)_+\). Sorting the \(N\) observations proves the deterministic identity \(U_k=\min_{s\ge0}L_k(s)\). A minimizer \(\widehat t_k\) lies between the \((N-k)\)-th and \((N-k+1)\)-th ascending order statistics. As \(F(t)=1-1/q\), positivity and continuity of its density at \(t\), together with the empirical distribution's binomial concentration, imply \(\widehat t_k-t=O_p(k^{-1/2})\). In the same shrinking neighborhood, \(\sup_{s}|N_s-k|=O_p(\sqrt k)\), where \(N_s\) counts observations exceeding \(s\). This follows from monotonicity of \(N_s\), binomial fluctuations at the endpoints, and the local Lipschitz property of \(F\). Integrating the slope \(L_k'(s)=k-N_s\) between \(t\) and \(\widehat t_k\) yields

\[
0\le L_k(t)-U_k=O_p(1)=o_p(\sqrt{k}).
\]

The endpoint inclusion can be made rigorous by first restricting to \(\lvert\widehat t_k-t\rvert\le B/\sqrt{k}\), whose probability tends arbitrarily close to one as \(B\to\infty\), then applying the count bound on the fixed \(B/\sqrt{k}\) interval.

**Strong law and central limit theorem.** The strong law gives \(C_k/k\to f\), and also \(L_k(t)/k\to u\). To transfer the latter to \(U_k/k\) almost surely, note that \(L_k(s)/k\to s+q\mathbb E(X-s)_+\) simultaneously at all nonnegative rational \(s\), by the strong law; both the empirical and limiting functions are convex and locally Lipschitz. The limiting function has unique minimizer \(t\) because \(F\) is strictly increasing near \(t\); its value is \(u\). The minimizers stay in a bounded interval almost surely (the empirical \((1-1/q)\)-quantile converges to \(t\)). Uniform convergence on this interval transfers minima, proving \(U_k/k\to u\) almost surely.

Now subtract the bloc maxima:

\[
D_k=kt+\sum_{i=1}^k\left[\sum_{j=1}^q(X_{ij}-t)_+-M_i\right]+o_p(\sqrt k).
\]

The bracketed variables are independent across blocs, identically distributed, and have finite variance. Their mean equals \(d-t\), and their variance equals \(\sigma^2\). The ordinary iid central limit theorem and Slutsky's theorem prove the stated Gaussian limit. The exact value \(d\) is strictly positive for continuous nondegenerate \(F\): pointwise \(t+\sum_j(X_j-t)_+\ge M\), with strict inequality when all \(q\) qualities lie below \(t\), an event of positive probability. The ratio follows from the strong law and \(u>0\). Applying the multivariate central limit theorem to the paired bloc variables \((M_i,\sum_j(X_{ij}-t)_+)\) and then the delta method to the smooth quotient yields the displayed ratio fluctuation variance.

**Uniform specialization.** With \(F(x)=x\) for \(0\le x\le1\), the mean of the maximum of \(q\) samples is \(q/(q+1)\). The expected ascending order statistic of rank \(r\) among \(kq\) uniforms equals \(r/(kq+1)\). Thus

\[
\mathbb E U_k=\frac{k(2kq-k+1)}{2(kq+1)},\qquad
\mathbb E C_k=\frac{kq}{q+1},
\]

whose difference simplifies exactly to the claimed \(k(k-1)(q-1)/[2(kq+1)(q+1)]\). Also \(t=a=1-1/q\), \(u=1-1/(2q)\), and \(f=q/(q+1)\), giving the limiting deficit and ratio.

For the variance, set \(Y_j=(X_j-a)_+\). Independence gives

\[
\operatorname{Var}\left(\sum_jY_j\right)=\frac1{3q^2}-\frac1{4q^3},\qquad
\operatorname{Var}(M)=\frac{q}{(q+1)^2(q+2)}.
\]

Conditioning on \(X_1=x\) yields \(\mathbb E[M\mid X_1=x]=(q-1+x^q)/q\), whence

\[
\operatorname{Cov}\left(\sum_jY_j,M\right)
=\int_a^1(x-a)x^q\,dx-\frac{1}{2q^2(q+1)}.
\]

The integral is \((1-a^{q+2})/(q+2)-a(1-a^{q+1})/(q+1)\). The variance-of-difference identity now gives the displayed rational expression for \(\sigma_q^2\). At \(q=2\), exact arithmetic reduces it to \(1/72\). Using the same covariance in the ratio delta-method formula yields \(52/2187\). The ratio \(2q^2/[(q+1)(2q-1)]\) equals \(1-(q-1)/(2q^2+q-1)\); the latter subtracted term is strictly decreasing for real \(q>2\) (its derivative is \(2q(2-q)/(2q^2+q-1)^2\)), which establishes the sharp \(8/9\) bound over integer \(q\ge2\).

## Verification

Run `python3 verify_price.py` with Python 3. The standalone program checks the exact uniform expectation identities against an independent beta-integral sum, independently computes the covariance and variance in rational arithmetic, and performs fixed-seed finite simulations. A passed simulation only checks an implementation and is not used as a proof of the strong law, the Gaussian limit, or any novelty claim. The mathematical derivation above is standalone.

## Relationship to prior work

Boehmer, Dong, Kreisel and Utke (2026) introduce quality-aware multiwinner representation and study worst-case quality loss and reciprocal-quality axioms. The present result instead uses the classical, quality-independent JR/EJR axioms on equally sized disjoint party lists and characterizes the *stochastic*, quality-maximizing welfare loss under independently sampled quality scores. It adds an arbitrary-distribution limit and dependent-block Gaussian fluctuation formula, along with an exact uniform finite-sample expected deficit. The original paper's complete manuscript was not accessible in this review; its abstract and detailed publicly available section summaries were inspected, but the absence of an identical result cannot be certified from partial access. Aziz et al. introduced JR and EJR, and earlier group-fair top-\(k\) ranking literature studies different ranking and constrained-selection formulations. Neither those axioms alone nor a worst-case quality guarantee determines the exact stochastic loss law.

## Limitations

The committee model is deliberately restricted to equal-sized, disjoint approvals with one required seat per bloc, iid qualities, and additive total-quality welfare. It does not solve arbitrary-profile quality-aware proportionality, dependent candidate qualities, strategic reporting, or the effects of noise in the quality estimates. The normal approximation fixes \(q\) and increases \(k\); it does not assert a simultaneous growing-\(q\) limit. The original recent motivating manuscript was not completely accessible, and unindexed or unpublished equivalent statements remain a novelty risk. The result has received no independent scientific audit.

## References

1. N. Boehmer, C. Dong, L. Kreisel, M. Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830, first submitted 2026-09-08, https://arxiv.org/abs/2609.08830.
2. H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, T. Walsh, *Justified Representation in Approval-Based Committee Voting*, AAAI 2015, https://doi.org/10.1609/aaai.v29i1.9324.
3. M. Zehlike, F. Bonchi, C. Castillo, S. Hajian, M. Megahed, R. Baeza-Yates, *FA*IR: A Fair Top-k Ranking Algorithm*, arXiv:1706.06368, 2017, https://arxiv.org/abs/1706.06368.
4. T. Delemazure, T. Demeulemeester, M. Eberl, J. Israel, P. Lederer, *Strategyproofness and Proportionality in Party-Approval Multiwinner Elections*, AAAI 2023, https://doi.org/10.1609/aaai.v37i5.25694.
