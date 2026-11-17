# Pointwise quadratic singular-value bounds for the second Cesàro–Mellin defect

## Theorem (precise new contribution)
On complex \(\ell^2(\mathbb N)\), using positive integer indices, put
\[
 C_{ab}=a^{-1}\mathbf1_{b\le a},\quad (W_2)_{ab}=a^{-1}\log(a/b)\mathbf1_{b\le a},\quad E=C^2-W_2.
\]
There are absolute positive constants \(c,C_0\) such that **each individual singular value**, in nonincreasing order with multiplicity, satisfies
\[
\boxed{c n^{-2}\le s_n(E)\le C_0n^{-2}\quad\text{for every }n\ge1.}
\]
In particular \(E\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}\), and \(E\in\mathcal S_p\) exactly when \(p>1/2\). **The quasi-Schatten threshold and weak-endpoint upper bound were already established in earlier published work on this identical operator.** The new contribution claimed here is the uniform **pointwise lower bound** \(s_n(E)\ge c n^{-2}\), completing a two-sided singular-number order, rather than re-establishing the previously known threshold. No limit of \(n^2s_n(E)\) is asserted.

## Exact formulas and proof
The Cesàro matrix is bounded on \(\ell^2\); the following estimates also prove the boundedness and compactness of \(E\). Let \(H_k=\sum_{j=1}^k j^{-1}\), \(H_0=0\), and let \(\gamma\) denote Euler's constant. Direct summation gives
\[
 E_{ab}=\frac{\mathbf1_{b\le a}}a\left(H_a-H_{b-1}-\log\frac ab\right).
\]
Write \(h_a=H_a-\log a-\gamma\), \(g_b=\gamma+\log b-H_{b-1}\). Elementary integral comparison yields \(0<h_a\le 1/a\), \(0<g_b\le1/b\) and \(h_a+g_a=1/a\); hence
\[
 E_{ab}=a^{-1}(h_a+g_b)\mathbf1_{b\le a}.
\tag{1}
\]

**Upper pointwise bound.** Partition the indices into dyadic intervals \(I_r=[2^r,2^{r+1}-1]\cap\mathbb N\). Write \(E=B+R\), where \(B=\bigoplus_r P_{I_r}EP_{I_r}\) and \(R=\sum_{r>s}P_{I_r}EP_{I_s}\). For \(m=2^r\), the diagonal block is
\[
 B_r=\operatorname{diag}(h_a/a)L_m+\operatorname{diag}(1/a)L_m\operatorname{diag}(g_b),
\]
where \(L_m\) is the lower-triangular all-ones matrix. Its singular numbers satisfy
\[
 s_j(L_m)=\left(2\sin\frac{(2j-1)\pi}{4m+2}\right)^{-1}\le C m/j.
\]
The elementary two-term singular-number inequality and (1) imply \(s_j(B_r)\le C2^{-r}/j\) for \(1\le j\le2^r\). The direct-sum counting function obeys
\[
 \#\{j:s_j(B)>t\}\le\sum_{r\ge0}\min(2^r,C2^{-r}/t)\le C't^{-1/2};
\]
splitting the geometric sum at \(2^r\asymp t^{-1/2}\) proves the last bound. Thus \(s_n(B)=O(n^{-2})\).

When \(r>s\), every cross-block entry lies below the diagonal, and (1) decomposes the block into **two rank-one operators**:
\[
 P_{I_r}EP_{I_s}=(h_a/a)_{a\in I_r}\otimes(1)_{b\in I_s}^*+(1/a)_{a\in I_r}\otimes(g_b)_{b\in I_s}^*.
\]
Their singular norms are at most \(C2^{-(3r-s)/2}\) and \(C2^{-(r+s)/2}\). For each \(p>0\), the sum of their \(p\)-th powers over \(r>s\ge0\) converges. The Schatten (quasi-)triangle inequality gives \(R\in\mathcal S_p\) for **every** positive \(p\), in particular \(s_n(R)=O(n^{-3})\) by choosing \(p=1/3\). Weyl's singular-number sum inequality implies \(s_n(E)=O(n^{-2})\).

**New lower pointwise bound.** For each \(n\ge1\), let \(J_n=\{n,\ldots,2n-1\}\) and compress \(E\) to \(E^{(n)}=P_{J_n}EP_{J_n}\), regarded as an \(n\times n\) lower-triangular matrix. Put \(D=\operatorname{diag}(a)_{a\in J_n}\) and let \(\Delta\) be the first-difference operator on the rows, with zero boundary preceding row \(n\). Taking successive differences of (1) yields the **exact identity**
\[
 \Delta D E^{(n)}=D^{-1}(I-K),\qquad
 K_{ab}=\begin{cases}a\log\!\frac a{a-1}-1,&a>b,\\0,&a\le b.\end{cases}
\tag{2}
\]
Here \(K\) is strictly lower triangular. For \(a\ge n+1\), \(0<K_{ab}\le 1/(a-1)\le1/n\). Each entry of \(K^j\) is a sum over strictly increasing index chains; consequently every absolute row and column sum of \(K^j\) is at most \(\binom nj n^{-j}\le1/j!\). The Schur bound shows \(\|K^j\|\le1/j!\) and therefore
\[
 \|(I-K)^{-1}\|\le\sum_{j\ge0}\|K^j\|\le e.
\]
Equation (2) gives
\[
 (E^{(n)})^{-1}=(I-K)^{-1}D\Delta D,
\quad \|(E^{(n)})^{-1}\|\le e(2n)(2)(2n)=8e n^2.
\]
Thus \(s_n(E^{(n)})\ge(8e n^2)^{-1}\). The compression inequality \(s_n(P_{J_n}EP_{J_n})\le s_n(E)\) proves the theorem with \(c=1/(8e)\). This is a **pointwise, all-rank** estimate, not just an eigenvalue-moment or Schatten-divergence argument.

The two-sided bounds give the endpoint statements by summing \(s_n(E)^p\). Their mathematical validity does not rest on finite numerical tests.

## Relationship to prior results, significance, and limits
The October 25, 2026 finding *Sharp quasi-Schatten threshold for the Cesàro–Mellin square defect* and the November 1, 2026 finding *Sharp quasi-Schatten threshold for the second Cesàro–Mellin defect* treat precisely \(D=C^2-W_2\). Both prove \(D\in\mathcal S_p\iff p>1/2\); the latter also establishes the weak endpoint and an \(O(n^{-2})\) upper singular-number estimate. The October result derives nonmembership through divergent eigenvalue sums, which **does not imply** a uniform lower bound for each singular number. The November result likewise proves sharp nonmembership through eigenvalue summability, without the all-rank lower bound supplied in (2). Those earlier claims and their Fredholm determinant formulas are credited, not presented here as new. The source article by Bellavita–Stylogiannis, arXiv:2609.09453, introduces the sampled Mellin calculus and its general Hilbert–Schmidt defect. The new sharp two-sided pointwise law refines that operator-ideal work and identifies the full distribution's noncollapse scale; it is not an exact leading asymptotic coefficient.

Scope is the single classical square defect on \(\ell^2(\mathbb N)\), not arbitrary convolution kernels, higher powers or row-constant Rhaly matrices. A historical approximation-number theorem could subsume the pointwise bound under different terminology; priority remains a qualified best-of-knowledge comparison. The finite checker `check_mellin_square.py` corroborates formulas but does not prove an infinite-rank theorem.

Sources: [October 25 prior result](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-quasi-schatten-threshold-for-the-ces-ro-mellin-square-defe--3f3f70ce03a7); [November 1 prior result](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-sharp-quasi-schatten-threshold-for-the-second-ces-ro-mellin-defe--11eeafffaf9b); [Bellavita–Stylogiannis](https://arxiv.org/abs/2609.09453).
