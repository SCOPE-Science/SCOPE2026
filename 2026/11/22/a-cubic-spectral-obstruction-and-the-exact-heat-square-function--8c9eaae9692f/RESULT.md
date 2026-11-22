# A cubic spectral obstruction and the exact heat square-function boundary on finite cycles

## Finding
For every finite simple unweighted cycle \(C_n\) with \(n\ge3\), every real or complex Hilbert space \(H\), and every signal \(f:C_n\to H\), the exact contraction dichotomy is
\[
\|G_2(f)\|_{\ell^4(C_n)}\le\tfrac12\|f-Ff\|_{\ell^4(C_n;H)}\text{ for all }f
\quad\Longleftrightarrow\quad n\in\{3,4\}.
\]
The coefficient \(1/2\) is optimal for both contracting cycle sizes. For every \(n\ge5\), an explicit universal real witness is
\[
f_n(j)=\cos(2\pi j/n)-\tfrac1{64}\cos(6\pi j/n),\qquad j=0,\ldots,n-1.
\]
The obstruction comes from a nonvanishing cubic cross moment between distinct eigenmodes. The same perturbative criterion works for finite real symmetric graph Laplacians beyond cycles. On \(C_4\), equality holds exactly when the eigenvalue-two and eigenvalue-four components are pointwise orthogonal with respect to the real part of the Hilbert inner product.

## Assumptions and scope
The graph \(C_n\) is unweighted and has the usual degree-two combinatorial Laplacian \(L\); \(C_3\) is the triangle. The heat semigroup is \(T_t=\exp(-tL)\). The projection \(F\) replaces the signal by its constant vertex mean. All \(\ell^4\)-norms use the same counting measure; normalizing by \(1/n\) does not change any assertion. Define the *temporal* square function
\[
G_2(f)(j)=\left(\int_0^\infty\big\|t\partial_tT_tf(j)\big\|_H^2\,\frac{dt}{t}\right)^{1/2}.
\]
The assertion is not about spatial-gradient square functions, nonlinear graph diffusion, or discrete-time heat approximations. The eigenvectors in the separate obstruction criterion are real scalar functions with distinct positive eigenvalues of a finite real symmetric Laplacian; they are therefore orthogonal and mean-zero. There is no assumption of nonnegative input.

## Proof
**1. Exact two-eigenmode interaction.** Let real eigenvectors \(Lu=\lambda u\) and \(Lv=\mu v\) have \(\lambda,\mu>0\) and \(\lambda\ne\mu\). For any real \(s\) and each vertex, integration of exponential products gives
\[
G_2(u+s v)(j)^2=\tfrac14u_j^2+\tfrac14s^2v_j^2+2a s u_jv_j,
\qquad a=\frac{\lambda\mu}{(\lambda+\mu)^2},\quad 0<a<\tfrac14.
\]
The full fourth-power deficit, without approximation, is
\[
\begin{aligned}
\Delta(s)&=\|u+s v\|_4^4-16\|G_2(u+s v)\|_4^4\\
&=4(1-4a)s\left(A+(1+4a)sB+s^2C\right),\\
A&=\sum_j u_j^3v_j,\quad B=\sum_j u_j^2v_j^2,\quad C=\sum_j u_jv_j^3.
\end{aligned}
\]
This follows by expanding the two squares at every vertex. If \(A\ne0\), choosing a sufficiently small \(s\) with the sign opposite to \(A\) makes \(\Delta(s)<0\). This proves the general cubic spectral obstruction: strict failure of the factor-\(1/2\) estimate.

**2. Every cycle of length at least five fails.** For \(n\ge5\), put \(\theta_j=2\pi j/n\), \(u_j=\cos\theta_j\), and \(v_j=\cos(3\theta_j)\). Their positive Laplacian eigenvalues are \(\lambda=2-2\cos(2\pi/n)\) and \(\mu=2-2\cos(6\pi/n)\), which are distinct at every such \(n\). Both eigenvectors have zero mean. The identity \(\cos^3\theta=(3\cos\theta+\cos3\theta)/4\) and the orthogonality of distinct modes give
\[
A=\tfrac14\sum_jv_j^2\ge n/8.
\]
The inequality is an equality except at \(n=6\), where \(A=n/4\). Since \(|u_j|,|v_j|\le1\), we have \(0\le B\le n\) and \(|C|\le n\). For the *same* \(s=-1/64\) at every \(n\ge5\),
\[
A+(1+4a)s B+s^2 C\ge n\left(\tfrac18-\tfrac2{64}-\tfrac1{4096}\right)>0.
\]
As \(1-4a>0\) and \(s<0\), the exact formula yields \(\Delta(s)<0\), proving strict amplification by the displayed witness for every \(n\ge5\).

**3. The triangle.** The only nonzero Laplacian eigenvalue of \(C_3\) is \(3\). Consequently, for \(h=f-Ff\), pointwise integration gives \(G_2(f)(j)=\|h(j)\|_H/2\). There is equality for every nonconstant signal.

**4. The four-cycle, including complex Hilbert signals.** Decompose \(h=f-Ff=u+v\), where \(u\) lies in the eigenvalue-\(4\) eigenspace and \(v\) in the eigenvalue-\(2\) eigenspace. Set \(q_j=\|u_j\|_H^2+\|v_j\|_H^2\) and \(c_j=2\operatorname{Re}\langle u_j,v_j\rangle_H\). The exact integral is
\[
4G_2(f)(j)^2=q_j+\rho c_j,\qquad \rho=\frac{4(4)(2)}{(4+2)^2}=\frac89.
\]
At opposite vertices of \(C_4\), \(u_{j+2}=u_j\), \(v_{j+2}=-v_j\), so \(q_{j+2}=q_j\) and \(c_{j+2}=-c_j\). Therefore \(\sum_jq_jc_j=0\), yielding the exact nonnegative deficit
\[
\begin{aligned}
\|h\|_4^4-16\|G_2(f)\|_4^4
&=\sum_j\big((q_j+c_j)^2-(q_j+\rho c_j)^2\big)\\
&=\left(1-\rho^2\right)\sum_jc_j^2
=\frac{17}{81}\sum_jc_j^2\ge0.
\end{aligned}
\]
Equality holds if and only if \(c_j=0\) for every vertex, as stated. Every single positive-eigenvalue signal has equality, proving sharpness of the coefficient \(1/2\).

## Verification
The derivation above uses only analytic spectral decompositions and exact integrals; it applies to infinitely many graph orders without assuming that finite enumeration is exhaustive. The standalone `check_cycle_square.py` independently verifies the scalar two-eigenmode polynomial identity symbolically, the four-cycle deficit coefficient exactly, the real witness numerically on all cycles \(C_5\) through \(C_{500}\), and the vector-valued four-cycle identity on 200 reproducibly seeded complex examples. The finite numerical checks are diagnostics, not a replacement for the general proof. Execute `python check_cycle_square.py` with Python, SymPy and NumPy installed.

## Relationship to prior work
Lai, Li and Li (November 7, 2026) establish dimension-free order bounds for Hilbert-valued temporal Littlewood--Paley functions of symmetric semigroups; their general estimates do not yield the graph-specific factor-\(1/2\) dichotomy or the cycle witnesses proved here. Dungey's graph square-function estimates concern spatial gradients, not the temporal derivative used here. Feneuil's work on discrete graph Littlewood--Paley functionals likewise concerns a different functional; only accessible abstract material was checked, so complete comparison with that paper remains a limitation. Closely related finite heat-Lipschitz and graph-variation results measure different operators and norms. The special contracting small graphs occur in other finite-graph work, but they do not imply the all-cycle failure theorem or its cubic spectral criterion.

## Limitations
This theorem classifies only whether the exact coefficient \(1/2\) works; it does not determine the optimal \(\ell^4\) amplification constant for cycles of order at least five. The simple-cycle edges have unit weight; arbitrary weighted graphs are outside the cycle classification, although the spectral obstruction applies to their self-adjoint generators where its hypotheses hold. No independent mathematical audit has been performed. The literature comparison may miss a less-obvious, historically earlier equivalent formulation of the general cubic criterion.

## References
1. X. Lai, B. Li, and J. Li, *Optimal orders for Hilbert-valued Littlewood–Paley functions of symmetric semigroups*, arXiv:2611.10710v1 (first posted November 7, 2026), https://arxiv.org/abs/2611.10710.
2. N. Dungey, *A Littlewood–Paley–Stein estimate on graphs and groups*, *Studia Mathematica* 189 (2008), https://www.impan.pl/shop/en/publication/transaction/download/product/90064.
3. J. Feneuil, *Littlewood–Paley functionals on graphs*, arXiv:1404.1353 (2014), https://arxiv.org/abs/1404.1353.
