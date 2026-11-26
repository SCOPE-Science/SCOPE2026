# Eventual optimal leader allocation on highly imbalanced complete bipartite graphs

## Finding
On the simple unit-conductance graph \(K_{p,q}\) with \(p,q\ge2\), ground exactly \(k\) noise-free leaders and minimize \(\operatorname{tr}(L_{FF}^{-1})\), with \(L_{FF}\) the follower principal block of the original combinatorial Laplacian. Fix \(p\) and \(k\ge1\), then take \(q\) sufficiently large (depending on \(p,k\)). Put \(r=\min\{j\ge1:j(j+1)\ge p\}\). The possible numbers \(a\) of leaders in the fixed part are exactly as follows:

* If \(p<r(r+1)\) or \(k\le r\), only \(a=\min(k,r)\) is optimal.
* Otherwise \(p=r(r+1)\), \(k\ge r+1\). If \(2k<3(r+1)\), only \(a=r+1\) is optimal. If \(2k>3(r+1)\), only \(a=r\) is optimal.
* If \(p=r(r+1)\) and \(2k=3(r+1)\), only \(a=r\) is optimal for \(r>1\), while \(a=1\) and \(a=2\) are both optimal for \((p,k)=(2,3)\).

Every choice of the required vertices in the respective parts attains the same value. The unconstrained small-part allocation scale is \(r\sim\sqrt p\); this comparison is made after the fixed-\(p,k\), large-\(q\) classification, with the budget constraint in the theorem. No simultaneous-growth assertion is made.

## Proof
For \(a\) leaders in the first part set \(x=p-a\), \(y=q-k+a\). For positive \(x,y\), the grounded matrix \(\left(\begin{smallmatrix}qI_x&-J_{x,y}\\-J_{y,x}&pI_y\end{smallmatrix}\right)\) has eigenvalues \(q,p\) on within-part zero-sum spaces of dimensions \(x-1,y-1\). Its remaining block in normalized part-constant coordinates has diagonal \(q,p\) and off-diagonal \(-\sqrt{xy}\). This gives the standard block formula
\[
C(a)=\frac{x-1}{q}+\frac{y-1}{p}+\frac{p+q}{pq-xy}.
\tag{1}
\]
It also holds when one part is empty by cancellation, in agreement with diagonal inversion. Since \(k\ge1\) and at least one follower remains, \(pq>xy\). The objective depends only on the counts.

Eventually the feasible counts are \(0,1,\ldots,\min(p,k)\). At zero the cost is \(q/p+q/(pk)+O_{p,k}(1)\), whereas for \(a\ge1\) it is \(q/p+(a-k-1)/p+1/a+O_{p,k}(q^{-1})\). Thus zero and all counts not minimizing \(g(a)=a/p+1/a\) are eventually suboptimal, since the candidate set is finite. The adjacent difference \(g(a+1)-g(a)=1/p-1/[a(a+1)]\) proves the unique count when the budget truncates before the tie, or \(p<r(r+1)\); otherwise the only candidates are \(r,r+1\).

To break that tie, put \(B_a=(p-a)(k-a)\); the last term in (1) is \((q+p)/(aq+B_a)\). The coefficients of \(q^{-1}\) and \(q^{-2}\) in \(C(a)\) are
\[
h(a)=p-a-1+p/a-B_a/a^2,\qquad j(a)=\frac{(B_a/a)(B_a/a-p)}a.
\]
The remainder after those terms is \(O_{p,k}(q^{-3})\), uniformly over the finite set of positive counts, by expansion of \((1+B_a/(aq))^{-1}\). For \(p=r(r+1)\), substitution gives \(B_r=r^2(k-r)\), \(B_{r+1}=(r-1)(r+1)(k-r-1)\), hence
\[
h(r+1)-h(r)=\frac{2k-3(r+1)}{r+1}.
\]
At equality, \(B_r/r=r(r+3)/2\) and \(B_{r+1}/(r+1)=(r^2-1)/2\). Substitution into \(j\) therefore gives \(j(r+1)-j(r)=(r-1)^2/4\). This is positive if \(r>1\), selecting \(r\). For \(r=1,k=3,p=2\), formula (1) gives \(C(1)=(q-1)/2=C(2)\) for all sufficiently large \(q\), and zero was already excluded. Finally \(r(r-1)<p\le r(r+1)\) yields the square-root scale.

## Relation to prior work and limits
The inverse-trace criterion is standard (Lin–Fardad–Jovanović, [arXiv:1302.0450](https://arxiv.org/abs/1302.0450), §II-A; Fitch–Leonard, [arXiv:1407.1569](https://arxiv.org/abs/1407.1569), §I). Treat (1) as a preparatory block computation, not as a new evaluated coherence formula. Wang, Wang and Sun, [doi:10.1142/S012918312450092X](https://doi.org/10.1142/S012918312450092X), report exact leader–follower coherence for freely assigned leaders on complete multipartite networks in their abstract. Full text was not available in the comparison, so overlap with the eventual optimizer classification cannot be excluded on that evidence alone.

The 25 Oct. 2026 Resultary three-leader allocation record (`133a17f467a6`, Finding and Proof §1) already gives (1) for three leaders, with a large-\(q\) allocation table including the tie \((p,k)=(2,3)\). The 25 Oct. nearly balanced square-root switch (`16f6de623c22`, Finding and Eq. (1)) classifies \(K_{m,m+1}\) in all budgets, implying the nonnested \(K_{2,3}\) example. The 2 Nov. hub-threshold result (`6f11a7095f0f`, Finding and class-cost proof) gives a fixed-two-vertex-part threshold that implies the mixed \(K_{2,9}\) example. Neither example is a new claim here. The finding compares arbitrary fixed part sizes and budgets at large imbalance, including the higher-order comparison needed on the pronic tie locus \(p=r(r+1)\). The inspected earlier special cases do not give this general classification. Historical priority is not certified.

## Verification
The all-parameter conclusion follows from the exact expansion and finite-candidate argument. A separate symbolic subtraction checked both adjacent coefficient formulas. For a finite exact check of the tied leading-order regime, enumerate \(r=1,\ldots,12\), \(k=1,\ldots,3r+6\), with \(p=r(r+1)\) and \(q\in\{10^6,10^8\}\). Evaluate (1) as a rational number for each feasible count and compare the full minimizing set to the theorem. All 612 comparisons agreed. These tests neither provide a uniform cutoff in \(q\) nor establish the infinite result by themselves.
