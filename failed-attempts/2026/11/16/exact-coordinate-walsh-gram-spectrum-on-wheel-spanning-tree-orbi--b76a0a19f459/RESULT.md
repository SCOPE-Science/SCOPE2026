# Exact coordinate-Walsh Gram spectrum on wheel spanning-tree orbits

## Finding

For an integer \(n\ge3\), let \(W_n\) be the simple wheel with rim vertices \(1,\ldots,n\), hub \(0\), spokes \(\{0,j\}\), and rim edges \(\{j,j+1\}\), with cyclic indices. Its \(2n\) edges index the binary vector space \(\mathbb F_2^{2n}\). Let \(\mathcal T_n\) be the set of its spanning-tree edge-incidence vectors, equipped with uniform probability measure. For each edge \(e\), restrict the coordinate Walsh character \(\chi_e(T)=(-1)^{\mathbf1_{e\in T}}\) to \(\mathcal T_n\). Let \(G_n=(\mathbb E_{T\in\mathcal T_n}\chi_e(T)\chi_f(T))_{e,f}\) be the uncentered \(2n\)-by-\(2n\) Gram matrix.

Put
\[
\rho=\frac{3-\sqrt5}{2},\qquad H_n=\frac{1+\rho^n}{1-\rho^n},\qquad \mu_n=1-\frac{2H_n}{\sqrt5}.
\]
The complete eigenvalue multiset of \(G_n\) consists of the two real numbers
\[
0,\qquad \nu_n=\frac{16H_n}{5\sqrt5}-\frac{16n\rho^n}{5(1-\rho^n)^2}+2n\mu_n^2
\]
and, for every integer \(k\) with \(1\le k<n\), the two numbers
\[
\lambda_{n,k}^{-}=\frac{8H_n}{\sqrt5}\frac{1-t_{n,k}}{3-2t_{n,k}},\qquad
\lambda_{n,k}^{+}=\frac{8H_n}{\sqrt5}\frac{1+t_{n,k}}{3+2t_{n,k}},\qquad
 t_{n,k}=\left|\cos\left(\frac{\pi k}{n}\right)\right|.
\]
Every eigenvalue occurs with the multiplicity prescribed by this multiset, including any coincidences. In particular, \(G_n\) has rank exactly \(2n-1\). Its kernel is spanned by the all-ones edge coefficient vector, corresponding to the pointwise relation \(\sum_e\chi_e(T)=0\).

The sharp least positive eigenvalue is
\[
\boxed{\lambda_{\min}^{+}(G_n)=\frac{8H_n}{\sqrt5}\frac{1-\cos(\pi/n)}{3-2\cos(\pi/n)}}.
\]
For \(n\ge4\), this eigenvalue has multiplicity exactly two, from the two rim angular modes \(k=1\) and \(k=n-1\). For \(n=3\), its multiplicity is three because \(\nu_3=\lambda_{3,1}^{-}=\lambda_{3,2}^{-}=1\). The sharp largest eigenvalue is the explicit two-way maximum
\[
\boxed{\lambda_{\max}(G_n)=\max\left\{\nu_n,\frac{8H_n}{\sqrt5}\frac{1+\cos(\pi/n)}{3+2\cos(\pi/n)}\right\}}.
\]
Consequently the exact Gram condition ratio on the orthogonal complement of the forced null direction is their quotient, and
\[
\lambda_{\min}^{+}(G_n)=\frac{4\pi^2}{\sqrt5\,n^2}+O(n^{-4}),\qquad
\lambda_{\max}(G_n)=2\left(1-\frac2{\sqrt5}\right)^2n+O(1),
\]
\[
\boxed{\frac{\lambda_{\max}(G_n)}{\lambda_{\min}^{+}(G_n)}\sim
\frac{(\sqrt5-2)^2}{2\sqrt5\,\pi^2}\,n^3.}
\]
Thus coordinate-Walsh sampling on wheel spanning-tree orbits loses stability at an exact cubic Gram-condition rate, despite having only one forced linear relation.

## Assumptions and scope

The wheel has exactly \(n\ge3\) rim vertices and one hub; here \(W_3\) is the complete graph on four vertices. All graph edges are unweighted. A spanning tree has exactly \(n\) edges and occurs with equal probability. The Walsh characters are real-valued and unnormalized, while the Gram inner product uses probability normalization \(\mathbb E_{T\in\mathcal T_n}\). The statement concerns the degree-one coordinate Walsh family alone, not every character of the full binary edge group. The eigenvalue multiset has \(2n\) entries and is real and nonnegative.

## Proof

**1. Spanning-tree inclusion moments.** Remove the hub row from an oriented incidence matrix. Orient the spoke edges so that their columns are the standard basis of \(\mathbb R^n\), and rim edges from \(j+1\) to \(j\). Then \(B=[I\ D]\), where \(D=I-S\) and \(S\) is cyclic shift. The reduced Laplacian is
\[
L=BB^{\mathsf T}=I+DD^{\mathsf T}=3I-S-S^{-1}.
\]
For positive edge weights \(w_e\), the weighted matrix-tree identity gives \(Z(w)=\det(B\operatorname{diag}(w)B^{\mathsf T})=\sum_{T\in\mathcal T_n}\prod_{e\in T}w_e\). Differentiate this polynomial at all weights equal to one. With \(K=B^{\mathsf T}L^{-1}B\), logarithmic determinant differentiation gives
\[
\mathbb P(e\in T)=K_{ee},\qquad
\mathbb P(e,f\in T)=K_{ee}K_{ff}-K_{ef}^2\quad(e\ne f).
\]
Therefore, for \(I_e=\mathbf1_{e\in T}\), the covariance matrix is
\[
\operatorname{Cov}(I_e,I_f)=\delta_{ef}K_{ee}-K_{ef}^2.
\]
These are the familiar transfer-current two-edge identities; their derivation above fixes normalization and orientation.

**2. Periodic Green kernel.** Define \(g_d=(L^{-1})_{j,j+d}\) with cyclic indices. The number \(\rho=(3-\sqrt5)/2\) satisfies \(\rho+\rho^{-1}=3\). Direct substitution into \(3g_d-g_{d-1}-g_{d+1}=\delta_{d0}\) yields, for \(0\le d<n\),
\[
g_d=\frac{\rho^d+\rho^{n-d}}{\sqrt5(1-\rho^n)},\qquad g_0=\frac{H_n}{\sqrt5}.
\]
The transfer-current blocks indexed by spokes \(s_j\) and rim edges \(r_j\) are
\[
K_{s_i,s_j}=g_{i-j},\qquad K_{r_i,r_j}=\delta_{ij}-g_{i-j},\qquad
K_{s_i,r_j}=g_{i-j}-g_{i-j-1},
\]
where a consistent cyclic orientation is understood. The second identity follows from \(D^{\mathsf T}L^{-1}D=I-L^{-1}\); a reversed rim orientation conjugates the mixed blocks without altering any claimed eigenvalue. Thus the spoke and rim mean Walsh values are respectively \(\mu_n=1-2g_0\) and \(-\mu_n\).

**3. Two-by-two cyclic Fourier blocks.** Write \(h_d=g_d-g_{d-1}\). Since \(\chi_e=1-2I_e\),
\[
G_n=4\operatorname{Cov}(I)+\mathbb E\chi\,(\mathbb E\chi)^{\mathsf T}.
\]
The spoke-spoke and rim-rim covariance blocks have entries \(\delta_{d0}g_0-g_d^2\), while the spoke-rim block has entries \(-h_d^2\), up to a consistent harmless reversal of cyclic indices. Hence the covariance is block-circulant. For \(\theta_k=2\pi k/n\) and \(t_{n,k}=|\cos(\theta_k/2)|\), finite geometric-series summation of the explicit \(g_d\) gives
\[
\sum_{d=0}^{n-1}g_d^2e^{-i\theta_kd}=
\frac{3H_n}{\sqrt5(9-4t_{n,k}^2)}+
\frac{2n\rho^n}{5(1-\rho^n)^2}\mathbf1_{\{k=0\}},
\]
\[
\sum_{d=0}^{n-1}h_d^2e^{-i\theta_kd}=
\frac{H_n(1+e^{-i\theta_k})}{\sqrt5(9-4t_{n,k}^2)}-
\frac{2n\rho^n}{5(1-\rho^n)^2}\mathbf1_{\{k=0\}}.
\]
For completeness, these identities result by expanding squares of \(\rho^d+\rho^{n-d}\) and of their first differences, summing the two geometric progressions, and using \(\rho^2-3\rho+1=0\) and \(1-\rho^2=\sqrt5\rho\). They can also be verified directly by multiplying both sides by \(9-4t_{n,k}^2\) and applying the finite geometric-series formula.

For every \(k\ne0\), the mean outer product vanishes. The Hermitian Fourier block is
\[
4\begin{pmatrix}a_k&b_k\\ \overline b_k&a_k\end{pmatrix},\qquad
 a_k=\frac{H_n}{\sqrt5}\left(1-\frac3{9-4t_{n,k}^2}\right),\quad
 |b_k|=\frac{2H_nt_{n,k}}{\sqrt5(9-4t_{n,k}^2)}.
\]
Its eigenvalues \(4(a_k\pm|b_k|)\) simplify, by factoring \(9-4t^2=(3-2t)(3+2t)\), to the two displayed \(\lambda_{n,k}^{\pm}\).

At \(k=0\), the covariance block has a null vector \((1,1)\), and its other eigenvalue equals
\[
\frac{16H_n}{5\sqrt5}-\frac{16n\rho^n}{5(1-\rho^n)^2}.
\]
The mean vector contributes exactly \(2n\mu_n^2\) to the anti-diagonal mode \((1,-1)\), giving \(\nu_n\). As every tree uses precisely \(n\) of the \(2n\) graph edges, \(\sum_e\chi_e(T)=2n-2n=0\) pointwise, identifying the unique zero direction. Every nonconstant eigenvalue is strictly positive because \(0\le t_{n,k}<1\) for \(1\le k<n\).

**4. Exact extrema and asymptotics.** The function \((1-t)/(3-2t)\) is strictly decreasing and \((1+t)/(3+2t)\) strictly increasing for \(0\le t<1\); their derivatives are \(-1/(3-2t)^2\) and \(1/(3+2t)^2\). Among the nonzero cyclic modes, the smallest and largest eigenvalues therefore occur at \(k=1,n-1\), where \(t=\cos(\pi/n)\). For \(n=3\), direct substitution gives \(\nu_3=\lambda_{3,1}^{-}=1\). For every \(n\ge4\), using \(n\rho^n\le4\rho^4\) and \(H_n\ge1\) gives
\[
\nu_n\ge\frac{16}{5\sqrt5}-\frac{64\rho^4}{5(1-\rho^4)^2}>1,
\]
whereas monotonicity and \(H_n\le H_3\) imply \(\lambda_{n,1}^{-}<1\). This proves the sharp positive minimum and its multiplicity. The sharp maximum is the greater of the constant anti-diagonal mode and the highest nonconstant mode, as asserted.

Finally, \(H_n=1+O(\rho^n)\), \(1-\cos(\pi/n)=\pi^2/(2n^2)+O(n^{-4})\), and the nonconstant positive eigenvalues remain bounded above. The formula for \(\nu_n\) grows as \(2(1-2/\sqrt5)^2n+O(1)\). Substitution yields both asymptotics and the exact leading cubic Gram-condition coefficient.

## Verification

The accompanying `checker.py` constructs every spanning tree of \(W_n\) by independently testing all \(n\)-edge subsets for acyclicity, forms the integer Walsh Gram sum from the resulting \(\{-1,1\}^{2n}\) vectors, and compares its complete numerical eigenvalue multiset against the formula. It tests every integer \(3\le n\le10\), including the \(n=3\) degeneracy. The eight direct enumerations contain respectively \(16,45,121,320,841,2205,5776,15125\) trees and have maximum observed spectral disagreement less than \(3\times10^{-15}\). They also independently check trace, nullity, the pointwise linear relation, and tree counts. Run with `python checker.py` using Python 3 and NumPy. Numerical checks support the exact symbolic proof; they are not a proof for unrestricted \(n\).

## Relationship to prior work

Burton and Pemantle's transfer-impedance theorem gives joint edge-inclusion probabilities for general uniform spanning trees; this establishes the general probabilistic starting point but does not evaluate the wheel coordinate-Walsh Gram spectrum or its sharp positive eigenvalue. Benjamin and Yerger give the classical wheel spanning-tree count, including the cyclic reduced-Laplacian geometry. Dall and Pfeifle explain weighted matrix-tree identities for graphic and regular matroids. The present finding evaluates the full \(2n\)-eigenvalue Walsh sampling spectrum and extracts a sharp twofold weakest mode and cubic instability law. General covariance or matrix-tree identities alone should not be mistaken for the explicit evaluated result; conversely the theorem does not claim the underlying determinant identities are new.

## Limitations

The theorem concerns unweighted wheel graphs and only first-degree coordinate Walsh characters. It does not evaluate all binary Walsh coefficients of the spanning-tree indicator, nor does it address arbitrary graphs. The Gram matrix necessarily has one null direction; reported conditioning is on its orthogonal complement. Search-based historical priority remains bounded, and independent mathematical verification has not been performed.

## References

1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Ann. Probab. 21 (1993), 1329–1371; first arXiv upload April 2, 2004, https://arxiv.org/abs/math/0404048 . Sections 1 and 4, finite-graph transfer-current determinant and pair inclusion identities.
2. A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, manuscript dated November 14, 2004; Bull. Inst. Combin. Appl. 47 (2006), 37–42. https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/Combinatorial-Interpretations-of-Spanning-Tree-Identities.pdf . Theorems 1.2 and 1.3 and wheel reduced Laplacian.
3. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, first arXiv upload April 15, 2014, https://arxiv.org/abs/1404.3876 . Sections 1–4, weighted matrix-tree context.
