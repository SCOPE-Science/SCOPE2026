# Sharp complete-pair Gini heat contraction on the Petersen graph

## Finding

Let \(P\) be the Petersen graph, realized on the ten unordered pairs of \(\{0,1,2,3,4\}\), with adjacency when two pairs are disjoint. Let \(A\) be its adjacency matrix and \(H_t=\exp(t(A-3I))\), for real \(t\geq0\). For real vertex signals, put
\[
G(f)=\sum_{\{u,v\}\subset V(P)}|f(u)-f(v)|.
\]
Its sharp induced quotient-seminorm is, **for every** \(t\geq0\),
\[
\boxed{\gamma(t):=\sup_{G(f)>0}\frac{G(H_tf)}{G(f)}=
\frac{11e^{-2t}-2e^{-5t}}9.}
\]
Each singleton indicator, and its complement, attains equality for every \(t\). For \(t>0\), these are the only extremizers **among nontrivial binary cuts**. The classical Dobrushin/Hopf oscillation coefficient is instead
\[
\delta(t)=\frac{4e^{-2t}-e^{-5t}}3,
\qquad \delta(t)-\gamma(t)=\frac{e^{-2t}(1-e^{-3t})}9>0\quad(t>0).
\]
Thus the exact Gini contraction is strictly sharper than the Dobrushin oscillation bound at every positive time. In particular, \(\gamma'(0)=-4/3\) and \(\lim_{t\to\infty}e^{2t}\gamma(t)=11/9\).

## Assumptions and scope

The graph is the ten-state Petersen graph with unit rates along all three incident edges. The generator is \(A-3I\), not the degree-normalized generator. The signal space is \(\mathbb R^{10}\), considered modulo additive constants; the pairwise Gini seminorm counts unordered vertex pairs once, without extra normalization. Time includes \(t=0\). The result is an all-time exact operator-seminorm statement, not merely a bound for particular inputs or an asymptotic formula.

## Proof

**Step 1: coarea reduction.** Any nonconstant real signal can be translated so its smallest entry is zero. With \(S_u=\{i:f_i>u\}\), the layer-cake identity gives \(f=\int_0^\infty\mathbf 1_{S_u}\,du\) and \(G(f)=\int_0^\infty |S_u|(10-|S_u|)\,du\). Linearity and the triangle inequality give \(G(H_tf)\leq\int_0^\infty G(H_t\mathbf 1_{S_u})\,du\). Hence \(\gamma(t)\) is the maximum over the \(2^{10}-2=1022\) nontrivial binary cuts.

**Step 2: exact spectral decomposition.** Each row of \(A\) sums to three, and the Petersen common-neighbor counts give \(A^2=2I-A+J\), where \(J\) is the all-ones matrix. Thus \(A\) has eigenvalues \(3,1,-2\), and for any vertices \(i,j\) and any real vector \(x\),
\[
3\big((H_tx)_i-(H_tx)_j\big)
=e^{-2t}\big((Ax)_i-(Ax)_j+2(x_i-x_j)\big)
+e^{-5t}\big((x_i-x_j)-((Ax)_i-(Ax)_j)\big).
\]
For a cut indicator \(x=\mathbf 1_S\), set \(y=(A+2I)x\), \(z=(I-A)x\), and \(r=e^{-3t}\in[0,1]\). Then
\[
G(H_tx)=\frac{e^{-2t}}3G(y+rz),\qquad y+z=3x.
\]

**Step 3: an exact finite Petersen cut lemma.** For every nonempty proper \(S\),
\[
G((A+2I)\mathbf1_S)\leq\frac{11}{3}|S|(10-|S|),
\]
with equality precisely when \(|S|=1\) or \(|S|=9\). The complete exact cut calculation is the following size-by-size maximum of \(G((A+2I)\mathbf1_S)/[|S|(10-|S|)]\):

| \(|S|\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maximum | \(11/3\) | \(7/2\) | \(67/21\) | \(37/12\) | \(3\) | \(37/12\) | \(67/21\) | \(7/2\) | \(11/3\) |

This is a finite exhaustive certificate, not a sample of cuts: the complete, dependency-free `CHECKER.py` included with this result enumerates all 1022 nontrivial bitmasks of ten two-subsets, constructs each adjacency count from disjointness, and compares integer numerators exactly. It independently verifies the complete orbit partition into 32 classes under all 120 relabelings of the five ground points; the nine displayed maxima and strictness for sizes 2 through 8 follow from integer comparisons. For a singleton \(S=\{u\}\), \((A+2I)\mathbf1_S\) takes values \(2\) once, \(1\) three times, and \(0\) six times, so its Gini variation is exactly \(33=(11/3)\cdot9\). Complementation gives the nine-point equality case. A reader can reproduce the finite proof with `python3 CHECKER.py`; there is no external solver, database, or assumption about unexamined cuts.

**Step 4: all-time sharpness.** By convexity of \(G\), for any cut indicator,
\[
G(y+rz)\leq(1-r)G(y)+rG(y+z)
\leq\left[\frac{11}3(1-r)+3r\right]G(x),
\]
since \(y+z=3x\). Thus \(G(H_tx)/G(x)\leq e^{-2t}(11-2r)/9\). For singleton \(x\), the vector \(y+rz\) takes values \(2+r\) once, \(1-r\) at three neighbors and \(0\) at six nonneighbors, whose relative order remains unchanged for \(0\leq r\leq1\). Therefore the convex interpolation inequality is equality, establishing the sharp formula for all continuous \(t\ge0\). When \(t>0\), \(r<1\), so strictness of the finite cut lemma excludes every other binary cut.

**Step 5: oscillation comparison.** The heat kernel has diagonal entry \((1+5e^{-2t}+4e^{-5t})/10\), neighbor entry \((3+5e^{-2t}-8e^{-5t})/30\), and nonneighbor entry \((3-5e^{-2t}+2e^{-5t})/30\). The half-\(\ell^1\) distance of adjacent heat-kernel rows is \(e^{-2t}\), while that of nonadjacent rows is \((4e^{-2t}-e^{-5t})/3\); the latter is larger for \(t>0\). The standard Doeblin–Dobrushin formula therefore gives the displayed \(\delta(t)\) and strict difference. Differentiation and the long-time limit are immediate.

## Verification

Run `python3 CHECKER.py` with Python 3 standard library. It checks the exact strongly regular adjacency relation, enumerates every one of the 1022 nontrivial cuts, confirms the sharp endpoint lemma, verifies strictness away from the 20 singleton/complement cuts, checks all 32 relabeling-orbits, and tests convex interpolation at six rational parameters. The analytical spectral identity, convexity and equality argument cover the full continuous time range. Finite parameter tests are corroborating checks only, not evidence for an unproved continuum extrapolation.

## Relationship to prior work

Gaubert and Qu's 2013 preprint on Dobrushin's ergodicity coefficient develops the sharp Hopf oscillation (equivalently dual total-variation) contraction coefficient for stochastic operators, not the complete-pair Gini seminorm of vertex signals. Here the Dobrushin value is explicitly computed and is strictly larger at positive times, so that theorem alone does not imply this equality. Published related work on graph heat kernel positivity concerns numerical time-stepping rather than the exact Gini semigroup norm; published Petersen graph maximal-operator studies concern a different nonlinear operator and Hilbert norm. These comparisons support a specific gap but cannot establish absolute historical priority, especially against unindexed literature.

## Limitations

This theorem concerns only the unit-rate continuous-time Markov semigroup on the ten-vertex Petersen graph, real signals, and unweighted complete-pair Gini variation. It does not classify other strongly regular graphs, arbitrary weighted edges, degree-normalized time, or nonlinear graph filters. The exactness claim is mathematical and computer-assisted only for a fully enumerated ten-vertex lemma; no independent external audit or novelty certification has been obtained.

## References

1. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649 (first publicly posted 2013-07-17), especially introduction and Theorem 1.1. https://arxiv.org/abs/1307.4649
2. Related published mathematical record, *Sharp Gauss–Legendre heat-step positivity on strongly regular graphs*, published-finding corpus, 2026-11-08 (different time-stepping and positivity problem; complete text not accessed in this review).
3. Related published mathematical record, *Sharp Hilbert norm and rigidity of the centered maximal operator on the Petersen graph*, published-finding corpus, 2026-11-02 (different nonlinear operator and norm; complete text not accessed in this review).
