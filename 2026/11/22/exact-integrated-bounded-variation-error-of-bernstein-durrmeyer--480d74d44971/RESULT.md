# Exact integrated bounded-variation error of Bernstein–Durrmeyer approximation

## Finding
For each integer \(n\ge 0\), define the classical Bernstein–Durrmeyer operator on integrable real functions by
\[
(M_n f)(x)=(n+1)\sum_{k=0}^n b_{n,k}(x)\int_0^1 b_{n,k}(t)f(t)\,dt,
\qquad b_{n,k}(x)=\binom nk x^k(1-x)^{n-k}.
\]
Its exact integrated approximation seminorm on distributional bounded variation is
\[
\boxed{\sup_{f\in BV(0,1),\ |Df|(0,1)>0}\frac{\|M_n f-f\|_{L^1(0,1)}}{|Df|(0,1)}=
\frac{\binom{2n+2}{n+1}}{4^{n+1}}.}
\]
Equality holds precisely for a nonzero multiple, plus a constant, of the centered single jump \(\mathbf 1_{(1/2,1)}\), modulo almost-everywhere equality. As \(n\to\infty\), the sharp constant equals
\[
\frac1{\sqrt{\pi(n+1)}}\left(1-\frac{1}{8(n+1)}+O(n^{-2})\right).
\]

## Assumptions and scope
Here \(BV(0,1)\) means real \(L^1(0,1)\) functions whose distributional derivative \(Df\) is a finite signed Radon measure on \((0,1)\); \(V(f)=|Df|((0,1))\). We identify functions agreeing almost everywhere, so arbitrary endpoint values or removable point spikes are not counted. For a nonconstant \(f\), the denominator is positive. The positive operator \(M_n\) acts on \(L^1(0,1)\); the theorem includes degree zero. Its kernel preserves constants, is symmetric and is normalized with respect to Lebesgue measure in either variable. The norm involves the **integrated error** \(\|M_n f-f\|_1\), not the variation of the image and not a pointwise operator norm.

## Proof
**1. Positive symmetric kernel and jump reduction.** Define
\[
K_n(x,t)=(n+1)\sum_{k=0}^n b_{n,k}(x)b_{n,k}(t).
\]
Each Bernstein basis function integrates to \(1/(n+1)\); therefore \(K_n\ge0\), \(K_n(x,t)=K_n(t,x)\), and \(\int_0^1 K_n(x,t)\,dt=\int_0^1 K_n(x,t)\,dx=1\). For \(0<s<1\), put \(H_s=\mathbf1_{(s,1)}\). Because \(M_n H_s\) is in \([0,1]\), the two terms in its error have definite signs on the two sides of \(s\). Symmetry and conservation of integrals give
\[
E_n(s):=\|M_n H_s-H_s\|_1
=2\int_0^s\int_s^1 K_n(x,t)\,dt\,dx.
\]

**2. An exact binomial representation.** Write \(m=n+1\) and
\[
F_k(s)=m\int_0^s b_{n,k}(x)\,dx
=\Pr\{X_s\ge k+1\},\qquad X_s\sim\operatorname{Bin}(m,s),\quad 0\le k<m.
\]
The identity follows from differentiating the binomial tail and matching its zero boundary. Inserting the kernel into the double integral yields
\[
E_n(s)=\frac2m\sum_{k=0}^{m-1}F_k(s)(1-F_k(s)).
\]
For independent \(X_s,Y_s\sim\operatorname{Bin}(m,s)\), the integer-valued tail-sum identity gives
\[
\mathbb E|X_s-Y_s|=2\sum_{k=0}^{m-1}F_k(s)(1-F_k(s)),
\qquad E_n(s)=\frac1m\mathbb E|X_s-Y_s|.
\]
This identity is exact for every \(s\in[0,1]\), with continuous zero limits at the endpoints.

**3. Strict localization of the worst jump.** Couple \(X_s-Y_s\) as a sum of \(m\) independent differences of pairs of Bernoulli variables. Each summand equals \(-1\) and \(+1\) with probability \(u=s(1-s)\) each and equals \(0\) with probability \(1-2u\). Let \(S_{m,u}\) be this sum. For any fixed real \(z\), differentiating the distribution of one summand shows
\[
\frac{d}{du}\mathbb E|S_{m,u}|=m\mathbb E\bigl(|S_{m-1,u}+1|+|S_{m-1,u}-1|-2|S_{m-1,u}|\bigr)
=2m\Pr\{S_{m-1,u}=0\}>0.
\]
The equality uses the fact that the summands are integers. The probability is positive throughout \(0\le u\le1/4\), because every summand can be zero with positive probability; this also holds when \(m=1\) by the empty-sum convention. Thus \(E_n(s)\) is strictly increasing in \(s(1-s)\), and its unique maximizer on \([0,1]\) is \(s=1/2\).

**4. Exact maximum.** At \(s=1/2\), independence and reflection give
\[
X_{1/2}-Y_{1/2}\ \stackrel d=\ Z-m,\qquad Z\sim\operatorname{Bin}(2m,1/2).
\]
The binomial recurrence
\( (j-m)\binom{2m}{j}=m[\binom{2m-1}{j-1}-\binom{2m-1}{j}]\)
for \(j>m\) telescopes to
\[
\mathbb E|Z-m|=m\frac{\binom{2m}{m}}{4^m},
\qquad E_n(1/2)=\frac{\binom{2m}{m}}{4^m}.
\]

**5. Global sharpness and equality rigidity.** Every \(f\in BV(0,1)\) has a representative with
\[
f(x)=c+\int_{(0,1)}H_s(x)\,d\mu(s)\quad\text{for a.e. }x,
\qquad \mu=Df,\quad |\mu|((0,1))=V(f).
\]
Constant preservation, Fubini, and the triangle inequality give
\[
\|M_nf-f\|_1\le\int_{(0,1)}E_n(s)\,d|\mu|(s)
\le E_n(1/2)V(f).
\]
Equality at a positive variation forces \(|\mu|\) to be concentrated at \(1/2\), since all other jump positions have strictly smaller \(E_n\). Conversely a nonzero centered jump attains the constant. This proves both the sharp norm and its complete equality family.

**6. Asymptotics.** Apply Stirling's expansion to the central binomial coefficient:
\(4^{-m}\binom{2m}{m}=(\pi m)^{-1/2}(1-1/(8m)+O(m^{-2}))\), with \(m=n+1\).

## Verification
The included standalone Python file `check.py` uses exact rational integration of Bernstein basis polynomials, an independent binomial absolute-deviation sum, and exact checks of the central-binomial formula for degrees \(0\) through \(15\). It also checks Markov symmetry and nonnegative jump images, plus signed multi-jump numerical stress tests. Execute `python check.py` with Python 3 standard library. Finite checks are corroboration; the universal result rests on the analytical argument above.

## Relationship to prior work
The classical Bernstein–Durrmeyer operator and its bounded-variation approximation have a substantial prior literature. Wang and Zhou (2009), building on Zeng and Chen (2000), gave **pointwise** estimates for Durrmeyer–Bézier operators on BV data; these do not state the exact global \(L^1\)-to-variation error constant or classify all its equality cases. Öksüzer, Karsli, and Taşdelen Yeşildal (2016) proved variation diminution and convergence in the **variation seminorm**, a different quantity. Berdysheva, Dyn, Farkhi, and Mokhov (2022) established an \(O(n^{-1/2})\) integrated approximation bound in a more general setting, but not the sharp classical scalar coefficient or its unique norming jump. Liu (2014) addressed other positive Bernstein–Durrmeyer approximation rates. The known sharp integrated BV constant for point-sampled Bernstein polynomials behaves as \((2\pi n)^{-1/2}\), whereas the integral Durrmeyer modification has the different leading constant \((\pi n)^{-1/2}\); the resulting \(\sqrt2\) asymptotic ratio measures the sharp cost of extra smoothing. This is a comparison, not a claim that the earlier results fail.

## Limitations
The proof is for the unweighted classical one-dimensional kernel and Lebesgue \(L^1\) error. It does not cover Jacobi-weighted variants, irregular domains, multi-dimensional operators or other error norms. Historical-priority verification is not exhaustive: the full 2000 Zeng–Chen paper and older Guo work were not available for complete comparison; their accessible abstracts and subsequent published theorem quotations concern pointwise BV approximation, but do not logically exclude an equivalent result elsewhere. No independent audit is claimed.

## References
- P. Wang and Y. Zhou, *A New Estimate on the Rate of Convergence of Durrmeyer–Bézier Operators*, Journal of Inequalities and Applications 2009, article 702680, published 2009-05-05, DOI: 10.1155/2009/702680.
- X.-M. Zeng and W. Chen, *On the Rate of Convergence of the Generalized Durrmeyer Type Operators for Functions of Bounded Variation*, Journal of Approximation Theory 102 (2000), 1–12, DOI: 10.1006/jath.1999.3367.
- G. Liu, *Pointwise approximation for a type of Bernstein–Durrmeyer operators*, Journal of Inequalities and Applications 2014, article 106, published 2014-03-04, DOI: 10.1186/1029-242X-2014-106.
- Ö. Öksüzer, H. Karsli, F. Taşdelen Yeşildal, *Convergence of the Bernstein–Durrmeyer Operators in Variation Seminorm*, arXiv:1605.03976 (first submitted 2016-04-30), https://arxiv.org/abs/1605.03976.
- E. Berdysheva, N. Dyn, M. Farkhi, A. Mokhov, *Metric approximation of set-valued functions of bounded variation by integral operators*, arXiv:2212.00439 (2022), https://arxiv.org/abs/2212.00439.
