# Sharp half-Schatten boundary for the Cesàro Mellin square defect

## Finding

The natural multiplicative defect of the sampled Mellin calculus associated with two classical Cesàro factors has a sharp quadratic singular-value law. Specifically, there are constants \(0<c<C_0<\infty\), independent of the singular-value index, such that
\[
\frac{c}{n^2}\le s_n(E)\le\frac{C_0}{n^2}\qquad(n\ge1).
\]
Therefore, for every real \(p>0\),
\[
E\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12,
\qquad E\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}.
\]
Here \(\mathcal S_p\) includes quasi-Banach Schatten ideals for \(0<p<1\), and \(\mathcal S_{1/2,\infty}\) denotes the weak ideal defined by \(\sup_n n^2s_n(E)<\infty\). The full decay order, rather than a trace-class consequence, is the finding.

## Assumptions and scope

Work on complex \(\ell^2(\mathbb N)\) with standard basis indexed by positive integers. Define the classical Cesàro operator
\[
C_{a,b}=\frac{\mathbf1_{\{b\le a\}}}{a}.
\]
Let \(\omega(t)=\mathbf1_{(0,1]}(t)\). Its multiplicative convolution with itself is \((\omega\star\omega)(t)=\mathbf1_{(0,1]}(t)(-\log t)\). The sampled Mellin operator associated with this kernel is
\[
(W_2)_{a,b}=\frac{\mathbf1_{\{b\le a\}}}{a}\log\frac ab.
\]
Both operators are bounded by the classical Hardy inequality and the sampled Mellin calculus (alternatively, boundedness of \(W_2\) follows from \(W_2=C^2-E\) after the compact estimate below). Put \(E=C^2-W_2\). As usual \(s_n\) means the \(n\)-th decreasing singular value, with multiplicity. No claims are made for arbitrary Mellin kernels or for an exact leading singular-value coefficient.

## Proof

**1. Exact triangular factorization.** Write \(H_a=\sum_{j=1}^{a}j^{-1}\), \(H_0=0\), and let \(\gamma\) be Euler's constant. Direct matrix multiplication gives, for \(a\ge b\),
\[
E_{a,b}=\frac{H_a-H_{b-1}-\log(a/b)}{a}.
\]
Set
\[
h_a=H_a-\log a-\gamma,\qquad
 g_b=\gamma+\log b-H_{b-1}.
\]
Thus
\[
E_{a,b}=\frac{h_a+g_b}{a}\mathbf1_{\{b\le a\}},
\qquad h_a+g_a=\frac1a.
\]
Elementary integral comparisons for the harmonic numbers give \(0<h_a\le a^{-1}\) and \(0<g_a\le a^{-1}\). In particular, on a dyadic block whose indices are comparable with \(2^r\), the two coefficients \(h_a/a\) and \(g_b/a\) are \(O(2^{-2r})\).

**2. Uniform upper singular-value bound.** Partition \(\mathbb N\) into \(I_r=\{2^r,\ldots,2^{r+1}-1\}\), with projections \(P_r\), and split
\[
E=B+R,\qquad B=\bigoplus_{r\ge0}P_rEP_r,
\quad R=\sum_{r>s\ge0}P_rEP_s.
\]
The latter sum converges in every quasi-Schatten ideal, as shown below. For \(m_r=2^r\), let \(L_{m_r}\) be the lower-triangular matrix with entries \(\mathbf1_{\{i\ge j\}}\). On \(I_r\),
\[
P_rEP_r=\operatorname{diag}(h_a/a)L_{m_r}
 +\operatorname{diag}(1/a)L_{m_r}\operatorname{diag}(g_b).
\]
The exact singular values of \(L_m\), obtained by diagonalizing the tridiagonal positive matrix \((L_m^{-1})^*L_m^{-1}\), are
\[
s_j(L_m)=\left[2\sin\frac{(2j-1)\pi}{4m+2}\right]^{-1}
\le \frac{Cm}{j}\qquad(1\le j\le m).
\]
Applying \(s_{u+v-1}(X+Y)\le s_u(X)+s_v(Y)\) to the two summands and using the dyadic coefficient bounds gives
\[
s_j(P_rEP_r)\le C\frac{2^{-r}}{j}\quad (1\le j\le 2^r).
\]
The singular values of a Hilbert direct sum are the union of those of its blocks. Its distribution therefore satisfies, for all \(t>0\),
\[
N_B(t):=\#\{j:s_j(B)>t\}
\le\sum_{r\ge0}\min\left(2^r,\frac{C2^{-r}}t\right)
\le C' t^{-1/2}.
\]
This is obtained by splitting the geometric sum near \(2^r=t^{-1/2}\) (for \(t\) above a fixed constant the count is zero). Hence \(s_n(B)=O(n^{-2})\).

For \(r>s\), the exact cross-block factorization is a sum of two rank-one operators,
\[
P_rEP_s=\bigl(h_a/a\bigr)_{a\in I_r}
 \otimes\bigl(1\bigr)_{b\in I_s}^{*}
 +\bigl(1/a\bigr)_{a\in I_r}
 \otimes\bigl(g_b\bigr)_{b\in I_s}^{*}.
\]
Their sole nonzero singular values are bounded respectively by
\[
C2^{-(3r-s)/2}\quad\text{and}\quad C2^{-(r+s)/2}.
\]
For every \(p>0\), the sums of their \(p\)-th powers over \(r>s\ge0\) converge. By the ideal triangle inequality when \(p\ge1\), and the \(p\)-quasi-triangle inequality when \(0<p<1\), it follows that \(R\in\mathcal S_p\) for **every** \(p>0\). In particular \(R\in\mathcal S_{1/3}\), which implies \(s_n(R)=O(n^{-3})\). A final singular-value sum inequality yields \(s_n(E)=O(n^{-2})\).

**3. Uniform lower singular-value bound.** Fix \(n\ge1\) and compress \(E\) to the contiguous set \(J_n=\{n,n+1,\ldots,2n-1\}\). Let \(E^{(n)}=P_{J_n}EP_{J_n}\) and let \(\Delta\) be the \(n\)-by-\(n\) first-difference matrix, \((\Delta z)_a=z_a-z_{a-1}\), with \(z_{n-1}=0\). Write \(D=\operatorname{diag}(a)_{a\in J_n}\). Then the preceding factorization, followed by subtraction of consecutive rows, gives the **exact identity**
\[
\Delta D E^{(n)}=D^{-1}(I-K),
\]
where \(K\) is strictly lower triangular and
\[
K_{a,b}=a\log\frac{a}{a-1}-1
\quad(a>b),\qquad K_{a,b}=0\quad(a\le b).
\]
The elementary inequality \(0<a\log(a/(a-1))-1\le1/(a-1)\) gives \(0\le K_{a,b}\le1/n\) in the block. Every row and column sum of \(K^j\) is at most \(\binom nj n^{-j}\le1/j!\) by counting strictly increasing chains of length \(j\). The Schur norm test yields \(\|K^j\|\le1/j!\), so
\[
\|(I-K)^{-1}\|\le\sum_{j\ge0}\|K^j\|\le e.
\]
Consequently
\[
(E^{(n)})^{-1}=(I-K)^{-1}D\Delta D,
\qquad
\|(E^{(n)})^{-1}\|\le8e n^2,
\]
using \(\|D\|\le2n\) and \(\|\Delta\|\le2\). Compression cannot increase ordered singular values, so
\[
s_n(E)\ge s_n(E^{(n)})\ge\frac{1}{8e n^2}.
\]
Combining this with Step 2 proves the two-sided estimate.

**4. Exact Schatten endpoint.** By definition \(E\in\mathcal S_p\) precisely if \(\sum_n s_n(E)^p<\infty\). The two-sided power bound gives convergence exactly for \(2p>1\). At \(p=1/2\), the sum diverges like the harmonic series, whereas the weak quasi-norm \(\sup_n n^2s_n(E)\) is finite.

## Verification

The accompanying standalone Python checker `check_mellin_square.py` calculates the matrix defect from independent finite Cesàro products and independently from the harmonic-number and factorization formulas. With exact rational arithmetic it verifies positivity and elementary finite block arithmetic across the stated test ranges; when NumPy is available it additionally checks the matrix inverse identity and finite lower singular-value bound. Execute `python3 check_mellin_square.py`. The observed output was `MELLIN_SQUARE_DEFECT_FINITE_OK 456187` (456,187 finite assertions). The entire infinite-dimensional statement rests on the preceding proof, not these finite tests.

## Relationship to prior work

Bellavita and Stylogiannis introduced sampled-ratio matrices and established a Hilbert–Schmidt multiplicativity defect for their full kernel algebra (arXiv:2609.09453v1, Theorem 1.2 and Section 11). Their article names Schatten refinements as a natural question. A pre-existing related note, *Trace-class Mellin semigroup defects and zeta traces for Cesàro powers* (published-finding corpus 2026/09/19, identified below), already proves \(C^m-W_m\in\mathcal S_1\) and \(\operatorname{Tr}(C^2-W_2)=\zeta(2)\); these are **not** claimed as new. That note expressly leaves \(0<p<1\) unclassified. The result here establishes the exact optimal singular-value order and hence the previously unaddressed half-Schatten boundary for the specific square defect. Bellavita, Dellepiane and Stylogiannis (arXiv:2503.21930) treat the different class of row-constant Rhaly matrices, and only characterize their \(\mathcal S_q\)-membership for \(q>1\); their theorem does not imply the present result for a non-terraced defect.

## Limitations

The two-sided estimates do not identify a limit of \(n^2s_n(E)\), and no claim is made for general sampled Mellin products or higher Cesàro powers. Equivalence to an older theorem in the theory of discrete Hardy operators or triangular matrix approximation numbers remains a publication-priority risk. Related works were inspected and searched by aliases, but a negative literature search is not a mathematical proof of publication priority. Independent mathematical validation has not been performed.

## References

1. C. Bellavita and G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1 (public September 8, 2026), https://arxiv.org/abs/2609.09453.
2. *Trace-class Mellin semigroup defects and zeta traces for Cesàro powers* (2026), previously available proof at https://github.com/published-finding corpus/2026/blob/main/2026/9/19/SCOPE-zeta-trace-cesaro-mellin-defects--b8e60639c683/RESULT.md.
3. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930v3 (2025), https://arxiv.org/abs/2503.21930.
