# Strict reverse likelihood-ratio ordering of marked birthday collisions

## Finding

Let \(m\ge2\), and let \(p_1,\ldots,p_m>0\) sum to one. Draw independent labels \(X_1,X_2,\ldots\) with \(\Pr(X_s=i)=p_i\). Let \(T\) be the first index at which a label repeats, and let \(C=X_T\) be the repeated label. For \(2\le t\le m+1\), the joint mass is
\[
K_{i,t}:=\Pr(C=i,T=t)=(t-1)!p_i^2 e_{t-2}(p_{-i}),
\]
where \(e_k\) is the \(k\)-th elementary symmetric polynomial, \(e_0=1\), and \(p_{-i}\) means the collection of all probabilities other than \(p_i\).

If \(p_i>p_j\), then **every** two times \(2\le t<u\le m+1\) obey
\[
K_{i,t}K_{j,u}>K_{i,u}K_{j,t}.
\]
In other words, the first-repeat time conditioned on repeating the higher-probability label is strictly *smaller in likelihood-ratio order* than the corresponding time conditioned on the lower-probability label. The conditional distribution functions satisfy
\[
\Pr(T\le t\mid C=i)>\Pr(T\le t\mid C=j),
\qquad 2\le t\le m,
\]
and therefore \(\mathbb E[T\mid C=i]<\mathbb E[T\mid C=j]\). Moreover, for each supported time \(t\), the joint mass \(K_{i,t}\) is strictly greater than \(K_{j,t}\), and \(T\) is independent of \(C\) if and only if the vector of label probabilities is uniform.

## Assumptions and scope

There are finitely many, at least two, labels; each probability is strictly positive. No distinctness, separation, or monotonicity of the full probability vector is assumed. The first repeated draw is counted, so the support of \(T\) is exactly the integers from \(2\) through \(m+1\). Equal-probability labels have identical rows in the joint law; the strict conclusions concern any two labels with strictly unequal probabilities. The probabilities are fixed during the sampling process, and the draws are independent.

For a list \(z_1,\ldots,z_r\), define \(e_k(z)=\sum_{|A|=k}\prod_{a\in A}z_a\) for \(0\le k\le r\), and set \(e_k=0\) otherwise. All conditional probabilities are well-defined because \(p_i>0\) for every label.

## Proof

**Joint distribution.** On \(\{C=i,T=t\}\), the first \(t-1\) sampled labels are distinct, precisely one is \(i\), the other \(t-2\) labels are chosen from the other \(m-1\) types, and draw \(t\) equals \(i\). For each choice of the other labels, the \(t-1\) initial distinct labels can be ordered in \((t-1)!\) ways. Multiplication of their probabilities and that of the final draw gives exactly \(K_{i,t}=(t-1)!p_i^2 e_{t-2}(p_{-i})\). These events partition the sample space because a repeat occurs by draw \(m+1\), and every entry is strictly positive.

**Strict likelihood-ratio comparison.** Fix \(i,j\) with \(p_i=p>q=p_j\). Let \(r=m-2\), and let \(E_k=e_k(p_{-\{i,j\}})\) for \(0\le k\le r\), with \(E_{-1}=E_{r+1}=0\). Then \(E_0=1\) and \(E_k>0\) on its natural range, including the empty-vector case \(r=0\). Separating the other marked label from the elementary symmetric sum yields
\[
\frac{K_{i,k+2}}{K_{j,k+2}}
=\frac{p^2}{q^2}\frac{E_k+qE_{k-1}}{E_k+pE_{k-1}},
\qquad 0\le k\le r+1.
\]
The denominators are all strictly positive, including at the maximal time \(k=r+1\). For adjacent indices \(k\) and \(k+1\), with \(0\le k\le r\), the cross-product difference of the unscaled fractions is
\[
(E_k+qE_{k-1})(E_{k+1}+pE_k)
-(E_{k+1}+qE_k)(E_k+pE_{k-1})
=(p-q)(E_k^2-E_{k-1}E_{k+1})>0.
\]
The final positivity uses the strict log-concavity of elementary symmetric coefficients of a positive finite vector: \(E_k^2>E_{k-1}E_{k+1}\). For interior indices this follows, for example, from Newton's inequalities applied to the real-rooted product \(\prod_{\ell\notin\{i,j\}}(1+p_\ell z)\); at the two boundaries it follows from \(E_{-1}=E_{r+1}=0\). For \(r=0\), the same boundary inequality is \(1>0\). Thus \(K_{i,t}/K_{j,t}\) is strictly decreasing through all supported times. Multiplying by positive entries establishes every stated strict two-by-two inequality.

**Implications.** Normalize each of the two rows by its positive sum to obtain the laws of \(T\) given \(C=i\) and \(C=j\). Their likelihood ratio remains strictly decreasing. A strictly decreasing likelihood ratio between two everywhere-positive mass functions forces strict stochastic ordering at every nontrivial cutoff: writing the difference of the two conditional cumulative masses, or using a one-crossing argument, proves the displayed strict conditional CDF inequality. The strict expected-time inequality follows by summing survival probabilities.

For each \(k=t-2\), subtraction gives
\[
K_{i,t}-K_{j,t}
=(t-1)!(p-q)[(p+q)E_k+pqE_{k-1}]>0;
\]
at the first time \(E_0>0\), and at the last time \(E_r>0\), so there are no exceptional boundaries. If all \(p_i\) are equal, permutation symmetry makes \(C\) uniform and independent of \(T\). Conversely, if some \(p_i>p_j\), the strict variation in their joint row ratio contradicts independence; this proves the independence characterization.

## Verification

The accompanying standalone Python 3 standard-library file `check.py` computes the proposed law using exact rational arithmetic. It also independently enumerates all possible drawing sequences up to the first repeat in four small rational examples, and checks the strict two-by-two inequalities, row comparison, cumulative ordering, and normalization for 807 additional weight vectors of sizes two through six. A successful run yields `PASS: 201721 exact assertions over 807 weight vectors plus 4 independent enumerations`. These finite checks diagnose formula or boundary errors; the preceding algebra and strict Newton inequality, not the enumerations, establish the theorem for all real positive vectors and all finite sizes.

As an exact example, take \((p_1,p_2,p_3)=(1/2,1/3,1/6)\). The conditional masses of \(T=2,3,4\) given \(C=1\) are \((3/7,3/7,1/7)\), compared with \((3/11,5/11,3/11)\) given \(C=3\). The likelihood ratio decreases strictly at each step.

## Relationship to prior work

The starting source is Camarri and Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, first available as Berkeley Statistics Report 523 dated June 1, 1998, later published in *Electronic Journal of Probability* 5 (2000), paper 2. Its equations (1), (2), (13) and Section 3.1 give **unmarked** first-repeat distributions and observed-set weights, and its main theorems characterize scaling limits; this provides basic counting context but does not state a label-conditioned strict likelihood-ratio comparison.

Flajolet, Gardy and Thimonier's *Birthday paradox, coupon collectors, caching algorithms and self-organizing search* (1987 report; 1992 journal publication), Section 3, studies expectations and generating functions for repeated labels under unequal probabilities, including a symmetric-polynomial waiting-time formula. Those formulas cover the basic unmarked enumeration mechanism; they do not supply the present all-pairs strict reverse likelihood-ratio ordering of the **marked** stopping event. Fadnavis's *A generalization of the Birthday problem and the chromatic polynomial* (2011) studies distinctness probabilities and majorization, a different comparison. Holst's *The general birthday problem* (1995) addresses the effect of equalizing probabilities on total waiting times; only its abstract could be checked, so this is a stated coverage risk. None of the comparisons is a proof of priority or uniqueness.

## Limitations

The theorem concerns the first repeat only, with finitely many strictly positive iid label probabilities. It does not assert corresponding orderings for later repeats, changing sampling distributions, arbitrary dependent sequences, or continuous label spaces. Historical priority beyond the inspected sources remains unverified. The elementary symmetric formula follows naturally from existing unmarked birthday enumerations; the contribution assessed here is the strict reverse likelihood-ratio and conditional stochastic-order structure, including its boundary and independence characterization.

## References

1. M. Camarri and J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, Berkeley Statistics Technical Report 523 (June 1, 1998), https://statistics.berkeley.edu/tech-reports/523 ; *Electronic Journal of Probability* 5 (2000), paper 2, https://doi.org/10.1214/EJP.v5-58.
2. P. Flajolet, D. Gardy and L. Thimonier, *Birthday paradox, coupon collectors, caching algorithms and self-organizing search*, INRIA Report RR-0720 (1987); *Discrete Applied Mathematics* 39 (1992), 207–229, https://doi.org/10.1016/0166-218X(92)90177-C; accessible report https://inria.hal.science/inria-00075832v1.
3. L. Holst, *The general birthday problem*, *Random Structures & Algorithms* 6 (1995), 201–208, https://doi.org/10.1002/rsa.3240060207.
4. S. Fadnavis, *A generalization of the Birthday problem and the chromatic polynomial* (2011), https://arxiv.org/abs/1105.0698.
