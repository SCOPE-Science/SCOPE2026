# A five-site Gini-instability threshold for the Cesàro residual

## Finding
For real finite sequences, the residual from prefix averaging crosses from nonexpansivity to strict amplification of complete-pair dispersion **exactly at five sites**. Define the quotient-seminorm \(\Lambda_n=\sup_{G_n(x)>0}G_n((I-C_n)x)/G_n(x)\). Then
\[
\Lambda_2=\frac12,\qquad \Lambda_3=\frac56,\qquad \Lambda_4=\frac{11}{12},\qquad \Lambda_n>1\quad(n\ge5).
\]
There is also an exact **leading-order** asymptotic, without an exact finite formula claimed for the larger dimensions:
\[
\lim_{n\to\infty}\frac{\Lambda_n}{\log n}=1.
\]
The threshold is sharp: it states precisely when one pass of the high-pass residual \(I-C_n\) can increase global pairwise variation, despite its bounded standard endpoint norms.

## Assumptions and scope
Fix an integer \(n\ge2\) and a real vector \(x=(x_1,\ldots,x_n)\). Let \((C_nx)_i=i^{-1}\sum_{j=1}^i x_j\), \(D_n=I-C_n\), and \(G_n(x)=\sum_{1\le i<j\le n}|x_i-x_j|\). Since \(D_n\mathbf1=0\), its quotient-seminorm modulo constant signals is well-defined. Let \(H_m=\sum_{j=1}^m 1/j\).

## Proof
**1. Binary cuts give the full operator norm.** Every nonconstant real vector admits the layer-cake representation \(x-\min x\,\mathbf1=\int \mathbf1_{\{x>t\}}\,dt\) over the interval from its minimum to its maximum. Linearity and the triangle inequality give \(G_n(D_nx)\le\int G_n(D_n\mathbf1_{\{x>t\}})\,dt\), while the exact coarea equality gives \(G_n(x)=\int |\{x>t\}|(n-|\{x>t\}|)\,dt\). Thus it suffices to test every nontrivial binary cut, and each such cut is itself admissible.

**2. Exact small dimensions.** Enumerating the nonempty proper subsets of \(\{1,\ldots,n\}\) yields the following *exhaustive* maxima of \(G_n(D_n\mathbf1_S)/(|S|(n-|S|))\): \(1/2\) among two cuts at \(n=2\), \(5/6\) among six cuts at \(n=3\), and \(11/12\) among fourteen cuts at \(n=4\). Each rational value is checked by the standalone exact-arithmetic program bundled with this result. These finite enumerations are complete, not sampling claims.

**3. A strict witness in every larger dimension.** For \(n\ge3\), take \(x=e_3\). The output has entries \(0\) before coordinate three, \(2/3\) at coordinate three, and \(-1/i\) at coordinate \(i>3\). Direct separation of the zero, positive, and negative pairs gives
\[
G_n(D_ne_3)=\frac{2(n-1)}3+(n+7)(H_n-H_3)-2(n-3).
\]
Since \(G_n(e_3)=n-1\), its amplification ratio \(R_n\) is the right-hand side divided by \(n-1\). Define
\[
F_n=(n+7)(H_n-H_3)-\frac{7n-19}{3}.
\]
The inequality \(R_n>1\) is equivalent to \(F_n>0\). Exact arithmetic gives \(F_5=1/15\) and \(F_6-F_5=17/60\). For every integer \(n\ge5\),
\[
(F_{n+2}-F_{n+1})-(F_{n+1}-F_n)=\frac{n-5}{(n+1)(n+2)}\ge0.
\]
All first differences are therefore positive from dimension five, and \(F_n>0\) for every \(n\ge5\).

**4. Universal column-mass estimate and sharp logarithmic leading term.** We prove an auxiliary inequality. For any real row-stochastic \(n\)-by-\(n\) matrix \(P\) with column sums \(c_j\) and \(M=\max_jc_j\), one has \(G_n(Px)\le M G_n(x)\) for every real \(x\). By the binary-cut reduction, take \(x=\mathbf1_S\) with \(k=|S|\) and put \(q=P\mathbf1_S\). Thus \(0\le q_i\le1\), \(s=\sum_iq_i\le Mk\), and \(n-s\le M(n-k)\). Since \(|a-b|\le a(1-b)+b(1-a)\) for \(a,b\in[0,1]\), summing over pairs gives
\[
G_n(q)\le s(n-s)-\sum_iq_i(1-q_i)\le s(n-s).
\]
If \(s\ge k\), then \(s(n-s)\le Mk(n-k)\); if \(s\le k\), the inequality follows instead from \(n-s\le M(n-k)\). This proves the auxiliary estimate for all real inputs by coarea. For \(P=C_n\), the largest column sum is \(H_n\). Therefore \(\Lambda_n\le 1+H_n\) by the triangle inequality for \(D_n=I-C_n\). The explicit witness gives
\[
\frac23+\frac{(n+7)(H_n-H_3)-2(n-3)}{n-1}\le\Lambda_n\le1+H_n\qquad(n\ge5).
\]
Both bounds equal \(\log n+O(1)\), establishing the asserted limit coefficient one.

## Verification
Run `python3 check_cesaro_residual.py` using Python's standard library. It exhausts all nontrivial binary cuts for \(n=2,3,4\), verifies the third-coordinate rational formula, the first- and second-difference identities, and the strict threshold through \(n=100\). It also checks a range of stochastic column-mass examples. The infinite-dimensional range \(n\ge5\) is established by the displayed first- and second-difference proof, **not** by that finite test range; the column-mass inequality and asymptotic are proved analytically.

## Relationship to prior work
The classical prefix Cesàro operator and its norm properties are extensively studied. Work on Cesàro operator orbits concerns different dynamical properties; work on Hardy-space Cesàro operators concerns analytic-function norms and spectra. Published \(\ell^p\)-norm results for the discrete residual \(C-I\) do not imply a stability threshold for the **quotient seminorm defined by all pairwise differences**. Likewise, an exact Gini norm for \(C_n\) alone does not determine that of \(I-C_n\), as the triangle inequality only gives a one-sided estimate. Here the residual requires its own signed-coordinate witness and a small-dimensional all-cut analysis.

## Limitations
Only one finite prefix Cesàro residual step is considered, with real inputs and unweighted complete-pair Gini variation. The exact values of \(\Lambda_n\) for \(n\ge5\), their maximizing inputs, weighted means, multiple residual steps, and complex signals are not classified. Historical priority is subject to inaccessible older sources, including the foundational 1965 Cesàro-operator paper; no claim of independence or outside certification is made.

## References
1. F. León–Saavedra, A. Piqueras–Lerena, and J. B. Seoane–Sepúlveda, *Orbits of Cesàro type operators*, Mathematische Nachrichten 282 (2009), 764–773. DOI: 10.1002/mana.200610769. First online date: 2009-04-16.
2. A. G. Arvanitidis and A. G. Siskakis, *Cesaro operators on the Hardy spaces of the half-plane*, arXiv:1006.1520v1 (2010-06-08).
3. G. Sinnamon, *Norm of the discrete Cesàro operator minus identity*, Mathematical Inequalities & Applications 25 (2022), 41–48. DOI: 10.7153/mia-2022-25-04.
4. A. Brown, P. R. Halmos, and A. L. Shields, *Cesàro operators*, Acta Scientiarum Mathematicarum 26 (1965), 125–137 (historical reference; full text not inspected).
