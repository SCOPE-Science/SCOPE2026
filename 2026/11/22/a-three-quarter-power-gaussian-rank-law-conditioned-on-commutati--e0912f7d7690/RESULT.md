# A three-quarter-power Gaussian rank law conditioned on commutation in the symmetric inverse monoid

## Finding

Let \(\mathcal I_n\) be the symmetric inverse monoid of all partial bijections of \([n]\), including the empty map, and let \(E_n\) be its \(2^n\) idempotents (partial identities). Choose \(e\in E_n\) and \(f\in\mathcal I_n\) independently and uniformly. Set \(K_n=|\operatorname{dom}e|\), and let \(\mathsf C_n\) denote \(ef=fe\). For all \(n\geq 0\), writing
\[
R_m=\sum_{j=0}^m\binom mj^2j!=m!L_m^{(0)}(-1),
\]
where \(L_m^{(\alpha)}\) is the generalized Laguerre polynomial,
\[
\Pr(\mathsf C_n)=\frac{L_n^{(1)}(-2)}{2^nL_n^{(0)}(-1)},\qquad
\Pr(K_n=k\mid\mathsf C_n)=\frac{L_k^{(0)}(-1)L_{n-k}^{(0)}(-1)}{L_n^{(1)}(-2)}\quad(0\le k\le n).
\]
The exact formulas are consequences of the established idempotent-centralizer decomposition; they are not advanced as new by themselves. The asserted asymptotic conclusion is that
\[
\Pr(\mathsf C_n)\sim \frac{e^{-1/2}}{2^{3/4}}\,\sqrt n\,2^{-n}\exp\bigl(2(\sqrt2-1)\sqrt n\bigr)
\]
and, conditionally on \(\mathsf C_n\),
\[
\frac{K_n-n/2}{n^{3/4}}\ \Longrightarrow\ \mathcal N\left(0,\frac1{2\sqrt2}\right).
\]
More precisely, uniformly for \(x\) in any fixed bounded real interval, with \(k_n=\lfloor n/2+xn^{3/4}\rfloor\),
\[
 n^{3/4}\Pr(K_n=k_n\mid\mathsf C_n)\longrightarrow\frac{2^{1/4}}{\sqrt\pi}e^{-\sqrt2x^2}.
\]
Unconditionally, \(K_n\) is \(\operatorname{Bin}(n,1/2)\); thus conditioning on the rare commuting event broadens its fluctuations from \(n^{1/2}\) to \(n^{3/4}\).

## Assumptions and scope

All maps are functions between subsets of the labeled set \([n]=\{1,\dots,n\}\); multiplication means composition, and equality of partial maps requires equality of domains and values. The empty set convention makes \(\mathcal I_0\) a one-element monoid and all finite formulas valid at \(n=0\). Limit statements concern integer \(n\to\infty\). The choice of \(e\) is uniform among *idempotents*, not among all elements of \(\mathcal I_n\).

The generalized Laguerre normalization throughout is
\[
 L_n^{(\alpha)}(z)=\sum_{j=0}^{n}\binom{n+\alpha}{n-j}\frac{(-z)^j}{j!},\qquad \alpha\in\{0,1\}.
\]

## Proof

**(1) Established centralizer decomposition and finite count.** The idempotent \(e=e_S\) is the identity precisely on some \(S\subseteq[n]\). For every \(x\in\operatorname{dom}f\), equality \(e_Sf=fe_S\) forces \(x\in S\) if and only if \(f(x)\in S\); conversely this condition makes the two compositions equal. Therefore \(f\) splits uniquely into independent partial bijections on \(S\) and \([n]\setminus S\). For \(|S|=k\) the centralizer has size \(R_kR_{n-k}\). Since the number of partial bijections of rank \(j\) on \(m\) points is \(\binom mj^2j!\), the number of commuting pairs with idempotent rank \(k\) equals \(\binom nkR_kR_{n-k}\).

**(2) Laguerre convolution.** The classical generating series
\[
 \sum_{m\ge0}L_m^{(0)}(-1)z^m=(1-z)^{-1}\exp\bigl(z/(1-z)\bigr)
\]
implies, on squaring,
\[
 \sum_{k=0}^nL_k^{(0)}(-1)L_{n-k}^{(0)}(-1)=L_n^{(1)}(-2).
\]
After cancellation of factorials, the exact probabilities in the finding follow.

**(3) Negative-argument Laguerre asymptotics.** For fixed \(\alpha\in\{0,1\}\) and fixed \(x>0\), the classical Perron asymptotic at the negative argument \(-x\) is
\[
 L_n^{(\alpha)}(-x)=\frac{e^{-x/2}}{2\sqrt\pi}\,x^{-\alpha/2-1/4}n^{\alpha/2-1/4}\exp(2\sqrt{nx})\bigl(1+O(n^{-1/2})\bigr).
\]
This can also be reconstructed from the positive sum above: its terms concentrate at \(j=\sqrt{nx}+O(n^{1/4})\); uniformly in this window, expansion of the falling factorial gives \(\binom{n+\alpha}{n-j}=n^{j+\alpha}e^{-j^2/(2n)}(j+\alpha)!^{-1}(1+o(1))\). Stirling's formula and a Gaussian sum supply the coefficient; the terms outside a growing multiple of this window are negligible by adjacent-term ratios. This is an asymptotic theorem, not an inference from finite checks.

Applying this formula to \((\alpha,x)=(1,2)\) and \((0,1)\) proves the commuting-probability asymptotic, with all constants shown in the finding.

**(4) Local and global conditional Gaussian law.** Write \(k=n/2+s\), where \(s=xn^{3/4}+O(1)\) and \(x\) ranges in a fixed compact set. The two \(L^{(0)}\) expansions from (3) are uniform here, since both indices tend to infinity proportionally to \(n\). Taylor expansion at the midpoint gives
\[
2\sqrt{k}+2\sqrt{n-k}=2\sqrt{2n}-\sqrt2\,x^2+o(1),\qquad
[k(n-k)]^{-1/4}=\sqrt2\,n^{-1/2}(1+o(1)).
\]
Substituting the denominator expansion with \((\alpha,x)=(1,2)\) yields
\[
\Pr(K_n=k\mid\mathsf C_n)=n^{-3/4}\frac{2^{1/4}}{\sqrt\pi}e^{-\sqrt2 x^2}(1+o(1)),
\]
uniformly for bounded \(x\). Summing over the lattice points in any fixed bounded interval gives convergence to the corresponding Gaussian integral. As that limiting density integrates to one, taking intervals increasing to the full real line proves tightness and weak convergence. This completes all quantified claims.

## Verification

The standalone `check.py` constructs every partial bijection for \(0\le n\le4\) independently of the counting formula and explicitly compares compositions with every partial identity. It checks the exact rank-resolved counts, plus an independent recurrence for \(R_m\). Its finite outputs are recorded in `check_output.txt`. The program also computes asymptotic ratios at dimensions \(100,400,1600,6400\); these diagnostics are not a proof of any limit. See `VERIFICATION.md` for the precise commands and limitations.

## Relationship to prior work

Araújo, Bentz and Konieczny (2012), Proposition 2.2 and Lemma 2.3, already establish the commuting criterion and idempotent block decomposition in the symmetric inverse semigroup. The exact enumeration here is an immediate consequence and is not claimed as an independently new contribution. Konieczny (2020) develops general first- and second-centralizer structures in this monoid; only its abstract was accessible for comparison. The classical Laguerre convolution and negative-argument asymptotics are standard analytic inputs. The assessment of novelty is confined to the *specific conditional rank local limit, its \(n^{3/4}\) fluctuation scale, and the sharp probability asymptotic in this semigroup experiment*. Relevant existing random partial-map results concern different conditioning events.

## Limitations

This theorem concerns one uniform idempotent paired with one uniform arbitrary partial injection; it does not describe commutation of two unrestricted uniform partial injections. Full-text historical comparison with the 2020 centralizer paper was unavailable, so priority is not independently certified. The asymptotic error rate beyond \(1+o(1)\) is not quantified for the conditional distribution. No external independent mathematical review has been performed.

## References

1. J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664 (initial public version 2012-05-08), https://arxiv.org/abs/1205.1664; especially Proposition 2.2 and Lemma 2.3.
2. J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, Communications in Algebra 48 (2020), 5181–5194, https://doi.org/10.1080/00927872.2020.1782926 (abstract consulted; full text unavailable).
3. A. Laradji and A. Umar, *On the Number of Nilpotents in the Partial Symmetric Semigroup*, Communications in Algebra 32 (2004), 3017–3023, https://doi.org/10.1081/AGB-120038637 (abstract; Laguerre enumeration in a different counting problem).
4. G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society (1975), Theorem 8.22.3 (Perron asymptotics for Laguerre polynomials at negative arguments), https://people.math.osu.edu/nevai.1/SZEGO/szego%3Dszego1975%3Dops%3DOCR.pdf. See also NIST DLMF §18.15(iv), https://dlmf.nist.gov/18.15.
5. OEIS A002720, https://oeis.org/A002720 (the classical total number of partial permutations, not a claim of novelty).
