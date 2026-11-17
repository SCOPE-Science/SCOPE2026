# Universal dihedral-angle spectra and Gaussian ridge law for generalized parking-function polytopes

## Finding
Let \(n\ge3\), let \(\mathbf b=(b_1,\ldots,b_n)\in\mathbb Z_{>0}^n\), and let \(P_n(\mathbf b)\subset\mathbb R^n\) be the convex hull of all generalized parking functions. In the standard coordinate Euclidean metric, its **entire multiset of interior ridge dihedral angles is independent of \(b_2,\ldots,b_n\)**, and depends on \(b_1\) only through the dichotomy \(b_1=1\) versus \(b_1>1\). This is an assertion about actual Euclidean angles, not merely the common combinatorial type.

Write \(\mathcal K=\{1,\ldots,n\}\) for \(b_1>1\), and \(\mathcal K=\{1,\ldots,n-2,n\}\) for \(b_1=1\). For a multiset \(\mathscr A_n(\mathbf b)\), write \(m\,\delta_\alpha\) for an angle \(\alpha\) of multiplicity \(m\). Then

\[
\boxed{\displaystyle
\mathscr A_n(\mathbf b)=
\sum_{\substack{s<t\\s,t\in\mathcal K}}
\binom nt\binom ts\,
\delta_{\pi-\arccos\sqrt{s/t}}
+R_n\,\delta_{\pi/2}
+A_n\,\delta_{\arccos(1/\sqrt n)}.}
\]

For \(b_1>1\), \(R_n=n(2^{n-1}-1)+\binom n2\) and \(A_n=0\). For \(b_1=1\), \(R_n=n(2^{n-1}-2)+\binom n2\) and \(A_n=n\). Angles with coinciding numerical values across several \((s,t)\) are added as a multiset. Thus the classical-type family has exactly \(n\) acute ridges, while the stellohedral-type family has none; every other non-right angle is obtuse.

The number of ridges with nested upper facets is
\[
N_n=\begin{cases}
3^n-2^{n+1}+1,&b_1>1,\\
3^n-2^{n+1}+1-n(2^{n-1}-1),&b_1=1.
\end{cases}
\]
In particular, if \(\Theta_n\) is the interior dihedral angle of a uniformly selected ridge of \(P_n(\mathbf b)\), for **any sequence** of positive-integer parameter vectors \(\mathbf b=\mathbf b^{(n)}\), then
\[
\boxed{\displaystyle
\Theta_n\xrightarrow{\mathsf P}\frac{3\pi}{4},\qquad
\sqrt n\left(\Theta_n-\frac{3\pi}{4}\right)
\xrightarrow{\mathrm d}N\!\left(0,\frac38\right).}
\]
The probability that the ridge belongs to the nested-upper class is \(1-O(n(2/3)^n)\), uniformly over both parameter regimes. The variance \(3/8\) is expressed in squared radians.

## Assumptions and scope
A generalized \(\mathbf b\)-parking function is a positive integer vector whose weakly increasing rearrangement \(\beta'_1\le\cdots\le\beta'_n\) satisfies \(\beta'_j\le B_j:=\sum_{i=1}^jb_i\). The polytope is the convex hull of these vectors in the **unscaled ambient standard Euclidean metric**. A ridge means a codimension-two face; its *interior* angle is the supplement of the angle between its incident outward unit facet normals. Every \(P_n(\mathbf b)\) is full-dimensional and simple for the asserted range, and hence each ridge lies in exactly two facets. The theorem includes unrestricted variation of all \(b_i\) with \(n\), including the transition between \(b_1=1\) and \(b_1>1\).

## Proof
The published minimal facet description gives lower facets \(L_i=\{x_i=1\}\), with outward normals \(-e_i\), and upper facets \(U_S=\{\sum_{i\in S}x_i=\sum_{j=n-|S|+1}^{n} B_j\}\), with outward normals \(\mathbf1_S\), for precisely the nonempty \(S\subseteq[n]\) whose sizes belong to \(\mathcal K\). The published vertex description is given by coordinate permutations of \((1,\ldots,1,B_{k+1},\ldots,B_n)\); the upper bounds are strictly increasing, except that \(B_1=1\) merges the \(k=0\) and \(k=1\) layers. Both descriptions are valid for arbitrary positive \(\mathbf b\) [Bayer et al., 2024].

At a vertex of a nonmerged layer the tight upper facets are exactly the nonempty prefixes of the ordered set of coordinates with values greater than one, while the remaining coordinates are tight lower facets. Hence \(U_S\cap U_T\) is a ridge exactly if \(S\subsetneq T\) or \(T\subsetneq S\), and two distinct lower facets always meet along a ridge. An upper facet \(U_S\) and lower facet \(L_i\) meet along a ridge precisely when \(i\notin S\), **with one exception**: if \(b_1=1\), \(U_{[n]}\) and \(L_i\) meet at the merged top vertex layer, for every \(i\). To see sufficiency rather than merely compatibility, order the coordinates of \(S\), extend this ordering through \(T\), and use the corresponding published vertex; likewise choose a lower-coordinate set disjoint from \(S\). Since the polytope is simple, any two distinct facets sharing a vertex meet in a ridge. Necessity follows from the complete list of tight facets at each vertex. The exceptional \(b_1=1\) case is forced by \(B_1=1\) and the full-sum upper inequality. This also proves there are no omitted ridge classes.

For \(S\subsetneq T\), the cosine of the angle between outward normals is
\[
\frac{\langle\mathbf1_S,\mathbf1_T\rangle}{\sqrt{|S||T|}}=\sqrt{|S|/|T|}.
\]
Thus its interior angle is \(\pi-\arccos\sqrt{|S|/|T|}\). Disjoint upper/lower pairs and lower/lower pairs have perpendicular outward normals, and therefore interior angle \(\pi/2\). Only the exceptional full-upper/lower pairs have outward-normal cosine \(-1/\sqrt n\), and hence interior angle \(\arccos(1/\sqrt n)\). These calculations produce precisely the advertised three angle classes and show complete independence from the values of the parking bounds beyond \(b_1=1\).

For fixed \(s<t\), select \(T\) and then \(S\subset T\); there are \(\binom nt\binom ts\) nested ordered pairs of upper facets. Each choice gives one ridge. In the full stellohedral case, partition each coordinate into \(S\), \(T\setminus S\), or \([n]\setminus T\). Of the \(3^n\) assignments, exclude the two events \(S=\varnothing\) and \(T\setminus S=\varnothing\) by inclusion-exclusion, giving \(3^n-2^{n+1}+1\) nested pairs. In the classical case, remove \(n\) unavailable \((n-1)\)-subsets: they occur as \(T\) in \(n(2^{n-1}-2)\) nested pairs, and as \(S\) in exactly \(n\) more pairs. This removes \(n(2^{n-1}-1)\) pairs. For upper/lower pairs, \(\sum_{\varnothing\ne S\subseteq[n]}(n-|S|)=n(2^{n-1}-1)\). In the classical case deleting size-\(n-1\) upper facets removes \(n\) right angles, while the exceptional full-upper/lower incidences add exactly \(n\) acute angles. Finally there are \(\binom n2\) lower/lower ridges. This completes all multiplicity formulas.

For the limit theorem, uniformly selecting a nested-upper ridge is asymptotically equivalent in total variation to assigning each coordinate independently and equiprobably to one of three bins \(S\), \(T\setminus S\), \([n]\setminus T\). The forbidden empty-bin and \(n-1\)-subset events have probability \(O(n(2/3)^n)\), and right/acute ridges also comprise an \(O(n(2/3)^n)\) fraction. Let \(X_n=|S|/n\) and \(Y_n=|T\setminus S|/n\). A bivariate multinomial central limit theorem and the delta method for \(r=X_n/(X_n+Y_n)\) give
\[
\sqrt n(r-1/2)\xrightarrow{\mathrm d}N(0,3/8),
\]
since the gradient at \((1/3,1/3)\) is \((3/4,-3/4)\), and a single coordinate's bin-indicator difference has variance \(2/3\). The angle map \(r\mapsto\pi-\arccos\sqrt r\) has derivative \(1\) at \(r=1/2\), giving the claimed \(3\pi/4\) center and variance \(3/8\) by a second delta method. This proof is uniform over all admissible parameter sequences.

## Verification
The accompanying `verify_angles.py` independently generates vertices from cumulative parking bounds and supporting facet equations, detects ridges by computing the **affine rank** of common active vertices, and recomputes interior angles from normal dot products. It checks 18 general parameter vectors in dimensions \(3,4,5\), including nonconstant \(b_2,\ldots,b_n\) and both first-parameter regimes. All comparisons match the formulas. Execute with Python 3 and NumPy using `python verify_angles.py`. The script's exact incidence tests use integral vertices and active equalities, while its affine-rank and angle comparisons use floating-point linear algebra; the infinite theorem is proved analytically above.

## Relationship to prior work
Hanada, Lentfer and Vindas-Meléndez first developed the geometric theory and facet inequalities for the two-parameter family [2022]. Bayer et al. established the complete arbitrary-parameter vertex, facet and nested-set face descriptions [2024]. Those are indispensable inputs to the present proof, and neither their combinatorial classification nor their inequality descriptions are claimed as new. They do not state the Euclidean angle multiset, the classical-type acute-ridge exception as a metric phenomenon, parameter-uniform angle rigidity, or the uniformly selected ridge's Gaussian limit. Prior work on geometric radii, widths, and Gaussian *vertex normal cones* concerns different invariants; Euclidean ridge dihedral angles are calculated here from facet incidence and outward normals.

## Limitations
This is a result for the **standard Euclidean coordinate realization**, not for arbitrary affine images or alternate stellohedral realizations. Only interior ridge dihedral angles are classified; ridge volumes and volume-weighted angle distributions are not. The Gaussian limit is for ridges chosen uniformly by count, not by their Euclidean areas. The facet and face descriptions are previously known, and any historical priority claim for the derived metric distribution remains provisional pending independent literature review. No independent mathematical audit has been performed.

## References
1. M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, preprint first posted December 13, 2022, arXiv:2212.06885; Annals of Combinatorics (2024). https://arxiv.org/abs/2212.06885
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, preprint first posted March 12, 2024, arXiv:2403.07387, Theorems 2.3 and 3.12; Discrete & Computational Geometry (online 2025). https://arxiv.org/abs/2403.07387
3. Classical multinomial central limit theorem and multivariate delta method, used in their standard probabilistic forms.
