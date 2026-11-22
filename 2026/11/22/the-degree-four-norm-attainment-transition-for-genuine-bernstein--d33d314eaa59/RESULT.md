# The degree-four norm-attainment transition for genuine Bernstein–Durrmeyer approximation

## Finding

Let \(U_n\) denote the genuine Bernstein–Durrmeyer (Goodman–Sharma) operator for each integer \(n\geq1\), with endpoint values set by one-sided traces. Define the sharp integrated-error coefficient
\[
C_n=\sup_{f\in BV(0,1),\ |Df|(0,1)>0}\frac{\|U_nf-f\|_{L^1(0,1)}}{|Df|(0,1)}.
\]
For each \(s\in(0,1)\), let independent random variables \(A\sim\mathrm{Bin}(n+1,s)\) and \(B\sim\mathrm{Bin}(n-1,s)\), and put
\[
E_n(s)=\frac{1}{n+1}\mathbb E|A-B-1|.
\]
Then \(C_n=\max_{0\le s\le1}E_n(s)\), taking the continuous extension at the two endpoints. In particular, this is an exact, finite polynomial maximization with no approximation or infinite search.

**The sharp boundary-to-interior transition is at degree four:**
\[
C_n=\frac{1}{n+1}\quad(n=1,2,3),
\]
with **no nonconstant norm-attaining input** at these three degrees. For every \(n\ge4\), \(C_n>1/(n+1)\) and at least one interior single-jump input attains the sharp norm. The explicit midpoint certificate for every degree is
\[
E_n(1/2)=\frac{n}{n+1}\frac{\binom{2n}{n}}{4^n}.
\]
Moreover
\[
\lim_{n\to\infty}\sqrt n\,C_n=\frac1{\sqrt\pi},
\qquad
\lim_{n\to\infty}s_n=\frac12
\]
for **every** choice of global maximizing jump location \(s_n\in(0,1)\) at each \(n\ge4\). No claim is made that the midpoint is a finite-degree global maximizer or that all equality inputs for \(n\ge4\) are single jumps.

## Assumptions and scope

We use real distributional \(BV(0,1)\), choosing its regulated one-sided trace representative at the endpoints; in particular \(f(0)=f(0+)\) and \(f(1)=f(1-)\). This endpoint convention matters because \(U_n\) evaluates both endpoint values. Let \(p_{n,k}(x)=\binom nk x^k(1-x)^{n-k}\) and
\[
(U_nf)(x)=(1-x)^nf(0)+x^nf(1)+(n-1)\sum_{k=1}^{n-1}p_{n,k}(x)\int_0^1p_{n-2,k-1}(t)f(t)\,dt.
\]
The empty sum at \(n=1\) is zero. All integrals and error norms are unweighted Lebesgue integrals. The variation denominator counts only interior distributional variation. Constants are reproduced.

## Proof

**1. Reduction to jumps.** For \(s\in(0,1)\) write \(h_s=\mathbf1_{[s,1]}\), with endpoint traces \(h_s(0)=0\), \(h_s(1)=1\). Every admissible real \(BV\) representative has the signed-measure representation \(f(x)=c+\int_{(0,1)}h_s(x)\,Df(ds)\) almost everywhere. Fubini and the triangle inequality imply
\[
\|U_nf-f\|_1\le\int E_n(s)\,|Df|(ds),
\]
where \(E_n(s)=\|U_nh_s-h_s\|_1\). Conversely, a single jump attains the value \(E_n(s)\), so the supremum is the supremum of these responses.

**2. Exact two-binomial identity.** Write \(Q_s(x)=(U_nh_s)(x)\). For \(0<s<1\),
\[
Q_s(x)=x^n+\sum_{k=1}^{n-1}p_{n,k}(x)\bigl[1-I_s(k,n-k)\bigr],
\]
where \(I_s(a,b)\) denotes the regularized incomplete Beta integral. Integration in \(x\) and the identity \(\sum_{k=1}^{n-1}(1-I_s(k,n-k))=(n-1)(1-s)\) yield
\[
E_n(s)=\frac{1-2s}{n+1}+\frac2{n+1}\left[s^{n+1}+\sum_{k=1}^{n-1}I_s(k+1,n-k+1)\bigl(1-I_s(k,n-k)\bigr)\right].
\]
For independent \(A\sim\mathrm{Bin}(n+1,s)\), \(B\sim\mathrm{Bin}(n-1,s)\), the beta-binomial tail identity identifies the two factors in the sum as \(\Pr(A\ge k+1)\) and \(\Pr(B\le k-1)\). Counting the integers \(k\) satisfying \(B+1\le k\le A-1\), \(1\le k\le n-1\), gives
\[
\sum_{k=1}^{n-1}\Pr(A\ge k+1)\Pr(B\le k-1)=\mathbb E(A-B-1)_+-s^{n+1}.
\]
As \(\mathbb E(A-B-1)=2s-1\) and \(2v_+=|v|+v\), substitution proves \(E_n(s)=\mathbb E|A-B-1|/(n+1)\), also valid for \(n=1\). Thus it is the expectation of \(|W-n|\) for \(W=A+n-1-B\), a sum of \(n+1\) independent Bernoulli\((s)\) and \(n-1\) independent Bernoulli\((1-s)\) variables. In particular \(E_n\) extends polynomially to \([0,1]\), with \(E_n(0)=E_n(1)=1/(n+1)\). This proves the finite exact maximum formula.

**3. Nonattainment through degree three.** Put \(q=s(1-s)\). Direct binomial expansion yields
\[
(n+1)E_n(s)=\begin{cases}
1-2q,&n=1,\\
1-2q+4q^2,&n=2,\\
1-2q+10q^2-12q^3,&n=3.
\end{cases}
\]
For \(0<s<1\), \(0<q\le1/4\), and all three polynomials are strictly below \(1\): the three respective differences from \(1\) factor as \(-2q\), \(-2q(1-2q)\), and \(-2q(1-2q)(1-3q)\). Hence the supremum is the unattained endpoint limit \(1/(n+1)\). For arbitrary nonconstant \(f\), the jump bound integrates a strictly positive deficit against the nonzero measure \(|Df|\), so such \(f\) cannot attain equality either.

**4. Degree-four interior attainment.** At \(s=1/2\), \(W\sim\mathrm{Bin}(2n,1/2)\). Binomial telescoping yields \(\mathbb E|W-n|=n4^{-n}\binom{2n}{n}\). Define \(a_n=n4^{-n}\binom{2n}{n}\); then \(a_{n+1}/a_n=(2n+1)/(2n)>1\), while \(a_3=15/16<1\) and \(a_4=35/32>1\). Consequently \(E_n(1/2)>1/(n+1)\) at every \(n\ge4\). Continuity and compactness show that a maximum lies in \((0,1)\), and its single-jump function is a norming input.

**5. Sharp large-degree limit and localization.** For \(s\in[0,1]\), the above Bernoulli sum satisfies \(\mathbb E W=n+2s-1\) and \(\operatorname{Var}(W)=2ns(1-s)\). For any sequence \(s_n\to s\in(0,1)\), the triangular-array central limit theorem for bounded independent Bernoulli variables gives
\[
\frac{W_{n,s_n}-n}{\sqrt n}\ \Longrightarrow\ N\bigl(0,2s(1-s)\bigr).
\]
Uniform boundedness of the corresponding second moments gives uniform integrability, hence
\[
\sqrt n\,E_n(s_n)\longrightarrow\frac{2\sqrt{s(1-s)}}{\sqrt\pi}.
\]
If \(s_n\to0\) or \(s_n\to1\), the second-moment bound instead gives a limit of zero. This sequential convergence on the compact parameter interval implies uniform convergence of \(\sqrt n E_n(s)\) to the continuous profile \(2\sqrt{s(1-s)/\pi}\). The latter has the unique maximizer \(1/2\) and maximum \(1/\sqrt\pi\), proving both asserted limits for the sharp coefficients and **every** maximizing location.

## Verification

The self-contained checker `verify_genuine_bd.py` symbolically expands the exact two-binomial formula for the first three degrees, checks midpoint and endpoint identities in exact arithmetic through degree fourteen, and compares the direct integrated single-jump response with the independent binomial formula for 112 degree/step pairs. It also checks the central-value asymptotic numerically at several degrees. Run `python3 verify_genuine_bd.py` with SymPy and SciPy installed. The infinite-degree limit and norm attainment are proved analytically above, not extrapolated from these finite checks.

## Relationship to prior work

Gonska, Kacsó and Raşa established approximation and semigroup results for the genuine operator; Sauer studied its multivariate singular-weight framework. Direct/inverse estimates and smooth-function asymptotics do not by themselves fix the sharp integrated BV error or the attainment transition. The 2021 Durrmeyer–Stancu article gives the defining classical formula as background and develops modified operators, not the present BV-to-integrated-error extremal problem. A known exact result for the **ordinary** Bernstein–Durrmeyer integral operator has a midpoint norming jump in every degree and thus does not imply the degree-four transition of the distinct endpoint-interpolating genuine operator. The binomial absolute-moment reduction is specific to the latter's two endpoint atoms and interior Beta weights.

## Limitations

The exact maximizing position and exact closed-form coefficient for each finite \(n\ge4\) are not classified; only the finite polynomial prescription, attainment, center lower bound and sharp large-degree limit are proved. No classification of **all** norming BV functions is claimed at these degrees. Arbitrary endpoint assignments, weighted Lebesgue error, and higher-dimensional genuine operators are excluded. The available original 2012 article was a subscription preview rather than inspectable full text; historical priority therefore carries a residual literature risk, and independent validation is not claimed.

## References

1. H. Gonska, D. Kacsó and I. Raşa, *The Genuine Bernstein–Durrmeyer Operators Revisited*, Results in Mathematics 62 (2012), 295–310, first online August 18, 2012. https://doi.org/10.1007/s00025-012-0287-1
2. H. Gonska, D. Kacsó and I. Raşa, *On Genuine Bernstein–Durrmeyer Operators*, Results in Mathematics 50 (2007), 213–225. University Duisburg–Essen preprint archive (2007): https://www.uni-due.de/mathematik/preps07_en
3. T. Sauer, *The Genuine Bernstein–Durrmeyer Operator on a Simplex*, Results in Mathematics 26 (1994), 99–130. https://doi.org/10.1007/BF03322291
4. A. Alotaibi et al., *Approximation of functions by a class of Durrmeyer–Stancu type operators which includes Euler's beta function*, Advances in Difference Equations (2021), article 13. https://doi.org/10.1186/s13662-020-03164-0
5. U. Abel, A. M. Acu, M. Heilmann and I. Raşa, *Asymptotic Expansions for Generalized Bernstein–Durrmeyer and Genuine Bernstein–Durrmeyer Operators*, Complex Analysis and Operator Theory 20 (2026), article 70. https://doi.org/10.1007/s11785-026-01929-1
