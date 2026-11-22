# A complete three-cumulant feasibility region for Bernoulli–negative-binomial count laws

## Finding

Consider a count \(X=B+Y\), the convolution of a Bernoulli count and a negative-binomial count. For every \(0<p<1\), \(\nu>0\), and \(0<\theta<1\), let \(B\sim\operatorname{Bernoulli}(p)\) and \(Y\sim\operatorname{NB}(\nu,\theta)\) be independent, where
\[
\Pr(Y=k)=\frac{(\nu)_k}{k!}\theta^k(1-\theta)^\nu,\qquad k=0,1,\ldots .
\]
Define the factorial cumulants \(\kappa_{[j]}=(\mathrm d^j/\mathrm dz^j)\log\mathbb E(1+z)^X\vert_{z=0}\). Write \(m=\kappa_{[1]}\), \(v=\kappa_{[2]}\), and \(t=\kappa_{[3]}/2\).

**Theorem (complete attainable region and unique inversion).** For real numbers \((m,v,t)\), set \(b=\min\{1,m\}\). The triple occurs for exactly one interior parameter vector \((p,\nu,\theta)\) if and only if
\[
 m>0,\quad v>-b^2,\quad L(m,v)<t<U(m,v),
\]
where
\[
L(m,v)=\begin{cases}v^2/m,&v\ge0,\\(-v)^{3/2},&v<0,\end{cases}
\qquad
U(m,v)=\begin{cases}\infty,&0<m\le1,\\1+(v+1)^2/(m-1),&m>1.\end{cases}
\]
The parameter \(p\) is the unique root in \(\bigl(\max\{0,\sqrt{\max\{0,-v\}}\},b\bigr)\) of
\[
 t=p^3+\frac{(v+p^2)^2}{m-p}.
\]
Then the remaining parameters are reconstructed by
\[
a=\frac{\theta}{1-\theta}=\frac{v+p^2}{m-p},\quad
\nu=\frac{(m-p)^2}{v+p^2},\quad\theta=\frac{a}{1+a}.
\]
The map from interior parameters to \((m,v,t)\) is a smooth bijection onto the displayed open region, with smooth inverse.

**Consequence (sharp underdispersion obstruction).** If \(v<0\), then
\[
\kappa_{[3]}>2(-\kappa_{[2]})^{3/2}.
\]
The constant is sharp as an unattained boundary value when the mean and negative second factorial cumulant are fixed. No nondegenerate \(\operatorname{Bin}(N,q)\), for any integer \(N\ge2\) and \(0<q<1\), agrees with all three cumulants of any interior model in this family.

## Assumptions and scope

The statement covers all real negative-binomial shapes \(\nu>0\), all \(0<p,\theta<1\), independent components, and factorial cumulants of the **population** count law. It is a precise moment-feasibility and parameter-identifiability theorem, not a finite-sample estimation or hypothesis-test calibration guarantee. The endpoints \(p=0,1\), \(\theta=0\), and the Poisson limit of negative-binomial distributions are excluded. The first public source date for the model is 18 September 2023.

## Proof

Put \(a=\theta/(1-\theta)>0\). The probability-generating function, expanded about one, gives
\[
K(z):=\log\mathbb E(1+z)^X=\log(1+pz)-\nu\log(1-az).
\]
Direct differentiation yields
\[
\kappa_{[j]}=(j-1)!\bigl(\nu a^j+(-1)^{j-1}p^j\bigr),\quad j\ge1.
\]
In particular,
\[
 m=p+\nu a,\qquad v=-p^2+\nu a^2,\qquad t=p^3+\nu a^3.
\]
Hence \(A=m-p=\nu a>0\), \(B=v+p^2=\nu a^2>0\), and \(0<p<1\), exactly when
\[
\max\{0,\sqrt{\max\{0,-v\}}\}<p<\min\{1,m\}.
\]
Such a nonempty interval exists precisely when \(m>0\) and \(v>-\min\{1,m\}^2\). Given a feasible \(p\), solving \(A=\nu a\) and \(B=\nu a^2\) uniquely gives \(a=B/A\) and \(\nu=A^2/B\). Substituting into the third cumulant reduces the inverse problem to the scalar function
\[
F_{m,v}(p)=p^3+\frac{(v+p^2)^2}{m-p}.
\]
Throughout its nonempty domain,
\[
F'_{m,v}(p)=3p^2+\frac{(v+p^2)\bigl(v+p^2+4p(m-p)\bigr)}{(m-p)^2}>0,
\]
because \(p>0\), \(m-p>0\), and \(v+p^2>0\). Thus every attainable \(t\) has one and only one preimage. If \(v\ge0\), the lower endpoint \(p\downarrow0\) gives \(L=v^2/m\); if \(v<0\), the lower endpoint \(p\downarrow\sqrt{-v}\) gives \(L=(-v)^{3/2}\). If \(m\le1\), the upper endpoint \(p\uparrow m\) gives \(F\uparrow\infty\), since \(v+m^2>0\); if \(m>1\), the upper endpoint \(p\uparrow1\) gives \(U=1+(v+1)^2/(m-1)\). Strict endpoint exclusion and continuity prove the full open image region. The strict derivative and the inverse formulas prove the smooth-inverse assertion by the inverse-function theorem.

For \(v<0\), the identity \(v+p^2=\nu a^2>0\) implies \(p>\sqrt{-v}\); hence \(t=p^3+\nu a^3>(-v)^{3/2}\). To see sharpness, fix any \(m>0\), \(-\min\{1,m\}^2<v<0\), let \(p\downarrow\sqrt{-v}\) from the feasible interval, and reconstruct \(a,\nu\) as above. Then \(a\downarrow0\), \(\nu\to\infty\) with \(\nu a=m-p\), and \(t\downarrow(-v)^{3/2}\). The boundary is a Bernoulli-plus-Poisson weak limit, not an interior negative-binomial law.

For \(\operatorname{Bin}(N,q)\), the factorial cumulants are \(\kappa_{[j]}=(-1)^{j-1}(j-1)!Nq^j\). When \(N\ge2\), its \(v=-Nq^2<0\) and \(t=Nq^3\) obey
\[
 t=Nq^3<N^{3/2}q^3=(-v)^{3/2},
\]
contradicting the necessary strict bound. The obstruction can occur even when mean and variance agree: \(\operatorname{Bin}(2,1/4)\) has \((m,v,\kappa_{[3]})=(1/2,-1/8,1/16)\), whereas the mixture with \((p,\nu,\theta)=(2/5,2/7,7/27)\) has the same \((m,v)\) but \(\kappa_{[3]}=61/400\).

## Verification

The attached standalone Python/SymPy checker independently differentiates the generating function, checks the inverse and derivative identities symbolically, verifies the displayed binomial/mixture example using rational arithmetic, and reconstructs parameters on a finite grid. The checker reported 204 passed exact assertions. Its finite grid supports reproducibility but does not substitute for the quantified positivity and monotonicity proof above. Reproduce using `python3 moment_region_check.py` with SymPy installed.

## Relationship to prior work

Ong, Sim, Liu and Srivastava introduced the NB-shifted NB model, its Bernoulli-convolution generating function, its mean/variance, dispersion regimes, numerical fitting and log-concavity discussion. Their open full text does not formulate or solve the inverse map from the first three factorial cumulants, determine its complete feasible image, or identify the strict binomial moment obstruction. Earlier general factorial-cumulant work supplies the classical binomial and negative-binomial component identities, not the resulting three-parameter feasible region. Prior work on Poisson-binomial effective trial counts and zero-inflated negative-binomial infinite divisibility treats other count-law structures, without an implication that supplies this region.

## Limitations

The theorem does not claim that empirical factorial cumulants always lie in the open feasible region or that the corresponding method-of-moments estimator is well behaved near its boundaries. It does not address finite-sample testing error, maximum-likelihood algorithms, or the multi-Bernoulli and other mixture generalizations. The claimed originality is a literature-supported assessment rather than an independently certified priority result; general work on constrained moment maps may contain related principles.

## References

1. S. H. Ong, S. Z. Sim, S. Liu and H. M. Srivastava, “A Family of Finite Mixture Distributions for Modelling Dispersion in Count Data,” *Stats* **6** (2023), 942–955, DOI: 10.3390/stats6030059. https://www.mdpi.com/2571-905X/6/3/59
2. “Asymptotic Normality Through Factorial Cumulants and Partition Identities,” *Combinatorics, Probability and Computing* (author manuscript 2014), Section 5.1, https://pmc.ncbi.nlm.nih.gov/articles/PMC3938197/
3. “Cumulant effective-trial hierarchy for Poisson-binomial laws,” published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-poisson-binomial-cumulant-effective-trial-hierarchy--c64930932dda
4. “Sharp infinite divisibility threshold for zero-inflated negative-binomial laws of integer shape,” published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-infinite-divisibility-threshold-for-zero-inflated-negative--e4339a2d413f
