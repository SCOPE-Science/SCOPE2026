# A three-phase support law for robust maximal lotteries, with a pooled Condorcet-loser reversal

## Finding

Consider three alternatives \(A,B,C\) and two populations in which \(A\) and \(B\), respectively, are strict Condorcet winners, with the same pairwise majority-margin magnitudes in mirror order. For an exact interval of uncertain population weights, the robust maximal lottery has a fully explicit support classification at maximum ambiguity. In a separate open parameter region, increasing the robustness radius forces a discontinuous change from the equal lottery on \(A,B\) to a deterministic choice of \(C\), despite \(C\) being the strict Condorcet loser of the equally pooled electorate.

Write the two skew-symmetric group margin matrices, in alternative order \(A,B,C\), as
\[
M^{(1)}=\begin{pmatrix}0&u&v\\-u&0&-w\\-v&w&0\end{pmatrix},\qquad
M^{(2)}=\begin{pmatrix}0&-u&-w\\u&0&v\\w&-v&0\end{pmatrix},
\]
where \(0<u,v,w\leq1\). For \(0<r\leq1\), let \(\mathcal W_r\) consist of group-1 mixture weights in \([(1-r)/2,(1+r)/2]\). A robust lottery maximizes
\[
V_r(p)=\min_{\theta\in\mathcal W_r}\min_{j\in\{A,B,C\}}p^{\mathsf T}\left(\theta M^{(1)}+(1-\theta)M^{(2)}\right)e_j.
\]

**Full ambiguity, exact classification.** Every maximizer has the form \(p=((1-z)/2,(1-z)/2,z)\). At \(r=1\), all maximizers are classified by
\[
\begin{array}{c|c}
\text{condition}&\text{optimal }z\\ \hline
u<2v,\ w\leq u+v&0\text{ uniquely}\\
u<2v,\ w>u+v&(w-u-v)/(w+v-u)\text{ uniquely}\\
u>2v&1\text{ uniquely}\\
u=2v,\ w\leq3v&[0,1]\\
u=2v,\ w>3v&[(w-3v)/(w-v),1].
\end{array}
\]
Thus, depending on quantitative margins, the unique robust lottery may have support of size two, three, or one, even though both groupwise maximal lotteries have support one.

**Pooled Condorcet-loser reversal.** If \(0<w<v\) and \(u>2v\), let
\[
r_c=\frac{v-w}{u-v-w}\in(0,1).
\]
Then the entire radius path, excluding the unrobust endpoint \(r=0\), is
\[
\operatorname{argmax}V_r=
\begin{cases}
\{(1/2,1/2,0)\},&0<r<r_c,\\
\{((1-z)/2,(1-z)/2,z):0\leq z\leq1\},&r=r_c,\\
\{(0,0,1)\},&r_c<r\leq1.
\end{cases}
\]
Nevertheless the evenly pooled matrix \((M^{(1)}+M^{(2)})/2\) has margins \((v-w)/2>0\) for both \(A\) versus \(C\) and \(B\) versus \(C\). Therefore \(C\) is its **strict Condorcet loser**, excluded by its ordinary maximal lottery, while it is the unique robust choice for every \(r>r_c\).

## Assumptions and scope

Pairwise margins mean the fraction ranking the first alternative above the second minus the fraction ranking it below; they lie in \([-1,1]\). All preferences are strict and complete. The matrix statements apply to any attainable margins \(u,v,w\) in the stated range. Group 1 ranks \(A\) over both rivals in majority comparisons, and group 2 ranks \(B\) over both rivals. This theorem is about the worst-case game guarantee \(V_r\), **not** optimizing a weighted sum of separately computed maximal lotteries. There are no stochastic sampling assumptions. The relevant group-weight uncertainty is total variation radius \(\rho=r/2\) about equal weights; for larger radii \(r=1\) suffices.

For a concrete profile realizing the reversal, in group 1 of twenty voters take \(3\) ballots \(A\succ C\succ B\), \(7\) ballots \(A\succ B\succ C\), \(2\) ballots \(B\succ A\succ C\), and \(8\) ballots \(C\succ A\succ B\); group 2 swaps the labels \(A\) and \(B\) in each ballot. This realizes \((u,v,w)=(4/5,1/5,1/10)\), so \(r_c=1/5\), or total-variation radius \(\rho_c=1/10\).

A separate twenty-voter-per-group strict-profile example realizes full support at \(r=1\): group 1 has \(12\) ballots \(A\succ C\succ B\), \(2\) ballots \(B\succ A\succ C\), and \(6\) ballots \(C\succ B\succ A\), with group 2 obtained by swapping \(A,B\). Here \((u,v,w)=(1/5,2/5,4/5)\) and the unique robust lottery is \((2/5,2/5,1/5)\).

## Proof

**Reduction to one scalar.** Set \(p=(x,y,z)\), \(x+y+z=1\), and \(d=(x-y)/2\), so that \(x=(1-z)/2+d\) and \(y=(1-z)/2-d\). The worst-case group weight for a fixed opponent is an endpoint of the weight interval. Direct multiplication of both margin matrices gives
\[
V_r(p)=\min\left\{-ru\left(\frac{1-z}{2}+|d|\right)
+\frac{z}{2}\bigl(w-v-r(w+v)\bigr),\quad
\frac{(v-w)(1-z)}{2}-r(v+w)|d|\right\}.
\]
Both displayed expressions strictly decrease with \(|d|\), because \(r,u,v,w>0\); hence every maximizer has \(d=0\), not merely some maximizer. With \(d=0\), the objective is the lower envelope of two affine functions of \(z\in[0,1]\):
\[
f_1(z)=-\frac{ru}{2}+\frac{w-v+r(u-w-v)}{2}z,\qquad
f_3(z)=\frac{(v-w)(1-z)}{2}.
\]
Thus all claimed finite-dimensional cases follow from exact comparison of slopes and endpoint/intersection values; no limiting or discrete approximation is needed.

**Full-ambiguity classification.** At \(r=1\), \(f_1(z)=-u/2+(u-2v)z/2\). If \(u>2v\), it is strictly increasing and satisfies \(f_1(1)=-v<f_3(1)=0\), so the lower envelope uniquely maximizes at \(z=1\). If \(u<2v\), \(f_1\) is strictly decreasing. For \(w\leq u+v\), \(f_3(0)\geq f_1(0)\), and \(z=0\) uniquely maximizes the envelope. For \(w>u+v\), \(f_3\) is strictly increasing and initially below \(f_1\); the unique maximizing intersection solves \(f_1(z)=f_3(z)\), giving \(z=(w-u-v)/(w+v-u)\). If \(u=2v\), \(f_1\equiv-v\), so precisely those \(z\) with \(f_3(z)\geq-v\) are optimal, yielding the two stated intervals at \(w=3v\). This proves every boundary case.

**Radius transition.** Under \(0<w<v\) and \(u>2v\), \(f_3(z)\geq0\) throughout \([0,1]\), whereas \(f_1(0)=-ru/2<0\) and \(f_1(1)=(w-v-r(w+v))/2<0\). Because \(f_1\) is affine, it stays negative and the lower envelope equals \(f_1\) everywhere. Its slope has the sign of \((w-v)+r(u-w-v)\). The denominator \(u-v-w\) is positive, and \(0<r_c=(v-w)/(u-v-w)<1\) because \(u>2v\). Therefore the slope is negative, zero, or positive as \(r\) lies below, at, or above \(r_c\). The three optimal sets follow. The groupwise winners and strict pooled loser follow directly by inspecting signs in the matrices. In the twenty-ballot examples, counting the given strict comparisons verifies all specified rational margins exactly.

## Verification

The standalone file `robust_lottery_verify.py` uses only Python's standard library and exact rational arithmetic. It independently enumerates vertices of the four-variable robust linear program (lottery coordinates plus guarantee) using all six opponent/end-weight inequalities and three simplex inequalities. It compares exact optimal values with the derived scalar envelope on \(625\) quadruples \((u,v,w,r)\) with positive coordinates on a five-point grid, checks all three explicitly realizable twenty-ballot triples, and tests the radius switch. Run from the extracted package directory: `python robust_lottery_verify.py`. Reported output: `PASS: 625 exact rational LP/analytic comparisons; 3 exact ballot profiles; radius switch 1/5`. This finite test does **not** replace the analytic proof of the universal classification.

## Relationship to prior work

Khalaf, Wang, Halpern, Shapira, du Pin Calmon and Procaccia (2026) introduce robust maximal lotteries over varying subpopulation weights, prove robust Condorcet and dominance properties, and give a general linear-programming formulation (Theorems 8, 9 and 17). That framework is directly used here. Their relevant text and appendix do not state this opposed-winner three-alternative support classification, the explicit rational parameter chambers, or the pooled-Condorcet-loser reversal with a sharp ambiguity-radius threshold. The general LP permits instance-specific numerical solution but does not by itself provide these quantified analytic support and uniqueness conclusions. Classical maximal lotteries concern one fixed matrix and exclude a strict Condorcet loser of that matrix; they are not equivalent to the worst-case population-shift problem.

## Limitations

This is a symmetric two-population, three-alternative subfamily; no claim is made for all pairs of three-alternative margin matrices or more populations. The classification at full ambiguity and the stated radius transition are exact, but the theorem does not assert a full support-phase classification at all intermediate radii for arbitrary \((u,v,w)\). Originality is based on accessible literature and research-record comparison, not an independent exhaustive literature certification. Self-review has been performed; independent audit has not.

## References

1. H. Khalaf, S. L. Wang, D. Halpern, I. Shapira, F. du Pin Calmon, and A. D. Procaccia, *Robust AI Evaluation through Maximal Lotteries*, arXiv:2602.21297v1, first publicly posted 24 February 2026. https://arxiv.org/html/2602.21297v1
2. F. Brandl, C. Brandt, and H. G. Seedig, *Consistent Probabilistic Social Choice*, Econometrica 84 (2016), 1839–1880. https://arxiv.org/abs/1503.00694
3. F. Brandl and collaborators, *A natural adaptive process for collective decision-making*, Theoretical Economics (2024). https://onlinelibrary.wiley.com/doi/full/10.3982/TE5380
