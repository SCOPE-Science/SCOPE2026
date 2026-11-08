# Three-level self-Fourier spectra of even-dimensional finite quadratic cones

## Finding
Let \(V\) be a vector space of dimension \(2m\) over \(\mathbb F_q\), where \(m\ge2\) and \(q\) is any prime power, including powers of two. Let \(Q:V\to\mathbb F_q\) be a nondegenerate quadratic form, let \(B(x,y)=Q(x+y)-Q(x)-Q(y)\) be its nondegenerate polar form, and let \(C=\{x\in V:Q(x)=0\}\), **including the origin**. Fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\). On complex-valued functions indexed by \(C\), define the square, ambient-unitarily-normalized self-Fourier sampler
\[
T_{x,y}=q^{-m}\psi(B(x,y)),\qquad x,y\in C.
\]
Write \(\varepsilon=+1\) for the split (hyperbolic) quadratic type and \(\varepsilon=-1\) for the nonsplit (elliptic) type. Put
\[
N=q^{2m-1}+\varepsilon(q-1)q^{m-1},\quad
P=\frac{N-1}{q-1},\quad
c=\frac{q^{2m}-1}{q^2-1},\quad b=(q-2)P,\quad a=P+1-c.
\]
Then \(|C|=N\), and **the complete singular-value multiset of \(T\)** is
\[
\boxed{1\ \text{with multiplicity }a,\qquad
q^{-1/2}\ \text{with multiplicity }b,\qquad
q^{-1}\ \text{with multiplicity }c.}
\]
Here \(a,c\ge1\), and the middle level is absent when \(q=2\). In particular, every sampler is invertible, and its sharp Euclidean singular-value condition number is exactly \(q\), **independent of dimension and quadratic type**. The dimension of the perfectly concentrated subspace—signals supported on \(C\) whose ambient unitary Fourier transforms are also supported on \(C\)—is exactly \(a\).

## Assumptions and scope
All vector spaces and quadratic forms are over the stated finite field. Nondegenerate means that the polar bilinear form \(B\) is nondegenerate, including in characteristic two. In every even dimension there are exactly two isometry types, distinguished by \(\varepsilon\). All norms on \(\mathbb C^C\) use counting measure, so \(q^{-m}\) is the normalization that makes the ambient Fourier transform on \(\mathbb C^V\) unitary. The same \(B\) identifies \(V\) and its Pontryagin dual. The theorem is only about **self-restriction to the full zero cone**; deleting the origin or sampling a nonzero level set changes the problem. The case \(m=1\) is not part of the assertion.

## Proof
**Step 1: exact Fourier transform of the cone.** The standard quadratic Gauss sum for nondegenerate even-dimensional forms is
\[
\sum_{y\in V}\psi(tQ(y))=\varepsilon q^m\qquad(t\in\mathbb F_q^\times),
\]
including characteristic two. This is checked by decomposing \(Q\) into hyperbolic planes and, for nonsplit type, one anisotropic two-plane. The hyperbolic plane contributes \(q\); the anisotropic plane contributes \(-q\). In odd characteristic the usual one-dimensional Gauss factors give the same product because the dimension is even. Completing the square by translation \(y\mapsto y+t^{-1}w\), a valid identity also in characteristic two, gives
\[
\sum_{y\in V}\psi(tQ(y)+B(w,y))=\varepsilon q^m\psi(-Q(w)/t).
\]
Character orthogonality applied to \(1_{Q(y)=0}\) therefore yields, for every \(w\in V\),
\[
\sum_{y\in C}\psi(B(w,y))=
q^{2m-1}\mathbf1_{w=0}+\varepsilon q^{m-1}
\bigl(q\mathbf1_{Q(w)=0}-1\bigr).
\tag{1}
\]
Taking \(w=0\) gives the stated value \(N\). For isotropic \(x,z\), the condition \(Q(x-z)=0\) is equivalent to \(B(x,z)=0\). Thus the Gram matrix \(G=(q^mT)(q^mT)^*\) has the exact form
\[
G=q^{2m-1}I+\varepsilon q^{m-1}(qA-J),
\tag{2}
\]
where \(A_{x,z}=\mathbf1_{B(x,z)=0}\), while \(J\) is the all-ones matrix on \(C\). This fixes all Fourier signs and normalizations.

**Step 2: decompose by isotropic projective rays.** There are \(P\) nonzero projective isotropic points, each contributing exactly \(q-1\) vectors, and one separate origin. On the subspace of functions whose sum on each nonzero ray is zero and whose origin value is zero, both \(A\) and \(J\) vanish. Its dimension is \(P(q-2)\), and by (2) the eigenvalue of \(G\) is \(q^{2m-1}\).

On functions constant on each ray, let \(M\) denote the projective \(P\)-by-\(P\) matrix with \(M_{L,L'}=1\) when the two isotropic lines are perpendicular, **including the diagonal**. On the subspace whose ray constants sum to zero, the origin decouples and the eigenvalues of \(G\) are
\[
q^{2m-1}+\varepsilon q^m(q-1)\lambda,
\tag{3}
\]
where \(\lambda\) runs through the nonconstant eigenvalues of \(M\).

For completeness, those eigenvalues can be obtained by elementary orthogonal-complement counting. Let \(S_j=q^{2j-1}+\varepsilon(q-1)q^{j-1}\) count isotropic vectors in a nondegenerate \(2j\)-space of type \(\varepsilon\). When \(m\ge3\), the number of projective points perpendicular to a fixed isotropic point is \(H=(qS_{m-1}-1)/(q-1)\); two distinct perpendicular isotropic points have \((q^2S_{m-2}-1)/(q-1)\) common perpendicular isotropic points; two nonperpendicular points have \((S_{m-1}-1)/(q-1)\). Subtracting the constant part of the resulting identity for \(M^2\) yields
\[
\lambda^2-\varepsilon(q-1)q^{m-2}\lambda-q^{2m-3}=0.
\tag{4}
\]
For split type the roots are \(q^{m-1}\) and \(-q^{m-2}\); for nonsplit type they are \(q^{m-2}\) and \(-q^{m-1}\). Substituting either pair into (3) gives precisely \(q^{2m}\) and \(q^{2m-2}\). When \(m=2\), the split quadric is the projective grid and gives the same two eigenvalues directly. The nonsplit quadric is an ovoid with no perpendicular distinct isotropic points, so \(M=I\), yielding only \(q^{2m-2}\) on the ray-sum-zero subspace. Thus all cases are covered, including characteristic two.

**Step 3: origin and the uniform ray mode.** In the orthonormal basis consisting of the origin indicator and the normalized indicator of \(C\setminus\{0\}\), the remaining two-by-two block of \(G\) is
\[
\begin{pmatrix}
N & \varepsilon(q-1)q^{m-1}\sqrt{N-1}\\
\varepsilon(q-1)q^{m-1}\sqrt{N-1}&
q^{2m-1}+\varepsilon q^{m-1}\bigl(q(q-1)H-(N-1)\bigr)
\end{pmatrix},
\]
where \(H=(qS_{m-1}-1)/(q-1)\) also applies to \(m=2\). Substitution of \(N\) and \(H\) shows its trace is \(q^{2m-2}(1+q^2)\) and determinant is \(q^{4m-2}\). Hence its eigenvalues are exactly \(q^{2m-2}\) and \(q^{2m}\).

**Step 4: multiplicities and stability.** The eigenvalues of \(G\) have now been shown to lie in \(\{q^{2m-2},q^{2m-1},q^{2m}\}\), with middle multiplicity \(b=P(q-2)\). The remaining multiplicities \(c,a\) satisfy \(a+c=P+1\). Because all entries of \(q^mT\) have absolute value one, \(\operatorname{tr}G=N^2\), hence
\[
a q^{2m}+bq^{2m-1}+cq^{2m-2}=N^2.
\]
Solving yields \(c=(q^{2m}-1)/(q^2-1)\) and \(a=P+1-c\). Both extreme levels occur because the two-by-two block contains each once. Division by \(q^{2m}\) gives the squared singular values \(1,1/q,1/q^2\), and hence \(\kappa_2(T)=q\). Finally, \(T\) is the compression of a unitary ambient Fourier transform to the cone. A singular value one is equivalent to a supported input having all its Fourier output again supported on the cone; its multiplicity is \(a\), as claimed. \(\square\)

## Verification
The accompanying standalone script `verify.py` builds the Fourier sampling matrices directly, without using the projective-graph eigenvalue formulas, and compares their numerical Gram eigenvalues with all asserted multiplicities. It checks both quadratic types over \(\mathbb F_2\) in dimensions four and six, over \(\mathbb F_3\) and \(\mathbb F_5\) in dimension four, and over the nonprime field \(\mathbb F_4\) in dimension four: ten field-form configurations. Run `python verify.py` with NumPy installed. These are finite corroborations; the argument above provides the proof for all prime powers and all \(m\ge2\).

## Relationship to prior work
The finite-field quadratic-surface restriction framework and standard Gauss sum identities are classical, notably the 2008 preprint of Iosevich and Koh. Koh and Yeom's 2016 study of averaging operators restricted to algebraic varieties explicitly computes the Fourier transform of an even-dimensional cone (Lemma 4.1) and studies its mapping properties. Likewise, spectra of projective orthogonal polar collinearity graphs are established geometric-combinatorial information. **No novelty is asserted for these inputs.** The asserted distinction is their combination into the *complete principal self-Fourier singular multiset* for both quadratic types and all field characteristics, including its uniform sharp reconstruction condition number and exact perfect-concentration multiplicity. The inspected primary statements concern Fourier decay, extension bounds, or restricted averaging rather than this finite square self-sampling operator. A more general published theory of quadratic-form association schemes could implicitly contain the spectral corollary; historical priority is not conclusively established.

## Limitations
The origin must be included in the cone; excluding it produces a different matrix. The polar pairing must be the one associated with \(Q\), not an unrelated fixed dot product unless it has first been transported by a linear isomorphism. No statement is made for odd-dimensional forms, singular quadratic forms, nonzero quadratic level sets, weighted cones, or exact arithmetic Smith invariants. The checker is a finite numerical verification and not an independent proof of the infinite family. Independent mathematical auditing and priority certification have not been performed.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first publicly posted 2008-04-28, https://arxiv.org/abs/0804.4505.
2. D. Koh and S. Yeom, *Restriction of averaging operators to algebraic varieties over finite fields*, arXiv:1601.07677, first publicly posted 2016-01-28, https://arxiv.org/abs/1601.07677, particularly Lemma 4.1.
3. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first publicly posted 2002-04-18, https://arxiv.org/abs/math/0204234 (general finite-field restriction context).
