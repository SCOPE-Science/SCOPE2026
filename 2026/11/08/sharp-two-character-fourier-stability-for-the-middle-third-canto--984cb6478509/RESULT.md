# Sharp two-character Fourier stability for the middle-third Cantor measure

## Finding

Let \(\mu\) be the fair middle-third Cantor probability measure, the distribution of
\[
X=\sum_{j=1}^{\infty}\frac{2\varepsilon_j}{3^j},\qquad
\mathbb P(\varepsilon_j=0)=\mathbb P(\varepsilon_j=1)=\tfrac12
\]
with independent digits. Define the positive constant
\[
C_3=\prod_{j=1}^{\infty}\left|\cos\!\left(\frac{2\pi}{3^j}\right)\right|
=0.371437356708765\ldots.
\]
For every nonzero integer \(n\),
\[
\boxed{|\widehat\mu(n)|\le C_3,\quad
|\widehat\mu(n)|=C_3\iff n=\pm3^a\text{ for an integer }a\ge0.}
\]
Here \(\widehat\mu(n)=\int e^{-2\pi inx}\,d\mu(x)\). Thus, for every pair of distinct integers \(u,v\), the Gram matrix of \(e^{2\pi iux}\) and \(e^{2\pi ivx}\) in \(L^2(\mu)\) has sharp, simultaneous universal spectral bounds
\[
\boxed{1-C_3\le\lambda_{\min}\le\lambda_{\max}\le1+C_3.}
\]
Both extreme bounds are attained simultaneously exactly when \(|u-v|\) is a nonnegative integral power of three. Equivalently, the largest squared spectral condition number among all such two-character systems is exactly \((1+C_3)/(1-C_3)=2.181862653382873\ldots\).

## Assumptions and scope

The measure has independent balanced digits \(0,2\) in base three; frequencies are **integers**; each exponential is unweighted and has unit \(L^2(\mu)\) norm. This is a two-dimensional Riesz-sequence result, not a Fourier frame of the entire infinite-dimensional space. The normalization of \(\widehat\mu\) is explicitly specified above. The theorem covers every pair of distinct integers without a bound on frequency separation.

## Proof

**1. Self-similar Fourier product.** Independence of the digits gives the uniformly convergent-on-compact-sets representation
\[
|\widehat\mu(t)|=\prod_{j=1}^{\infty}
\left|\cos\!\left(\frac{2\pi t}{3^j}\right)\right|,
\qquad t\in\mathbb R.
\]
For integers \(n\), set \(P_k(n)=\prod_{j=1}^{k}|\cos(2\pi n/3^j)|\). Then \(|\widehat\mu(n)|\le P_k(n)\), and \(|\widehat\mu(3n)|=|\widehat\mu(n)|\). It therefore suffices to consider integers not divisible by three.

**2. A strict rational screening threshold.** We claim \(C_3>1/3\). The first factor of \(C_3\) is \(1/2\); the second is \(\cos(2\pi/9)>3/4\), by \(\cos t\ge1-t^2/2\) and \(\pi^2<10\). For \(j\ge3\), \(0<\cos(2\pi/3^j)\le1\), so \(\prod(1-a_j)\ge1-\sum a_j\) with \(1-\cos t\le t^2/2\) yields
\[
\prod_{j=3}^{\infty}\cos\!\left(\frac{2\pi}{3^j}\right)
\ge 1-\sum_{j=3}^{\infty}\frac{2\pi^2}{3^{2j}}
=1-\frac{\pi^2}{324}>\frac{157}{162}.
\]
Consequently \(C_3>\frac12\cdot\frac34\cdot\frac{157}{162}>\frac13\).

**3. Four surviving ternary residue classes.** For each integer \(k\ge2\), put \(M=3^k\) and
\[
E_k=\left\{1,\ M-1,\ \frac{M-1}{2},\ \frac{M+1}{2}\right\}\subset\{0,\ldots,M-1\}.
\]
We prove by induction that, for every integer \(n\) not divisible by three,
\[
\boxed{P_k(n)>C_3\quad\Longrightarrow\quad n\bmod3^k\in E_k.}\tag{*}
\]
For \(k=2\), the six residues prime to three modulo nine split into the pairs \(\pm1,\pm2,\pm4\). At \(\pm2\), the first two factors have product \(\tfrac12\cos(4\pi/9)<1/4<C_3\); the other four residues are precisely \(E_2=\{1,4,5,8\}\). This establishes the base.

Assume (*) at depth \(k\), and suppose \(P_{k+1}(n)>C_3\). Its prefix \(P_k(n)\) exceeds \(C_3\), so its residue modulo \(M\) is one of four classes in \(E_k\). Each class has exactly three descendants modulo \(3M\), with residues \(r\), \(r+M\), \(r+2M\). For \(r=1\) or \(M-1\), the unique descendant in \(E_{k+1}\) is \(1\) or \(3M-1\), respectively. Each of the other two descendants has final cosine factor of modulus at most
\[
\frac12+\frac{2\pi}{3M}\le\frac12+\frac{2\pi}{27}<\frac34.
\]
The prefix product in those classes is at most \(P_2(1)=\tfrac12\cos(2\pi/9)<\sqrt3/4<7/16\), so the full product is less than \(21/64<1/3<C_3\).

For \(r=(M-1)/2\) or \((M+1)/2\), the unique descendant in \(E_{k+1}\) is \(r+M=(3M\mp1)/2\); the other two descendants have final cosine factor at most
\[
\frac12+\frac{\pi}{3M}\le\frac12+\frac{\pi}{27}<\frac23.
\]
The prefix product in those classes is at most \(P_2(4)=\tfrac12\cos(\pi/9)<1/2\), making their full products strictly below \(1/3<C_3\). The angle bounds follow from \(|\cos x-\cos y|\le|x-y|\) near the angles \(2\pi/3\), \(4\pi/3\), \(\pi/3\), or \(5\pi/3\). Thus every descendant outside \(E_{k+1}\) is excluded, completing the induction.

**4. Infinite conclusion and all equality cases.** Fix an integer \(n\) not divisible by three with \(n\ne\pm1\). For sufficiently large \(k\), the residue \(n\bmod3^k\) cannot belong to \(E_k\): the two middle residues grow like \(3^k/2\), while the other two require \(n=1\) or \(n=-1\). The contrapositive of (*) gives \(P_k(n)\le C_3\), hence \(|\widehat\mu(n)|\le C_3\). In fact the inequality is strict: a subsequent factor is strictly less than one for every nonzero integer \(n\). Meanwhile, \(|\widehat\mu(\pm1)|=C_3\) by definition, and the scaling identity proves equality at \(n=\pm3^a\). Removing factors of three from every other nonzero integer proves that there are no further equality cases.

**5. Riesz bounds.** The Gram matrix for two normalized characters at frequencies \(u,v\) has diagonal entries one and off-diagonal entry \(\widehat\mu(u-v)\) or its conjugate. Its eigenvalues are exactly \(1\pm|\widehat\mu(u-v)|\), so the sharp bounds, equality classification, and condition-number statement follow.

## Verification

The standalone executable file `CHECK.py` evaluates Fourier products directly, checks finite-level residue screening through depth fifteen, checks every positive integer frequency up to 15,000, and separately computes Gram entries by enumerating finite Cantor digit configurations. It includes numerical checks of the rational screening margins. The full integer-frequency conclusion is proved by the induction above; finite tests are not used as a substitute for the infinite quantifiers. Execute with `python3 CHECK.py` (Python standard library only).

## Relationship to prior work

The 2026 work of de Dios Pont, Liehr, and Taylor proves that odd-base Cantor measures admit no Fourier frame for the entire \(L^2\) space. Its Theorem 1.1 and self-similar Fourier identity address global frame existence, not the sharp worst-conditioned two-character subspace or its complete equality classification. Zuberman's 2026 work studies maximal orthogonal systems for Cantor measures, a distinct question from the present quantitative uniform nonorthogonal bound. The classical Cantor Fourier product and the fact that integer powers of three retain the same coefficient are background ingredients, not claimed as new. No inspected source established that these are the **largest** nonzero integer Fourier coefficients.

## Limitations

This is an exact statement for the fair base-three law and **integer** frequencies only. It does not establish a uniform Riesz bound for arbitrary real frequency pairs, for three or more exponentials, for uneven digit weights, or for all odd bases. No independent external priority review has been performed. Older harmonic-analysis literature could contain an equivalent coefficient-maximization result under different terminology.

## References

1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, arXiv:2607.08656, first posted 2026-07-09; especially Theorem 1.1, Lemma 3.1 and Sections 3–4.
2. L. Zuberman, *On the spectra of Cantor measures*, arXiv:2605.18471, first posted 2026-05-18.
3. P. E. T. Jorgensen and S. Pedersen, classical spectral Cantor-measure constructions, cited in reference 1, Section 1.
