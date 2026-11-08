# Exact prime-square cubic-chirp spectrogram fibers above one residue class

## Finding
Let \(p\ge5\) be prime, \(N=p^2\), \(\omega=\exp(2\pi i/N)\), and \(g(j)=N^{-1/2}\omega^{j^3}\) for \(j\in\mathbb Z_N\). For a complex signal \(x\in\mathbb C^{\mathbb Z_N}\), its *complete cubic-chirp spectrogram* is
\[
I_x(a,b)=\left|\sum_{j\in\mathbb Z_N}x(j)\overline{g(j-a)}\omega^{-bj}\right|^2,\qquad a,b\in\mathbb Z_N.
\]
The projective fiber is \(\{y:I_y=I_x\}/\mathbb T\), where \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) acts by global multiplication. For each residue \(r\in\mathbb Z_p\), put \(x_r(m)=x(r+pm)\) for \(m\in\mathbb Z_p\), let \(R(x)=\{r:x_r\not\equiv0\}\), and define
\[
E_r=\sum_{m\in\mathbb Z_p}|x_r(m)|^2,\qquad
C_r(h)=\sum_{m\in\mathbb Z_p}x_r(m)\overline{x_r(m-h)}.
\]
**Theorem.** Every signal with \(|R(x)|\ge3\) is uniquely determined up to global phase by \(I_x\). If \(R(x)=\{r,s\}\) consists of exactly two classes, its projective fiber has **two** elements precisely when \(E_r\ne E_s\) and \(C_r(h)=C_s(h)=0\) for every \(h\in\mathbb Z_p\setminus\{0\}\); in every other two-class case the fiber has **one** element. In the exceptional case the only nontrivial partner, modulo global phase, is
\[
y_r=\sqrt{E_s/E_r}\,x_r,\qquad y_s=\sqrt{E_r/E_s}\,x_s,\qquad y_t=0\ \ (t\notin\{r,s\}).\]
Thus the spectrogram map is injective projectively on the dense open set of signals whose supports meet at least three residue classes, despite its window having many vanishing ambiguity coefficients. The theorem makes no classification claim when \(|R(x)|\le1\).

## Assumptions and scope
All indices and frequency variables are taken modulo \(N\); the ordering \(r+pm\) is the canonical residue decomposition. Fourier sums are **unnormalized** unless a factor is explicitly displayed; the window \(g\) has unit Euclidean norm. The theorem holds for every prime \(p\ge5\) and **all complex signals**, with no nonvanishing assumption on coordinates within a populated residue class. The phrase *perfect periodic autocorrelation* means \(C_r(h)=0\) at every nonzero lag, equivalently the one-dimensional Fourier transform of \(x_r\) having constant modulus; it imposes no constant-amplitude condition on the time coefficients.

## Proof
**1. Exact ambiguity support.** Let
\[
A_g(u,v)=\sum_{j\in\mathbb Z_N}\overline{g(j)}g(j-u)\omega^{vj}.
\]
Expansion of the cubic phase gives
\[
A_g(u,v)=N^{-1}\omega^{-u^3}\sum_{j\in\mathbb Z_N}\omega^{-3u j^2+(3u^2+v)j}.
\]
Because \(p\ge5\), elementary quadratic Gauss-sum evaluation over \(\mathbb Z_{p^2}\) yields the **complete**, rather than merely one-way, support and magnitude rule
\[
|A_g(u,v)|=\begin{cases}
1,&u=v=0,\\
1/p,&p\nmid u,\\
1/\sqrt p,&u=ph\ne0\ \text{and}\ p\mid v,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(p\nmid u\), the quadratic coefficient is a unit, so the standard odd-prime-power complete quadratic Gauss sum has modulus \(p\), hence normalized modulus \(1/p\). For \(u=ph\ne0\), the coefficient is \(-3ph\) with \(p\nmid h\); writing \(j=t+pm\) first sums the \(p\) values of \(m\), giving zero unless \(p\mid v\), and otherwise the normalized classical nondegenerate Gauss sum over \(\mathbb F_p\) has modulus \(1/\sqrt p\). At \(u=0\), Fourier orthogonality for the flat window gives \(A_g(0,v)=\mathbf1_{v=0}\). This support contains all \((u,v)\) with \(p\nmid u\), all \((ph,pt)\) for \(h\ne0\) and arbitrary \(t\), and the origin, totaling \(p^4-p^3+p^2-p+1\) points.

**2. Which signal correlations are measured.** Define
\[
\chi_x(u,v)=\sum_{j\in\mathbb Z_N}x(j)\overline{x(j-u)}\omega^{-vj}.
\]
A direct expansion followed by both finite Fourier orthogonality identities shows, with no unspecified proportionality,
\[
\sum_{a,b\in\mathbb Z_N}I_x(a,b)\omega^{bu-va}
=N\,\chi_x(u,v)\,A_g(u,v).
\]
Consequently two signals have the same spectrogram **if and only if** their \(\chi\)-transforms coincide at every nonzero location of \(A_g\). For \(p\nmid u\) all \(v\) are available; inverse Fourier transformation in \(v\) recovers separately **every** cross-class product \(x(j)\overline{x(j-u)}\), namely every \(x(j)\overline{x(k)}\) with \(j\not\equiv k\pmod p\). For \(u=ph\ne0\), all \(v=pt\) are available; here
\[
\chi_x(ph,pt)=\sum_{r\in\mathbb Z_p}e^{-2\pi itr/p}\,C_r(h),
\]
so a length-\(p\) inverse Fourier transform recovers **each** \(C_r(h)\) for every nonzero \(h\). The final available value \(\chi_x(0,0)\) is exactly \(\sum_r E_r\). These cross-class products, classwise nonzero-lag autocorrelations, and total energy are thus necessary **and sufficient** data for spectrogram equality.

**3. Rank-one cross-block rigidity.** Suppose \(I_y=I_x\) and \(|R(x)|\ge2\). The recovered cross-class products imply \(R(y)=R(x)\) and, for each populated class, a unique scalar \(\alpha_r\in\mathbb C\setminus\{0\}\) with \(y_r=\alpha_r x_r\). Indeed, choose one nonzero coordinate from each of two different classes: its nonzero cross-product forces the corresponding two \(y\)-entries to be nonzero; every other coordinate is determined, including its zeros, by its product with an entry in another populated class. Equality of the resulting outer products gives
\[
\alpha_r\overline{\alpha_s}=1\qquad(r\ne s\text{ in }R(x)).
\]
If at least three classes occur, three pairwise equations force all scalars to coincide with a common element of \(\mathbb T\). This proves uniqueness for \(|R(x)|\ge3\).

**4. Exact two-class fibers.** When \(R(x)=\{r,s\}\), the pairwise equation says that, after removal of a common unit phase, every partner has precisely the form \(y_r=\lambda x_r\), \(y_s=\lambda^{-1}x_s\) with \(\lambda>0\). Agreement of recovered nonzero-lag correlations says
\[
(\lambda^2-1)C_r(h)=0,\qquad(\lambda^{-2}-1)C_s(h)=0\quad(h\ne0).
\]
Hence a nontrivial partner requires perfect periodic autocorrelations in both classes. Under that necessary condition, the only remaining equality is that of total energies:
\[
\lambda^2E_r+\lambda^{-2}E_s=E_r+E_s.
\]
Because \(E_r,E_s>0\), multiplication by \(\lambda^2\) factors it as \((\lambda^2-1)(E_r\lambda^2-E_s)=0\). Thus the only solutions are \(\lambda=1\) and \(\lambda=\sqrt{E_s/E_r}\), the latter distinct exactly when \(E_r\ne E_s\). Conversely both candidate solutions preserve every measured datum from step 2, proving the asserted completeness, not just necessity.

**5. Attaining the exceptional branch.** For any two distinct residues \(r,s\), put
\[
x_r(m)=2e^{2\pi i m^2/p},\qquad x_s(m)=3e^{2\pi i(2m^2+m)/p}.
\]
The standard quadratic-character orthogonality of nontrivial cyclic shifts gives \(C_r(h)=C_s(h)=0\) for all nonzero \(h\). Both blocks are nonzero at *every* internal coordinate; their energies are \(4p\) and \(9p\), so the exceptional partner rescales the first by \(3/2\) and the second by \(2/3\). The theorem therefore exhibits nontrivial phaseless ambiguity for densely populated two-class supports, not merely isolated two-atom examples.

## Verification
A standalone `CHECK.py` evaluates the unnormalized quadratic correlation numerically for primes \(p=5,7,11\) after normalizing the cubic chirp, testing every pair \((u,v)\) and the predicted three nonzero amplitude levels. It independently evaluates the entire raw spectrogram of explicit perfect-correlation two-class partners, unequal-amplitude two-spike partners, and nonexceptional control pairs; all checks pass. The computational checks establish finite examples only. The theorem for all primes follows from the exact Gauss-sum, double Fourier-identity, and rank-one proof above.

## Relationship to prior work
Dongwei Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (first posted September 9, 2026), Proposition 5.1, proves a one-sided divisibility **vanishing** condition for the cubic chirp modulo \(p^a\), including \(p^2\). This is used as motivation, not claimed as new; that proposition neither identifies the full spectrogram fibers nor supplies the three-residue recovery theorem or the exact exceptional two-residue interchange.

David Bartusel, *Injectivity Conditions for STFT Phase Retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)* (first posted June 2022; published 2023), Theorem 2.2.3 assumes full ambiguity-frequency support for each allowed translation, which fails for the flat cubic chirp at zero translation and nonzero modulation. Its specialized cyclic classification theorems concern short-support windows and separated signals; they do not give the present fiber statement. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval* (May 29, 2026), gives sufficient conditions for certain **shapes** of ambiguity support, rather than a theorem that every window with an arbitrary prescribed number of nonzeros is globally injective. The present cubic window is not globally injective, as the explicit exceptional partners demonstrate. Standard CAZAC constructions supply examples of perfect cyclic autocorrelation; the perfect-sequence concept itself is not new.

## Limitations
The result concerns complete, noiseless intensities with all \(N^2\) time-frequency shifts; it does not give a stability constant, an algorithm robust to noise or erasures, or a classification of fibers for signals occupying zero or one residue class. The originality comparison is evidence-based, not proof of global absence of an earlier equivalent statement. No independent external mathematical validation has been performed.

## References
1. Dongwei Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1, 2026-09-09, Proposition 5.1. https://arxiv.org/abs/2609.09614
2. David Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Zd and Rd*, arXiv:2206.06729 (2022), *J. Fourier Anal. Appl.* 29 (2023), 53, Theorems 2.2.3 and 4.2.6–4.2.8. https://doi.org/10.1007/s00041-023-10026-2
3. David Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, 2026-05-29. https://arxiv.org/abs/2605.31507
4. D. C. Chu, *Polyphase codes with good periodic correlation properties*, *IEEE Trans. Information Theory* 18 (1972), 531–532. https://doi.org/10.1109/TIT.1972.1054840
