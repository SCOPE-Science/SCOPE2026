# Oscillatory digit memory and a unique fluctuation maximum on a three-step double-base locus

## Finding
Fix any real \(b\in(0,1)\) and put \(q_1=b^{-1}\), \(q_0=1+b+b^2\), \(Q=q_0\), and \(D=1+2b+3b^2\). The greedy double-base map (defined below) has a stationary binary digit process \((D_n)_{n\ge0}\) with the following properties.

1. Every finite word containing \(111\) has probability zero, and every finite word avoiding \(111\) has positive probability. The digits are **second-order Markov but not first-order Markov**, for every \(b\in(0,1)\). The stationary length-of-current-one-run chain (states \(0,1,2\)) has transition matrix
\[
P_b=\begin{pmatrix}
Q^{-1}&b(1+b)Q^{-1}&0\\
(1+b)^{-1}&0&b(1+b)^{-1}\\
1&0&0
\end{pmatrix},
\qquad
\pi_b=\frac{1}{D}(Q,b(1+b),b^2).
\]
2. Write \(p_b=\mathbb E D_0=b(1+2b)/D\) and \(C_n=\operatorname{Cov}(D_0,D_n)\). Then
\[
C_0=p_b(1-p_b),\quad C_1=-\frac{b^3(b+2)}{D^2},\quad
C_{n+2}=-\frac{b(1+b)}{Q}C_{n+1}-\frac{b^2}{Q}C_n\quad(n\ge0).
\]
Its two nonconstant spectral modes are
\[
\lambda_\pm=\frac{b}{2Q}\bigl(-(1+b)\pm i\sqrt{3+2b+3b^2}\bigr).
\]
Consequently the correlations change sign infinitely often and their sharp root-exponential decay rate is
\[
\limsup_{n\to\infty}|C_n|^{1/n}=\frac{b}{\sqrt Q}.
\]
3. For \(S_N=\sum_{n=0}^{N-1}D_n\), a central limit theorem holds:
\[
\frac{S_N-Np_b}{\sqrt N}\xrightarrow{\mathcal D}
\mathcal N(0,\sigma_b^2),\qquad
\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}N=\sigma_b^2
=\frac{bQ(1+4b+b^2)}{D^3}.
\]
The exact independent-digit variance gap is
\[
p_b(1-p_b)-\sigma_b^2=\frac{6b^3(1+b)Q}{D^3}>0.
\]
The function \(b\mapsto\sigma_b^2\) has a **unique global maximum** at \(b_*=0.340712206148\ldots\), with \(\sigma_{b_*}^2=0.147153184831\ldots\). Precisely, \(b_*\) is the only positive root of
\[
H(b)=3b^6+26b^5+39b^4+40b^3+7b^2-6b-1.
\]

## Assumptions and scope
The parameters satisfy \(q_1=b^{-1}>1\), \(q_0=1+b+b^2>1\), and \(q_0+q_1>q_0q_1\), since \((1-b)q_0=1-b^3<1\). The greedy map on \([0,(q_1-1)^{-1}]\) is
\[
G(x)=\begin{cases}q_0x,&0\le x<b,\\b^{-1}x-1,&b\le x\le(q_1-1)^{-1}.\end{cases}
\]
Its unique absolutely continuous invariant probability \(\mu_b\), established in the cited source, is supported on \([0,r]\) where \(r=bQ=b+b^2+b^3\). Let \(X\sim\mu_b\), and define \(D_n=\mathbf1_{[b,\infty)}(G^nX)\). Endpoint conventions do not affect stationary probabilities. Markov order refers to the law of this stationary *binary* process and not to the three-state Markov partition. The asymptotic variance is variance per iteration of the greedy map.

## Proof
**1. Exact three-step postcritical orbit and stationary density.** Put \(u=b+b^2\), and partition \([0,r]\) into \(J_0=[0,b)\), \(J_1=[b,u)\), \(J_2=[u,r]\). Direct substitution gives
\[
G(r)=u,\qquad G(u)=b,\qquad G(b)=0,
\]
with one-sided endpoints understood as appropriate. The interiors of these three atoms map linearly as
\[
G(J_0)=[0,r],\qquad G(J_1)=[0,b],\qquad G(J_2)=[b,u].
\]
The invariant density is constant on each atom, with successive values
\[
h_0=\frac{Q}{bD},\qquad h_1=\frac{1+b}{bD},\qquad h_2=\frac1{bD}.
\]
Indeed, its total integral is \(h_0b+h_1b^2+h_2b^3=(Q+b(1+b)+b^2)/D=1\), and substituting each value into the Perron--Frobenius balance equations gives
\[
h_0=h_0/Q+b h_1,\quad h_1=h_0/Q+b h_2,\quad h_2=h_0/Q.
\]
Uniqueness of the absolutely continuous invariant probability identifies this density with \(d\mu_b/dx\).

**2. A finite Markov partition and genuine order two.** The image of every allowed atom transition is exactly its target atom, and slopes are constant. Hence for any positive-probability atom cylinder, the conditional distribution of its final point is uniform on the last atom. The stationary atom sequence is the Markov chain with
\[
R_b=\begin{pmatrix}Q^{-1}&bQ^{-1}&b^2Q^{-1}\\1&0&0\\0&1&0\end{pmatrix},
\quad \widetilde\pi_b=D^{-1}(Q,b(1+b),b^2).
\]
Here digit zero is exactly atom \(J_0\); digit one is either \(J_1\) or \(J_2\). Every zero resets the atom state to \(J_0\); a subsequent one chooses \(J_1\) with conditional probability \(1/(1+b)\) or \(J_2\) with conditional probability \(b/(1+b)\). State \(J_1\) must next emit zero, while \(J_2\) must next emit one and then zero. Thus a run of ones has exactly length one or two, independently after each zero, and the digit process has the run-length transition matrix \(P_b\) displayed in the finding. This proves second-order Markovity, the exact forbidden-word statement, and positivity of every other finite word. Since both \(01\) and \(11\) have positive probability but \(\Pr(D_{n+1}=1\mid 01)=b/(1+b)>0\) and \(\Pr(D_{n+1}=1\mid11)=0\), the binary process is *not* first-order Markov.

**3. Complete covariance spectrum and sign changes.** With \(g=(0,1,1)^\top\), \(p_b=\widetilde\pi_b g\), the exact finite-chain formula is
\[
C_n=\widetilde\pi_b\operatorname{diag}(g)R_b^n g-p_b^2.
\]
At lag zero this gives \(C_0=p_b(1-p_b)\), and at lag one it gives \(C_1=b^2/D-p_b^2=-b^3(b+2)/D^2\). The characteristic polynomial factors as
\[
\det(zI-R_b)=(z-1)\left(z^2+\frac{b(1+b)}Q z+\frac{b^2}Q\right).
\]
The constant eigenspace contribution cancels upon centering, so Cayley--Hamilton gives the claimed covariance recurrence for every \(n\ge0\). The quadratic discriminant is \(-b^2(3+2b+3b^2)/Q^2<0\). The nonconstant eigenvalues are the stated complex conjugates, both having modulus \(b/\sqrt Q<1\). Since \(C_0>0\), their coefficient pair is not zero; the real oscillatory sequence \(C_n=2\operatorname{Re}(A\lambda_+^n)\), \(A\ne0\), takes each strict sign infinitely often, whether the argument of \(\lambda_+\) is rational or irrational modulo \(2\pi\). It has the sharp stated limsup root rate.

**4. Gaussian fluctuation strength and suppression.** The primitive (irreducible and aperiodic) finite-state matrix \(R_b\) implies the stationary additive-functional CLT. By the absolutely summable covariance series,
\[
\sigma_b^2=C_0+2\sum_{n=1}^\infty C_n.
\]
Let \(A=b(1+b)/Q\), \(B=b^2/Q\). Summing the recurrence by its generating function gives
\[
\sum_{n=0}^\infty C_n=\frac{C_0+C_1+AC_0}{1+A+B}.
\]
Algebraic substitution yields \(\sigma_b^2=bQ(1+4b+b^2)/D^3>0\). Direct subtraction from \(p_b(1-p_b)\) gives the exact strictly positive gap displayed above. Alternatively, the tilted transfer matrix has Perron eigenvalue \(\Lambda(s)\), the positive root near \(s=0\) of
\[
\Lambda^3-Q^{-1}\Lambda^2-bQ^{-1}e^s\Lambda-b^2Q^{-1}e^{2s}=0,
\]
with \(\Lambda(0)=1\), \((\log\Lambda)'(0)=p_b\), and \((\log\Lambda)''(0)=\sigma_b^2\), giving an independent exact pressure check.

**5. A sharp and unique fluctuation optimum.** Differentiation and cancellation give
\[
\frac{d}{db}\sigma_b^2=-\frac{H(b)}{D^4},\quad
H(b)=3b^6+26b^5+39b^4+40b^3+7b^2-6b-1.
\]
The signs of its nonzero coefficients in descending powers change exactly once, so Descartes' rule of signs gives at most one positive zero; since \(H(0)=-1\) and \(H(1)=108>0\), this zero exists in \((0,1)\). The derivative is positive below and negative above that root, so it is the unique global maximizer. The numerical values stated arise from ordinary high-precision root evaluation; the exact defining equation is the proof.

## Verification
Run `python CHECKER.py` with Python 3 and SymPy installed. It checks the exact invariant-density balances, stationary Markov law, covariance identities, second-order recurrence, eigenvalue discriminant, variance sum, pressure derivatives and maximizing polynomial over the rational-function field, and then tests several exact rational parameters. Its finite tests are corroboration: the all-parameter, all-length and CLT results follow from the exact proofs above.

## Relationship to prior work
Huang--Komornik--Zou (arXiv:2605.08641v1, 2026) establish existence, uniqueness, support and a series formula for absolutely continuous invariant measures of double-base maps. These facts are used, not newly claimed. A published study *Exactly two Markov loci for greedy double-base digit dynamics* identifies all **first-order** digit Markov parameters and computes correlations on its two Markov loci. Its result explicitly leaves higher-order finite-memory processes outside its classification; the present curve has \(q_0=1+b+b^2>1+b\) and \(q_0<1/(1-b)\), so it does not lie on either first-order locus. The present result instead gives a genuine **second-order** digit chain, a complete complex oscillatory correlation spectrum, a sharp variance-suppression identity and an internally optimized variance over an entire unequal-base curve. Results for intermediate equal-slope \(\beta\)-shifts of finite type concern a different map; classical finite-state CLT and spectral perturbation theory are tools, not new inventions.

## Limitations
This is a one-parameter exact postcritical family, not a classification of all higher-order Markov parameters. Other invariant measures and the nonstationary transient before support entry are not described. Novelty is assessed from available primary literature and mathematical-record comparisons, not every unpublished computation or equivalent symbolic convention. The Gaussian limit is a classical finite-state theorem; novelty lies in the exact double-base realization, covariance spectrum and unique optimal fluctuation parameter. Independent scientific audit has not been performed.

## References
1. W. Huang, V. Komornik, and Y. Zou, *Invariant measure for double base expansions*, arXiv:2605.08641v1 (first public 2026-05-09), main theorems and invariant-density construction. https://arxiv.org/abs/2605.08641
2. *Exactly two Markov loci for greedy double-base digit dynamics*, public mathematical research record dated 2026-10-26; https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exactly-two-markov-loci-for-greedy-double-base-digit-dynamics--84eb54c8ccaf
3. B. Li, T. Sahlsten, and T. Samuel, *Intermediate \(\beta\)-shifts of finite type*, arXiv:1401.7027 (2014), related but different equal-slope maps. https://arxiv.org/abs/1401.7027
