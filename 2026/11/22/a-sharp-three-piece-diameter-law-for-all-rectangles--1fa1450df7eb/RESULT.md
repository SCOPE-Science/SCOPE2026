# A sharp three-piece diameter law for all rectangles

## Finding
Let \(R_\lambda=[0,\lambda]\times[0,1]\), where \(\lambda\ge1\). Among all partitions of \(R_\lambda\) into exactly three closed convex sets with pairwise disjoint interiors, let \(D_3(\lambda)\) be the least attainable value of the largest Euclidean diameter of a part. Then
\[
D_3(\lambda)^2=\begin{cases}
1+\dfrac{(\lambda^2-3/4)^2}{4\lambda^2},&1\le\lambda\le3/2,\\[5pt]
1+\dfrac{\lambda^2}{9},&\lambda\ge3/2.
\end{cases}
\]
Both branches are attained by partitions consisting of three rectangles and obtainable with two successive straight cuts. For \(1\le\lambda\le3/2\), an attaining partition is a full-height vertical strip of width \(u=(\lambda^2-3/4)/(2\lambda)\) and two equal-height rectangles of width \(\lambda-u\). For \(\lambda\ge3/2\), three equal-width full-height strips attain the minimum. The optimal value changes branch at exactly \(\lambda=3/2\). The theorem does not assert that these are the only optimal partitions.

## Assumptions and scope
Here a convex three-part partition means three nonempty compact convex subsets of the closed rectangle, covering it, whose interiors are pairwise disjoint. Boundaries may be shared. Diameter is \(\sup\{|x-y|:x,y\in K\}\) for Euclidean distance. We minimize the maximum of the three diameters, allowing arbitrary convex boundaries; our construction happens to use rectangles. Scaling gives the value for any rectangle whose shorter side is \(b>0\): multiply the displayed value by \(b\), with \(\lambda\) the longer-to-shorter aspect ratio.

## Proof
**1. Corner lemma.** Consider \(Q=[0,t]\times[0,s]\), with \(s,t>0\), partitioned into three closed convex parts with maximum diameter \(d\). Suppose one part \(C_0\) contains the two corners \((0,0),(0,s)\). Assume
\[
d\ge s,\quad \eta:=\sqrt{d^2-s^2}<t/2,\quad d<\sqrt{t^2+s^2/4}.
\]
Then one of the following lower bounds holds:
\[
\eta\ge t/3,\qquad\text{or}\qquad 2t\eta\ge t^2-3s^2/4.\tag{1}
\]
Indeed, convexity gives the whole left side in \(C_0\). Every point of \(C_0\) on the top or bottom side has horizontal coordinate at most \(\eta\), by measuring its distance from the opposite left corner. Furthermore, \(C_0\) cannot meet the right side: any point \((t,y)\) has distance at least \(\sqrt{t^2+s^2/4}\) from one of the two left corners. Let \(a,b\le\eta\) be the rightmost coordinates of \(C_0\) on the top and bottom sides, respectively.

The two right corners therefore belong to the other parts. If a part \(C_1\) contains *both* right corners, convexity forces the whole right side into \(C_1\). Its top and bottom traces begin no earlier than \(t-\eta\): each such trace-point must be within distance \(d\) from the opposite right corner. Because \(\eta<t/2\), the remaining part \(C_2\) must cover the gaps between \(C_0\) and \(C_1\) on both top and bottom sides. Thus \(C_2\) contains \((a,s)\) and some \((c,0)\) with \(c\ge t-\eta\). Consequently
\[
d^2\ge s^2+(t-2\eta)^2.
\]
Since \(d^2=s^2+\eta^2\) and \(t-2\eta>0\), this gives \(\eta\ge t/3\).

Otherwise the top and bottom right corners belong to distinct parts \(C_1\) and \(C_2\). There is a common right-side interface point \((t,z)\) with \(0\le z\le s\). The top endpoint \((a,s)\) of \(C_0\) must also belong to \(C_1\), not \(C_2\): its distance to \((t,0)\) exceeds \(d\), because \(a\le\eta<t/2\). Similarly \((b,0)\) belongs to \(C_2\). Thus
\[
d^2\ge(t-a)^2+(s-z)^2,\qquad d^2\ge(t-b)^2+z^2.
\]
Since \(a,b\le\eta\) and \(\max\{z^2,(s-z)^2\}\ge s^2/4\), we obtain \(d^2\ge(t-\eta)^2+s^2/4\). Substituting \(d^2=s^2+\eta^2\) gives the second inequality in (1). These two cases exhaust the possible right-corner allocations, including shared boundary points.

**2. Candidate and vertical-side lower bound.** Put
\[
F_v(\lambda)=1+\frac{(\lambda^2-3/4)^2}{4\lambda^2},\qquad
G_v(\lambda)=1+\frac{\lambda^2}{9}.
\]
The proposed squared optimum is \(H(\lambda)=\min\{F_v(\lambda),G_v(\lambda)\}\), since
\[
F_v-G_v=\frac{(2\lambda-3)(2\lambda+3)(20\lambda^2-9)}{576\lambda^2}.
\]
Suppose that a three-part convex partition has maximum diameter \(d<\sqrt{H(\lambda)}\). Some part contains at least two of the four rectangle corners, by pigeonhole. These cannot be diagonally opposite because \(\sqrt{H(\lambda)}<\sqrt{1+\lambda^2}\); therefore they are adjacent. Assume first they are the endpoints of a *vertical* side. We may reflect the rectangle to put the pair on the left. Necessarily \(d\ge1\), and with \(\eta=\sqrt{d^2-1}\), we have \(\eta<\lambda/2\) and \(d<\sqrt{\lambda^2+1/4}\). Both strict inequalities follow immediately from \(d^2<H(\lambda)\), since \(H(\lambda)\le G_v(\lambda)\) and the displayed expression for \(F_v\) on \(1\le\lambda\le3/2\). Applying the corner lemma with \(s=1,t=\lambda\), either \(d^2\ge G_v(\lambda)\) or \(d^2\ge F_v(\lambda)\), contradicting \(d^2<H(\lambda)\).

**3. Horizontal-side exclusion.** Suppose instead one part contains both corners of a *horizontal* side, length \(s=\lambda\). Then \(d\ge\lambda\). Set
\[
\lambda_0=\sqrt{\frac{5+2\sqrt{13}}{12}}=1.0087575919\ldots.
\]
The polynomial identity
\[
F_v(\lambda)-\lambda^2=-\frac{48\lambda^4-40\lambda^2-9}{64\lambda^2}
\]
shows that \(H(\lambda)<\lambda^2\) for \(\lambda>\lambda_0\), so this horizontal case is impossible there. For \(1\le\lambda\le\lambda_0\), we have \(H=F_v\), and if \(d^2<H\) with \(d\ge\lambda\), then
\[
0\le\eta^2:=d^2-\lambda^2< F_v(\lambda)-\lambda^2\le1/64.
\]
In particular \(\eta<1/2\), while \(d<\sqrt{1+\lambda^2/4}\), so the corner lemma applies with \(s=\lambda,t=1\). It yields either
\[
d^2\ge G_h(\lambda):=\lambda^2+1/9
\]
or
\[
d^2\ge F_h(\lambda):=\lambda^2+\frac{(1-3\lambda^2/4)^2}{4}.
\]
Both exceed or equal \(F_v(\lambda)\) on this range, as is certified by the identities
\[
F_h-F_v=\frac{3(\lambda-1)(\lambda+1)(3\lambda^4+11\lambda^2+3)}{64\lambda^2}\ge0,
\]
\[
G_h-F_v=\frac{432\lambda^4-296\lambda^2-81}{576\lambda^2}>0
\quad(\lambda\ge1).
\]
The latter numerator is increasing on \([1,\infty)\) and equals \(55\) at \(\lambda=1\). Again \(d^2<H\) is impossible. This proves the lower bound for all convex three-part partitions.

**4. Attainment.** For \(1\le\lambda\le3/2\), take the three rectangles
\[
[0,u]\times[0,1],\quad [u,\lambda]\times[0,1/2],\quad [u,\lambda]\times[1/2,1],
\qquad u=\frac{\lambda^2-3/4}{2\lambda}.
\]
The defining equation \(1+u^2=(\lambda-u)^2+1/4=F_v(\lambda)\) shows that all three have diameter \(\sqrt{H(\lambda)}\). For \(\lambda\ge3/2\), three full-height strips of width \(\lambda/3\) each have squared diameter \(G_v(\lambda)=H(\lambda)\). Both constructions are successive straight-cut divisions. The explicit factorization in Step 2 fixes the crossover at exactly \(3/2\). Thus the claimed minimum is attained in the unrestricted class of convex partitions.

## Verification
Run `python3 verify.py` alongside this file (SymPy 1.10 or later). It checks twelve rational/algebraic identities, the precise horizontal-case cutoff, representative rational points of each strict sign regime, and the construction equalities. The sign inequalities for continuous real ranges are proved by the factorizations and monotonicity arguments in Steps 2–3, **not** by finite sampling. An independent elementary check is obtained by evaluating each constructed rectangle's diameter from its side lengths. No assertion of uniqueness of optimizers is required.

## Relationship to prior work
The value at \(\lambda=1\) is \(D_3(1)=\sqrt{65}/8\), the 1958 Wenceslas–Lipman square result, as documented by Chaidee and Wichiramala (2016). Cañete, Fernández and Márquez (2023, Section 3.1) address the general convex-body min–max diameter problem and give bounds, but not this aspect-ratio profile. Disk-covering work by Heppes and Melissen (1997), and Fekete et al. (2023), concerns enclosing the rectangle in three *disks*, not partitioning it into convex pieces of small diameter. A set of diameter \(d\) need not fit in a disk of radius \(d/2\), so sharp three-disk covering bounds do not by themselves prove the convex-piece lower bound derived here. The present contribution is the full sharp value for every rectangle and its exact transition \(\lambda=3/2\), not the known square endpoint or an assertion about disk-covering optimality.

## Limitations
This theorem assumes exactly three planar convex parts; it does not address three arbitrary disconnected sets, unequal weights, or more than three pieces. The exhibited T and strip constructions need not be the sole optimal partitions. The near-square comparison with historical exact three-disk coverings creates a genuine priority-search risk, especially because the full 1997 paper was not accessible in this examination. The distinction between diameter-constrained partitions and disk covers is mathematical, not proof that no earlier author stated the same partition theorem. No independent mathematical audit has been carried out.

## References
1. A. Cañete, I. Fernández, A. Márquez, *Optimal divisions of a convex body*, arXiv:2311.13882v1 (first posted November 23, 2023), Section 3.1, https://arxiv.org/html/2311.13882v1.
2. S. Chaidee and W. Wichiramala, *Optimal partitioning of a square: a numerical approach*, ScienceAsia 42 (2016), 150–157, https://doi.org/10.2306/scienceasia1513-1874.2016.42.150 (earlier three-part square result attributed to Wenceslas and Lipman, 1958).
3. A. Heppes and H. Melissen, *Covering a Rectangle With Equal Circles*, Periodica Mathematica Hungarica 34 (1997), 65–81, https://doi.org/10.1023/A:1004224507766 (related covering problem; full text not inspected).
4. S. P. Fekete et al., *Worst-Case Optimal Covering of Rectangles by Disks*, Discrete & Computational Geometry, published online October 6, 2023, https://doi.org/10.1007/s00454-023-00582-1 (Section 5.1 and discussion of three-disk configurations).
