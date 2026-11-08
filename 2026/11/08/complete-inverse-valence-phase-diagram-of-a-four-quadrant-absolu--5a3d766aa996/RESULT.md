# Complete inverse-valence phase diagram of a four-quadrant absolute-value map

## Finding

Consider the continuous piecewise-affine planar map introduced by Tikjha,
\[
T_{a,c}(x,y)=(|x|+ay-1,\;x+c|y|-1),\qquad a>0,\ c>0.
\]
For every target \((X,Y)\in\mathbb R^2\), write \(U=X+1\), \(V=Y+1\), and define
\[
S=U+V,\quad D=V-U,\quad E=aV-cU,\quad R=aV+cU.
\]
Let \(N_{a,c}(X,Y)\) be the number of **distinct real preimages** of \((X,Y)\).
The complete classification, including all critical rays, is:

**Homeomorphic phase, \(0<c<a\).** Every target has exactly one preimage. The map is a globally orientation-reversing piecewise-affine homeomorphism of \(\mathbb R^2\).

**Folded phase, \(0<a<c\).** The image is the closed pointed cone
\[
T_{a,c}(\mathbb R^2)=\{(X,Y): S\ge0,\ R\ge0\}.
\]
Outside the cone there are no preimages. Inside the cone the complete valence is
\[
N_{a,c}(X,Y)=
\begin{cases}
1,&(U,V)=(0,0)\text{ or }(S=0\text{ or }R=0),\\
3,&S>0,\ R>0,\ (D=0\text{ or }E=0),\\
4,&S>0,\ R>0,\ D>0,\ E<0,\\
2,&S>0,\ R>0,\ DE\ne0\text{ and not }(D>0,E<0).
\end{cases}
\]
The two internal fold rays \(D=0\) and \(E=0\) each have exactly three inverse points away from the cone apex. In particular, an **open nonempty four-preimage sector** occurs exactly when \(c>a>0\). The oriented count of regular inverse branches inside the image is zero (and the proper map has topological degree zero).

**Collapsed phase, \(c=a>0\).** The image is the closed half-plane \(\{S\ge0\}\). There are no preimages for \(S<0\). For \(S>0\), the preimage is unique when \(D\ne0\), but has cardinality continuum when \(D=0\). Every point of the boundary line \(S=0\) has cardinality-continuum preimage. Thus the intermediate degeneracy is not merely a failure of a determinant test: its fibers change from one-dimensional continua on precisely two explicit critical sets to ordinary singleton fibers elsewhere in the image.

All assertions quantify over every positive real parameter pair and every target; none concerns only generic points.

## Assumptions and scope

The entire domain and codomain are \(\mathbb R^2\), with no bounded-domain or attracting-basin restriction. Parameters obey \(a,c>0\). The output shift by \((1,1)\) is a change of coordinates only; the claimed cardinalities are for the original map. The term preimage means a distinct point, not the number of formally valid quadrant formulas (which can double-count points on axes). The conclusion is about one-step inverse fibers, not periods or the number of backward trajectories of a prescribed infinite itinerary.

## Proof

Translate the output and write every input in its quadrant as \((x,y)=(\sigma p,\tau q)\), where \(p,q\ge0\) and \(\sigma,\tau\in\{-1,1\}\). The four image cones in the \((U,V)\)-plane are the nonnegative spans of the following rays:
\[
r_1=(1,1),\quad r_2=(1,-1),\quad r_3=(a,c),\quad r_4=(-a,c).
\]
Precisely, the images of quadrants one through four are
\[
Q_1:\operatorname{cone}(r_1,r_3),\quad
Q_2:\operatorname{cone}(r_2,r_3),\quad
Q_3:\operatorname{cone}(r_2,r_4),\quad
Q_4:\operatorname{cone}(r_1,r_4).
\]
The nonnegative preimage coordinates \((p,q)\) in the four quadrants solve the following systems:
\[
\begin{array}{c|c|c}
\text{quadrant}&(p,q)&\text{condition when }c\ne a\\\hline
1&( (-E)/(c-a),\ D/(c-a))&(-E)/(c-a)\ge0,\ D/(c-a)\ge0\\
2&( (-E)/(a+c),\ S/(a+c))&E\le0,\ S\ge0\\
3&( R/(c-a),\ S/(c-a))&R/(c-a)\ge0,\ S/(c-a)\ge0\\
4&( R/(a+c),\ D/(a+c))&R\ge0,\ D\ge0
\end{array}
\]
For example, in quadrant three \((x,y)=(-p,-q)\), so \((U,V)=(p-aq,-p+cq)\); hence \(S=(c-a)q\) and \(R=(c-a)p\). Direct substitution verifies all four rows. When \(c\ne a\), every candidate in a quadrant is unique, because all four determinants \(c-a,-(a+c),c-a,-(a+c)\) are nonzero.

For \(c<a\), the four ray angles in counterclockwise order are \(r_2,r_3,r_1,r_4,r_2\), with the final \(r_2\) interpreted one full turn later. Adjacent gaps are strictly between zero and \(\pi\). The quadrants' image cones occupy **exactly** these four disjoint angular sectors: \(Q_2,Q_1,Q_4,Q_3\), respectively. They cover the whole plane and meet only along the listed rays. Along any common ray, the two formulae are the same original axis preimage (by the displayed linear equations); at the origin all quadrant formulae yield the same origin. This proves existence and uniqueness everywhere, as well as continuity of the piecewise-affine inverse. All four determinant signs are negative, so the homeomorphism reverses orientation.

For \(c>a\), the ray angles instead obey \(r_2,r_1,r_3,r_4\), in counterclockwise order, with each adjacent gap below \(\pi\). Quadrant three spans exactly \(\{S\ge0,R\ge0\}\), the largest cone, so this is the entire image. In the three successive open angular sectors between \(r_2,r_1,r_3,r_4\), the active quadrant sets are, respectively, \(\{2,3\}\), \(\{1,2,3,4\}\), and \(\{3,4\}\). These give multiplicities two, four, two. The middle sector is characterized by \(D>0,E<0\). On \(r_1\), quadrants one and four share the same preimage on the positive \(x\)-axis, while the other two branches are distinct; on \(r_3\), quadrants one and two share a positive \(y\)-axis preimage, while the other two are distinct. The boundary rays \(r_2,r_4\) have one preimage each because the adjoining quadrant formulas coincide on their shared axis. The apex has exactly one. This establishes every boundary and interior case. The signs of the determinants in the two-preimage sectors are opposite, and in the four-preimage sector are two positive and two negative. Thus every regular value has oriented inverse count zero. As the origin is the only preimage of the translated origin and the map is homogeneous after translation, the map is proper, proving the topological-degree statement.

Finally let \(c=a\). Quadrants two and four have nonsingular images forming respectively the two sectors \(S\ge0,D\le0\) and \(S\ge0,D\ge0\). Quadrant one collapses onto the positive diagonal ray \(U=V\ge0\), with \(x+ay=U\), \(x,y\ge0\); its preimage is an entire segment if \(U>0\). Quadrant three collapses onto the full line \(S=0\), since \(U=p-aq\), \(V=-U\) for \(p,q\ge0\); every fixed \(U\in\mathbb R\) admits a half-line of such pairs. These are the only collapsed images. Away from them, exactly one nonsingular sector contributes, establishing the complete singular classification.

The sharpness assertions follow: for \(0<c<a\) all fibers have cardinality one, for \(c=a\) some fibers are infinite, and for \(0<a<c\) open sectors contain four distinct preimages. For instance, at \((a,c)=(1,2)\), the target \((X,Y)=(2,3)\) has precisely the four inverse points \((2,1),(-2/3,7/3),(-10,-7),(10/3,-1/3)\), checked by direct substitution.

## Verification

Run the standalone standard-library script `verify.py` with Python 3. It solves all four quadrant linear systems over rational numbers, rejects candidates outside their quadrants, merges duplicate axis preimages, and compares the observed count against the analytical piecewise formula. It checks eight rational parameter pairs, an integer grid of targets, all four critical rays, and explicit families of arbitrarily many distinct preimages at the degenerate parameter. The resulting output is `VERIFY_OK checks=11617`. This finite check supports but does not replace the all-real-parameter proof above.

## Relationship to prior work

Tikjha, arXiv:2607.13519v1, introduces the exact four-quadrant map, develops fixed-point and low-period bifurcations, and notes the rank collapse on \(c=a\) and \(c=-a\). Its full accessible text, including its degenerate-case section and appendix, does not give the complete inverse-valence function or the four-preimage sector.

Gardini and Tikjha (2020) give an invertibility transition and a zero/one/infinite-versus-zero/two classification **for a different two-partition map**, \((|x|-ay,x-cy+1)\). It does not imply the four-preimage sector for the present map. General global inverse criteria for at most four convex pieces, including Poggiolini and Spadini (2013, 2018), account for the homeomorphism subcase; that subcase is not claimed to be a new general inverse-function theorem. The evaluated contribution is the complete object-specific phase diagram including every target, the two- and four-fold regions, exact ray valences, and degenerate infinite-fiber sets.

## Limitations

The result applies to \(a,c>0\) only; parameters of mixed or negative signs can have different arrangements of the four image rays. It does not prove existence of new attractors, stability of cycles, entropy estimates, or higher-iterate inverse counts. The relation to the general nonsmooth inversion literature leaves a historical-priority risk for the complete special-case multiplicity table, even though no directly covering result was located among the sources inspected.

## References

1. W. Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map* (preprint version *Multistability and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*), arXiv:2607.13519v1, first public 2026-07-15. https://arxiv.org/abs/2607.13519
2. L. Gardini and W. Tikjha, *Dynamics in the transition case invertible/non-invertible in a 2D Piecewise Linear Map*, Chaos, Solitons & Fractals 137 (2020), 109813, https://doi.org/10.1016/j.chaos.2020.109813.
3. L. Poggiolini and M. Spadini, *Local inversion of planar maps with nice nondifferentiability structure*, Advanced Nonlinear Studies 13 (2013), 411–430, https://doi.org/10.1515/ans-2013-0209.
4. L. Poggiolini and M. Spadini, *Local inversion of a class of piecewise regular maps*, Communications on Pure and Applied Analysis 17 (2018), 2207–2224, https://doi.org/10.3934/cpaa.2018105.
