# Sharp injectivity-to-fold transition in risk-sensitive population learning

## Finding
Consider the two-dimensional risk-sensitive multiplicative-weights update with a linearly refreshed risk belief,
\[
 F(x,q)=\left(\frac{x}{x+(1-x)\exp(a(x-b+cq))},\ (1-k)q+k(p_0+p_1x)\right).
\]
Fix \(a,c>0\), \(0<b<1\), \(p_0\ge0\), \(p_1>0\), \(p_0+p_1\le1\), and \(0<k\le1\). Write \(I=(p_0,p_0+p_1)\). Both \((0,1)^2\) and the physical band \(D=(0,1)\times I\) are invariant in the sense that their points map into the same domains.

**Theorem (sharp physical folding boundary).** The map is injective on each of these two domains if and only if
\[
 k\ge\frac1{1+cp_1}\quad\text{or}\quad
 \left(0<k<\frac1{1+cp_1}\ \text{and}\ a\le a_c\right),
 \qquad a_c=\frac{4(1-k)}{1-k(1+cp_1)}.
\]
In the open regime \(0<k<1/(1+cp_1)\), the following sharper assertions hold.

1. For \(a<a_c\), the map is a smooth orientation-preserving diffeomorphism onto its image. At \(a=a_c\), it is still a continuous one-to-one embedding but its Jacobian vanishes along \(x=1/2\); transverse inverse displacement scales with the cube root of target displacement, so local inverse Hölder exponent \(1/3\) is optimal.
2. For \(a>a_c\), the Jacobian vanishes exactly on the two nondegenerate fold lines
\[
 x=x_\pm:=\frac{1\pm\sqrt{1-4(1-k)/(a[1-k(1+cp_1)])}}2.
\]
The determinant is negative between the lines and positive outside. Every target has at most three preimages from either domain, while some targets have at least two preimages from \(D\).
3. Keeping all parameters other than \(a\) fixed, for every sufficiently small \(\eta>0\) with \(a=a_c(1+\eta)\), there is a target having exactly three distinct preimages from \(D\).

These are statements about one-step map geometry. They do not assert that folding is necessary or sufficient for chaos.

## Assumptions and scope
The first coordinate is a population fraction \(x\in(0,1)\). The belief coordinate is \(q\in(0,1)\), with its natural forward-invariant risk interval \(I\). The strict assumption \(p_1>0\) matters: it makes instantaneous belief updating at \(k=1\) information-preserving. Neither zero population nor endpoint belief values are needed for the theorem. The result concerns the given exact discrete map, not a small-step approximation or a stochastic process.

## Proof
Let \(L(x)=\log(x/(1-x))\). The first coordinate \(X\) of the image satisfies
\[
 L(X)=L(x)-a(x-b+cq),\qquad Q=(1-k)q+k(p_0+p_1x).
\]
The positive function \(x\mapsto X\) takes values in \((0,1)\). The second coordinate is a convex combination of \(q\) and a point in \(I\), proving invariance of \(D\). Since \(p_0+p_1x\in(0,1)\), it also proves invariance of the full open unit square.

First suppose \(0<k<1\). For a fixed target \((X,Q)\), the belief variable in a preimage must be
\[
 q=\frac{Q-kp_0-kp_1x}{1-k}.
\]
Substitution reduces inversion to a scalar level-set equation
\[
 H(x)=L(X)-ab+\frac{ac}{1-k}(Q-kp_0),\qquad
 H(x)=L(x)-\frac{a\chi}{1-k}x,
\]
where \(\chi=1-k(1+cp_1)\). The crucial derivative and its sign are
\[
 H'(x)=\frac1{x(1-x)}-\frac{a\chi}{1-k},
\quad
 \det DF(x,q)=\frac{X(1-X)}{x(1-x)}\big[(1-k)-a\chi x(1-x)\big].
\]
The determinant identity follows by direct differentiation; all prefactors outside the bracket are positive.

If \(\chi\le0\), the function \(H\) is strictly increasing for every \(a>0\). If \(\chi>0\), then \(x(1-x)\le1/4\) shows that \(H\) is strictly increasing if and only if \(a\le a_c=4(1-k)/\chi\). At equality the derivative vanishes only at \(x=1/2\), so strict monotonicity still holds. Thus two preimages of the same target must have equal \(x\), and then equal \(q\): injectivity follows. In the strict inequality case the determinant is positive everywhere, giving a smooth inverse on the image by the inverse-function theorem and injectivity.

If \(\chi>0\) and \(a>a_c\), the equation \(H'(x)=0\) has exactly two roots \(x_-<1/2<x_+\) displayed above. Direct differentiation gives
\[
 H''(x)=-\frac{1-2x}{x^2(1-x)^2},
\]
which is negative at \(x_-\) and positive at \(x_+\). Each critical line is a nondegenerate fold: use \((x,Q)\) as smooth source coordinates, possible since \(1-k>0\), and \((L(X),Q)\) as target coordinates. The resulting map is \((x,Q)\mapsto(H(x)+ab-ac(Q-kp_0)/(1-k),Q)\), whose fold normal form follows from \(H''(x_\pm)\ne0\). It has a local double inverse near either fold within any open belief interval. The determinant sign is positive, negative, positive on the three consecutive \(x\)-intervals. Since \(H\) is strictly monotone on each, there can be at most three preimages for any target, regardless of domain restrictions.

To show two preimages exist inside \(D\), select any interior belief \(q_0\in I\) and a point on one fold. At a target with the same \(Q\), two nearby distinct values of \(x\) on opposite sides of the extremum have equal \(H(x)\); the associated beliefs computed above vary continuously and stay in \(I\). Thus the map is not injective on either \(D\) or the full square.

The triple-inverse assertion is stronger. Put \(a=a_c(1+\eta)\), and write \(t_\eta\in(0,1/2)\) for the unique positive solution
\[
 \frac{\operatorname{artanh}(2t_\eta)}{2t_\eta}=1+\eta.
\]
Uniqueness follows because the left side increases continuously and strictly from \(1\) to infinity. Also \(t_\eta\to0\) as \(\eta\downarrow0\). Because \(a\chi/(1-k)=4(1+\eta)\), the three numbers \(x=1/2\) and \(x=1/2\pm t_\eta\) give the same scalar value \(H(x)\). Choose \(q_0=p_0+p_1/2\) and, for each of the three values of \(x\), choose
\[
 q(x)=q_0-\frac{kp_1}{1-k}\left(x-\frac12\right).
\]
All three have identical \(Q\), and for sufficiently small \(\eta\) they lie in \(I\). Hence they also have the same first image coordinate, producing three physical preimages. The at-most-three result proves there are exactly three.

At \(a=a_c\), holding \(Q\) fixed and setting \(x=1/2+t\) gives
\[
 H(1/2+t)-H(1/2)=\frac{16}{3}t^3+O(t^5).
\]
The logit of the first target coordinate differs by exactly this quantity, and the logit function has nonzero finite derivative at each interior target. Thus the local inverse is Hölder \(1/3\) in the transverse direction and is not Hölder with any exponent greater than \(1/3\), in particular not locally Lipschitz. The affine formula for \(q\) shows the complete local inverse has the same optimal exponent.

Finally, if \(k=1\), then \(Q=p_0+p_1x\) determines \(x\) uniquely because \(p_1>0\); the first image coordinate then determines \(q\) uniquely because \(ac>0\). Its determinant is \(acp_1X(1-X)>0\). This closes all cases.

## Verification
A standalone Python checker (`verify.py`) verifies the determinant factorization exactly with SymPy, the third derivative giving the cubic contact, and an explicit physical triple-preimage witness with 75-digit mpmath arithmetic. For the source's illustrative values \(p_0=10^{-5}\), \(p_1=10^{-3}\), \(c=500\), \(b=0.3\), and \(k=1/2\), the threshold is \(a_c=8\). At \(a=8.1\), the checker obtains three preimages with first coordinates approximately \(0.4042511491\), \(0.5\), \(0.5957488509\), all mapping to \(X\approx0.02447078861\) and \(Q=0.00051\). Symbolic and numeric checks supplement the general proof, not replace it.

## Relationship to prior work
Metaxas and Sapsis (2026) introduce this exact risk-sensitive learning map, prove equilibrium and Cesàro-average properties, and investigate complex attractors, phase locking, and crises numerically. Their detailed main text and appendices do not state a global one-step injectivity criterion, its two fold lines, the three-preimage onset, or the cubic endpoint inverse law. Chotibut and colleagues (2018) investigate multiplicative-weights chaos in a different game model and on an invariant one-dimensional diagonal; it does not imply the present two-dimensional adaptive-belief inversion classification. Adomaitis and Kevrekidis (1991) establish the relevance of noninvertibility to complicated basin structure in a different adaptive-control map. The importance of fold curves is known; the exact boundary for the current risk-memory map is the claimed contribution. For the source's numerical parameters \(c=500\), \(p_1=10^{-3}\), and \(k=0.865\), the sharp condition gives \(k>2/3\), hence the map is globally one-to-one at every learning intensity—even in the parameter regime where the source numerically observes complex attractors. Thus folding is not a prerequisite for the reported complexity. The analysis of prior literature is not an independent guarantee of historical priority.

## Limitations
The result characterizes injectivity and local fold geometry, not global attractors or the topology of any basin boundary. Above threshold some targets may have fewer than three physical preimages; three preimages are guaranteed sufficiently near onset, not for every target or at every supercritical parameter. The map is not claimed to be onto the unit square. The strict assumption \(p_1>0\) excludes degenerate instantaneous-memory updates. The inverse Hölder assertion is local on the image near the critical line, not a uniform global estimate.

## References
1. K. Metaxas and T. P. Sapsis, “Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics,” arXiv:2606.29967, first submitted June 29, 2026. https://arxiv.org/abs/2606.29967
2. T. Chotibut, F. Falniowski, M. Misiurewicz, and G. Piliouras, “Family of chaotic maps from game theory,” arXiv:1807.06831 (2018); *Dynamical Systems* (2021). https://arxiv.org/abs/1807.06831
3. R. A. Adomaitis and I. G. Kevrekidis, “Noninvertibility and the structure of basins of attraction in a model adaptive control system,” *Journal of Nonlinear Science* **1** (1991), 95–105. https://doi.org/10.1007/BF01209149
