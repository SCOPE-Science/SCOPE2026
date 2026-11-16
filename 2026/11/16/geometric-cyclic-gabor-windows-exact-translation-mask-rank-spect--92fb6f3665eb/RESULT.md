# Geometric cyclic Gabor windows: exact translation-mask rank, spectral rigidity, and optimal taper

## Finding
For integers \(q,m\ge2\), let \(N=qm\) and choose any \(q\)-element subset \(K\subset\mathbb Z_N\). Fix \(0<\rho<1\) and the finite, cyclically translated geometric window \(g_\rho(j)=\rho^j\) for \(0\le j<N\). Use the modulation subgroup \(L=\{0,q,2q,\ldots,(m-1)q\}\), with unnormalized atoms \(M_\ell T_tg_\rho\) for \(\ell\in L\), \(t\in K\). These \(N\) atoms form a basis of \(\mathbb C^N\) **if and only if**
\[
K=r+m\mathbb Z_N=\{r,r+m,\ldots,r+(q-1)m\}\quad\text{for one }0\le r<m.
\]
Thus exactly \(m\) of the \(\binom{qm}{q}\) translation masks give a basis; every other mask loses rank despite the window being nonzero at all \(N\) coordinates.

More generally, write every \(t\in\{0,\ldots,N-1\}\) uniquely as \(t=ma(t)+b(t)\), with \(0\le a(t)<q\) and \(0\le b(t)<m\). The exact synthesis rank, valid also for singular masks, is
\[
\operatorname{rank}\mathcal G_K=\sum_{j=0}^{m-1}\left|\left\{a(t)+\mathbf1_{\{b(t)>j\}}\pmod q:t\in K\right\}\right|.
\]
Here the cardinality counts distinct residues; no numerical tolerance or genericity assumption is involved.

For every admissible coset, the **full frame-operator spectrum**, with all \(N\) eigenvalues counted by \((s,k)\), is
\[
\boxed{\displaystyle
\lambda_{s,k}=m\rho^{2s}\,
\frac{(1-\rho^N)^2}{1+\rho^{2m}-2\rho^m\cos(2\pi k/q)},
\quad0\le s<m,\quad0\le k<q.}
\]
It is independent of the coset representative. Put \(R=\rho^m\), and \(c_q=1\) for even \(q\), while \(c_q=\cos(\pi/q)\) for odd \(q\). The exact squared synthesis/frame bounds are
\[
\boxed{\displaystyle A=m\rho^{2(m-1)}\frac{(1-\rho^N)^2}{1+R^2+2c_qR},\qquad
B=m\frac{(1-\rho^N)^2}{(1-R)^2}.}
\]
The squared frame condition number is \(\kappa^2=B/A=R^{-2(m-1)/m}(1+R^2+2c_qR)/(1-R)^2\). It has exactly one minimizing taper \(\rho_*=R_*^{1/m}\in(0,1)\), where \(R_*\) is the unique solution in \((0,1)\) to
\[
\boxed{\displaystyle
\frac{m-1}{m}=\frac{(1+c_q)R_*(1+R_*)}{(1-R_*)(1+R_*^2+2c_qR_*)}.}
\]
For even \(q\), writing \(\alpha=(m-1)/m\), the root is explicitly \(R_*=(\sqrt{1+\alpha^2}-1)/\alpha\). The squared volume of a basis is
\[
\boxed{\det S=m^N\rho^{qm(m-1)}(1-\rho^N)^{2m(q-1)}.}
\]
These identities combine a complete mask-rank classification with exact spectral and optimal-conditioning design.

## Assumptions and scope
The group is \(\mathbb Z_N\) with counting-measure inner product \(\langle u,v\rangle=\sum_{j=0}^{N-1}u(j)\overline{v(j)}\). The operators are \((T_tf)(j)=f(j-t\bmod N)\) and \((M_\ell f)(j)=e^{2\pi i\ell j/N}f(j)\). The ordered exponent \(j\in\{0,\ldots,N-1\}\) defines a finite window; it is **not** the function \(\rho^{j\bmod N}\) interpreted as a periodic infinite exponential. No unit-norm rescaling of the window is applied. Multiplying all atoms by one common constant multiplies \(A,B\) and all eigenvalues by its squared modulus but leaves rank and \(B/A\) unchanged. The exact rank expression covers arbitrary distinct \(q\)-translation masks; the spectral expression, determinant and optimal taper concern the masks that form bases. For the strict design theorem both \(m\) and \(q\) are at least two.

## Proof
**1. Fourier-fiber reduction.** For a fixed translation \(t\), the \(m\) modulation columns have restrictions to coordinates \(j+hm\) (\(0\le j<m\), \(0\le h<q\)) given by \(e^{2\pi i\ell j/N}g_\rho(j+hm-t\bmod N)\), since \(e^{2\pi i\ell h m/N}=1\) for \(\ell\in L\). Apply the unitary \(m\)-point Fourier transform to those \(m\) columns and permute rows by residue modulo \(m\). The synthesis matrix becomes an orthogonal sum, over \(j=0,\ldots,m-1\), of matrices \(\sqrt m\,M_j\) of size \(q\times q\), with
\[
(M_j)_{h,t}=\rho^{(j+hm-t)\bmod N}.
\]
The unitary column transform preserves every singular value and the rank.

**2. An invertible cyclic-geometric factor.** Write \(t=ma+b\) with \(0\le a<q\), \(0\le b<m\). Put \(s_j(t)=(j-b)\bmod m\) (the least nonnegative residue), and \(c_j(t)=a+\mathbf1_{\{b>j\}}\bmod q\). Directly reducing the exponent modulo \(N\) gives
\[
(M_j)_{h,t}=\rho^{s_j(t)}R^{(h-c_j(t))\bmod q},\qquad R=\rho^m.
\]
Let \(C_R\) be the \(q\)-circulant whose column at index \(c\) is \((R^{(h-c)\bmod q})_{h=0}^{q-1}\). Its Fourier eigenvalues are \((1-R^q)/(1-R e^{-2\pi ik/q})\), \(0\le k<q\). Every one is nonzero for \(0<R<1\); indeed \(\det C_R=(1-R^q)^{q-1}>0\). Thus each \(M_j\) has exactly the rank of its distinct selected column indices \(c_j(t)\), proving the rank formula in the finding.

**3. Necessity and sufficiency of translation cosets.** If every fiber is invertible, the fiber \(j=m-1\) forces the quotients \(a(t)=\lfloor t/m\rfloor\) to run through the complete set \(0,1,\ldots,q-1\). Write the unique selected translation with quotient \(a\) as \(ma+b_a\). At fiber \(j\), its column index is \(a+\mathbf1_{\{b_a>j\}}\bmod q\). If these binary indicators are not all equal, their circular binary sequence has an adjacent \(1\)-to-\(0\) transition, say at \(a\) and \(a+1\): then both chosen columns have index \(a+1\), a contradiction. Hence all indicators are identical for each \(j\). If any two remainders \(b_a\) differ, choosing \(j\) between their minimum and maximum makes the indicator sequence nonconstant. It follows that all \(b_a=r\), i.e., \(K=r+m\mathbb Z_N\). Conversely, for such a coset every \(M_j\) is \(\rho^{s_j}C_R\) times a column permutation, with \(s_j=(j-r)\bmod m\); it is invertible. This also proves exactly \(m\) masks are feasible.

**4. Entire spectrum, endpoints and volume.** For a feasible coset, \(M_jM_j^*=\rho^{2s_j}C_RC_R^*\); the \(s_j\)'s permute \(\{0,\ldots,m-1\}\). Fourier diagonalization of \(C_R\) gives the claimed \(\lambda_{s,k}\) exactly. The denominator is smallest for \(k=0\) and largest for the frequency nearest \(\pi\), i.e. \(\cos(2\pi k/q)=-c_q\). Independently, the smallest geometric factor is \(\rho^{2(m-1)}\). These are attained fiber eigenvalues, establishing *sharp*, not merely sufficient, bounds. Multiplying the \(N\) eigenvalues and using \(\prod_k|\lambda_k(C_R)|^2=(1-R^q)^{2(q-1)}\) gives \(\det S=m^N\rho^{qm(m-1)}(1-\rho^N)^{2m(q-1)}\).

**5. Existence and uniqueness of the optimal taper.** Set \(\alpha=(m-1)/m>0\) and \(c=c_q\ge0\). Writing \(J(R)=(1+R^2+2cR)/(1-R)^2=1+2(1+c)R/(1-R)^2\), the condition number is \(\kappa^2=R^{-2\alpha}J(R)\). Its logarithmic derivative with respect to \(\log R\) vanishes precisely when
\[
\alpha=\frac{R}{2}\frac{J'(R)}{J(R)}=\frac{(1+c)R(1+R)}{(1-R)(1+R^2+2cR)}.
\]
The right-hand side is strictly increasing from zero to infinity: write \(w=R/(1-R)^2\), so twice that side is the product of \(2(1+c)w/[1+2(1+c)w]\) and \((1+R)/(1-R)\), both strictly increasing positive functions. Therefore a unique root exists. Since \(\kappa^2\to\infty\) as \(R\downarrow0\) or \(R\uparrow1\), it is the unique global minimum. When \(q\) is even, \(c=1\), and the root equation reduces to \(\alpha=2R/(1-R^2)\), yielding the stated quadratic radical. This completes the theorem.

## Verification
Run `python check_geometric_masks.py` with Python 3 and NumPy. The checker constructs the original \(N\times N\) complex synthesis matrix independently from cyclic translations and modulations, compares its numerical rank with the exact index-count formula for 506 masks, and compares the entire spectrum, both sharp endpoints and the determinant for 36 admissible instances. It also checks 42 unique-root designs and the even-\(q\) radical formula. Observed output: `CHECK_OK masks=506 full_spectra=36 optimizer_pairs=42`. These finite numerical tests do not imply the all-dimensional theorem; Steps 1–5 are exact proofs.

## Relationship to prior work
Asipchuk, De Carli and Rodriguez, *Block-equivalent finite Gabor frames* (first public May 15, 2026; arXiv:2605.16139, Theorem 1.1 and Sections 3–5), establish a general subgroup block decomposition for arbitrary windows and translation sets. That result supplies the natural Fourier-fiber reduction but does **not itself state** this exponential-window arbitrary-mask rank formula, its rigid coset-only basis criterion, the explicit full spectrum and determinant, or the unique optimally conditioned taper. The distinction is not the mere presence of a block decomposition, which is credited here, but the classification of every mask and exact evaluation of its geometric fibers.

The published result *Dimension-free linear rigidity of nonnegative critically sampled cyclic Gabor windows* concerns an inverse near-Parseval estimate for fixed subgroup translations and nonnegative windows; its exact scalar Fourier spectra are on a different fixed lattice. The published result *Rank strata and sharp phase-resonance instability for complex-geometric cyclic Gabor measurements* analyzes the full \(N^2\)-entry matrix-intensity lifting map of a geometric window, not whether a selected \(N\)-atom synthesis matrix is a basis. Dongwei Li's *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (first public September 9, 2026; arXiv:2609.09614) studies perturbed full-spark constructions and ambiguity margins. Its accessible abstract was inspected, not claimed as a full-text exclusion. No inspected statement provides the joint mask-rigidity and optimal-taper result here.

## Limitations
This is a finite cyclic, positive real geometric-window theorem, not a classification for arbitrary windows, general modulation masks, or continuous-line Gabor systems. The exact condition-number optimum is within this one-parameter taper family, not globally over all windows. Normalized-window frame bounds require scaling by the window norm. Existing broad Fourier-fiber and circulant techniques are essential ingredients; originality relative to older specialized finite-Gabor or displacement-structured-matrix literature remains provisional, and the Li paper's full text was inaccessible. No independent mathematical audit has been performed.

## References
1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (first posted 2026-05-15), https://arxiv.org/abs/2605.16139; full text inspected at https://arxiv.org/html/2605.16139v2.
2. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1 (first posted 2026-09-09), https://arxiv.org/abs/2609.09614 (abstract inspected).
3. *Dimension-free linear rigidity of nonnegative critically sampled cyclic Gabor windows*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-dimension-free-linear-rigidity-of-nonnegative-critically-sampled--83baf3ba44b5 (full RESULT.md inspected).
4. *Rank strata and sharp phase-resonance instability for complex-geometric cyclic Gabor measurements*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-strata-and-sharp-phase-resonance-instability-for-complex-ge--51cfce1c5210 (full RESULT.md inspected).
