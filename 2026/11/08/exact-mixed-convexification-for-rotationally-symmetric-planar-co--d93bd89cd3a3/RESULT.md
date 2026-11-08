# Exact mixed convexification for rotationally symmetric planar convexifiers

## Finding

Let \(n\ge3\). For the unit-circumradius regular polygon
\[
P_n=\operatorname{conv}\{v_j=(\cos(2\pi j/n),\sin(2\pi j/n)):0\le j<n\},\qquad A_n=\{v_j:0\le j<n\},
\]
let \(K\subset\mathbb R^2\) be any compact convex body invariant under rotation about the origin by \(2\pi/n\). For a nonzero vector \(u\), denote its exposed face by \(F(K,u)=\{x\in K: u\cdot x=h_K(u)\}\). Put
\[
u=(\cos(\pi/n),\sin(\pi/n)),\quad
\ell=\mathcal H^1(F(K,u)),\quad
r_K=\inf\{t>0:-v_0\in tK\},\quad s_n=2\sin(\pi/n).
\]
(Thus \(\ell\) is the length of the exposed segment, or zero when the face is a point.) Then for **every** \(\lambda\ge0\),
\[
A_n+\lambda K\text{ is convex}
\quad\Longleftrightarrow\quad
\ell>0\text{ and }\lambda\ge\max\{r_K,s_n/\ell\}.
\]
Equivalently, the exact relative finite-convexification threshold is infinite for \(\ell=0\) and equals the displayed maximum otherwise. This is an attained threshold for all bodies satisfying the hypotheses, including nonsmooth bodies with curved boundary arcs.

**Two regular-polygon classification.** Let \(K=\mathcal R_\delta P_m\) for \(m\ge3\), where \(P_m\) is a centered unit-circumradius regular polygon and \(\mathcal R_\delta\) is planar rotation. Finite convexification occurs exactly if
\[
n\mid m,\qquad \delta\equiv\frac\pi n-\frac\pi m\pmod{2\pi/m}.
\]
Under this necessary and sufficient alignment, the exact minimum is
\[
\lambda_*=
\begin{cases}
1,&m=n\text{ even},\\
\sec(\pi/n),&m=n\text{ odd},\\
\sin(\pi/n)/\sin(\pi/m),&m>n.
\end{cases}
\]
In particular, arbitrarily small nonzero perturbations of an aligned rotation can make the threshold infinite; if \(m=kn\) with fixed \(k\ge2\), the finite threshold tends to \(k\) as \(n\to\infty\).

## Assumptions and scope

All Minkowski sums are pointwise. Convexity is ordinary Euclidean set convexity; \(K\) is compact, convex, and has nonempty interior. Rotational invariance ensures \(0\in\operatorname{int}K\), since a full-dimensional body invariant under a nontrivial rotation of order at least three cannot separate the origin from itself by a supporting line. The gauge quantity \(r_K\) is finite and positive. The regular polygons are centered at the origin with circumradius exactly one. No restriction to polygonal \(K\) is made in the main statement. The same theorem for circumradius \(R>0\) replaces \(s_n\) by \(2R\sin(\pi/n)\) and \(r_K\) by the gauge of \(-R v_0\).

## Proof

**Exposed-face obstruction and its sharp scale.** Write \(C=P_n+\lambda K\), \(U=A_n+\lambda K\). For every \(\lambda\ge0\), \(\operatorname{conv}U=C\), hence \(U\) is convex exactly when \(U=C\). Fix the outward normal \(u\) to the polygon side \([v_0,v_1]\). For \(\lambda>0\), the exposed face of \(C\) is
\[
F(C,u)=[v_0,v_1]+\lambda F(K,u),
\]
while the exposed set of \(U\) in this direction is
\[
F(U,u)=(\{v_0,v_1\}+\lambda F(K,u)).
\]
The two translated copies of the segment \(\lambda F(K,u)\) lie on the same supporting line. They have equal length \(\lambda\ell\), and their starting points differ along that line by exactly \(s_n=\|v_1-v_0\|\). Their union covers their convex hull if and only if \(\lambda\ell\ge s_n\). If \(\ell=0\), no positive scale can cover the nontrivial intervening segment. Rotating by multiples of \(2\pi/n\) proves the same criterion at every side normal of \(P_n\).

For every other direction \(w\), the exposed face \(F(P_n,w)\) is a single vertex \(v_j\), hence the exposed face of \(C\) is \(v_j+\lambda F(K,w)\), wholly inside \(U\). Every boundary point of the planar convex body \(C\) has a supporting direction, so we have proved the **exact boundary criterion**
\[
\partial C\subseteq U\quad\Longleftrightarrow\quad \lambda\ell\ge s_n.
\]
This remains true when \(K\) has infinitely many exposed directions or curved arcs. The necessity of the boundary criterion follows from \(U=C\).

**Central obstruction and sufficiency.** Since \(0\in C\), the equality \(U=C\) implies \(0\in U\), i.e. \(-v_j\in\lambda K\) for at least one \(j\). Invariance of \(K\) under the \(n\)-fold rotation makes this equivalent to \(-v_j\in\lambda K\) for **every** \(j\), which is equivalent to \(\lambda\ge r_K\). Conversely, if \(\lambda\ge r_K\), then **every** translated convex body \(v_j+\lambda K\) contains the origin. If also \(\lambda\ell\ge s_n\), the boundary criterion gives \(\partial C\subseteq U\). For any \(x\in C\), choose the terminal point \(y\in\partial C\) of the radial segment from the origin through \(x\). Some translate \(v_j+\lambda K\) contains \(y\), and it contains \(0\) as well. Convexity of this single translate therefore puts the full segment \([0,y]\), including \(x\), in \(U\). Thus \(C\subseteq U\), proving the stated sharp equivalence, including equality at the threshold. At \(\lambda=0\), the finite vertex set is not convex and the positive lower bound excludes it.

**Regular-convexifier arithmetic.** The outward normals to edges of \(P_n\) are \(\pi/n+2\pi j/n\), and those for \(\mathcal R_\delta P_m\) are \(\delta+\pi/m+2\pi k/m\). Every first set normal must appear in the second for \(\ell>0\). This happens exactly when \(n\mid m\) and \(\delta\equiv\pi/n-\pi/m\pmod{2\pi/m}\). Then \(\ell=2\sin(\pi/m)\). For \(m=n\) we have \(K=P_n\), whose antipodal vertex gauge is \(r_K=1\) for even \(n\) and \(r_K=\sec(\pi/n)\) for odd \(n\) (an antipodal ray reaches a vertex or the midpoint of a side respectively). The side-length ratio is one, giving the first two cases.

For \(m=kn>n\), \(k\ge2\), the polygon \(K\) contains its incircle of radius \(\cos(\pi/m)\), so \(r_K\le\sec(\pi/m)\). Put \(a=\pi/m\). Since \(2a\le\pi/n\le\pi/3\), we have
\[
\frac{\sin(\pi/n)}{\sin a}\ge\frac{\sin(2a)}{\sin a}=2\cos a\ge\sec a,
\]
where the last inequality uses \(a\le\pi/6\). Thus the side-length obstruction dominates the central obstruction and the third case follows. The claimed asymptotic is immediate from the small-angle expansion of sine.

## Verification

A pure-standard-library Python verifier (`mixed_polygon_verify.py`) independently constructs convex hulls of finite Minkowski sums and tests side, center, and radial witnesses. It examines all aligned pairs of side counts \(3\le n\le14\), \(m=kn\) with \(1\le k\le5\) and \(m\le65\), as well as nonsimilar rotationally symmetric polygons made as Minkowski sums of rotated regular polygons for \(3\le n\le12\). It also checks strict subthreshold and misalignment witnesses. The locally executed output was:

```text
MIXED_REGULAR_POLYGON_TESTS_OK 61438
N_FOLD_SYMMETRIC_CONVEXIFIER_TESTS_OK 82508
```

The real-parameter and arbitrary-convex-body statements are proved above, **not** inferred from finite tests. Floating-point hull/containment checks are supplementary consistency tests only; no numeric tolerance appears in the analytic proof.

## Relationship to prior work

Meyer's *Finite convexification by Minkowski summation* (arXiv:2610.26744v1, first submitted 2026-10-19) gives general exposed-face criteria for finite convexification, including a planar finiteness test. The present theorem is compatible with those criteria but adds the **exact threshold**, its attained endpoint, and a symmetry-based interior-versus-facet formula for every rotationally symmetric convexifier. Neither the displayed formula nor the two-polygon arithmetic classification is asserted in the examined source.

Artstein-Avidan, Falah, and Slomka's *Vertex generated polytopes* (arXiv:2407.20604v1) investigates the case where the convexifier is the convex hull of the vertex set. Its general simplex bound and its result that zonotopes are vertex generated cover parts of the \(m=n\) subfamily, but not the mixed case \(K\ne P_n\) or the facet-normal rotational obstruction. The 2018 Fradelizi–Madiman–Marsiglietti–Zvavitch survey supplies background on Schneider's index and finite/nonfinite convexification, not the mixed regular-polygon phase diagram. Relevant published mathematical records concerning simplex-skeleton convexification and geometric invariants of regular polygons have different mathematical objects or functionals; no equivalence was identified from the material available.

## Limitations

The exact formula requires the full \(n\)-fold rotational symmetry of the convexifier, not arbitrary asymmetric \(K\) or a nonregular source polygon. It does not solve finite convexification in higher dimensions. The theorem uses a precise support-segment condition; convergence of smooth approximations does not preserve the finite threshold. Historic priority remains subject to further specialist verification, especially older results on finite unions of polygon translates and vertex-generated polytopes. No independent audit has been performed.

## References

1. M. Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (2026-10-19), https://arxiv.org/abs/2610.26744.
2. S. Artstein-Avidan, T. Falah, B. A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1 (2024-07-30), https://arxiv.org/abs/2407.20604.
3. M. Fradelizi, M. Madiman, A. Marsiglietti, A. Zvavitch, *The convexification effect of Minkowski summation*, EMS Surv. Math. Sci. 5 (2018), 1–64, https://doi.org/10.4171/EMSS/26.
