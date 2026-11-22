# A sharp diagonal advantage for two-node cubature in tensor Brownian-bridge spaces

## Finding

Fix an integer \(d\ge 2\). Let \(\mathcal H_d=H_0^1(0,1)^{\otimes d}\) be the real tensor-product reproducing-kernel Hilbert space with kernel
\[
K_d(x,y)=\prod_{j=1}^d\bigl(\min(x_j,y_j)-x_jy_j\bigr),\qquad x,y\in[0,1]^d.
\]
For the integration functional \(I(f)=\int_{[0,1]^d}f(x)\,dx\), choose exactly two evaluation nodes and arbitrary real cubature weights to minimize squared worst-case error on the unit ball of \(\mathcal H_d\).

**Theorem.** Among all node pairs that differ in *at most one coordinate* (one-axis designs), the unique optimal geometry, up to a permutation of coordinate axes and exchange of nodes, has all shared coordinates equal to \(1/2\) and the two varying coordinates at \(1/3\) and \(2/3\). The two optimal weights equal \(2^{-(d-1)}/3\). The exact optimal squared error is
\[
E_{\mathrm{axis},d}=12^{-d}-\frac{32}{27}\,16^{-d}.
\]

In the reflected-diagonal family \(x=(t,\ldots,t)\), \(y=(1-t,\ldots,1-t)\), \(0<t<1/2\), there is a unique optimal separation: put \(s_d=t_d/(1-t_d)\), where \(s_d\in(0,1)\) is the unique root of
\[
1-s_d=2s_d^{d+1},\qquad t_d=\frac{s_d}{1+s_d}.
\]
The weights at these nodes are both \(1/[2^d(1+s_d^d)]\), and their exact squared worst-case error is
\[
E_{\mathrm{diag},d}=12^{-d}-\frac{2}{4^d}\,\frac{[s_d/(1+s_d)^2]^d}{1+s_d^d}.
\]
For every \(d\ge2\), **strictly** \(E_{\mathrm{diag},d}<E_{\mathrm{axis},d}\). Moreover the ratio of the captured integration-representer squared norms,
\[
\mathcal R_d=\frac{12^{-d}-E_{\mathrm{diag},d}}{12^{-d}-E_{\mathrm{axis},d}},
\]
is strictly increasing with \(d\), and
\[
\lim_{d\to\infty}\mathcal R_d=\frac{27}{16}.
\]
The optimum reflected separation satisfies
\[
1-2t_d\sim \frac{W_0(2d)}{2d},
\]
where \(W_0\) is the principal Lambert function. A simultaneous reflection of either node's coordinates preserves the reflected-family kernel values, so the stated class comparison also applies to the equivalent diagonals obtained by independently reversing coordinate orientations.

For \(d=2\), \(t_2\approx0.370972063760764\), the one-axis captured squared norm is \(1/216\), and the diagonal captured squared norm is approximately \(0.00505014088873647\). Their squared worst-case integration errors are respectively \(1/432\) and approximately \(0.00189430355570798\).

## Assumptions and scope

The nodes are nonadaptive, noiseless point evaluations; their weights are optimized in the RKHS worst-case sense. The one-axis class consists of pairs differing in at most one coordinate, including coinciding nodes and boundary nodes. The reflected-diagonal class consists of the specified symmetric pairs and their coordinatewise orientation reversals. The theorem does **not** assert that the reflected-diagonal configuration is globally optimal over all unrestricted pairs in \([0,1]^d\). The reference norm is the canonical Hilbert tensor-product norm, not the usual isotropic Sobolev norm. The same formulas are posterior integral variances under the centered Gaussian field with covariance \(K_d\), but no noise or random-node averaging is assumed.

## Proof

**Kernel quadrature identity.** Write \(k(u,v)=\min(u,v)-uv\), \(v(u)=u(1-u)\). Direct integration gives
\[
\int_0^1 k(u,z)\,dz=\frac{v(u)}2,\quad
\int_0^1\!\int_0^1 k(u,z)\,du\,dz=\frac1{12}.
\]
Consequently the integration-representer squared norm equals \(C_d=12^{-d}\), the kernel-mean vector at two nodes is \(g_i=2^{-d}\prod_jv(x_{ij})\), and the Gram matrix is \(G_{ij}=K_d(x_i,x_j)\). For distinct interior nodes this Gram matrix is positive definite. The worst-case squared error for weights \(w\in\mathbb R^2\) is
\[
C_d-2w^\mathsf Tg+w^\mathsf TGw.
\]
Its unique optimal weights are \(G^{-1}g\), and the captured squared norm is \(g^\mathsf TG^{-1}g\). Coinciding or boundary nodes supply at most one nonzero evaluation and cannot attain the two-node optima below.

**One-axis optimum.** Suppose the two nodes have common coordinates \(c_2,\ldots,c_d\), and first coordinates \(a,b\). Tensor separation yields
\[
g^\mathsf TG^{-1}g=Q_1(a,b)\prod_{j=2}^d\frac{v(c_j)}4,
\]
where \(Q_1(a,b)\) is the optimal captured squared norm of the *one-dimensional* integral using two evaluations at \(a,b\). For \(0<a<b<1\), the one-dimensional Brownian-bridge interpolation residual consists of three independent bridge intervals with lengths \(a\), \(b-a\), \(1-b\); alternatively, the same fact follows by orthogonal projection onto piecewise linear tent functions in \(H_0^1\). Hence
\[
\frac1{12}-Q_1(a,b)=\frac{a^3+(b-a)^3+(1-b)^3}{12}.
\]
Strict convexity of the cube and the three lengths summing to one show that the unique maximizer is \((a,b)=(1/3,2/3)\), with \(Q_1=2/27\). Furthermore \(v(c_j)/4\le1/16\), with equality only at \(c_j=1/2\). This proves the exact one-axis bound, its equality cases, and the weights from tensorized kernel interpolation (one-dimensional integration weights \(1/3,1/3\), multiplied by \(1/2\) for each shared coordinate).

**Reflected-diagonal optimum.** Let \(s=t/(1-t)\in(0,1)\). The two equal diagonal Gram entries are \(p=[t(1-t)]^d=[s/(1+s)^2]^d\), their mutual entry is \(t^{2d}=ps^d\), and the two kernel means equal \(p/2^d\). Thus the inverse of the symmetric two-by-two Gram matrix gives equal optimal weights \(1/[2^d(1+s^d)]\) and captured norm
\[
Q_d(s)=\frac{2}{4^d}\,\frac{[s/(1+s)^2]^d}{1+s^d}.
\]
An exact differentiation shows
\[
\frac{d}{ds}\log Q_d(s)=\frac{d(1-s-2s^{d+1})}{s(1+s)(1+s^d)}.
\]
Its numerator decreases strictly from \(1\) to \(-2\) on \([0,1]\). Therefore the root \(s_d\) is unique, and \(Q_d\) increases then decreases, proving the exact optimum on this family, including all strict equality conditions.

**Strict dimensional advantage and limit.** Set \(s=e^{-\ell/d}\), \(\ell>0\). The *normalized* captured squared norm becomes
\[
16^d Q_d(s)=F_d(\ell):=\frac{2\operatorname{sech}^{2d}(\ell/(2d))}{1+e^{-\ell}}.
\]
The function \(z\mapsto\log\cosh z\) is strictly convex and vanishes at \(z=0\). For any fixed \(\ell>0\), the quantity \(d\log\cosh(\ell/(2d))\) strictly decreases with positive integer \(d\); hence \(F_{d+1}(\ell)>F_d(\ell)\). Their attained maxima \(M_d=\max_{\ell>0}F_d(\ell)\) are therefore strictly increasing. The one-dimensional computation above gives \(M_1=16(2/27)=32/27\). Since the axis optimum has the *same* normalized captured value \(32/27\) for all dimensions, \(M_d>32/27\) for every \(d\ge2\). For finite \(d\), \(F_d(\ell)<2\); choosing \(\ell=d^{1/4}\) yields \(F_d(\ell)\to2\), so \(M_d\uparrow2\) and \(M_d/(32/27)\to27/16\).

**Separation asymptotic.** The defining equation gives \(s_d\to1\) and \(s_d^d=(1-s_d)/(2s_d)\to0\). Let \(a_d=-d\log s_d\), so \(a_d\to\infty\) and \(a_d/d\to0\). Then \(1-s_d\sim a_d/d\), \(s_d^{d+1}\sim e^{-a_d}\), and the root identity implies \(a_de^{a_d}\sim2d\). Consequently \(a_d\sim W_0(2d)\) and \((1-s_d)/(1+s_d)\sim W_0(2d)/(2d)\). This proves the final assertion.

## Verification

Run `python3 verify.py` in an ordinary Python 3 environment. The standalone script performs 379 exact `fractions.Fraction` checks of the Gram-inverse formula, tensor factorization, and explicit one-axis optimum for sample dimensions, plus 150 numerical root and monotonicity spot checks. It also prints the two-dimensional numerical values. No finite test is used as a substitute for the general proof above.

## Relationship to prior work

Briol et al. (2017) study sampling distributions for kernel quadrature and associated error-rate constants, rather than sharp deterministic two-node tensor-bridge comparisons. Kacwin et al. (2018), especially Theorem 5.4 and Section 7.1, provide the general tensor-product reproducing-kernel and worst-case cubature machinery used here; they do not give the stated two-node one-axis equality classification, reflected-family root, or dimension-sharp strict advantage. Santin (2022), Theorem 5 and the flat-kernel limit, establishes equally spaced points for a *one-dimensional interpolation power-function* objective, distinct from the multivariate integral functional compared here. The one-dimensional bridge interval formula is standard and is not asserted to be new. The novelty claim is confined to the conjunction of the sharp two-node design-family comparison, unique reflected-diagonal optimizer, and strict dimensional ratio law.

## Limitations

The comparison is between two geometrically natural restricted families; there is no global optimality theorem over all unrestricted pairs. The \(27/16\) asymptotic ratio applies to captured representer energy \(C_d-E\), **not** to the total integration error or a runtime speedup. In high dimensions \(C_d=12^{-d}\) and the captured quantities are of order \(16^{-d}\), so both two-node rules capture an exponentially small fraction of the total squared representer norm. Older literature on tensorized spline cubature, sparse grids, or optimal design may contain equivalent formulas; publication priority is not independently certified.

## References

1. F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen and M. Girolami, *On the Sampling Problem for Kernel Quadrature*, ICML/PMLR 70 (2017), 586–595; first public arXiv version June 11, 2017, https://arxiv.org/abs/1706.03369 .
2. C. Kacwin, J. Oettershagen, M. Ullrich and T. Ullrich, *Numerical performance of optimized Frolov lattices in tensor product reproducing kernel Sobolev spaces*, arXiv:1802.08666, first public February 23, 2018, https://arxiv.org/abs/1802.08666 .
3. G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959, first public October 28, 2022, https://arxiv.org/abs/2210.15959 .
