# Sharp structural identifiability of a replication-gated protein timing clock

## Finding
Consider the replication-gated Poisson protein-accumulation model described below, in which the only observable is the exact law of the first time \(T_\ell\) at which a cell has produced \(\ell\) proteins. When \(k>0\), \(\alpha>0\), \(\Lambda>1\), and the positive integers \(N,\ell\) are all unknown, **the law of \(T_\ell\) identifies every parameter uniquely except for exactly one sharp case**: \(N=\ell=1\) and \(k+\alpha\ne\Lambda k\). In that case it identifies \(k\) and the unordered pair \(\{k+\alpha,\Lambda k\}\); there are exactly two admissible parameter triples, interchanged by
\[
(k,\alpha,\Lambda)\longmapsto
\left(k,\Lambda k-k,\frac{k+\alpha}{k}\right).
\]
When \(N=\ell=1\) but \(k+\alpha=\Lambda k\), identification is unique. In the exceptional twofold case, observing the exact first-passage law at threshold \(\ell=2\), even without observing the replication event, resolves the ambiguity. At the excluded dosage boundary \(\Lambda=1\), the law reduces to an Erlang law independent of \(\alpha,N\); these hidden clock parameters cannot be recovered.

## Assumptions and scope
Let \(k,\alpha>0\), dosage \(\Lambda\ge1\), and integers \(N,\ell\ge1\). Initially there are no protein molecules and the gene is in replication stage zero. Independent rate-\(\alpha\) transitions move its stage sequentially through \(0,1,\ldots,N\). Protein productions are a Poisson process at rate \(k\) while the stage is below \(N\), and at rate \(\Lambda k\) thereafter. The replication clock is independent of basal protein-production randomness. Proteins do not degrade. Let \(T_\ell\) be the first time when the protein count reaches \(\ell\). An observation consists of the complete ideal probability distribution of \(T_\ell\), not a finite, noisy sample, and parameters are compared within this family of models. No independent observation of the replication time is assumed. If the dosage amplification is absent, \(\Lambda=1\), all positive \(\alpha\) and integers \(N\) are observationally equivalent at a fixed \(k,\ell\).

## Proof
**1. Rational law.** Set \(r=k+\alpha\), \(q=\Lambda k\), \(A=s+r\), and \(B=s+q\). The first-passage Laplace transform \(H_\ell(s)=\mathbb E[e^{-sT_\ell}]\) is, for \(s\ge0\),
\[
H_\ell(s)=
\sum_{j=0}^{N-1}\binom{\ell+j-1}{j}
 \frac{k^\ell\alpha^j}{A^{\ell+j}}
+\frac{\alpha^Nq^\ell}{A^NB^\ell}
\sum_{m=0}^{\ell-1}\binom{N+m-1}{m}
\left(\frac{B}{\Lambda A}\right)^m.
\tag{1}
\]
This is the finite-sum expression (S21) of Marmolejo-Lozano, Popović, and Grima (2026). It also follows from the absorbing Markov chain on the states \((i,j)\), with protein count \(i\in\{0,\ldots,\ell-1\}\) and replication stage \(j\in\{0,\ldots,N\}\): there are protein births at the stage-dependent rates and replication transitions at rate \(\alpha\). The first sum collects absorption before stage \(N\); the second collects absorption afterward. Equation (1) is a rational identity after combining the finite sums.

**2. Baseline rate and triggering count.** In (1), as \(s\to+\infty\), the only term of order \(s^{-\ell}\) is \(j=0\) of the first sum. Consequently
\[
H_\ell(s)=k^\ell s^{-\ell}(1+O(s^{-1})).
\tag{2}
\]
The order of decay identifies the integer \(\ell\), and its positive leading coefficient identifies \(k\). Hence two equal first-passage laws must share these values, even if neither was supplied beforehand.

**3. Exact poles, including the collision.** Suppose \(\Lambda>1\) and \(r\ne q\). At \(s=-q\), (1) has a pole of order exactly \(\ell\), with leading Laurent coefficient \(\alpha^Nq^\ell/(r-q)^N\ne0\). At \(s=-r\), it has a pole of order exactly \(\ell+N-1\): the highest-order terms are \(j=N-1\) of the first sum and \(m=\ell-1\) of the second, with combined coefficient
\[
k^\ell\alpha^{N-1}\binom{\ell+N-2}{N-1}
\left(1+\frac{\Lambda\alpha}{q-r}\right)
=k^\ell\alpha^{N-1}\binom{\ell+N-2}{N-1}
\frac{(\Lambda-1)r}{q-r}\ne0.
\tag{3}
\]
No other poles occur. If instead \(r=q\), every term of the second sum in (1) has denominator \((s+r)^{\ell+N}\), with a strictly positive total leading coefficient
\[
\alpha^Nq^\ell\sum_{m=0}^{\ell-1}
 \binom{N+m-1}{m}\Lambda^{-m}>0.
\tag{4}
\]
The first sum has lower pole order, so the law then has exactly one pole, of order \(\ell+N\). Thus the pole count separates the collision from the distinct-rate case, and the collision pole order recovers \(N\), while \(r=q\), \(\alpha=r-k\), and \(\Lambda=q/k\) recover all parameters.

With distinct poles, when \(N\ge2\) the orders \(\ell+N-1\) and \(\ell\) are different. Their locations recover the *ordered* rates \(r\) and \(q\), and their orders recover \(N\). The original parameters follow from \(\alpha=r-k\) and \(\Lambda=q/k\). Any other member of this family with the same rational function has the same poles and their multiplicities, hence cannot yield an additional representation with different \(N\).

**4. The only possible rate exchange.** When \(N=1\), both distinct poles have the same order \(\ell\). As both rates exceed \(k\), interchanging \(r\) and \(q\) always gives another *admissible* parameter triple; no other choice is possible from the pole set. Expand (1) at infinity:
\[
H_\ell(s)=k^\ell s^{-\ell}
\left[1+\frac{C_\ell(r,q)}s+O(s^{-2})\right],\quad
C_\ell(r,q)=-\ell r+(r-k)\sum_{j=1}^{\ell}(q/k)^j.
\tag{5}
\]
Let \(x=q/k>1\) and \(y=r/k>1\). Straight finite-sum rearrangement gives
\[
\frac{C_\ell(r,q)-C_\ell(q,r)}k
=(x-1)(y-1)\sum_{j=1}^{\ell-1}(\ell-j)(x^j-y^j).
\tag{6}
\]
For every \(\ell\ge2\), the right side has the strict sign of \(x-y\); the exchanged parameters therefore give *different* laws. For \(\ell=1\), the sum is empty, but a direct simplification of (1) proves the complete symmetry
\[
H_1(s)=\frac{ks+rq}{(s+r)(s+q)}.
\tag{7}
\]
This proves precisely two admissible representations if \(r\ne q\), and one if \(r=q\). An observation at \(\ell=2\) distinguishes the two representations by (6), providing the sharp second-threshold remedy.

**5. No-amplification boundary.** For \(\Lambda=1\), production is a homogeneous Poisson process with rate \(k\) regardless of the replication clock, so \(H_\ell(s)=(k/(s+k))^\ell\). No amplified model \(\Lambda>1\) has this law: (3) gives two noncancelling poles when the rates differ, while (4) gives a pole order strictly larger than \(\ell\) when they coincide. Hence the boundary stratification is complete.

## Verification
The standalone `check.py` computes the exact rational transforms, checks distinct and coincident pole multiplicities for 40 integer/rational configurations, verifies the rate-exchange identity for nine thresholds, and compares three independent finite-state absorbing-chain resolvents against the closed transform. It establishes the explicit witness
\[
(k,\alpha,\Lambda,N,\ell)=(1,2,4,1,1)
\quad\text{and}\quad(1,3,3,1,1),
\]
whose common transform is \((s+12)/[(s+3)(s+4)]\). At \(\ell=2\) the two numerators over the common denominator \((s+3)^2(s+4)^2\) are, respectively, \(s^2+48s+144\) and \(s^2+42s+144\), so the laws are different. Finite computer checks are auxiliary; the inequalities and pole noncancellation in (3), (4), and (6) provide the proof for all parameters. Run `python check.py` with Python 3.10+ and SymPy installed.

## Relationship to prior work
Marmolejo-Lozano, Popović, and Grima (2026) supply the precise protein-accumulation/replication model and its complete first-passage Laplace transform, including supplemental equation (S21), but study timing variability and its minimum rather than the global inverse parameter map. The present result **does not claim the transform or general phase-type pole theory as new**. Lindqvist (2023) and the classical work reviewed there establish general representational nonuniqueness and Coxian/phase-type canonical theory; these results do not themselves give the specific exchange/nonexchange classification across all thresholds and replication-stage counts for this biochemical subfamily. Rijal, Prasad, and Das (2020) study protein-threshold FPTs with feedback, and Verma et al. (2026) study mRNA thresholds with a different replication mechanism. Their accessible summaries do not establish the present full conditional-Erlang replication-clock classification; their inaccessible full texts are a residual priority limitation.

## Limitations
This is **structural** identifiability from an exact, complete one-dimensional distribution, not statistical consistency, finite-sample estimation, robustness, or model adequacy. Extremely close poles may make inference practically ill-conditioned despite theoretical uniqueness. Protein degradation, production bursts, age heterogeneity, thresholds defined by concentration rather than integer counts, and unknown initial protein counts fall outside the claim. The exact overlap comparison covers accessible primary and general literature, but historical equivalences outside it have not been excluded. Independent validation has not been performed.

## References
1. J. D. Marmolejo-Lozano, N. Popović, and R. Grima, *The impact of DNA replication on the timing of cellular events*, arXiv:2611.15356v1 (first released 2026-11-11), especially Eq. (S21). https://arxiv.org/html/2611.15356v1
2. B. H. Lindqvist, *Phase-type models for competing risks, with emphasis on identifiability issues*, Lifetime Data Analysis 29, 318–341 (2023), first released 2022-02-08. https://doi.org/10.1007/s10985-022-09547-7
3. K. Rijal, A. Prasad, and D. Das, *Protein hourglass: Exact first passage time distributions for protein thresholds*, Physical Review E 102, 052413 (2020). https://doi.org/10.1103/PhysRevE.102.052413
4. A. K. Verma, H. K. Barman, K. Rijal, and D. Das, *Distributions of threshold crossing times of messenger RNA* (2026), doi:10.64898/2026.08.20.745891. https://sciety.org/articles/activity/10.64898/2026.08.20.745891
