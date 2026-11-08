# A two-threshold peak invariance law for record-biased random permutations

## Finding
For every integer \(n\ge3\), bias \(\theta>0\) and interior position \(2\le i\le n-1\), let \(\pi\) be sampled from the record-biased law \(\mathbb P_\theta(\pi)=\theta^{\operatorname{rec}(\pi)}/(\theta)^{\overline n}\), where \(\operatorname{rec}\) counts left-to-right maxima and \((\theta)^{\overline n}=\prod_{j=0}^{n-1}(\theta+j)\). The strict local-peak probability is exactly
\[
\mathbb P_\theta\{\pi(i-1)<\pi(i)>\pi(i+1)\}=\frac13-\frac{\theta(\theta-1)(\theta-2)}{3(\theta+i-2)(\theta+i-1)(\theta+i)}.
\]
Therefore **every interior peak probability** equals its uniform-permutation value \(1/3\) precisely at the two positive biases \(\theta=1\) and \(\theta=2\). It is strictly above \(1/3\) throughout \(1<\theta<2\), and strictly below it for \(0<\theta<1\) and \(\theta>2\). This classification holds at every finite size and every interior position.

Writing \(P_n=\sum_{i=2}^{n-1}\mathbf1\{\pi(i-1)<\pi(i)>\pi(i+1)\}\), its exact expectation is
\[
\mathbb E_\theta P_n=\frac{n-2}{3}-\frac{(\theta-1)(\theta-2)}6\left(\frac1{\theta+1}-\frac{\theta}{(\theta+n-2)(\theta+n-1)}\right).
\]
The sign of the bias in this expectation is the same as the local sign, since the bracket is strictly positive.

## Assumptions and scope
The permutation is of \(\{1,\dots,n\}\), records are *strict* left-to-right maxima, and peaks occur only at interior indices. The parameter \(\theta\) is a fixed positive real, with no asymptotic restriction. The rising factorial normalizes the probability law. No assertion is made about the *complete joint peak-set distribution* or higher peak moments.

## Proof
Use the insertion-rank representation of record-biased permutations: for \(1\le j\le n\), \(R_j\) is the rank of \(\pi(j)\) among \(\pi(1),\dots,\pi(j)\), and these ranks are independent, with \(\mathbb P(R_j=j)=\theta/(\theta+j-1)\) and \(\mathbb P(R_j=r)=1/(\theta+j-1)\) for \(1\le r<j\). This can also be proved directly: the Lehmer-type rank sequence bijectively specifies the permutation, and each time \(R_j=j\) corresponds exactly to a record, so the product of the stated independent rank masses is the given record-bias weight.

Fix \(2\le i\le n-1\). The event \(\pi(i-1)<\pi(i)>\pi(i+1)\) is exactly \(R_{i-1}<R_i\) together with \(R_{i+1}\le R_i\). If \(R_i=b<i\), the probability of these two conditions conditional on \(R_i=b\) is \((b-1)b/[(\theta+i-2)(\theta+i)]\). If \(R_i=i\), the corresponding probability is \(i/(\theta+i)\). Independence of ranks and \(\sum_{b=1}^{i-1}b(b-1)=i(i-1)(i-2)/3\) give
\[
\mathbb P_\theta(\text{peak at }i)
=\frac{ i[\theta(\theta+i-2)+(i-1)(i-2)/3]}{(\theta+i-2)(\theta+i-1)(\theta+i)}.
\]
Subtracting \(1/3\) and factoring the resulting cubic numerator gives the displayed peak-probability formula. All denominator factors are strictly positive, and the sign is controlled by \(-\theta(\theta-1)(\theta-2)\); hence the sharp two-threshold classification, including the fact that there are no other positive zeroes.

For the expectation, sum the local probabilities and use the telescoping identity
\[
\frac1{x(x+1)(x+2)}=\frac12\left(\frac1{x(x+1)}-\frac1{(x+1)(x+2)}\right).
\]
The bracket in the expectation expression is positive because \((\theta+n-2)(\theta+n-1)>\theta(\theta+1)\) for \(n\ge3\).

## Verification
A self-contained Python standard-library program, `verify.py`, exhaustively sums the exact \(\theta^{\operatorname{rec}}\) weights of all \(n!\) permutations for \(3\le n\le8\) and the five rational biases \(\theta\in\{1/2,1,3/2,2,3\}\). It compares every interior peak probability, the expected peak total, the rising-factorial normalizer, and the sign classification using exact rational arithmetic. Its recorded execution result was `VERIFY_OK 270 exact assertions`. Finite checks corroborate the algebraic proof but are not a substitute for it.

## Relationship to prior work
Bouvel, Nicaud and Pivoteau introduced the present record-biased framework and give its independent-rank construction and analyses of several statistics, including descents; their relevant 2024 open preprint sections do not report this local peak law. The older paper by Billey, Burdzy and Sagan studies peak sets under the **uniform** permutation measure. Gessel and Zhuang give strong peak/descents generating functions jointly with **cycle type**; their cycle-weighted ensemble is not the present record-weighted measure (left-to-right maxima are not permutation cycles in one-line notation). In particular, those generating functions do not directly imply this exact record-bias phase classification. The source model and independent ranks are credited, not claimed as novel.

## Limitations
This is an exact one-point peak-marginal and expectation theorem, not an assertion that the full peak-set law is unchanged at the exceptional biases. The proof is finite and uniform in \(n\) but does not establish variance, joint limits, or large deviations. Related unlocated record-biased peak enumerations may have implicit equivalent formulas; historical priority is not independently settled.

## References
1. M. Bouvel, C. Nicaud and C. Pivoteau, *Record-biased permutations and their permuton limit*, arXiv:2409.01692v1 (public 2024-09-03), https://arxiv.org/abs/2409.01692 . Primary MSC 60C05 on the journal record.
2. S. Billey, K. Burdzy and B. Sagan, *Permutations with given peak set*, arXiv:1209.0693 (2012), https://arxiv.org/abs/1209.0693 .
3. I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654 (2020), https://arxiv.org/abs/2001.00654 .
