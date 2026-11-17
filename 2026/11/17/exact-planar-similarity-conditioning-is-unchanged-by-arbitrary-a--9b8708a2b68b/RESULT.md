# Exact planar similarity conditioning is unchanged by arbitrary amplification

## Finding

For similar matrices \(A,B\in M_2(\mathbb C)\), define their optimal similarity condition number by
\[
 s(A,B)=\min_{Y\in GL_2(\mathbb C),\ YA=BY}\|Y\|\,\|Y^{-1}\|.
\]
The norms are spectral (Hilbert-space) operator norms. If \(K\) is **any nonzero complex Hilbert space**, not necessarily finite-dimensional, set \(A_K=A\otimes I_K\) and \(B_K=B\otimes I_K\), acting on \(\mathbb C^2\otimes K\), and define \(s_K(A,B)\) by the analogous infimum over bounded invertible intertwiners. Then
\[
 \boxed{s_K(A,B)=s(A,B).}
\]
Indeed, both sides are explicit. There are three exhaustive cases:

1. If \(A\) is scalar, similarity forces \(B=A\), and \(s(A,B)=1\).
2. If \(A\) has one eigenvalue \(\lambda\) but is not scalar, put \(a=\|A-\lambda I\|\) and \(b=\|B-\lambda I\|\). Then \(a,b>0\), and
\[
 \boxed{s(A,B)=\max\{a/b,b/a\}.}
\]
3. If \(A\) has two distinct eigenvalues \(\lambda_1,\lambda_2\), define \(P_A=(A-\lambda_2 I)/(\lambda_1-\lambda_2)\), \(P_B=(B-\lambda_2 I)/(\lambda_1-\lambda_2)\), and \(Q_A=2P_A-I\), \(Q_B=2P_B-I\). With \(a=\|Q_A\|\), \(b=\|Q_B\|\), one has \(a,b\geq1\) and
\[
 \boxed{s(A,B)=\max\{a/b,b/a\}.}
\]

In the notation of the quantitative similarity-cancellation problem, for every positive integer \(q\) and every real \(t\geq1\),
\[
 \boxed{\theta_{2,q}(t)=t},
\]
where \(\theta_{2,q}(t)\) is the supremum of \(s(A,B)\) among similar \(2\)-by-\(2\) matrices whose \(q\)-fold direct sums admit an intertwiner of condition number at most \(t\). The equality is attained.

## Assumptions and scope

All matrices are complex \(2\)-by-\(2\), with the Euclidean operator norm. The pair must be similar over \(\mathbb C\). A Hilbert amplification uses a nonzero complex Hilbert space \(K\) and the spatial tensor product; it does not assert an analogous result in Banach-space tensor norms or higher base dimensions. The spectral labels in the distinct-eigenvalue case agree for \(A\) and \(B\).

## Proof

**Step 1: A universal amplified lower bound.** If bounded invertible \(X\) satisfies \(XA_K=B_KX\), then for every polynomial \(p\),
\[
 X(p(A)\otimes I_K)=(p(B)\otimes I_K)X.
\]
Since \(\|C\otimes I_K\|=\|C\|\) for a nonzero Hilbert space \(K\), submultiplicativity gives
\[
 \max\!\left\{\frac{\|p(A)\|}{\|p(B)\|},\frac{\|p(B)\|}{\|p(A)\|}\right\}
 \leq\|X\|\,\|X^{-1}\|
\]
whenever the denominator norms are nonzero. In the distinct-eigenvalue case take \(p(z)=2(z-\lambda_2)/(\lambda_1-\lambda_2)-1\), giving the lower bound \(\max\{a/b,b/a\}\). In the nontrivial repeated-eigenvalue case take \(p(z)=z-\lambda\), giving the same bound for the nilpotent parts. The scalar case has the trivial lower bound one.

**Step 2: Exact normal form when the eigenvalues differ.** Choose unit eigenvectors \(v_+,v_-\) for \(A\) at \(\lambda_1,\lambda_2\). Rephase one so that \(\langle v_+,v_-\rangle=c\in[0,1)\) is real. The vectors
\[
 e_1=\frac{v_++v_-}{\sqrt{2(1+c)}},\qquad
 e_2=\frac{v_+-v_-}{\sqrt{2(1-c)}}
\]
form an orthonormal basis. Since \(Q_Av_+=v_+\) and \(Q_Av_-=-v_-\), the matrix of \(Q_A\) in this basis is
\[
 \begin{pmatrix}0&a\\a^{-1}&0\end{pmatrix},
 \qquad a=\sqrt{\frac{1+c}{1-c}}=\|Q_A\|\geq1.
\]
Apply the same construction to \(B\), obtaining an orthonormal basis with matrix \(\bigl(\begin{smallmatrix}0&b\\b^{-1}&0\end{smallmatrix}\bigr)\), \(b=\|Q_B\|\). In these two orthonormal coordinate systems,
\[
 D=\begin{pmatrix}b/a&0\\0&1\end{pmatrix}
\]
satisfies \(DQ_A=Q_BD\), hence also \(DA=BD\) after writing \(A=(\lambda_1+\lambda_2)I/2+(\lambda_1-\lambda_2)Q_A/2\). The associated global intertwiner is unitarily equivalent on its domain and codomain to \(D\), so
\[
 \|D\|\,\|D^{-1}\|=\max\{b/a,a/b\}.
\]
This attains the lower bound from Step 1.

**Step 3: The Jordan case.** If \(A\) has repeated eigenvalue \(\lambda\) and is not scalar, then \(N_A=A-\lambda I\neq0\) and \(N_A^2=0\). Consequently \(\operatorname{ran}N_A=\ker N_A\) is one-dimensional. Choosing unit vectors in the kernel and its orthogonal complement, with a suitable phase, puts \(N_A\) in the form
\[
 \begin{pmatrix}0&a\\0&0\end{pmatrix},\qquad a=\|N_A\|>0.
\]
The analogous form for \(N_B\) has upper-right entry \(b>0\). The same diagonal matrix \(D=\operatorname{diag}(b/a,1)\) intertwines the nilpotent parts and therefore \(A,B\), with condition number \(\max\{a/b,b/a\}\). In the scalar case \(A=B\), so the identity is optimal.

**Step 4: Amplification equality.** In each case Steps 2–3 give a concrete two-dimensional optimal intertwiner \(Y\). Then \(Y\otimes I_K\) is bounded invertible and intertwines the amplified operators, with exactly the same condition number. Together with Step 1 this proves \(s_K(A,B)=s(A,B)\), even for infinite-dimensional \(K\).

**Step 5: The exact amplification envelope.** Every pair in the definition of \(\theta_{2,q}(t)\) has \(s(A,B)\leq t\) by Step 4, hence \(\theta_{2,q}(t)\leq t\). For the reverse inequality take
\[
 Q_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 Q_t=\begin{pmatrix}0&t\\t^{-1}&0\end{pmatrix}.
\]
Both have eigenvalues \(1,-1\), so are similar. Their involution norms are \(1,t\), hence \(s(Q_1,Q_t)=t\) by Step 2, and the same is true after any nonzero amplification. This pair belongs to the defining set and attains \(t\). The theorem follows. \(\square\)

## Verification

The key canonical-form identities can be checked exactly without limiting arguments. The accompanying `verify.py` runs 1,200 exact rational assertions for the distinct-eigenvalue and Jordan forms, then 1,792 floating-point assertions on random unitary conjugates with complex phases (2,992 assertions total). Run with a standard Python 3 interpreter:

```sh
python verify.py
```

These diagnostics verify finitely many identities; the full statement for all matrices and all Hilbert multiplicity spaces follows only from the proof above. The last step constructs a witness for every \(t\geq1\), so it is an attainment result rather than numerical interpolation.

## Relationship to prior work

Jiang, Ma, Shi and Zhang introduced the doubled similarity number and its envelope, and asked whether amplification preserves the exact optimum. Their Remark 4.2 suggests equality. Aouichaoui subsequently defined \(\theta_{n,q}\) for arbitrary multiplicities, proved finiteness and near-isometric cancellation at fixed matrix size, and exhibited strict improvement under doubling in larger, varying dimensions. The result here answers the previously unquantified smallest nontrivial base dimension: amplification of **any** multiplicity leaves the complete optimal condition number unchanged, with an explicit all-Jordan-type formula.

Demmel studied the least-conditioned diagonalizer of a single matrix, relating it to spectral projections. That is essential classical context for the two-line geometry above; it is not itself a comparison theorem for least-conditioned similarities between **two arbitrary matrices**, including the Jordan case, nor an amplification theorem. Marcoux, Sarkowicz and Zhang studied **distances between unitary orbits** of amplifications, a different optimization functional. These comparisons do not establish absolute publication priority.

## Limitations

The result depends on the Hilbert operator norm, a common complex base dimension two, and similarity of the two matrices. It does not claim exact amplification invariance for \(3\)-by-\(3\) or larger matrices, or for simultaneous intertwining of families. In fact, known higher-dimensional constructions show that the analogous unconditional equality fails in general when the base size is allowed to grow. The spectral-projection normal form is elementary, so an earlier equivalent planar condition-number formula under different terminology remains a genuine priority risk.

## References

1. C. Jiang, M. Ma, R. Shi and Y. Zhang, *Kaplansky's second test problem in operator algebras*, arXiv:2607.20593v1 (2026-07-22), especially Definition 4.1 and Remark 4.2. https://arxiv.org/abs/2607.20593
2. M. A. Aouichaoui, *Similarity cancellation and primitive operator roots*, arXiv:2611.01298v1 (2026-10-31), especially Theorem 1.3, Proposition 2.2 and Corollary 5.1. https://arxiv.org/html/2611.01298v1
3. J. W. Demmel, *The Condition Number of Similarities that Diagonalize Matrices*, University of California, Berkeley, Technical Report UCB/CSD-83-127 (1983). https://www2.eecs.berkeley.edu/Pubs/TechRpts/1983/CSD-83-127.html
4. L. W. Marcoux, P. Sarkowicz and Y. Zhang, *Kaplansky's problem and unitary orbits in matrix amplifications*, arXiv:2508.13834v1 (2025-08-19). https://arxiv.org/html/2508.13834v1
