# Sharp Taylor-jet cusp widths for zero-fixing Hardy composition operators

## Finding
Let \(\varphi:\mathbb D\to\mathbb D\) be holomorphic, with \(\varphi(0)=0\), and let \(C_\varphi\) act on the classical Hardy Hilbert space \(H^2\). Write
\[
\mathcal B_\varphi=\left\{b_\varphi(w)=\frac{1-|w|^2}{1-\overline w\varphi(w)}:w\in\mathbb D\right\}.
\]
Suppose \(a=\varphi'(0)\in(-1,1)\) is real, \(\varphi\) is nonlinear, and the first nonlinear Taylor coefficient occurs at order \(m\ge2\):
\[
\varphi(w)=aw+cw^m+O(w^{m+1}),\qquad c\ne0.
\]
For sufficiently small \(\varepsilon>0\), the vertical section \(\mathcal B_\varphi\cap\{z:\Re z=1-\varepsilon\}\) is nonempty and compact. Let \(U(\varepsilon)\) and \(L(\varepsilon)\) be its maximum and minimum imaginary parts. Then the **sharp two-sided cusp law** is
\[
\lim_{\varepsilon\downarrow0}\frac{U(\varepsilon)}{\varepsilon^{(m+1)/2}}
=\frac{|c|}{(1-a)^{(m+1)/2}},\qquad
\lim_{\varepsilon\downarrow0}\frac{L(\varepsilon)}{\varepsilon^{(m+1)/2}}
=-\frac{|c|}{(1-a)^{(m+1)/2}}.
\]
Consequently, the section width is asymptotic to
\[
2|c|(1-a)^{-(m+1)/2}\varepsilon^{(m+1)/2}.
\]
Thus the local shape of the Berezin range recovers the first nonlinear **order** \(m\) and the normalized **magnitude** \(|c|/(1-a)^{(m+1)/2}\), from the set alone.


## Assumptions and scope
The disk is \(\mathbb D=\{w\in\mathbb C:|w|<1\}\). The Hardy space uses the Szegő reproducing kernel \(K_w(z)=(1-\overline w z)^{-1}\), and the Berezin transform is computed using its unit normalization. No boundary regularity of \(\varphi\) is assumed. The sharp width theorem assumes a *real interior* multiplier \(-1<a<1\), a finite first nonlinear order \(m\ge2\), and \(c\ne0\). It does not cover symbols with a nonreal derivative or purely linear symbols; those do have the qualitative classification but not the stated transverse-width normalization. The coefficient \(c\) may have any complex phase.

## Proof
**1. The reproducing-kernel formula and isolation of the tip.** For a disk selfmap fixing zero, write \(\varphi(w)=w h(w)\); Schwarz's lemma gives \(|h(w)|\le1\). Normalizing the Szegő kernels gives
\[
b_\varphi(w)=\frac{1-|w|^2}{1-|w|^2h(w)},\qquad b_\varphi(0)=1.
\]
If \(|a|<1\), Schwarz–Pick gives
\[
|h(w)|\le\frac{|w|+|a|}{1+|a||w|}.
\]
Hence, for every \(\delta>0\),
\[
\sup_{\delta\le|w|<1}|b_\varphi(w)|<1.
\]
Indeed the continuous strict bound \((1-r^2)/(1-r^2(r+|a|)/(1+|a|r))\) has limit \(2(1+|a|)/(3+|a|)<1\) as \(r\uparrow1\). Thus any values approaching \(1\) come from parameters \(w\to0\). This separation also makes sufficiently near-tip vertical sections compact in parameter space.

**2. Uniform expansion.** Put \(w=re^{i\theta}\). The Taylor hypothesis yields, uniformly in \(\theta\),
\[
b_\varphi(re^{i\theta})
=\frac{1-r^2}{1-ar^2}+c\,r^{m+1}e^{i(m-1)\theta}+O(r^{m+2}).
\]
The first displayed term is real since \(a\) is real. Therefore
\[
1-\Re b_\varphi(re^{i\theta})=(1-a)r^2+o(r^2),\qquad
\Im b_\varphi(re^{i\theta})=r^{m+1}\Im(ce^{i(m-1)\theta})+o(r^{m+1}),
\]
with error uniform over the circle. Every point of a section \(\Re b=1-\varepsilon\) must have \(r^2/\varepsilon\to1/(1-a)\) as \(\varepsilon\downarrow0\), uniformly in its angular parameter. Consequently every section value obeys the asserted upper and lower bounds asymptotically.

**3. Both bounds are attained asymptotically.** Choose angles \(\theta_+\) and \(\theta_-\) with \(ce^{i(m-1)\theta_+}=i|c|\) and \(ce^{i(m-1)\theta_-}=-i|c|\) (possible because \(m\ge2\)). For either fixed angle, the real quantity \(\Re b_\varphi(re^{i\theta})\) is continuous, equals \(1\) at \(r=0\), and is less than \(1-\varepsilon\) at a sufficiently small radius proportional to \(\sqrt{\varepsilon}\). The intermediate-value theorem supplies a radius satisfying the *exact* section equation. Its square is asymptotic to \(\varepsilon/(1-a)\); substitution in the uniform imaginary expansion yields the two sharp limits. Isolation from step 1 and compactness of a small closed parameter disk ensure the extrema exist, rather than being merely suprema.


## Verification
The included standalone Python checker `check_berezin_cusp.py` prints `BEREZIN_JET_CUSP_FINITE_OK 29037`. It checks exact radial formulas, small-section computations for polynomial symbols of orders two through four, and sample disk selfmapping inequalities. The proof of the limiting constants, set classification, and compactness is analytic; finite computations are consistency checks only. Reproduce with `python3 check_berezin_cusp.py` from the extracted package.

## Relationship to prior work
Bourdon, Le, and Thompson (2026, arXiv:2610.17634v1) study shape, corners, and convexity of Hardy composition Berezin ranges. Their full open HTML manuscript, notably Lemma 3.10, Theorem 3.11, Remark 3.12 and Theorem 4.1, proves an arbitrarily narrow **qualitative** cusp at \(1\) for zero-fixing symbols and classifies convexity for **linear** symbols. Cowen and Felder (2021/2022, arXiv:2109.12095) studied rotation and automorphism cases and raised broader convexity questions. The known linear-symbol convexity results are background, not part of the asserted new contribution. The claimed new content is the uniform **exact transverse-width asymptotic** at every finite nonlinear Taylor order, including its coefficient and inverse-jet interpretation; it is not stated by the cited qualitative cusp theorem or linear-symbol classification.

## Limitations
The shape invariant determines only the modulus of the leading nonlinear coefficient after normalization by \(a\), not its complex phase. The theorem is local near the Berezin value \(1\), not an expression for the entire global boundary. There is no claim of a quantitative law for nonreal \(a\), of stability under noisy measurements, or of independent publication-priority certification. Earlier equivalent theorems formulated in terms of fine Berezin geometry or Taylor jets cannot be excluded absolutely.

## References
1. P. Bourdon, T. Le, and D. Thompson, *Berezin ranges of composition operators on \(H^2\)*, arXiv:2610.17634v1 (first publicly posted 2026-10-13), https://arxiv.org/html/2610.17634v1, especially Sections 3.4 and 4.
2. C. C. Cowen and C. Felder, *Convexity of the Berezin range*, arXiv:2109.12095 (2021), later Linear Algebra and its Applications 647 (2022), Sections 4 and 5, https://arxiv.org/abs/2109.12095.
3. Classical Schwarz lemma, Schwarz–Pick lemma, the open-mapping theorem, and Szegő reproducing kernels (standard analytic ingredients).
