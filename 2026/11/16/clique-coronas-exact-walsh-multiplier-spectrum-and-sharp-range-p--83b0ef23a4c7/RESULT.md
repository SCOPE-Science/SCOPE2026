# Clique coronas: exact Walsh multiplier spectrum and sharp range-projection norms

## Finding
Let \(h\ge2\), \(b\ge1\), and \(q=2^b\). Form \(G_{h,b}=K_h\circ(bK_1)\): the \(h\) core vertices form a clique, and each core vertex has \(b\) distinct private leaves. Let \(\mathcal I_{h,b}\subseteq\mathbb F_2^{h(b+1)}\) be the independent-set incidence vectors, and let \(C_{h,b}\) be **unnormalized convolution** by \(\mathbf1_{\mathcal I_{h,b}}\). Its Walsh eigenvalues are \(W(\omega)=\sum_{x\in\mathcal I_{h,b}}(-1)^{\langle\omega,x\rangle}\).

Every multiplier is determined by the number \(z\) of leaf-frequency blocks containing at least one nonzero bit and, when \(z=0\), by the number \(j\) of nonzero core-frequency bits:
\[
W(\omega)=\begin{cases}
0,&z\ge2,\\
\pm q^{h-1},&z=1,\\
q^{h-1}(q+h-2j),&z=0.
\end{cases}
\]
For \(z=1\), the sign is the core Walsh sign at the unique nontrivial leaf block. Thus the complete **signed** multiplier distribution is: zero, initially with multiplicity \(2^h(q^h-1-h(q-1))\); each of \(+q^{h-1}\) and \(-q^{h-1}\), with multiplicity \(2^{h-1}h(q-1)\); and \(q^{h-1}(q+h-2j)\), with multiplicity \(\binom hj\), for \(0\le j\le h\), with coincident numerical values aggregated.

Write \(\delta=1\) if \(h\) is even and \(q\le h\), and \(\delta=0\) otherwise; in the first case put \(j_*=(h+q)/2\). The zero set contains an **additional entire core Hamming shell** exactly when \(\delta=1\). Consequently,
\[
\operatorname{rank}C_{h,b}=2^h(1+h(q-1))-\delta\binom h{j_*},
\qquad
\min_{W(\omega)\ne0}|W(\omega)|=q^{h-1}.
\]
Here and below the product \(\delta\binom h{j_*}\) is understood as zero when \(\delta=0\). In particular, \(C_{h,b}\) is singular for every \(h\ge2\), and its Moore--Penrose pseudoinverse has exact \(\ell^2\)-norm \(q^{1-h}\). Its nullity is \((2q)^h-\operatorname{rank}C_{h,b}\).

Let \(\Pi_{h,b}\) be the orthogonal projection onto \(\operatorname{range}C_{h,b}\). It has the smallest \(\ell^1\)- and \(\ell^\infty\)-operator norms among all projections onto that Fourier subspace. These equal a common number \(L_{h,b}\). If \(\delta=0\), then
\[
L_{h,b}=q^{-h}\sum_{z=0}^h\binom hz(q-1)^{h-z}|qz+1-h|.
\]
If \(\delta=1\), define the (unnormalized) binary Krawtchouk value
\[
K_{j_*}(t;h)=\sum_{a=\max(0,j_*+t-h)}^{\min(j_*,t)}(-1)^a\binom ta\binom{h-t}{j_*-a},
\qquad c=2^{-h}\binom h{j_*}.
\]
Then the sharp, **exact** endpoint norm is
\[
L_{h,b}=q^{-h}\sum_{z=0}^h\binom hz(q-1)^{h-z}|qz+1-h-c|
+2^{-h}\sum_{t=1}^h\binom ht|K_{j_*}(t;h)|.
\]
In particular, if \(q>h\), no shell is removed and
\[
L_{h,b}=1+2(h-1)(1-q^{-1})^h.
\]
For each fixed \(h\ge2\), as \(b\to\infty\), the Fourier-rank fraction tends to zero, the smallest positive multiplier increases without bound, yet \(L_{h,b}\to 2h-1\).

## Assumptions and scope
All graphs are finite, simple, and labelled by their core and leaf coordinates. The character pairing is the standard binary dot product, with no Fourier normalization in the definition of \(W\) or of convolution. The inverse Fourier transform of a multiplier on \(\mathbb F_2^n\) uses the factor \(2^{-n}\). All operator norms use counting measure; the equal norm values also hold with uniformly normalized counting measure. The orthogonal range projection is uniquely determined by multiplier \(\mathbf1_{\{W\ne0\}}\). There is no restriction that \(q\) exceed \(h\) except in the simplified last formula.

## Proof
Write \(u_i\in\{-1,1\}\) for the core sign at clique vertex \(i\), and \(t_{i,k}\in\{-1,1\}\) for its private leaf signs. Put \(A_i=\prod_{k=1}^b(1+t_{i,k})\). Each \(A_i\) equals \(0\) or \(q\), and equals \(q\) precisely if the entire leaf-frequency block vanishes. An independent set contains either no clique vertex or exactly one. Summing independently over leaves conditional on the clique choice gives the exact identity
\[
W=\prod_{i=1}^h A_i+\sum_{i=1}^h u_i\prod_{r\ne i}A_r.\tag{1}
\]
If at least two blocks have \(A_i=0\), every term is zero. If just the block \(i\) has \(A_i=0\), only its summand remains and equals \(u_iq^{h-1}\). If all blocks have \(A_i=q\), (1) is \(q^{h-1}(q+\sum_i u_i)=q^{h-1}(q+h-2j)\). Counting the \(q-1\) nonzero assignments in each leaf block and the \(\binom hj\) assignments of \(j\) negative core signs proves the signed distribution. Since \(q\) is even, \(q+h-2j=0\) with \(0\le j\le h\) is possible precisely when \(h\) is even and \(q\le h\). The rank follows. Every eigenvalue is divisible by \(q^{h-1}\), while the \(z=1\) case attains both signs, proving the sharp positive gap and the pseudoinverse norm.

Identify the dual group as the product of core bits \(\omega_c\in\mathbb F_2^h\) and \(h\) leaf blocks \(\omega_i\in\mathbb F_2^b\). Let \(E\) be the frequencies having at most one nonzero leaf block, with core bits arbitrary. Its inverse Fourier kernel at spatial coordinates \((y_c;y_1,\ldots,y_h)\) is
\[
\mathbf1_{\{y_c=0\}}q^{-h}\bigl(1-h+qz(y)\bigr),\qquad
z(y)=|\{i:y_i=0\}|,\tag{2}
\]
because \(\sum_{\omega_i\ne0}(-1)^{\langle\omega_i,y_i\rangle}=q\mathbf1_{\{y_i=0\}}-1\).

When \(\delta=1\), the exact Fourier support is \(E\) minus the frequencies with all leaf blocks zero and core Hamming weight \(j_*\). Fourier inversion subtracts the kernel
\[
(2^hq^h)^{-1}K_{j_*}(|y_c|;h).\tag{3}
\]
Otherwise there is no subtraction. Summing the absolute values of (2)--(3) over the spatial group yields the displayed formulas: for \(y_c=0\), the number of leaf-block arrays with \(z\) zero blocks is \(\binom hz(q-1)^{h-z}\); for \(y_c\ne0\), a fixed core Hamming weight \(t\) contributes \(q^h\binom ht\) arrays. This also proves the formula for \(L_{h,b}\), because the \(\ell^1\)- and \(\ell^\infty\)-norm of a finite-group convolution is the \(\ell^1\)-norm of its kernel.

If \(q>h\), the sole negative kernel values in (2) occur when \(z=0\). Since the kernel sums to one, adding twice the total negative mass \((h-1)(1-q^{-1})^h\) yields the simplified norm. Finally, let \(P\) be any bounded projection onto the same translation-invariant Fourier subspace. Averaging \(T_gPT_g^{-1}\) over translations \(g\) preserves its projection property, target and range action, and does not increase its norm. The averaged operator commutes with translations and is forced to be the unique Fourier multiplier \(\mathbf1_{\{W\ne0\}}\); hence \(\Pi_{h,b}\) minimizes the endpoint norms. The rank-fraction and fixed-\(h\) limits follow from the exact formulas.

## Verification
The accompanying standalone Python script `check_clique_corona.py` performs complete integer Walsh transforms of the graph independent-set indicators, recomputes the signed frequency distributions and exact Fourier-projection norms by a second Walsh transform, and compares all quantities to the formulas using rational arithmetic. It checks twelve pairs \((h,b)\), with \(2\le h\le7\) and \(1\le b\le3\), including resonant and nonresonant cases, through sixteen graph vertices. The verification marker is `CLIQUE_CORONA_EXACT_PASS 12 complete transforms`. Finite tests corroborate the all-parameter proof, not replace it.

## Relationship to prior work
The unsigned corona independence-polynomial framework and the case of a single leaf per core vertex are classical; the 2003 work of Levit--Mandrescu gives the latter transformation. Their 2013 study gives more general corona polynomial transformations and coefficient symmetries, not all binary signed specializations or Fourier-range projection norms. Those transformations support the decomposition leading to (1), but neither source's results imply the resonance shell, signed distribution, sharp positive spectral gap, or exact endpoint projection norms as stated. The Fourier-kernel norm identity and translation averaging are classical; the contribution here is the complete family-specific spectral determination and its arithmetic transition. Equivalence to a prior specialized evaluation of these particular sign sums is a remaining priority risk.

## Limitations
The theorem concerns clique-core coronas with uniform, independent pendant leaves; it does not classify arbitrary base graphs or heterogeneous leaf counts. The resonance norm is given by a finite Krawtchouk sum, not a single elementary expression in every parameter regime. No independent mathematical audit or exhaustive historical-priority certification is claimed.

## References
1. V. E. Levit and E. Mandrescu, *On the Roots of Independence Polynomials of Almost All Very Well-Covered Graphs*, first posted 2003-05-15, arXiv:math/0305227, especially Theorem 2.1. https://arxiv.org/html/math/0305227v1
2. V. E. Levit and E. Mandrescu, *On f-Symmetries of the Independence Polynomial*, first posted 2013-03-11, arXiv:1303.2564, especially Theorem 1.2 and Section 2. https://arxiv.org/html/1303.2564v1
