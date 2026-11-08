# Sharp golden-ratio threshold and exceptional-density law for twofold Beatty range tests

## Finding
Let \(\alpha>1\) be irrational, let \(f_\alpha(n)=\lfloor\alpha n\rfloor\) on positive integers, and put
\[u_x=\{x/\alpha\},\qquad v_x=\{x/\alpha^2\},\qquad \varphi=(1+\sqrt5)/2.\]
Consider the twofold range condition from Khani–Valizadeh–Zarei (2026):
\[C_\alpha(x):\quad 1-1/\alpha<u_x<1,\quad 1-2/\alpha<v_x-u_x/\alpha<1-1/\alpha.\]
For **every** irrational \(\alpha>1\) and positive integer \(x\), the exact missing branch is
\[x\in f_\alpha^{\circ2}(\mathbb N)\iff C_\alpha(x)\ \text{or}\ E_\alpha(x),\]
where
\[E_\alpha(x):\quad 1-1/\alpha<u_x<2-\alpha,\qquad v_x>2-2/\alpha+u_x/\alpha.\]
The two branches are disjoint. In particular, the published twofold condition is **sufficient for every irrational** \(\alpha>1\), and is **necessary as well for every irrational** \(\alpha\ge\varphi\). The cutoff \(\varphi\) is best possible as a uniform assertion: for every \(1<\alpha<\varphi\) with \(1,\alpha^{-1},\alpha^{-2}\) linearly independent over \(\mathbb Q\), its false-negative set \(E_\alpha\) has natural density
\[\boxed{\delta(\alpha)=\frac{(1-\alpha+\alpha^{-1})^2}{2\alpha}>0.}\]
Thus the corresponding condition is exact at and above \(\varphi\), but omits a positive-density family for generic moduli below \(\varphi\). The independence hypothesis is essential for the density formula, not for the exact two-branch identity: for \(\alpha=\sqrt2\), the exceptional set is empty despite \(\alpha<\varphi\).

## Assumptions and scope
The domain is positive integers and irrational real moduli \(\alpha>1\). The result concerns exactly **two** compositions of the same floor map, rather than arbitrary iterates or mixed moduli. The existence of the density is asserted only under the stated rational-independence hypothesis, which holds for every transcendental \(\alpha>1\) and for algebraic \(\alpha\) of degree at least three. For other irrational moduli the exact pointwise condition remains valid but the generic density formula need not hold.

## Proof
**One-step inversion.** For integer \(x\ge1\), \(x/\alpha\) is irrational. The only possible positive integer preimage under \(f_\alpha\) is
\[y=\lfloor x/\alpha\rfloor+1=x/\alpha+1-u_x.\]
Indeed, \(f_\alpha(y)=x\) precisely when \(x\le\alpha y<x+1\), equivalently when \(u_x>1-1/\alpha\). Therefore \(x\) lies in the range of \(f_\alpha^{\circ2}\) if and only if this first inequality holds and \(y\) itself lies in the range of \(f_\alpha\).

**The two branches.** Assuming \(u=u_x>1-1/\alpha\), set \(v=v_x\) and \(s=(1-u)/\alpha\). Then \(0<s<1/\alpha^2\), and
\[\{y/\alpha\}=\{v+s\},\qquad 0<v+s<1+1/\alpha^2<2.\]
The one-step inversion criterion for \(y\) is \(\{y/\alpha\}>1-1/\alpha\). There are exactly two possibilities:
\[1-1/\alpha<v+s<1\qquad\text{or}\qquad 2-1/\alpha<v+s<2.\]
The first is exactly \(C_\alpha(x)\), because substituting \(s=(1-u)/\alpha\) yields the required two inequalities for \(v-u/\alpha\). The second is exactly \(E_\alpha(x)\): its lower inequality becomes \(v>2-2/\alpha+u/\alpha\), and the requirement \(v<1\) forces \(u<2-\alpha\). Conversely, these inequalities imply the second possibility. The two branches cannot overlap since their \(v+s\) values lie on opposite sides of one.

**Sharp threshold.** The interval \((1-1/\alpha,2-\alpha)\) is nonempty exactly when
\[1-1/\alpha<2-\alpha\iff \alpha^2-\alpha-1<0\iff1<\alpha<\varphi.\]
Thus \(E_\alpha\) is empty for all \(\alpha\ge\varphi\). Below this threshold it is a nonempty open triangle in the unit torus. In particular, its nonemptiness for every modulus with rationally independent frequencies proves the uniform threshold is sharp. As a concrete exact witness, \(\alpha=\sqrt[3]{3}\), \(x=2\) works: \(\lfloor2\alpha\rfloor=2\), hence \(2\in f_\alpha^{\circ2}(\mathbb N)\), whereas \(v_2-u_2/\alpha=1/\alpha>1-1/\alpha\), violating \(C_\alpha(2)\).

**Natural density.** If \(1,1/\alpha,1/\alpha^2\) are rationally independent, Kronecker–Weyl equidistribution makes \((u_x,v_x)\), for positive integers \(x\), uniformly distributed on the unit square. The region \(E_\alpha\) has piecewise-linear boundary of planar measure zero. Its area is
\[\begin{aligned}
\int_{1-1/\alpha}^{2-\alpha}\left(1-\left(2-2/\alpha+u/\alpha\right)\right)\,du
&=\frac{(2-\alpha-(1-1/\alpha))^2}{2\alpha}\\
&=\frac{(1-\alpha+1/\alpha)^2}{2\alpha}.
\end{aligned}\]
Equidistribution therefore proves the claimed natural density for the **false negatives** and, since \(C_\alpha\) is always sufficient, also the precise discrepancy density.

**Exceptional quadratic modulus.** For \(\alpha=\sqrt2\), \(v_x=\{x/2\}\in\{0,1/2\}\). On the proposed exceptional branch, the lower bound on \(v_x\) is strictly larger than \(2-1/\alpha-1/\alpha^2=3/2-1/\sqrt2>1/2\), an impossibility. Hence the twofold test is exact for \(\sqrt2\), even though the universal cutoff is \(\varphi\).

## Verification
Run `python3 verify.py` with Python 3. The verifier independently enumerates images of the twofold floor map and compares both the published test and the derived exceptional branch, including \(\sqrt2\), \(\sqrt6\), \(\sqrt[3]{3}\), \(\pi/2\), and \(\varphi\). It uses only standard-library high-precision decimal arithmetic. All direct membership comparisons and branch decompositions passed over the checked finite domains. These computations are illustrative and do not prove the infinite statement; the proof rests on exact inversion and Kronecker–Weyl equidistribution.

## Relationship to prior work
Khani, Valizadeh, and Zarei (2026, arXiv:2607.12817) give the multi-iterate fractional-part test for irrational \(\alpha>(3+\sqrt5)/2\), and explicitly ask about lower moduli. The present theorem handles just the first nontrivial iterate, obtains the smaller **sharp** uniform threshold \(\varphi\), determines the exact omitted region for all irrational moduli, and computes its density for rationally independent frequencies. Ashfaque (2026) discusses apparent lower-modulus failures computationally, but neither the sharp twofold cutoff nor the exact triangular density law is stated there. In fact, its reported false-positive behavior for the particular second-iterate condition is incompatible with the elementary one-step inversion: the condition is always sufficient. This comparison refers strictly to the twofold condition as stated above and does not assess arbitrary iterates or alternate predicates. Fraenkel's 1994 study of iterated floors primarily concerns algebraic identities and bounded errors; no covering general density theorem was established from the material accessible in the present literature check.

## Limitations
The result does not address third or higher iterates. For quadratic irrational parameters below \(\varphi\), rational independence can fail and the density formula may not apply; the exact pointwise two-branch criterion still does. Kronecker–Weyl supplies a limit, not an explicit convergence rate. Priority is qualified by the possibility of unindexed equivalent observations and incomplete access to one older full article; independent mathematical assessment has not been performed.

## References
1. M. Khani, A. N. Valizadeh, A. Zarei, *A Note on Iterated Beatty Sequences*, arXiv:2607.12817 (first public version July 14, 2026), https://arxiv.org/abs/2607.12817.
2. J. M. Ashfaque, *An Empirical Analysis of Iterated Beatty Sequences Below the Golden Threshold: Interval Collapse and Non-Uniform Bifurcation*, public full text dated July 15, 2026, https://www.researchgate.net/publication/409977651.
3. A. S. Fraenkel, *Iterated Floor Function, Algebraic Numbers, Discrete Chaos, Beatty Subsequences, Semigroups*, Transactions of the American Mathematical Society 341 (1994), 639–664, https://doi.org/10.1090/S0002-9947-1994-1138949-9.
4. J. J. Chew III, S. M. Tanny, *Further results on iterated Beatty functions*, Journal of Difference Equations and Applications 7 (2001), 413–434, https://doi.org/10.1080/10236190108808279.
5. Kronecker–Weyl equidistribution theorem for irrational torus rotations (classical).
