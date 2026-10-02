# Isolated points are exactly the boundary for point-mass isotropy restriction

## Statement

Let \(\mathcal G\) be a Hausdorff ample groupoid, let \(R\) be a nonzero commutative ring with identity, let \(A=A_R(\mathcal G)\) be its Steinberg algebra, and fix \(x\in\mathcal G^{(0)}\). Write
\[
\mathcal G_x^x=\{\gamma\in\mathcal G:r(\gamma)=s(\gamma)=x\}.
\]

### Theorem 1: point masses exist exactly at isolated units

The following are equivalent:

1. \(x\) is isolated in \(\mathcal G^{(0)}\);
2. \(1_{\{x\}}\in A\);
3. \(1_{\{\gamma\}}\in A\) for some \(\gamma\in\mathcal G_x^x\);
4. \(1_{\{\gamma\}}\in A\) for every \(\gamma\in\mathcal G_x^x\).

Consequently, the canonical point-mass formula
\[
R[\mathcal G_x^x]\longrightarrow A_R(\mathcal G),
\qquad
\delta_\gamma\longmapsto 1_{\{\gamma\}},
\]
is a well-defined algebra embedding if and only if \(x\) is isolated.

If these conditions hold and \(e_x=1_{\{x\}}\), then
\[
\boxed{e_xAe_x\cong R[\mathcal G_x^x]}
\]
via point masses, and
\[
\boxed{Ae_x\cong R L_x,\qquad L_x:=s^{-1}(x),}
\]
as \(A\)-\(R[\mathcal G_x^x]\) bimodules. Thus at isolated units the standard Steinberg induction bimodule is literally the point-idempotent corner bimodule.

### Proof

Suppose \(1_{\{\gamma\}}\in A\) for some \(\gamma\in\mathcal G_x^x\). Since \(R\neq0\), local constancy at \(\gamma\) gives an open neighbourhood on which the function equals \(1\); because its support is the singleton \(\{\gamma\}\), the singleton itself is open. The source map of an étale groupoid is a local homeomorphism, hence open, so
\[
\{x\}=s(\{\gamma\})
\]
is open. Thus \(x\) is isolated. The case \(\gamma=x\) gives \(2\Rightarrow1\).

Conversely, assume \(\{x\}\) is open. Let \(\gamma\in\mathcal G_x^x\), and choose a compact open bisection \(B\) containing \(\gamma\). Then
\[
B\cap s^{-1}(\{x\})=\{\gamma\}.
\]
This is an open singleton; in a Hausdorff groupoid it is also closed, and a singleton is compact. Hence it is a compact open bisection and \(1_{\{\gamma\}}\in A\). This gives \(1\Rightarrow4\), while \(4\Rightarrow3\) is immediate.

Now assume \(x\) is isolated. Multiplication by \(e_x\) on the left and right restricts support to arrows with range and source \(x\). Every arrow in \(\mathcal G_x^x\) is isolated by the preceding argument. Therefore a compactly supported locally constant function supported on \(\mathcal G_x^x\) has finite support, so
\[
e_xAe_x=\bigoplus_{\gamma\in\mathcal G_x^x}R\,1_{\{\gamma\}},
\]
with convolution equal to the group law. This is \(R[\mathcal G_x^x]\).

Similarly, \(Ae_x\) consists exactly of finite-support functions on \(L_x=s^{-1}(x)\), because every element of \(L_x\) is isolated once \(x\) is isolated. Hence \(Ae_x\) identifies with the free \(R\)-module \(RL_x\), and convolution gives the standard left \(A\)-action and right isotropy action. \(\square\)

## Correction to arXiv:2609.20230v1

Nguyen's arXiv:2609.20230v1 identifies \(KP_R(\Lambda)\) with the Steinberg algebra \(A_R(\mathcal G_\Lambda)\) and, for every infinite path \(x\), defines
\[
\iota_x(u^p)=1_{\{(x,p,x)\}}
\]
as an embedding of \(R[\mathcal G_{\Lambda,x}]\) into \(A_R(\mathcal G_\Lambda)\) (Equation (4.1), Proposition 4.1). Definition 4.2 then defines restriction of scalars along this map and induction by
\[
KP_R(\Lambda)\otimes_{R[\mathcal G_{\Lambda,x}]}-.
\]

Theorem 1 shows that this construction is valid exactly when \(x\) is isolated in \(\Lambda^\infty\). For a general row-finite \(k\)-graph with no sources, boundary-path points need not be isolated, so the point-mass functions in (4.1) need not belong to the Steinberg algebra at all.

### Minimal counterexample

Let \(E\) be the directed graph with one vertex and two loops \(a,b\). It satisfies the source paper's row-finite/no-sources hypotheses. Its infinite path space is
\[
E^\infty=\{a,b\}^{\mathbb N},
\]
a Cantor space, so no point is isolated.

Take the periodic path
\[
x=a^\infty.
\]
Then \(\operatorname{Per}(x)\cong\mathbb Z\), but
\[
1_{\{(x,0,x)\}}\notin A_R(\mathcal G_E),
\]
already because the unit singleton \(\{x\}\) is not open. Hence the map in Equation (4.1) is not well-defined for this allowed example. The same applies to every claimed point mass \(1_{\{(x,n,x)\}}\).

Thus Proposition 4.1 and the subsequent restriction-of-scalars construction are false as stated for arbitrary \(x\). This does not invalidate standard Steinberg isotropy induction: the established construction uses the bimodule \(RL_x\), \(L_x=s^{-1}(x)\), and does not require point masses at nonisolated units.

## Sharp repair at isolated paths

When \(x\) is isolated, Theorem 1 gives
\[
R[\mathcal G_{\Lambda,x}]\cong e_x A_R(\mathcal G_\Lambda)e_x
\]
and
\[
A_R(\mathcal G_\Lambda)e_x\cong RL_x.
\]
Accordingly, the ordinary corner functors
\[
M\longmapsto e_xM,
\qquad
W\longmapsto A_R(\mathcal G_\Lambda)e_x\otimes_{e_xAe_x}W
\]
recover the point-mass restriction and standard isotropy induction at precisely those paths.

For nonisolated \(x\), there is no point idempotent \(e_x=1_{\{x\}}\) in the Steinberg algebra and no restriction-of-scalars functor arising from the point-mass formula. General isotropy induction/restriction must instead use the standard groupoid-fiber machinery.

## A finite-dimensional graded obstruction

There is an additional sharp consequence in the \(k\)-graph setting.

### Theorem 2

Let \(\Lambda\) be a row-finite \(k\)-graph with no sources, \(x\in\Lambda^\infty\) an isolated path, and
\[
M=\bigoplus_{g\in\mathbb Z^k}M_g
\]
a finite-dimensional graded \(KP_R(\Lambda)\)-module. If
\[
e_xM\neq0,
\]
then
\[
\boxed{\operatorname{Per}(x)=0.}
\]

### Proof

Suppose \(0\neq p\in\operatorname{Per}(x)\). Since \(x\) is isolated, the isotropy point mass
\[
u_p:=1_{\{(x,p,x)\}}\in e_xAe_x
\]
exists and is homogeneous of degree \(p\). It is invertible in the corner, with inverse \(u_{-p}\).

Because \(e_x\) has degree \(0\), \(e_xM\) is a graded subspace. Choose a nonzero homogeneous \(m\in e_xM\), say \(m\in M_g\). For every \(n\in\mathbb Z\),
\[
u_p^n m\neq0
\]
because \(u_p\) is invertible on \(e_xM\), and
\[
u_p^n m\in M_{g+np}.
\]
The degrees \(g+np\) are pairwise distinct since \(p\neq0\). Therefore \(M\) contains infinitely many nonzero homogeneous components, contradicting finite dimensionality. Hence \(\operatorname{Per}(x)=0\). \(\square\)

This exposes a second boundary in the source paper's Section 4. Its Corollary 4.8 treats finite-dimensional graded modules together with nontrivial Laurent-polynomial isotropy. Under the corrected point-corner interpretation, a nonzero finite-dimensional graded fiber at an isolated path cannot have nontrivial periodicity at all.

In particular, the one-loop example used there has a unique infinite path \(x\), hence \(x\) is isolated and \(\operatorname{Per}(x)=\mathbb Z\). The one-dimensional character module
\[
\mathbb C[t^{\pm1}]\to\mathbb C,\qquad t\mapsto\alpha\in\mathbb C^\times
\]
is a valid ungraded simple module, but it is not a nonzero finite-dimensional graded module for the standard \(\mathbb Z\)-grading: multiplication by \(t\) shifts degree by \(1\) invertibly. Thus it does not satisfy the graded hypothesis of Corollary 4.8.

## Prior literature and originality boundary

The groupoid-fiber induction itself is prior art. Nguyen--Nguyen, *On induced graded simple modules over graded Steinberg algebras with applications to Leavitt path algebras* (arXiv:2006.09931; later Journal of Algebra and Its Applications), explicitly builds on Steinberg's induction/restriction between \(A_R(\mathcal G)\)-modules and isotropy-group modules. The standard induction module is based on the source fiber \(RL_x\), not on a point-mass subalgebra at an arbitrary nonisolated unit.

Open singleton corners are also prior art. Clark--Gil Canto--Martín Barquero--Martín González--Ruiz Campos, *On the socle of a class of Steinberg algebras* (arXiv:2502.15574), proves in particular that if \(\{x\}\) is open and \(x\mathcal Gx\cong\mathbb Z^k\), then the corner \(1_{\{x\}}A_K(\mathcal G)1_{\{x\}}\) is the corresponding Laurent polynomial algebra.

The claimed contribution here is therefore narrow: the exact isolated-point boundary for the point-mass embedding asserted in arXiv:2609.20230v1, the explicit two-loop counterexample to its unrestricted Proposition 4.1, the corner repair showing when that particular restriction-of-scalars construction is legitimate, and the finite-dimensional graded periodicity obstruction above. The general theory of Steinberg induction and the known open-singleton corner results are not claimed as new.

The point-mass criterion is elementary and may be implicit in older Steinberg-algebra literature; originality is asserted only to the best of our knowledge. The correction to the 2026 preprint is unaffected by that residual risk, because the source statement is explicitly quantified over arbitrary boundary paths.

## References

1. B. Van Nguyen, *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1 (2026). https://arxiv.org/abs/2609.20230v1
2. Q. L. Nguyen and B. V. Nguyen, *On induced graded simple modules over graded Steinberg algebras with applications to Leavitt path algebras*, arXiv:2006.09931 (2020); Journal of Algebra and Its Applications 23 (2024), 2450126. https://arxiv.org/abs/2006.09931
3. L. O. Clark, C. Gil Canto, D. Martín Barquero, C. Martín González, I. Ruiz Campos, *On the socle of a class of Steinberg algebras*, arXiv:2502.15574 (2025). https://arxiv.org/abs/2502.15574
