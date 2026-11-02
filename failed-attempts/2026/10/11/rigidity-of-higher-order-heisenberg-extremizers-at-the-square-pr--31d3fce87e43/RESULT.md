# Rigidity of higher-order Heisenberg extremizers at the square-profile level
## Finding
Let \(N\ge2\) and \(m\ge3\). Consider the sharp higher-order Heisenberg inequality of Hu, Liu, and Zou,
\[
\left(\int_{\mathbb R^N}|P_m u|^2\right)
\left(\int_{\mathbb R^N}|x|^2|\nabla^{m-1}u|^2\right)
\ge \mu_m(N)\left(\int_{\mathbb R^N}|P_{m-1}u|^2\right)^2,
\]
where
\[
\mu_m(N)=\left(\frac{2+\sqrt{N^2+4(m-2)(N-1)}}2\right)^2.
\]
Write \(j=\lfloor m/2\rfloor\) and \(v=\Delta^{j-1}u\). For a nondegenerate real extremizer, define
\[
A=\int|P_m u|^2,\qquad
B=\int |x|^2|\nabla^{m-1}u|^2,\qquad
C=\int|P_{m-1}u|^2,
\qquad b=\sqrt{A/B}.
\]
Assume that \(v\) is smooth and lies in the natural square domain of the source proof, defined below. Then the equality conditions completely determine the \(P_{m-2}\)-profile.

If \(m\) is even, then for some \(a\ne0\),
\[
P_{m-2}u(x)=a e^{-b|x|^2/2}{}_1F_1\!\left(
\frac{N-\sqrt{N^2+4(m-2)(N-1)}}4,
\frac N2,
\frac{b|x|^2}{2}
\right).
\]
If \(m\) is odd, then for some \(a\ne0\),
\[
P_{m-2}u(x)=a x e^{-b|x|^2/2}{}_1F_1\!\left(
\frac{N+2-\sqrt{N^2+4(m-2)(N-1)}}4,
\frac{N+2}{2},
\frac{b|x|^2}{2}
\right).
\]
Consequently, within this natural square domain, every equality case is radial at the \(P_{m-2}\)-profile level, and the radial hypergeometric profiles constructed in the focal source exhaust the possible profiles up to scalar multiplication and the positive dilation parameter \(b\).

## Assumptions and scope
The scalar field is real. The claim is restricted to \(N\ge2\), \(m\ge3\), and nondegenerate equality cases with \(A,B,C>0\).

For even \(m\), the square domain is the smooth part of the graph-norm closure of \(C_c^\infty(\mathbb R^N)\) for
\[
\|v\|_2+\|\nabla v\|_2+\|\Delta v\|_2+\||x|\nabla v\|_2.
\]
For odd \(m\), it is the smooth part of the graph-norm closure for
\[
\|\nabla v\|_2+\|\Delta v\|_2+\|\nabla\Delta v\|_2+\||x|\Delta v\|_2.
\]
These domains are exactly strong enough to extend the source square identities from compactly supported smooth functions by cutoff approximation. The claim is a profile classification: it determines \(P_{m-2}u\), not necessarily a preferred representative of \(u\) modulo the null space of the seminorm. For odd \(m\), adding a constant to the scalar potential \(v\) does not change \(P_{m-2}u=\nabla v\).

## Proof
Set
\[
s=\sqrt{N^2+4(m-2)(N-1)}.
\]
First suppose \(m=2j\) is even. The source introduces
\[
\mathcal E_{b,c}(v)=\Delta v+b x\cdot\nabla v+bcv
\]
and chooses
\[
c_e=\frac{N+s}{2},
\]
so that the lower-order coefficient cancels. Its square expansion and the pointwise inequality
\[
(x\cdot\nabla v)^2\le |x|^2|\nabla v|^2
\]
give, after the source tensor identity is inserted,
\[
0\le \|\mathcal E_{b,c_e}v\|_2^2
\le A+b^2B-b(2c_e-N+2)C.
\]
Choose \(b=\sqrt{A/B}\). Equality in the sharp uncertainty principle says
\[
2\sqrt{AB}=(2c_e-N+2)C,
\]
so the right-hand side is zero. Hence both nonnegative losses vanish. In particular,
\[
\mathcal E_{b,c_e}v=0
\]
and
\[
|x|^2|\nabla v|^2-(x\cdot\nabla v)^2=0
\]
almost everywhere. The latter identity is the squared tangential gradient, so smoothness implies that \(v\) is radial.

For a radial \(v=v(r)\), the equation becomes
\[
v''+\left(\frac{N-1}{r}+br\right)v'+bc_e v=0.
\]
A smooth radial solution satisfies \(v'(0)=0\). The regular solution space at the origin is one-dimensional: after fixing \(v(0)\), the divergence-form equation
\[
\left(r^{N-1}e^{br^2/2}v'\right)'=-bc_e r^{N-1}e^{br^2/2}v
\]
has a unique smooth solution. The focal source exhibits the normalized solution
\[
v_e(r)=e^{-br^2/2}{}_1F_1\!\left(\frac{N-c_e}{2},\frac N2,\frac{br^2}{2}\right).
\]
Since
\[
\frac{N-c_e}{2}=\frac{N-s}{4},
\]
we obtain \(v=a v_e\), which is exactly the even formula in the finding.

Now suppose \(m=2j+1\) is odd. The source uses
\[
\mathcal O_{b,c}(v)=\nabla\Delta v+b x\Delta v+bc\nabla v
\]
and
\[
c_o=\frac{2-N+s}{2}>0.
\]
Here the square expansion is an identity. With the same choice \(b=\sqrt{A/B}\), equality in the sharp uncertainty principle forces
\[
\mathcal O_{b,c_o}(v)=0.
\]
Let
\[
w=\Delta v+bc_o v.
\]
Then
\[
\nabla w=-b x\Delta v.
\]
Every tangential derivative of \(w\) therefore vanishes, so \(w\) is radial. Its gradient is radial as well, and the displayed equation then forces \(\Delta v\) to be radial. Because \(bc_o>0\),
\[
v=\frac{w-\Delta v}{bc_o}
\]
is radial.

Write
\[
y(r)=\frac{v'(r)}r,
\]
with the smooth value at \(r=0\) obtained by continuation. Substitution into \(\mathcal O_{b,c_o}(v)=0\) gives
\[
y''+\left(\frac{N+1}{r}+br\right)y'+b(N+c_o)y=0.
\]
Again the smooth solution space at the origin is one-dimensional. The normalized solution furnished by the focal source is
\[
y_o(r)=e^{-br^2/2}{}_1F_1\!\left(\frac{2-c_o}{2},\frac{N+2}{2},\frac{br^2}{2}\right).
\]
Thus \(y=a y_o\), and hence
\[
\nabla v=a x y_o(r).
\]
Since
\[
\frac{2-c_o}{2}=\frac{N+2-s}{4},
\]
this is exactly the odd formula. The additive constant left undetermined in \(v\) disappears under \(\nabla v=P_{m-2}u\).

## Verification
The argument uses only exact identities. The parity parameters were algebraically checked:
\[
\frac{N-c_e}{2}=\frac{N-s}{4},\qquad
\frac{2-c_o}{2}=\frac{N+2-s}{4}.
\]
For the odd case, direct differentiation of \(v'=r y\) gives
\[
\mathcal O_{b,c_o}(v)=\frac{x}{r}\,r\left[y''+\left(\frac{N+1}{r}+br\right)y'+b(N+c_o)y\right],
\]
which confirms the reduced radial equation. No finite experiment or numerical approximation is used as proof.

The focal source itself proves the necessary decay and cutoff estimates for its profiles, including convergence of the square errors under cutoff. Those estimates show that the published profiles lie in the intended limiting square framework. The classification here is intentionally not extended to arbitrary abstract elements of the seminorm completion for which a smooth square-domain representative is unavailable.

## Relationship to prior work
Hu--Liu--Zou prove the sharp constant for every order and construct some radial extremizers by solving \(\mathcal E_b(v)=0\) and \(\mathcal O_b(v)=0\). Their Theorem 1.2 is stated as an existence result: the constant is attained by some radially symmetric \(\Phi_{b,m}\). Their Section 4 constructs radial solutions but does not classify all equality cases. The proof of Theorem 1.1 contains the additional rigidity information used here: for even order, equality must also saturate the radial Cauchy step; for odd order, the vector equation itself forces radiality.

Recent Fourier work of Do--Lam--Lu--Nguyen characterizes optimizers for two fractional Heisenberg families and develops the second-order Heisenberg stability theory. Its public abstract identifies the second-order inequality and fractional-Laplacian families, not the \(m\ge3\) full-tensor \(P_m\) inequality treated here. Earlier second-order stability work likewise concerns \(m=2\). The present statement is therefore an equality classification for the genuinely higher-order family introduced by the focal source, within the explicit square domain above.

## Limitations
The theorem does not assert a classification for every abstract element of \(\mathcal H^m\) without a smooth square-domain representative. It does not prove a quantitative stability estimate, a spectral gap around the extremizer manifold, or uniqueness of a representative \(u\) modulo the seminorm null space. It also excludes \(m=2\), where Gaussian optimizer and stability theory are already developed in the literature.

A related September 2026 preprint on Fourier methods was inspected through its public abstract; its full text was not available for inspection. The abstract describes different fractional families and second-order stability, so it is not an implication-level cover of the present \(m\ge3\) full-tensor profile classification, but the incomplete full-text comparison remains a literature risk.

## References
1. H. Hu, M. Liu, W. Zou, *Sharp higher-order uncertainty principles*, arXiv:2610.01561v1, first posted 2026-10-01.
2. A. Do, N. Lam, G. Lu, V. H. Nguyen, *A Fourier approach to the sharp stability of Heisenberg Uncertainty Principles of higher and fractional orders: a new perspective*, arXiv:2609.31949v1, first posted 2026-09-25.
3. A. X. Do, N. Lam, G. Lu, *Sharp stability of the Heisenberg Uncertainty Principle: Second-Order and Curl-Free Field Cases*, arXiv:2505.02758v1, first posted 2025-05-05.
