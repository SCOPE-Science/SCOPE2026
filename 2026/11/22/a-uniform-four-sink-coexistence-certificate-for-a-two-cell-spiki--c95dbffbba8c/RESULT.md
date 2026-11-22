# A uniform four-sink coexistence certificate for a two-cell spiking map

## Finding

For every real \(\alpha\ge 6\), the published two-cell map at Euler step \(T=1\),
\[
 F_\alpha(x,y)=\left(\tfrac{17}{10}\tanh(\alpha x)-\tanh(\alpha y)-\tfrac3{10},\;\tanh(\alpha x)+\tfrac{17}{10}\tanh(\alpha y)+\tfrac3{10}\right),
\]
has **at least nine distinct hyperbolic fixed points**. At least four of these are attracting sinks with disjoint nonempty open basins, at least four are saddles, and at least one is a repeller. The result holds simultaneously for every \(\alpha\) in the entire unbounded interval, including the endpoint \(\alpha=6\). It is a lower-bound theorem, not a claim that the complete fixed-point census is nine.

## Assumptions and scope

All states are real; \(\tanh\) has its usual real definition. All results concern the specified coefficients \((\mu,s,i_1,i_2)=(7/10,1,-3/10,3/10)\), exactly those used in the source model, and step \(T=1\). The fixed-point *locations* remain fixed points for every step \(T>0\), because the Euler equilibrium equations do not depend on \(T\); the stability types asserted here are for \(T=1\) only.

Put \(u=\tanh(\alpha x)\) and \(v=\tanh(\alpha y)\). A box specified using \(u\) or \(v\) is expressed in that transformed coordinate; the corresponding physical coordinate is \(x=\operatorname{artanh}(u)/\alpha\) or \(y=\operatorname{artanh}(v)/\alpha\). The following nine product boxes are nonempty and pairwise disjoint for every \(\alpha\ge6\):

| Label | First coordinate | Second coordinate | Type |
|---|---|---|---|
| \(C_{++}\) | \(x\in[0.34,0.45]\) | \(y\in[2.90,3.10]\) | sink |
| \(C_{+-}\) | \(x\in[2.30,2.50]\) | \(y\in[-0.45,-0.34]\) | sink |
| \(C_{-+}\) | \(x\in[-3.20,-2.80]\) | \(y\in[0.90,1.10]\) | sink |
| \(C_{--}\) | \(x\in[-1.20,-0.80]\) | \(y\in[-2.60,-2.20]\) | sink |
| \(X_+\) | \(u\in[0.70,0.94]\) | \(y\in[2.65,2.98]\) | saddle |
| \(X_-\) | \(u\in[-0.55,-0.35]\) | \(y\in[-2.00,-1.65]\) | saddle |
| \(Y_+\) | \(x\in[2.05,2.37]\) | \(v\in[-0.94,-0.70]\) | saddle |
| \(Y_-\) | \(x\in[-2.60,-2.34]\) | \(v\in[0.35,0.55]\) | saddle |
| \(Z\) | \(u\in[0,0.14]\) | \(v\in[-0.29,-0.13]\) | repeller |

## Proof

Write the fixed-point residual as
\[
 H_1=\tfrac{17}{10}u-v-\tfrac3{10}-x,\qquad
 H_2=u+\tfrac{17}{10}v+\tfrac3{10}-y.
\]
The sign of \(H_1\) is strictly constant on either first-coordinate face of each displayed box and strictly opposite on its other first-coordinate face. The analogous statement holds for \(H_2\) on its second-coordinate faces. The signs, in the order first lower/upper and second lower/upper, are
\[
\begin{array}{c|c}
C_{++},C_{+-},C_{-+},C_{--}&(+,-;+,-)\\
X_+,X_-&(-,+;+,-)\\
Y_+,Y_-&(+,-;-,+)\\
Z&(-,+;-,+).
\end{array}
\]
For example the critical positive lower first-coordinate face of \(C_{++}\) obeys \(H_1\ge 1.7(29/30)-1-0.3-0.34=1/300>0\). The critical upper first-coordinate face of \(X_+\) obeys \(H_1\ge1.7(0.94)-1-0.3-7/24>0\). All 36 face comparisons, using exact rational arithmetic and the bounds below, appear in the accompanying standalone checker. The Poincaré–Miranda theorem (allowing independent reversal of each component's signs) therefore supplies one zero of \((H_1,H_2)\) in the interior of each box.

These uniform face bounds require only
\[
\tanh(\alpha t)>29/30\quad(t\ge0.34),\qquad
\tanh(\alpha t)>999/1000\quad(t\ge0.90)
\]
and the analogous odd-symmetry bounds for negative arguments. Both follow for \(\alpha\ge6\) from \(e^{4.08}>59\) and \(e^{10.8}>1999\). For transformed coordinates the bounds are \(\operatorname{artanh}(t)<A\) for the pairs \((t,A)=(0.14,0.15),(0.29,0.30),(0.35,0.375),(0.55,0.625),(0.70,0.90),(0.94,1.75)\), using monotonicity and \(e^{2A}>(1+t)/(1-t)\). Each exponential comparison is certified from a positive Taylor partial sum, so it is an exact inequality, not a floating-point estimate.

To distinguish the nine roots, observe that a transformed coordinate of modulus at most \(0.94\) has physical modulus at most \(7/24<0.292\). The four corner boxes have at least one physical coordinate of modulus at least \(0.34\); the four mixed boxes have nonoverlapping ranges on their other, large, coordinate; and the central transformed ranges are disjoint from every mixed range. Direct comparison of the displayed endpoints handles the remaining overlaps. Thus the nine constructed zeros are different.

For stability at \(T=1\), the Jacobian is
\[
 J=W\operatorname{diag}(d_1,d_2),\quad
 W=\begin{pmatrix}1.7&-1\\1&1.7\end{pmatrix},\quad
 d_1=\alpha(1-u^2),\;d_2=\alpha(1-v^2).
\]
For every physical coordinate of modulus at least \(0.34\), \(d_i\le24/59\). For modulus at least \(0.90\), \(d_i\le24/1999\). This follows from \(\operatorname{sech}^2 z<4e^{-2|z|}\) and monotonicity of \(\alpha e^{-2\alpha t}\) on \(\alpha\ge6\). The four corner boxes each have one coordinate of modulus at least \(0.90\) and the other at least \(0.34\), so \(\lVert J\rVert_\infty\le1.7(24/59)+24/1999<1\); each corner fixed point is an attracting hyperbolic sink.

In each mixed box, one transformed coordinate has modulus at most \(0.94\), hence its corresponding diagonal factor \(d_{\rm active}\ge6(1-0.94^2)>0.698\), while the other physical coordinate has modulus at least \(1.65\) and \(d_{\rm tiny}\le24/1999\). Since
\[
\det(I-J)=1-1.7(d_1+d_2)+3.89d_1d_2<0,
\]
the two eigenvalues are real and lie on opposite sides of \(1\). Moreover \(\det J=3.89d_1d_2\le3.89(144/1999)<1\), by the decreasing bound \(4\alpha^2e^{-3.3\alpha}\le144e^{-19.8}<144/1999\). Both eigenvalues are positive, one below \(1\) and one above: each mixed fixed point is a hyperbolic saddle.

In the central box \(d_1,d_2\ge6(1-0.29^2)>5.49\). As \(\det W=3.89\),
\[
\lVert J^{-1}\rVert_\infty\le
\frac{2.7}{3.89\,6(1-0.29^2)}<1.
\]
Every eigenvalue of \(J\) therefore has modulus greater than \(1\), and the central fixed point is a hyperbolic repeller. Hyperbolic sinks have disjoint nonempty open attraction basins. This completes the proof for all real \(\alpha\ge6\).

## Verification

Run `python3 checker.py` without external dependencies. It executes the 36 rational face tests, six rational exponential-majorant tests, and the explicit rational uniform Jacobian inequalities. Recheck each cited analytic estimate from the positive exponential Taylor lower bound; the program does not substitute a finite gain sample for the universal proof. The enclosing rectangles and monotonicity arguments establish the continuum in \(\alpha\).

## Relationship to prior work

Buscarino, Famoso and Fortuna (2023), Sections 2–4 and Figures 4–6, give the exact fixed-point equations and numerical examples with one, three or five intersections for gains near \(1\)–\(1.8\), together with plotted stable-state regions. The certified simultaneous four-sink coexistence for every gain at least six is not established there. Jin and Gupta (1996) discuss general two-neuron upper-capacity bounds of nine equilibria and four stable equilibria, but give neither existence nor this explicit uniform gain threshold for the published asymmetric-coupling map. Duncan and collaborators (2021) derive a general qualitative steep-sigmoid/switching correspondence; its small-parameter existence is not an effective bound \(\alpha\ge6\), and its regular-switching assumptions also require care at shared thresholds. The novelty asserted here is the quantitative source-specific nine-witness, four-sink certificate, not the general principle of sigmoid multistability or an optimal capacity theorem.

## Limitations

The gain threshold six is a certified sufficient threshold, not claimed sharp. No upper bound on the total number of equilibria, complete bifurcation diagram, attraction-basin measure, or global dynamics is established. Hyperbolic type at other step sizes is not claimed. The source's plotted ranges are not a global theorem, and the present result does not establish that the article's figures are erroneous within their studied ranges. General classic feedback-network bounds and the possibility of equivalent unindexed prior quantitative results remain relevant to publication priority. 

## References

1. A. Buscarino, C. Famoso, L. Fortuna, “Bifurcations in a new two-cell spiking map: a numerical and experimental study,” *Nonlinear Dynamics* **111** (2023), 20361–20375, published online September 27, 2023. https://doi.org/10.1007/s11071-023-08897-7 . Open-access full text: https://www.iris.unict.it/bitstream/20.500.11769/596535/2/Bifurcations%20in%20a%20new%20two%20cell%20spiking%20map%20a%20numerical%20and%20experimental%20study.pdf .
2. L. Jin, M. M. Gupta, “Equilibrium Capacity of Analog Feedback Neural Networks,” *IEEE Transactions on Neural Networks* **7** (1996), 782–786. https://madangupta.com/pages/info/mmg/paper/RJ/RJ-092.pdf .
3. W. Duncan, T. Gedeon, H. Kokubu, K. Mischaikow, H. Oka, “Equilibria and Their Stability in Networks with Steep Sigmoidal Nonlinearities,” arXiv:2103.17184, first posted March 31, 2021. https://arxiv.org/abs/2103.17184 .
