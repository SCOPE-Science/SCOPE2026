# Sharp multiplier and basin-split realization of closed Milnor attractors by interval flows

## Finding
Let \(K\subset[0,1]\) be any nonempty closed set. For an orientation-preserving \(C^1\) diffeomorphism \(f\) fixing \(K\) pointwise and having \(K\) as its **Milnor global attractor** for Lebesgue measure, the possible prescribed derivative functions \(d=f'|_K\) are **exactly** the continuous functions \(d:K\to(0,1]\) satisfying
\[
 d(p)=1\quad\text{for every accumulation point }p\text{ of }K.
\]
Every admissible \(d\) is realized by the time-one map of a globally defined \(C^1\) vector field on \([0,1]\). There is additional independent control over the attraction basins and repelling multipliers. Namely, for **each bounded complementary interval** \(J=(a,b)\) of \(K\) (so \(a,b\in K\)), prescribe an arbitrary split point \(m_J\in(a,b)\) and a number \(\rho_J>1\). If the gaps form an infinite family, require only
\[
\lim_{\lvert J\rvert\to0}\rho_J=1,
\]
meaning that for every \(\varepsilon>0\) all sufficiently short gaps satisfy \(\lvert\rho_J-1\rvert<\varepsilon\). Then a realizing flow can be selected with **exactly one extra fixed point \(m_J\)** in each such gap, with \(f'(m_J)=\rho_J\), and with
\[
 \lim_{n\to\infty}f^n(x)=
 \begin{cases} a,&a<x<m_J,\\ b,&m_J<x<b.\end{cases}
\]
If \(K\) does not contain one or both endpoints of \([0,1]\), those ambient endpoints are the only additional fixed points in the outer complementary intervals, are repelling, and every other point of each outer interval approaches its endpoint in \(K\). Conversely, for any \(C^1\) realization with the displayed gap repellers, the condition \(\rho_J\to1\) along shrinking gaps is necessary. Thus the derivative and repeller prescriptions are sharp. No assertion is made about other interval maps not fixing \(K\) pointwise, about dimension two, or about \(C^2\) regularity.

## Assumptions and scope
The measure defining the Milnor global attractor is normalized Lebesgue measure. For a continuous map of a compact interval, \(\omega_f(x)\) is the set of forward subsequential limits. The Milnor global attractor is the smallest closed \(C\) for which \(\omega_f(x)\subseteq C\) for almost every \(x\). The theorem concerns orientation-preserving \(C^1\) diffeomorphisms of \([0,1]\) and, for existence, time-one maps of autonomous \(C^1\) flows. The derived set \(K'\) consists of accumulation points of \(K\). The function \(d\) is continuous on the relative topology of \(K\). Complementary gaps are disjoint, countably many, and for each \(\delta>0\) only finitely many have length at least \(\delta\). The prescribed split points may approach either gap endpoint at **any** rate, independently of the multipliers. There is no implicit lower bound on the split proportions.

## Proof
**1. Necessary fixed-point multipliers.** Suppose \(f\in\operatorname{Diff}^1_+([0,1])\) fixes \(K\) pointwise and has Milnor global attractor \(K\). Positivity and continuity of \(f'\) give a positive continuous function on \(K\). For \(p\in K'\), choose distinct \(q_j\in K\) approaching \(p\). Since \(f(q_j)=q_j\) and \(f(p)=p\), the difference quotients equal \(1\), so \(f'(p)=1\).

For an isolated \(p\in K\), suppose \(f'(p)>1\). Then in a sufficiently small interval around \(p\), \(f(x)-x\) has the sign of \(x-p\). No point other than \(p\) can converge to \(p\), because any orbit of an increasing interval homeomorphism is monotone and approaches a fixed point; such an orbit would have to move *toward* \(p\) in a punctured neighbourhood. Injectivity also excludes a finite-time hit from another point. Thus the set of initial points whose omega-limit contains \(p\) is the singleton \(\{p\}\), which has measure zero. Since \(p\) is isolated in \(K\), \(K\setminus\{p\}\) is closed. It would still have full basin, contradicting minimality of the Milnor global attractor. Hence \(f'(p)\le1\). This proves the necessity of the displayed conditions.

**2. Polynomial field on a bounded gap.** Let \(J=(a,b)\), let \(m=m_J\), write
\[
 A=-\log d(a)\ge0,\quad B=-\log d(b)\ge0,\quad R=\log\rho_J>0.
\]
For \(x\in[a,m]\), put \(L=m-a\) and \(s=(x-a)/L\), and define
\[
 v(x)=-L s(1-s)\bigl(A(1-s)+Rs\bigr).
\]
For \(x\in[m,b]\), put \(L=b-m\), \(s=(x-m)/L\), and define
\[
 v(x)=L s(1-s)\bigl(R(1-s)+Bs\bigr).
\]
These formulas vanish at \(a,m,b\) and have exact one-sided slopes
\[
 v'(a)=-A,\qquad v'(m-)=v'(m+)=R,\qquad v'(b)=-B.
\]
The field is negative on \((a,m)\) and positive on \((m,b)\), including the neutral cases \(A=0\) or \(B=0\). Its only zeros on \([a,b]\) are \(a,m,b\). The elementary polynomial derivatives satisfy a universal constant estimate
\[
 \sup_{x\in J}|v'(x)|\le C(A+B+R),
\]
with \(C\) independent of both the gap length and the split point. Thus arbitrarily asymmetric basin splits cause no derivative blow-up.

**3. Outer gaps and global \(C^1\) gluing.** Define \(v=0\) on \(K\). If \((0,a)\) is a complementary interval with \(a=\min K>0\), write \(L=a\), \(s=x/L\), \(B=-\log d(a)\) and set
\[
 v(x)=L s(1-s)\bigl((1-s)+Bs\bigr).
\]
This is positive on \((0,a)\), with derivatives \(v'(0)=1\) and \(v'(a)=-B\). If \((b,1)\) is an outer gap with \(b=\max K<1\), write \(L=1-b\), \(s=(x-b)/L\), \(A=-\log d(b)\), and set
\[
 v(x)=-L s(1-s)\bigl(A(1-s)+s\bigr).
\]
It is negative in the interior, with \(v'(b)=-A\) and \(v'(1)=1\). These are the only outer-gap zeros. If \(K=\{0\}\), \(K=\{1\}\), or \(K=[0,1]\), the same formulas (or \(v\equiv0\)) apply directly.

At each isolated point \(p\in K\), the adjacent polynomial pieces have the common derivative \(\log d(p)\), so the field is \(C^1\) there. At each \(p\in K'\), continuity of \(d\) and \(d(p)=1\) imply \(-\log d(q)\to0\) as \(q\in K\) approaches \(p\). The condition on \(\rho_J\) gives \(R_J\to0\) along shrinking gaps. The uniform derivative estimate in Step 2 then forces \(v'\to0\) through all small gaps near \(p\); only finitely many longer gaps exist, and their endpoint derivatives at \(p\) are zero. On \(K\), the field vanishes, and its difference quotient at every accumulation point is therefore zero by the mean value theorem applied between \(x\) and a nearby endpoint of its gap. Thus \(v'(p)=0\) and \(v'\) is continuous there. The finite outer gaps have no effect. In conclusion \(v\in C^1([0,1])\), with \(v'(p)=\log d(p)\) for all \(p\in K\). The field is globally Lipschitz and vanishes at \(0,1\), so its flow \(\Phi_t\) exists for all real \(t\) and preserves \([0,1]\).

**4. Exact dynamics and minimality.** Set \(f=\Phi_1\). Its derivative at every equilibrium \(q\) is \(f'(q)=\exp(v'(q))\), from the scalar variational equation. Hence the prescribed multipliers hold at every \(p\in K\) and \(m_J\). The sign pattern implies that points left of \(m_J\) monotonically converge to \(a\), those right of it to \(b\), and points in outer gaps converge to their sole \(K\)-endpoint. There is no other recurrent behaviour. Only the countably many \(m_J\) and possibly \(0,1\notin K\) have omega-limits outside \(K\). Consequently \(K\) has full Lebesgue basin.

To show minimality, take any proper closed subset \(C\subsetneq K\) and select \(p\in K\setminus C\) with a relative neighbourhood \(U\) disjoint from \(C\). If \(U\) meets \(\operatorname{int}K\), its positive-length subset of fixed points has omega-limits outside \(C\). Otherwise \(p\) lies on the boundary of \(K\). The endpoints in \(K\) of complementary gaps (including outer gaps where relevant) are dense in \(\partial K\): every neighbourhood of a boundary point contains a point outside \(K\), and a closest adjacent endpoint lies between that point and \(K\). Some such endpoint \(e\in U\) has a positive-length interval of points converging to \(e\), so \(C\) cannot have full basin. Hence no proper closed subset of \(K\) has full basin, and \(\Lambda(f)=K\).

**5. Sharpness of the shrinking-gap condition.** If infinitely many different bounded gaps \(J_k\) shrink in length, any selection \(m_{J_k}\in J_k\) has a subsequence converging to an accumulation point \(p\in K'\). For any \(C^1\) diffeomorphism fixing \(K\), Step 1 gives \(f'(p)=1\). Continuity then forces \(f'(m_{J_k})\to1\) (the conclusion holds for every sequence of shrinking gaps, by compactness). Thus \(\rho_J\to1\) is necessary if all prescribed repellers are to be realized.

## Verification
The complete construction is an explicit formula on each complementary interval; it needs no numerical root-finding, generic-position assumption, or finite approximation of \(K\). The accompanying standalone program `verify.py` symbolically checks the four gap-endpoint slope identities, tests positivity and negativity on rational meshes for neutral and hyperbolic endpoint choices, and checks uniform dimensionless derivative envelopes for sharply unequal split proportions and shrinking gap sizes. These finite checks do not establish the global \(C^1\) claim, which is proved in Step 3, or the Milnor minimality claim, proved in Step 4.

## Relationship to prior work
Hantáková and Mlíchová (2026, Section 4) construct homeomorphic realizations of every nonempty closed subset of a compact one-dimensional manifold, using interval sectors and monotone maps. The present assertion requires more: \(C^1\) differentiable time-one flow realizations with a *complete necessary-and-sufficient derivative profile on the prescribed attractor*, independently prescribed positions and unstable multipliers for one gap separator per bounded gap, and the sharp compatibility condition on those separators. The earlier topological realization does not imply any of these derivative data. Eynard-Bontemps and Navas (2019) study time-one flow embeddings and asymptotic distortion of interval diffeomorphisms; their general flow-embedding theory does not prescribe Milnor attractors, basin splits, or these joint equilibrium-multiplier data. Milnor (2006) gives the attractor framework, not the realization classification. The polynomial interpolation is elementary, but the combined global \(C^1\) compatibility, full-basin minimality and sharp spectral admissibility are the additional mathematical assertion.

## Limitations
The result is restricted to one-dimensional orientation-preserving diffeomorphisms fixing \(K\) pointwise. It uses \(C^1\) (not \(C^2\)) regularity; a higher-regularity prescription would impose extra Whitney-type compatibility at accumulation points. It does not realize arbitrary dynamics on \(K\), and it does not classify all maps with Milnor attractor \(K\). The time-one map can have repelling fixed points outside \(K\) on a Lebesgue-null exceptional set; thus \(K\) need not be a classical uniformly attracting set. Historical priority cannot be guaranteed by database search alone, particularly for basic one-dimensional smooth flow interpolation methods.

## References
1. J. Hantáková and M. Mlíchová, *Universal Realization of Milnor Attractors in Low Dimensions*, arXiv:2611.15353v1, first posted 11 November 2026. https://arxiv.org/html/2611.15353v1
2. H. Eynard-Bontemps and A. Navas, *Mather invariant, distortion, and conjugates for diffeomorphisms of the interval*, arXiv:1912.09305, first posted 19 December 2019. https://arxiv.org/abs/1912.09305
3. J. Milnor, *Attractors*, Scholarpedia 1(11):1815 (2006), doi:10.4249/scholarpedia.1815. https://www.scholarpedia.org/article/Attractors
