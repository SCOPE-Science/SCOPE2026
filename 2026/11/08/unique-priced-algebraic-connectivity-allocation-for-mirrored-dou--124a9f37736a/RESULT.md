# Unique priced algebraic-connectivity allocation for mirrored double-stars

## Finding

Let \(m\ge2\). The balanced double-star has hubs \(h_+,h_-\), leaves \(u_i\) adjoining \(h_+\), and leaves \(v_i\) adjoining \(h_-\), for \(1\le i\le m\). Both pendant edges indexed \(i\) have positive price \(c_i\), while the hub-to-hub edge has positive price \(d\). All individual edge conductances are separately adjustable and nonnegative; the resource budget is \(B>0\). There is no assumption that an optimizer respects the reflection symmetry.

Put
\[
s_i=\sqrt{c_i},\quad t=\sqrt d,\quad
K=2\sum_{i=1}^m c_i+2t\sum_{i=1}^m s_i+\frac{m+1}{2}d.
\]
Then the unique global maximizing conductances are
\[
\boxed{w_{h_+u_i}^*=w_{h_-v_i}^*=\frac{B}{K}\left(1+\frac{t}{2s_i}\right),\quad
w_{h_+h_-}^*=\frac{B}{K}\left(\frac{m+1}{2}+\frac{\sum_i s_i}{t}\right).}
\]
The maximum second-smallest eigenvalue is
\[
\boxed{\max\lambda_2(L)=B/K.}
\]
It is simple at the optimizer, and all optimal weights are strictly positive. In particular, the price-dependent increment beyond the optimal spectral rate follows the exact inverse-square-root law
\[
\sqrt{c_i}\,(w_{h_+u_i}^*-\lambda_2^*)=\frac{\lambda_2^*\sqrt d}{2}.
\]
This result treats any heterogeneous mirrored positive price vector, not just two uniform spoke-price classes.

## Assumptions and scope

For a vector of nonnegative edge conductances \(w\), define the combinatorial weighted Laplacian
\[
L(w)=\sum_{\{a,b\}\in E}w_{ab}(e_a-e_b)(e_a-e_b)^{\mathsf T}.
\]
The feasible region is exactly
\[
\sum_{i=1}^m c_i(w_{h_+u_i}+w_{h_-v_i})+d w_{h_+h_-}\le B.
\]
Every weight, including reflection-paired weights, is initially an independent decision variable. All quantified parameters are finite and strictly positive, except that candidate conductances may be zero. The eigenvalue \(\lambda_2\) is the second-smallest eigenvalue of this unnormalized Laplacian; no normalization by vertex degree or stochastic holding probabilities is used.

## Proof

**Upper bound for every feasible allocation.** Consider the nonzero, centered vector \(x\) defined by
\[
x_{h_+}=t/2,\quad x_{h_-}=-t/2,\qquad
x_{u_i}=s_i+t/2,\quad x_{v_i}=-s_i-t/2.
\]
Its entries sum to zero. Its squared norm is
\[
\|x\|^2=2\sum_i(s_i+t/2)^2+2(t/2)^2=K.
\]
Each pendant-edge coordinate difference has squared magnitude \(c_i\), and the central-edge difference has squared magnitude \(d\). Therefore, for every feasible \(w\),
\[
\lambda_2(L(w))\le\frac{x^{\mathsf T}L(w)x}{\|x\|^2}
=\frac{\sum_i c_i(w_{h_+u_i}+w_{h_-v_i})+d w_{h_+h_-}}{K}\le\frac BK.
\]
This bound does not require candidate symmetry, positivity of every weight, or any assumption about the spectral multiplicity.

**Construction attaining the bound.** Write \(\lambda=B/K\) and set
\[
w_i=\lambda(1+t/(2s_i)),\qquad
q=\lambda((m+1)/2+\sum_i s_i/t).
\]
Direct expansion gives \(2\sum_i c_iw_i+dq=\lambda K=B\). The Laplacian action on each positive-side leaf is
\[
(Lx)_{u_i}=w_i(x_{u_i}-x_{h_+})=w_i s_i
=\lambda(s_i+t/2)=\lambda x_{u_i}.
\]
The negative side follows by reflection. At the positive hub,
\[
(Lx)_{h_+}=-\sum_i w_i s_i+qt
=\lambda\left[-\sum_i(s_i+t/2)+(m+1)t/2+\sum_i s_i\right]
=\lambda t/2=\lambda x_{h_+}.
\]
The other hub equation follows by antisymmetry. Hence \(Lx=\lambda x\).

**Proving this is the Fiedler eigenvalue.** Under exchange of the two halves, the Laplacian splits into even and odd orthogonal subspaces. On the even subspace, the corresponding half-vector \((z,z_1,\ldots,z_m)\) is orthogonal to constants precisely when \(z+\sum_i z_i=0\). Its Rayleigh energy is \(\sum_i w_i(z_i-z)^2\); hence
\[
\sum_i w_i(z_i-z)^2\ge(\min_i w_i)\sum_i(z_i-z)^2
\ge(\min_iw_i)(z^2+\sum_i z_i^2).
\]
The final inequality follows from \(\sum_i z_i=-z\), giving \(\sum_i(z_i-z)^2=\sum_i z_i^2+(m+2)z^2\). Every nonzero even-sector eigenvalue therefore exceeds \(\lambda\), because \(w_i>\lambda\).

In the odd subspace, the half-coordinate matrix is the symmetric positive-definite arrow matrix \(M\) with leaf diagonal entries \(w_i\), leaf–hub entries \(-w_i\), and hub diagonal entry \(\sum_i w_i+2q\). The positive vector \(v=(t/2,s_1+t/2,\ldots,s_m+t/2)\) satisfies \(Mv=\lambda v\). For any real half-vector \(y\), the ground-state identity gives
\[
y^{\mathsf T}(M-\lambda I)y
=\sum_i w_i\,v_{h_+}v_{u_i}
\left(\frac{y_{u_i}}{v_{u_i}}-\frac{y_{h_+}}{v_{h_+}}\right)^2\ge0.
\]
Thus \(\lambda\) is the smallest odd-sector eigenvalue; the identity shows its eigenspace is one dimensional. Comparing sectors proves \(\lambda_2(L)=\lambda=B/K\), simple. The upper bound is attained.

**Global uniqueness, including asymmetric candidates.** Any other allocation attaining \(B/K\) must spend the entire budget and attain equality in the preceding Rayleigh inequality at \(x\). Consequently \(L(w)x=(B/K)x\). Each leaf equation uniquely forces its individual pendant-edge conductance to equal \(\lambda(1+t/(2s_i))\), independently on both sides. Either hub equation then uniquely forces the central conductance to equal \(q\). Hence no other feasible optimizer exists. All forced conductances are positive.

## Verification

The standalone `verify.py` in this package uses only Python's standard library. It constructs rational prices from integer square roots and checks, exactly, all budget, eigenvector and Rayleigh identities for 108 parameter instances. It also diagonalizes 120 independently generated optimizers using a Jacobi eigensolver and checks 1,440 asymmetric, nonnegative same-budget competitors. Its expected terminal line is `VERIFY_OK exact_certificates=108 eigenvalue_instances=120 asymmetric_competitors=1440`.

For an exact example with \(m=2\), \(c=(1,4)\), \(d=9\), and \(B=100\), one has \(K=83/2\), \(\lambda_2^*=200/83\), pendant conductances \(500/83\) and \(350/83\) on each respective side, and hub-edge conductance \(500/83\). The cost is exactly \(100\). Finite checks alone do not prove the infinite-parameter theorem; the algebraic argument above does.

## Relationship to prior work

The continuous-time fastest-mixing formulation and its general semidefinite/maximum-variance-unfolding dual appear in Sun, Boyd, Xiao and Diaconis [1], including arbitrary linear edge-resource constraints. That general framework does not itself evaluate the heterogeneous mirror-priced double-star optimizer or its uniqueness. Fiedler [2] characterized absolute algebraic connectivity of trees under a uniform sum of weights. Richter and Rocha [3] evaluated the unpriced double-broom family and associated eigenvectors. Our uniform-cost specialization is part of that established line of work and is **not** claimed novel. The contribution is an explicit solution and unique full-weight classification for any number of unequal *mirrored* spoke prices and an independent central price, a setting not implied by their uniform-cost formula.

## Limitations

The theorem assumes strict positivity of prices and a reflection-paired price vector; it does not classify unbalanced trees or arbitrary unrelated left and right pendant prices. General tree SDP duality is prior art, not a new contribution. The originality assessment rests on examined primary materials and indexed searches; independent literature and mathematical audits are not claimed. The original 1990 Fiedler full text was unavailable for direct detailed comparison, although the specified equal-sum objective is identifiable from its published abstract.

## References

[1] J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821, https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published online 2006-11-02).

[2] M. Fiedler, *Absolute Algebraic Connectivity of Trees*, Linear and Multilinear Algebra 26 (1990), 85–106, DOI: 10.1080/03081089008817967, https://www.tandfonline.com/doi/abs/10.1080/03081089008817967.

[3] S. Richter, I. Rocha, *Absolute algebraic connectivity of double brooms*, 2014 preprint (later Discrete Applied Mathematics 201 (2016), 213–221), https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf.
