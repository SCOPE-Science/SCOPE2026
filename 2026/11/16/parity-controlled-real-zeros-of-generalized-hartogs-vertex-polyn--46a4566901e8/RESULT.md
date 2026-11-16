# Parity-controlled real zeros of generalized Hartogs vertex polynomials

## Finding
For every integer \(N\ge2\) and real \(0<\alpha\le1\), define
\[
Q_{N,\alpha}(z)=\sum_{n=1}^{N}n(N+\alpha-n)z^{n-1}.
\]
All its coefficients are strictly positive. Its real-zero diagram is complete:

* **Even \(N\).** There is precisely one real zero, negative and simple. It is strictly below \(-1\) if \(0<\alpha<1\), and equals \(-1\) if \(\alpha=1\).
* **Odd \(N\ge3\).** There exists precisely one parameter \(\alpha_N\in(0,(N-1)/(2N+1))\) at which a real-root collision occurs. When \(0<\alpha<\alpha_N\), there are exactly two distinct, simple real zeros, both less than \(-1\); at equality there is precisely one double real zero below \(-1\); and when \(\alpha_N<\alpha\le1\), there are no real zeros. All other zeros, in every case, are simple and nonreal.

The exact parameter characterization is
\[
\alpha_N=\max_{x>1}R_N(x),\qquad
R_N(x)=\frac{x^N[(N+1)+(N-1)x]-[(N-1)+(N+1)x]}{(1+x)[1+x^N(N+1+Nx)]}.
\]
The maximum is attained at exactly one \(x_N>1\), and
\[
\lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}\alpha_N=\tfrac12.
\]
In particular, the threshold for \(N=3\) is \(\alpha_3=(\sqrt6-2)/2\), a previously noted low-degree instance, now placed in the full parity diagram.

## Assumptions and scope
The polynomial occurs in generalized Hartogs triangle Bergman analysis with \(1<\gamma<2\), \(\delta=1-1/\gamma\), \(1/\delta=N+\alpha\), and \(N=\lceil1/\delta\rceil-1\). The normalized vertex polynomial of Fu is exactly \(P_\delta=\delta Q_{N,\alpha}\); positive scaling does not affect its roots. The assertion concerns every integer \(N\ge2\), the whole half-open range \(0<\alpha\le1\), and all real roots counted with multiplicity. There are no positive roots, because every coefficient is positive.

## Proof
Write \(S(z)=(1-z)^3Q_{N,\alpha}(z)=A(z)+z^NB(z)\), with
\[
A(z)=N+\alpha-1-(N+\alpha+1)z,
\quad B(z)=(N+1)(1-\alpha)+(2N\alpha+\alpha-N+1)z-N\alpha z^2.
\]
The identity follows by subtracting the tail from the two geometric sums for \(\sum nz^{n-1}\) and \(\sum n^2z^{n-1}\). For each \(x\in[0,1)\), both parity cases give \(S(-x)>0\). To see this uniformly in \(\alpha\), inspect its endpoints. If \(N\) is odd, at \(\alpha=0\) the value is
\[
N-1+(N+1)x-x^N[(N+1)+(N-1)x]\ge (N-1)(1-x^2)>0,
\]
and the \(\alpha\)-coefficient is \((1+x)[1+x^N(N+1+Nx)]>0\). If \(N\) is even, at \(\alpha=0\) the value is the strictly positive sum
\(N-1+(N+1)x+x^N[(N+1)+(N-1)x]\); at \(\alpha=1\) it is
\[
N+(N+2)x-x^{N+1}[(N+2)+Nx]\ge N(1-x^2)>0.
\]
Linearity in \(\alpha\) gives positivity for all intermediate parameters. At \(x=1\), \(S(-1)=4(N+1)\alpha>0\) for odd \(N\), and \(S(-1)=4N(1-\alpha)\) for even \(N\). Since \(1+x>0\), these statements transfer from \(S\) to \(Q\).

Put \(x=1+y\) with \(y>0\), and let \(C_j=\binom Nj\), extended by zero outside \(0\le j\le N\). For \(2\le j\le N+2\), put
\[
U_j=(4N+2)C_j+(4N+1)C_{j-1}+NC_{j-2},
\quad V_j=2NC_j+(N-1)C_{j-1}.
\]
Every \(U_j\) is positive. The ratios \(r_j=V_j/U_j\) strictly decrease from \(r_2=(N-1)/(2N+1)\) to \(r_{N+2}=0\). Here is an elementary justification of the needed monotonicity. Associate the three coefficient positions \(k=0,1,2\) with positive weights \(a=(4N+2,4N+1,N)\) and decreasing values \(b_k/a_k=(2N/(4N+2),(N-1)/(4N+1),0)\). The probability masses proportional to \(a_kC_{j-k}\) shift to larger \(k\) as \(j\) increases, because \(C_{j+1-k}/C_{j-k}=(N-j+k)/(j+1-k)\) is increasing in \(k\) whenever defined; zeros at support endpoints preserve this monotone-likelihood-ratio ordering. The expectation of the strictly decreasing sequence \(b_k/a_k\) therefore strictly decreases. This also proves the endpoint values by direct binomial simplification.

Direct expansion at \(-1-y\) now yields, for odd \(N\),
\[
S(-1-y)=4(N+1)\alpha+2(N+1)[(2N+1)\alpha-(N-1)]y
+\sum_{j=2}^{N+2}(\alpha U_j-V_j)y^j.
\]
Its coefficients have at most two sign changes (positive constant, at most one contiguous negative run, then positives), because \(r_j\) decreases and \(r_2=(N-1)/(2N+1)\). Descartes' rule of signs bounds the number of positive \(y\)-roots, counted with multiplicity, by two. On \(x>1\) the equation \(S(-x)=0\) is equivalent to \(\alpha=R_N(x)\). The function \(R_N\) is strictly positive on \(x>1\): use \(x^N\ge x\) and \(x[(N+1)+(N-1)x]-[(N-1)+(N+1)x]=(N-1)(x^2-1)>0\). It is continuous and tends to zero at both endpoints \(x\downarrow1\) and \(x\to\infty\). Consequently it has a positive attained maximum \(\alpha_N\). For \(\alpha<\alpha_N\), the value of \(S(-x)\) changes sign twice between the two positive ends of the \(y\)-axis; Descartes forces exactly two simple roots. At the maximum, there is at least a double root; Descartes forces it to be the unique root, of multiplicity exactly two, and also forces uniqueness of the maximizing point. Above the maximum, there is no root. At \(\alpha=r_2\), all coefficients in this expansion are nonnegative and the constant is strictly positive, hence \(\alpha_N<r_2\). Since \(R_N(x)\to1/(1+x)\) for each fixed \(x>1\) through odd \(N\), and \(\alpha_N<(N-1)/(2N+1)\to1/2\), we obtain \(\alpha_N\to1/2\) by first taking \(N\to\infty\), then \(x\downarrow1\).

For even \(N\), the corresponding coefficient expansion has the opposite high-degree sign:
\[
S(-1-y)=4N(1-\alpha)+2N[(N+1)-(2N+3)\alpha]y
+\sum_{j=2}^{N+2}(V_j-\alpha U_j)y^j.
\]
Because \((N+1)/(2N+3)>r_2\) and the \(r_j\) decrease, its signs undergo at most one positive-to-negative change. For \(0<\alpha<1\), the constant is positive and the leading coefficient \(-N\alpha\) is negative, so Descartes plus the intermediate value theorem gives exactly one simple root \(y>0\). At \(\alpha=1\), the constant vanishes and every remaining coefficient is strictly negative, so the only negative real root is \(z=-1\), simple. Combined with the absence of roots on \((-1,\infty)\), this proves the real-root classification.

To exclude nonreal multiple roots, differentiate \(S=A+z^NB\) and eliminate the \(z^N\)-term:
\[
zBS'-(NB+zB')S=-N(N+1)(z-1)^2[\alpha(N+\alpha+1)z+(1-\alpha)(N+\alpha-1)].
\]
A multiple zero of \(Q\) cannot equal \(0\) or \(1\), and would have to be the single negative real number \(-\frac{(1-\alpha)(N+\alpha-1)}{\alpha(N+\alpha+1)}\). Triple multiplicity is impossible because the right-hand side has only a simple zero there. Thus all remaining zeros are simple, as asserted.

## Verification
The independent reproducibility script `checker.py` checks the polynomial and elimination identities symbolically for representative degrees, the strictly decreasing binomial ratios by exact rational arithmetic, the signs of the coefficient expansions, and small-degree exact real-root counts on both sides of the analytically defined transition. These finite checks support but do not establish the all-degree theorem: its proof is the argument above.

For each noncritical parameter, the locally uniformly convergent vertex sections \(F_t(v)=\pi^2t(1-t)^2K_\gamma(vt,t)\to\delta Q_{N,\alpha}(v)\) have exactly the same number of real negative zeros among the \(N-1\) zeros remaining in any fixed sufficiently large disk, for all sufficiently small \(t>0\). This follows from Rouché's theorem on disjoint disks around the simple roots, conjugation symmetry, and the real implicit function theorem. No claim is made here about the double-root splitting at the critical parameter or about possible zeros outside the prescribed disk.

## Relationship to prior work
Edholm and Mathew (first public May 26, 2025) introduced a rational generalized-Hartogs kernel framework and asked for zeros in the subcritical exponent range. The subsequent full manuscript of Fu (first public November 11, 2026) defines precisely the polynomial \(P_\delta\), proves compact-uniform vertex-section convergence, and proves all roots are simple except possibly one double negative root; it also exhibits the \(N=3\) critical example. Those statements are retained as prior results, not claimed here. The new contribution is an all-degree, exact parity classification of **how many real roots there are**, the unique threshold at every odd degree, its maximization characterization, and its asymptotic limit; these do not follow from the one-possible-double-root lemma alone. The diagonal-oblique fixed-gap Hartogs numerator literature studies a different polynomial family and does not directly settle this count.

## Limitations
The threshold formula is variational rather than a radical formula for general degrees. The result does not classify the full complex angular distribution, does not count all kernel zeros throughout the unrestricted admissible section, and does not independently reprove the cited kernel-convergence theorem. An unlocated older result on the real roots of related truncated power sums could subsume the count; novelty is therefore a best-knowledge literature assessment rather than a uniqueness guarantee. The exact 2026 vertex-limit framework is credited as prior work; the earlier 2025 Hartogs-kernel study motivates the question.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489, first public 2025-05-26, https://arxiv.org/abs/2505.20489 .
2. Qian Fu, *Bergman Kernel Zeros on Generalized Hartogs Triangles*, arXiv:2611.15406v1, first public 2026-11-11, https://arxiv.org/html/2611.15406v1 ; especially Lemmas 2.3 and 3.1, read in full.
3. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480, first public 2026-11-05, https://arxiv.org/abs/2611.07480 ; its palindromic oblique-diagonal numerator is a different polynomial.
