# Exact dyadic period spectrum and symplectic-area law for a fully periodic polygon pair

## Finding

For the square–rhombus symplectic billiard of Albers, Lander and Westermann [1, Example 2.29], the least period of **every regular phase point** is determined by the dyadic depths of its two edge parameters. The period spectrum is **exactly**
\[
\{4,12,20,28,\ldots\}=\{8k+4:k\in\mathbb Z_{\ge0}\}.
\]
Under normalized invariant symplectic area, the least period \(P\) obeys the exact distribution
\[
\boxed{\Pr(P=8k+4)=\frac{2k+1}{3\,2^{k+1}},\qquad k=0,1,\ldots .}
\]
In particular,
\[
\Pr(P>8k+4)=\frac{2k+5}{3\,2^{k+1}},\qquad
\mathbb EP=\frac{68}{3},\qquad
\mathbb E[e^{sP}]<\infty\iff s<\frac{\log2}{8}.
\]
The last two statements use the probability measure defined below; the pointwise classification does not depend on a measure. The exact law distinguishes the sizes of infinitely many period classes in an example previously known to have periodic points of unbounded periods.

## Assumptions and scope

Let \(S\) be the counterclockwise square with consecutive vertices
\[
(0,0),(4,0),(4,4),(0,4),
\]
and let \(R\) be the counterclockwise rhombus with consecutive vertices
\[
(6,5),(8,1),(12,-1),(10,3).
\]
These are precisely the polygons of [1, Example 2.29]. Denote the vertices in each list by \(S_i,R_j\), indices taken modulo four, and define directed edge vectors \(E_i=S_{i+1}-S_i\) and \(D_j=R_{j+1}-R_j\). The map \(\Phi\) sends \((x,y)\), with \(x\) on one polygon and \(y\) on the other, to \((y,z)\), where \(z\) is the second boundary intersection with the line through \(x\) parallel to the edge containing \(y\). We consider the regular invariant phase space on which these successive intersections are defined and never pass through polygon vertices. Its two orientations \(S\times R\) and \(R\times S\) alternate at each step.

For \((x,y)\in S\times R\), write \(x=S_i+sE_i\), \(y=R_j+tD_j\), with \(0<s,t<1\). Put
\[
 u=\begin{cases}s&i\text{ even},\\1-s&i\text{ odd},\end{cases}
\qquad
 v=\begin{cases}t&j\text{ even},\\1-t&j\text{ odd}.\end{cases}
\]
For any positive \(w\) not on a dyadic cut, let \(d(w)\) be the unique nonnegative integer satisfying
\[
2^{-d(w)-1}<w<2^{-d(w)}.
\]
In particular, the cut points \(2^{-m}\) for positive integers \(m\) and the endpoints are removed from the regular chart; all open dyadic cells are regular. Set \(m=d(u)\), \(n=d(v)\), and \(\varepsilon=(i+j)\bmod 2\). The pointwise formula is
\[
\boxed{\operatorname{per}_{\Phi}(x,y)=8(m+n+\varepsilon)+4.}
\]
The same period formula holds in the opposite orientation by applying the inverse of one iteration. For the probability law, normalize the invariant two-dimensional density \(\lvert\det(E_i,D_j)\rvert\,ds\,dt\) over the regular part of \(S\times R\). The equally weighted two-orientation extension has the same least-period law.

## Proof

**1. Exact two-step chart dynamics.** Write \(q(a)=a+(-1)^{a+1}\pmod4\) and \(h(a)=a+2\pmod4\). Thus \(q\) exchanges edge indices \(0\leftrightarrow3\) and \(1\leftrightarrow2\), whereas \(h\) takes the opposite edge. A direct line–edge intersection computation gives the following **exhaustive** table for \(\Phi^2:(i,j,u,v)\mapsto(i',j',u',v')\), with \(m=d(u)\), \(n=d(v)\):

| Case | New edge indices | New inward parameters |
| --- | --- | --- |
| \(\varepsilon=0,\ m>0\) | \((q(i),q(j))\) | \((2u,v/2)\) |
| \(\varepsilon=0,\ m=0,\ n>0\) | \((h(i),q(j))\) | \((3/2-u,2v)\) |
| \(\varepsilon=0,\ m=n=0\) | \((h(i),h(j))\) | \((3/2-u,3/2-v)\) |
| \(\varepsilon=1,\ n>0\) | \((q(i),q(j))\) | \((u/2,2v)\) |
| \(\varepsilon=1,\ n=0\) | \((q(i),h(j))\) | \((u/2,3/2-v)\) |

For completeness, this table can be derived without iterating numerical points: on each candidate target edge \(P_k+w(P_{k+1}-P_k)\), solve
\[
P_i+s(P_{i+1}-P_i)+\lambda D_j
=P_k+w(P_{k+1}-P_k).
\]
The intersections satisfying \(0<w<1\), excluding the starting point, specify the new edge. Repeating with the polygons interchanged gives the displayed affine formulas. Since each row is valid on its entire open cell (the only branch inequalities are \(m=0\), \(n=0\), or their complements), the five cases cover all sixteen ordered edge pairs and all regular open chart cells. The exact-rational script supplied with this result checks all sixteen edge pairs at every depth pair up to four, independently using polygon–line intersections.

**2. The periodic depth walk.** Let \(L=m+n+\varepsilon\). Every row of the table preserves \(L\). For \(L=0\), the unique depth state is \((m,n,\varepsilon)=(0,0,0)\). For \(L\ge1\), all depth states lie on the following single cycle of length \(r=2L+1\):
\[
 (L,0,0)\to(L-1,1,0)\to\cdots\to(0,L,0)
 \to(0,L-1,1)\to(1,L-2,1)\to\cdots\to(L-1,0,1)\to(L,0,0).
\]
Thus the depth state has least return time \(r=2L+1\) under \(\Phi^2\). This calculation uses *all* possible initial depth states, not merely a chosen representative.

**3. Edge antipodes and the affine reflection.** During one depth cycle, the first polygon's edge index undergoes \(2L\) applications of \(q\) and one application of \(h\); the second does too. Because \(q^2=h^2=\mathrm{id}\) and \(qh=hq\), each edge index becomes its antipode after exactly \(r\) two-step iterations.

For the representative state \((L,0,0)\), the parameter maps, for \(L\ge1\), are \(L\) steps of \((u,v)\mapsto(2u,v/2)\), one step of \((u,v)\mapsto(3/2-u,2v)\), then \(L-1\) steps of \((u,v)\mapsto(u/2,2v)\), and one step of \((u,v)\mapsto(u/2,3/2-v)\). Their composition is
\[
 (u,v)\longmapsto\left(\frac3{2^{L+1}}-u,\frac32-v\right).
\]
When \(L=0\), the third row of the table gives the identical formula. The other cells in the same depth cycle are carried to this representative by invertible affine branch maps; conjugating a central reflection by an affine map is again the central reflection on that cell. Consequently, after exactly \(r\) applications of \(\Phi^2\), **every** cell maps to its opposite-edge partner by the central reflection in both of its open dyadic intervals. On the next depth cycle, the two reflections and both edge antipodes cancel. Hence \(\Phi^{4r}\) is the identity on the whole cell.

No smaller positive return of \(\Phi^2\) is possible: its depth state cannot return before \(r\) steps, and at that time both edge indices are opposite, not equal. The least return of \(\Phi^2\) is therefore \(2r\). Since \(\Phi\) exchanges two disjoint polygon orientations, no odd iterate fixes a phase point, and the least return of \(\Phi\) is \(4r=8L+4\). Each nonnegative \(L\) occurs on an open cell; this gives the exact spectrum and proves that all such open-cell points avoid the vertex singularities. The missing dyadic cut lines are singular: successive affine doubling or halving takes any cut to a chart boundary corresponding to a vertex.

**4. Invariance and the probability law.** On an edge pair with tangent vectors \(E_i,D_j\), write the billiard map as \((s,t)\mapsto(t,s')\) and denote its new first-polygon edge vector by \(E_k\). The chord condition \(z-x\parallel D_j\), differentiated with respect to \(s\), yields
\[
\left|\frac{\partial s'}{\partial s}\right|
=\frac{\lvert\det(E_i,D_j)\rvert}{\lvert\det(D_j,E_k)\rvert}.
\]
Thus the absolute symplectic density \(\lvert\det(E_i,D_j)\rvert\,ds\,dt\) is invariant across orientations. In this polygon pair,
\[
\lvert\det(E_i,D_j)\rvert
=\begin{cases}16&i+j\text{ even},\\8&i+j\text{ odd}.\end{cases}
\]
There are eight ordered pairs of each parity, so the normalized parity variable \(B=\varepsilon\) has \(\Pr(B=0)=2/3\) and \(\Pr(B=1)=1/3\). Conditional on the edge pair, \(u,v\) are independent uniform points of \((0,1)\). Their dyadic depths \(G_1,G_2\) are therefore independent with \(\Pr(G_i=a)=2^{-a-1}\), and are independent of \(B\). The period formula becomes
\[
P=8(G_1+G_2+B)+4.
\]
For any \(k\ge0\), convolution gives
\[
\begin{aligned}
\Pr(G_1+G_2+B=k)
&=\frac23\frac{k+1}{2^{k+2}}+
 \frac13\mathbf1_{k\ge1}\frac{k}{2^{k+1}}\\
&=\frac{2k+1}{3\,2^{k+1}}.
\end{aligned}
\]
Summing the geometric-arithmetic series yields the claimed tail. The independent depth means equal one, giving \(\mathbb EP=4+8(1+1+1/3)=68/3\). The terms in the exponential-moment series are asymptotic to a positive constant times \(k\exp((8s-\log2)k)\); therefore convergence holds exactly when \(s<\log2/8\), including divergence at equality.

## Verification

The standalone file `CHECK.py`, executable with Python 3's standard library and no dependencies, reconstructs each geometric billiard step by exact rational line–segment intersections. It checks **800** distinct exact-rational two-step branch and primitive-period assertions over all sixteen edge pairs and twenty-five pairs of dyadic depths, verifies all sixteen determinant weights, and verifies twenty-five exact survival-mass identities. It prints `PASS` if all assertions hold. This finite checker is independent supporting evidence for the explicit general proof above, not an exhaustive proof over arbitrary real coordinates.

## Relationship to prior work

Albers, Lander and Westermann [1, Example 2.29] construct this very square–rhombus pair and establish that its regular billiard dynamics is fully periodic with unbounded periods. That essential prior fact is not claimed here as new. The present result determines the **least period at each regular phase point**, the exact allowed period spectrum, and the invariant-area period distribution including a sharp moment threshold. These quantitative statements and their dyadic partition were not identified in the inspected original text. Related work on polygonal symplectic billiards [2] treats other polygon configurations and periodicity phenomena. Existing quantitative results for a different square–kite/“necktie” polygon pair concern induced odometer return statistics on a one-dimensional fiber; they do not imply this two-dimensional square–rhombus period law.

## Limitations

This classification concerns only the stated square–rhombus pair and the regular billiard phase space; it makes no claim about vertex hits or other polygon pairs. The distribution uses **invariant symplectic area**, not equal weighting of the sixteen edge pairs or ordinary uniform arclength product. The proof of priority is necessarily limited to the primary literature and mathematically relevant records inspected; equivalent results in unindexed material remain possible. Independent verification has not been performed.

## References

[1] P. Albers, F. Lander, and J. M. Westermann, *Symplectic billiards for pairs of polygons*, first public arXiv submission 2024-02-19, arXiv:2402.12244, particularly Example 2.29. https://arxiv.org/abs/2402.12244 and https://arxiv.org/html/2402.12244.

[2] P. Albers, G. Banhatti, F. Sadlo, R. Schwartz, and S. Tabachnikov, *Polygonal symplectic billiards*, arXiv:1912.09404; Experimental Mathematics, published 2025. https://arxiv.org/abs/1912.09404.
