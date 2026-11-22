# A golden-ratio exception to positive peak–valley covariance in Mallows permutations

## Finding

Let \(\pi\) be a Mallows random permutation of \([n]\), with \(\Pr(\pi)=q^{\operatorname{inv}(\pi)}/[n]_q!\), \(q>0\). Count interior peaks and valleys, respectively,
\[
P_n=\sum_{i=1}^{n-2}\mathbf1\{\pi_i<\pi_{i+1}>\pi_{i+2}\},\qquad
V_n=\sum_{i=1}^{n-2}\mathbf1\{\pi_i>\pi_{i+1}<\pi_{i+2}\}.
\]
Their **complete finite-sample covariance sign classification** is as follows:

* For \(n=3\), the covariance is strictly negative for every \(q>0\).
* For \(n=4\), put \(\varphi=(1+\sqrt5)/2\). The covariance is positive for \(0<q<\varphi^{-1}\) and for \(q>\varphi\); zero at \(q=\varphi^{-1},\varphi\); negative for \(\varphi^{-1}<q<\varphi\).
* For **every \(n\ge5\)**, the covariance is strictly positive for **every \(q>0\)**, without exceptions.

The exact formulas, valid at all real \(q>0\), are
\[
\operatorname{Cov}(P_3,V_3)=-\frac{q^2}{(1+q+q^2)^2},
\]
\[
\operatorname{Cov}(P_4,V_4)=
\frac{q(q^2-q-1)(q^2+q-1)}{(1+q)^2(1+q+q^2)^2}.
\]
For \(n\ge5\), define
\[
\begin{aligned}
S_3(q)&=1+q+q^2,\qquad S_5(q)=1+q+q^2+q^3+q^4,\\
T(q)&=q^6-q^5+2q^3-q+1,\\
F(q)&=2q^8+2q^7-3q^6-q^5+3q^4-q^3-3q^2+2q+2.
\end{aligned}
\]
Then
\[
\boxed{\operatorname{Cov}(P_n,V_n)=
\frac{q\left[F(q)+(n-5)(1+q)^2T(q)\right]}
{(1+q)^2S_3(q)^2S_5(q)}.}
\]

In addition, the peak and valley counts have the same variance. For \(n\ge4\),
\[
\operatorname{Var}(P_n)-\operatorname{Cov}(P_n,V_n)=\frac{q}{(1+q)^2}.
\]
Thus for every fixed \(q>0\) their correlation approaches one with the sharp correction
\[
\operatorname{Corr}(P_n,V_n)
=1-\frac{S_3(q)^2S_5(q)}{(1+q)^2T(q)}\frac1n+O_q(n^{-2}).
\]

## Assumptions and scope

All permutations of \([n]\) are included; inversions count pairs \(i<j\) with \(\pi_i>\pi_j\). The normalization is \([n]_q!=\prod_{j=1}^n(1+q+\cdots+q^{j-1})\). All peaks and valleys are **strictly interior**; neither sentinel endpoints nor circular comparisons are imposed. The threshold statement applies to integers \(n\ge3\) and real \(q>0\); it excludes the degenerate limiting measures at \(q=0\) or \(q=\infty\).

## Proof

**Local reduction.** Standardization of any contiguous window of length \(m\) has Mallows \((m,q)\) law; standardized orders in two disjoint contiguous windows are independent. This follows by conditioning on the unordered labels in each window: inversion contributions between distinct windows depend on the sets of labels, not on their internal ordering. This is the weak-dissociation and consecutive-homogeneity property of the Mallows distribution.

Write \(I_i\) and \(J_i\) for the peak and valley indicators at window \(i,i+1,i+2\). Disjoint windows have zero covariance, while overlap by one or two positions is determined completely by standardized permutations of four or five letters. Set
\[
\begin{aligned}
a(q)&=\operatorname{Cov}(I_i,J_i),\\
b(q)&=\operatorname{Cov}(I_i,J_{i+1})+\operatorname{Cov}(J_i,I_{i+1}),\\
c(q)&=\operatorname{Cov}(I_i,J_{i+2})+\operatorname{Cov}(J_i,I_{i+2}).
\end{aligned}
\]
Exact enumeration of the six prescribed local configurations in lengths three, four, and five, with each rank pattern weighted by \(q^{\operatorname{inv}}\), gives
\[
\begin{aligned}
a(q)&=-\frac{q^2}{S_3(q)^2},\\
b(q)&=\frac{q(q^4+2q^3+q^2+2q+1)}{(1+q)^2S_3(q)^2},\\
c(q)&=-\frac{q^2(q^6+2q^5+q^4-q^3+q^2+2q+1)}{(1+q)^2S_3(q)^2S_5(q)}.
\end{aligned}
\]
For \(n\ge4\), the covariance is the overlap sum
\[
(n-2)a(q)+(n-3)b(q)+(n-4)c(q).
\]
For \(n=3\) only the \(a(q)\) term is present. Algebraically simplifying the \(n=4\) expression gives the two golden-ratio zeros displayed above. At \(n=5\), this expression reduces to \(qF(q)/[(1+q)^2S_3(q)^2S_5(q)]\); each further increment of \(n\) adds \(a+b+c=qT(q)/[S_3(q)^2S_5(q)]\). This proves the exact family formula.

**Strict positivity for all larger sizes.** Put \(u=q+q^{-1}-2=(q-1)^2/q\ge0\). The reciprocal polynomials satisfy the identities
\[
q^{-4}F(q)=2u^4+18u^3+49u^2+37u+3,
\]
\[
q^{-3}T(q)=u^3+5u^2+5u+2.
\]
Every displayed coefficient is positive; hence \(F(q)>0\) and \(T(q)>0\) for all \(q>0\), proving strict positivity for every \(n\ge5\). For \(n=4\), the two quadratic factors have exactly the positive zeros \(\varphi^{-1}\) and \(\varphi\), respectively, yielding the complete sign classification.

**Near-perfect correlation.** For a descent indicator \(D_i=\mathbf1\{\pi_i>\pi_{i+1}\}\), the difference of the peak and valley counts telescopes:
\[
P_n-V_n=D_{n-1}-D_1.
\]
The Mallows law is invariant under simultaneous reversal of positions and complementation of values, which exchanges peaks and valleys. Hence their variances are equal. For \(n\ge4\), the endpoint descent indicators are independent Bernoulli variables of mean \(q/(1+q)\) by weak dissociation. Therefore \(\operatorname{Var}(P_n-V_n)=2q/(1+q)^2\) and the stated variance-minus-covariance identity follows. The exact covariance is \(nqT(q)/[S_3(q)^2S_5(q)]+O_q(1)\) with a strictly positive coefficient, so the correlation expansion follows by division.

## Verification

The standalone `CHECK.py` uses only the Python standard library. It independently enumerates every Mallows-weighted permutation for 26 size/parameter cases (all sizes three through seven at five rational parameters, and size eight at one parameter); separately constructs the four- and five-letter overlap probabilities as exact integer polynomials; and checks six universal rational-polynomial identities, including the length-affine formula. It also checks the two exact positivity-certificate identities. All checks passed on the packaged copy. Finite enumeration is only a cross-check, not the proof of the infinitely many cases, which rests on the displayed algebraic identities and positive-coefficient certificates.

## Relationship to prior work

Crane, DeSalvo and Elizalde establish weak dissociation and consecutive homogeneity for Mallows consecutive patterns and give overlap formulas for the variance of counts of a **single** specified pattern. Pan and Zeng's inversion-refined multivariate Eulerian generating function, reproduced explicitly by Dong, Lin and Pan, encodes peak and valley statistics jointly; **the underlying joint enumerator and its generic coefficient extraction are not claimed as new**. These are stronger enumerative frameworks, but their inspected statements do not present the strict finite-sample sign classification with the isolated four-letter golden-ratio reversal or the all-parameter correlation correction. A published result on peak–double-ascent covariance concerns a different paired statistic and a distinct large-size dependence transition, and neither its main formula nor its threshold inequality entails the present peak–valley sign theorem without additional analysis.

## Limitations

The theorem is about the Kendall-inversion Mallows law and interior extrema only. It does not imply stochastic association or independence; a positive covariance is weaker. The exact joint generating function was known and can in principle be differentiated to recover mixed moments; the contribution here is the independently verified **sharp sign inequality and boundary** and its quantitative near-perfect-correlation consequence. The original Pan–Zeng article could not be read directly using available access; its theorem was checked in its reproduced form in Dong–Lin–Pan. Therefore an earlier unstated equivalent inequality remains a historical-priority risk. No external independent mathematical audit has been performed.

## References

[1] H. Crane, S. DeSalvo and S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, first arXiv posting September 6, 2016, arXiv:1609.01370, https://arxiv.org/abs/1609.01370.

[2] Q. Pan and J. Zeng, *A q-analogue of generalized Eulerian polynomials with applications*, Advances in Applied Mathematics 104 (2019), 85–99, https://doi.org/10.1016/j.aam.2018.12.002.

[3] Y. Dong, Z. Lin and Q. Pan, *A q-analog of the Stirling-Eulerian Polynomials*, first arXiv posting April 15, 2024, arXiv:2404.09777, https://arxiv.org/abs/2404.09777. In particular, Theorem 1.2 explicitly reproduces the Pan–Zeng generating formula.

[4] A. Borodin, P. Diaconis and J. Fulman, *On adding a list of numbers (and other one-dependent determinantal processes)*, first arXiv posting April 23, 2009, arXiv:0904.3740, https://arxiv.org/abs/0904.3740.
