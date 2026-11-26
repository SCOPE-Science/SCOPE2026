# A cubic spectral obstruction and the exact heat square-function boundary on finite cycles

## Finding

Let \(C_n\) be a finite simple unweighted cycle with \(n\ge3\), and let \(H\ne\{0\}\) be a real or complex Hilbert space. For each fixed such \(H\),
\[
 \bigl[\,\|G_2(f)\|_{\ell^4(C_n)}\le\tfrac12\|f-Ff\|_{\ell^4(C_n;H)}\text{ for all } f:C_n\to H\,\bigr]
 \quad\Longleftrightarrow\quad n\in\{3,4\}.
\]
The coefficient \(1/2\) is optimal on these two sizes. For every \(n\ge5\), a real scalar witness is
\[
 f_n(j)=\cos(2\pi j/n)-\tfrac1{64}\cos(6\pi j/n),\qquad 0\le j<n.
\]
Multiplication by any unit vector of \(H\) gives an \(H\)-valued witness. On \(C_4\), equality holds precisely when the eigenvalue-two and eigenvalue-four components of \(f-Ff\) are pointwise orthogonal with respect to the real part of the inner product. For the trivial Hilbert space \(H=\{0\}\), the estimate holds on every cycle, and the least nonnegative coefficient is zero.

## Setting

The generator \(L\) is the degree-two combinatorial Laplacian; \(C_3\) is the triangle. The heat semigroup is \(T_t=e^{-tL}\), and \(Ff\) is the constant vertex mean. The temporal square function is
\[
 G_2(f)(j)=\left(\int_0^\infty\|t\partial_tT_tf(j)\|_H^2\,\frac{dt}{t}\right)^{1/2}.
\]
Vertex norms use counting measure, or the same normalized counting measure on both sides. This is not a spatial-gradient square function or a discrete-time functional.

## Proof

**Two-eigenmode obstruction.** Let \(u,v\) be real eigenvectors of a finite real symmetric graph Laplacian with distinct positive eigenvalues \(\lambda,\mu\). Both have zero mean. By integrating \(\int_0^\infty t e^{-(\lambda+\mu)t}\,dt=(\lambda+\mu)^{-2}\), at each vertex
\[
 G_2(u+s v)^2=\tfrac14u^2+\tfrac14s^2v^2+2asu v,
 \qquad a=\frac{\lambda\mu}{(\lambda+\mu)^2}<\tfrac14.
\]
For \(A=\sum_j u_j^3v_j\), \(B=\sum_j u_j^2v_j^2\) and \(C=\sum_j u_jv_j^3\), expanding the fourth powers gives
\[
 \Delta(s):=\|u+sv\|_4^4-16\|G_2(u+sv)\|_4^4
 =4(1-4a)s\bigl[A+(1+4a)sB+s^2C\bigr].
\]
Equivalently, pointwise this is the difference of squares of \(u^2+s^2v^2+2suv\) and \(u^2+s^2v^2+8asuv\), summed over vertices. If \(A\ne0\), a sufficiently small \(s\) of the opposite sign makes the deficit negative. This suffices for strict failure of the estimate on any such graph, also for every nonzero Hilbert target by scalar embedding.

**Cycles of length at least five.** Take \(\theta_j=2\pi j/n\), \(u_j=\cos\theta_j\) and \(v_j=\cos(3\theta_j)\). The eigenvalues \(2-2\cos(2\pi/n)\) and \(2-2\cos(6\pi/n)\) are positive and distinct: for \(n\ge5\), frequency 3 is neither 0 nor \(\pm1\) modulo \(n\). Thus \(u,v\) are orthogonal. Since \(\cos^3\theta=(3\cos\theta+\cos3\theta)/4\), one obtains \(A=\tfrac14\sum_j v_j^2\). The sum of squares is \(n/2\) unless \(n=6\), when it is \(n\) because \(v_j=(-1)^j\). Hence \(A\ge n/8\). Since \(0\le B\le n\) and \(|C|\le n\), at \(s=-1/64\) the bracket in \(\Delta(s)\) is bounded below by
\[
 n\left(\tfrac18-\tfrac2{64}-\tfrac1{4096}\right)>0.
\]
Then \(s<0\) gives the strict violation.

**Triangle.** On mean-zero signals the only eigenvalue is \(3\). Thus \(G_2(f)(j)=\|f(j)-Ff\|_H/2\) pointwise, with equality for every signal. There is a nonzero mean-zero signal if \(H\ne\{0\}\), so the coefficient is optimal.

**Four-cycle.** Decompose the centered signal as \(h=u+v\) in the eigenvalue-\(4\) and eigenvalue-\(2\) eigenspaces, respectively. Set \(q_j=\|u_j\|_H^2+\|v_j\|_H^2\) and \(c_j=2\operatorname{Re}\langle u_j,v_j\rangle_H\). Integration gives \(4G_2(f)(j)^2=q_j+\rho c_j\) with \(\rho=4\cdot4\cdot2/(4+2)^2=8/9\). Here \(u_{j+2}=u_j\), \(v_{j+2}=-v_j\), so \(q_{j+2}=q_j\), \(c_{j+2}=-c_j\) and \(\sum_j q_jc_j=0\). Consequently
\[
 \|h\|_4^4-16\|G_2(f)\|_4^4
 =\sum_j\big[(q_j+c_j)^2-(q_j+\rho c_j)^2\big]
 =\tfrac{17}{81}\sum_j c_j^2.
\]
This proves the inequality and the stated equality condition for both real and complex signals. A nonzero pure eigenmode attains the coefficient. In the trivial target every signal is identically zero, giving the exceptional case of the statement.

## Verification and limitations

The proof is analytic for all cycle lengths. The accompanying verification note isolates exact sample checks and the scope of the original finite diagnostics. The theorem does not determine the optimal constant for the failing cycles and does not classify weighted graphs. The general cubic test is sufficient, not claimed necessary.

## Relationship to prior work

Lai, Li and Li [1] prove dimension-free Hilbert-valued temporal bounds and give the exact spatial \(L^2\) normalization. These do not resolve the sharp half-benchmark for each cycle at spatial exponent four. Dungey [2] treats a spatial-gradient functional. Feneuil [3, Sections 1–1.2] treats fractional discrete-time Markov functionals. The connected-graph onset result [4] already contains the scalar triangle and the pointwise spectral kernel. The complete-bipartite result [5] includes the four-cycle as \(K_{2,2}\), including its Hilbert equality condition, and exhibits a special cubic imbalance. The additional results here are the strict explicit witness simultaneously for every \(n\ge5\) and the two-eigenmode cubic criterion stated for general real symmetric graph Laplacians. The comparison does not rule out an older equivalent perturbative criterion.

## References

1. X. Lai, B. Li and J. Li, *Optimal orders for Hilbert-valued Littlewood–Paley functions of symmetric semigroups*, arXiv:2611.10710 (2026), https://arxiv.org/abs/2611.10710.
2. N. Dungey, *A Littlewood–Paley–Stein estimate on graphs and groups*, *Studia Math.* **189** (2008), 175–187.
3. J. Feneuil, *Littlewood–Paley functionals on graphs*, arXiv:1404.1353, https://arxiv.org/abs/1404.1353.
4. *Four vertices are necessary and sufficient for fourth-norm amplification of the heat square function on an unweighted graph*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-four-vertices-are-necessary-and-sufficient-for-fourth-norm-ampli--10b68babaeff/RESULT.md.
5. *The exact \(L^4\) heat square-function contraction boundary on complete bipartite graphs*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-exact-l-4-heat-square-function-contraction-boundary-on-compl--94da44836cfd/RESULT.md.
