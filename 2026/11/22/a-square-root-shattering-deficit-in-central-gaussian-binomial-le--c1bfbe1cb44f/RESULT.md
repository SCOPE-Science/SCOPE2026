# A square-root shattering deficit in central Gaussian-binomial levels

## Finding

Let \(m\ge1\), let \(P_m=[m]\times[m]\) carry the coordinatewise order, and let \(\mathcal C_{m,k}\) be the Boolean membership concepts of lower ideals \(I\subseteq P_m\) of exactly \(k\) cells, for \(0\le k\le m^2\). For \(S\subseteq P_m\), put \(\downarrow S=\{x\in P_m:\exists s\in S,\ x\le s\}\) and \(\uparrow S=\{x\in P_m:\exists s\in S,\ x\ge s\}\). The following assertions hold.

**Preliminary rank-slice criterion (credited background, reproved for completeness).** A set \(S\) is shattered by \(\mathcal C_{m,k}\) if and only if \(S\) is an antichain and
\[
|\downarrow S|\le k\le m^2-|\uparrow S|.
\]
This is the specialization of an earlier general rank-selected lower-ideal criterion; it is not claimed new here. The new extremal assertion is the square-root deficit and its sharp central-band attainment.

**Square-root deficit theorem.** Set
\[
t_m=\left\lceil\frac{\sqrt{4m+1}-1}{2}\right\rceil,
\qquad d_m=m-t_m.
\]
Then **every** cardinality level satisfies \(\operatorname{VCdim}(\mathcal C_{m,k})\le d_m\), and the central Gaussian-binomial level attains equality:
\[
\boxed{\operatorname{VCdim}(\mathcal C_{m,\lfloor m^2/2\rfloor})=d_m.}
\]
More precisely, put \(B_m=d_m(2m-d_m+1)/2\). The equality \(\operatorname{VCdim}(\mathcal C_{m,k})=d_m\) holds for every integer \(k\) with \(B_m\le k\le m^2-B_m\). The interval is nonempty, and is an *attainment guarantee*, not a claim that all other levels have strictly smaller dimension. Thus restriction to a middle fixed-area layer reduces the unrestricted ideal-class VC dimension \(m\) by exactly \(t_m=\sqrt m+O(1)\).

## Assumptions and scope

An ideal here means any downward-closed subset, including the empty ideal; no directedness requirement is imposed. A concept is the indicator \(x\mapsto\mathbf 1_{x\in I}\), with the domain the \(m^2\) individual grid cells. A set \(S\) is shattered when every labeling \(T\subseteq S\) is the trace \(I\cap S\) of some ideal with exactly \(k\) cells. All parameters and inequalities above include their stated endpoints; when \(m=1\) the central class contains only the empty ideal and the dimension is zero.

## Proof

**1. Exact support criterion on any finite poset.** Let \(P\) be a finite poset of size \(N\), \(0\le k\le N\), and \(\mathcal J_k(P)\) its \(k\)-element lower ideals. If \(x<y\) are both queried, the labeling \(x\mapsto0,y\mapsto1\) is impossible. Hence every shattered support is an antichain. For an antichain \(S\), the all-positive labeling forces \(\downarrow S\) into its witnessing ideal, while the all-negative labeling forces the ideal to avoid \(\uparrow S\). Necessarily \(|\downarrow S|\le k\le N-|\uparrow S|\).

Conversely assume these two inequalities and choose any positives \(T\subseteq S\) and negatives \(S\setminus T\). Define the lower ideals
\[
L_T=\downarrow T,\qquad H_T=P\setminus\uparrow(S\setminus T).
\]
The antichain property implies \(L_T\subseteq H_T\): otherwise a negative point lies below a positive one. Also \(|L_T|\le|\downarrow S|\le k\) and \(|H_T|\ge N-|\uparrow S|\ge k\). Every finite interval of ideals \([L_T,H_T]\) contains an ideal of each intermediate cardinality: choose a linear extension of the induced poset on \(H_T\setminus L_T\) and adjoin its elements one at a time. Hence an ideal \(I\) of size exactly \(k\) can be chosen between \(L_T\) and \(H_T\). It contains exactly the queried positives \(T\) and no queried negatives. The claimed criterion follows, including \(S=\varnothing\).

**2. An obstruction from incomparable grid cells.** Let \(S\subseteq P_m\) be a shattered antichain of size \(s\). No two elements of \(S\) share a row or a column, because equal first or second coordinates make them comparable. Let \(F\) be the set of cells incomparable with **every** element of \(S\), i.e. the complement of \(\downarrow S\cup\uparrow S\). A cell in a selected row or selected column is comparable with a selected cell, so every point of \(F\) lies in one of the \(m-s\) unselected rows and one of the \(m-s\) unselected columns. Consequently
\[
|F|\le(m-s)^2.
\]
Also \(\downarrow S\cap\uparrow S=S\): if \(x\le a\) and \(b\le x\) for \(a,b\in S\), then \(b\le a\); antichainness forces \(a=b=x\). Inclusion–exclusion gives
\[
|\downarrow S|+|\uparrow S|=m^2-|F|+s.
\]
The support criterion yields \(|\downarrow S|+|\uparrow S|\le m^2\), so \(|F|\ge s\). Therefore
\[
\boxed{s\le(m-s)^2.}
\]
Writing \(t=m-s\), this is \(t(t+1)\ge m\). Hence \(s\le m-t_m=d_m\) for every cardinality level, proving the universal upper bound.

**3. An all-labeling construction at the central rank and its guaranteed band.** Let \(s=d_m\) and select the anti-diagonal prefix
\[
S_s=\{(i,m+1-i):1\le i\le s\}.
\]
It is an antichain. Its down-closure has row lengths \(m,m-1,\ldots,m-s+1\) followed by zeros, so
\[
|\downarrow S_s|=sm-\binom{s}{2}
=\frac{s(2m-s+1)}2=:B.
\]
Its up-closure has \(s\) consecutive row lengths \(1,2,\ldots,s\) followed by \(m-s\) rows of length \(s\). Thus \(|\uparrow S_s|=s(s+1)/2+(m-s)s=B\). The inequality \(s\le(m-s)^2\) rearranges to \(2B\le m^2\), which implies that \([B,m^2-B]\) contains the central integer \(\lfloor m^2/2\rfloor\). Applying the support criterion to \(S_s\), this \(s\)-point support is shattered at every level in that band. It reaches the universal bound, proving all assertions.

**4. Unrestricted comparison and asymptotic.** For the class of all lower ideals of \(P_m\), a support is shattered precisely when it is an antichain (apply the unrestricted versions of the preceding extension argument). The grid has width \(m\), witnessed by the whole anti-diagonal; any antichain has distinct rows, hence size at most \(m\). Its unrestricted VC dimension is exactly \(m\). Finally the displayed quadratic-root formula gives \(t_m=\sqrt m+O(1)\), completing the claimed deficit.

## Verification

The bundled standard-library Python program `verify.py` enumerates **all** lower ideals by weakly decreasing row lengths; directly derives every support trace from the concept masks; and compares trace shattering to the closure criterion for all ranks for \(1\le m\le5\), plus the central rank for \(m=6\). It also checks the explicit anti-diagonal closure sizes and computed central dimensions. The output `verify_output.txt` records a successful replay of 8,900 support–rank comparisons. Enumeration confirms finite instances only; the proof above establishes the infinite result.

## Relationship to prior work

A prior rank-slice result already establishes the general finite-poset antichain/two-closure criterion, including a complete treatment for unions of chains. That criterion is used and reproved here but **not** claimed as new. The square-grid extremal inequality and sharp central-rank square-root formula do not follow from its chain-union specialization. The 2019 study of function-class shatter complexes and intersection-closed families by Chen, Eur, Yang and Zhang supplies the structural learning-theory context, but a nontrivial fixed-cardinality level of lower ideals is generally **not** intersection-closed; its main theorems do not determine the VC dimension claimed here. Iams, Johnston and Muth (2020) study adaptive searches for unknown poset ideals under a bound on positive answers, with special results for product posets. Their search objective is not fixed-cardinality VC shattering; moreover their paper's finite-poset “ideals” are directed lower sets, not the arbitrary Ferrers diagrams considered here. Familiar Gaussian-binomial rank enumeration identifies the number of diagrams in each area level, but neither that count nor the full-class width theorem determines the square-root shattering deficit. Searches of nearby published results did not reveal a covering exact theorem; this is not a proof of absolute historical novelty.

## Limitations

The result gives an exact **central** VC dimension and a guaranteed band of ranks, not an all-rank formula for \(\operatorname{VCdim}(\mathcal C_{m,k})\), not the full shattering polynomial, and not a Littlestone dimension. A rank-level support can be shattered outside the guaranteed band. The finite checks are consistency tests, not substitutes for the all-order proof. Related inaccessible or unindexed work could affect historical priority. Independent mathematical validation has not been performed.

## References

1. J. Chen, C. Eur, G. Yang and M. Zhang, *Free resolutions of function classes via order complexes*, arXiv:1909.02159, first posted September 5, 2019; https://arxiv.org/abs/1909.02159 (especially Introduction and Section 2 on shatter complexes).
2. A. Iams, H. Johnston and R. Muth, *Searching for quicksand ideals in partially ordered sets*, arXiv:2009.07348, first posted September 15, 2020; https://arxiv.org/abs/2009.07348 (especially Sections 1–2 and the scope of Problem 1).
3. The Gaussian-binomial rank interpretation of partitions in rectangles is classical background; e.g. *The Gaussian coefficients*, MIT 18.212 lecture 10 (2021), https://math.mit.edu/~apost/courses/18.212_2021/lectures/18212_lecture10.pdf. This source is cited for background only, not for novelty.
