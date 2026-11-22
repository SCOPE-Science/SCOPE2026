# Three exceptional stable fibers of a Chebyshev pencil on the Cayley cubic

## Finding

For each integer \(n\geq2\), let \(T_n\) be the first-kind Chebyshev polynomial, characterized by \(T_n(\cos\theta)=\cos(n\theta)\), and consider the affine Cayley cubic surface
\[
S:\quad x^2+y^2+z^2-2xyz-1=0
\]
with regular function \(f_n=y-T_n(x)\). The fiber \(f_n^{-1}(\lambda)\) is an intersection with the shifted Chebyshev cylinder \(y=T_n(x)+\lambda\). Give the fibers their natural proper double-cover compactification described below, denoted \(C_{n,\lambda}\).

**Theorem.** The curves \(C_{n,\lambda}\) form a proper flat family of connected stable curves of arithmetic genus \(n\) over \(\mathbb A^1_{\mathbb C}\), with precisely three singular parameter values \(\lambda=0,2,-2\). All geometric singularities in all fibers are ordinary nodes. The zero fiber is the union of two smooth rational curves intersecting transversely in exactly \(n+1\) points, with dual graph consisting of two vertices and \(n+1\) connecting edges. At the other exceptional values the fibers are integral, and the counts \(\delta\) of nodes and their normalization genera \(g_{\mathrm{norm}}\) are

| Parity and parameter | \(\delta\) | \(g_{\mathrm{norm}}\) |
| --- | ---: | ---: |
| \(n=2k\), \(\lambda=2\) | \(k\) | \(k\) |
| \(n=2k\), \(\lambda=-2\) | \(k+1\) | \(k-1\) |
| \(n=2k+1\), \(\lambda=2\) | \(k+1\) | \(k\) |
| \(n=2k+1\), \(\lambda=-2\) | \(k+1\) | \(k\) |

Writing \(F_n(x,\lambda)=(x^2-1)((T_n(x)+\lambda)^2-1)\), its polynomial discriminant satisfies, for nonzero constants \(c_n\in\mathbb C\),
\[
\operatorname{Disc}_x F_{2k}=c_{2k}\lambda^{2k+3}(\lambda-2)^k(\lambda+2)^{k+3},
\]
\[
\operatorname{Disc}_x F_{2k+1}=c_{2k+1}\lambda^{2k+4}(\lambda^2-4)^{k+2}.
\]
The total space has exactly four ordinary quadratic surface singularities, located over the four nodes of \(S\), and its compactification adds no singularities at infinity. The connected generalized Jacobian of \(C_{n,0}\) is the split torus \((\mathbb G_m)^n\).

## Assumptions and scope

The ground field is \(\mathbb C\), all curves are geometric, and \(n\ge2\) is arbitrary. The base is the affine parameter line; **no assertion is made about the fiber over \(\lambda=\infty\)** after compactifying the base. The stable curve compactification is defined by two affine charts: on the finite \(x\)-chart set
\[
w=z-x(T_n(x)+\lambda),\qquad w^2=F_n(x,\lambda);
\]
on the infinity chart put \(u=1/x\), \(v=u^{n+1}w\), and
\[
v^2=u^{2n+2}F_n(1/u,\lambda).
\]
Glue by \(u=1/x\), \(v=u^{n+1}w\). The leading coefficient of \(F_n\) is \(2^{2n-2}\), independent of \(\lambda\), so the two points over infinity are disjoint smooth sections \(v=\pm2^{n-1}\) at \(u=0\). The construction gives a finite flat double cover of \(\mathbb P^1\times\mathbb A^1\), hence a proper flat family over the parameter line.

## Proof

**1. Genus, fibers, and singular values.** Completing the square in the Cayley equation after imposing \(y=T_n(x)+\lambda\) gives the stated hyperelliptic equation. The polynomial \(F_n\) has degree \(2n+2\) and no repeated roots for generic \(\lambda\), so Riemann–Hurwitz gives genus \(n\). Flatness keeps arithmetic genus \(n\) in all fibers. The Chebyshev identity
\[
T_n(x)^2-1=(x^2-1)U_{n-1}(x)^2
\]
uses the second-kind polynomial \(U_{n-1}\), whose \(n-1\) roots are simple and distinct from \(\pm1\). The derivative of \(T_n\) is \(nU_{n-1}\), and its critical values alternate between \(+1\) and \(-1\), with all critical points simple. Thus the only possible multiple roots of \(F_n(\cdot,\lambda)\) occur when an endpoint \(x=\pm1\) is also a zero of \(T_n(x)+\lambda\pm1\), or when the latter polynomial takes a root at a critical point of \(T_n\). All such parameters belong to \(\{0,2,-2\}\). Conversely, each of those values does produce repeated roots, so the list is exhaustive. Every repeated root has multiplicity exactly two: at \(\lambda=0\) this follows from the displayed identity; at \(\lambda=\pm2\), the critical points are nondegenerate and at an endpoint the other factors are nonzero. A local equation \(w^2=(x-a)^2h(x)\), with \(h(a)\ne0\), is a node.

**2. Central fiber.** At \(\lambda=0\) one has
\[
w^2=(x^2-1)^2U_{n-1}(x)^2,
\]
so the two components are graphs \(w=\pm(x^2-1)U_{n-1}(x)\), each a rational curve extending smoothly to its own point over infinity. They meet in precisely the \(n+1\) distinct simple zeros of \((x^2-1)U_{n-1}(x)\), hence transversely in \(n+1\) nodes and nowhere else. Each rational component meets the other at at least three points, so the fiber is stable. The dual graph has first Betti number \(n\), so its generalized Jacobian has identity component \((\mathbb G_m)^n\).

**3. The two integral nodal fibers.** The \(n-1\) critical points \(a_j=\cos(j\pi/n)\), \(1\le j\le n-1\), obey \(T_n(a_j)=(-1)^j\). When \(n=2k\), \(k\) critical points have value \(-1\) and \(k-1\) have value \(+1\); when \(n=2k+1\), exactly \(k\) have each sign. At \(\lambda=2\), a repeated root occurs at each critical point of value \(-1\), together with the endpoint \(x=-1\) only when \(n\) is odd. At \(\lambda=-2\), it occurs at each critical point of value \(+1\), together with \(x=1\) always and \(x=-1\) when \(n\) is even. This gives the table of node counts. The factor \(T_n(x)+\lambda\pm1\) whose value corresponds to \(\pm3\) has \(n\) simple roots, because critical values of \(T_n\) are only \(\pm1\). It prevents \(F_n\) from being a square in \(\mathbb C[x]\); hence \(w^2-F_n\) is irreducible at \(\lambda=\pm2\). A nodal integral curve of arithmetic genus \(n\) with \(\delta\) nodes has normalization genus \(n-\delta\). Since \(n\ge2\), these integral nodal curves are stable.

**4. Exact discriminant exponents.** Factor \(F_n=A B C\) with \(A=x^2-1\), \(B=T_n+\lambda-1\), \(C=T_n+\lambda+1\). The product discriminant formula is
\[
\operatorname{Disc}(ABC)=\operatorname{Disc}(A)\operatorname{Disc}(B)\operatorname{Disc}(C)\operatorname{Res}(A,B)^2\operatorname{Res}(A,C)^2\operatorname{Res}(B,C)^2,
\]
up to a nonzero scalar (leading-coefficient conventions do not affect parameter exponents). The last resultant is constant and nonzero since \(B-C=-2\). Because the critical points are simple, \(\operatorname{Disc}(B)\operatorname{Disc}(C)\) is, up to a nonzero scalar,
\[
\begin{cases}
\lambda^{2k-1}(\lambda-2)^k(\lambda+2)^{k-1},&n=2k,\\
\lambda^{2k}(\lambda^2-4)^k,&n=2k+1.
\end{cases}
\]
Evaluating \(B,C\) at \(x=\pm1\) gives
\[
\operatorname{Res}(A,B)^2\operatorname{Res}(A,C)^2=
\begin{cases}
\lambda^4(\lambda+2)^4,&n\text{ even},\\
\lambda^4(\lambda^2-4)^2,&n\text{ odd}.
\end{cases}
\]
Multiplying yields the two stated exact factors.

**5. The fixed four nodes of the total surface.** The equation \(\lambda=y-T_n(x)\) identifies the *affine total space*, not merely its individual fibers, with the Cayley cubic \(S\). Its Jacobian vanishes exactly at the four points \((x,y,z)\in\{\pm1\}^3\) with \(xyz=1\), all ordinary quadratic nodes. Each occurs at its uniquely determined parameter \(\lambda=y-T_n(x)\). The two infinity sections of the chosen compactification are smooth with derivative \(\partial(v^2)/\partial v\ne0\). Thus there are precisely four total-space nodes. This is compatible with all fiber singularities: the remaining fiber nodes occur at smooth points of the total space where the map \(f_n\) is critical.

## Verification

A standalone exact-arithmetic script `check.py` verifies, for degrees \(2\le n\le8\), the stated discriminant factors up to nonzero rational constants, the repeated-root counts at \(0,\pm2\), the squarefreeness of a generic fiber, and the central Chebyshev square identity. Its finite checks do not replace the universal proof above. Execute with Python 3 and SymPy using `python check.py` from a directory containing the script. The two-chart infinity argument and the local node analysis are proved symbolically above, not inferred from numerical tests.

## Relationship to prior work

Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties* (arXiv:2611.15725v1, Section 3, Example 3.2), exhibits the Cayley cubic and the parabolic cylinder \(y=T_2(x)\) and proves that their intersection is the union of two rational Lissajous curves. That result supplies the geometric starting example, **not** the classification of the translated family, its stable compactification, the three exceptional finite parameters, or all-degree discriminant factors. The particular genus-two degeneration into two rational components meeting at three nodes is also documented in a 2017 MathOverflow discussion of a related family; it is not asserted to be newly discovered. The claim here is the *combined uniform classification for the fixed Cayley surface map* \(f_n=y-T_n(x)\), including all exceptional members and four total-space nodes.

## Limitations

Everything is over \(\mathbb C\) and over the affine parameter line. No fiber at parameter infinity, semistable regular total-space resolution, Néron component group, finite-characteristic analogue, or uniqueness in the whole mathematical literature is asserted. The four ordinary double points show the proper total space is **not regular**, although all geometric fibers are stable nodal curves. The classification is a self-review only and has not undergone independent audit. Prior unindexed treatments of Cayley–Chebyshev pencils remain an originality risk.

## References

1. Francesco Maria Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1 (first submitted 11 November 2026), https://arxiv.org/html/2611.15725v1 . See Example 3.2 and Section 5.
2. MathOverflow, *Different stable degenerations of the hyperelliptic curve* (21–22 February 2017), https://mathoverflow.net/questions/262818/different-stable-degenerations-of-the-hyperelliptic-curve-y2-x2x2-12/262831 . Records a related genus-two three-node limit and an explicit two-chart compactification argument.
3. AMS, *MSC2020 classification*: 14D06, fibrations and degenerations in algebraic geometry, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=14Dxx .
