# Sharp Gumbel widths and exponential support localization for stack-sorting simplices

## Finding

Let \(n\ge3\), let \(\tau_n=(2,3,\ldots,n,1)\), and let \(\Delta_n\subset\mathbb R^n\) be the convex hull of every iterate of the standard deterministic stack-sorting map, including \(\tau_n\) and the sorted permutation. All calculations use the canonical Euclidean metric in \(\mathbb R^n\), restricted to the translation space \(H_n=\{x:\sum_i x_i=0\}\). Its vertices in sorted-to-unsorted order are
\[
v_j=(2,3,\ldots,j+1,1,j+2,\ldots,n),\quad 0\le j\le n-1,
\]
where \(v_0=(1,2,\ldots,n)\). Let \(U_n\) be uniform on the unit sphere in \(H_n\), and define the directional width and exposed indices by
\[
W_n=\max_{0\le j<n}\langle U_n,v_j\rangle-\min_{0\le j<n}\langle U_n,v_j\rangle,\qquad
J_n^\pm=\mathop{\rm arg\,max/min}_{0\le j<n}\langle U_n,v_j\rangle.
\]
The exposed indices are almost surely unique. Write
\[
t_n=\sqrt{2\log n},\qquad c_n=\tfrac32\log(2\log n)+\tfrac12\log(2\pi),\qquad b_n=t_n-c_n/t_n.
\]
As \(n\to\infty\), jointly,
\[
\left(\frac{t_n}{\sqrt n}(W_n-2\sqrt n\,b_n),
\frac{t_n^2(n-J_n^+)}n,\frac{t_n^2(n-J_n^-)}n\right)
\xrightarrow{\rm d}(G_++G_-,E_+,E_-),
\]
where \(G_+,G_-\) are independent standard Gumbels with distribution function \(\exp(-e^{-x})\), and \(E_+,E_-\) are independent \(\operatorname{Exp}(1)\), independent also of both Gumbels. In particular the contact vertices for typical positive and negative directions independently localize within \(n/(2\log n)\) of the most unsorted tip; the width has a precise three-halves logarithmic-logarithmic centering shift.

## Assumptions and scope

The ambient hyperplane has dimension \(n-1\). The metric is the unscaled standard coordinate metric, NOT the lattice-equivalent lecture-hall metric. Gaussian and spherical directions are isotropic in \(H_n\). All limits are as integer \(n\to\infty\); the centering \(b_n\) need not be positive for the smallest admissible dimensions. The theorem includes no claim of independence at finite \(n\).

## Proof

**Step 1: exact orthogonal realization.** The stack-sorting rule takes \(v_j\) to \(v_{j-1}\) for every \(j\ge1\), so these are all the iterates. Setting \(d_j=v_j-v_0\) gives
\[
d_j=\sum_{i=1}^j e_i-j e_{j+1},\qquad
\langle d_j,d_k\rangle=\mathbf1_{\{j=k\}}j(j+1)
\quad(1\le j,k\le n-1).
\]
Indeed if \(j<k\), the first \(j\) coordinates of \(d_k\) cancel its coefficient at \(j+1\) in the scalar product. Hence the normalized vectors \(f_j=d_j/\sqrt{j(j+1)}\) form an orthonormal basis of \(H_n\), and \(\Delta_n\) is congruent, after translation, to the orthogonal simplex \(\operatorname{conv}\{0,\sqrt{j(j+1)}f_j:1\le j<n\}\).

**Step 2: exact Gaussian maxima.** For a standard Gaussian vector \(G_n=\sum_{j=1}^{n-1}Z_jf_j\) in \(H_n\), the coefficients \(Z_j\) are independent standard normals. Put \(\ell_j=\sqrt{j(j+1)}\), and
\[
M_n^+=\max(0,\max_{1\le j<n}\ell_jZ_j),\qquad M_n^-=\max(0,\max_{1\le j<n}-\ell_jZ_j).
\]
The Gaussian directional width equals \(M_n^++M_n^-\). For every \(u,v\ge0\), using \(\overline\Phi(x)=\Pr\{Z>x\}\), the exact finite joint law is
\[
\Pr\{M_n^+\le nu,M_n^-\le nv\}
=\prod_{j=1}^{n-1}\left[1-\overline\Phi\!\left(\frac{nu}{\ell_j}\right)-\overline\Phi\!\left(\frac{nv}{\ell_j}\right)\right].
\]
The expression follows because the two exceedance events at one coordinate are disjoint; independence applies across coordinates, not across signs at fixed dimension.

**Step 3: the sharp boundary-layer tail.** For fixed \(x\in\mathbb R\), set \(u_n(x)=b_n+x/t_n\). We claim
\[
\sum_{j=1}^{n-1}\overline\Phi(nu_n(x)/\ell_j)\longrightarrow e^{-x}.\tag{1}
\]
Write \(k=n-j\), \(a_{n,k}=\ell_{n-k}/n\). Uniformly for \(k\le K n/t_n^2\), for each fixed \(K\),
\[
a_{n,k}=1-\frac{k-1/2}{n}+O\!\left(\frac{k^2+1}{n^2}\right),\qquad
\frac{\overline\Phi(u_n(x)/a_{n,k})}{\overline\Phi(u_n(x))}
=\exp(-t_n^2 k/n)(1+o(1)).\tag{2}
\]
The second equality follows from Mills' normal-tail formula \(\overline\Phi(y)\sim\phi(y)/y\), because \(u_n(x)\sim t_n\) and \(t_n^2 k^2/n^2=O(t_n^{-2})\). After multiplication by \(\overline\Phi(u_n(x))\sim\phi(u_n(x))/u_n(x)\), the sum over the stated window is
\[
\frac{n\phi(u_n(x))}{u_n(x)^3}\,(1-e^{-K})+o(1).
\]
For the omitted range, monotonicity of \(a_{n,k}\), Mills' upper bound, and \(1/a_{n,k}^2-1\ge 2(k-1/2)/n\) imply that the tail after \(K n/t_n^2\) is \(O(e^{-K/2})\,n\phi(u_n(x))/u_n(x)^3\), uniformly for large \(n\); indices with \(k\) proportional to \(n\) contribute still less. Sending \(K\to\infty\) gives
\[
\sum_j\overline\Phi(nu_n(x)/\ell_j)
\sim\frac{n\phi(u_n(x))}{u_n(x)^3}.
\]
Finally \(u_n(x)^2/2=\log n-c_n+x+o(1)\), and \(\exp(c_n)=\sqrt{2\pi}\,t_n^3\), so the last ratio tends to \(e^{-x}\). Also \(\max_j\overline\Phi(nu_n(x)/\ell_j)=O(t_n^2/n)=o(1)\).

**Step 4: joint extreme heights and vertex locations.** Assign to coordinate \(j\) the location mark \(s_{n,j}=t_n^2(n-j)/n\). The same local estimate (2), now restricted to \(s_{n,j}\in[a,b]\subset[0,\infty)\), proves for any fixed \(x\), \(0\le a<b<\infty\),
\[
\sum_{j:s_{n,j}\in[a,b]}\Pr\{t_n(\ell_j Z_j/n-b_n)>x\}
\longrightarrow e^{-x}\int_a^b e^{-s}\,ds.\tag{3}
\]
The corresponding statement holds for \(-Z_j\). Distinct indices are independent; at a fixed index, positive and negative exceedances above the high positive threshold cannot both occur. On finitely many disjoint height/location rectangles, the elementary product expansion \(\log(1-p)=-p+O(p^2)\), with \(\max p=o(1)\), therefore gives **two independent limiting marked Poisson point processes**. Each has intensity \(e^{-x}e^{-s}\,dx\,ds\) on \(\mathbb R\times[0,\infty)\), where \(x\) is the recentered Gaussian height. The tail bound from Step 3 provides tightness at large \(s\), while the continuous height distribution prevents ties. The largest height in each process is standard Gumbel. Since the intensity factorizes and \(\int_0^\infty e^{-s}ds=1\), its location mark is \(\operatorname{Exp}(1)\), independent of its height; the two signs are independent. It follows that
\[
\left(t_n(M_n^+/n-b_n),s_{n,J_n^+},
 t_n(M_n^-/n-b_n),s_{n,J_n^-}\right)
\xrightarrow{\rm d}(G_+,E_+,G_-,E_-)
\]
with the four limits independent. The exceptional event that the exposed index is \(0\) has probability at most \(2^{-(n-1)}\) for each sign, so it does not affect the limits.

**Step 5: spherical directions.** The direction \(U_n=G_n/\|G_n\|\) is Haar-uniform in \(H_n\), independent of \(\|G_n\|\); it has the same exposed indices as \(G_n\). The strong law or chi-square concentration yields \(\|G_n\|/\sqrt n=1+O_{\Pr}(n^{-1/2})\). Since \(M_n^++M_n^-=O_{\Pr}(n\sqrt{\log n})\), the error from replacing \(1/\|G_n\|\) by \(1/\sqrt n\) is \(O_{\Pr}(\sqrt{\log n})\), which, after multiplication by \(t_n/\sqrt n\), tends to zero. Slutsky's theorem completes the joint width-and-location limit.

## Verification

The standalone standard-library script `VERIFY.py` reconstructs the stack-sorting orbit and checks the exact orthogonal Gram identities for every \(3\le n\le25\). It evaluates the exact Gaussian maxima product formula on selected finite inputs and prints illustrative exceedance sums. It uses only exact integer arithmetic for the geometric identities. Finite calculations do not prove either asymptotic statement; those follow from Steps 3–5. Execute with `python VERIFY.py`.

## Relationship to prior work

Lee, Mitchell and Vindas-Meléndez introduced these stack-sorting simplices and proved their Ehrhart/lattice relationships to lecture-hall simplices and cubes [1]. Ake, Lewis, Louie and Vindas-Meléndez subsequently studied general stack-sorting simplex geometry and relative volume [2]. Neither paper gives this canonical-metric random-direction width law or its joint Gaussian extreme/endpoint-localization limit. Standard independent identically distributed Gaussian maxima [3] have a different half-log-log centering coefficient; the present graded norm profile produces three halves through an effective boundary population of order \(n/\log n\). Generic extreme-value results do not in themselves establish the claimed geometric identification and the joint marked limit for this concrete polytope.

## Limitations

The results are asymptotic and require the exact standard-coordinate embedding; an arbitrary lattice equivalence does not preserve width. Convergence is slow because the effective population size changes logarithmically. The point-process argument uses standard normal-tail asymptotics with explicit localization, not a finite enumeration. Historical priority cannot be conclusively certified against unindexed or inaccessible work, and no external independent proof audit is claimed.

## References

[1] E. Lee, C. Mitchell, A. R. Vindas-Meléndez, *Stack-sorting simplices: geometry and lattice-point enumeration*, arXiv:2308.16457, first posted 2023-08-31, https://arxiv.org/abs/2308.16457.

[2] C. Ake, S. F. Lewis, A. Louie, A. R. Vindas-Meléndez, *On the geometry of stack-sorting simplices*, arXiv:2508.00219 (2025), https://arxiv.org/abs/2508.00219. Its published version assigns primary MSC2020 \(52B05\).

[3] A. Gasull, M. Jolis, F. Utzet, *On the norming constants for normal maxima*, arXiv:1308.5541 (2013), https://arxiv.org/abs/1308.5541; background on classical Gaussian maxima, not the graded simplex theorem.
