# Spaceable closed and empty summability-selection spectra via projective tensors

## Finding
For every real \(r>1\), there are a real Banach space \(E_r\) and an infinite-dimensional norm-closed subspace \(W_r\subset\ell_\infty(E_r^*)\) such that every nonzero sequence \(u=(u_n)\in W_r\), after multiplication by the single scalar \(1/\|u_1\|\), is a normalized weakly null \(1\)-symmetric Schauder basic sequence whose **original**, **subsequence**, and **normalized successive-block** density spectra all equal \([r,\infty)\). There also exist a real Banach space \(E_\varnothing\) and a closed infinite-dimensional \(W_\varnothing\subset\ell_\infty(E_\varnothing^*)\) for which these three spectra equal \(\varnothing\) for **every** nonzero sequence. In both cases \(W\) is isometric to a hereditarily \(\ell_1\) Lorentz sequence space; all coordinate norms of each nonzero sequence agree and are positive.

These statements settle, by changing the ambient dual rather than requiring a tensor inequality inside a given Lorentz space, the closed-threshold and empty-spectrum spaceability questions explicitly distinguished from the open-threshold case in the motivating paper [1, §8]. No claim is made for a fixed prescribed predual or for the excluded endpoint \([1,\infty)\).

## Assumptions and scope
All Banach spaces and tensor products are **real**. For a bounded sequence \(y=(y_n)\subset E^*\), put
\[
G_q(y)=\{x\in E:(y_n(x))_{n\ge1}\in\ell_q\},\qquad q>0.
\]
Write \(\mathcal P(y)=\{q>0:\overline{G_q(y)}=E\}\), \(\mathcal S(y)=\{q>0:\text{some subsequence of }y\text{ has dense }G_q\}\), and, when \(y\) is Schauder basic, \(\mathcal B(y)=\{q>0:\text{some normalized successive block sequence of }y\text{ has dense }G_q\}\). The closures here are norm closures. These are density conditions, not the stronger all-point condition \(G_q(y)=E\).

Let \(w=(w_n)_{n\ge1}\) be positive and nonincreasing, with \(w_1=1\), \(w_n\to0\), and \(\sum_nw_n=\infty\). Define the real Lorentz sequence space \(Z=d(w,1)\) by
\[
\|a\|_Z=\sum_{n\ge1}a_n^*w_n,
\]
where \(a^*\) is the decreasing rearrangement of the absolute coordinates, and take the completion of finitely supported sequences. Let \(e_n\) denote its canonical unit basis, and put \(A_w=\{q>0:\sum_n w_n^q<\infty\}\). Such \(Z\) has a normalized \(1\)-symmetric, weakly null basis and is hereditarily \(\ell_1\); the relevant standard properties and their precise use appear in [1, §3.1] and [2].

For the closed-threshold case choose, for each \(r>1\),
\[
w_n=n^{-1/r}\left(\frac{\log 2}{\log(n+1)}\right)^{2/r}.
\]
For the empty case choose
\[
w_n=\frac{\log2}{\log(n+1)}.
\]
Both weights satisfy the stated assumptions. Elementary integral comparison gives \(A_w=[r,\infty)\) in the first case and \(A_w=\varnothing\) in the second. The values \(r\) are arbitrary fixed real numbers greater than one, not integers.

## Proof
**1. A fixed ambient space supporting a linear family.** Fix one of the two weights. Form the completed Banach-space projective tensor product
\[
V=Z\widehat\otimes_\pi Z,\quad E=V^*,\quad E^*=V^{**},
\]
and let \(J_V:V\to V^{**}\) be its canonical isometric embedding. For \(v\in Z\) define the bounded sequence of functionals
\[
\Theta(v)=u(v)=(J_V(e_n\otimes v))_{n\ge1}\in\ell_\infty(E^*).
\]
The equality \(\|a\otimes b\|_\pi=\|a\|_Z\|b\|_Z\) follows both from the defining projective upper bound and from a pair of norming functionals given by Hahn--Banach. Thus
\[
\|u(v)_n\|=\|v\|_Z,\qquad
\|\Theta(v)\|_{\ell_\infty(E^*)}=\|v\|_Z.
\]
The map \(\Theta\) is a linear isometry. Its range \(W=\Theta(Z)\) is consequently closed and infinite dimensional, and is hereditarily \(\ell_1\) because \(Z\) is. For each \(v\ne0\), the map
\[
J_v:Z\longrightarrow E^*,\qquad J_v(a)=J_V(a\otimes v)/\|v\|_Z
\]
is an isometry, with \(J_ve_n=u(v)_n/\|v\|_Z\). It follows at once that this normalized sequence is a \(1\)-symmetric Schauder basis for its own closed linear span: for every finite scalar family \((c_n)\),
\[
\left\|\sum_n c_nJ_ve_n\right\|=\left\|\sum_n c_ne_n\right\|_Z.
\]
The basis is weakly null in \(E^*\), because \((e_n)\) is weakly null in \(Z\) and \(J_v\) is bounded. In particular it is weak-star null, so it is normal.

**2. Every allowed exponent has all-point summability.** The space \(E=V^*\) is the Banach space of continuous real bilinear forms on \(Z\times Z\), under the standard projective-tensor duality. For \(B\in E\), \(v\in Z\), define \(f_{B,v}(a)=B(a,v)\). Then \(f_{B,v}\in Z^*\) and \(\|f_{B,v}\|\le\|B\|\|v\|_Z\). For every \(q\in A_w\), necessarily \(q>1\), Hölder's inequality for the Lorentz norm and duality yield the explicit coefficient estimate
\[
\left(\sum_n|f(e_n)|^q\right)^{1/q}\le\|f\|\left(\sum_nw_n^q\right)^{1/q}\qquad(f\in Z^*).
\]
Therefore the evaluation sequence \((u(v)_n(B))=(B(e_n,v))\) belongs to \(\ell_q\) for every \(B\in E\), and in fact
\[
\|(u(v)_n(B))\|_q\le\|B\|\|v\|_Z\|w\|_q.
\]
Thus \(G_q(u(v))=E\) for every \(q\in A_w\). The same holds after scalar normalization.

**3. Forbidden exponents remain forbidden for all normalized blocks and subsequences.** Let \(Y_v=J_vZ\subset E^*\) for \(v\ne0\). We verify independently the two hypotheses of the Lorentz weight criterion [1, Theorem 3.1] for this **new** embedding \(J_v\), rather than assume that the criterion automatically transfers under tensoring.

First, the norm-closed subspace \(X_v=\{a\otimes v:a\in Z\}\) of \(V\) is isomorphic to the hereditarily \(\ell_1\) space \(Z\). If a normalized strongly normal sequence existed in \(J_VX_v\subset V^{**}\) with predual \(V^*\), the restriction quotient map \(V^*\twoheadrightarrow X_v^*\) would transfer density of its \(G_1\)-domain to \(X_v^*\), because this restriction is surjective and open by Hahn--Banach. The canonical image of a hereditarily \(\ell_1\) space in its bidual admits no normalized strongly normal sequence [1, Lemma 2.4; 2, §10]. This is hypothesis (H1).

Second, weak-star convergence of a sequence in \(J_VX_v\) against every element of \(V^*\) is exactly weak convergence of the underlying sequence in \(X_v\), since every functional on \(X_v\) extends to \(V\). This is (H2).

The inspected Lorentz weight criterion [1, Theorem 3.1 and proof] now applies to \(J_v\) and gives, for **every normalized sequence** \(z\subset Y_v\),
\[
\overline{\bigcup_{q\notin A_w}G_q(z)}\ne E.
\]
The strength of this source theorem is essential: its proof passes from hypothetical dense summability to all-point summability, uses weakly null block approximation and Lorentz block domination, and then contradicts \(\sum_nw_n^q=\infty\) by testing coefficients \(w_n^{q-1}\) for \(q>1\). Thus it rules out every exponent outside \(A_w\) even for normalized blocks, not only for the coordinate sequence.

Since the normalized sequence \((J_ve_n)\) itself witnesses all exponents in \(A_w\), and every normalized block or subsequence lies in \(Y_v\), we conclude
\[
\mathcal P(J_ve_n)=\mathcal S(J_ve_n)=\mathcal B(J_ve_n)=A_w.
\]
For the first chosen weight this is \([r,\infty)\); for the second it is \(\varnothing\). Multiplying an entire sequence by a fixed nonzero scalar does not change any of these spectra, completing both assertions. \(\square\)

## Verification
The projective crossnorm equality for simple tensors and the norm identity for finite combinations are exact consequences of the definition and Hahn--Banach, not numerical approximations. The critical nonstandard input, the hereditary exclusion of all forbidden exponents, was inspected in [1, §3.1, Theorem 3.1]; its structural hypotheses were checked separately above for the new tensor ambient space. The first weight has \(w_n^r=(\log2)^2/[n(\log(n+1))^2]\), giving endpoint inclusion; lower powers diverge. For the second, each \(w_n^q\) dominates a suitable constant multiple of \(n^{-1/2}\) for all large \(n\), so no finite positive exponent is allowed. The two endpoint calculations are elementary infinite-series comparisons; no finite computation purports to certify them.

## Relationship to prior work
Śliwa [1, Corollary 3.5 and Theorem 3.6] constructs **one** normalized weakly null basic sequence with each of the listed spectra, including closed and empty. His Theorem 3.10 establishes a **closed linear space of sequences** only for open thresholds \((r,\infty)\), using a special coordinate-tensor inequality for the pure power weight, and §8 explicitly leaves closed-threshold and empty-spectrum spaceability open. The present tensor product changes the **ambient dual**, preserving the Lorentz hereditary obstruction while obtaining a closed linear family with no special coordinate-tensor estimate. Individual realizability and the hereditary obstruction are credited to [1], not claimed as new. The related paper [2, Theorem 26] constructs a closed subspace of functionals containing no strongly normal sequence at the exponent-one level; it does not give the two stated uniform all-exponent spaceability classifications of **sequences**. The survey [3] describes general spaceability methodology, without this density-spectrum classification.

## Limitations
The conclusion concerns real dual spaces constructed separately for each weight, and the norm-closed subspace \(W\) lies in the **sequence space** \(\ell_\infty(E^*)\), not merely in \(E^*\). No fixed-predual or smallest-density claim is made. No classification of arbitrary triples of spectra is asserted; no claim concerns the inadmissible closed endpoint \([1,\infty)\). The proof depends on the published/preprint Lorentz hereditary criterion [1], whose classical block-domination input is cited there. While full-text scientific comparisons were made with the closest sources, a previously unlocated general lineability or tensor-stability theorem could subsume the construction; publication priority is not independently certified.

## References
[1] W. Śliwa, *Selection spectra and sharp perturbations of normal sequences*, arXiv:2610.38853v2 (first public version October 28, 2026), especially §§3.1–3.3 and 8. https://arxiv.org/html/2610.38853v2 .

[2] W. Śliwa, *Reflexivity of Grothendieck Spaces and Strongly Normal Sequences*, arXiv:2610.12787 (October 8, 2026), especially §10, Theorem 26. https://arxiv.org/abs/2610.12787 .

[3] L. Bernal-González, D. Pellegrino and J. B. Seoane-Sepúlveda, *Linear subsets of nonlinear sets in topological vector spaces*, Bull. Amer. Math. Soc. 51 (2014), 71–130. https://doi.org/10.1090/S0273-0979-2013-01421-6 .
