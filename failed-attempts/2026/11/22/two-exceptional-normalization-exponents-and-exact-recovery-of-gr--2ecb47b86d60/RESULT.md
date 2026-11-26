# Two exceptional normalization exponents and exact recovery of group-size laws in quadratic contagion

## Finding

Consider a population of size \(N\ge3\) with annealed, focal-update SIS or SIR transmission. A susceptible focal individual draws the number of partners \(T=n-1\in\{1,\ldots,N-1\}\) with known participant-view probability law \(Q\), samples \(T\) distinct partners uniformly without replacement, and becomes infected at rate \(\beta\ell^2/T^\eta\) when \(\ell\) sampled partners are infected. Recoveries have rate \(\mu I\), with known \(\beta,\mu>0\) and exponent \(\eta\ge0\). Generator identifiability means unique recovery of \(Q\) from all exact aggregate transition rates when its admissible finite support is known.

Let the admissible partner counts be any \(m\) distinct integers \(1\le t_1<\cdots<t_m\le N-1\), allowing zero probabilities. The linear map from the probabilities to normalization and the two observable factorial moments has rank
\[
\boxed{\operatorname{rank}A_\eta=\begin{cases}\min(m,2),&\eta\in\{1,2\},\\\min(m,3),&\eta\notin\{1,2\}.\end{cases}}
\]
Consequently, on an admissible support of exactly three sizes, a complete stochastic generator uniquely determines \(Q\) for every nonnegative \(\eta\) **except** \(\eta=1,2\); at either exceptional exponent the interior probability simplex contains a one-parameter family of indistinguishable laws. Every two-size law is identifiable for all \(\eta\ge0\), while four or more admissible sizes are nonidentifiable for every exponent. The ambiguity is genuine for strictly positive laws, not merely for measures with vanished weights.

At \(\eta=1\) the entire generator depends on the law only through the arithmetic mean \(\mathbb E_Q[T]\). At \(\eta=2\), the prevalence-squared kernel, it depends only through the inverse mean \(H=\mathbb E_Q[1/T]\). If exact generators under **both** these normalizations are observed, their joint information identifies any law on at most three known sizes, including precisely where either separate experiment is nonidentifying. Four distinct admissible sizes again permit nonidentifiability even with both experiments.

Sharp rational witnesses at \(N\ge4\) are: at \(\eta=2\), \(Q_A(T=2)=1\) and \(Q_B(T=1)=1/4\), \(Q_B(T=3)=3/4\), both with \(H=1/2\). At \(\eta=1\), \(Q_A(T=2)=1\) and \(Q_C(T=1)=Q_C(T=3)=1/2\), both with \(\mathbb E[T]=2\). Each pair has identical complete finite SIS and SIR generators despite different group-size distributions. These rational examples illustrate rank loss but the rank formula is universal in the finite domain specified above.

## Assumptions and scope

The exposure rate is focal and does not infect other group participants simultaneously; group memberships are independently resampled at each opportunity, and the participant-view law does not depend on disease state. Only the aggregate SIS or SIR continuous-time Markov generator is observed, and \(\beta,\mu,N,\eta\) and the admissible support are fixed and known. Identifiability is structural from ideal transition rates, not statistical consistency under partial noisy observations. The group-size normalization is exactly \(T^{-\eta}\), with strictly positive \(T\). The assertion concerns a quadratic kernel (not arbitrary higher-order kernels), with finite \(N\ge3\).

## Proof

**1. Generator-to-moment equivalence.** The hypergeometric factorial-moment identity gives
\[
\mathbb E[\ell^2\mid T,I]=\frac{TI}{N-1}+\frac{T(T-1)I(I-1)}{(N-1)(N-2)}.
\]
Writing \(M_1=\mathbb E_Q[T^{1-\eta}]\) and \(M_2=\mathbb E_Q[(T-1)T^{1-\eta}]\), the susceptible infection hazard is therefore
\[
\bar\lambda(I)=\beta\left(\frac{M_1I}{N-1}+\frac{M_2I(I-1)}{(N-1)(N-2)}\right).
\]
SIS has birth rate \((N-I)\bar\lambda(I)\) and death rate \(\mu I\); SIR has infection rate \(S\bar\lambda(I)\) and recovery rate \(\mu I\). The rates at \(I=1\) and \(I=2\), with at least one susceptible, determine \(M_1\) and then \(M_2\) separately, for \(N\ge3\). Conversely these two moments determine all rates. Hence, with known \(\beta\), exact generator equivalence is exactly equality of these two moments.

**2. Rank calculation.** For an admissible size \(t>0\), the column of the normalized moment map is
\[
\begin{pmatrix}1\\t^p\\(t-1)t^p\end{pmatrix},\qquad p=1-\eta.
\]
For \(p=0\), the second row is identical to the normalization row and the third is \(t-1\), strictly increasing; for \(p=-1\), the third row is one minus the second, which equals \(1/t\), strictly decreasing. Thus both exceptional ranks are \(\min(m,2)\).

For \(p\notin\{0,-1\}\), subtract the second row from the third to obtain the functions \(1,t^p,t^{p+1}\). The latter two functions form a strictly curved graph: setting \(x=t^p\), \(y=t^{p+1}\), differentiation yields
\[
\frac{d^2y}{dx^2}=\frac{p+1}{p^2}\,t^{1-p}\ne0\qquad (t>0).
\]
Since \(x=t^p\) is strictly monotone, any three distinct abscissae lie on a strictly convex or concave curve and their three columns are linearly independent. Two columns are always independent: their common first coordinate is one, and equality of both remaining coordinates would imply equality of \(t\), because their ratio is \(t-1\) and \(t^p>0\). Consequently the full rank is exactly \(\min(m,3)\) outside the exceptions. When \(m\) exceeds rank, a nonzero null vector has zero coordinate sum; perturb a strictly positive normalized law in both directions by a sufficiently small multiple of this vector to produce distinct valid laws with the identical generator.

**3. The arithmetic/harmonic collapse.** At \(\eta=1\), \(M_1=1\), \(M_2=\mathbb E[T]-1\). At \(\eta=2\), \(M_1=H=\mathbb E[1/T]\), \(M_2=1-H\). Each supplies only one nonconstant statistic beyond normalization. The displayed witnesses have exactly matching statistics by direct rational calculation. At \(\eta=2\), for instance, either law gives \(M_1=M_2=1/2\), so for \(N=4\) the hazard is exactly \(\beta I(I+1)/12\) for every \(I=0,1,2,3\).

**4. Combined-protocol recovery and sharpness.** Combining the two experiments gives the linear functions \(1,t,1/t\). For any three distinct positive \(t\), these are linearly independent: a nonzero relation \(a+bt+c/t=0\) at three such values would make the quadratic \(bt^2+at+c\) have three distinct zeros, impossible unless \(a=b=c=0\). Thus the joint map has rank \(\min(m,3)\), uniquely determining any law on at most three sizes. For four or more sizes, a nontrivial null vector exists and strict-positive perturbations again give indistinguishable pairs. This proves every sharp cutoff.

## Verification

Run `python check.py` from this package. The checker evaluates 2,501 exact-rational identities, including direct hypergeometric averaging versus the factorial-moment hazard for many finite populations, both rational ambiguity pairs, exact three-column rank determinants at integer normalizations, and nonzero three-size reconstruction determinants for the joint protocols. The analytic proof of strict curvature, not the finite computations, certifies all real exponents and arbitrary population sizes.

## Relationship to prior work

Muslim (2026) establishes the finite-population moment-sufficiency theorem, its general rank criterion on prescribed supports, and examples of moment-matched distributions. Those foundational results are **not** claimed here as new. The present claim computes the rank completely over the continuum of normalization exponents in the quadratic model, identifies exactly the two exceptional values, proves sharp two/three/four-size support boundaries, and proves identifiability recovery by pairing the two natural normalization protocols. The cited article's discussion of a general rank test does not state this exceptional-exponent partition or the combined-protocol recovery theorem. St-Onge et al. (2022) analyze heterogeneous quenched/random hypergraphs through group-based approximate master equations; that process does not provide the identical finite annealed focal-generator inverse problem. Liyanage et al. (2025) treat general structural identifiability in compartmental ODEs without deriving this moment-map rank partition.

## Limitations

The rank theorem presumes known baseline transmission scale and known admissible group sizes, and describes ideal observation of all aggregate rates; unknown scale or partial observation can add ambiguity. There is no claim that observing two protocols is operationally feasible or that changing normalization leaves the underlying population unchanged in reality. The result does not extend the rank classification to arbitrary nonlinear exponent \(q>2\), persistent contact networks, correlated groups, or unobserved heterogeneity. The possibility of older equivalent classifications outside the inspected literature is a historical-priority risk. No independent scientific validation has been performed.

## References

1. R. Muslim, *Exact moment equivalence and structural nonidentifiability in nonlinear epidemics*, arXiv:2608.04943v1 (first public 2026-08-05), https://arxiv.org/abs/2608.04943; especially Sections II, III.1, III.3, III.4.
2. G. St-Onge et al., *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, Communications Physics 5, 25 (2022); arXiv:2105.07092, https://arxiv.org/html/2105.07092v2.
3. Y. R. Liyanage et al., *A Tutorial on Structural Identifiability of Epidemic Models Using StructuralIdentifiability.jl*, arXiv:2505.10517 (2025), https://arxiv.org/abs/2505.10517.
