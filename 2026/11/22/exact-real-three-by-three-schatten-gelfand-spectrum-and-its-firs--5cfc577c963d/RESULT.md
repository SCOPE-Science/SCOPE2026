# Exact real three-by-three Schatten Gelfand spectrum and its first rank-one-free threshold

## Finding

For every \(0<p\le1\) and \(2\le q\le\infty\), all nine Gelfand numbers of the identity from the **real** three-by-three Schatten \(p\)-class to the Schatten \(q\)-class are exactly

\[
c_k(\mathcal S_p^3(\mathbb R)\hookrightarrow\mathcal S_q^3(\mathbb R))=
\begin{cases}
1,&1\le k\le4,\\
2^{1/q-1/p},&5\le k\le8,\\
3^{1/q-1/p},&k=9.
\end{cases}
\]

The first strict decrease occurs at **index five**, where the codimension-four test space of traceless symmetric matrices attains the sharp bound. The new first-transition and interior-plateau values are \(k=4,5,6,7\); the penultimate value at \(k=8\) and terminal value at \(k=9\) follow also from previously published endpoint results [4]. The result is a fixed-dimension **exact** refinement of the asymptotic up-to-constants theorem of Prochno [1].

## Assumptions and scope

Matrices, subspaces, codimensions, and linear measurements are all **over \(\mathbb R\)**. For a nonzero real three-by-three matrix \(A\), write its three singular values \(s_1\ge s_2\ge s_3\ge0\) and set

\[
\|A\|_{\mathcal S_t}=\left(\sum_{j=1}^3s_j^t\right)^{1/t}\quad(0<t<\infty),
\qquad\|A\|_{\mathcal S_\infty}=s_1.
\]

The exact convention is \(1/\infty=0\), and for each integer \(1\le k\le9\)

\[
c_k=\inf_{\substack{F\le\mathbb R^{3\times3}\\\operatorname{codim}F<k}}
\ \sup_{0\ne A\in F}
\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}.
\]

Only nonzero test subspaces occur in this index range. The case \(0<p<1\) is quasi-Banach; the definition and arguments do not rely on norm convexity. The theorem is stated in the recent paper's parameter range, although some individual algebraic ingredients apply more broadly.

## Proof

**1. Singular-value bounds.** For any nonzero matrix of rank at most \(r\), with \(1\le r\le3\), the ordinary finite-dimensional power-mean inequality gives

\[
r^{1/q-1/p}\le\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}\le1.
\tag{1}
\]

Both endpoint values for a fixed rank are attained when its positive singular values are all equal. In particular a rank-one matrix has ratio one; a matrix of rank at most two has ratio at least \(2^{1/q-1/p}\), and an arbitrary nonzero matrix has ratio at least \(3^{1/q-1/p}\). These inequalities hold also when \(q=\infty\).

**2. Every codimension-three subspace contains rank one.** Let \(F\subset\mathbb R^{3\times3}\) have codimension \(m\le3\). Choose Hilbert–Schmidt annihilators \(B_1,\ldots,B_m\) and pad them with zeros up to three matrices. For \(u\in\mathbb R^3\), form the real three-by-three matrix \(D(u)\) whose \(i\)-th row is \((B_i^{\mathsf T}u)^{\mathsf T}\). The map \(u\mapsto\det D(u)\) is continuous and odd, because every row depends linearly on \(u\). On the connected unit sphere it must vanish at some unit vector \(u\): either it vanishes everywhere, or a path from a point to its antipode crosses zero. Hence \(D(u)\) has a nonzero real kernel vector \(v\). The nonzero rank-one matrix \(uv^{\mathsf T}\) satisfies

\[
\langle B_i,uv^{\mathsf T}\rangle_{\mathrm{HS}}=u^{\mathsf T}B_iv=(B_i^{\mathsf T}u)^{\mathsf T}v=0
\]

for all \(i\), and thus belongs to \(F\). If \(1\le k\le4\), every admissible test subspace has codimension at most three, so its restriction norm is one by (1), proving \(c_k=1\) for these indices.

**3. Every real matrix two-plane contains a singular matrix.** Let \(F\) have codimension at most seven, so \(\dim F\ge2\). Choose independent \(U,V\in F\). The continuous scalar function

\[
h(\theta)=\det(\cos\theta\,U+\sin\theta\,V)
\]

satisfies \(h(\theta+\pi)=-h(\theta)\), because determinants of real three-by-three matrices change sign under multiplication by \(-1\). Hence \(h\) vanishes for some \(\theta\). Linear independence ensures the corresponding matrix is **nonzero**, and its rank is at most two. Applying (1) proves

\[
c_k\ge 2^{1/q-1/p}\quad(1\le k\le8).
\tag{2}
\]

**4. A sharp five-dimensional witness.** Let

\[
F_0=\{A\in\mathbb R^{3\times3}:A=A^{\mathsf T},\ \operatorname{tr}A=0\}.
\]

It is a five-dimensional real subspace, hence \(\operatorname{codim}F_0=4\). For every nonzero \(A\in F_0\), real symmetry permits orthogonal diagonalization. Its eigenvalues can, after a simultaneous change of sign and permutation, be written \(M,-a,-b\), with \(M>0\), \(a,b\ge0\), and \(M=a+b\). Thus the singular values are \(M,a,b\). Since \(q\ge1\) and \(0<p\le1\), respectively,

\[
\|A\|_{\mathcal S_q}^q=M^q+a^q+b^q\le 2M^q,
\qquad
\|A\|_{\mathcal S_p}^p=M^p+a^p+b^p\ge2M^p.
\]

At \(q=\infty\), the corresponding statement is \(\|A\|_{\mathcal S_\infty}=M\). Therefore

\[
\sup_{0\ne A\in F_0}\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}
\le2^{1/q-1/p}.
\]

Equality is realized by \(\operatorname{diag}(1,-1,0)\in F_0\), so the restriction norm is exactly \(2^{1/q-1/p}\). As \(F_0\) is admissible for every \(k\ge5\), combine this bound with (2) to obtain all middle values \(5\le k\le8\).

**5. Final index.** By (1) every nonzero matrix gives ratio at least \(3^{1/q-1/p}\). For \(k=9\), the real one-dimensional subspace \(\mathbb R I_3\) is admissible and every nonzero element has three equal positive singular values. Hence \(c_9=3^{1/q-1/p}\). This finishes the classification. \(\square\)

## Verification

The two nonstandard incidence assertions are proved **for every allowed subspace** by odd real determinants: the auxiliary annihilator determinant in Step 2 forces rank-one intersection at codimension at most three, while the matrix-pencil determinant in Step 3 forces rank at most two in any two-plane. Both vanishing arguments are continuous real-variable arguments, not finite tests. The witness in Step 4 has dimension five, trace zero and explicit equality matrix; the final witness is one-dimensional. No external computation is needed to establish the theorem. The inequalities and all endpoint conventions have been checked analytically, including \(p=1\) and \(q=\infty\).

## Relationship to prior work

Prochno [1] establishes the complete **asymptotic order up to constants**, not fixed-size exact Gelfand numbers, for \(0<p\le1\) and \(2\le q\le\infty\). The works [2,3] give earlier comparison bounds, likewise not the above exact three-by-three sequence. A published parity theorem [4] already proves the real three-by-three **penultimate** value \(c_8=2^{1/q-1/p}\), as well as the known final-index value; these are credited, not presented as independently novel. A published first-drop theorem [5] proves the complex three-by-three plateau through index five, and determines both scalar fields at size two, but does not give the **real** three-by-three initial threshold or interior middle plateau. A related published two-row classification [6] concerns matrices with two rows, not the square three-row subspace geometry. The principal contribution is thus the real size-three **first drop at index five** and exact values at indices five through seven, yielding the first complete odd-size real spectrum.

The rank and power-mean arguments are classical ingredients, not independent discoveries. Searches do not establish mathematical publication priority; equivalent formulations could be hidden in historical matrix-space or Gelfand-width work.

## Limitations

The theorem applies only to real three-by-three matrices in the stated exponent range. It does not determine the complex three-by-three interior numbers, larger real matrix sizes, nonlinear measurement widths, or extremizer classification beyond the exhibited sharp subspace. The literature comparison is best-knowledge, not exhaustive, and no independent mathematical audit has been performed.

## References

1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1 (first public 2026-11-05), https://arxiv.org/abs/2611.08448.
2. A. Hinrichs, J. Prochno, J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554v1 (2020), https://arxiv.org/abs/2011.06554.
3. J. Prochno, M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050v1 (2021), https://arxiv.org/abs/2103.13050.
4. *A parity law for the penultimate Gelfand number of real Schatten embeddings*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-parity-law-for-the-penultimate-gelfand-number-of-real-schatten--fc1996e343be.
5. *First strict Gelfand-number drop for complex Schatten embeddings and a real–complex two-by-two gap*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-first-strict-gelfand-number-drop-for-complex-schatten-embeddings--7a7fcb96fc42.
6. *Parity and scalar-field thresholds for two-row Schatten Gelfand numbers*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-parity-and-scalar-field-thresholds-for-two-row-schatten-gelfand--184ac32d0d8a.
