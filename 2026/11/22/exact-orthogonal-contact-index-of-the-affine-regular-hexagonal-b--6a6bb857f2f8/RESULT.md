# Exact orthogonal-contact index of the affine-regular hexagonal Banach plane

## Finding

Let \(G\) be the real normed plane with
\[
\|(x,y)\|_G=\max\{|x|,|y|,|x+y|\}.
\]
For a real two-dimensional Banach space \(E\), define the Hilbert orthogonal-contact index
\[
\omega_\perp(E)=\max\Bigl\{\min\{\|Qu\|_2,\|Qv\|_2\}:\ Q:E\longrightarrow\mathbb R^2,\ \|Q\|\le 1,\ u,v\in S_E,\ \langle Qu,Qv\rangle=0\Bigr\}.
\]
Then
\[
\boxed{\omega_\perp(G)=\frac{3-\sqrt3}{\sqrt2}=\sqrt{6-3\sqrt3}.}
\]
The maximum is attained explicitly. Put \(\tau=2-\sqrt3\), let \(u=(1,-\tau)\), \(v=(-\tau,1)\), let \(S:\mathbb R^2\to G\) have these vectors as its two columns, and put
\[
K=\|S^{-1}:G\to\ell_2^2\|=\frac{\sqrt{1+\tau^2}}{1-\tau^2},\qquad Q=K^{-1}S^{-1}.
\]
Then \(u,v\in S_G\), \(\|Q\|=1\), \(Qu=K^{-1}e_1\), \(Qv=K^{-1}e_2\), and \(K^{-1}=(3-\sqrt3)/\sqrt2\). In particular, the orthogonal-contact property \(\omega_\perp(G)=1\) fails by an exact, strictly positive amount.

## Assumptions and scope

All vectors, norms, and operators are over the **real** field. The target is Euclidean \(\mathbb R^2\), as in the two-dimensional specialization of the orthogonal-contact definition introduced in Zhang--Xu--Liu--Li (2026, equation (7)). No assertion is made about complexification, arbitrary hexagonal norms, or the value of a von Neumann--Jordan tensor constant. This is the exact value of the *Hilbert orthogonal-contact index*, a distinct geometric invariant.

## Proof

**Step 1: a factorization formula.** The unit ball of \(G\) is the hexagon whose vertices are \(\pm e_1\), \(\pm e_2\), and \(\pm(e_1-e_2)\). If \(S\) is a real invertible two-by-two matrix with columns \(u,v\in B_G\), set
\[
\rho(S)=\frac{1}{\|S^{-1}:G\to\ell_2^2\|}.
\]
The contraction \(Q=\rho(S)S^{-1}\) sends the two columns to perpendicular vectors of equal Euclidean length \(\rho(S)\). Scaling either column outward to the unit sphere cannot decrease \(\rho(S)\): with the other column fixed, the numerator in the formula below grows linearly in the scaling variable, whereas every denominator term is the Euclidean norm of a vector with only one coordinate scaled. Thus the supremum of \(\rho(S)\) over independent unit-ball columns is attained using columns on \(S_G\).

Conversely, let \(Q\) be a contraction and let \(u,v\in S_G\) have nonzero perpendicular images with lengths \(a,b\). Expressing the target in the orthonormal basis given by the image directions and setting \(S=[(r/a)u\ \ (r/b)v]\), where \(r=\min\{a,b\}\), gives \(S\) with columns in \(B_G\) and \(Q S=rI\). Consequently \(r\le\rho(S)\). The zero-image cases do not affect the maximum because a positive example exists. Hence
\[
\omega_\perp(G)=\max_{u,v\in S_G\,\text{independent}}\rho([u\ v]).
\]
If \(u=(u_1,u_2)\), \(v=(v_1,v_2)\), evaluation of \(S^{-1}\) at the six vertices gives the exact formula
\[
\rho([u\ v])=
\frac{|u_1v_2-u_2v_1|}
{\max\!\left\{\sqrt{u_1^2+v_1^2},\ \sqrt{u_2^2+v_2^2},\ \sqrt{(u_1+u_2)^2+(v_1+v_2)^2}\right\}}.
\tag{1}
\]

**Step 2: reduce to two edge configurations.** The linear isometry \(R(x,y)=(-y,x+y)\), together with reflection, acts transitively on the six edges of \(B_G\). We may therefore take \(u=(1,-s)\), \(0\le s\le1\). Replacing \(v\) by \(-v\) leaves (1) unchanged. Thus its possible edge locations reduce to
\[
v=(1,-t),\quad v=(t,1-t),\quad\text{or}\quad v=(-t,1),\qquad 0\le t\le1.
\]
The middle configuration is equivalent to the last: the isometry \(F(x,y)=(x,-x-y)\) takes \(u\) to \((1,-(1-s))\) and \(v=(t,1-t)\) to \((t,-1)\), whose negative is \((-t,1)\). The first (same-edge) configuration gives \(|\det[u\ v]|=|s-t|\le1\), while the first denominator term of (1) is \(\sqrt2\); hence \(\rho\le1/\sqrt2\).

It remains to maximize the last configuration. There (1) becomes
\[
F(s,t)=\frac{1-st}{\max\left\{\sqrt{1+s^2},\sqrt{1+t^2},\sqrt{(1-s)^2+(1-t)^2}\right\}},\qquad 0\le s,t\le1.
\tag{2}
\]
By symmetry assume \(0\le s\le t\le1\), and put \(A(t)=\sqrt{1+t^2}\), \(B(s,t)=\sqrt{(1-s)^2+(1-t)^2}\). The first square-root in (2) is at most \(A(t)\). For fixed \(t\), \((1-st)/A(t)\) is nonincreasing in \(s\), whereas
\[
\frac{\partial}{\partial s}\frac{1-st}{B(s,t)}
=\frac{(1-t)(1-s-t+t^2)}{B(s,t)^3}\ge0,
\]
because \(s\le t\) implies \(1-s-t+t^2\ge(1-t)^2\). Thus the best \(s\) is at the transition \(A=B\), if it lies in the allowed interval, or at an endpoint.

**Step 3: solve all three parameter regimes.** Write \(\tau=2-\sqrt3\), the smaller root of \(t^2-4t+1=0\). The transition \(A=B\) occurs at \(s_c(t)=1-\sqrt{2t}\).

For \(0\le t\le\tau\), one has \(s_c(t)\ge t\) and \(B(s,t)\ge A(t)\) throughout \(0\le s\le t\). By the preceding monotonicity, the maximum is at \(s=t\), where \(F(t,t)=(1+t)/\sqrt2\le(1+\tau)/\sqrt2\).

For \(\tau\le t\le1/2\), one has \(0\le s_c(t)\le t\). The maximum for fixed \(t\) is at \(s=s_c(t)\) and equals
\[
g(t)=\frac{1-t+t\sqrt{2t}}{\sqrt{1+t^2}}.
\]
The sign of \(g'(t)\) is the sign of
\[
h(t)=-1-t+\frac{\sqrt{2t}}2(3+t^2).
\]
On this interval,
\[
h'(t)=-1+\frac{3+t^2}{2\sqrt{2t}}+t\sqrt{2t}>0.
\]
Thus \(g'\) has at most one zero and, if it exists, is negative before and positive after it. Therefore the maximum of \(g\) is at an endpoint. These values are \(g(\tau)=(1+\tau)/\sqrt2\) and \(g(1/2)=2/\sqrt5\). The former is larger because
\[
\frac{(1+\tau)^2}{2}-\frac45=\frac{26-15\sqrt3}{5}>0,
\]
with the final strict inequality following from \(26^2>3\cdot15^2\).

For \(1/2\le t\le1\), one has \(s_c(t)\le0\), so \(B(s,t)\le A(t)\) for every allowed \(s\). The maximum occurs at \(s=0\) and is \(1/\sqrt{1+t^2}\le2/\sqrt5\). The same-edge bound \(1/\sqrt2\) is smaller too. Thus the global maximum of (2) is
\[
\frac{1+\tau}{\sqrt2}=\frac{3-\sqrt3}{\sqrt2}.
\]
At \(s=t=\tau\), \(A=B\) because \(1+\tau^2=2(1-\tau)^2\). The explicit operator in the finding attains the maximum. This completes the proof.

## Verification

The proof above is symbolic and covers all real contractions and sphere pairs, including edge endpoints. The accompanying standalone script `check_hexagonal_contact.py` verifies the exact algebraic identities, the explicit extremal matrix, invariance under the stated hexagonal isometries, and a reproducible finite randomized check of (1)--(2) and the proved upper bound. Finite sampling is auxiliary and is not a substitute for the all-parameter analytic maximization.

## Relationship to prior work

Zhang, Xu, Liu and Li (2026) define \(\omega_\perp(E)\) in their equation (7) and, in Example 3.12, show \(\omega_\perp(H_6)<1\) for their affine-regular hexagonal plane, by ruling out two orthogonal *unit* Hilbert contacts. The affine-regular hexagon used there is linearly isometric to \(G\). Their result does not give a numerical maximum below one or an extremizing contraction; the present calculation determines both.

Related published or publicly indexed exact constants for the affine-regular hexagon concern different functionals: Euclidean Banach--Mazur distortion, James/Schäffer orthogonality, and the von Neumann--Jordan constant of a Hilbert--hexagon tensor product. In particular, the known tensor identity \(C_{\mathrm{NJ}}=1+\sqrt3/2\), together with the one-sided comparison \(C_{\mathrm{NJ}}\ge2\omega_\perp^2\), gives only \(\omega_\perp\le\sqrt{(2+\sqrt3)/4}\), strictly larger than the value proved here. That tensor identity therefore does not itself determine the contact index. The known Euclidean distortion \(2/\sqrt3\) likewise supplies a weaker lower estimate \(\sqrt3/2\), not the exact index. The classical geometric ingredients are not claimed to be new.

## Limitations

The result is confined to the real affine-regular hexagonal plane and the orthogonal-contact invariant defined above. It does not classify all operators attaining the maximum, does not calculate other hexagonal families, and does not improve the already-known exact tensor von Neumann--Jordan constant. Equivalence with an unindexed prior computation cannot be ruled out by search alone. The verification is an analytic self-review supported by supplementary finite checks, not an independent mathematical audit.

## References

1. W. Zhang, Y. Xu, Q. Liu and Y. Li, *Von Neumann--Jordan Constants in Banach Tensor Products*, arXiv:2609.37503, first public 27 September 2026; especially equation (7), Theorem 3.11, Example 3.12. https://arxiv.org/abs/2609.37503
2. *Exact von Neumann--Jordan constant of Hilbert--hexagon tensor products*, publicly indexed mathematical research record dated 1 November 2026 (comparison source; its theorem concerns a distinct invariant).
3. *Euclidean Banach--Mazur profile of a classical hexagonal family*, publicly indexed mathematical research record dated 4 October 2026 (comparison source; its theorem concerns Euclidean distortion).
