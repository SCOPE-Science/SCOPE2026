# Two-height return towers and bounded physical-time clocks on translated-cone caps

## Finding

The polygonal invariant curves called \(n\)-stepped caps in Cockram–Ashwin–Rodrigues carry an explicitly defined four-interval exchange. For every integer \(n\geq1\) and positive \(L,\eta\), this exchange is an exact two-tower suspension of a circle rotation, with **first-return heights** \(2\) and \(4n+1\), and with a uniformly bounded cumulative discrepancy in original iteration time.

Put \(A=L+\eta\) and \(S=2L+(4n+1)\eta\). The induced first return to \(B=[0,A)\) is
\[
R(x)=\begin{cases}x+L,&0\leq x<\eta,\\x-\eta,&\eta\leq x<A,\end{cases}
\qquad
\tau(x)=\begin{cases}4n+1,&0\leq x<\eta,\\2,&\eta\leq x<A.\end{cases}
\]
For \(x\in B\), define \(x_k=R^k(x)\), the number \(H_k\) of excursions of height \(4n+1\) among the first \(k\) returns, and \(t_k\), the corresponding number of original-map iterations. **For every \(k\geq1\) and every \(x\in B\)**,
\[
H_k=k-\left\lfloor\frac{x+kL}{A}\right\rfloor,
\qquad
 t_k=2k+(4n-1)H_k
      =\frac{S}{A}k+\frac{4n-1}{A}(x_k-x).
\]
Consequently \(|H_k-k\eta/A|<1\) and \(|t_k-kS/A|<4n-1\), uniformly over all parameters and all return counts. In particular, there is **no growing return-clock variance**, even when the rotation is irrational.

More precisely, when \(x\) is uniform on \(B\), \(H_k\) has the exact two-point law
\[
\mathbb P(H_k=\lfloor k\eta/A\rfloor)=1-\beta_k,
\quad
\mathbb P(H_k=\lfloor k\eta/A\rfloor+1)=\beta_k,
\qquad \beta_k=\{k\eta/A\};
\]
when \(\beta_k=0\), the latter probability is zero. Thus
\[
\mathbb E[t_k]=kS/A,
\qquad
\operatorname{Var}(t_k)=(4n-1)^2\beta_k(1-\beta_k)
\leq(4n-1)^2/4.
\]
A single excursion has mean \(S/A\) and variance \((4n-1)^2L\eta/A^2\) under uniform base sampling; these excursion lengths are generally **not independent**.

If \(L/\eta=u/v\) with coprime positive integers \(u,v\), every point of the half-open four-IET has **least original-map period**
\[
P_{n;u,v}=2u+(4n+1)v.
\]
For each fixed \(n\) and cap angle \(0<\phi<\pi/2\), all coprime pairs \((u,v)\) occur for admissible cone-map parameters, and hence the complete set of least periods attained as that parameter varies is
\[
\big\{\,2u+(4n+1)v:\ u,v\in\mathbb N,\ \gcd(u,v)=1\,\big\}.
\]
For irrational \(L/\eta\), all regular cap trajectories are aperiodic; the long-excursion indicator is a balanced Sturmian coding of an irrational rotation. Its frequencies are \(\eta/A\) and \(L/A\), with exact bounded finite-time errors above.

## Assumptions and scope

Fix \(n\ge1\), \(L>0\), and \(\eta>0\), and partition \(I=[0,S)\) into four half-open intervals:
\[
\begin{aligned}
I_0&=[0,L+\eta),\\
I_1&=[L+\eta,L+(2n+1)\eta),\\
I_2&=[L+(2n+1)\eta,L+(4n+1)\eta),\\
I_3&=[L+(4n+1)\eta,S).
\end{aligned}
\]
On these pieces define the invertible interval exchange
\[
T(x)=\begin{cases}
x+L+4n\eta,&x\in I_0,\\
x+(2n-1)\eta,&x\in I_1,\\
x-(2n+1)\eta,&x\in I_2,\\
x-L-(4n+1)\eta,&x\in I_3.
\end{cases}
\]
This is the precise four-IET in Section 3.2 of the first-public arXiv version of the cited work; its embedding into a translated-cone exchange is established there. For the geometric statement, normalize the cone translation parameter to \(\rho=1\), take \(\eta=1-\lambda\), and put \(L=\lambda-2n(1-\lambda)(1+\cos\phi)>0\), with \(0<\lambda<1\), \(0<\phi<\pi/2\). The semiconjugate polygonal dynamics agrees on the regular set; endpoints, where planar branch assignment may be ambiguous, are excluded from that geometric assertion. The algebraic half-open IET theorem holds on all of \(I\).

All probabilities below refer to normalized **Lebesgue measure in the curve parameter \(x\)**, not to planar area or unweighted Euclidean arclength on the polygon. The induced base distribution is normalized Lebesgue measure on \(B=I_0\). The symbols \(t_k\) count iterates of \(T\), equivalently iterates of the planar map on the regular embedded curve.

## Proof

**1. Exact two return corridors.** If \(\eta\leq x<L+\eta\), then \(T(x)=L+(4n+1)\eta+(x-\eta)\) belongs to \(I_3\), and \(T^2(x)=x-\eta\in I_0\). The first-return time is exactly \(2\).

If \(0\leq x<\eta\), write the outside states as \(L+j\eta+x\). The first state after leaving \(I_0\) corresponds to \(j=4n\). For \(1\leq j\leq2n\) the next translation updates \(j\) to \(j+2n-1\); for \(2n+1\leq j\leq4n\) it updates \(j\) to \(j-(2n+1)\). For the nonzero indices, this is adding \(2n-1\) modulo \(4n\), since the two formulas differ by \(4n\). As \(\gcd(2n-1,4n)=1\), the successive indices visit each value \(1,\dots,4n\) exactly once before reaching \(j=0\). No earlier state is in \(I_0\), while the terminal state is \(L+x\in I_0\). Counting the initial move and the following \(4n\) moves gives first-return time \(4n+1\), proving both branch formulas.

The resulting towers comprise translates of \([\eta,A)\) at levels \(0,1\), and translates of \([0,\eta)\) at levels \(0,\ldots,4n\). The first-return property and invertibility ensure these levels are pairwise disjoint up to harmless boundary conventions. Their total length is \(2L+(4n+1)\eta=S\), so they exhaust \(I\) up to endpoints. This is an explicit two-column Rokhlin tower description and transfers all orbit-count statements on \(B\) to the full interval exchange.

**2. Rotation and exact clock identity.** Both return branches give \(R(x)=x+L\pmod A\), where the representative lies in \([0,A)\). A short excursion occurs exactly when this addition wraps around \(A\). Since \(0\leq x<A\), the number of wraps among the first \(k\) additions is \(\lfloor(x+kL)/A\rfloor\). Subtracting this count from \(k\) gives the formula for \(H_k\). Each long excursion costs \(4n+1\) iterates and each short one costs \(2\), proving the first formula for \(t_k\). The identity \(x_k=x+kL-A\lfloor(x+kL)/A\rfloor\) yields
\[
H_k-k\eta/A=(x_k-x)/A,
\quad
t_k-kS/A=(4n-1)(x_k-x)/A.
\]
Since \(-A<x_k-x<A\), both inequalities are strict for every \(k\) and \(x\). No ergodicity hypothesis is required.

**3. Exact two-point time law.** For fixed \(k\), write \(kL/A=m+\theta\), where \(m\) is integral and \(0\leq\theta<1\). A uniform \(x/A\) gives \(\lfloor(x+kL)/A\rfloor=m\) with probability \(1-\theta\), and \(m+1\) with probability \(\theta\). Hence \(H_k\) assumes only two consecutive integers with the claimed probabilities; they may also be expressed using \(\beta_k=\{k\eta/A\}\), since \(k\eta/A=k-kL/A\). Its expectation is \(k\eta/A\) and variance \(\theta(1-\theta)=\beta_k(1-\beta_k)\). The affine identity for \(t_k\) gives the stated mean and variance. The one-step distribution follows directly from the two base interval lengths \(\eta\) and \(L\).

**4. Exact rational least periods and realization.** If \(L/\eta=u/v\) in lowest terms, then the rotation increment is \(L/A=u/(u+v)\). Every \(x\in B\) has least return-map period \(u+v\). In one such orbit, the wrap count is exactly \(u\), so there are exactly \(v\) long excursions and \(u\) short excursions. Thus its least original-map period is \(2u+(4n+1)v\); a shorter full return would induce a shorter return to the same \(x\) under \(R\), impossible. Every point outside \(B\) lies on one of the two towers and has the same least period, because \(T\) is invertible.

To realize any coprime \((u,v)\) with prescribed \(n\) and \(\phi\), set \(c=2n(1+\cos\phi)+u/v\), \(\lambda=c/(1+c)\), \(\eta=1/(1+c)\), and \(L=(u/v)\eta\). All required inequalities hold, and the corresponding cap exists by the cited geometric construction. For irrational ratio, the induced rotation is aperiodic; every orbit of \(T\) meets \(B\), so the full exchange has no periodic points. The long-excursion coding is the standard mechanical coding of irrational rotation by the complementary interval, and its balance property already follows from the exact floor identity. The usual Sturmian-word terminology is pre-existing mathematics, not asserted as an independent discovery here.

## Verification

An accompanying standalone exact-rational checker evaluates the original four-piece map, not a numerical approximation, for \(54\) choices of \((n,L,\eta)\), including \(3{,}456\) base points and their repeated returns. It separately tests \(700\) rational least periods against iterates of the full four-piece map, and performs \(180\) exact checks of the cumulative clock mean and variance on rational uniform grids. Execute `python checker.py` with the Python standard library. These tests cover finite rational instances; they are not substituted for the proof of the parameter-uniform theorem.

## Relationship to prior work

Cockram, Ashwin and Rodrigues establish the geometric invariant curves and explicitly write the four-IET and its first-return two-IET. Those results are foundational hypotheses, **not** new claims here. Their discussion classifies periodic versus dense behavior by a rationality condition, without the full two-height tower, the exact two-point distribution of the \(k\)-return physical clock, its uniform \(O(1)\) fluctuation bound, or the original-time least-period spectrum across admissible parameters. The present quantitative return-time classification is derived by resolving the intermediate four-IET itinerary, rather than by treating a first-return step as one iteration. Mechanical sequences, balanced Sturmian coding and the basic theory of inducing are classical; they are applied here to the explicit cap-specific roof and original time. General rotation theorems explain the clock once the roof is known, and therefore the principal additional content is the exact identification and global realization of that roof for this geometric model.

## Limitations

The parameter regime requires \(n\ge1\), \(L>0\), and \(\eta>0\). Degenerate caps at \(L=0\) and zero translation gap \(\eta=0\) are excluded. The geometric interpretation is restricted to regular points of the embedded curve, not the ambient planar attractor or basin measures; only normalized curve-parameter Lebesgue measure is used. The finite numerical checks do not address arbitrary real parameters, which are instead handled analytically. No novelty claim is made for Sturmian balance or for the original embedding and first-return two-IET. General interval-exchange tower literature may contain equivalent implicit formulations, and publication-priority assessment remains subject to independent comparison.

## References

1. N. Cockram, P. Ashwin, A. Rodrigues, *Construction of invariant curves for some planar Piecewise Isometries*, arXiv:2312.17412v1, first posted 29 December 2023. Full text: https://arxiv.org/html/2312.17412v1 . Published as *Construction of invariant curves for some piecewise isometries*, **Dynamical Systems** 40 (2025), 602–625, DOI 10.1080/14689367.2025.2514193. The preprint's Section 3.2 supplies the exact four-IET and induced rotation.
2. M. Lothaire, *Algebraic Combinatorics on Words*, Chapter 2, “Sturmian Words,” Cambridge University Press, 2002. Standard background on mechanical words, rotation coding and balance.
3. J. Berstel, L. Vuillon, *Coding rotations on intervals*, arXiv:math/0106217 (2001). Background on rotation coding (not a claim concerning the specific translated-cone cap).
