# Parity-dependent optimal laziness for finite-horizon star-walk variation

## Finding

**Theorem (exact finite-horizon edge-variation optimization).** Let \(k\ge 2\), let \(K_{1,k}\) be the unweighted star with hub \(o\) and leaves \(v_1,\ldots,v_k\), and let \(0\le\alpha\le1\). Define a single lazy random-walk averaging step on real vertex signals by
\[
 (P_\alpha f)(o)=\alpha f(o)+\frac{1-\alpha}{k}\sum_{i=1}^k f(v_i),\qquad
 (P_\alpha f)(v_i)=\alpha f(v_i)+(1-\alpha)f(o).
\]
For the edge-total-variation seminorm \(J(f)=\sum_{i=1}^k|f(v_i)-f(o)|\), and every integer horizon \(m\ge1\), put
\[
 L_{k,m}(\alpha)=\sup_{J(f)>0}\frac{J(P_\alpha^m f)}{J(f)},\quad a=\alpha^m,\quad b=(2\alpha-1)^m.
\]
The **exact attained operator norm** is
\[
 \boxed{L_{k,m}(\alpha)=\max\!\left\{|b|,\frac{2(k-1)a-(k-2)b}{k}\right\}.}
\]
There is a **unique** minimizer of \(L_{k,m}\) on \([0,1]\) for every \(k\ge2\), \(m\ge1\), as follows:

1. **Even \(m\):** \(\alpha_*=1/3\) and \(\min L_{k,m}=3^{-m}\), independently of the number of leaves.
2. **Odd \(m=1\):** \(\alpha_*=1/(k+1)\) and \(\min L_{k,1}=(k-1)/(k+1)\).
3. **Odd \(m\ge3\), \(k=2,3\):** With \(r=(k-1)^{1/m}\), the unique optimum is \(\alpha_*=1/(2+r)\) and \(\min L_{k,m}=(r/(2+r))^m\).
4. **Odd \(m\ge3\), \(k\ge4\):** With \(s=((k-1)/(k-2))^{1/(m-1)}\), the unique optimum is \(\alpha_*=1/(2+s)\) and
\[
 \boxed{\min L_{k,m}=\frac{k-1}{k}(2+s)^{-(m-1)}.}
\]

Thus \(k=4\) is the exact onset of an **interior stationary optimum** for odd horizons beyond one step; the two- and three-leaf cases remain optimized at a cusp where competing norm branches agree. For even horizons, \(\alpha=1/3\) has the stronger universal *edgewise* identity
\[
 (P_{1/3}^{m}f)(v_i)-(P_{1/3}^{m}f)(o)
 =3^{-m}\big(f(v_i)-f(o)\big)\qquad (m\text{ even}).
\]
For completeness, when \(k=1\), \(L_{1,m}(\alpha)=|2\alpha-1|^m\), uniquely minimized by \(\alpha_*=1/2\) with value zero for every \(m\ge1\).

## Assumptions and scope

All signals are arbitrary real functions on the \(k+1\) vertices. The holding probability is **the same at every vertex** and is held fixed across all \(m\) steps. At the hub, non-holding means uniformly averaging all leaves; at a leaf, it means moving to the hub. No data normalization or positivity condition is imposed. The variation is the unweighted sum over the \(k\) undirected edges counted once; it is *not* total-variation distance of probability distributions or the shift discrepancy \(\|f-Pf\|_1\). Because constants are fixed and form the kernel of \(J\), the quotient operator norm is well-defined. The theorem covers all finite \(k\) and all positive integer \(m\), including the extreme probabilities \(0,1\). It does not optimize among nonuniform or time-varying holding policies.

## Proof

Write the leaf-to-hub gradient as \(g_i=f(v_i)-f(o)\). Direct substitution gives
\[
 (P_\alpha f)(v_i)-(P_\alpha f)(o)
 =\alpha g_i-\frac{1-\alpha}{k}\sum_{j=1}^{k}g_j.
\]
Thus on the \(k\)-dimensional edge space the step matrix is
\[
 B_\alpha=\alpha I-(1-\alpha)Q,\qquad Q=\frac1k\mathbf1\mathbf1^{\mathsf T},\quad Q^2=Q.
\]
The complementary projectors \(I-Q\) and \(Q\) have respective eigenvalues \(\alpha\) and \(2\alpha-1\), so
\[
 B_\alpha^m=a(I-Q)+bQ.
\]
Its diagonal entries are \(((k-1)a+b)/k\); its off-diagonal entries are \((b-a)/k\). The \(\ell^1\) induced matrix norm equals the common absolute column sum
\[
 \frac{|(k-1)a+b|+(k-1)|b-a|}{k}.
\]
For \(a\ge0\) and any real \(b\), a split into \(b\ge a\), \(-(k-1)a\le b\le a\), and \(b\le-(k-1)a\) simplifies this to
\[
 \max\left\{|b|,\frac{2(k-1)a-(k-2)b}{k}\right\}.
\]
The gradient map from vertex signals modulo constants onto \(\mathbb R^k\) is bijective; \(J(f)=\|g\|_1\). Hence this is the *exact* variation norm, attained by every nonzero input whose edge gradient is a single coordinate vector, for example the nonnegative indicator of one leaf. This also proves the formula at endpoints and at all eigenvalue sign changes.

For the optimization, first observe that on \([1/2,1]\), \(0\le b\le a\) for every \(m\ge1\). The active branch is \([2(k-1)a-(k-2)b]/k\), and it strictly increases with \(\alpha\), because its derivative is
\[
 \frac{2m}{k}\left[(k-1)\alpha^{m-1}-(k-2)(2\alpha-1)^{m-1}\right]>0
\]
(with the evident interpretation at \(m=1\)). It suffices to optimize in \([0,1/2]\). Write \(q=1-2\alpha\), so \(q\ge0\).

If \(m\) is even, \(b=q^m\). For \(0\le\alpha\le1/3\), one has \(q\ge\alpha\) and the norm is \(q^m\), strictly decreasing. For \(1/3\le\alpha\le1/2\), the norm is \([2(k-1)\alpha^m-(k-2)q^m]/k\), strictly increasing. Thus the unique minimum is at \(1/3\), equals \(3^{-m}\), and at this parameter both eigenvalues have magnitude \(1/3\) and identical \(m\)-th powers. Consequently \(B_{1/3}^m=3^{-m}I\) for even \(m\), yielding the edgewise identity.

If \(m\) is odd, \(b=-q^m\) on \([0,1/2]\). The norm is exactly
\[
 \max\left\{q^m,\ F(\alpha)\right\},\qquad
 F(\alpha)=\frac{2(k-1)\alpha^m+(k-2)q^m}{k}.
\]
The branches meet precisely when \(q^m=(k-1)\alpha^m\), at
\[
 \alpha_0=\frac1{2+(k-1)^{1/m}}.
\]
For \(\alpha<\alpha_0\), \(q^m\) is the active and strictly decreasing branch. For \(\alpha>\alpha_0\), \(F\) is active. Its derivative has the sign of
\[
 (k-1)\alpha^{m-1}-(k-2)q^{m-1}.
\]
For \(m=1\) this is positive (indeed it equals \(1\)), so the unique optimum is \(\alpha_0=1/(k+1)\). For \(m\ge3\) odd and \(k=2,3\), the derivative is positive throughout \([\alpha_0,1/2]\): for \(k=2\) it is positive directly; for \(k=3\) it is already positive at \(\alpha_0\) since \(2>2^{(m-1)/m}\), and increases thereafter. Thus the cusp \(\alpha_0\) uniquely minimizes and yields the asserted value.

Finally, for \(m\ge3\) odd and \(k\ge4\), the derivative of \(F\) is negative at \(\alpha_0\) since \((k-2)^m>k-1\), while positive at \(1/2\); its sign changes exactly once, because \(\alpha/q\) increases strictly. The stationary point satisfies \(q=s\alpha\) for \(s=((k-1)/(k-2))^{1/(m-1)}\), hence \(\alpha_*=1/(2+s)>\alpha_0\). This is the unique global minimizer. At stationarity, \((k-1)\alpha^{m-1}=(k-2)q^{m-1}\); using \(2\alpha+q=1\),
\[
 F(\alpha_*)=\frac{2(k-1)\alpha_*^m+(k-2)q_*^m}{k}
 =\frac{k-1}{k}\alpha_*^{m-1}.
\]
This is the claimed minimum. The separate \(k=1\) edge map is multiplication by \(2\alpha-1\), establishing the last assertion. \(\square\)

## Verification

The accompanying dependency-free `check.py` uses `fractions.Fraction`. It independently iterates the **vertex** random-walk update and checks its single-edge variation against the closed edge-matrix norm at 4,368 exact rational parameter combinations, verifies 2,050 arbitrary signed-input inequalities, tests 3,150 even-horizon edgewise scalar identities using exact arithmetic, and compares the odd-horizon analytic minimizers to 300,300 points on a fine numerical parameter grid. These tests are diagnostic: the all-size, all-horizon and uniqueness statements follow from the preceding analytical proof, not from the grid. Run `python check.py` after extracting the package.

## Relationship to prior work

The standard finite-tree edge-total-variation seminorm and its use for regularization are treated by Kolmogorov, Pock and Rolinek (2015), whose full preprint studies **optimization with variation penalties**, not variation norms of powers of lazy Markov averaging. Sandryhaila and Moura (2013) study a different graph-shift variation \(\|f-A_{\mathrm{norm}}f\|_1\) and design filters but do not give this edge-variation horizon optimization. Boyd, Diaconis and Xiao (2003/2004) optimize an **asymptotic spectral mixing rate** for symmetric stochastic chains and distinguish it from distributional total variation; that objective does not imply the finite-horizon \(\ell^1\) edge-gradient optimum of this generally nonsymmetric counting-measure chain.

The closest reported graph-edge result for lazy walks is the **one-step** complete-bipartite theorem restricted to \(K_{p,q}\) with \(p,q\ge2\) (published-finding corpus, 2026-11-02). Its sharp one-step coefficient can be extended algebraically to a star, so the isolated \(m=1\) value is **not claimed as a novelty by itself**. Its proof and statement do not give the all-horizon powers, the even-horizon scalar identity, or the different cusp/interior odd-horizon optimizers. The finite-horizon lazy directed-triangle result (published-finding corpus, 2026-10-26) instead minimizes *distributional* total-variation distance of a different chain. A related continuous-time tree-heat variation criterion (published-finding corpus, 2026-10-26) does not supply finite-power optimal holding probabilities. These comparisons support originality of the **combined all-horizon optimal-laziness theorem**, not priority of its elementary spectral decomposition alone.

## Limitations

The optimization is within the single-parameter family of homogeneous-holding lazy neighbor averages, with the same parameter at all steps, on unweighted finite stars. It does not optimize over all stochastic matrices with the same graph support, variable holding probabilities across vertices or time, or stationary-distribution mixing metrics. The exact spectral decomposition is classical linear algebra; the new content proposed here is its sharp edge-variation all-horizon norm and the complete parity-sensitive optimization. The literature comparison cannot eliminate an unindexed earlier equivalent computation. Independent scientific validation has not been performed.

## References

1. V. Kolmogorov, T. Pock and M. Rolinek, *Total variation on a tree*, arXiv:1502.07770, first submitted 2015-02-26, SIAM Journal on Imaging Sciences 9 (2016), 605–636. https://arxiv.org/abs/1502.07770.
2. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, arXiv:1307.0468, first submitted 2013-07-01. https://arxiv.org/abs/1307.0468.
3. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, Stanford technical report 2003-04 (February 2003), SIAM Review 46 (2004), 667–689. https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Diaconis/Diaconis7.pdf.
4. *Sharp edge-variation contraction of lazy walks on complete bipartite graphs*, published-finding corpus record 2026/11/2/SCOPE-sharp-edge-variation-contraction-of-lazy-walks-on-complete-bipar--77f0e7590ff5, 2026.
5. *Exact finite-horizon total-variation optimizers for a lazy directed triangle*, published-finding corpus record 2026/10/26/SCOPE-exact-finite-horizon-total-variation-optimizers-for-a-lazy-direc--5e5efd39850a, 2026.
6. *A conductance-independent contraction criterion for weighted tree heat flow in total variation*, published-finding corpus record 2026/10/26/SCOPE-a-conductance-independent-contraction-criterion-for-weighted-tre--9fedb9294a7c, 2026.
