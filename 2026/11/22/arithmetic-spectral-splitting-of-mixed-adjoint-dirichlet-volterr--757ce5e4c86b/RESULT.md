# Arithmetic spectral splitting of mixed adjoint Dirichlet–Volterra commutators

## Finding

Let \(\mathcal H^2\) be the Hardy Hilbert space of ordinary Dirichlet series, with orthonormal basis \(e_n(s)=n^{-s}\), \(n\geq1\). For each integer \(c\geq2\), let \(V_c\) be the Volterra operator induced by the Dirichlet monomial \(g_c(s)=c^{-s}\):
\[
V_cf(s)=-\int_s^{+\infty}f(w)g_c'(w)\,dw.
\]
For arbitrary integers \(a,b\geq2\), define the mixed adjoint commutator \(K_{a,b}=V_a^*V_b-V_bV_a^*\), put \(A=\log a\), \(B=\log b\), \(d=\gcd(a,b)\), and \(a'=a/d\). The complete **positive** singular-value multiset of \(K_{a,b}\) is the union, with multiplicities, of
\[
\left\{\frac{AB}{[\log(ba'm)]^2}:m\geq1,\ d\nmid m\right\}
\quad\text{and}\quad
\left\{AB\left[\frac1{(\log k+A)(\log k+B)}-\frac1{(\log k+A+B)^2}\right]:k\geq1\right\}.
\]
Both constituent sequences are strictly decreasing in their indicated integer arguments. No additional positive singular values occur. In particular, every \(K_{a,b}\) is compact of infinite rank but belongs to no finite Schatten class.

Writing \(N_{a,b}(t)=\#\{j:s_j(K_{a,b})>t\}\), the leading counting law has an **arithmetic phase transition**:
\[
\begin{aligned}
 d>1:&\qquad N_{a,b}(t)\sim\frac{d-1}{ab}\exp\!\left(\sqrt{\frac{AB}{t}}\right),\\
 d=1:&\qquad N_{a,b}(t)\sim
 \exp\!\left(-\frac{2A^2+5AB+2B^2}{3(A+B)}\right)
 \exp\!\left(\left[\frac{AB(A+B)}{t}\right]^{1/3}\right),
 \qquad t\downarrow0.
\end{aligned}
\]
Thus
\[
s_j(K_{a,b})\sim
\begin{cases}
AB/(\log j)^2,&d>1,\\
AB(A+B)/(\log j)^3,&d=1.
\end{cases}
\]
When \(d>1\), the cubic branch does **not** disappear: subtracting the exactly computable quadratic-branch counting function exposes the same cubic counting law, including its exponential prefactor. In the self-commutator case \(a=b\), the quadratic branch is the positive spectrum and the cubic branch is the absolute value of the negative spectrum, so the two signed spectral counts have different stretched-exponential scales.

## Assumptions and scope

All operators act on the same complex Hilbert space \(\mathcal H^2\), not on a weighted or vector-valued variant. The integral is taken along a rightward ray for Dirichlet polynomials, and operators are extended by boundedness. The integers \(a,b\) need not be distinct, prime, or coprime. The convention is \(N(t)=\#\{s_j>t\}\), with strict inequality and singular values counted with multiplicity. Limits are at fixed \(a,b\) as \(t\downarrow0\) or \(j\to\infty\). All logarithms are natural. No assertion is made about arbitrary Dirichlet-polynomial symbols, general Bergman measures, or eigenvalues of a nonnormal mixed commutator.

## Proof

**1. Exact coefficient action.** Direct integration gives \(V_ce_n=(\log c/\log(cn))e_{cn}\). Since \(n\mapsto cn\) is injective and the coefficient is at most one and tends to zero, \(V_c\) is a compact weighted partial permutation. In particular its adjoint satisfies \(V_c^*e_{cm}=(\log c/\log(cm))e_m\) and vanishes off multiples of \(c\). For every \(n\geq1\),
\[
K_{a,b}e_n=AB\left[
\frac{\mathbf1_{a\mid bn}}{[\log(bn)]^2}
-\frac{\mathbf1_{a\mid n}}{\log n\,\log(bn/a)}
\right]e_{bn/a},
\]
where the indicated output basis vector is used only when its integer index is defined. Each summand with a zero indicator is **omitted**, rather than evaluated as a product involving an undefined denominator; in particular the second summand is zero for \(n=1\). If neither indicator is one, the result is zero. This is an exact identity, not an asymptotic.

**2. Arithmetic decomposition and complete singular spectrum.** Write \(a=da'\) and \(b=db'\) with \(\gcd(a',b')=1\). The divisibility condition \(a\mid bn\) is equivalent to \(a'\mid n\). Every nonzero input therefore has the form \(n=a'm\). If \(d\nmid m\), the second term is absent and the output is \(e_{b'm}\), with coefficient \(AB/[\log(ba'm)]^2\). If \(d\mid m\), write \(m=dk\), so \(n=ak\); both terms occur, their output is \(e_{bk}\), and their coefficient is the negative of
\[
AB F(\log k),\qquad
F(u)=\frac1{(u+A)(u+B)}-\frac1{(u+A+B)^2}.
\]
All output indices are distinct because \(n\mapsto bn/a\) is injective on the allowed divisibility domain, including across the two branches. Hence \(K_{a,b}^*K_{a,b}\) is diagonal in the original basis, with exactly the two claimed squared-weight branches and zero elsewhere. The positive singular multiset follows. The quadratic weights decrease strictly. To see \(F(u)>0\) and strictly decreasing for \(u\geq0\), factor
\[
F(u)=\frac1{(u+A)(u+B)}\left[1-\frac{(u+A)(u+B)}{(u+A+B)^2}\right].
\]
Both factors are positive and strictly decreasing: the bracket decreases because its subtracted ratio has positive logarithmic derivative \(1/(u+A)+1/(u+B)-2/(u+A+B)>0\). Compactness follows because both weights tend to zero. The cubic sequence gives infinite rank even if \(d=1\).

**3. Exact counting of the quadratic branch.** Set \(X(t)=\exp(\sqrt{AB/t})/(ba')\). The quadratic weight at \(m\) exceeds \(t\) exactly when \(m<X(t)\). The number of such positive integers not divisible by \(d\) is exactly
\[
N_{\mathrm{quad}}(t)=\lceil X(t)\rceil-\lceil X(t)/d\rceil.
\]
For \(d=1\) this is identically zero; for \(d>1\), it equals \((1-1/d)X(t)+O(1)=(d-1)\exp(\sqrt{AB/t})/(ab)+O(1)\).

**4. Cubic branch and its exponential prefactor.** Put \(C=AB(A+B)>0\), \(D=-AB(2A^2+5AB+2B^2)\). Expansion of the exact rational function in inverse \(u\) yields
\[
ABF(u)=Cu^{-3}+Du^{-4}+O(u^{-5}),\qquad u\to+\infty.
\]
For \(0<t<ABF(0)\), there is a unique \(U(t)>0\) satisfying \(ABF(U(t))=t\). Substituting \(x=(C/t)^{1/3}\), the monotonicity and expansion imply
\[
U(t)=x+\frac{D}{3C}+O(x^{-1}).
\]
The number of cubic weights exceeding \(t\) is exactly \(N_{\mathrm{cubic}}(t)=\lceil e^{U(t)}\rceil-1\). Since \(e^{U(t)}\to\infty\),
\[
N_{\mathrm{cubic}}(t)\sim \exp\left(\frac{D}{3C}\right)\exp\left((C/t)^{1/3}\right).
\]
The exponent constant is \(D/(3C)=-(2A^2+5AB+2B^2)/(3(A+B))\). Summing the exact two counts proves the two cases of the counting law: \(\exp(\sqrt{AB/t})\) dominates \(\exp((C/t)^{1/3})\) if \(d>1\), while the quadratic count vanishes if \(d=1\). The individual singular-value laws follow by monotone inversion of the counting functions. Finally \(\sum_{j\geq2}(\log j)^{-rp}\) diverges for every finite \(r,p>0\); thus no finite Schatten membership holds.

**5. Signed self-commutator.** If \(a=b\), then \(K_{a,a}\) is diagonal. Inputs not divisible by \(a\) have strictly positive eigenvalues from the quadratic branch; inputs divisible by \(a\) have strictly negative eigenvalues from the cubic branch. The preceding exact counts therefore apply separately to the positive and negative eigenvalue populations. This is not a claim about the sign of a nonselfadjoint \(K_{a,b}\) when \(a\ne b\).

## Verification

The standalone `verify.py` checks the original two-step Volterra action against the exact arithmetic coefficients for several coprime and noncoprime pairs, tests the positivity/monotonicity and rationalized identity of \(F\), compares finite direct singular multisets with the two branches, and checks asymptotic coefficients numerically. The proof above supplies the infinite-dimensional spectral decomposition, counting constants and divergence for all finite Schatten exponents; finite checks alone cannot establish these global statements.

## Relationship to prior work

Bommier-Hato's 2020 work studies boundedness, compactness and Schatten nonmembership of individual Dirichlet-series Volterra operators on weighted Hilbert spaces. Gómez-Cabello, Lefèvre and Queffélec (first public 2024) establish a general non-Schatten theorem and polynomial-symbol compactness for Bergman spaces of Dirichlet series. Neither inspected article analyzes mixed **adjoint** Volterra commutators or an arithmetic two-branch singular-value decomposition.

A previously published mathematical result, *Singular spectra and two-number rigidity for Dirichlet–Volterra commutators* (2026), gives complete singular spectra for the **unstarred** commutator \([V_a,V_b]\): its action sends \(e_n\) to \(e_{abn}\), while the present mixed-adjoint operator sends only eligible inputs to \(e_{bn/a}\) and has a gcd-dependent quadratic/cubic phase transition. The former's coefficient involves \(|\log a-\log b|\), vanishing for equal indices; the present self-commutator is nonzero with signed branches. Consequently neither statement implies the other by a simple relabeling or taking adjoints. The previously published general sharp leading logarithmic singular-value laws for **individual** polynomial-symbol Volterra operators do not determine either commutator's spectrum. These comparisons do not rule out an alternative derivation from older general weighted-partial-permutation or operator-ideal theory.

## Limitations

The formulas use the unweighted coefficient space \(\mathcal H^2\) and individual positive-integer monomial symbols. Exact finite-rank approximation ranks are determined here only via the singular values of these mixed-adjoint commutators. The statement is not generalized to nonmonomial symbols or to other Dirichlet spaces. Originality is qualified by the possibility of unindexed special-operator commutator results or general weighted-permutation formulations. Independent mathematical validation and independent priority assessment have not been performed.

## References

1. H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, arXiv:2004.04087v1 (first public 8 April 2020), https://arxiv.org/html/2004.04087v1.
2. C. Gómez-Cabello, P. Lefèvre and H. Queffélec, *Volterra operator acting on Bergman spaces of Dirichlet series*, arXiv:2402.12524 (first public 19 February 2024), https://arxiv.org/abs/2402.12524.
3. O. F. Brevig, K.-M. Perfekt and K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729 (2016), https://arxiv.org/abs/1602.04729, foundational context only.
4. *Singular spectra and two-number rigidity for Dirichlet–Volterra commutators*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-singular-spectra-and-two-number-rigidity-for-dirichlet-volterra--a9dd2157993b.
5. *Sharp logarithmic singular-value law for polynomial Volterra operators on Bergman–Dirichlet spaces*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-logarithmic-singular-value-law-for-polynomial-volterra-ope--e7ab3387ec4a.
