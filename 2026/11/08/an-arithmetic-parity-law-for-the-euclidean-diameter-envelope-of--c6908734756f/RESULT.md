# An arithmetic parity law for the Euclidean diameter envelope of moment-curve polytopes

## Finding

Let \(d\ge2\) and \(m\ge1\) be integers. Put
\[
\gamma_d(t)=(t,t^2,\ldots,t^d),\qquad
P_d(T)=\operatorname{conv}\{\gamma_d(t):t\in T\},
\]
for any finite \(T\subseteq\{-m,-m+1,\ldots,m\}\) with at least two elements. Define
\[
S_{d,m}=\sum_{i=1}^d m^{2i},\qquad
O_{d,m}=4\sum_{\substack{1\le i\le d\\i\text{ odd}}}m^{2i}.
\]
The following *universal sharp bounds and complete equality conditions* hold.

**Odd dimensions.** If \(d\) is odd, then \(\operatorname{diam}_2(P_d(T))^2\le O_{d,m}\). Equality holds if and only if \(\{-m,m\}\subseteq T\); then \(\{\gamma_d(-m),\gamma_d(m)\}\) is the unique unordered diametral pair.

**Even dimensions at the smallest integer scale.** If \(d\) is even and \(m=1\), the same assertion with \(O_{d,1}\) and the unique pair \(\{-1,1\}\) holds.

**Even dimensions at larger integer scales.** If \(d\) is even and \(m\ge2\), then \(\operatorname{diam}_2(P_d(T))^2\le S_{d,m}\). Equality holds exactly when \(T\) contains at least one of the sets \(\{-m,0\}\) and \(\{0,m\}\). Every diametral pair at equality is exactly one of the corresponding vertex pairs, and there are no others. Thus the number of diameter-attaining unordered pairs is one or two according to whether exactly one or both endpoint-zero pairs occur in \(T\).

In particular, for the full integer sample \(T=\{-m,\ldots,m\}\), the displayed bounds are *equalities* for all \(d,m\), and the number of diametral pairs is one if \(d\) is odd or \(m=1\), and two if \(d\) is even and \(m\ge2\). The upper envelopes are independent of the interior sample points. In every even dimension, the two competing endpoint-pair distances satisfy the exact ratio
\[
\frac{O_{d,m}}{S_{d,m}}=\frac{4}{1+m^2},
\]
which explains the integer-scale switch, though excluding *other* competing pairs requires the arithmetic estimate in the proof.

## Assumptions and scope

All distances use the ordinary ambient Euclidean metric of the displayed, **unweighted** moment-curve coordinates. Both \(d\) and the symmetric parameter bound \(m\) are integers; \(T\) consists of integers and is nonempty with at least two distinct elements. For \(|T|\ge d+1\) the hull is a full-dimensional cyclic lattice polytope; smaller samples are included as lower-dimensional convex hulls. The claim is not about combinatorial/edge-graph diameter, arbitrary real parameters, arbitrary rescalings of coordinates, or translated nonsymmetric parameter windows.

## Proof

**Step 1: vertex reduction.** Every \(\gamma_d(t)\) is an exposed vertex: the linear functional \(x\mapsto 2t x_1-x_2\) takes value \(t^2-(s-t)^2\) at \(\gamma_d(s)\), uniquely maximal at \(s=t\). The square of Euclidean distance is strictly convex in either argument. Hence any pair realizing the diameter of the convex hull is a pair of its distinct listed vertices. It suffices to prove a sharp pairwise distance bound and classify equality.

**Step 2: pairs with the same sign.** For \(0\le u\le v\le m\), each power difference \(0\le v^i-u^i\le m^i\). The same holds in absolute value if both parameters are nonpositive. Thus every pair with product of parameters nonnegative has squared distance at most \(S_{d,m}\). Equality requires \(\{u,v\}=\{0,m\}\), already forced by equality in the first coordinate. In odd dimension \(d=2r+1\), the strict inequality \(S_{d,m}<O_{d,m}\) follows by grouping each positive even-power term \(m^{4j}\) beneath the following odd-power term \(m^{4j+2}\), and observing that the resulting sum is strictly below four times the total odd-power sum.

**Step 3: odd-dimensional opposite-sign pairs.** Write the parameters as \(-u\) and \(v\) with \(0\le u,v\le m\), and \(d=2r+1\). The first coordinate contributes at most \(4m^2\), with equality only at \(u=v=m\). For each \(1\le j\le r\), let \(a=u/m\), \(b=v/m\). Since \(m\ge1\), the contribution of coordinates \(2j\) and \(2j+1\) obeys
\[
\begin{aligned}
&(u^{2j}-v^{2j})^2+(u^{2j+1}+v^{2j+1})^2\\
&\quad\le m^{4j+2}\big[(a^{2j}-b^{2j})^2+(a^{2j}+b^{2j})^2\big]\\
&\quad=2m^{4j+2}(a^{4j}+b^{4j})\le4m^{4j+2}.
\end{aligned}
\]
Adding proves \(\|\gamma_d(-u)-\gamma_d(v)\|^2\le O_{d,m}\). The first-coordinate equality condition forces the unique extremal parameter pair \(\{-m,m\}\), which attains the bound exactly because all even powers cancel. Together with Step 2 this finishes all odd dimensions.

**Step 4: even-dimensional opposite-sign pairs and the integer gap.** Let \(d=2r\), \(m\ge2\), and write the parameters \(-u,v\), with integers \(0\le u,v\le m\). For each odd \(p\in\{1,3,\ldots,2r-1\}\), define
\[
F_p(u,v)=(u^p+v^p)^2+(u^{p+1}-v^{p+1})^2.
\]
We claim
\[
F_p(u,v)\le m^{2p}+m^{2p+2},
\]
with equality if and only if \(\{u,v\}=\{0,m\}\). Let \(w=\max\{u,v\}\) and \(z=\min\{u,v\}\).

If \(z=0\), then \(F_p=w^{2p}+w^{2p+2}\) and equality occurs precisely when \(w=m\). If \(w=z\ge2\), then \(F_p=4w^{2p}<(1+w^2)w^{2p}\). If \(w=z=1\), then \(F_p=4<m^{2p}+m^{2p+2}\). Finally, if \(1\le z<w\), the exact difference is
\[
F_p(w,z)-(w^{2p}+w^{2p+2})
=z^p\left[2w^p(1-wz)+z^p(1+z^2)\right].
\]
Here \(w\ge z+1\ge2\), so \(1+z^2\le2(wz-1)\), because \(2wz-z^2-3\ge z^2+2z-3\ge0\). Also \(z^p<w^p\), and \(wz-1>0\). Hence the bracket is *strictly negative*. We have proved the pair estimate and its equality conditions. Summing over all \(r\) odd indices \(p\) gives the bound \(S_{d,m}\) for opposite-sign pairs, with equality only at an endpoint and zero. Step 2 covers same-sign pairs and supplies the same equality cases.

**Step 5: the exceptional integer scale.** If \(m=1\), the only possible parameters are \(-1,0,1\). In even dimension, the opposite endpoint pair has squared distance \(4(d/2)=2d=O_{d,1}\), whereas either endpoint-zero pair has squared distance \(d\). Hence the former is uniquely maximal.

**Step 6: sharpness and full contact classification.** The relevant extremal pairs exist in the full integer sample. Strictness in Steps 2–5 excludes every other pair at the stated bound. Taking an arbitrary subset \(T\) can only remove pairs, never create a new pair at the universal bound. This proves every asserted equality criterion and count.

## Verification

The standalone `verify.py` computes squared distances with exact integers for every unordered parameter pair in the complete integer interval for all \(2\le d\le16\) and \(1\le m\le16\): **240 parameter instances and 46,920 pairs**. In each instance it checks the sharp bound and the *entire equality-pair set*. It additionally tests 736 generated sparse sample sets, 14,240 direct integer-lemma cases, and 120 exact-rational real-parameter perturbations. The command `python3 verify.py` prints `EXACT_PASS` on success. Finite checks are not used to justify the all-parameter theorem; Steps 1–6 are the unrestricted proof.

## Relationship to prior work

Konoike's 2026 work studies the same integral moment-curve realization and establishes an Ehrhart-polynomial averaging formula and ensuing positivity and root properties. Liu's earlier work establishes Ehrhart polynomial identities for integral cyclic polytopes. Their inspected full texts concern lattice-point enumeration, not ambient Euclidean diameter or the equality-pair classification here. The literature also uses *diameter* to mean graph-theoretic distance: Maksimenko's ridge-graph diameter, for example, measures adjacency paths in a dual polytope, not Euclidean distance of listed moment-curve points. These results neither imply nor contradict the present metric statement. The finite-support upper-envelope and its parity transition are the new assertion, not the established definition of cyclic polytopes.

## Limitations

The sharp result relies on integer parameters and an unweighted monomial coordinate system. It does not determine the actual diameter of a sparse \(T\) that omits all universal extremal pairs; it only proves that such a diameter is strictly smaller than the displayed envelope. This restriction is essential: when \(d\) is even and \(m\ge2\), a small positive *real* \(\varepsilon\) satisfies
\[
\|\gamma_d(-m)-\gamma_d(\varepsilon)\|^2=S_{d,m}+2m\varepsilon+O(\varepsilon^2)>S_{d,m},
\]
so the same bound fails for continuous parameter intervals. Full-dimensionality requires \(|T|\ge d+1\). Historical priority remains subject to independently discovering further equivalent metric statements; no independent mathematical audit has been conducted.

## References

1. Masato Konoike, *Ehrhart polynomials of cyclic polytopes as averages of zonotope Ehrhart polynomials*, arXiv:2609.28417v1 (public 2026-09-23), https://arxiv.org/abs/2609.28417.
2. Fu Liu, *Ehrhart polynomials of cyclic polytopes*, arXiv:math/0409337 (public 2004-09-20), https://arxiv.org/abs/math/0409337.
3. A. N. Maksimenko, *The diameter of the ridge-graph of a cyclic polytope*, Discrete Mathematics and Applications 19 (2009), 47–53, doi:10.1515/DMA.2009.003.
