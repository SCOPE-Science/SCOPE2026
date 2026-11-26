# Arithmetic rank and translated-intersection spectrum of cubic-graph Gabor tomography

## Finding
For every prime \(p\ge5\), let \(G=\mathbb F_p^2\), let \(C=\{(t,t^3):t\in\mathbb F_p\}\), and let \(g=p^{-1/2}\mathbf1_C\in\ell^2(G)\). For all translations \(u\in G\) and modulations \(v\in G\), set \(W_{u,v}=M_vT_u\), with \((T_uf)(x)=f(x-u)\) and \((M_vf)(x)=\exp(2\pi i\,v\cdot x/p)f(x)\). Define the **complex-linear operator measurement map**
\[
\mathcal L_g(H)_{u,v}=\operatorname{tr}\bigl(H\,W_{u,v}|g\rangle\langle g|W_{u,v}^*\bigr),\qquad H\in\mathbb C^{p^2\times p^2}.
\]
Then, writing \(\delta_p=1\) if \(p\equiv2\pmod3\) and \(\delta_p=0\) otherwise,
\[
\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_g=\frac{p^2(p^2+1)}2-(p-1)(1+\delta_p).}
\]
Its complex nullity is \(p^4-\operatorname{rank}_{\mathbb C}\mathcal L_g\). In particular, the cubic-graph Gabor measurement is **never linearly informationally complete**, and the precise lower-order defect has a divisibility-by-three transition.

**Complete kernel.** Put \(\zeta=\exp(2\pi i/p)\). The matrix kernel is the complex span of precisely the Weyl matrices \(W_{(h,k),(a,b)}\) indexed by one of the following disjoint conditions:

1. \((h,k)\ne(0,0)\) and either \(h=0\), or \(h\ne0\) and \(s=(k-h^3/4)/(3h)\) is a quadratic nonsquare in \(\mathbb F_p\).
2. \((h,k)=(0,0)\), \(a\ne0\), and \(b=0\).
3. \((h,k)=(0,0)\), \(a=0\), \(b\ne0\), and \(p\equiv2\pmod3\).

There are exactly \((p^2-1)/2\) empty translated intersections, \(p-1\) one-point intersections, and \((p-1)^2/2\) two-point intersections. These counts exclude the identity translation, whose intersection is \(C\).

**Explicit singular-value bands.** All singular values of \(\mathcal L_g\) are \(p|\langle g,W_{u,v}g\rangle|\). The nonidentity, nonempty translations contribute the following multiset of singular values, counting all modulation frequencies:
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity from nonidentity translations}\\\hline
1&p^2(p-1)\\
2& p(p-1)^2/2\\
2\cos(\pi j/p),\quad 1\le j\le(p-1)/2&p(p-1)^2\quad\text{for each }j.
\end{array}
\]
The empty translations contribute \(p^2(p^2-1)/2\) zero singular values. The identity translation contributes the remaining \(p^2\) singular values \(\bigl|\sum_{t\in\mathbb F_p}\zeta^{at+bt^3}\bigr|\); their exact zero positions are precisely the last two kernel classes above. No claim is made that these cubic Gauss-sum magnitudes have only finitely many distinct values independently of \(p\).

## Assumptions and scope
The ambient group is the **elementary abelian plane** \(\mathbb F_p^2\), not the cyclic ring \(\mathbb Z/p^2\mathbb Z\). The vector \(g\) has norm one under counting-measure \(\ell^2\) normalization. All measurements, matrices, and ranks are complex; \(\mathcal L_g\) acts on the full complex matrix space rather than only on Hermitian operators or pure states. All modular inverses in the formulas exist because \(p\ge5\). The fourth-moment/Fourier-extension norm of \(C\) is a different object and is not evaluated here.

## Proof
**1. Exact translated-intersection classification.** For a translation \(u=(h,k)\), the coordinates of the common support \(C\cap(C+u)\) correspond bijectively to parameters \(t\in\mathbb F_p\) satisfying \(t^3-(t-h)^3=k\). If \(h=0\), this forces \(k=0\), so every nonzero vertical translation has empty intersection. When \(h\ne0\), completing the square gives
\[
3h\left(t-\frac h2\right)^2+\frac{h^3}{4}=k
\quad\Longleftrightarrow\quad
\left(t-\frac h2\right)^2=s:=\frac{k-h^3/4}{3h}.
\]
Thus the intersection has respectively zero, one, or two points according as \(s\) is a nonsquare, zero, or a nonzero square. For each of the \(p-1\) nonzero values of \(h\), \(k\mapsto s\) is bijective. Therefore the nonidentity translation populations are as claimed.

**2. Ambiguity zeros on nonidentity translations.** The ambiguity function for the normalized window is
\[
A_g(u,v)=\langle g,W_{u,v}g\rangle=\frac1p\sum_{x\in C\cap(C+u)}\zeta^{v\cdot x}.
\]
It is zero for an empty intersection. A one-point intersection gives a single nonzero root of unity. A two-point intersection gives the sum of two \(p\)-th roots of unity, which cannot cancel because \(p\) is odd: otherwise their quotient would be \(-1\), of order two. Hence every modulation survives on every nonempty nonidentity translation. The number of such Weyl coordinates is exactly \(p^2(p^2-1)/2\).

**3. Identity-translation zeros and cubic permutation rigidity.** At \(u=0\),
\[
pA_g(0,(a,b))=\sum_{t\in\mathbb F_p}\zeta^{at+bt^3}.
\]
This sum has exactly \(p\) terms. Because \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) is irreducible over \(\mathbb Q\), an integer-coefficient sum of \(p\)-th roots vanishes if and only if each of the \(p\) residues occurs equally often among the exponents. As there are exactly \(p\) exponents, this occurs precisely when \(t\mapsto at+bt^3\) is a permutation of \(\mathbb F_p\).

When \(b=0\), this happens exactly for \(a\ne0\). When \(a=0\) and \(b\ne0\), this happens exactly when \(\gcd(3,p-1)=1\), equivalently \(p\equiv2\pmod3\). Neither coefficient zero yields the nonzero constant-map exception.

It remains to rule out \(a,b\ne0\). Set \(c=a/b\ne0\). Distinct parameters \(t,u\) have equal values under \(t\mapsto t^3+ct\) exactly if
\[
t^2+tu+u^2=-c.
\]
The quadratic form \(Q(t,u)=t^2+tu+u^2\) is nondegenerate because \(p\ne2,3\), and its discriminant is \(-3\). Every nonzero level has \(p-\chi(-3)\ge p-1\ge4\) ordered solutions: indeed, after replacing \(t\) by \(t+u/2\), the equation is a nondegenerate norm equation, and the standard quadratic-character identity \(\sum_z\chi(z^2+d)=-1\) for \(d\ne0\) gives this count. At most two solutions have \(t=u\), since then \(3t^2=-c\). Thus an off-diagonal collision exists, ruling out permutation. This proves that the only vanishing identity-translation frequencies are the two indicated coordinate axes, of combined size \((p-1)(1+\delta_p)\).

**4. Weyl diagonalization and rank.** Let \(d=|G|=p^2\). The \(d^2\) operators \(W_{u,v}\) form an orthogonal basis of \(\mathbb C^{d\times d}\), with Hilbert--Schmidt norm \(\sqrt d\). Conjugation of a Weyl operator by another Weyl operator multiplies it by one of the distinct characters of the phase-space group \(G\times G\). Consequently, evaluating \(W_{u,v}/\sqrt d\) under \(\mathcal L_g\) yields a phase-space character of constant modulus \(|A_g(u,v)|/\sqrt d\); the columns for different \((u,v)\) are orthogonal. Their squared norms are \(d|A_g(u,v)|^2\). Thus the singular values are \(\sqrt d|A_g(u,v)|=p|A_g(u,v)|\), and the kernel is exactly the Weyl span of the zeros found in Steps 2--3. Counting gives
\[
\operatorname{rank}\mathcal L_g=\frac{p^2(p^2-1)}2+\left[p^2-(p-1)(1+\delta_p)\right],
\]
which simplifies to the displayed result.

**5. Translation-resolved singular-value bands.** For a one-point intersection \(A_g=p^{-1}\zeta^m\), hence the associated singular values are all \(1\). For a two-point intersection at distinct \(x_1,x_2\), the singular value is
\[
|\zeta^{v\cdot x_1}+\zeta^{v\cdot x_2}|=2\left|\cos\left(\frac{\pi(v\cdot(x_1-x_2))}{p}\right)\right|.
\]
The linear functional \(v\mapsto v\cdot(x_1-x_2)\) is nonzero, so each residue occurs exactly \(p\) times among the \(p^2\) modulations. One residue yields value \(2\); each unordered pair \(\{j,p-j\}\) yields \(2\cos(\pi j/p)\) with total multiplicity \(2p\). Summing over the \((p-1)^2/2\) two-point translations gives the claimed bands. The identity contribution is the formula in Step 3, which need not simplify further to establish the rank or the translation-band claims.

## Verification
Run `python3 cubic_gabor_verify.py` (Python 3 standard library only) in the directory containing this document and the checker. The checker enumerates every curve intersection and tests all nonempty nonidentity one- and two-point ambiguities for exact nonvanishing via coefficients of the cyclotomic polynomial; it tests every identity-translation phase for exact vanishing and verifies the rank formula. For empty intersections, all modulation coefficients are zero by the empty-sum identity without enumerating each modulation. It checks the entire translation stratification for each \(p\in\{5,7,11,13,17,19,23,29,31,37\}\), including the two-point band multiplicities. It reports `ALL EXACT CHECKS PASSED`; the recorded stdout is provided as `cubic_gabor_verify_output.txt`. These finite tests are checks of the proof, not a replacement for the all-prime argument.

## Relationship to prior work
Goldberger, Kang and Okoudjou [1] establish the general finite-Gabor POVM framework and its Gram-eigenvalue characterization. Bojarovska and Flinth [2] develop the ambiguity-function viewpoint and operator-spreading diagonalization in Gabor phase retrieval. Those general results explain why an explicit ambiguity-zero classification is the natural target, but they do not give the arithmetic rank for the indicator of this plane cubic graph. The familiar cubic-permutation-polynomial criterion and finite-field quadratic-form counts are preexisting mathematical inputs, not claimed as novel lemmas. Related work on Fourier extension for the cubic graph studies a fourth-moment operator rather than the Gabor operator lifting studied here; likewise, orthogonal exponential bases for cubic graphs over prime-square cyclic rings use a different ambient group and a different matrix problem. The specific rank, full Weyl kernel, and nonidentity spectral bands are the added conclusions.

## Limitations
Only odd prime characteristics at least five are treated, not general prime powers, characteristic two or three, arbitrary plane curves, weighted windows, or cyclic groups of order \(p^2\). Failure of injectivity on all complex operators does **not** by itself prove a failure of nonlinear phase retrieval for pure signals. Exact arithmetic singular values for zero translation remain written as cubic exponential sums, so there is no claim to a closed classification of their nonzero magnitudes. Although the cited sources and neighboring results were compared against these statements, an equivalent unindexed special-case calculation remains a bibliographic risk; independent mathematical auditing has not been performed.

## References
1. A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (first publicly posted 2021-06-02), Sections 1--3; https://arxiv.org/abs/2106.01509.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (first publicly posted 2015-03-19), Sections 1--2; https://arxiv.org/abs/1503.05800.
3. Classical irreducibility of prime cyclotomic polynomials, quadratic character sums, and elementary cubic permutation-polynomial tests, used in the specific forms proved above.
