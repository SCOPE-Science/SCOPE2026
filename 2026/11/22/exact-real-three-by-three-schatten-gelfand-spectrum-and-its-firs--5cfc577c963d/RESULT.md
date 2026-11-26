# Exact real three-by-three Schatten Gelfand spectrum and its first rank-one-free threshold

## Finding

For real three-by-three matrices and every \(0<p\le1\), \(2\le q\le\infty\), the Gelfand numbers of the Schatten embedding are
\[
c_k(\mathcal S_p^3(\mathbb R)\hookrightarrow\mathcal S_q^3(\mathbb R))=
\begin{cases}
1,&1\le k\le4,\\
2^{1/q-1/p},&5\le k\le8,\\
3^{1/q-1/p},&k=9.
\end{cases}
\]
The key sharp bound is at the first drop, \(k=5\): the five-dimensional space of real traceless symmetric matrices attains \(2^{1/q-1/p}\). The subsequent plateau follows by monotonicity from this bound and the known \(c_8\). The initial plateau through \(k=4\) also follows from the two-row result [6] by padding with a zero row. The penultimate and final values are covered by [4]; \(c_7\) can also be recovered by combining the classical real skew-symmetric normal form with \(c_8\). The full sequence is given for context, not as nine independent novelty claims.

## Assumptions and scope

All matrices, measurements and linear subspaces are real. Denote the singular values by \(s_1\ge s_2\ge s_3\ge0\) and let \(\|A\|_{\mathcal S_t}=(\sum_j s_j^t)^{1/t}\) for \(0<t<\infty\) and \(\|A\|_{\mathcal S_\infty}=s_1\). Set \(1/\infty=0\). For \(1\le k\le9\),
\[
c_k=\inf_{\substack{F\le\mathbb R^{3\times3}\\\operatorname{codim}F<k}}
\sup_{0\ne A\in F}\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}.
\]
Only nonzero test subspaces occur. The case \(p<1\) uses a quasi-norm; no norm convexity for \(\mathcal S_p\) is assumed.

## Proof

**Singular-value bounds.** If \(A\ne0\) has rank at most \(r\), then by the power-mean inequality applied to its singular values padded with zeros to length \(r\),
\[
r^{1/q-1/p}\le \frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}\le1.
\]
The lower bound is attained at rank \(r\) with all positive singular values equal; the upper bound is attained at rank one. The bounds also hold for \(q=\infty\).

**Initial plateau.** Let \(F\subset\mathbb R^{3\times 3}\) have codimension at most three. Choose Hilbert–Schmidt annihilators \(B_1,B_2,B_3\), padding with zero matrices if necessary. The matrix \(D(u)\) with rows \(u^{\mathsf T}B_i\) has determinant odd in \(u\). This continuous determinant vanishes somewhere on the unit sphere by connectedness and the antipodal sign change. At such a unit vector \(u\), choose a nonzero \(v\) in the kernel of \(D(u)\). Then \(uv^{\mathsf T}\ne0\) and \(\langle B_i,uv^{\mathsf T}\rangle=u^{\mathsf T}B_iv=0\), so \(F\) contains a rank-one matrix. Thus every admissible space at \(k\le4\) has restriction norm one.

**Lower bound through index eight.** In any real matrix space of dimension at least two, choose linearly independent \(U,V\). The determinant of \(\cos\theta\,U+\sin\theta\,V\) is continuous and odd under \(\theta\mapsto\theta+\pi\), so it vanishes for some \(\theta\). The matrix is nonzero by linear independence, and its rank is at most two. All admissible spaces through \(k=8\) have dimension at least two, giving \(c_k\ge2^{1/q-1/p}\) for those indices. This is also the odd-determinant argument behind the known penultimate lower bound [4].

**Sharp upper bound at index five.** The real symmetric traceless subspace has dimension five and codimension four. For every nonzero matrix in it, the eigenvalues, after permutation and an overall sign change if needed, are \(M,-a,-b\) with \(a,b\ge0\) and \(M=a+b>0\). Its singular values are \(M,a,b\). Because \(q\ge1\) and \(p\le1\), for finite \(q\) we have
\[
\|A\|_{\mathcal S_q}^q=M^q+a^q+b^q\le 2M^q,
\qquad
\|A\|_{\mathcal S_p}^p=M^p+a^p+b^p\ge2M^p.
\]
For \(q=\infty\) the numerator is exactly \(M\). Thus the restriction norm is at most \(2^{1/q-1/p}\), and \(\operatorname{diag}(1,-1,0)\) attains equality. This space is admissible at \(k=5\) and at all larger indices, proving the middle plateau together with the preceding lower bound.

**Final index.** Every nonzero matrix has ratio at least \(3^{1/q-1/p}\). The admissible line \(\mathbb R I_3\) attains that bound at \(k=9\).

## Verification

The proof addresses all admissible subspaces analytically. Both determinant vanishing arguments use continuous real odd functions and produce nonzero witnesses. The symmetric witness has exact codimension four, and equality in the ratio is explicit, including at \(p=1\) and \(q=\infty\). No finite experiment is required.

## Relationship to prior work

Prochno [1, Theorem A and Remark 1.1] gives asymptotic order up to constants in this exponent range. The earlier works [2,3] likewise provide comparison bounds, not the sharp first-drop value here.

The exact rectangular theorem [6] gives \(c_4=1\) for real \(2\times3\) matrices. Inserting a zero row embeds that space into the square space, isometrically for both quasi-norms. Intersecting an admissible square test subspace with the rectangular copy cannot increase codimension measured in the copy. Therefore its restriction norm is at least the rectangular \(c_4\), giving \(c_4=1\) for the square space by the upper bound one. The rectangular theorem does not give the opposite, sharp upper bound at square index five. The odd-size result [4] gives \(c_8=2^{1/q-1/p}\) and \(c_9=3^{1/q-1/p}\); monotonicity already gives the lower bound \(2^{1/q-1/p}\) for \(k\le8\). In addition, the real skew-symmetric three-dimensional subspace is admissible at \(k=7\): each nonzero element has singular values \((s,s,0)\) by the real skew-symmetric block form. This gives \(c_7=2^{1/q-1/p}\) together with the known lower bound.

The distinct supported claim is the sharp value at the first drop, \(c_5=2^{1/q-1/p}\), with the symmetric traceless space as an explicit optimizer. In particular \(c_6\) follows from \(c_5\), \(c_8\) and monotonicity, without a new argument at index six. The complex size-three plateau instead includes index five [5], so the first drop gives a genuine scalar-field contrast. No claim of historical priority for the individual matrix-space ingredients is made.

## Limitations

The exact sequence is for real \(3\times3\) matrices in the stated exponent range. No claim is made about complex interior values beyond the cited comparison, larger real sizes, nonlinear measurements or the classification of all optimizers. The literature comparison is bounded; older work under alternative terminology may contain an equivalent sharp upper bound.

## References

1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, [arXiv:2611.08448v1](https://arxiv.org/abs/2611.08448v1).
2. A. Hinrichs, J. Prochno and J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, [arXiv:2011.06554](https://arxiv.org/abs/2011.06554).
3. J. Prochno and M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, [arXiv:2103.13050](https://arxiv.org/abs/2103.13050).
4. *A parity law for the penultimate Gelfand number of real Schatten embeddings*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-parity-law-for-the-penultimate-gelfand-number-of-real-schatten--fc1996e343be).
5. *First strict Gelfand-number drop for complex Schatten embeddings and a real–complex two-by-two gap*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-first-strict-gelfand-number-drop-for-complex-schatten-embeddings--7a7fcb96fc42).
6. *Parity and scalar-field thresholds for two-row Schatten Gelfand numbers*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-parity-and-scalar-field-thresholds-for-two-row-schatten-gelfand--184ac32d0d8a).
