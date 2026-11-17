# Sharp zero-moment discrete Sobolev limit and two-lobe rigidity

## Finding

The extra vanishing-moment condition changes the sharp first-difference discrete \(\ell^1\)-to-\(\ell^2\) Sobolev constant by a factor of two at leading order, and rigidly selects two opposite parabolic lobes in every asymptotically extremizing sequence.

For each integer \(d\ge2\), define
\[
K_d=\max_{\substack{a\in\mathbb R^d\setminus\{0\}\\\sum_{i=1}^d a_i=0}}
\frac{\sum_{i=1}^d|a_i|}{\left(\sum_{i=1}^{d+1}(a_i-a_{i-1})^2\right)^{1/2}},
\quad a_0=a_{d+1}=0.
\]
The exact asymptotic constant is
\[
\boxed{\lim_{d\to\infty}\frac{K_d}{(d+1)^{3/2}}=\frac1{\sqrt{48}}.}
\]
For every \(d\ge2\), the finite-size upper bound is
\[
\boxed{K_d\le\frac{(d+1)^{3/2}}{\sqrt{48}}+\frac{\sqrt{d+1}}4.}
\]
For \(d=2k\), where \(k\ge1\) is an integer, the explicit finite-size lower bound is
\[
\boxed{K_{2k}^2\ge\frac{k(k+1)(k^2+k+1)}{3(2k+1)}.}
\]

The limiting statement has an equality-rigidity strengthening. Put
\[
v(t)=\begin{cases}
\dfrac{t(\frac12-t)}2,&0\le t\le\frac12,\\[2pt]
-\dfrac{(t-\frac12)(1-t)}2,&\frac12\le t\le1,
\end{cases}
\qquad u_*(t)=\sqrt{48}\,v(t).
\]
For any sequence of nonzero, real, zero-sum vectors \(a^{(d)}\) satisfying
\[
\frac{\sum_i|a_i^{(d)}|}{K_d\sqrt{E_d(a^{(d)})}}\longrightarrow1,
\qquad E_d(a)=\sum_{i=1}^{d+1}(a_i-a_{i-1})^2,
\]
let \(U_d\) be the continuous piecewise-linear interpolant with nodes \(U_d(i/(d+1))=a_i^{(d)}\), including the zero boundary nodes. Set \(u_d=U_d/\sqrt{(d+1)E_d(a^{(d)})}\). Then
\[
\boxed{\min_{\varepsilon\in\{-1,1\}}
\|u_d'-\varepsilon u_*'\|_{L^2(0,1)}\longrightarrow0.}
\]
The conclusion includes convergence in the \(H_0^1\) topology. No rate of this rigidity convergence is claimed.

## Assumptions and scope

All vector entries are real; sign changes are essential. The energy includes both zero-extension boundary differences. The coefficient-sum constraint is literal \(\sum_i a_i=0\) and is equivalent to a root at \(1\) of the generating polynomial \(\sum_{i=1}^d a_i z^{i-1}\). The finite-dimensional maximum exists by compactness of the unit-energy sphere in the zero-sum hyperplane. The exact asymptotic is as \(d\to\infty\) with no additional parameters. Complex coefficients, higher-order differences, additional vanishing moments and sharp formulas for all finite dimensions are outside the claim.

## Proof

**1. Sharp real continuous zero-moment lemma.** For every real \(u\in H_0^1(0,1)\) with \(\int_0^1u=0\),
\[
\int_0^1|u|\le\frac1{\sqrt{48}}\left(\int_0^1|u'|^2\right)^{1/2}.
\tag{1}
\]
Equality for a nonzero \(u\) holds precisely for nonzero scalar multiples of \(v\), as defined above. Indeed, let \(M=\int u_+=\int u_-\), \(p=|\{u>0\}|\), and \(n=|\{u<0\}|\). Unless \(u=0\), both \(p,n>0\), and \(p+n\le1\). On each connected positivity interval \(I\) of length \(\ell\), the Dirichlet Green function \(w_I(x)=(x-\inf I)(\sup I-x)/2\) obeys \(-w_I''=1\) and \(\int_I|w_I'|^2=\ell^3/12\). Integration by parts and Cauchy--Schwarz give
\[
\left(\int_Iu_+\right)^2\le\frac{\ell^3}{12}\int_I|u_+'|^2.
\]
Summing over all disjoint positivity intervals, applying Cauchy--Schwarz, and using \(\sum_I\ell_I^3\le(\sum_I\ell_I)^3=p^3\), yields \(M^2\le(p^3/12)\int|u_+'|^2\). Similarly \(M^2\le(n^3/12)\int|u_-'|^2\). As derivatives vanish almost everywhere on the zero set,
\[
\int|u'|^2\ge12M^2(p^{-3}+n^{-3})\ge192M^2.
\]
The last inequality follows from \(p+n\le1\) and strict convexity of \(t\mapsto t^{-3}\), with equality only at \(p=n=1/2\). Since \(\int|u|=2M\), this proves (1). Equality requires each sign set to be one interval, their lengths both \(1/2\), and each lobe to be a positive multiple of its Green parabola. Equal positive and negative masses give the same multiple, and only the two possible orders remain: \(v\) and \(-v\). Direct integration gives \(\int|v'|^2=\int|v|=1/48\), so \(\|u_*'\|_2=1\) and \(\int|u_*|=1/\sqrt{48}\).

**2. Universal discrete upper bound.** Let \(N=d+1\), \(h=1/N\), and interpolate the vector linearly as \(U\in H_0^1(0,1)\). Then
\[
\int_0^1U=h\sum_{i=1}^d a_i=0,
\qquad \int_0^1|U'|^2=N E_d(a).
\]
On one mesh interval with endpoint values \(x,y\), the absolute-value trapezoidal error
\[
\frac h2(|x|+|y|)-\int_{\text{interval}}|U|
\]
is zero for same-sign endpoints, and equals \(h|xy|/(|x|+|y|)\) for opposite signs (zero when either endpoint is zero). Because \(4|xy|\le(|x|+|y|)^2=|x-y|^2\) for opposite signs, it is at most \(h|x-y|/4\). Summing yields
\[
0\le h\sum_{i=1}^d|a_i|-\int|U|
\le\frac h4\sum_{i=1}^{N}|a_i-a_{i-1}|.
\]
Apply (1), multiply by \(N\), and use \(\sum_i|a_i-a_{i-1}|\le\sqrt N\sqrt{E_d(a)}\). This establishes the finite bound in the finding.

**3. Explicit even-dimensional lower witnesses.** Fix \(k\ge1\), \(d=2k\), \(N=2k+1\). For \(1\le i\le k\), put
\[
b_i=\frac{i[2k^2+2k+1-(2k+1)i]}{2(2k+1)},
\qquad b_{N-i}=-b_i,
\qquad b_0=b_N=0.
\]
All first-half entries are positive; the vector is antisymmetric and has zero sum. Direct second differences give
\[
2b_i-b_{i-1}-b_{i+1}=\begin{cases}1,&1\le i\le k,\\-1,&k<i\le2k.\end{cases}
\]
Multiply by \(b_i\) and sum. Dirichlet summation by parts implies
\[
E_{2k}(b)=\sum_{i=1}^{2k}|b_i|
=\frac{k(k+1)(k^2+k+1)}{3(2k+1)}.
\]
This supplies the stated lower bound for \(K_{2k}^2\). Its quotient by \((2k+1)^3\) converges to \(1/48\). Appending a zero coordinate leaves both the energy and numerator unchanged and preserves the zero sum, so \(K_{d+1}\ge K_d\). This transfers the matching lower asymptotic to odd dimensions. Combining with the finite upper bound completes the limit.

**4. Near-extremizer rigidity.** Normalize an asymptotically extremizing sequence as in the finding. Then \(\|u_d'\|_2=1\), \(\int u_d=0\), and the trapezoidal estimate, applied to \(u_d\), gives
\[
0\le\frac{\sum_i|a_i^{(d)}|}{N^{3/2}\sqrt{E_d(a^{(d)})}}-\int|u_d|\le\frac1{4N}.
\]
The already established sharp limit forces \(\int|u_d|\to1/\sqrt{48}\). Boundedness in \(H_0^1(0,1)\) gives weakly convergent subsequences; in one dimension these are uniformly convergent after subsubselection by the estimate \(|u_d(t)-u_d(s)|\le|t-s|^{1/2}\). Their limits retain zero integral and absolute integral \(1/\sqrt{48}\), and have derivative energy at most \(1\) by weak lower semicontinuity. The sharp inequality (1) forces derivative energy exactly \(1\), hence each limit is \(u_*\) or \(-u_*\). Weak convergence of derivatives plus convergence of their Hilbert norms yields strong \(L^2\) convergence. A subsequence contradiction proves convergence in distance to the two-element extremizer set for the whole sequence.

## Verification

All boundary conventions and normalization factors are specified above. Running `python3 checker.py` performs 3,037 exact rational assertions: integer difference equations and energy identities for the even witnesses at \(1\le k\le30\); exhaustive sign-dual optimizations for \(2\le d\le10\); and exact inverses of the discrete Dirichlet tridiagonal matrix for \(2\le d\le20\). The checker uses only Python standard-library exact fractions. Those finite tests are diagnostic; the proofs of (1), the all-dimensional bounds, the limit and the rigidity statement are analytical.

## Relationship to prior work

Hindov, Nitzan, Olsen and Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (first submitted October 13, 2026), prove the unrestricted first-difference sharp constant
\[
C_{1,d}=\sqrt{\frac{d(d+1)(d+2)}{12}},
\]
with one-sign Landau polynomial extremizers. The present zero-sum hyperplane excludes all such nonzero one-sign extremizers and exhibits instead half the unrestricted leading coefficient, plus a two-lobe unique asymptotic profile. The new result neither claims nor rederives their exact unrestricted finite constants.

The same authors' 2025 *A sharp higher order Sobolev embedding*, DOI 10.1112/mtk.70012, determines the corresponding unrestricted real continuous inequality via a one-sign Landau kernel. The additional zero-integral constraint and its sharp signed two-lobe equality analysis here are distinct. Standard single-sign Dirichlet Green inequalities are used as ingredients, not claimed as novel.

## Limitations

The constant \(1/\sqrt{48}\) is an **asymptotic** sharp constant, not a formula for every finite \(d\). The explicit even-dimensional sequences certify lower bounds but their global finite-dimensional optimality is not asserted. The result is real only; complex-valued cancellation may have different geometry. No quantitative stability rate, higher-difference analogue, or general multi-moment extension is proved. Published-priority uncertainty remains for alternative formulations of zero-mean one-dimensional sharp Sobolev inequalities.

## References

1. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1, October 13, 2026. https://arxiv.org/html/2610.19010v1
2. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp higher order Sobolev embedding*, Mathematika **71** (2025), e70012, DOI:10.1112/mtk.70012. https://doi.org/10.1112/mtk.70012
