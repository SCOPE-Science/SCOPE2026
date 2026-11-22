# Three communities are sharp for transmissibility-dependent outbreak-source ranking reversals

## Finding

For every finite two-type Poisson Galton–Watson epidemic with strictly positive mean-offspring matrix \(B=(b_{ij})\), the ordering of the two introduction-site survival probabilities is exactly the ordering of their *total* expected offspring counts, at **every supercritical uniform transmissibility** \(\tau>1/\rho(B)\). Specifically, writing \(r_i=\sum_j b_{ij}\) and \(p_i(\tau)\) for the probability of perpetual nonextinction from one initial type-\(i\) infection,
\[
\operatorname{sgn}\bigl(p_1(\tau)-p_2(\tau)\bigr)=\operatorname{sgn}(r_1-r_2).
\]
Three types are the sharp minimum for violation of this ordinal rule and for a strict *transmissibility-dependent* reversal in the ordering of introduction-site survival probabilities. The witness below has \(r_1>r_2\), but \(p_1(1)<p_2(1)\) and \(p_1(20)>p_2(20)\), despite all nine reproduction links being strictly positive. By continuity there is at least one crossing \(\tau_*\in(1,20)\); no uniqueness of the crossing is asserted.

## Assumptions and scope

There are \(n\in\{1,2,3\}\) types (communities). Each infected type-\(i\) parent independently generates \(\operatorname{Poisson}(\tau b_{ij})\) type-\(j\) children for each \(j\). Different parents also reproduce independently. Thus each row of \(B\) describes infections **from** one source community (the transpose of the convention for the reproduction operator in Wang and Valdano). Assume every \(b_{ij}>0\), and \(\tau>0\); the supercritical condition is \(\tau\rho(B)>1\). Survival probabilities are the unique strictly positive solution of
\[
 p_i=1-\exp\!\left(-\tau\sum_{j=1}^n b_{ij}p_j\right),\qquad 1\le i\le n.
\]
All claims concern the early-stage infinite-branching approximation, not finite-population outbreak size or a time-varying epidemic reproduction operator. The row sums \(r_i\) are mean *total* offspring from type \(i\), including within-community and cross-community offspring.

## Proof

**Positive fixed point.** Define \(F_\tau(p)_i=1-\exp[-\tau(Bp)_i]\). If \(\tau\rho(B)>1\), a small positive multiple of a Perron right eigenvector is a strict subsolution, while the all-ones vector is a strict supersolution. Monotone iteration gives a positive fixed point. It is unique: if two positive fixed points \(u,v\) differ and \(\theta=\max_i(u_i/v_i)>1\), then at an index attaining \(u_i=\theta v_i\), strict subhomogeneity of \(1-e^{-x}\) yields \(u_i=F_\tau(u)_i\le F_\tau(\theta v)_i<\theta F_\tau(v)_i=\theta v_i\), a contradiction. Reverse the roles of \(u,v\) if necessary. The Jacobian at this fixed point satisfies \(DF_\tau(p)p<p\) componentwise, since \(z e^{-z}<1-e^{-z}\) for every \(z>0\). Consequently its spectral radius is below one and the fixed point depends continuously (indeed smoothly) on \(\tau\) on the supercritical interval.

**Two-type rigidity.** Put \(h(x)=-\log(1-x)/x\), strictly increasing on \((0,1)\); indeed the derivative numerator is \(x/(1-x)+\log(1-x)>0\). If \(p_1>p_2\), divide the logarithmic fixed-point equations by the respective positive \(p_i\) to obtain
\[
\tau r_1>\tau\left(b_{11}+b_{12}\frac{p_2}{p_1}\right)=h(p_1)>h(p_2)=\tau\left(b_{21}\frac{p_1}{p_2}+b_{22}\right)>\tau r_2.
\]
Thus \(p_1>p_2\) forces \(r_1>r_2\). The symmetrical argument shows \(p_1<p_2\) forces \(r_1<r_2\). If \(p_1=p_2>0\), the same fixed-point equations force \(r_1=r_2\). Trichotomy proves the claimed equivalence, including equality. In particular its sign is independent of the common scale \(\tau\) for all supercritical \(\tau\). For one type there is no pair of sources to compare.

**A three-type complete-mixing witness.** Take the strictly positive, rational matrix
\[
 B=\begin{pmatrix}
 1/10&1/1000&5\\
 1/1000&2&1/1000\\
 1/1000&1/1000&1/10
 \end{pmatrix},\quad
 (r_1,r_2,r_3)=(5101/1000,1001/500,51/500).
\]
Since \(b_{22}=2\), strict positivity gives \(\rho(B)>2\), so \(\tau=1\) and \(\tau=20\) both have positive, unique survival vectors. At \(\tau=1\), the second type's within-type offspring alone have mean two. Hence \(p_2\) exceeds the positive solution of \(s=1-e^{-2s}\), which is greater than \(1/2\) because \(1-e^{-1}>1/2\). Using \(1-e^{-z}\le z\), \(p_1,p_2\le1\) and the third fixed-point equation gives
\[
 p_3\le\frac{p_1+p_2}{1000}+\frac{p_3}{10}
 \le\frac1{500}+\frac{p_3}{10},\qquad p_3\le\frac1{450}.
\]
The first fixed-point equation then gives
\[
 p_1\le\frac{p_1}{10}+\frac1{1000}+5p_3
 \le\frac{p_1}{10}+\frac1{1000}+\frac1{90},\qquad
 p_1\le\frac{109}{8100}<\frac1{50}<\frac12<p_2.
\]
At \(\tau=20\), the third type's self-offspring have mean two, so \(p_3>1/2\). Consequently
\[
 p_1=1-e^{-20(Bp)_1}>1-e^{-50},
 \qquad p_2=1-e^{-20(Bp)_2}\le1-e^{-20r_2}=1-e^{-40.04}.
\]
Since \(50>40.04\), these bounds imply \(p_1(20)>p_2(20)\). Continuity in \(\tau\) provides a crossing in \((1,20)\). Strict inequalities survive sufficiently small perturbations of the nine positive entries. Since the two-type theorem excludes all crossings for \(n\le2\), the dimension three is sharp.

## Verification

The supplied `verify.py` checks the exact rational row sums, strict matrix positivity, the \(109/8100\) and exponent inequalities, and numerically iterates the independent-Poisson branching fixed-point map from the all-ones supersolution. It also tests the two-type ordering across deterministic-seed randomized strictly positive matrices and transmissibility scales. Floating-point probabilities at \(\tau=20\) round to one; the verifier compares log-extinction exponents instead. All-size and all-matrix statements rest on the analytical inequalities above, not the finite numerical tests.

## Relationship to prior work

Wang and Valdano (first public preprint posted January 27, 2026; published July 2026) introduce a seed-specific outbreak reproduction ratio and the Poisson multitype survival fixed point. They show that mean total reproduction does not encode the magnitude of introduction-site outbreak risk and analyze homogeneous total reproductive potential, but do not establish the **two-type exact ordinal law**, its all-transmissibility invariance, or the **sharp three-type crossing witness**. Their general multitype fixed-point formula is the starting point here, not a theorem already asserting the present rank rigidity. Earlier classical multitype branching theory gives the extinction/supercriticality criterion, not this source-ranking classification. Other work on source ranking in network SIS models or on finite-outbreak risk concerns different outcomes and equations.

## Limitations

This is an exact mathematical statement for independent-Poisson, positive, finite-type Galton–Watson offspring only. The two-type ordering need not extend to type-dependent overdispersion or non-Poisson offspring, and no such extension is asserted. The three-type witness need not be a calibrated real contact network. The theorem guarantees *at least one*, not exactly one, rank crossing; it addresses perpetual branching survival, not finite-horizon incidence, epidemic size, or later susceptible depletion. No independent assessment of mathematical priority has been performed.

## References

- B. Wang and E. Valdano, *Redefining and estimating the early-phase reproduction ratio for epidemic outbreaks in spatially structured populations*, medRxiv v1, posted January 27, 2026, doi:10.64898/2026.01.26.26344841; *PLOS Computational Biology* 22 (2026), e1014425, doi:10.1371/journal.pcbi.1014425. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13349308/ .
- P. van der Hofstad, *Random Graphs and Complex Networks*, Vol. 2, Cambridge University Press, §3.4 (standard multitype Poisson branching survival criterion), doi:10.1017/9781316795552.004.
