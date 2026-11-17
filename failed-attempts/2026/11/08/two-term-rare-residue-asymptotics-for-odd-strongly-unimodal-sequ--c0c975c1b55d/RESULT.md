# Two-term rare-residue asymptotics for odd strongly unimodal sequences

## Finding

Let \(u_{\mathrm{odd}}^*(n)\) count odd strongly unimodal sequences of total weight \(n\): finite strictly increasing-then-strictly-decreasing sequences of positive **odd** integers, with a distinguished maximum, whose terms sum to \(n\). For integer \(X\ge3\), set
\[
R_2(X)=\#\{1\le n\le X:\ n\text{ odd and }u_{\mathrm{odd}}^*(n)\equiv2\pmod4\}.
\]
Then, as \(X\to\infty\),
\[
\boxed{R_2(X)=\frac{\pi^2}{12}\frac{X}{\log X}
+\frac{\pi^2}{12}\left(1+\frac43\log2-\frac54\log3
-2\frac{\zeta'(2)}{\zeta(2)}\right)\frac{X}{(\log X)^2}
+O\!\left(\frac{X}{(\log X)^3}\right).}
\]
The implied constant is absolute. The first two numerical coefficients are approximately \(0.822467033424\) and \(1.390670740738\).

Moreover, let \(M=\lfloor\sqrt{(3X-1)/2}\rfloor\). The count of **odd** values among the same odd-indexed coefficients is exactly
\[
R_{\mathrm{odd}}(X)=M-\lfloor M/3\rfloor
=\sqrt{2X/3}+O(1).
\]
Consequently the count of nonzero residues modulo four among odd indices is \(R_2(X)+R_{\mathrm{odd}}(X)\). The residue zero has natural density one *among positive odd indices*, while residue two has the two-term rare-event law above.

## Assumptions and scope

The argument uses Banerjee and Ghosh Dastidar's exact 2026 residue characterization for positive **odd** \(n\) (their Theorem 1.5), not a new proof of that characterization. In their notation, the residue-two condition is equivalent to
\[
3n-1=\varepsilon p^{4j+1}m^2,
\qquad \varepsilon\in\{1,2\},\ j\ge0,\ m\ge1,
\]
with \(p\ge5\) prime, \(p\nmid m\), and Legendre symbol \(\left(\frac{-2}{p}\right)=-1\). The parity condition is \(3n-1=2m^2\). The new contribution is the global two-term frequency law and its explicit constants, rather than the published pointwise membership criterion. The only further analytic input is the prime number theorem in fixed reduced residue classes modulo \(24\).

## Proof

**1. Admissible prime classes.** For odd \(n\), \(3n-1\equiv2\pmod6\). The character condition \(\left(\frac{-2}{p}\right)=-1\) is equivalent to \(p\equiv5,7\pmod8\). In the representation above, \(3\nmid m\) necessarily. If \(\varepsilon=1\), then \(m\) must be even and \(p\equiv2\pmod3\), giving \(p\equiv5,23\pmod{24}\). If \(\varepsilon=2\), every \(m\) coprime to three is permitted and \(p\equiv1\pmod3\), giving \(p\equiv7,13\pmod{24}\). Conversely, each indicated representation gives a valid positive odd \(n=(\varepsilon p^{4j+1}m^2+1)/3\). The representing odd-exponent prime is unique, and the parity of the exponent of two determines \(\varepsilon\), so there is no double counting.

**2. Negligible higher powers and repeated primes.** The representations with \(j\ge1\) contribute at most
\[
O\!\left(\sqrt X\sum_{p\ge5}\sum_{j\ge1}
 p^{-(4j+1)/2}\right)=O(\sqrt X).
\]
For \(j=0\), temporarily including the prohibited pairs \(p\mid m\) adds at most
\[
O\!\left(\sqrt X\sum_{p\ge5}p^{-3/2}\right)=O(\sqrt X).
\]
Both statements follow by bounding the number of possible square multipliers and using convergent prime sums.

**3. Prime counts and truncation.** Write \(L=\log X\), let \(\mathcal M_1=\{m\ge1:2\mid m,\ 3\nmid m\}\), and let \(\mathcal M_2=\{m\ge1:3\nmid m\}\). Fix \(T=L^4\). The contribution from \(m>T\) is \(O(X/T)\), since the number of primes up to \(Y\) is at most \(Y\). For each remaining multiplier set \(Y=3X/(\varepsilon m^2)\); uniformly \(Y\ge X/(2L^8)\). The prime number theorem for the two applicable reduced classes modulo \(24\) gives
\[
\pi(Y;24,a_1)+\pi(Y;24,a_2)=\tfrac14\operatorname{Li}(Y)+O\bigl(Ye^{-c\sqrt{\log Y}}\bigr)
\]
for some constant \(c>0\), where the classes are \(\{5,23\}\) or \(\{7,13\}\). Therefore, up to \(O(X/L^4)+O(\sqrt X)\), \(R_2(X)\) equals
\[
\frac14\sum_{\varepsilon=1}^2\ \sum_{\substack{m\in\mathcal M_\varepsilon\\m\le T}}
 \operatorname{Li}\left(\frac{3X}{\varepsilon m^2}\right).
\]

**4. Two asymptotic coefficients.** Uniformly for \(m\le L^4\), with \(a=3/(\varepsilon m^2)\),
\[
\operatorname{Li}(aX)=aX\left[\frac1L+
\frac{1-\log a}{L^2}+
O\left(\frac{1+(\log a)^2}{L^3}\right)\right].
\]
The sums of \(m^{-2}(1+\log^2m)\) converge. Thus the total error is \(O(X/L^3)\), and one may extend the coefficient sums to all positive allowed multipliers.

Set \(S=\sum_{3\nmid m}m^{-2}=(1-3^{-2})\zeta(2)=4\pi^2/27\) and \(T_1=\sum_{3\nmid m}(\log m)/m^2\). The even-multiplier sums are \(S/4\) and \((S\log2+T_1)/4\). Consequently the first coefficient is
\[
\frac34\left(\frac S4+\frac S2\right)=\frac{\pi^2}{12}.
\]
For the second coefficient, let \(D\) denote its value and \(C=\pi^2/12\). Directly summing the \(1-\log a\) terms gives
\[
\frac DC=1-\log3+\frac43\log2+\frac{2T_1}{S}.
\]
Differentiating \((1-3^{-s})\zeta(s)\) at \(s=2\) shows
\[
\frac{T_1}{S}=-\frac{\zeta'(2)}{\zeta(2)}-\frac18\log3.
\]
Substitution gives the stated second coefficient. The previous estimates give the asserted \(O(X/L^3)\) remainder.

**5. Exact odd-residue count.** By the same published characterization, odd-indexed coefficients are odd exactly when \(3n-1=2m^2\). This produces a positive odd integer \(n=(2m^2+1)/3\) precisely when \(3\nmid m\). With \(m\le M\), there are exactly \(M-\lfloor M/3\rfloor\) choices. Its square-root order is negligible compared with the residue-two count, proving the final assertion.

## Verification

Running `python3 verify_unimodal.py` computes the generating function
\[
\sum_{j\ge0}q^{2j+1}\prod_{h=0}^{j-1}(1+q^{2h+1})^2
\]
modulo four up to weight \(5000\), then independently tests all positive odd indices in that range against the factorization characterization. It also counts the allowed prime/square representations for heights \(10000\), \(100000\) and \(1000000\) with an exact prime sieve. The finite counts are \(1138\), \(8785\) and \(70499\), respectively. An exponent-five case occurs at weight \(4167\), where the coefficient is \(2\pmod4\). These finite checks do not prove the asymptotic; the preceding prime-distribution argument does.

## Relationship to prior work

Banerjee and Ghosh Dastidar (2026), Theorem 1.5, establishes the exact arithmetic conditions for odd-indexed residues modulo four, which are used as an explicit premise. Bringmann and Lovejoy establish the generating function and congruence families. Their work on coefficient-size asymptotics does not give the *index frequency* of residues. He and Liu study probabilistic shape and rank statistics of odd unimodal sequences rather than the arithmetic frequency of coefficient congruence classes. The two-term coefficient-frequency law and the explicit zeta-derivative constant are not stated in the material located for these works. A prior general asymptotic theorem specialized to the same prime-square family might imply the result; historical priority is not independently certified.

## Limitations

This is a conditional *derivation from a published pointwise congruence theorem*, not an independent reconstruction of its proof. It applies to positive odd indices; no assertion is made about even indices or the split of odd coefficients between residues one and three modulo four. The counting asymptotic uses the classical prime number theorem in arithmetic progressions and is not an elementary finite certificate. Computational checks are illustrative, not proof of the infinite asymptotic. A potentially relevant 2026 source could only be inspected in accessible introductory and theorem sections; later sections were not exhaustively read, leaving a bounded historical-priority risk. No independent mathematical audit has been performed.

## References

1. K. Banerjee and M. Ghosh Dastidar, *Conguences for Odd Unimodal Sequences and a Problem of Bringmann And Lovejoy*, arXiv:2610.20135v1, first posted 2026-10-14. See Theorem 1.5 and equation (1.2). https://arxiv.org/abs/2610.20135
2. K. Bringmann and J. Lovejoy, *Odd Unimodal Sequences*, preprint, 2025. https://lovejoy.perso.math.cnrs.fr/OddUnimodal_Revised.pdf
3. B. He and G. Liu, *Asymptotic Statistics of Odd Unimodal Sequences: Rank Distributions and Probabilistic Structures*, arXiv:2605.06459v1, 2026-05-07. https://arxiv.org/abs/2605.06459
4. Prime number theorem for arithmetic progressions to a fixed modulus, in the classical de la Vallée Poussin error form.
