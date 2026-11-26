# A sharp three-piece diameter law for all rectangles

## Finding and scope

For \(\lambda\ge1\), let \(D_3(\lambda)\) be the least possible maximum Euclidean diameter in a partition of \([0,\lambda]\times[0,1]\) into exactly three nonempty compact convex sets with pairwise disjoint interiors. The pieces may share boundary points. Then
\[
D_3(\lambda)^2=\begin{cases}
1+\dfrac{(\lambda^2-3/4)^2}{4\lambda^2}, & 1\le\lambda\le3/2,\\[4pt]
1+\dfrac{\lambda^2}{9}, & \lambda\ge3/2.
\end{cases}
\]
For a rectangle with shorter side \(b>0\) and aspect ratio \(\lambda\), the optimum diameter is \(bD_3(\lambda)\); its square is \(b^2D_3(\lambda)^2\). A T-shaped arrangement of three rectangles attains the first branch; three equal-width strips attain the second. Both are obtainable with two successive straight cuts. The theorem does not characterize all optimizers.

## Proof

**Corner lemma.** Cover \(Q=[0,t]\times[0,s]\) with three compact sets of diameter at most \(d\), one of which, \(C_0\), contains both left corners. Suppose \(d\ge s\), \(\eta=\sqrt{d^2-s^2}<t/2\), and \(d<\sqrt{t^2+s^2/4}\). Then
\[
\eta\ge t/3\qquad\text{or}\qquad 2t\eta\ge t^2-3s^2/4.
\]
Indeed, each point of \(C_0\) on a horizontal side has horizontal coordinate at most \(\eta\), by its distance to the opposite left corner. Denote the rightmost horizontal coordinates of the top and bottom traces of \(C_0\) by \(a,b\), respectively. The set \(C_0\) cannot touch the right side: for each point there at least one left corner is at distance \(\sqrt{t^2+s^2/4}\) or greater.

If another piece \(C_1\) contains both right corners, its top and bottom traces lie in \(x\ge t-\eta\). The remaining piece covers the interval between \(a\) and the leftmost top coordinate of \(C_1\), and the analogous interval on the bottom. By closedness it contains \((a,s)\) and some \((c,0)\) with \(c\ge t-\eta\). Hence \(d^2\ge s^2+(t-2\eta)^2\), which gives \(\eta\ge t/3\).

Otherwise the right corners are in distinct pieces, say \((t,s)\in C_1\) and \((t,0)\in C_2\). The two closed traces cover the right side, so share some \((t,z)\). At \((a,s)\) the distance to \((t,0)\) exceeds \(d\), since \(t-a\ge t-\eta>\eta\). This exclusion persists just to the right of \((a,s)\); those points are also outside \(C_0\), so they lie in \(C_1\). Closedness gives \((a,s)\in C_1\); similarly \((b,0)\in C_2\). Thus
\[
d^2\ge \max\{(t-a)^2+(s-z)^2,\ (t-b)^2+z^2\}\ge (t-\eta)^2+s^2/4.
\]
Substitute \(d^2=s^2+\eta^2\) to obtain the second bound. The two cases cover all allocations of the right corners, even with shared boundary points.

**Lower bound.** Write
\[
F_v=1+\frac{(\lambda^2-3/4)^2}{4\lambda^2},\qquad G_v=1+\lambda^2/9,\qquad H=\min(F_v,G_v).
\]
Since
\[
F_v-G_v=\frac{(2\lambda-3)(2\lambda+3)(20\lambda^2-9)}{576\lambda^2},
\]
\(H\) has the stated two branches. Suppose a partition has maximum diameter \(d<\sqrt H\). Some piece contains two rectangle corners, by pigeonhole; they cannot be diagonally opposite because \(H\le G_v<1+\lambda^2\).

For corners on a vertical side, orient them on the left and apply the lemma with \(s=1,t=\lambda\). Here \(d\ge1\), \(\eta^2=d^2-1<\lambda^2/9\), and \(d^2<G_v<\lambda^2+1/4\) for \(\lambda\ge1\). The two bounds of the lemma yield respectively \(d^2\ge G_v\) or \(d^2\ge F_v\), the latter since \(\lambda^2-3/4>0\). Both contradict \(d^2<H\).

For corners on a horizontal side \(d\ge\lambda\). Put \(\lambda_0=\sqrt{(5+2\sqrt{13})/12}\). The identity
\[
F_v-\lambda^2=-\frac{48\lambda^4-40\lambda^2-9}{64\lambda^2}
\]
and \(H\le F_v\) rule out this case for \(\lambda>\lambda_0\). For \(1\le\lambda\le\lambda_0<3/2\) one has \(H=F_v\) and \(\eta^2=d^2-\lambda^2<F_v-\lambda^2\le1/64\); the last difference decreases on \([1,\infty)\). Also \(d^2<F_v<1+\lambda^2/4\) because \(F_v-(1+\lambda^2/4)=-3/8+9/(64\lambda^2)<0\). Apply the lemma with \(s=\lambda,t=1\). Since \(1-3\lambda^2/4>0\) in this range, it gives one of
\[
G_h=\lambda^2+1/9\le d^2,\qquad F_h=\lambda^2+\frac{(1-3\lambda^2/4)^2}{4}\le d^2.
\]
Both are at least \(F_v\) there, by
\[
 F_h-F_v=\frac{3(\lambda-1)(\lambda+1)(3\lambda^4+11\lambda^2+3)}{64\lambda^2},\qquad
 G_h-F_v=\frac{432\lambda^4-296\lambda^2-81}{576\lambda^2}>0.
\]
The last numerator is positive at 1 and increasing on \([1,\infty)\). This completes the lower bound. The argument does not require convexity beyond the stated compact partition setting; in particular the right-side interface follows from closedness, not any assumption on how the pieces were cut.

**Attainment.** For \(\lambda\le3/2\), take a vertical strip of width \(u=(\lambda^2-3/4)/(2\lambda)\), where \(0<u<\lambda\), then bisect the remaining strip horizontally. The three squared diameters are \(1+u^2=(\lambda-u)^2+1/4=F_v\). For \(\lambda\ge3/2\) take three full-height strips of width \(\lambda/3\), giving squared diameter \(G_v\). They agree at \(\lambda=3/2\).

## Verification

The accompanying `verify.py` (Python 3, SymPy 1.10 or later) checks the rational identities, the horizontal-case cutoff, sample signs and construction diameters. The geometric lower bound and continuous sign arguments above are the proof, not the finite sample tests.

## Relationship to prior work and limitations

The square value \(\sqrt{65}/8\) and its T partition are classical (Wenceslas–Lipman, 1958, as reported by Chaidee–Wichiramala). Cañete–Fernández–Márquez treat successive-cut divisions and give general bounds, including a grid construction that yields the strip upper bound here. Fekete et al., Lemmas 3.2 and 5.1 and Figures 2 and 24, give the same T construction and the corresponding expression \(F_v/4\) for squared radius in their three-equal-disks configuration, with a disk lower bound near the square. Their argument also uses the corner allocation but exploits disk placement and circular intersections. A diameter-\(d\) convex set need not fit in a disk of radius \(d/2\); the disk lower bound is therefore not the required lower bound for arbitrary convex pieces. The distinct claim here is the all-rectangle sharp diameter law in the partition class, including exact lower bounds and the crossover at \(3/2\), not priority for the T construction or its diameter expression. This comparison does not rule out earlier equivalent work, particularly in inaccessible parts of the equal-disk literature. No uniqueness, higher-piece-count, or higher-dimensional result is asserted.

## References

1. A. Cañete, I. Fernández, A. Márquez, *Optimal divisions of a convex body*, [arXiv:2311.13882v1](https://arxiv.org/html/2311.13882v1), §2 and §3.1.
2. S. Chaidee and W. Wichiramala, *Optimal partitioning of a square: a numerical approach*, ScienceAsia 42 (2016), 150–157, [DOI 10.2306/scienceasia1513-1874.2016.42.150](https://doi.org/10.2306/scienceasia1513-1874.2016.42.150).
3. A. Heppes and H. Melissen, *Covering a Rectangle With Equal Circles*, Periodica Mathematica Hungarica 34 (1997), 65–81, [DOI 10.1023/A:1004224507766](https://doi.org/10.1023/A:1004224507766) (full text not inspected).
4. S. P. Fekete et al., *Worst-Case Optimal Covering of Rectangles by Disks*, Discrete & Computational Geometry 72 (2024), 1232–1283, [DOI 10.1007/s00454-023-00582-1](https://doi.org/10.1007/s00454-023-00582-1), §3.1 and §5.1.
