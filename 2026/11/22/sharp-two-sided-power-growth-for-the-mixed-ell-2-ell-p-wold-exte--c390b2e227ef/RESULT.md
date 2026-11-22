# Sharp two-sided power growth for the mixed \(\ell_2\)–\(\ell_p\) Wold extension

## Finding

Let \(1<p<\infty\). The concrete Hilbert-negative-tail extension of the right shift on \(\ell_p\), described below, has exactly one direction of polynomial power growth when \(p\ne2\):
\[
(\|U^n\|,\|U^{-n}\|)=
\begin{cases}
((n+1)^{1/p-1/2},1),&1<p<2,\\
(1,1),&p=2,\\
(1,(n+1)^{1/2-1/p}),&2<p<\infty
\end{cases}\qquad(n\in\mathbb N,\ n\ge1).
\]
All these bounds are attained on finitely supported vectors. Moreover, \(\sigma(U)=\mathbb T\). For \(p\ne2\), no equivalent norm makes this particular extension a surjective isometry, although the underlying unilateral shift has a different, genuinely isometric bilateral extension.

## Assumptions and scope

Fix \(1<p<\infty\) and complex scalars. Let \(X_p=\ell_p(\mathbb N_0)\), \(S e_j=e_{j+1}\), and \(L=\operatorname{span}\{e_0\}\). The range of \(S\) is complemented by \(L\) with a norm-one coordinate projection. Define
\[
Y_p=\ell_2(\mathbb Z_{<0})\oplus_2\ell_p(\mathbb N_0),\qquad
\|x\|_{Y_p}^2=\sum_{j<0}|x_j|^2+\left(\sum_{j\ge0}|x_j|^p\right)^{2/p}.
\]
Let \(U e_j=e_{j+1}\) for every \(j\in\mathbb Z\). This is the extension obtained by specializing the construction in Lemma 5.3, equation (5.1), of Jana–Pal–Roy to \(S\) and \(L\). It is invertible and agrees with \(S\) on the embedded positive-coordinate copy of \(X_p\).

## Proof

Write \(x=(x_-,x_+)\) in the displayed direct sum. For every \(n\ge1\), split the negative tail into the \(n\) coordinates \(u\in\mathbb C^n\) crossing the junction under \(U^n\), and the remaining negative tail \(v\). Set \(b=\|x_+\|_p\). Then exactly
\[
\|x\|_{Y_p}^2=\|u\|_2^2+\|v\|_2^2+b^2,
\quad
\|U^n x\|_{Y_p}^2=\|v\|_2^2+
\big(\|u\|_p^p+b^p\big)^{2/p}.
\]
If \(p<2\), the sharp finite-dimensional comparison
\[
\big(\|u\|_p^p+b^p\big)^{1/p}
\le(n+1)^{1/p-1/2}\big(\|u\|_2^2+b^2\big)^{1/2}
\]
yields the upper bound. Equality follows by taking \(v=0\), all \(n\) entries of \(u\) equal to one, and \(x_+=e_0\). The norm ratio is \((n+1)^{1/p-1/2}\). If \(p\ge2\), comparison of \(\ell_p\) against \(\ell_2\) gives \(\|U^n\|\le1\); a vector supported entirely on sufficiently negative coordinates gives equality one.

For the inverse, split the positive tail into the first \(n\) coordinates \(u\in\mathbb C^n\) crossing the junction under \(U^{-n}\), and the remaining part \(w\), with \(b=\|w\|_p\). Write \(a=\|x_-\|_2\). Exactly
\[
\|x\|_{Y_p}^2=a^2+(\|u\|_p^p+b^p)^{2/p},
\quad
\|U^{-n}x\|_{Y_p}^2=a^2+\|u\|_2^2+b^2.
\]
If \(p>2\), the sharp comparison of \(\ell_2^{n+1}\) to \(\ell_p^{n+1}\) gives
\[
\|U^{-n}x\|_{Y_p}\le(n+1)^{1/2-1/p}\|x\|_{Y_p}.
\]
Equality is obtained by setting \(x_-=0\), all \(n\) entries of \(u\) equal to one, and \(w=e_n\) interpreted as the first remaining positive coordinate. If \(p\le2\), the embedding inequality in the other direction shows \(\|U^{-n}\|\le1\), and negative-supported vectors prove the reverse bound. At \(p=2\), \(Y_2=\ell_2(\mathbb Z)\) and both directions are isometric.

Both \(\|U^n\|\) and \(\|U^{-n}\|\) grow at most polynomially, so the spectral-radius formula gives \(r(U)=r(U^{-1})=1\) and \(\sigma(U)\subseteq\mathbb T\). The diagonal isometries \((D_\theta x)_j=e^{ij\theta}x_j\) obey \(D_\theta U D_\theta^{-1}=e^{i\theta}U\). The spectrum of any bounded operator on a nonzero complex Banach space is nonempty and is rotation invariant here, hence equals \(\mathbb T\).

If \(U\) were a surjective isometry under an equivalent norm, uniform equivalence of norms would bound \(\|U^n\|\) for every integer \(n\), contradicting the exact unbounded direction when \(p\ne2\). Meanwhile, the usual right bilateral shift on \(\ell_p(\mathbb Z)\) is a surjective isometry extending \(S\), showing that the obstruction belongs to the chosen mixed-norm extension, not to \(S\) itself.

## Verification

The sharp power bounds follow from equality cases in the finite-dimensional norm inequalities \(\|z\|_r\le d^{1/r-1/s}\|z\|_s\) for \(1\le r<s\) and \(d=n+1\). For every \(n\), the stated explicit vectors have exactly \(n+1\) equal nonzero coordinates straddling the norm interface, making the ratio exact. No numerical extrapolation or infinite-dimensional computation is needed. The nonzero spectral claim follows independently from the spectral-radius formula and rotation conjugation.

## Relationship to prior work

Jana, Pal and Roy, *On Słociński-type decomposition, BCL model and unitary extension of commuting Banach space Wold isometries* (arXiv:2611.11536, first public version 8 November 2026), construct precisely the one-step invertible extension in Lemma 5.3 and give a qualitative characterization of its isometric case in Theorem 5.4. Their Section 5 estimates the one-step operator norm and does not state the all-power growth profile or the resulting obstruction to equivalent isometric renorming. The mixed-norm power formula is a quantitative analysis of this specific construction, not a new general existence theorem for Banach-space unitary extensions. Related finite-block \(\ell_p\)-sum norm distortions are classical; the new assertion concerns their accumulation under every iterate across a single norm junction.

## Limitations

The theorem concerns the specific negative-\(\ell_2\), positive-\(\ell_p\) completion and not every invertible extension of \(S\). It makes no claim that \(S\) lacks a Banach unitary extension, nor that this power growth persists for alternative completions. The proof uses sharp elementary finite-dimensional norm comparison after identifying the junction geometry; the possibility of an earlier general mixed-sequence-shift treatment remains a bibliographic risk. Independent review has not been performed.

## References

1. S. Jana, S. Pal, S. Roy, *On Słociński-type decomposition, BCL model and unitary extension of commuting Banach space Wold isometries*, arXiv:2611.11536v1, 8 November 2026, Section 5, Lemma 5.3 and Theorem 5.4. https://arxiv.org/html/2611.11536v1
2. R. G. Douglas, *On extending commutative semigroups of isometries*, cited and discussed in Jana–Pal–Roy, Section 5. The general unitary-extension existence assertion is background, not a novelty claim.
