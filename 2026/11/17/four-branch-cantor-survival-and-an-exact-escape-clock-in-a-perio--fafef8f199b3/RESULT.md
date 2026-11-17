# Four-branch Cantor survival and an exact escape clock in a periodically thresholded neuron map

## Finding
Consider the period-two threshold neuron recurrence
\[
x_{n+1}=\beta_n x_n-g(x_n),\qquad
\beta_{2j}=a,\quad \beta_{2j+1}=b,\qquad
 g(x)=\begin{cases}1,&x\geq0,\\-1,&x<0.\end{cases}
\]
For unequal positive coefficients \(a,b\) in the open cone
\[
\boxed{b(a-1)>2,\qquad a(b-1)>2},
\]
put \(\Lambda=ab\), \(T=(b+1)/(\Lambda-1)\), and \(I=[-T,T]\). Then \(\Lambda>4\), and the set \(K\) of *all* initial values giving bounded forward trajectories is a compact, zero-length, four-branch Cantor repeller contained in \(I\). The even-time map restricted to \(K\) is topologically conjugate to the full one-sided shift on four symbols, and
\[
\boxed{\dim_{\rm H} K=\frac{\log 4}{\log(ab)}.}
\]
If \(x_0\) is uniformly distributed on \(I\), the probability of remaining in \(I\) through the first \(n\) complete two-step returns is *exactly*
\[
\boxed{\Pr\{x_{2j}\in I\text{ for }0\leq j\leq n\}=\left(\frac4{ab}\right)^n,\qquad n=0,1,2,\ldots.}
\]
Thus the first two-step exit time \(N=\min\{n\geq1:x_{2n}\notin I\}\) is geometric: \(\Pr(N>n)=(4/(ab))^n\) for integers \(n\ge0\). Every exited trajectory subsequently diverges to one of the infinities; for every \(x_0\in K\), the entire trajectory remains bounded. The precise result holds for all real initial conditions, including the threshold convention \(g(0)=1\); other conventions with \(g(0)\in\{-1,1\}\) yield the identical bounded set and survival law.

## Assumptions and scope
The coefficients are fixed real numbers \(a,b>0\), with \(a\ne b\), satisfying the two strict inequalities above. The recurrence starts at even time \(n=0\). Its first return \(F(x)=x_2\) has domain the whole real line with the stated convention. We count one *return* as two ordinary neuron updates. The interval \(I\) is determined by the two exterior repelling period-two orbits. The exact escape probability uses normalized Lebesgue measure on \(I\), not an invariant measure on \(K\). No assertion is made outside the parameter cone or for a stochastic perturbation of the recurrence.

## Proof
**1. Four affine branches.** Direct substitution gives, away from the three switching points,
\[
F(x)=\begin{cases}
\Lambda x+b+1,&x<-1/a,\\
\Lambda x+b-1,&-1/a<x<0,\\
\Lambda x+1-b,&0<x<1/a,\\
\Lambda x-b-1,&x>1/a.
\end{cases}
\]
The two conditions are exactly equivalent to \(T<1\) and \(T<b-1\), respectively. They imply \(a,b>1\) and, as shown in Step 3, \(\Lambda>4\). For each \(y\in I\), the four affine inverse branches are
\[
\begin{aligned}
\psi_1(y)&=(y-b-1)/\Lambda,&\psi_2(y)&=(y-b+1)/\Lambda,\\
\psi_3(y)&=(y+b-1)/\Lambda,&\psi_4(y)&=(y+b+1)/\Lambda.
\end{aligned}
\]
The inequalities \(T<1\) and \(T<b-1\) show that \(\psi_1(I)\subset[-T,-1/a)\), \(\psi_2(I)\subset(-1/a,0)\), \(\psi_3(I)\subset(0,1/a)\), and \(\psi_4(I)\subset(1/a,T]\). The first and fourth images contain the left and right endpoints of \(I\), respectively. All four compact images are pairwise disjoint, and \(F\circ\psi_i\) is the identity on \(I\). At the switching points \(-1/a,0,1/a\), either one-sided threshold convention sends the point outside \(I\) in one return, since \(T<\min(1,b-1)\). Therefore these points never belong to a survivor cylinder, and do not alter the argument.

**2. Precisely which orbits stay bounded.** Since \(\Lambda>1\), the two outer affine branches have fixed endpoints \(\pm T\). If an even iterate lies strictly above \(T\), then all later even iterates satisfy \(F(x)-T=\Lambda(x-T)\) and diverge to \(+\infty\); the analogous statement holds below \(-T\). Consequently an orbit is bounded precisely when all its even iterates remain in \(I\). The odd iterates of such an orbit are bounded because \(|x_{2j+1}|\leq aT+1\). Define
\[
S_n=\{x\in I:F^j(x)\in I\text{ for all }0\leq j\leq n\},\qquad K=\bigcap_{n\geq0}S_n.
\]
Since every preimage of \(I\) inside \(I\) falls in one of the four valid branch intervals, we have the disjoint cylinder recursion
\[
S_0=I,\qquad S_n=\bigcup_{i=1}^4\psi_i(S_{n-1}).
\]
Thus \(S_n\) is a disjoint union of \(4^n\) closed intervals, each of length \(2T\Lambda^{-n}\).

**3. Cantor structure and dimension.** The four similarities have the identical contraction ratio \(1/\Lambda\). The strict gap between distinct compact images gives the strong separation property. Their total length is \(4|I|/\Lambda<|I|\), hence \(\Lambda>4\). It follows from elementary nested-cylinder coding that every infinite four-symbol sequence specifies one point in \(K\), and no two sequences give the same point. Removing the first symbol under \(F\) gives the one-sided full four-shift. The similarity dimension satisfies \(4\Lambda^{-s}=1\); standard separated self-similar cylinder covers give the upper bound \(\dim_H K\le s\), while the equal-weight cylinder measure and positive gaps give the mass-distribution lower bound \(\dim_H K\ge s\). Therefore \(\dim_H K=\log4/\log\Lambda\in(0,1)\), and \(K\) has Lebesgue measure zero. The nested construction also makes \(K\) perfect, nowhere dense and totally disconnected.

**4. Exact survivor and exit law.** The cylinder lengths in Step 2 give
\[
\frac{|S_n|}{|I|}=\frac{4^n\,2T\Lambda^{-n}}{2T}
=\left(\frac4\Lambda\right)^n.
\]
This is the probability of surviving \(n\) complete returns under the stated uniform initial distribution. Since the sets \(S_n\) are nested, \(\Pr(N>n)=|S_n|/|I|\), and hence \(\Pr(N=n)=(1-4/\Lambda)(4/\Lambda)^{n-1}\) for integers \(n\ge1\). Every point not in \(K\) exits after finitely many returns, whence Step 2 gives divergence. This completes the proof.

## Verification
Run `python checker.py` in a directory containing the included source file. The standard-library checker performs exact-rational tests for three parameter pairs, verifies all four inverse-branch images lie in their prescribed switching intervals, checks the exact finite-cylinder lengths through four returns, and cross-checks one interior point from each inverse branch against the two-step recurrence. These finite tests do not prove the infinite Cantor or probability claims; Steps 1–4 do.

For \(a=5/2\), \(b=23/10\), the exact quantities are \(\Lambda=23/4\), \(T=66/95\), and \(\Pr(N>n)=(16/23)^n\), while \(\dim_H K=\log4/\log(23/4)\approx0.7925305718\).

## Relationship to prior work
Bula and Radin's 2023 period-two paper establishes the basic recurrence and two outer repelling cycles (Theorem 1), proves divergence for starts outside \(I\) (Theorem 3), and proves an invariant/attracting interval on the opposite side of the inequalities (Theorems 4 and 6). The bounded-set fractal structure and exact escape law here concern the strict high-expansion region \(b(a-1)>2\), \(a(b-1)>2\), not the interval-attracting region treated there. Their earlier 2020 paper concerns periodic and eventually periodic solutions and does not establish this model-specific high-expansion survivor dimension or exact return-time distribution. The dimension argument uses standard strong-separation self-similar-set theory, without claiming that generic theorem as new.

## Limitations
The exact statements require both strict inequalities and period-two deterministic coefficients. No classification is asserted at the inequality boundaries or in intermediate parameter bands, where fewer than four full inverse branches may survive. The uniform-in-\(I\) escape distribution is not an invariant physical measure, and the geometric law counts two-step returns rather than single neuron updates. The original source leaves \(g(0)\) unspecified; either sign convention is harmless for this survivor because the switching points exit immediately. A 2015 earlier paper on the same recurrence was accessible through abstract and later authoritative citations, but its full text was not independently inspected; a previously unindexed equivalent statement cannot be ruled out. Independent scientific validation has not been performed.

## References
1. I. Bula and M. A. Radin, *Chaotic single neuron model with periodic coefficients with period two*, Nonlinear Analysis: Modelling and Control 29(1), 111–123; first published online 2023-12-13. DOI: https://doi.org/10.15388/namc.2024.29.33766 . Full text: https://zurnalai.vu.lt/nonlinear-analysis/article/download/33766/32339/86114 .
2. I. Bula and M. A. Radin, *Eventually periodic solutions of single neuron model*, Nonlinear Analysis: Modelling and Control 25(6), 903–918, first published 2020-11-01. DOI: https://doi.org/10.15388/namc.2020.25.20555 . Full text: https://www.journals.vu.lt/nonlinear-analysis/article/download/20555/20005/37053 .
3. I. Bula and M. A. Radin, *Periodic orbits of a neuron model with periodic internal decay rate*, Applied Mathematics and Computation 266, 293–303 (2015). DOI: https://doi.org/10.1016/j.amc.2015.05.097 . Earlier periodic-orbit study; full text not inspected.
