# Sharp sparse Gabor tomography at Singer projective-plane lengths

## Finding

Let \(q\ge2\) be any prime power, \(N=q^2+q+1\), and \(r=q+1\). Among all unit vectors \(g\in\mathbb C^{\mathbb Z_N}\) supported on at most \(r\) sites, the **largest possible least singular value** of the full cyclic Gabor intensity lifting is exactly
\[
\boxed{\sup_{\|g\|_2=1,\ |\operatorname{supp}g|\le r}\sigma_{\min}(\mathcal L_g)=\frac{\sqrt N}{r}.}
\]
Equality occurs **exactly** when the support is a cyclic \((N,r,1)\) difference set and all nonzero entries have modulus \(1/\sqrt r\); their phases are arbitrary. Such optimizers exist for every prime power \(q\) by the classical Singer construction. In particular, the minimum support of an informationally complete **Gabor projector lifting** at these dimensions is \(r\), and its optimal spectral condition number within this sparsest class is exactly \(r\).

Every optimizer has the *entire* singular-value multiset
\[
\boxed{\sqrt N\ (1),\qquad\frac{\sqrt{Nq}}{r}\ (N-1),\qquad\frac{\sqrt N}{r}\ (N(N-1)).}
\]
Parenthesized integers denote multiplicities. The inverse problem is complete on the complex matrix space (not merely pure states); hence all underlying complex signals are phase retrievable up to global phase.

There is also a sharp **one-site deletion rank law**. Among every unit vector supported on at most \(q\) sites, the maximal complex rank of its full Gabor lifting is
\[
\boxed{\max\operatorname{rank}\mathcal L_h=N(q^2-q+1),\qquad\min\dim\ker\mathcal L_h=2qN.}
\]
Both extrema are attained by deleting any one site of a Singer set and assigning equal nonzero magnitudes and arbitrary phases to the surviving \(q\) sites. Thus removing a single site from a sparsest informationally complete design creates exactly \(2qN\) invisible matrix directions, and this is the smallest achievable nullity at that support budget.

## Assumptions and scope

Use the finite cyclic group \(G=\mathbb Z_N\), \(\omega=e^{2\pi i/N}\), the shifts \((T_a g)(x)=g(x-a)\), and modulations \((M_b g)(x)=\omega^{bx}g(x)\). For a unit vector \(g\), write \(v_{a,b}=M_bT_ag\). The *linear* full Gabor intensity lifting is
\[
\mathcal L_g:\mathbb C^{N\times N}\longrightarrow\mathbb C^{N^2},\qquad
\mathcal L_g(H)_{a,b}=\operatorname{tr}(H v_{a,b}v_{a,b}^{*}),\quad (a,b)\in G^2.
\]
The domain has the Hilbert–Schmidt norm, the target the counting-measure Euclidean norm, and no further measurement normalization is imposed. Define \(\kappa(\mathcal L_g)=+\infty\) for a singular map and otherwise the largest singular value divided by the smallest. An \((N,r,1)\) difference set is a subset \(D\subset G\) of \(r\) points in which every nonzero cyclic residue occurs *exactly once* among the ordered differences \(x-y\) with \(x\ne y\) in \(D\).

No result is claimed here about the minimum support for the **weaker** problem of phase retrieval on pure states without injectivity of the lifted map. The optimization of \(\sigma_{\min}\) and of the operator condition number is over all complex window coefficients, not only real or positive coefficients.

## Proof

**1. Weyl diagonalization and its normalization.** Define the ambiguity array
\[
A_g(u,v)=\sum_{x\in G}g(x)\overline{g(x-u)}\omega^{-vx}.
\]
The normalized Weyl operators \(N^{-1/2}M_vT_u\), indexed by \((u,v)\in G^2\), form an orthonormal Hilbert–Schmidt basis. Commuting them past the time-frequency shifts shows that their images under \(\mathcal L_g\) are distinct Fourier characters on \(G^2\), multiplied by \(A_g(u,v)/\sqrt N\) up to a unit phase. Each character has Euclidean norm \(N\), and distinct characters are orthogonal. Thus, with multiplicities,
\[
\operatorname{SingVal}(\mathcal L_g)
=\{\sqrt N\,|A_g(u,v)|:(u,v)\in G^2\},
\quad\operatorname{rank}\mathcal L_g=\#\{(u,v):A_g(u,v)\ne0\}.
\]
This standard Weyl-diagonalization identity is a previously known input, not the claimed new result. The coefficient \(A_g(0,0)=1\), and Cauchy–Schwarz gives \(|A_g(u,v)|\le1\), so the top singular value is always \(\sqrt N\).

**2. The sharp sparse support obstruction.** Put \(S=\operatorname{supp}g\), \(s=|S|\). If \(u\notin S-S\), then \(g(x)\overline{g(x-u)}=0\) for every \(x\), hence all \(N\) values \(A_g(u,v)\) vanish. Consequently
\[
\operatorname{rank}\mathcal L_g\le N|S-S|
\le N\min\{N,1+s(s-1)\}.
\]
Since \(N=1+r(r-1)\), every \(s<r\) forces a singular lifting. If \(s=r\) and the lifting is injective, then \(S-S=G\), and the \(r(r-1)=N-1\) ordered nonzero differences must each appear once. Therefore \(S\) is necessarily an \((N,r,1)\) difference set.

**3. Singer designs exist at every prime-power parameter.** Let \(E=\mathbb F_{q^3}\). The quotient \(E^*/\mathbb F_q^*\) is cyclic of order \(N\). Identify it with \(G\), and let \(D\) consist of the one-dimensional \(\mathbb F_q\)-subspaces \([x]\) satisfying \(\operatorname{Tr}_{E/\mathbb F_q}(x)=0\). The trace-zero subspace has dimension two and therefore contains \(r=q+1\) projective points. For any nonidentity quotient element \([z]\), the two independent linear forms \(\operatorname{Tr}(x)\) and \(\operatorname{Tr}(z^{-1}x)\) each vanish on a hyperplane, whose intersection is a one-dimensional \(\mathbb F_q\)-subspace. Their independence follows from nondegeneracy of the finite-field trace pairing and \(z\notin\mathbb F_q\). Thus \(|D\cap zD|=1\) for every nonidentity \([z]\): the unique-difference property.

**4. Exact spectrum for flat Singer windows.** Let \(S=D\) and \(g(x)=e^{i\theta_x}/\sqrt r\) for \(x\in D\), zero otherwise; the phases \(\theta_x\) are unrestricted. For every nonzero \(u\), exactly one summand in \(A_g(u,v)\) survives, whence \(|A_g(u,v)|=1/r\) for every \(v\). At \(u=0\), one has \(A_g(0,0)=1\), and for every \(v\ne0\),
\[
\begin{aligned}
|A_g(0,v)|^2&=\frac1{r^2}\left|\sum_{x\in D}\omega^{-vx}\right|^2\\
&=\frac1{r^2}\left(r+\sum_{\substack{x,y\in D\\x\ne y}}\omega^{-v(x-y)}\right)
=\frac{r-1}{r^2}=\frac q{r^2},
\end{aligned}
\]
because the nonzero differences exhaust \(G\setminus\{0\}\) exactly once. These are the three singular levels and the stated multiplicities. In particular all are strictly positive for every \(q\), including when \(N\) is composite.

**5. Maximin optimality and complete optimizer classification.** For any unit \(g\) supported on at most \(r\) sites, a singular lifting has least singular value zero. Otherwise Step 2 forces \(S\) to be a perfect difference set of size \(r\). Write \(a_x=|g(x)|>0\) for \(x\in S\). Each nonzero difference \(u\) is represented by a unique ordered pair \((x,y)\), so for all modulations \(v\), \(|A_g(u,v)|=a_xa_y\). Hence
\[
\min_{u,v}|A_g(u,v)|\le\min_{x\ne y}a_xa_y
\le\left(\prod_{x\in S}a_x\right)^{2/r}
\le\frac1r,
\]
where the last inequality is arithmetic–geometric mean applied to \(\sum_{x\in S}a_x^2=1\). Equality requires every \(a_x^2=1/r\); Steps 3–4 show that all such vectors do attain it. Since the largest singular value is always \(\sqrt N\), the optimal condition number equals \(r\) and has the same complete equality characterization.

**6. Sharp rank immediately below the support threshold.** If \(s\le q\), Step 2 gives \(\operatorname{rank}\mathcal L_g\le N(1+q(q-1))\). To attain this, delete any point \(d\) from a Singer set \(D\), let \(S=D\setminus\{d\}\), and choose arbitrary phases with \(|h(x)|=q^{-1/2}\) on \(S\). Its \(q(q-1)\) nonzero ordered differences remain distinct. At each of the corresponding nonzero shifts \(u\), there is a unique summand and therefore \(A_h(u,v)\ne0\) for every \(v\). At the zero shift and every \(v\ne0\),
\[
q A_h(0,v)=\sum_{x\in D}\omega^{-vx}-\omega^{-vd}.
\]
The first term has modulus \(\sqrt q>1\), while the second has modulus one, so the sum is nonzero. Also \(A_h(0,0)=1\). At every remaining shift all coefficients vanish. Thus the rank is exactly \(N(1+q(q-1))=N(q^2-q+1)\), and the nullity is \(N^2-N(q^2-q+1)=2qN\), attaining the universal support-\(q\) bound.

## Verification

Run `python CHECK.py` with Python 3 and NumPy. The checker verifies four explicit perfect difference sets at orders \(7,13,21,31\), computes all ambiguity magnitudes for nonconstant phase patterns, compares the predicted singular values to directly constructed complex lifted matrices at orders \(7\) and \(13\), checks sharp deletion ranks and predicted zero bands, and verifies that unequal amplitudes lose the maximin equality. Its expected final line is `CHECK_OK singer_designs=4 direct_lifting_orders=7,13`.

These tests are finite consistency checks. The existence proof, upper bound, equality characterization, spectral formula, and sharp rank theorem are the preceding all-prime-power arguments. Computations do not assert that their four explicit sets enumerate all possible Singer designs or all minimizers.

## Relationship to prior work

Bojarovska and Flinth [2, Theorems 2.2–2.3 and Proposition 2.2] previously proved that zero-free Gabor ambiguity yields phase retrieval and full matrix lifting, and explicitly used indicator functions of difference sets as examples. Goldberger, Kang, and Okoudjou [3, Theorem 2] previously identified the full projector Gram spectrum in terms of ambiguity magnitudes. Singer's cyclic projective-plane difference sets are classical [4]. **None of these ingredients, constructions, or general spectral identities is claimed as new.**

The specific contribution here is the all-complex-coefficient **sharp maximin** among *every* window with at most \(q+1\) nonzero entries at Singer lengths, the complete rigidity of all optimizers, the full resulting three-level operator spectrum and optimal stability, and the universally sharp operator-rank cutoff after reducing the support to \(q\) sites. These comparisons are about strength of conclusions, not merely shared terminology. Bartusel [1] motivates renewed interest in what ambiguity zeros permit but does not optimize this sparsest complete-lifting design.

## Limitations

The statement concerns the complete time-frequency orbit and the **linear matrix-lifting** stability under Hilbert–Schmidt and counting-measure norms, not the optimal conditioning of a nonlinear phase-retrieval algorithm, fewer measurements, or erasures of individual time-frequency samples. The support threshold applies to informational completeness of the lifted matrix problem, not to every weaker phase-retrieval design. Singer existence assumes prime-power \(q\), and the sharp rank theorem concerns the specific dimension \(N=q^2+q+1\). Independently unindexed equivalent design-theoretic or Gabor tomography implications remain a priority risk; no independent audit is asserted.

## References

[1] D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first publicly submitted 2026-05-29. https://arxiv.org/abs/2605.31507

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first publicly submitted 2015-03-19. https://arxiv.org/abs/1503.05800

[3] A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509, first publicly submitted 2021-06-02. https://arxiv.org/abs/2106.01509

[4] J. Singer, classical cyclic projective-plane difference-set construction. See the explicit Singer construction and parameters in SageMath's *Difference families* mathematical documentation: https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/designs/difference_family.html
