# A square-root onset and marked angular law for random three-terminal Steiner savings

## Finding

Let three independent points be uniformly sampled by Euclidean arclength on a circle of any radius. Denote by \(M\) the total length of their Euclidean minimum spanning tree, by \(S\) that of their Euclidean Steiner minimal tree, and set \(Q=1-S/M\). Thus \(Q\) measures the *relative length saving* obtained by permitting an auxiliary Steiner junction. The scale of the circle cancels.

There is an atom at zero:
\[
\Pr(Q=0)=\frac13.
\]
The positive part of the distribution has a square-root onset:
\[
\Pr(0<Q<t)=C\sqrt t+o(\sqrt t),\qquad t\downarrow0,
\]
where
\[
\begin{aligned}
h(\alpha)&=\frac{\sin(\alpha/2)\sin(\pi/3-\alpha/2)}{[\sin(\alpha/2)+\sin(\pi/3-\alpha/2)]^2},\\
C&=\frac3{\pi^2}\int_0^{2\pi/3}\sqrt{\frac2{h(\alpha)}}\,d\alpha
 =2.700948948484718\ldots.
\end{aligned}
\]
The integrable square-root singularities of this shape integral occur at its two endpoints.

For the conditional shape statement, number the three successive angular gaps cyclically, and let \(J\in\{1,2,3\}\) index the unique largest gap. Let \(B\) be the gap immediately following that largest gap in the cyclic orientation. Conditionally on \(0<Q<t\), the joint law of \((J,B,Q/t)\) converges in **total variation** to the product of a uniform law on \(\{1,2,3\}\), a law on \((0,2\pi/3)\) with density
\[
g(\alpha)=\frac{\sqrt{2/h(\alpha)}}{\int_0^{2\pi/3}\sqrt{2/h(u)}\,du},
\]
and a \(\operatorname{Beta}(1/2,1)\) law on \((0,1)\) with density \(1/(2\sqrt z)\). In particular, although the savings are small, the two nonlarge gaps have a nonuniform, explicitly weighted limiting shape distribution.

There is also an exact expression for the entire positive part of the distribution. For \(0<s<\pi/3\), put
\[
T(s)=\frac{2\pi}3+2s,\quad c(s)=\frac{4\pi}3-2s,\quad
\ell(s)=\max\{0,T(s)-c(s)\},\quad u(s)=\min\{T(s),c(s)\},
\]
\[
H(s,\alpha)=\frac{\sin(\alpha/2)\sin((T(s)-\alpha)/2)}{[\sin(\alpha/2)+\sin((T(s)-\alpha)/2)]^2},
\quad q(s,\alpha)=1-\sqrt{1-2H(s,\alpha)(1-\cos s)}.
\]
Then for every \(0<t<1\),
\[
\boxed{\Pr(0<Q<t)=\frac3{\pi^2}\int_0^{\pi/3}\int_{\ell(s)}^{u(s)}\mathbf 1_{\{q(s,\alpha)<t\}}\,d\alpha\,ds.}
\]
The inner integral has an explicit inverse-trigonometric evaluation given in the proof and in the numerical checker, reducing the distribution to a one-dimensional quadrature.

## Assumptions and scope

The three circle samples are independent and uniform in Euclidean arclength; coincident vertices and angular-gap ties have probability zero. Both networks are planar Euclidean shortest-length connecting trees, not intrinsic circle networks or independent-edge-weight trees. The result concerns exactly three terminals, all circle radii, the atom, the positive-saving distribution and its marked small-saving limit. The zero atom and deterministic \(120^\circ\) Steiner-junction rule are classical and are not asserted as new.

## Proof

**1. Gap measure and classical topology switch.**  Fix a cyclic orientation and write the successive angular gaps as \(a,b,c>0\) with \(a+b+c=2\pi\). By rotational invariance and order statistics, \((a,b)\) has constant density \(1/(2\pi^2)\) on this simplex; the gaps are exchangeable. A triangle angle equals half the opposite circular gap. A Euclidean Steiner junction improves on the MST if and only if each triangle angle is strictly less than \(2\pi/3\), hence precisely when \(\max\{a,b,c\}<4\pi/3\). The disjoint events that a particular gap exceeds \(4\pi/3\) each have probability \((1-2/3)^2=1/9\), proving the atom \(1/3\).

**2. Exact relative saving.**  Within the positive-saving region, designate the largest angular gap by \(c\), and write the other two as \(a=\alpha\) and \(b=2\pi-\alpha-c\). The triangle's longest chord faces its largest angle \(A=c/2\); let \(p=2\sin(a/2)\) and \(r=2\sin(b/2)\) be the shorter chords (the unit circle is sufficient). Then \(M=p+r\). For a triangle whose angles are all below \(120^\circ\), the classical Fermat–Torricelli length formula, obtained by building an external equilateral triangle, is
\[
S^2=\frac{p^2+r^2+d^2+4\sqrt3\,\Delta}{2}
=p^2+r^2-pr\cos A+\sqrt3\,pr\sin A,
\]
where \(d\) is the remaining side and \(\Delta=pr\sin A/2\) is the area. Introduce the angular distance \(s=2\pi/3-A=(4\pi/3-c)/2>0\). Since \(2+\cos A-\sqrt3\sin A=2(1-\cos s)\),
\[
Q=1-\sqrt{1-2\frac{pr}{(p+r)^2}(1-\cos s)}.
\]
The constraints that \(c\) is the largest gap are exactly \(\ell(s)<\alpha<u(s)\) as defined above. The substitution \(c=4\pi/3-2s\) has Jacobian \(2\), so multiplying the simplex density by three largest-gap labels yields the exact integral \(3/\pi^2\) displayed in the finding. For fixed \(s\), \(H(s,\alpha)\) increases from the left endpoint toward \(\alpha=T(s)/2\), then decreases symmetrically. When \(w=(2t-t^2)/(2(1-\cos s))<1/4\), the small-saving region in the entire interval \((0,T(s))\) consists of the two end portions cut at
\[
\alpha_*(s,t)=2\arctan\left(\frac{\rho\sin(T(s)/2)}{1+\rho\cos(T(s)/2)}\right),\quad
\rho=\frac{2w}{1-2w+\sqrt{1-4w}}.
\]
After intersection with \((\ell(s),u(s))\), its measure is
\[
[\min\{u(s),\alpha_*\}-\ell(s)]_+
+[u(s)-\max\{\ell(s),T(s)-\alpha_*\}]_+.
\]
For \(w\ge1/4\), the entire permitted interval is included. Here \([v]_+=\max\{v,0\}\). This proves the exact one-dimensional representation used by the checker.

**3. Boundary expansion and the leading coefficient.**  As \(s\downarrow0\), the two short-chord ratio tends to \(h(\alpha)\), uniformly on compact subsets of \(\alpha\in(0,2\pi/3)\). Since \(1-\cos s=s^2/2+O(s^4)\),
\[
q(s,\alpha)=\frac12h(\alpha)s^2+o(s^2).
\]
With \(s=\sqrt t\,y\), the condition \(0<q<t\) converges to \(0<y<\sqrt{2/h(\alpha)}\). Hence the limiting area of the narrow strip is exactly \(\sqrt t\int_0^{2\pi/3}\sqrt{2/h(\alpha)}\,d\alpha\). Multiplying by \(3/\pi^2\) gives \(C\).

For completeness, this passage is globally justified, rather than inferred from a pointwise Taylor expansion. Choose a small \(s_0<\pi/6\) and parameterize \(\alpha=T(s)v\), \(0<v<1\). For \(0<s<s_0\), elementary bounds for sine on a fixed compact interval give \(H(s,T(s)v)\ge k v(1-v)\) with \(k>0\), and \(q(s,\alpha)\ge H(s,\alpha)(1-\cos s)\ge k'v(1-v)s^2\). The contribution to \(\Pr(0<Q<t)/\sqrt t\) from \(v<\delta\) or \(v>1-\delta\) is at most \(O(\sqrt\delta)+O(\sqrt t)\). On \(s\ge s_0\), the same exact formula and the fact that at least one remaining gap is bounded away from zero imply \(q\ge k''\min\{a,b\}\); the allowed angular measure is \(O(t)\). Thus all configurations outside compact interior boundary strips contribute negligibly compared with \(\sqrt t\), proving the stated asymptotic and finiteness of \(C\).

**4. Total-variation marked limit.**  On any compact subinterval of the limiting \(\alpha\) range, the map \(s\mapsto z=q(s,\alpha)/t\) is strictly increasing for sufficiently small \(s\). Its inverse satisfies
\[
s=\sqrt{\frac{2tz}{h(\alpha)}}(1+o(1)),\quad
\frac{ds}{dz}=\sqrt{\frac{t}{2h(\alpha)}}z^{-1/2}(1+o(1))
\]
uniformly for \(z\) bounded away from zero and one. Thus the normalized marked density converges pointwise to \(g(\alpha)/(2\sqrt z)\) for each largest-gap label. The endpoint bounds from step 3 control the missing mass uniformly; convergence of the densities in \(L^1\) follows by dominated convergence on compact sets followed by endpoint exhaustion. This is joint **total-variation** convergence. Uniformity of the three labels is exact by exchangeability.

## Verification

The standalone `steiner_diagnostics.py` computes the coefficient through an independently evaluated endpoint integral, evaluates the exact one-dimensional angular formula using its inverse-trigonometric cutoff, and samples Cartesian unit-circle vertices to compute the two network lengths directly. The numerical output includes \(C\approx2.700948948484718\); at \(t=10^{-8}\), the exact probability is approximately \(0.00027017303691\), so its ratio to \(\sqrt t\) is approximately \(2.701730369\). With 1,200,000 independent Cartesian configurations, the simulated zero atom is approximately \(0.332825\), and the simulated positive-saving probabilities at \(t=0.001\) and \(t=0.01\) lie within \(0.0015\) of the exact-integral values. These numerical checks corroborate, but do not prove, the analytical limit.

## Relationship to prior work

The \(120^\circ\) switch between a Fermat junction and a two-edge tree, and the equilateral Steiner ratio, are classical; see Gilbert and Pollak (1968) and the historical account of Brazil, Graham, Thomas and Zachariasen. Cieslik, Ivanov and Tuzhilin discuss deterministic and global Steiner ratios on Riemannian manifolds. The finding instead quantifies the **probability, sharp square-root boundary layer, and conditional geometry** of near-vanishing three-terminal savings under uniform circular sampling. Deterministic topology results and extremal ratios alone do not imply the angular integral or the marked law. The earlier geometry ledger result concerning the *near-maximum length of the minimum spanning tree* is not a savings-ratio distribution and analyzes a different, equilateral regime.

## Limitations

Only three terminals, independent uniform circle sampling, and Euclidean lengths are covered. The positive-saving density has a square-root singular onset; no statement is made about more terminals or nonuniform sampling. The original Gilbert–Pollak (1968) full article and some other historical sources were not accessible for complete full-text comparison, so historical priority is provisional. No independent mathematical audit has been performed.

## References

- E. N. Gilbert and H. O. Pollak, “Steiner Minimal Trees,” *SIAM Journal on Applied Mathematics* 16 (1968), 1–29, DOI: 10.1137/0116001 (abstract and metadata inspected; original full text unavailable).
- D. Cieslik, A. O. Ivanov, A. A. Tuzhilin, “Steiner Ratio for Riemannian Manifolds,” arXiv:1101.3144 (first publicly posted January 17, 2011; full arXiv text inspected).
- M. Brazil, R. L. Graham, D. A. Thomas, M. Zachariasen, “On the History of the Euclidean Steiner Tree Problem,” freely available manuscript at `https://mathweb.ucsd.edu/~ronspubs/14_02_Steiner.pdf` (background and Fermat–Torricelli sections inspected).
- K. R. Vollmar and Y. Zhang, “On the Enumeration of Steiner-Tree Topologies for the Points on a Circle,” *SIAM Journal on Discrete Mathematics*, DOI: 10.1137/0406026 (abstract inspected; topological enumeration rather than random savings).
