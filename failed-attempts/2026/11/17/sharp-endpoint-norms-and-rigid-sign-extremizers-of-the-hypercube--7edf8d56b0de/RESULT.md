# Sharp endpoint norms and rigid sign extremizers of the hypercube Hodge gradient projection

## Finding

For every integer \(d\ge1\), let \(Q_d\) be the unit-edge Boolean hypercube graph, with all edges oriented from coordinate value zero to one. Let \(E_d\) be the set of its \(d2^{d-1}\) oriented edges. Equip real edge fields with the usual counting-measure \(\ell_2(E_d)\) inner product, and with the coordinate-maximum norm \(\|u\|_{\infty}=\max_{e\in E_d}|u_e|\).

Write \(B:\mathbb R^{\{0,1\}^d}\to\mathbb R^{E_d}\) for the oriented gradient, \((Bf)_{(x,x\oplus e_i)}=f(x\oplus e_i)-f(x)\), with \(x_i=0\). Let \(L=B^{\mathsf T}B\), and define the Euclidean gradient projection
\[
P_d=B L^\dagger B^{\mathsf T},
\]
where \(L^\dagger\) is the Moore--Penrose pseudoinverse. Thus \(P_d\) sends arbitrary edge data to the least-squares integrable edge gradient. The exact endpoint operator norms are
\[
\boxed{\|P_d\|_{\ell_\infty(E_d)\to\ell_\infty(E_d)}
=\|P_d\|_{\ell_1(E_d)\to\ell_1(E_d)}=\frac{d+1}{2}.}
\]

More precisely, for any fixed output edge \(e\) in coordinate direction \(i\), the absolute row sum of \(P_d\) over input edges parallel to \(i\) is exactly \(1\); over input edges parallel to any other fixed direction \(j\ne i\) it is exactly \(1/2\). No matrix entry is zero. Every norm-one input for the \(\ell_\infty\) operator norm is, for a unique oriented edge \(e\) and a sign \(\sigma\in\{-1,1\}\), the field \(u_f=\sigma\operatorname{sgn}((P_d)_{e,f})\). In particular there are exactly \(d2^d\) such norm-one sign fields.

The last assertion is about maximizers with \(\|u\|_\infty=1\) in the *full edge-flow space*, not merely integrable gradient inputs. The Hilbert-space norm of the same orthogonal projection equals \(1\).

## Assumptions and scope

All vector spaces and edge data are real. Each undirected edge is listed once, with positive coordinate orientation, unit conductance, and counting inner product. The case \(d=1\) is included and gives the identity on a one-dimensional edge space. The maximum norm is over all edge fields; no boundary conditions or divergence-free assumptions are imposed. The finite graph is the Cartesian product of \(d\) single edges, with \(2^d\) vertices. The stated operator is the *orthogonal* projector onto \(\operatorname{im}B\), not the nonlinear best approximation in \(\ell_1\) or \(\ell_\infty\).

## Proof

**1. Reduction to the dipole potential.** The graph is connected, so \(L\) has constants as its sole nullspace. The pseudoinverse formula is the unique Euclidean orthogonal projector onto \(\operatorname{im}B\): it is self-adjoint and idempotent, it fixes every \(Bf\), and its range lies in \(\operatorname{im}B\). The hypercube's signed coordinate-permutation and translation symmetries make the absolute row sums identical. It suffices to inspect the oriented edge \(e_0=(0,e_1)\), where \(0\) denotes the all-zero vertex.

Let \(h\) solve \(Lh=\delta_0-\delta_{e_1}\) with mean zero, and let \(z\in\{0,1\}^{d-1}\) index the remaining coordinates. Antisymmetry across the first coordinate forces \(h(0,z)=a_{|z|}\) and \(h(1,z)=-a_{|z|}\), where \(|z|\) is Hamming weight. The reduced vector \(a\) solves
\[
(L_{Q_{d-1}}+2I)a=\delta_{0}.
\]
Indeed at side zero the first-coordinate Laplacian term is \(2a\), and all other terms form \(L_{Q_{d-1}}a\). The transfer-current row is
\[
(P_d)_{e_0,f}=h(\operatorname{tail}f)-h(\operatorname{head}f),
\]
since \(B^{\mathsf T}\mathbf1_{e_0}=\delta_{e_1}-\delta_0\) and the two sign changes cancel.

**2. Explicit positive, strictly decreasing radial Green profile.** The resolvent integral and the one-bit heat kernel yield, for every integer \(0\le k\le d-1\),
\[
 a_k=2^{-d}\int_0^1(1+s)^{d-1-k}(1-s)^k\,ds.
\]
To verify the normalization, use \((L_{Q_{d-1}}+2I)^{-1}=\int_0^\infty e^{-2t}e^{-tL_{Q_{d-1}}}\,dt\), and the product heat kernel \(e^{-tL_{Q_{d-1}}}(0,z)=2^{-(d-1)}(1+e^{-2t})^{d-1-|z|}(1-e^{-2t})^{|z|}\); substitute \(s=e^{-2t}\). The resolvent is strictly positive. For \(0\le k\le d-2\), subtraction gives
\[
 a_k-a_{k+1}=2^{1-d}\int_0^1s(1+s)^{d-2-k}(1-s)^k\,ds>0.
\]
These identities include the endpoint \(d=1\), when the difference formula has an empty index range.

**3. Full entry signs and coordinate row budgets.** For an arbitrary output edge \(e=(x,x\oplus e_i)\) with \(x_i=0\), and input edge \(f=(y,y\oplus e_j)\) with \(y_j=0\), set \(k\) to be the number of unequal coordinates between \(x\) and \(y\), excluding \(i\) and (when \(j\ne i\)) \(j\). If \(i=j\), then
\[
(P_d)_{e,f}=2a_k>0.
\]
If \(i\ne j\), then
\[
(P_d)_{e,f}=(-1)^{x_j+y_i}(a_k-a_{k+1})\ne0.
\]
This follows directly by taking the signed difference of the potential in step 1. Thus the sign is explicit at every input-output edge pair.

Fix \(e\) and sum over the \(2^{d-1}\) parallel inputs. The binomial theorem under the integral gives
\[
 \sum_{f:\,\operatorname{dir}(f)=i}|(P_d)_{e,f}|
 =2\sum_{k=0}^{d-1}\binom{d-1}{k}a_k
 =2^{1-d}\int_0^1 2^{d-1}\,ds=1.
\]
For any fixed transverse direction \(j\ne i\), the two choices of first-side coordinate give the factor two. Another binomial identity yields
\[
 \sum_{f:\,\operatorname{dir}(f)=j}|(P_d)_{e,f}|
 =2\sum_{k=0}^{d-2}\binom{d-2}{k}(a_k-a_{k+1})
 =2^{2-d}\int_0^1 s\,2^{d-2}\,ds=\frac12.
\]
Hence each row has absolute sum \(1+(d-1)/2=(d+1)/2\). The \(\ell_\infty\) matrix operator norm equals the maximum absolute row sum, so the first sharp formula follows. Since \(P_d\) is symmetric, its maximum column sum is the same, proving the \(\ell_1\) formula.

**4. Complete extremizer rigidity.** For a real row with all entries nonzero, equality in
\[
\Big|\sum_f(P_d)_{e,f}u_f\Big|
 \le\sum_f|(P_d)_{e,f}|\,\|u\|_\infty
\]
forces every \(u_f\) to equal \(\sigma\operatorname{sgn}((P_d)_{e,f})\) when \(\|u\|_\infty=1\). Conversely each such sign field attains the row norm. The sign patterns for different output edges are genuinely distinct, even after allowing a global sign: if the output directions differ, the direction parallel to one edge is all positive in exactly one of the two patterns (the other pattern changes sign there because both values of the opposite output coordinate occur). If the directions coincide, the pattern is positive on that entire direction, fixing the global sign, and for each transverse direction \(j\) its sign depends on \(x_j\), which distinguishes the positions of the output edges. For \(d=1\) there is only one edge and the two global signs are distinct. There are \(2|E_d|=d2^d\) sign patterns in all, and no other maximizers. \(\square\)

## Verification

The companion standalone standard-library Python program `verify_hodge_cube.py` independently computes transfer-current coefficients in two ways: a rational Walsh-spectral sum and the rational integral Green formula. It checks the full row budget, strict sign rule, dipole Poisson equation, and explicit maximizing input. For every \(1\le d\le7\), all \(d2^{d-1}\) entries of a canonical row are independently matched; for \(d\le4\), every entry of the entire transfer-current matrix is independently cross-compared. The completed run reports `GREEN_VS_WALSH_CROSSCHECKS_PASSED 1954`, `RIGID_SIGN_WITNESS_CHECKS_PASSED 7`, and `ALL_EXACT_HYPERCUBE_HODGE_PROJECTION_CHECKS_PASSED`.

For \(d=1,2,3,4,5,6,7\), the respectively verified exact endpoint norms are \(1,\ 3/2,\ 2,\ 5/2,\ 3,\ 7/2,\ 4\). The analytical proof, rather than finite tests, establishes all dimensions and the complete equality classification.

## Relationship to prior work

Graph transfer-current matrices, via electrical dipole Green functions, are classical; Burton and Pemantle's transfer-impedance treatment identifies such matrices with spanning-tree correlation kernels. Jiang, Lim, Yao and Ye develop the least-squares gradient projection in graph-based statistical ranking, while distinguishing it from the nonlinear best \(\ell_1\) fit. March gives a general graph Helmholtz--Hodge framework. The present assertion concerns a different, quantitative endpoint issue: the **induced maximum-norm of that fixed Euclidean projection on the full hypercube edge space**, its exact per-coordinate absolute row budgets, and all maximizing input fields.

Direct comparison with those cited sources did not exhibit this complete quantitative and equality-case statement. The transfer-current construction alone does not state or evaluate the absolute signed row sums. Nor does general orthogonal-projection theory imply endpoint contractivity: the exact norm here increases linearly with dimension. Historical priority is qualified, not established conclusively; an equivalent calculation may be implicit in less accessible electrical-network or discrete Hodge literature.

## Limitations

The result concerns real coefficients, uniformly weighted finite hypercubes, edge counting measure, and the fixed Euclidean Hodge gradient projector. It does not determine optimal projection constants among *all* linear projections onto the gradient subspace, arbitrary graph/edge weights, nonlinear best maximum-norm approximation, or higher-dimensional cochain projections. The exact statement is mathematical, not a claim of independent external certification. The literature comparison may miss an equivalent historical formulation.

## References

1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, arXiv:math/0404048, first publicly posted 2004-04-02; particularly Section 4 on the transfer-impedance matrix.
2. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, first publicly posted 2008-11-07; sections on the \(L^2\) gradient fit and the distinct \(\ell_1\) minimization problem.
3. P. March, *Helmholtz-Hodge Decomposition on Graphs*, arXiv:2412.09434, first publicly posted 2024-12-12; the general graph decomposition and nonlocal curl framework.
