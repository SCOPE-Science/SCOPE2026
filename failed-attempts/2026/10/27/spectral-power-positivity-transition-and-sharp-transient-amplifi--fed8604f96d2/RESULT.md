# Spectral-power positivity transition and sharp transient amplification on cocktail-party graphs

## Finding
Let \(N\ge4\) be even. Remove a perfect matching from the complete graph on \(N\) vertices, denote its (unnormalized) Laplacian by \(L\), and for every real \(s>0\) set \(T_s(t)=\exp(-tL^s)\) for \(t\ge0\), where the power is spectral and \(0^s=0\). Write
\[
 F_{N,s}(t)=N e^{-(N-2)^s t}-(N-2)e^{-N^s t}-2.
\]
Then the **exact sharp endpoint stability constant at every time** is
\[
 \|T_s(t)\|_{\ell^1\to\ell^1}=\|T_s(t)\|_{\ell^\infty\to\ell^\infty}
 =1+\frac{[F_{N,s}(t)]_+}{N},\qquad [z]_+=\max\{z,0\}.
\]
If \(0<s\le1\), all entries are nonnegative for every \(t\ge0\) and both norms equal one. If \(s>1\), all off-diagonal entries except those between the deleted-matching partners are strictly positive at \(t>0\); the partner entry is strictly negative for \(0<t<\tau_{N,s}\), zero at the unique \(\tau_{N,s}>0\) satisfying \(F_{N,s}(\tau_{N,s})=0\), and positive thereafter. Hence the *entire matrix* is nonnegative exactly at \(t=0\) and \(t\ge\tau_{N,s}\).

For every \(s>1\), transient amplification is uniquely maximized at
\[
 \theta_{N,s}=\frac{(s-1)\log(N/(N-2))}{N^s-(N-2)^s},
\]
with exact maximum
\[
 \sup_{t\ge0}\|T_s(t)\|_{\ell^\infty\to\ell^\infty}
 =1+\frac{1}{N}\left(N\left[1-\left(\frac{N-2}{N}\right)^s\right]
 \exp\left[-(N-2)^s\theta_{N,s}\right]-2\right).
\]
At any time with \(F_{N,s}(t)>0\), the norm is attained by a sign function that is negative at one specified vertex's deleted-matching partner and positive at every other vertex.

There are three complementary sharp scaling laws:

1. **Growing graph, fixed spectral power \(s>1\).** Put \(u_s>0\) for the unique positive solution of \(e^{u_s}=1+s u_s\). Then
\[
 N^s\theta_{N,s}\longrightarrow\frac{s-1}{s},\qquad
 N^s\tau_{N,s}\longrightarrow u_s,
\]
\[
 N\left(\sup_{t\ge0}\|T_s(t)\|_{\ell^\infty\to\ell^\infty}-1\right)
 \longrightarrow 2\left(s e^{-(s-1)/s}-1\right).
\]
More precisely, at each fixed scaled time \(u\ge0\),
\[
 N\left(\|T_s(u/N^s)\|_{\ell^\infty\to\ell^\infty}-1\right)
 \longrightarrow 2\big[(1+s u)e^{-u}-1\big]_+.
\]
2. **Approach to the critical exponent, fixed even \(N\ge4\).** For \(\delta=s-1\downarrow0\), setting \(r_N=\log(N/(N-2))\),
\[
 \theta_{N,1+\delta}=\frac{r_N}{2}\delta+O_N(\delta^2),\qquad
 \tau_{N,1+\delta}=r_N\delta+o_N(\delta),
\]
\[
 \sup_{t\ge0}\|T_{1+\delta}(t)\|_{\ell^\infty\to\ell^\infty}
 =1+\frac{N-2}{4}r_N^2\delta^2+O_N(\delta^3).
\]
3. **High spectral power, fixed even \(N\ge4\).** As \(s\to\infty\),
\[
 (N-2)^s\tau_{N,s}\longrightarrow\log(N/2),\qquad
 \sup_{t\ge0}\|T_s(t)\|_{\ell^\infty\to\ell^\infty}\longrightarrow 2-\frac2N.
\]
The latter bound is not attained at finite \(s\). Every assertion concerns the unnormalized graph Laplacian and counting-measure norms.

## Assumptions and scope
The vertices occur in \(N/2\) disjoint unordered pairs. Distinct vertices are adjacent unless they lie in the same pair. Write \(J\) for the all-ones matrix and \(R\) for the permutation matrix swapping partners. The adjacency matrix is \(J-I-R\), so \(L=(N-1)I-J+R\). On the real coordinate space, \(\ell^p\) uses counting measure; on the complex space the same induced norm formulas hold. All exponents are real \(s>0\), all times are \(t\ge0\), and constants in \(O_N\) may depend on fixed \(N\).

## Proof
**Spectral resolution and signs.** Define mutually orthogonal projections
\[
 P_0=J/N,\qquad P_-=(I-R)/2,\qquad P_+=(I+R)/2-J/N.
\]
They sum to \(I\), and direct multiplication yields \(LP_0=0\), \(LP_-=(N-2)P_-\), and \(LP_+=NP_+\). Thus with \(a=e^{-(N-2)^st}\), \(b=e^{-N^st}\),
\[
 T_s(t)=P_0+aP_-+bP_+
 =\frac{1-b}{N}J+\frac{a+b}{2}I+\frac{b-a}{2}R.
\]
A diagonal entry is \((1-b)/N+(a+b)/2>0\). An ordinary adjacent off-diagonal entry is \((1-b)/N>0\) for \(t>0\). A deleted-matching partner entry is
\[
 h_s(t)=\frac{1-b}{N}+\frac{b-a}{2}=-\frac{F_{N,s}(t)}{2N}.
\]
All rows sum to one; this follows both from \(T_s(t)\boldsymbol 1=\boldsymbol 1\) and from the display. Exactly one entry in any row can be negative. Hence the absolute row sum is \(1+2[-h_s(t)]_+=1+[F_{N,s}(t)]_+/N\). Symmetry gives the equal sharp \(\ell^1\) norm. An aligned sign vector realizes the absolute row sum, so these are exact operator norms rather than bounds.

Put \(\alpha=(N-2)^s\) and \(\beta=N^s\), so \(0<\alpha<\beta\). We have \(F(0)=0\), \(F(\infty)=-2\), and
\[
 F'(t)=-N\alpha e^{-\alpha t}+(N-2)\beta e^{-\beta t}.
\]
Its sign is that of \(C e^{-(\beta-\alpha)t}-1\), with
\[
 C=\frac{(N-2)\beta}{N\alpha}=\left(\frac{N}{N-2}\right)^{s-1}.
\]
If \(s\le1\), then \(C\le1\), so \(F'(t)<0\) for \(t>0\). If \(s>1\), then \(C>1\); the derivative changes sign exactly once, from positive to negative, at \(\theta_{N,s}=\log C/(\beta-\alpha)\). Consequently \(F\) has a strictly positive unique maximum, then crosses zero at exactly one positive \(\tau_{N,s}>\theta_{N,s}\) and stays negative. Substitution of \(e^{-(\beta-\alpha)\theta}=1/C\) into \(F\) yields the displayed peak. Since \(a<1\) and \(b>0\) for finite \(t>0\), \(F(t)<N-2\), proving the strict bound \(\sup\|T\|<2-2/N\).

**Fixed-power high-dimensional limit.** Write \(\rho_N=1-2/N\) and scale \(u=N^s t\). Then
\[
 F_{N,s}(u/N^s)=N(e^{-\rho_N^s u}-e^{-u})+2(e^{-u}-1).
\]
Since \(N(1-\rho_N^s)\to2s\), the right side converges, uniformly on every compact \(u\)-interval, to \(2[(1+s u)e^{-u}-1]\). Its derivative is \(2(s-1-su)e^{-u}\); it increases to the unique maximum at \(u=(s-1)/s\), then decreases and has exactly one positive zero \(u_s\), since \(e^u-1-su\) is initially decreasing and strictly convex. The explicit formula for \(\theta_{N,s}\) yields the first limit. Positivity at scaled times immediately above and below \(u_s\), together with uniqueness of the finite cutoff, traps \(N^s\tau_{N,s}\) between such times. Evaluating the displayed peak formula at the scaled maximizer gives the sharp amplitude limit. Applying positive part to the fixed-time limit gives the scaled norm profile.

**Critical spectral exponent.** Put \(s=1+\delta\), \(r_N=\log(N/(N-2))\), and fix \(N\). At \(t=0\),
\[
 F'_{N,1+\delta}(0)=N(N-2)r_N\delta+O_N(\delta^2),
 \qquad F''_{N,1+\delta}(0)=-2N(N-2)+O_N(\delta).
\]
The exact \(\theta\) formula gives \(\theta=(r_N/2)\delta+O_N(\delta^2)\). Taylor's theorem uniformly for \(t=O_N(\delta)\) yields
\[
 F_{N,1+\delta}(t)=N(N-2)\left(r_N\delta t-t^2\right)+O_N(\delta^3).
\]
At \(t=\theta\), this gives \(F(\theta)=N(N-2)r_N^2\delta^2/4+O_N(\delta^3)\). To locate the *other* zero, substitute \(t=\delta v\): the normalized limiting quadratic is \(N(N-2)v(r_N-v)\). At any fixed \(0<v_-<r_N<v_+\), the function has opposite signs for small \(\delta\), and the unique positive-zero property traps \(\tau/\delta\) between \(v_-\) and \(v_+\). This proves the stated \(o_N(\delta)\) cutoff accuracy. Dividing the peak by \(N\) gives the norm expansion.

**Large spectral power.** Fix \(N\) and let \(q=N/(N-2)>1\). At the peak, \(\theta_{N,s}=(s-1)\log q/((N-2)^s(q^s-1))\). Thus \((N-2)^s\theta\to0\), whereas \(N^s\theta=(s-1)\log q/(1-q^{-s})\to\infty\). Therefore \(a(\theta)\to1\), \(b(\theta)\to0\), and \(F(\theta)\to N-2\). For the late cutoff write \(v=(N-2)^s t\). Its defining equation becomes \(N e^{-v}-(N-2)e^{-q^s v}-2=0\). For every fixed \(v>0\), this expression converges to \(N e^{-v}-2\), which changes sign at \(v=\log(N/2)>0\). Bracketing by any two fixed values on opposite sides and invoking the uniqueness of the positive root proves the limit.

## Verification
The self-contained Python 3 script `verify.py` performs exact-rational spectral projector and Laplacian-eigenvalue checks for all even \(4\le N\le16\), independently computes matrix exponentials of integer powers of \(L\) by a 55-term Taylor series, checks row sums and sharp norms across nine exponents and seven positive times, and brackets the unique positive cutoff for larger \(N\). On the stated run it passed 71,243 assertions. Numerical assertions are checks of examples, not substitutes for the complete analytic proof above. Run `python3 verify.py` from a directory containing that file.

## Relationship to prior work
Daners, Glück and Kennedy [1], especially their finite-dimensional Theorem 6.1, establish broad eventual-positivity criteria but not these graph-specific sharp norms, exact recovery and amplification times, nor the three scaling regimes. The published three-spectral-value barrier [2] establishes that such a semigroup has no gaps in its eventual positivity-time set; our monotonicity proof makes the cutoff and sharp norm quantitative in the spectrally powered graph family, including the critical exponent and simultaneous dimension limit. Abatangelo, Jarohs and Saldaña [3] study positive powers of continuous Laplacians via hypersingular integrals and boundary problems, not finite cocktail-party graph semigroup norms. Standard Laplacian spectrum identities for cocktail-party graphs are used as elementary input, not claimed novel. The new content is the complete, sharp endpoint amplification and recovery phase diagram, not the qualitative possibility of eventual positivity.

## Limitations
The result applies to complete graphs with a perfect matching deleted, with counting measure and unnormalized Laplacian. The explicit asymptotics hold only in the stated limits; the fixed-power dimension limit is not uniform in arbitrary varying spectral powers. No assertion is made about all strongly regular or arbitrary graphs. Existing literature may contain an equivalent graph-specific calculation under different terminology; historical priority remains provisional. Independent review has not been performed.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, first public arXiv v1 2015-11-29, arXiv:1511.09020, particularly Section 6.1, https://arxiv.org/abs/1511.09020 .

[2] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, 2026, publicly available research note, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-spectral-value-barrier-for-gaps-in-positivity-times-of-s--da21753d4271 .

[3] N. Abatangelo, S. Jarohs, A. Saldaña, *Positive powers of the Laplacian: from hypersingular integrals to boundary value problems*, arXiv:1709.00976, 2017, https://arxiv.org/abs/1709.00976 .
