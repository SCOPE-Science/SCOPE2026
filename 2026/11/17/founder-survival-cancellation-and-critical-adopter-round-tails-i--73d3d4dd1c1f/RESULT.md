# Founder-survival cancellation and critical adopter-round tails in two-stage contagion

## Finding

A newly introduced round-based two-stage adoption model admits an exact and unusually simple single-founder stochastic invasion probability, even though the number of within-round contacts and the survival of their initiator are correlated. The same model has a sharp, round-length-dependent critical adopter-round tail.

Fix \(\rho>0\), \(\nu>0\), \(\tau>0\), \(p\in(0,1]\), and a fixed integer \(r\ge1\). Define
\[
\lambda=1+\nu,\qquad f_\nu(\tau)=\frac{1-e^{-\nu\tau}}{\nu\tau},\qquad c=p\rho f_\nu(\tau),\qquad\kappa=1-e^{-\lambda\tau},\qquad\mathcal R=\frac c\lambda.
\]

For the stochastic population model defined below, let \(A_j^{(N)}\) be the adopter count in round \(j\) starting from exactly \(r\) adopters and \(N-r\) naive individuals. For any integer \(K>r\), take the probability of reaching \(K\) adopters at least once before extinction. The iterated large-population, large-threshold law is
\[
\boxed{\lim_{K\to\infty}\lim_{N\to\infty}\Pr\bigl(\sup_{j\ge0}A_j^{(N)}\ge K\bigr)=1-\min\{1,\mathcal R^{-1}\}^{r}.}
\]
The order of limits is part of the theorem. In particular, for one founder the probability is \(\max\{0,1-1/\mathcal R\}\). This law depends on the round length through \(\mathcal R\), but has no additional round-length correction after \(\mathcal R\) is fixed.

At \(\mathcal R=1\), for one initial founder let \(S\) denote the total number of adopter-round individuals in the limiting branching process, including a continuing adopter as an individual in each new round. Then
\[
\boxed{\Pr(S=n)\sim\frac{n^{-3/2}}{2\sqrt{\pi\kappa}},\qquad \Pr(S\ge n)\sim\frac{n^{-1/2}}{\sqrt{\pi\kappa}}}\qquad(n\to\infty).
\]
Thus the extinction probability depends only on \(\mathcal R\), whereas critical occupation tails retain the survival-per-round parameter \(\kappa\). For \(\mathcal R<1\), the limiting branching process has expected total adopter-round count \(r/[\kappa(1-\mathcal R)]\).

## Assumptions and scope

Use the finite-population synchronous Markov chain of Muñoz, Nuño and Meacci, Section 4.2 and Supplement S2 of arXiv:2611.08353v2. Its population classes are naive \(S_0\), primed \(S_1\), adopter \(A\), and recovered \(R\), with total \(N\). The dimensionless cessation rate is one; turnover rate is \(\nu\), contact rate per adopter is \(\rho\), and a naive contact adopts directly with probability \(p\). During each round an adopter contributes an independent active time \(T=\min(E,\tau)\) with \(E\sim\operatorname{Exp}(1+\nu)\), surviving as an adopter into the next round exactly if \(E\ge\tau\). All newly adopted individuals act only in the next round.

Conditional on the active times, set \(\Theta=\sum T_i\), \(\Lambda=\rho\Theta/N\) and \(m=\nu\tau\). Under the source's constant-within-round integrated-exposure closure, a naive individual converts directly to adopter with probability
\[
 p\,\frac{\Lambda}{\Lambda+m}\bigl(1-e^{-(\Lambda+m)}\bigr).
\]
Naive individuals may instead be primed; primed adopters and turnover are updated by the source's competing risks. Initially \(A=r\), \(S_0=N-r\), \(S_1=R=0\); all rates are held fixed as \(N\to\infty\). In the limit, \(\operatorname{Poisson}(cT)\) means a Poisson variable conditional on \(T\), not an independent mixed-Poisson variable separated from the parent's survival event.

## Proof

**1. One-step and finite-horizon limit.** For a fixed number \(a\) of adopters and fixed active-time sum \(\Theta\), Taylor expansion at \(\Lambda=0\) gives
\[
 \frac{\Lambda}{\Lambda+m}\bigl(1-e^{-(\Lambda+m)}\bigr)=f_\nu(\tau)\Lambda+O(\Lambda^2).
\]
At a fixed round horizon, the number of individuals in non-naive compartments is tight (each new non-naive transition occurs with total conditional expectation bounded by a constant times the current adopter count, and existing non-naive individuals cannot proliferate except through these transitions). Induction on the finite horizon makes \(\Theta=O_{\Pr}(1)\) and \(S_0/N\to1\). The direct-adoption binomial law therefore converges conditionally on the active times to \(\operatorname{Poisson}(c\Theta)\), while adoptions from the finite primed population vanish in probability. Splitting this Poisson sum among the \(a\) adopters yields independent conditional counts \(\operatorname{Poisson}(cT_i)\). Parent survival remains exactly \(\mathbf1_{\{E_i\ge\tau\}}\). By the exponential memoryless property, a continuing adopter's new-round clock has a fresh exponential law. The resulting limit for all fixed round horizons is an ordinary one-type Galton–Watson chain starting from \(r\) individuals, with independent copies of
\[
 Z=\mathbf1_{\{E\ge\tau\}}+P,\qquad P\mid E\sim\operatorname{Poisson}(c\min(E,\tau)),\qquad E\sim\operatorname{Exp}(\lambda).
\]

**2. Exact generating function.** Integrating over \(E<\tau\) and the atom \(E\ge\tau\) gives, for \(0\le s\le1\),
\[
 G(s)=\mathbb E[s^Z]=\int_0^\tau\lambda e^{-\lambda t}e^{-c(1-s)t}\,dt+s e^{-\lambda\tau}e^{-c(1-s)\tau}
 =\frac{\lambda[1-e^{-[\lambda+c(1-s)]\tau}]}{\lambda+c(1-s)}+s e^{-[\lambda+c(1-s)]\tau}.
\]
With \(\mathbb ET=\kappa/\lambda\), its mean is
\[
 G'(1)=e^{-\lambda\tau}+c\frac\kappa\lambda=1+\kappa(\mathcal R-1).
\]
If \(c>\lambda\), direct substitution of \(s=\lambda/c\) makes the denominator \(c\) and gives \(G(\lambda/c)=\lambda/c\): the two exponential terms cancel exactly. Because \(\Pr(Z=0)>0\) and \(\Pr(Z\ge2)>0\), \(G\) is strictly convex on \([0,1]\); a supercritical generating function has exactly one fixed point strictly below one, namely \(q=\lambda/c\). When \(c\le\lambda\), the finite nondegenerate Galton–Watson law becomes extinct almost surely, hence \(q=1\).

**3. Passage from bounded to unbounded invasion.** Fix \(K>r\), and stop the finite-population chain when \(A=0\) or \(A\ge K\). For \(N\) sufficiently large, from every intermediate state \(1\le A<K\), independently of the sizes of the other compartments, a lower bound on the next-round probability of \(A=0\) is
\[
 \delta_K=\kappa^{K-1}e^{-2\rho K\tau}>0.
\]
Indeed all existing adopters can undergo their terminating event, while conditional on their times each of the at most \(N\) remaining individuals has probability at most \(\rho K\tau/N\) of becoming an adopter. Hence the stopping time has a geometric tail uniform in large \(N\). Finite-horizon convergence, then this uniform tail, yields
\[
 \lim_{N\to\infty}\Pr(\sup_j A_j^{(N)}\ge K)=\Pr(\sup_j Z_j^{(r)}\ge K),
\]
where the right process is Galton–Watson and \(Z_0^{(r)}=r\). A nondegenerate supercritical Galton–Watson process grows unboundedly on nonextinction, while an extinct process has a finite maximum; in the critical/subcritical case extinction is certain. Letting \(K\to\infty\) proves the claimed \(1-q^r\) law. This does not assert indefinite survival for finite \(N\), for which the source proves almost-sure extinction.

**4. Critical occupation tail.** At \(c=\lambda\), the offspring factorial second moment is
\[
 G''(1)=c^2\mathbb E[T^2]+2c\tau e^{-\lambda\tau},\qquad
 \mathbb E[T^2]=\frac{2}{\lambda^2}\bigl[1-e^{-\lambda\tau}(1+\lambda\tau)\bigr],
\]
so \(G''(1)=2\kappa\). Since \(G'(1)=1\), the offspring variance is exactly \(2\kappa\), not merely asymptotic to it. The offspring distribution has exponential moments and positive probabilities at zero and one, so it has lattice span one. For one founder, the classical cyclic-shift identity (Dwass's formula) gives
\[
 \Pr(S=n)=\frac1n\Pr\left(\sum_{j=1}^n Z_j=n-1\right),
\]
with independent copies \(Z_j\). The aperiodic lattice local central limit theorem yields \(\Pr(\sum_{j=1}^n Z_j=n-1)\sim(4\pi\kappa n)^{-1/2}\). Division by \(n\) and summation of the regularly varying probabilities prove both coefficients. For \(\mathcal R<1\), geometric summation of the generation means gives \(\mathbb ES=r/[1-G'(1)]\).

## Verification

Run `python3 verify.py` using only the Python standard library. It compares the closed-form offspring generating function with an independent quadrature representation, its derivative with the predicted mean, the supercritical fixed-point substitution, and the critical factorial moment. It also numerically compares exact single-founder finite-population one-round generating functions at increasing \(N\) with the claimed branching limit. This is finite numerical corroboration, not proof of the infinite-horizon statements.

## Relationship to prior work

Muñoz, Nuño and Meacci explicitly define the stochastic finite-population four-compartment chain and derive the deterministic invasion threshold \(\mathcal R\) from its large-population map. Their pre-November-8 version reports large-initial-population stochastic simulations and almost-sure finite-population extinction, but no one-founder limiting establishment law or critical adopter-round tail. The exact threshold itself, the use of Galton–Watson extinction fixed points, cyclic-progeny identities, and local central limit methods are not new. The contribution here is the explicit correlated survival-and-contact offspring law for that model, its cancellation to an exact founder probability, the coupling of finite-population first-passage events to that law, and the \(\kappa\)-dependent occupation-tail coefficient. The general branching approximation literature and age-dependent extinction theory provide relevant broader methods.

## Limitations

The invasion result is a two-stage limit, first \(N\to\infty\) at fixed \(K\), then \(K\to\infty\); it is not an assertion of macroscopic outbreak probability or nonextinction at any fixed population size. The critical total-progeny law concerns adopter-round individuals of the limiting branching genealogy and is not a finite-population total outbreak-size law. The formula uses the source's uniform-within-round exposure closure, fixed rates, and a bounded founder count. It does not treat a simultaneous \(N,K\) limit, a growing initial seed, the source's alternative exact within-round hazard profile, or eventual persistence at a deterministic chaotic attractor. Broader historical priority, especially relative to age-dependent branching-process literature whose complete text was not accessible, remains for independent evaluation.

## References

1. F. J. Muñoz, J. C. Nuño, L. Meacci, *From elementary processes to chaos: a discrete-time two-stage contagion model and its continuous limit*, arXiv:2611.08353v2 (7 Nov 2026), especially Section 4.2, Proposition 4 and Appendix S2. First public v1: 5 Nov 2026. https://arxiv.org/html/2611.08353v2
2. F. Ball and P. Donnelly, *Strong approximations for epidemic models*, Stochastic Processes and their Applications **55** (1995), 1–21. https://doi.org/10.1016/0304-4149(94)00034-Q
3. L. A. Goodman, *The probabilities of extinction for birth-and-death processes that are age-dependent or phase-dependent*, Biometrika **54** (1967), 579–596. https://doi.org/10.1093/biomet/54.3-4.579
4. M. Dwass, *The total progeny in a branching process and a related random walk*, Journal of Applied Probability **6** (1969), 682–686. https://doi.org/10.2307/3212112
