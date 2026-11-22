# Linear entrywise instability of Frobenius projection onto the spectral-norm ball

## Finding
For integers \(m,n\ge2\), let \(\mathcal B_{m,n}=\{X\in\mathbb R^{m\times n}:\|X\|_{2\to2}\le1\}\), and let \(P_{m,n}\) be its nearest-point projector in Frobenius norm. Define the *maximum-entry* norm \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\) and its two-input global modulus
\[
L_{m,n}=\sup_{X\ne Y}\frac{\|P_{m,n}(X)-P_{m,n}(Y)\|_{\max}}{\|X-Y\|_{\max}}.
\]
Then
\[
\boxed{\frac12+\frac{(1+\sqrt{m-1})(1+\sqrt{n-1})}{4}\ \le L_{m,n}\le\frac{1+\sqrt{mn}}2.}
\]
In particular \(L_{2,2}=3/2\), exactly, and \(L_{d,d}=\Theta(d)\). Thus Frobenius nonexpansivity does *not* provide dimension-free entrywise stability.

There is a sharper, intrinsic statement about the rank-one smooth boundary. For unit vectors \(u\in\mathbb R^m\), \(v\in\mathbb R^n\), let \(G=uv^{\mathsf T}\) and \(J_G(H)=H-\langle G,H\rangle_FG\). The exact maximum of the coordinatewise operator norm of these tangent maps is
\[
T_{m,n}=\max_{0\le x,y\le1}\left\{1+xy\left[(x+\sqrt{m-1}\sqrt{1-x^2})(y+\sqrt{n-1}\sqrt{1-y^2})-2xy\right]\right\}.
\]
Every \(J_G\) is a limit of ordinary derivatives of \(P_{m,n}\) at matrices with exactly one singular value greater than one; consequently \(L_{m,n}\ge T_{m,n}\). If \(m,n\to\infty\) (both dimensions independently diverge), then
\[
\boxed{\frac{T_{m,n}}{\sqrt{mn}}\longrightarrow\frac14.}
\]
This limit is for the rank-one-boundary tangent family, *not* asserted to be the exact global leading constant of \(L_{m,n}\).

## Assumptions and scope
All matrices are real and rectangular, with \(m,n\ge2\). The spectral-norm radius is one, without loss of generality: positive rescaling of the ball preserves the global Lipschitz coefficient. Inputs are unrestricted matrices, and the projection is with respect to the Frobenius distance; both the input and output perturbation sizes are measured in the maximum-entry norm. No rank, convolution, positivity, symmetry or sparsity restriction is imposed on the **global** inputs. The tangent-family maximization, in contrast, is restricted to rank-one *boundary normals*.

## Proof
**1. Spectral clipping and smooth exterior points.** If \(X=U\operatorname{diag}(\sigma_i)V^{\mathsf T}\) is a singular-value decomposition, the Frobenius projector replaces each singular value \(\sigma_i\) by \(\min\{\sigma_i,1\}\). This is the classical Schatten-infinity-ball projection formula, not a new ingredient. Fix unit vectors \(u,v\), set \(G=uv^{\mathsf T}\), and let \(Z_s=(1+s)G\) for \(s>0\). Around \(Z_s\) the top singular value is simple and strictly greater than one, while every other singular value is less than one. Thus locally
\[
P_{m,n}(X)=X-(\sigma_1(X)-1)u_1(X)v_1(X)^{\mathsf T}.
\]
The leading singular-vector outer product is smooth locally (its simultaneous sign ambiguity cancels). Its derivative remains bounded as \(s\downarrow0\) by the fixed nonzero gap between the first and second singular values. Because \(D\sigma_1(Z_s)[H]=\langle G,H\rangle_F\), differentiation gives
\[
DP_{m,n}(Z_s)[H]=H-\langle G,H\rangle_FG-s\,D(u_1v_1^{\mathsf T})_{Z_s}[H].
\]
Consequently \(DP_{m,n}(Z_s)\to J_G\) in every finite-dimensional operator norm. Each derivative norm is bounded by \(L_{m,n}\); hence \(L_{m,n}\ge\|J_G\|_{\max\to\max}\).

**2. Exact tangent-row optimization.** In the coordinate basis of matrices the row indexed by \((i,j)\) of \(J_G\) has diagonal entry \(1-u_i^2v_j^2\) and other entries \(-u_iv_ju_kv_l\). Its absolute row sum is
\[
1+|u_iv_j|\|u\|_1\|v\|_1-2u_i^2v_j^2.
\]
For a selected \((i,j)\), write \(x=|u_i|\), \(y=|v_j|\). Cauchy--Schwarz gives
\[
\|u\|_1\le x+\sqrt{m-1}\sqrt{1-x^2},\qquad
\|v\|_1\le y+\sqrt{n-1}\sqrt{1-y^2}.
\]
Both inequalities are simultaneously equalities by taking each remaining absolute coordinate constant. The stated compact two-variable formula for \(T_{m,n}\) therefore follows, including boundary cases \(x=0\) or \(y=0\).

**3. Explicit dimension-growing witness.** Take
\[
u_1=v_1=1/\sqrt2,\qquad
u_i=1/\sqrt{2(m-1)}\ (i>1),\qquad
v_j=1/\sqrt{2(n-1)}\ (j>1).
\]
The first row sum of \(J_G\), meaning the row indexed by \((1,1)\), equals
\[
\frac12+\frac{(1+\sqrt{m-1})(1+\sqrt{n-1})}{4}.
\]
The smooth exterior points in Step 1 turn this derivative row sum into an arbitrarily close ratio between **distinct finite inputs**; no infinite-dimensional limit or assertion of exact finite-pair attainment is used.

**4. Universal upper bound.** More generally, an orthogonal metric projector \(P_C\) onto any nonempty closed convex subset of \(\mathbb R^N\) satisfies \(\|P_C\|_{\ell_\infty\mathrm{-Lip}}\le(1+\sqrt N)/2\). Indeed \(P_C\) is the gradient of the convex differentiable potential
\[
\Phi(z)=\sup_{w\in C}\left(\langle z,w\rangle-\tfrac12\|w\|_2^2\right).
\]
Firm nonexpansivity implies that its almost-everywhere Jacobian \(J\) is symmetric and satisfies \(0\preceq J\preceq I\). (Equivalently, mollify the Lipschitz gradient to avoid questions about exceptional line segments.) For each row \(i\), put \(t=J_{ii}\). Since \(J^2\preceq J\),
\[
\sum_{j\ne i}J_{ij}^2\le t(1-t),\qquad
\sum_j|J_{ij}|\le t+\sqrt{N-1}\sqrt{t(1-t)}\le\frac{1+\sqrt N}{2}.
\]
For a mollified projector the same positive-contraction Jacobian bounds persist under averaging, so the segment integral gives the bound globally; pass to the original map uniformly on compact sets. Set \(N=mn\) for \(P_{m,n}\). At \(m=n=2\) the lower and upper bounds both equal \(3/2\).

**5. Rank-one tangential asymptotic.** Expand the expression in Step 2. The term multiplying \(\sqrt{(m-1)(n-1)}\) is \(xy\sqrt{1-x^2}\sqrt{1-y^2}\le1/4\). The two singly square-rooted terms are bounded by \(\tfrac12\sqrt{m-1}\) and \(\tfrac12\sqrt{n-1}\), and the remaining terms by a dimension-independent constant. Thus
\[
T_{m,n}\le1+\tfrac12(\sqrt{m-1}+\sqrt{n-1})+\tfrac14\sqrt{(m-1)(n-1)}.
\]
Step 3 supplies the matching leading lower term. Dividing by \(\sqrt{mn}\) and letting both dimensions diverge proves the \(1/4\) limit. For square matrices, the lower and upper global bounds are both linear in \(d\), proving \(L_{d,d}=\Theta(d)\).

## Verification
Run `python3 checker.py` with NumPy. It independently constructs clipped SVD projections, differentiates finite input pairs just outside the rank-one boundary, compares with the analytic tangent-row sums, verifies the compact two-variable formula against direct row norms, and checks the universal bound on deterministic random pairs. These finite tests are supplements only; Steps 1--5 establish all quantifiers and asymptotic claims analytically.

## Relationship to prior work
Lefkimmiatis--Ward--Unser derived the Frobenius projection on Schatten norm balls by singular-value projection, including singular-value clipping at the spectral-norm endpoint. Sedghi--Gupta--Long used spectral-norm-ball projection to regularize convolutional layers. Neither inspected paper gives a global maximum-entry Lipschitz estimate, a sharp rank-one-tangent maximization, or the dimension-linear instability exhibited here. General Hilbert-space nonexpansivity gives only the Frobenius norm estimate; the refined universal endpoint bound follows from the positive-contraction Jacobian structure. Results about positive-semidefinite projection and nearest-correlation projection concern different feasible sets and do not imply this rank-one spectral-ball construction.

## Limitations
The exact unrestricted constant \(L_{m,n}\) is not determined for general \(m,n\), nor is its unrestricted asymptotic leading coefficient; the sharp limit \(1/4\) belongs only to the family of rank-one tangent maps. The lower bound is a supremal two-input amplification, not a claim of attainment at a fixed separated pair. The displayed formula concerns real matrices and coordinatewise perturbations without structural restrictions; convolutional-parameter perturbations may have different geometry. A more exhaustive literature review could reveal an earlier equivalent endpoint-norm statement.

## References
1. S. Lefkimmiatis, J. P. Ward, and M. Unser, *Hessian Schatten-Norm Regularization for Linear Inverse Problems*, IEEE Transactions on Image Processing (2013), Proposition 1 and Section III-F. Open manuscript: https://bigwww.epfl.ch/stamatis/publications/tipJ2013.pdf ; preprint https://arxiv.org/abs/1209.3318 .
2. H. Sedghi, V. Gupta, and P. M. Long, *The Singular Values of Convolutional Layers*, first public arXiv submission 2018-05-26, arXiv:1805.10408, Section 3 and Proposition 9; https://arxiv.org/abs/1805.10408 .
