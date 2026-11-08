# Isospectral translation-erasure masks for one-defect subgroup Gabor frames

## Finding
Let integers \(m,q\ge2\) and \(N=mq\) be fixed. In \(\mathbb C^{\mathbb Z_N}\), take the window \(g_z(j)=1+z\mathbf1_{\{0\}}(j)\) with any \(z\in\mathbb C\setminus\{0\}\), the modulation subgroup \(L=\{0,q,2q,\ldots,(m-1)q\}\), and a translation set \(K\subseteq\mathbb Z_N\). Write \(E=\mathbb Z_N\setminus K\), \(e=|E|\), and \(k=N-e\). The Gabor family \(\{M_\ell T_tg_z:\ell\in L,\ t\in K\}\) is a frame if and only if **at most one** translation is erased from each congruence class modulo \(m\).

When this condition holds, the entire frame-operator spectrum depends only on \(e\), not on which eligible translations were erased. Set \(u=|z|^2\), \(v=\operatorname{Re}z\), and
\[
T=qk+2(q-1)v+u,\qquad D=u(k-q+1),\qquad
\lambda_\pm=\frac{T\pm\sqrt{T^2-4D}}2,\qquad \rho=u+q(k+2v).
\]
For \(0\le e\le m\) the eigenvalues of the **unnormalized** Gabor frame operator, including multiplicity, are
\[
\underbrace{m\lambda_+,\ m\lambda_-}_{\text{once each per erased class}},\quad
\underbrace{mu}_{q-2\text{ copies per erased class}},\quad
\underbrace{m\rho}_{\text{once per unerased class}},\quad
\underbrace{mu}_{q-1\text{ copies per unerased class}}.
\]
Here there are exactly \(e\) erased classes and \(m-e\) unerased classes; an empty multiplicity group is omitted. Thus the optimal frame bounds are the smallest and largest numbers in the displayed multiset. For every \(e\le m\) there are exactly \(\binom me q^e\) admissible erasure sets of size \(e\); no erasure set of size \(e>m\) preserves a frame.

The family is tight precisely in the following cases: (i) \(e=0\) and \(\operatorname{Re}z=-N/2\); or (ii) \(e=m\), \(m=q=2\), and \(z=-2\). In particular every nonempty proper admissible erasure, except the four-dimensional endpoint, destroys tightness for every nonzero complex impulse.

## Assumptions and scope
The Hilbert-space norm is \(\|f\|_2^2=\sum_{j\in\mathbb Z_N}|f(j)|^2\). Translations and modulations are \((T_tg)(j)=g(j-t)\) and \((M_\ell g)(j)=e^{2\pi i\ell j/N}g(j)\), with all indices modulo \(N\). The window is **not normalized**; normalizing it multiplies all frame eigenvalues by \((N+2v+u)^{-1}\), leaving the frame criterion and tightness conditions unchanged. The number \(e\) counts erased **translation fibers**: deleting \(t\) removes all \(m\) atoms \(\{M_\ell T_tg_z:\ell\in L\}\). The theorem makes no claim about arbitrary individual time-frequency atom erasures or about nonlinear intensity recovery.

## Proof
Let \(S\) be the frame operator. Directly summing its rank-one outer products over modulations, the roots-of-unity identity gives
\[
S_{ij}=m\,\mathbf1_{\{i\equiv j\ (\mathrm{mod}\ m)\}}
\sum_{t\in K}g_z(i-t)\overline{g_z(j-t)}.
\]
Put \(a_i=\mathbf1_K(i)\). For \(i\equiv j\pmod m\), expansion of the last sum is
\[
S_{ij}/m=k+za_i+\overline z a_j+u a_i\mathbf1_{\{i=j\}}.
\]
Consequently \(S/m\) is an orthogonal direct sum of \(m\) Hermitian blocks, one for each residue class modulo \(m\), each of size \(q\). In a class with \(s\) retained translations, the block equals
\[
B=(k\mathbf1\mathbf1^*+z a\mathbf1^*+\overline z\mathbf1 a^*+u\operatorname{diag}(a)),
\]
where \(a\) is a zero-one vector with exactly \(s\) ones. If \(s\le q-2\), a nonzero vector supported on the at least two missing positions and summing to zero lies in the kernel. Thus a frame requires \(s\ge q-1\) in each class.

If \(s=q\), then \(B=(k+2v)\mathbf1\mathbf1^*+uI_q\). Its eigenvalues are \(u\) with multiplicity \(q-1\) and \(\rho=u+q(k+2v)\) once. For any admissible erasure pattern containing such a class, \(k\ge N-(m-1)=m(q-1)+1>q\); hence
\[\rho=|z+q|^2+q(k-q)>0.\]
If \(s=q-1\), the subspace of vectors supported on the \(q-1\) retained positions and summing to zero has eigenvalue \(u\) with multiplicity \(q-2\). On the orthogonal span of the normalized retained-sites indicator and the missing-site basis vector, the block has matrix
\[
\begin{pmatrix}
(q-1)(k+2v)+u&\sqrt{q-1}(k+z)\\
\sqrt{q-1}(k+\overline z)&k
\end{pmatrix}.
\]
Its trace is \(T\), and cancellation yields determinant
\[
 k\big((q-1)(k+2v)+u\big)-(q-1)|k+z|^2=u(k-q+1)=D.
\]
Because admissibility forces \(k\ge m(q-1)>q-1\), and \(z\ne0\), this Hermitian matrix is positive definite: it is a principal restriction of the positive-semidefinite frame operator and has strictly positive determinant. Its eigenvalues are precisely \(\lambda_\pm>0\). This proves both necessity and sufficiency of the erasure criterion and the spectrum. Exactly \(e\) of the \(m\) classes contain one erased translation. Choosing those classes and one of their \(q\) positions gives \(\binom me q^e\) masks, and pigeonhole excludes \(e>m\).

A Hermitian matrix is scalar exactly when all its off-diagonal entries vanish and all diagonals agree. For \(e=0\) every block is full, giving tightness exactly when \(k+2v=N+2v=0\). For \(0<e<m\), a full block requires \(k+2v=0\), while a one-missing block has a selected-to-missing entry \(k+z\) and requires \(z=-k\); these conditions are incompatible. For \(e=m\) all blocks have one missing entry. If \(q\ge3\), vanishing of the selected-to-missing and selected-to-selected off-diagonals again demands the incompatible equations \(z=-k\) and \(k+2v=0\). If \(q=2\), the only off-diagonal equation gives \(z=-k\); the two diagonal entries then agree exactly when \(k(k-1)=k\), so \(k=2\). As \(k=m\) here, this is exactly \(m=q=2\), \(z=-2\). All listed cases indeed give positive scalar operators, completing the tightness classification.

## Verification
The accompanying `CHECK.py` independently constructs every Gabor atom and its dense frame operator, diagonalizes it numerically, and compares its eigenvalues against the formula. It also exhausts all erasure masks in several small dimensions, checks exact mask counts, tests complex perturbations, and probes the tightness endpoints. These finite tests corroborate but do not replace the proof for every \(m,q\ge2\) and all nonzero \(z\).

## Relationship to prior work
Asipchuk, De Carli, and Rodriguez (2026) show general block equivalence for finite Gabor frames with a subgroup in either coordinate and provide a block-entry formula; the result here solves the entire spectrum, rank threshold, erasure-mask enumeration, and tightness boundary for a specified natural one-defect window. Salanevich and Strachan (2025) study robustness and frame bounds under finite Gabor erasures, including random and mutually unbiased constructions, but do not give this deterministic, mask-isospectral classification. The proof uses the same underlying root-of-unity block structure as the former; its novel asserted content is the simultaneous explicit erasure and spectral classification, not the general block-diagonalization principle.

## Limitations
Only entire translation fibers are erased, not arbitrary individual Gabor atoms. The window has exactly one additive defect against a flat background, and the modulation set is a subgroup. The theorem is not a frame-set classification for arbitrary windows; the exact spectrum uses the special rank-one-plus-diagonal block structure. In the present setting, erasure-mask spectra are identical for masks of the same admissible cardinality, but this should not be generalized to arbitrary windows. Older specialized calculations or easy consequences of general block formulas remain a publication-priority risk.

## References
1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (first submitted 2026-05-15), with v2 dated 2026-10-24. https://arxiv.org/html/2605.16139v2 .
2. P. Salanevich, N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325v1 (2025-09-01). https://arxiv.org/abs/2509.01325 .
