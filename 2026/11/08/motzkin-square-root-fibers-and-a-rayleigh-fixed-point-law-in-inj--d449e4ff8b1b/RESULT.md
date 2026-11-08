# Motzkin square-root fibers and a Rayleigh fixed-point law in injective partial Catalan monoids

## Finding
Let \(IC_n\) be the monoid of all injective, order-preserving, extensive partial self-maps of \([n]=\{1,\ldots,n\}\), including the empty map. For \(S=\{s_1<\cdots<s_k\}\subseteq[n]\), let \(e_S\) denote the partial identity on \(S\), and set \(s_0=0\), \(s_{k+1}=n+1\), \(g_i=s_{i+1}-s_i-1\) for \(0\le i\le k\). Let \(M_m\) be the \(m\)-th Motzkin number (\(M_0=1,M_1=1,M_2=2,\ldots\)). For every \(n\ge0\) and every such \(S\),
\[
\big|\{f\in IC_n:f^2=e_S\}\big|=\prod_{i=0}^{k}M_{g_i}.
\]
The factorization is canonical: each square root is a choice of one nonnegative Motzkin path in each fixed-point gap, with the fixed points themselves prescribed. In particular, the roots of the empty map number \(M_n\); two idempotents of equal rank can have different numbers of square roots.

Let \(Q_n=\{f\in IC_n:f^2\text{ is idempotent}\}\), and let \(K_n\) be the number of fixed points of a uniformly sampled member of \(Q_n\). The exact bivariate generating function is
\[
F(z,u)=\sum_{n\ge0}\sum_{f\in Q_n}z^n u^{|\operatorname{Fix}(f)|}
=\frac{M(z)}{1-uzM(z)},\quad
M(z)=\frac{1-z-\sqrt{1-2z-3z^2}}{2z^2},
\]
where \(M(0)=1\) by continuous extension. Moreover,
\[
\frac{K_n}{\sqrt n}\ \Longrightarrow\ \operatorname{Rayleigh}\big(\sqrt{2/3}\big),
\]
whose density on \(t>0\) is \(\frac{3t}{2}e^{-3t^2/4}\). The expected number of fixed points satisfies \(\mathbb E K_n\sim \sqrt{\pi n/3}\). If \(f\) is instead uniform in all of \(IC_n\), then
\[
\Pr(f^2\text{ is idempotent})\sim \frac{\sqrt3}{4}\,n\left(\frac34\right)^n.
\]

## Assumptions and scope
Composition is ordinary composition of partial maps: \(f^2(x)\) is defined exactly when \(x\in\operatorname{dom}f\) and \(f(x)\in\operatorname{dom}f\). Extensive means \(f(x)\ge x\) on the domain, and order-preserving means \(x<y\Rightarrow f(x)<f(y)\) for distinct domain points (injectivity makes the inequality strict). The statement is for every nonnegative integer \(n\), with \(IC_0\) containing only the empty map, and for arbitrary subsets \(S\subseteq[n]\). The asymptotics concern \(n\to\infty\); the Rayleigh statement conditions on membership in \(Q_n\).

## Proof
**Step 1: square-root reduction.** An idempotent in \(IC_n\) is a partial identity: whenever \(f^2=f\), injectivity implies every image point is fixed, and hence a domain point cannot move. Suppose now \(f^2=e_S\). For \(s\in S\), we have \(s\le f(s)\le f^2(s)=s\), so \(f(s)=s\). If \(x\notin S\) and \(f(x)=y\ne x\), then \(y>x\), and \(y\notin\operatorname{dom}f\), for otherwise \(f^2(x)\) would be defined outside \(S\). Conversely, any map fixing \(S\), moving every other domain point strictly forward, and having no moving image in its domain satisfies \(f^2=e_S\). No moving arrow can touch or cross a fixed point: touching contradicts injectivity, and crossing contradicts order preservation against \(f(s)=s\). Thus moving arrows split independently between the \(k+1\) gaps.

**Step 2: Motzkin bijection in a gap.** In a gap of length \(m\), assign letter \(U\) to the domain of a moving arrow, letter \(D\) to its image, and letter \(H\) to any unused position. Distinctness of moving domain and image makes this assignment unambiguous. Since the map is injective and order-preserving, the \(j\)-th \(U\) position is mapped to the \(j\)-th \(D\) position. The map is strictly extensive precisely when the \(j\)-th \(U\) precedes the \(j\)-th \(D\) for every \(j\), which is equivalent to the word having equally many \(U\) and \(D\) and every prefix having at least as many \(U\) as \(D\). These are exactly Motzkin paths; there are \(M_m\) of them. Inverting the encoding by ordered matching proves the product formula and its uniqueness.

**Step 3: generating function.** For fixed \(k\), summing over all \(k+1\) nonnegative gap lengths gives the series \(z^kM(z)^{k+1}\). Summing over \(k\ge0\) with a weight \(u^k\) gives \(F(z,u)=M(z)/(1-uzM(z))\). The fixed-point set in \(f^2=e_S\) agrees with the fixed-point set of \(f\) by Step 1. Motzkin first-step decomposition gives \(M(z)=1+zM(z)+z^2M(z)^2\), and therefore the displayed radical formula.

**Step 4: asymptotic count and moments.** Let \(\rho=1/3\), and write \(\varepsilon=1-3z\). The radical formula implies
\[
M(z)=3-3\sqrt3\,\sqrt\varepsilon+O(\varepsilon),\qquad
1-zM(z)=\sqrt3\,\sqrt\varepsilon+O(\varepsilon).
\]
The algebraic functions are analytic in a dented neighborhood of the unique dominant singularity \(\rho\). Consequently, standard square-root transfer gives
\[
|Q_n|=[z^n]F(z,1)\sim\sqrt{\frac3\pi}\,\frac{3^n}{\sqrt n}.
\]
For every fixed integer \(r\ge0\), differentiation in \(u\) gives
\[
\left.\partial_u^r F(z,u)\right|_{u=1}
=\frac{r!z^rM(z)^{r+1}}{(1-zM(z))^{r+1}}
\sim r!\,3^{(1-r)/2}\varepsilon^{-(r+1)/2}.
\]
Singularity transfer and division by \([z^n]F(z,1)\) yield
\[
\lim_{n\to\infty}\frac{\mathbb E[(K_n)_r]}{n^{r/2}}
=\frac{r!\,3^{-r/2}\sqrt\pi}{\Gamma((r+1)/2)}
=\left(\frac2{\sqrt3}\right)^r\Gamma\left(1+\frac r2\right).
\]
These are the ordinary moments of the stated Rayleigh law. Since factorial and ordinary moments have identical leading terms after normalization for each fixed \(r\), and the Rayleigh distribution is moment-determinate (its exponential-square tail satisfies Carleman's criterion), the method of moments proves weak convergence. Taking \(r=1\) proves the expectation asymptotic.

Finally, the known total cardinality \(|IC_n|=C_{n+1}=\binom{2n+2}{n+1}/(n+2)\) satisfies \(C_{n+1}\sim4^{n+1}/(\sqrt\pi n^{3/2})\). Dividing the asymptotic for \(|Q_n|\) by this count proves the rare-event estimate.

## Verification
The standalone Python program `verify.py` enumerates every order-preserving extensive partial injection on each chain of size \(0\) through \(9\) without using the Motzkin construction. It computes the actual partial square, tallies the fibers over every idempotent, compares each fiber with the independent Motzkin-path count, and checks the bivariate generating-function coefficients. It also checks \(\partial_u F(z,1)=zF(z,1)^2\) coefficientwise through degree \(29\). The replay reports `VERIFY_OK`; this finite computation is not used as proof of universal or asymptotic statements.

## Relationship to prior work
Gusev, Sapir, and Volkov (first publicly posted January 29, 2023) define these monoids and analyze their equational finite-basis behavior. Al-Kharousi, Umar, and Zubairu (first posted December 31, 2024) explicitly define quasi-idempotents by the condition that the square is idempotent and use shift-one quasi-idempotents to establish generation and rank properties. Their inspected relevant sections do not give the exact fibers of the square map or a conditioned fixed-point distribution. Laradji and Umar (2004, 2015) establish related enumerative results for order-decreasing partial transformation semigroups and subpermutations, with different enumerated quantities.

The **unweighted total sequence** \(1,2,5,13,35,96,\ldots\), its scalar Motzkin INVERT generating function, and its \(3^n/\sqrt n\) growth are **already recorded** in OEIS A005773 (with an index shift). They are not claimed as new independently. The asserted contribution is the power-fiber classification for every prescribed idempotent and the conditional fixed-point limit within this semigroup. General Motzkin-path and renewal asymptotics supply antecedent combinatorial techniques; the new claim is the identification of those techniques with these specific semigroup fibers and their conditional law.

## Limitations
No analogous statement is asserted for arbitrary partial transformations, noninjective maps, or other Catalan-type semigroups. The asymptotic statement is for the count of fixed points conditioned on the square being idempotent; it is not an unconditional Rayleigh law for uniform \(IC_n\). Finite enumeration alone does not establish a limit. Existing scalar sequences and their asymptotics must not be construed as novel numerical discoveries. Historical related material, notably Umar's 1992 thesis and Laradji–Umar's 2015 full paper, may require more comprehensive priority checking; these residual risks do not constitute an independent mathematical audit.

## References
1. S. V. Gusev, O. B. Sapir, and M. V. Volkov, *Strongly nonfinitely based monoids*, arXiv:2301.12426 (first posted 2023-01-29), Sections 2–3. https://arxiv.org/abs/2301.12426
2. F. S. Al-Kharousi, A. Umar, and M. M. Zubairu, *On injective partial Catalan monoids*, arXiv:2501.00285 (posted 2024-12-31), Sections 1 and 3. https://arxiv.org/pdf/2501.00285
3. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-decreasing partial transformations*, Journal of Integer Sequences 7 (2004), Article 04.3.8. https://cs.uwaterloo.ca/journals/JIS/VOL7/Umar/Umar034.pdf
4. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, Journal of Difference Equations and Applications 21 (2015), 269–283, DOI:10.1080/10236198.2015.1005080.
5. OEIS A001006 (Motzkin numbers) and A005773 (already known unweighted INVERT transform and asymptotic). https://oeis.org/A005773
6. A. Umar, *Semigroups of order-decreasing transformations*, PhD thesis, University of St Andrews (1992), DOI-neutral repository record https://research-repository.st-andrews.ac.uk/handle/10023/2834 (historical priority risk; detailed relevant sections not verified).
