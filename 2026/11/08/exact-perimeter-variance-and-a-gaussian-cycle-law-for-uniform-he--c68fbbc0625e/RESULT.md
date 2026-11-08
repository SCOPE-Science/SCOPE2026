# Exact perimeter variance and a Gaussian cycle law for uniform hemisphere vertices

## Finding

Let \(H=\{x\in S^2:x_3\geq0\}\) carry normalized spherical area. For each integer \(n\geq3\), choose independent uniform points \(X_1,\ldots,X_n\in H\), set \(X_{n+1}=X_1\), and define the perimeter of the geodesic cycle by
\[
L_n=\sum_{i=1}^n \arccos\langle X_i,X_{i+1}\rangle.
\]
The minimizing great-circle arcs are unique almost surely. For \(n=3\), this is the usual perimeter of the spherical convex-hull triangle; for \(n>3\) the cyclic polygon need not be simple or convex.

Put \(c_k=\binom{2k}{k}/4^k\) and
\[
S=\sum_{k=0}^\infty\frac{(4k+3)c_k^6}{(k+1)^6},\qquad
\gamma=\frac{\pi^2}{256}S-\left(\frac\pi2-\frac4\pi\right)^2.
\]
Then for **every** integer \(n\geq3\),
\[
\boxed{\ \mathbb E L_n=\frac{4n}\pi,\quad
\operatorname{Var}(L_n)=n\sigma_H^2,\quad
\sigma_H^2=2-\frac{16}{\pi^2}+2\gamma.\ }
\]
The constants have the approximations \(\gamma=0.0271870496201176\ldots>0\), \(\sigma_H^2=0.433235160962831\ldots\). In particular, the genuine random spherical triangle has
\[
\operatorname{Var}(L_3)=1.29970548288849\ldots,
\]
and its three geodesic sides are positively correlated pairwise, with covariance \(\gamma\). As \(n\to\infty\),
\[
\boxed{\ \frac{L_n-4n/\pi}{\sqrt n}\ \Longrightarrow\ N(0,\sigma_H^2).\ }
\]
The explicit series has a deterministic truncation certificate: for any integer \(N\geq1\),
\[
0<S-\sum_{k=0}^{N-1}\frac{(4k+3)c_k^6}{(k+1)^6}<\frac{4}{7N^7}.
\]
Thus the exact variance rate is directly computable with an a priori error bound.

## Assumptions and scope

The sphere has radius one; distances are intrinsic shorter great-circle distances in radians. All vertices are independent and area-uniform on the **same closed hemisphere**. Boundary and antipodal degeneracies have probability zero. The statement concerns geodesic cycles in their given random label order, not shortest tours or convex-hull boundary length for \(n\geq4\). No conclusion is claimed for nonuniform cap distributions, arbitrary dimensions, or general manifolds. The asserted Gaussian convergence is weak convergence, not a finite-sample normal approximation.

## Proof

**1. The exact one-edge law.** Let \(A=\arccos\langle X,Y\rangle\), with independent uniform \(X,Y\in H\). For independently uniform full-sphere points, the distance \(A\) has density \(\tfrac12\sin a\) on \((0,\pi)\). Conditional on a fixed separation \(a\), a uniformly oriented equatorial great circle separates the pair with probability \(a/\pi\). Rotational symmetry then gives \(\Pr(X,Y\in H\mid A=a)=(1-a/\pi)/2\). As \(\Pr(X,Y\in H)=1/4\), conditioning gives the exact hemisphere density
\[
f_A(a)=(1-a/\pi)\sin a,\qquad 0<a<\pi.
\]
Direct integration yields
\[
\mathbb E A=4/\pi,\qquad \mathbb E A^2=2,\qquad
v:=\operatorname{Var}(A)=2-16/\pi^2>0.
\]

**2. The common-vertex covariance.** Define \(m(x)=\mathbb E[\arccos\langle x,Y\rangle]\), where \(Y\) is an independent uniform point of \(H\). For independent \(Y,Z\), conditioning on \(X\) yields
\[
\operatorname{Cov}(\arccos\langle X,Y\rangle,\arccos\langle X,Z\rangle)
=\operatorname{Var}(m(X)).
\]
Write \(z=x_3\). Since the latitude height of a uniform hemisphere point is uniform on \([0,1]\), the last variance is a one-dimensional integral in \(z\).

Let \(P_j\) be the degree-\(j\) Legendre polynomial normalized by \(P_j(1)=1\), and set \(c_k=\binom{2k}{k}/4^k\). The Legendre expansion of spherical geodesic distance is
\[
\arccos t=\frac\pi2-\sum_{k=0}^\infty b_kP_{2k+1}(t),\qquad
b_k=\frac\pi2(c_k^2-c_{k+1}^2)
=\frac\pi8\frac{(4k+3)c_k^2}{(k+1)^2}.
\]
To verify the coefficients, use the Legendre antiderivative
\((2j+1)P_j=P_{j+1}'-P_{j-1}'\), integrate by parts, and use
\(\int_{-1}^1P_{2k}(t)(1-t^2)^{-1/2}dt=\pi c_k^2\). The even-degree coefficients vanish by oddness about \(t=0\); the constant term is \(\pi/2\). The bounds \(c_k\leq(k+1)^{-1/2}\) and \(|P_j(t)|\leq1\) prove absolute uniform convergence.

By the spherical addition theorem and axial symmetry of the hemisphere,
\[
\mathbb E_Y[P_{2k+1}(\langle x,Y\rangle)]=q_kP_{2k+1}(z),\qquad
q_k=\int_0^1P_{2k+1}(u)du
=(-1)^k\frac{c_k}{2(k+1)}.
\]
Indeed, integrate the Legendre antiderivative from \(0\) to \(1\) and substitute \(P_{2k}(0)=(-1)^kc_k\). Consequently
\[
m(z)=\frac\pi2-\sum_{k=0}^\infty b_kq_kP_{2k+1}(z).
\]
The odd-degree Legendre polynomials are orthogonal on \([0,1]\), with
\(\int_0^1P_{2k+1}(z)^2dz=1/(4k+3)\). Parseval therefore gives
\[
\int_0^1[m(z)-\pi/2]^2dz
=\sum_{k=0}^\infty\frac{b_k^2q_k^2}{4k+3}
=\frac{\pi^2}{256}\sum_{k=0}^\infty\frac{(4k+3)c_k^6}{(k+1)^6}.
\]
Since \(\int_0^1m(z)dz=\mathbb E A=4/\pi\), subtraction of the squared mean shift proves \(\operatorname{Var}(m(X))=\gamma\) exactly. Moreover, \(m(0)=\pi/2\) and \(m(1)=1\) by direct axial symmetry/integration, so \(m\) is not almost everywhere constant and \(\gamma>0\) strictly.

**3. All finite cycles.** Edges with disjoint endpoint sets are independent. Every pair of distinct edges sharing exactly one endpoint has covariance \(\gamma\), independent of positions by exchangeability. A simple cycle with \(n\geq3\) edges has exactly \(n\) unordered adjacent edge pairs, including the triangle case. Summing diagonal and off-diagonal covariances gives
\(\operatorname{Var}(L_n)=nv+2n\gamma=n\sigma_H^2\), while linearity gives \(\mathbb E L_n=4n/\pi\).

**4. Gaussian limit.** On an infinite iid vertex sequence, put \(Z_i=\arccos\langle X_i,X_{i+1}\rangle-4/\pi\). This is a bounded, strictly stationary, one-dependent sequence. Its long-run variance is \(v+2\gamma>0\). The classical central limit theorem for stationary one-dependent sequences gives \(n^{-1/2}\sum_{i=1}^n Z_i\Rightarrow N(0,\sigma_H^2)\). Closing the chain changes the sum by replacing one edge with another, a bounded difference of absolute value at most \(\pi\); Slutsky's lemma yields the displayed cyclic limit.

**5. Truncation error.** The central-binomial recurrence \(c_{k+1}/c_k=(2k+1)/(2k+2)\) and induction give \(c_k\leq1/\sqrt{k+1}\), because \((2k+1)^2(k+2)\leq4(k+1)^3\). For the tail from \(k=N\),
\[
0<\sum_{k=N}^\infty\frac{(4k+3)c_k^6}{(k+1)^6}
\leq4\sum_{k=N}^\infty(k+1)^{-8}<\frac4{7N^7}.
\]
The variance-rate error after \(N\) terms is therefore below \(\pi^2/(224N^7)\).

## Verification

The standalone `checker.py` recomputes the series through \(N=32\) terms with its deterministic error bound, then simulates independent area-uniform hemisphere vertices to check one-edge moments, adjacent-edge covariance, triangular perimeter variance and five-edge cyclic variance. The finite simulation is a consistency check and is not a proof. Its reproducible seed is fixed in the checker. The exact probability density, Legendre coefficient identities, norm identities and combinatorial covariance count constitute the proof.

## Relationship to prior work

Bárány, Hug, Reitzner and Schneider (first public preprint 2015-05-18) analyze convex hulls of uniform hemisphere points; their Theorem 5.1 gives an exact **first** perimeter moment, and for three points it gives the mean \(12/\pi\). The open-access full text was searched for second-moment claims and its introduction, Sections 3–6 and theorem statements were examined. The paper does not state the perimeter variance, the binomial-series constant, or the positive shared-vertex covariance. These are the specific additional statements here. The one-dependent CLT is a standard probabilistic implication once that covariance is evaluated; its general method is not claimed as new.

Le (1989) discusses shape densities for random spherical triangles sampled from a cap. Its available abstract does not settle whether a transformed shape-density identity could cover the present exact perimeter variance; this is an explicit residual priority risk. Neither a broad failed search nor distinct titles alone establish uniqueness. No published claim of independent validation is made.

## Limitations

The geometric object is the label-ordered geodesic cycle for \(n\geq4\); it may self-intersect and is not necessarily the spherical convex hull. The series is exact and rapidly convergent but is not asserted to have an elementary closed form. The numerical value is not an independently certified external calculation. The proof is self-contained apart from standard Legendre identities and the classical one-dependent central limit theorem. A complete historical survey of inaccessible older cap-triangle literature is not asserted.

## References

1. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1, publicly submitted 2015-05-18; Theorem 5.1 and Sections 3–6. https://arxiv.org/abs/1505.04672. Open-access 2015 version: https://discovery.ucl.ac.uk/id/eprint/1503478/1/1505.04672v1.pdf.
2. H. Le, *Random spherical triangles II: Shape densities*, Advances in Applied Probability 21 (1989), 581–594, DOI 10.2307/1427637 (abstract available; complete material not inspected).
3. Standard Legendre polynomial orthogonality, addition theorem and Rodrigues/recurrence identities; standard central limit theorem for bounded stationary one-dependent sequences (classical tools, not new results).
