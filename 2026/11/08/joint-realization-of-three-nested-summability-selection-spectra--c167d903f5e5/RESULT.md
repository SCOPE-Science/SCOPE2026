# Joint realization of three nested summability-selection spectra with a nonempty original domain

## Finding
Let \(\mathfrak A=\{\varnothing,(0,\infty),(1,\infty)\}\cup\{[r,\infty),(r,\infty):r>1\}\). **For every ordered triple \(K\subseteq I\subseteq J\) in \(\mathfrak A\), there is a real Banach space \(E\) and a normalized, weakly null, \(1\)-unconditional Schauder basic sequence \(y=(y_n)\subset E^*\) such that**
\[
 (\mathcal P(y),\mathcal S(y),\mathcal B(y))=(K,I,J).
\]
Here \(\mathcal P\) is the set of exponents for which the *original* evaluation-\(\ell_p\) domain is dense, \(\mathcal S\) the corresponding subsequence selection spectrum, and \(\mathcal B\) the normalized successive-block selection spectrum. Thus all three thresholds can be strictly different, including independently open or closed endpoints consistent with inclusion. The new case is \(\varnothing\ne K\subseteq I\subseteq J\subsetneq(0,\infty)\); the other cases follow by precise combinations of previously proved constructions. This is a realization theorem, **not** a necessary classification of original-sequence spectra outside \(\mathfrak A\).

## Assumptions and scope
All spaces and scalars are real. For \(0<p<\infty\) and bounded \(y\subset E^*\), set
\[
 G_p(y)=\{x\in E:(y_n(x))\in\ell_p\},\qquad
 \mathcal P(y)=\{p>0:\overline{G_p(y)}=E\}.
\]
For a normalized basic \(y\), define \(\mathcal S(y)\) using subsequences and \(\mathcal B(y)\) using normalized finite successive blocks. An admissible block may have zero coefficients within its supporting interval. A sequence is \(p\)-strongly normal when its \(G_p\) domain is dense. Norm-null perturbations preserve each fixed subsequence exponent (Śliwa [1], Corollary 2.11). We use four proved auxiliary facts from [1]: Lorentz weight criterion, the hereditary \(\ell_1\) obstruction to strongly normal sequences in the canonical predual, amplification of a proper dense \(G_p\) into strongly normal blocks for \(p>1\), and saturation of finite-dimensional \(\ell_1\)-block sums (Theorem 3.1; Lemmas 2.4 and 4.5; Proposition 2.5). They are invoked with their stated hypotheses; no assertion of independent proof of those inputs is made.

## Proof
**1. Lorentz data and an amplitude lemma.** For any nonempty proper \(H\in\mathfrak A\), let \(Z_H=d(w^H,1)\) be the Lorentz space with normalized symmetric basis \((e_n^H)\) and weight
\[
 w_n^H=\begin{cases}
 1/n,&H=(1,\infty),\\
 n^{-1/r},&H=(r,\infty),\\
 n^{-1/r}(\log2/\log(n+1))^{2/r},&H=[r,\infty).
 \end{cases}
\]
Its fundamental function is \(W_H(m)=\sum_{n\le m}w_n^H\). By [1, Theorem 3.1 and Corollary 3.5], \(w^H\in\ell_p\) exactly for \(p\in H\); its unit basis is weakly null, and no normalized sequence in \(Z_H\) has an upper \(\ell_{p'}\) synthesis estimate when \(p>1\) and \(p\notin H\). (For a general normalized sequence this follows from the stated hereditary non-density under the canonical embedding and the closed-graph equivalence.) Each \(Z_H\) is \(\ell_1\)-saturated.

Assume henceforth \(\varnothing\ne K\subseteq I\subseteq J\subsetneq(0,\infty)\). Choose a scalar function \(d(m)>0\), for sufficiently large integers \(m\), by
\[
 d(m)=\begin{cases}
 (\log(m+1))^2/m,&K=(1,\infty),\\
 m^{-1/t}\log(m+1),&K=(t,\infty),\\
 m^{-1/t},&K=[t,\infty).
 \end{cases}
\]
Direct power/logarithm comparison gives \(d(m)\to0\), and for every \(p>1\),
\[
 \sup_{m\gg1} d(m)m^{1/p}<\infty \ \Longleftrightarrow\ p\in K,
\]
where for \(p\notin K\), \(d(m)m^{1/p}\to\infty\). Further, inclusion \(K\subseteq I\) and the displayed Lorentz weights give
\[
 \frac{W_I(m)}{m d(m)}\longrightarrow0.
\]
At equal open thresholds this is the reciprocal of a logarithm; at equal closed thresholds it is a negative power of a logarithm. Strictly smaller thresholds improve the estimate. Choose increasing integers \(m_k\) so large that \(\delta_k=d(m_k)<1\), \(m_k\to\infty\), and
\[
 \frac{W_I(m_k)}{\delta_k m_k}\le2^{-k^2}.
\]
The asymptotics also show \(\sup_k\delta_km_k^{1/p}<\infty\) for \(p\in K\), and \(\delta_km_k^{1/p}\to\infty\) for any \(p>1\) not in \(K\).

**2. Three-layer construction.** Put
\[
 X=\left(\bigoplus_{k\ge1}\ell_1^{m_k}\right)_{Z_J},\qquad
 \|(x_{ki})\|_X=\left\|\sum_k\Bigl(\sum_{i=1}^{m_k}|x_{ki}|\Bigr)e_k^J\right\|_{Z_J},
\]
\(V=Z_I\oplus_\infty X\), and \(E=V^*\). Regard \(V\) canonically in \(E^*=V^{**}\). In lexicographic successive order \(n=n(k,i)\), define
\[
 y_{n(k,i)}=(e_{n(k,i)}^I,\delta_ke_{ki}^X).
\]
The coefficient norm is the maximum of the unconditional Lorentz norm and the weighted mixed-block norm; coordinate projections are contractive, so \(y\) is a \(1\)-unconditional Schauder basic sequence. Every term has norm one. The first coordinates tend weakly to zero, and the second coordinates have norm \(\delta_k\to0\), so \(y\) is weakly null. Lemma 4.5 of [1] makes \(V\) hereditarily \(\ell_1\); Lemma 2.4 therefore excludes normalized strongly normal sequences in its canonical image in \(E^*\).

**3. Exact original spectrum \(\mathcal P(y)=K\).** Fix \(p\in K\), so \(p>1\) and \(p\in I\cap J\). Since \(w^I,w^J\in\ell_p\), Lorentz-Hölder gives \(\|\sum c_ne_n^I\|\le\|w^I\|_p\|c\|_{p'}\). Also rowwise Hölder and Lorentz-Hölder give
\[
 \left\|\sum_{ki}\delta_kc_{ki}e_{ki}^X\right\|
 \le\|w^J\|_p\Bigl(\sup_k\delta_km_k^{1/p}\Bigr)\|(c_{ki})\|_{p'}.
\]
Hence \(y\) has an upper \(\ell_{p'}\) synthesis bound, equivalent by duality to \(G_p(y)=E\). Conversely, for \(p>1\) outside \(K\), choose coefficients one on an entire row \(k\) and zero elsewhere. Their \(\ell_{p'}\) norm is \(m_k^{1/p'}\), but the second component of their synthesis has norm \(\delta_km_k\). The synthesis ratio \(\delta_km_k^{1/p}\to\infty\), so the closed graph theorem implies \(G_p(y)\ne E\). If this domain were dense, Proposition 2.5 of [1] would create a normalized strongly normal block sequence inside \(V\), contrary to hereditary \(\ell_1\) obstruction. For \(0<p\le1\), dense \(G_p(y)\subseteq G_1(y)\) would directly make the normalized sequence strongly normal, again impossible. This proves \(\mathcal P(y)=K\), including its critical endpoint.

**4. Exact subsequence spectrum \(\mathcal S(y)=I\).** Compare \(y_{n(k,i)}\) to \(y_{n(k,i)}^0=(e_{n(k,i)}^I,0)\). Their norm difference is \(\delta_k\to0\). The Lorentz weight criterion gives every subsequence of \(y^0\) precisely the selection spectrum \(I\) (the extra direct-sum coordinate is annihilated). Corollary 2.11 of [1], applied separately for each exponent, preserves the existence or nonexistence of a good subsequence under norm-null errors. Thus \(\mathcal S(y)=I\).

**5. Exact block spectrum \(\mathcal B(y)=J\).** Define the normalized successive row blocks
\[
 u_k=\frac1{\delta_km_k}\sum_{i=1}^{m_k}y_{n(k,i)},\qquad
 t_k=\frac1{m_k}\sum_{i=1}^{m_k}e_{ki}^X.
\]
The second component of \(u_k\) is \(t_k\), with \(\|t_k\|=1\), while the first component has norm at most \(2^{-k^2}\). Thus \(\|u_k\|=1\). The sequence \((t_k)\) is isometric to the unit basis of \(Z_J\), so \((0,t_k)\) has \(G_p=E\) for every \(p\in J\). The summable errors \(2^{-k^2}\) preserve all these domains, proving \(J\subseteq\mathcal B(y)\).

For \(p\le1\), the hereditary \(\ell_1\) obstruction excludes all normalized strongly normal block sequences. For \(p>1\) outside \(J\), suppose normalized successive blocks \(b_j=(a_j,c_j)\in Z_I\oplus_\infty X\) had dense \(G_p\). By the same obstruction and Proposition 2.5, \(G_p(b)=E\), hence \(b\) has an upper \(\ell_{p'}\) synthesis estimate. Since \(\|b_j\|=1\), either a subsequence has \(\|a_j\|\ge\epsilon>0\), or a subsequence satisfies \(\|a_j\|\to0\) and \(\|c_j\|=1\). In the first case the normalized, successive disjoint \(a_j/\|a_j\|\) form a sequence in \(Z_I\) with an upper \(\ell_{p'}\) estimate. This contradicts the hereditary Lorentz weight criterion, since \(p\notin J\) and \(I\subseteq J\) imply \(p\notin I\). In the second case, thin the blocks so their finitely supported \(X\) coordinates occupy disjoint outer-row intervals (each outer row is finite). Define their row-profile vectors
\[
 d_j=\sum_k\Bigl(\sum_{i=1}^{m_k}|(c_j)_{ki}|\Bigr)e_k^J\in Z_J.
\]
These are normalized successive disjoint blocks of \(Z_J\), and, for arbitrary finitely supported scalars, their unconditional norms equal the norms of the corresponding combinations of \(c_j\) in \(X\). Thus they inherit an upper \(\ell_{p'}\) bound, again contradicting the hereditary Lorentz criterion for \(p\notin J\). Therefore \(\mathcal B(y)\subseteq J\) and equality holds.

**6. Boundary cases.** If \(K=\varnothing\), Theorem 4.4 of [1] constructs \((\mathcal P,\mathcal S,\mathcal B)=(\varnothing,I,J)\) for every \(I\subseteq J\) in \(\mathfrak A\). If \(J=(0,\infty)\), \(K\ne\varnothing\), and \(I\subsetneq(0,\infty)\), take [1, Corollary 4.2]'s sequence \(a\) with spectra \((I,I,(0,\infty))\), and a Lorentz sequence \(b\) with spectra \((K,K,K)\). Interleave \(a\) and \(b\) in the dual of the direct sum of their respective preduals. For an interleaved direct-sum sequence, the original domain is the direct sum of the two domains and so its spectrum is their intersection; the subsequence spectrum is the union (a good subsequence has infinitely many entries in at least one component, whereas good subsequences of either component can be selected); and any normalized block sequence of one component is allowed as a block sequence of the interleaving by inserting zero coefficients. Thus \((\mathcal P,\mathcal S,\mathcal B)=(K,I,(0,\infty))\). If \(I=J=(0,\infty)\), use the same interleaving with an orthonormal Hilbert-space basis in place of \(a\). The all-full triple is already realized by such a Hilbert basis. Every case is covered. \(\square\)

## Verification
All infinite-dimensional claims above follow by analytical inequalities, duality, hereditary Lorentz obstructions, and the explicitly cited published lemmas. No finite experiment is presented as an infinite proof. Critical checks are: (i) the amplitude/weight asymptotics, especially both open and closed critical endpoints; (ii) the exact row-vector synthesis ratio; (iii) the uniform \(\ell_{p'}\) bound in the favorable range; (iv) normalized row blocks and the disjoint-row profile argument; and (v) the direct-sum interleaving identities. A finite exact-arithmetic checker included with this result corroborates only the purely algebraic row-profile identities on finite matrices; it does not validate infinite-dimensional saturation or novelty.

## Relationship to prior work
Śliwa [1, Theorem 4.4] establishes all nested pairs \((\mathcal S,\mathcal B)\) and realizes them with \(\mathcal P=\varnothing\); its Section 8 explicitly leaves triple classification open. Its Corollary 4.2 realizes \(\mathcal P=\mathcal S=I\) and full \(\mathcal B\), while Theorem 3.6 realizes diagonal triples. None of those implications gives a nonempty **strictly smaller** original spectrum with three distinct proper thresholds. The present variable-amplitude construction controls \(\mathcal P\) while separately retaining \(\mathcal S\) and \(\mathcal B\), proving the stated sufficiency on the natural admissible family. The earlier paper [2] studies strong normality and quotients, not this three-parameter all-exponent realization. General Lorentz-space structural results [3] are used through the precise statements verified in [1].

## Limitations
The theorem does not classify what values of \(\mathcal P(y)\) may occur outside \(\mathfrak A\), nor prove that nestedness is sufficient for arbitrary nonstandard upper sets. Its constructions depend on the cited hereditary \(\ell_1\) and Lorentz basic-sequence results. No independent mathematical audit has been performed. Publication-priority comparison is best-knowledge, not proof of uniqueness; an equivalent older, differently formulated block-amplitude construction may exist.

## References
[1] Wiesław Śliwa, *Selection spectra and sharp perturbations of normal sequences*, arXiv:2610.38853v1, first posted 2026-10-28, Sections 2–4 and 8. https://arxiv.org/html/2610.38853v1

[2] Wiesław Śliwa, *The separable quotient problem and the strongly normal sequences*, J. Math. Soc. Japan 64 (2012), 387–397. https://doi.org/10.2969/jmsj/06420387

[3] A. Kamińska, A. I. Popov, E. Spinu, A. Tcaciuc, and V. G. Troitsky, *Norm closed operator ideals in Lorentz sequence spaces*, J. Math. Anal. Appl. 389 (2012), 247–260. https://doi.org/10.1016/j.jmaa.2011.11.034
