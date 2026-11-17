# Parity and scalar-field thresholds for two-row Schatten Gelfand numbers

## Finding
Let \(n\ge3\) be an integer, \(0<p<q\le\infty\), and set \(1/\infty=0\) and \(\beta=2^{1/q-1/p}\). For \(\mathbb F=\mathbb R\) or \(\mathbb C\), consider the identity \(I:\mathcal S_p^{2\times n}(\mathbb F)\to\mathcal S_q^{2\times n}(\mathbb F)\) and its Gelfand numbers formed with \(\mathbb F\)-linear subspaces. Put \(d=\lfloor n/2\rfloor\). The exact real sequence is
\[
c_k(I_{\mathbb R})=\begin{cases}1,&1\le k\le 2n-2d,\\ \beta,&2n-2d+1\le k\le2n.\end{cases}
\]
The complex sequence has three rigorously separated regimes:
\[
c_k(I_{\mathbb C})=\begin{cases}1,&1\le k\le n+1,\\ \text{strictly between }\beta\text{ and }1,&n+2\le k\le2n-d,\\\beta,&2n-d+1\le k\le2n.\end{cases}
\]
No numerical formula for the strictly intermediate complex numbers is asserted. The real first drop occurs at \(k=n+1\) for even \(n\) and \(k=n+2\) for odd \(n\). At this drop the real values reach the absolute two-singular-value lower bound immediately, but the complex values cannot do so before \(k=2n-d+1\).

Every real optimal test subspace at its first \(\beta\)-index has the form
\[
E=\left\{\begin{pmatrix}u^{\mathsf T}\\(Ju)^{\mathsf T}\end{pmatrix}:u\in U\right\},
\]
where \(U\subset\mathbb R^n\) has dimension \(2d\) (all of \(\mathbb R^n\) when \(n\) is even, a hyperplane when odd) and \(J:U\to U\) is an orthogonal complex structure: \(J^*=-J\) and \(J^*J=I_U\). Every complex optimal test subspace at its first \(\beta\)-index has the form \(E=\{(u^{\mathsf T},(Tu)^{\mathsf T})^{\mathsf T}:u\in U\}\), where \(U,V\subset\mathbb C^n\) are orthogonal \(d\)-dimensional subspaces and \(T:U\to V\) is a linear isometry. Conversely each such subspace is optimal at the stated index.

## Assumptions and scope
For a \(2\times n\) matrix \(A\), let \(s_1(A)\ge s_2(A)\ge0\) be its singular values and set \(\|A\|_r=(s_1^r+s_2^r)^{1/r}\) for finite positive \(r\), \(\|A\|_\infty=s_1\). The index range is \(1\le k\le2n\). Define
\[
c_k(I_{\mathbb F})=\inf_{\operatorname{codim}_{\mathbb F}E<k}\ \sup_{0\ne A\in E}\frac{\|A\|_q}{\|A\|_p}.
\]
All subspaces are finite-dimensional and automatically closed. The convention \(0<p<1\) is allowed; the domain is then a quasi-normed space. The theorem treats real and complex scalar fields separately and makes no claim about larger row counts.

## Proof
**1. The only possible extreme ratios.** Hölder's inequality and monotonicity of \(\ell_r\) quasi-norms on two nonnegative coordinates give, for every nonzero \(A\),
\[
\beta\le R(A):=\|A\|_q/\|A\|_p\le1.
\]
Because \(p<q\), equality \(R(A)=1\) holds precisely when \(\operatorname{rank}A=1\). Equality \(R(A)=\beta\) holds precisely when \(s_1(A)=s_2(A)>0\). These characterizations remain valid for \(p<1\) and \(q=\infty\).

**2. Real rank-one avoidance.** If a real linear subspace \(E\) contains no nonzero rank-one matrix, projection to the first row is injective (a matrix with vanishing first row has rank at most one). Consequently \(\dim E\le n\). If \(\dim E=n\), this projection identifies \(E\) with the graph of a real endomorphism \(T:\mathbb R^n\to\mathbb R^n\); rank-one avoidance says \(Tu\ne\lambda u\) for every nonzero real \(u\) and real \(\lambda\). For odd \(n\), a real linear map in odd dimension must have a real eigenvalue, a contradiction. Thus the maximal possible rank-one-free dimension is at most \(2d\). For even-dimensional \(U\subset\mathbb R^n\) with \(\dim U=2d\), choose an orthogonal complex structure \(J\), realized by planar quarter-turn blocks. Its graph contains no rank-one element and all nonzero matrices have equal singular values. It therefore has dimension \(2d\), proving sharpness.

Given \(k\le2n-2d\), every admissible test space has dimension at least \(2n-k+1\ge2d+1\), hence contains a rank-one matrix and its supremal ratio is \(1\). Given \(k\ge2n-2d+1\), the described graph of dimension \(2d\) is admissible and has constant ratio \(\beta\). This proves the entire real sequence.

**3. Real equality rigidity, including odd sizes.** At the first \(\beta\)-index a test space achieving the infimum must have dimension at least \(2d\). Since every nonzero matrix in it must have ratio \(\beta\), it is rank-one-free, hence has dimension exactly \(2d\). First-row projection gives a graph \(\{(u,Tu):u\in U\}\) with \(\dim U=2d\). Equality of the two singular values is equivalent to
\[
\|Tu\|=\|u\|,\qquad\langle u,Tu\rangle=0\quad(u\in U).
\]
When \(n\) is even, \(U=\mathbb R^n\); polarization gives \(T^*=-T\), while the first equality gives \(T^*T=I\). Thus \(T\) is an orthogonal complex structure.

When \(n\) is odd, \(U\) has codimension one. Choose a real unit normal \(e\), and decompose \(Tu=Au+\langle b,u\rangle e\), where \(A:U\to U\) and \(b\in U\). Polarization of \(\langle u,Tu\rangle=0\) yields \(A^*=-A\), while the norm identity gives
\[
A^*A=I_U-bb^*.
\]
On the even-dimensional real space \(U\), every eigenvalue of the nonnegative operator \(A^*A=-A^2\) has even multiplicity: a real skew-symmetric operator is an orthogonal sum of planar rotation blocks (including paired zero blocks). If \(b\ne0\), the right side has eigenvalue \(1\) of multiplicity \(2d-1\) and eigenvalue \(1-\|b\|^2\) of multiplicity one (these are distinct), contradicting even multiplicity. Therefore \(b=0\), and \(T=A=J\) maps \(U\) into itself, is orthogonal and skew-symmetric. Conversely these structures give all minimizers claimed.

**4. Complex rank-one avoidance.** A rank-one-free complex linear subspace has injective first-row projection and dimension at most \(n\). A dimension-\(n\) graph has a complex-linear endomorphism of \(\mathbb C^n\), which always has an eigenvector and hence a rank-one matrix. Thus the maximum is at most \(n-1\). It is attained by the graph of \(T:\operatorname{span}(e_1,\ldots,e_{n-1})\to\mathbb C^n\) with \(Te_j=e_{j+1}\). Indeed a nonzero vector and its one-step shift cannot be proportional (compare their first and last nonzero coordinates). Consequently, for \(k\le n+1\) every test subspace contains a nonzero rank-one matrix, yielding \(c_k=1\). For \(k\ge n+2\) the shift graph is admissible and rank-one-free, so compactness of its unit sphere and continuity of \(R\) imply \(c_k<1\).

**5. Complex optimal small-ratio subspaces.** Suppose every nonzero element of a complex linear subspace \(E\) has equal nonzero singular values. Again first-row projection gives a graph over \(U\subset\mathbb C^n\) with linear map \(T:U\to\mathbb C^n\). Equality of singular values gives \(\|Tu\|=\|u\|\) and \(\langle u,Tu\rangle=0\) for every \(u\in U\). Complex polarization using \(u+v\) and \(u+iv\) forces \(\langle u,Tv\rangle=0\) for all \(u,v\in U\), so \(T(U)\subset U^\perp\). Since \(T\) is an isometry, \(\dim U\le\lfloor n/2\rfloor=d\). Conversely take any orthogonal \(d\)-planes \(U,V\subset\mathbb C^n\) and unitary isometry \(T:U\to V\); its graph has constant ratio \(\beta\).

For \(k\ge2n-d+1\), that graph is admissible, and the universal lower bound gives \(c_k=\beta\). For \(k\le2n-d\), any admissible space has dimension at least \(d+1\) and cannot consist entirely of equal-singular-value matrices. Moreover the infimum is **strictly above** \(\beta\): the function \(E\mapsto\sup_{\|A\|_2=1,A\in E}R(A)\) is continuous on the compact complex Grassmannian of \((d+1)\)-planes, and none of those planes has supremum \(\beta\). Larger-dimensional spaces contain \((d+1)\)-planes and cannot improve the bound. Combined with step 4, this proves the complete complex three-regime classification and the critical-index optimizer description.

## Verification
The proof directly checks the two singular-value equality cases, quantifier directions for the codimension restriction, maximal dimensions of rank-one-free and conformal subspaces, and Grassmannian attainment. A supplementary, standalone finite arithmetic/numerical checker reproduces the predicted exact-plateau witnesses and strict-ratio witnesses in sample dimensions and exponents; such finite tests do not establish any infinite-dimensional or all-size claim. The all-size assertion follows from the written proof.

## Relationship to prior work
Prochno (2026, arXiv:2611.08448) proves all-index **order-of-magnitude estimates** for square real Schatten Gelfand numbers in a prescribed exponent range, using rectangular matrix spaces as an ingredient; it does not state the exact two-row real/complex sequences or critical optimizer classifications. Hinrichs–Prochno–Vybíral (2021, arXiv:2011.06554) and Prochno–Strzelecki (2022, arXiv:2103.13050) give broad square-matrix bounds, not the present rectangular two-row threshold laws. Known rank-restricted matrix-space constructions and the earlier exact two-by-two endpoint are useful background, but neither by itself identifies the all-\(n\), both-fields Gelfand sequences and all bottom-critical optimizers. Literature searches are not proof of publication priority; equivalent older matrix-pencil or constant-rank results remain a risk.

## Limitations
The intermediate complex Gelfand numbers are only proved to lie strictly between the two exact endpoints; their numerical values are not determined. Dimensions with three or more rows, nonstandard matrix norms, and nonlinear measurement models are outside the claim. No independent mathematical audit has been performed; the originality comparison is best-knowledge and may miss a differently formulated older theorem.

## References
- J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448 (first submitted 2026-11-05), https://arxiv.org/html/2611.08448v2.
- A. Hinrichs, J. Prochno, J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554; Math. Ann. 380 (2021), https://arxiv.org/abs/2011.06554.
- J. Prochno, M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050; J. Approx. Theory 277 (2022), https://arxiv.org/abs/2103.13050.
