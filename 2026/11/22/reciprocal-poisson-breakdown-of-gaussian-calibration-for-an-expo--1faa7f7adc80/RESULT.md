# Reciprocal-Poisson breakdown of Gaussian calibration for an exponential-weight Stein–Chen ratio

## Finding

Consider the published ratio-form Stein–Chen goodness-of-fit statistic with the weight function \(f_n(x)=u_n^x\):
\[
T_n=\frac{\overline{X u_n^X}}{\bar X\,\overline{u_n^{X+1}}}
=\frac{\sum_{i=1}^n X_{n,i}u_n^{X_{n,i}-1}}{\bar X_n\sum_{i=1}^n u_n^{X_{n,i}}}.
\]
In the rare-zero high-intensity regime specified below, \(T_n\) has a reciprocal-Poisson limit, including a positive atom at infinity. This invalidates fixed-parameter Gaussian calibration in a quantitatively sharp example, even under the exact Poisson null.

Specifically, if \(K\sim\operatorname{Poisson}(\lambda)\), then \(T_n\) converges weakly on the compactified half-line \([0,\infty]\) to
\[
W_\lambda=\begin{cases}\lambda/K,&K\ge1,\\+\infty,&K=0.\end{cases}
\]
Moreover, writing \(K_n=\sum_{i=1}^n\mathbf1_{\{X_{n,i}=0\}}\), we have \(K_n\Rightarrow K\), and, conditionally on \(K_n=0\),
\[\mu_nu_n T_n\xrightarrow{\Pr}1.\]

The fixed-parameter second-order delta-method Gaussian center and variance of this same ratio are exactly
\[
m_n=1+\frac{(1-u_n)e^{\mu_n(1-u_n)^2}}{n},\qquad
v_n=\frac{\bigl((1-u_n)^2+\mu_n^{-1}\bigr)e^{\mu_n(1-u_n)^2}-\mu_n^{-1}}{n}.
\]
Along the stated triangular array, \(m_n\to1+1/\lambda\) and \(v_n\to1/\lambda\). The same limits hold when the Gaussian-calibration formulas use \(\bar X_n\) in place of \(\mu_n\).

For the concrete choice \(\mu_n=\log n\), \(u_n=(\log n)^{-3}\) and \(n\ge3\), the nominal two-sided 5% Gaussian rejection rule \(\lvert T_n-m_n\rvert>z_{0.975}\sqrt{v_n}\) has **exact limiting null rejection probability**
\[
\boxed{e^{-1}+\Pr\{\operatorname{Poisson}(1)\ge25\}
=0.3678794411714423\ldots}. 
\]
In particular, the nominal 5% Gaussian approximation produces asymptotic null rejection near 36.79% in this triangular-array regime.

## Assumptions and scope

For each integer \(n\), let \(X_{n,1},\dots,X_{n,n}\) be independent Poisson counts with common mean \(\mu_n>0\), and let \(0<u_n<1\) be deterministic. Assume
\[
\mu_n\to\infty,\qquad n e^{-\mu_n}\to\lambda\in(0,\infty),\qquad \mu_nu_n\to0.
\]
These conditions entail \(\mu_n=\log n-\log\lambda+o(1)\), \(\mu_n/n\to0\), and \(u_n\to0\). Define \(T_n\) as displayed whenever \(\bar X_n>0\), assigning \(T_n=0\) on the otherwise undefined event \(\bar X_n=0\); the latter event has probability \(e^{-n\mu_n}\to0\). All convergence statements are under this null triangular array. Weak convergence at infinity uses the one-point compactification \([0,\infty]\) (equivalently, continuous mapping through \(t\mapsto t/(1+t)\)). The Gaussian calculation describes the **published fixed-parameter delta-method approximation evaluated at triangular-array parameters**, not the actual finite-sample moments of the statistic.

## Proof

**Step 1: the two low-count frequencies.** Write \(N_{j,n}=\sum_i\mathbf1_{\{X_{n,i}=j\}}\). Since \(K_n=N_{0,n}\sim\operatorname{Bin}(n,e^{-\mu_n})\), its law converges to \(\operatorname{Poisson}(\lambda)\). Also
\[
\mathbb E N_{1,n}=n\mu_ne^{-\mu_n},\qquad
\operatorname{Var}(N_{1,n})\le n\mu_ne^{-\mu_n};
\]
therefore \(N_{1,n}/\mu_n\to\lambda\) in probability. Finally, \(\mathbb E\bar X_n=\mu_n\) and \(\operatorname{Var}(\bar X_n)=\mu_n/n\to0\), whence \(\bar X_n-\mu_n\to0\) in probability and \(\bar X_n/\mu_n\to1\).

**Step 2: suppress higher counts, with separate numerator and denominator scales.** Define
\[
A_n=\sum_iX_{n,i}u_n^{X_{n,i}-1}=N_{1,n}+R_n,\quad
B_n=\sum_i u_n^{X_{n,i}}=K_n+u_nN_{1,n}+S_n,
\]
where \(R_n,S_n\ge0\) collect the terms with counts at least two. The Poisson probability-generating function yields the exact identities
\[
\mathbb ER_n=n\mu_ne^{-\mu_n}(e^{\mu_nu_n}-1),\quad
\mathbb ES_n=ne^{-\mu_n}(e^{\mu_nu_n}-1-\mu_nu_n).
\]
Consequently, Markov's inequality and \(\mu_nu_n\to0\) give \(R_n/\mu_n\to0\) and \(S_n/(\mu_nu_n)\to0\) in probability. In particular, \(A_n/\mu_n\to\lambda\), while \((B_n-K_n)/(\mu_nu_n)\to\lambda\). As \(\mu_nu_n\to0\), \(B_n-K_n\to0\) in probability.

**Step 3: the finite reciprocal atoms.** The joint convergence
\[
(K_n,A_n/\mu_n,B_n-K_n,\bar X_n/\mu_n)\ \Rightarrow\ (K,\lambda,0,1)
\]
and the discreteness of \(K_n\) imply that whenever \(K_n\ge1\), the ratio \(A_n/(\bar X_nB_n)\) approaches \(\lambda/K_n\) in probability on every fixed integer stratum. As the family \((K_n)\) is tight, this identifies the limiting masses at every finite positive reciprocal atom. On \(K_n=0\), the sharper denominator expansion from Step 2 gives
\[
\mu_nu_nT_n
=\frac{\mu_n}{\bar X_n}\,
\frac{A_n/\mu_n}{B_n/(\mu_nu_n)}\xrightarrow{\Pr}1
\]
conditionally on \(K_n=0\): unconditional probability bounds remain valid after conditioning because \(\Pr(K_n=0)\to e^{-\lambda}>0\). Thus \(T_n\to+\infty\) conditionally on \(K_n=0\). Together with \(K_n\Rightarrow K\), this proves the asserted compactified weak limit and its mass at infinity. More generally, for every fixed positive integer \(k\), \(T_n\to\lambda/k\) conditionally on \(K_n=k\).

**Step 4: actual fixed-parameter Gaussian center and variance formulas.** For a single \(\operatorname{Poisson}(\mu)\) count with fixed \(u\in(0,1)\), put \(G=e^{\mu(u-1)}\). The population means of \((X,Xu^X,u^{X+1})\) are \((\mu,\mu uG,uG)\). Applying the ordinary second-order delta method to \(h(x,a,b)=a/(xb)\) gives a mean correction coefficient
\[
b_{\mu,u}=(1-u)e^{\mu(1-u)^2}
\]
and a first-order variance coefficient
\[
\sigma^2_{\mu,u}=
\left((1-u)^2+\frac1\mu\right)e^{\mu(1-u)^2}-\frac1\mu.
\]
For independent verification, the influence function at the Poisson population is
\[
\psi_{\mu,u}(x)=\frac{x u^{x-1}-\mu u^x}{\mu G}-\frac{x-\mu}{\mu},
\]
whose expectation is zero and variance equals \(\sigma^2_{\mu,u}\). The bias coefficient is \(\tfrac12\operatorname{tr}(H_h\operatorname{Cov}(X,Xu^X,u^{X+1}))\); its simplification gives \(b_{\mu,u}\). These are expansions at **fixed** \(\mu,u\); this proof does not invoke a triangular-array central limit theorem. From \(\mu_n(1-u_n)^2=\mu_n+o(1)\) and \(e^{\mu_n}/n\to1/\lambda\), direct substitution yields \(m_n\to1+1/\lambda\), \(v_n\to1/\lambda\). Moreover \(\bar X_n-\mu_n\to0\) and \(u_n\to0\) imply \(e^{\bar X_n(1-u_n)^2}/n\to1/\lambda\) in probability, proving the plug-in statement.

**Step 5: exact limiting 5% size.** Take \(\lambda=1\), \(\mu_n=\log n\), \(u_n=\mu_n^{-3}\), and \(z=z_{0.975}=1.9599639845\ldots\). The normal acceptance interval converges to \([2-z,2+z]\). Its lower boundary obeys
\[
\frac1{25}<2-z<\frac1{24},
\]
and its upper boundary exceeds one. The limit \(W_1\) has atoms only at \(1/k\), \(k\ge1\), and infinity, none on these boundaries. Accordingly, the limiting rejection event is exactly \(\{K=0\}\cup\{K\ge25\}\), giving the displayed Poisson probability. This follows from weak convergence at the continuity boundaries and does not use finite-sample simulations.

## Verification

The standalone script `verify.py` uses only Python's standard library and can be executed with `python3 verify.py`. It reconstructs the original ratio from sample sums using exact rational arithmetic; independently computes the Poisson covariance matrix, the second-order delta-method bias and first-order variance, and the Poisson influence variance; checks probability-generating-function remainder identities; and determines the exact integer rejection set from the Gaussian threshold. It is a finite numerical and symbolic consistency check, **not** a replacement for Steps 1–5's limiting arguments.

## Relationship to prior work

Aleksandrov, Weiß and Jentsch introduced the ratio statistic \(\widehat T_2\), fixed-parameter Gaussian null approximation and bias correction, and noted possible division-by-zero issues. Weiß, Puig and Aleksandrov explicitly studied the family \(f(x)=u^x\), provided an alternative-independent delta-method derivation, and remarked that boundary weights can be degenerate. Both analyses work with fixed count distributions and fixed weight parameters, rather than \(\mu_n\to\infty\), \(u_n\to0\), and \(ne^{-\mu_n}\to\lambda\). The result here identifies a specific **non-Gaussian critical law with an atom at infinity** and an explicit null-size failure of the otherwise meaningful Gaussian calibration. The general Poisson approximation of a rare binomial count is classical; the additional content is the exact identification of the *published ratio statistic* and its *calibration* in this coupled regime. It does not claim priority for Poisson approximation or for the generic fact that a ratio becomes unstable near a rare denominator.

## Limitations

The theorem covers independent Poisson rows, deterministic weights satisfying the stated joint limits, and an asymptotically defined Gaussian rule. It does not say that the authors recommended a sequence with \(u_n\to0\) and \(\mu_n\to\infty\), or that their fixed-parameter asymptotics are false. The example is an intentionally stress-tested, high-intensity/boundary-weight regime; its practical frequency is not assessed. The statistic's undefined all-zero sample event is assigned a value only to make it a random variable, and its probability vanishes. No actual finite-sample rejection rate or universally valid replacement critical value is asserted. The 36.79% limit is specific to the displayed weight/mean sequence and a two-sided 5% Gaussian rule, although the reciprocal-Poisson limit holds throughout the broader assumptions. General earlier rare-ratio limit theorems may contain adaptable ingredients; no claim of independent validation or exhaustive historical priority is made.

## References

1. B. Aleksandrov, C. H. Weiß, and C. Jentsch, *Goodness-of-fit tests for Poisson count time series based on the Stein–Chen identity*, Statistica Neerlandica 76 (2022), 35–64; publicly available 27 June 2021. https://doi.org/10.1111/stan.12252 (especially Sections 3–4 and Theorem 1).
2. C. H. Weiß, P. Puig, and B. Aleksandrov, *Optimal Stein-type goodness-of-fit tests for count data*, Biometrical Journal 65 (2023); first online 27 September 2022. https://doi.org/10.1002/bimj.202200073 (especially Sections 2–3, Section 5, and Appendix A.3).
