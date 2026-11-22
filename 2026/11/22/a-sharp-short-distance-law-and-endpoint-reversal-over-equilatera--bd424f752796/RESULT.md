# A sharp short-distance law and endpoint reversal over equilateral bases in even-diameter Urysohn spaces

## Finding

Fix integers \(h\ge2\), \(n\ge1\). In the countable universal homogeneous metric space with positive distances \(1,\ldots,2h\), pointwise name an equilateral \(n\)-point base \(A\) whose mutual distances are \(2h\). Let \(T_s(n)\) be the number of complete types over \(A\) of ordered **distinct** new points \((x,y)\) with \(d(x,y)=s\), for \(1\le s\le2h\). These finite numbers do not depend on the choice of \(A\).

**Exact spectrum.** Define \(K_s(a,b)=1\) when \(|a-b|\le s\le a+b\), and \(0\) otherwise. Set \(J=\{h,\ldots,2h\}\), \(L=\{1,\ldots,h-1\}\), and
\[
\begin{aligned}
B_s&=\sum_{a,b\in J}K_s(a,b), & A_s(t)&=\sum_{b\in J}K_s(t,b),\\
P_s(t)&=\sum_{a=2h-t}^{2h}\sum_{b\in J}K_s(a,b), & Q_s(t,u)&=\sum_{a=2h-t}^{2h}\sum_{b=2h-u}^{2h}K_s(a,b),\\
E_s(t,u)&=\sum_{b=2h-u}^{2h}K_s(t,b).
\end{aligned}
\]
Then the complete all-distance, all-base-size formula is
\[
\begin{aligned}
T_s(n)={}&B_s^n+2n\sum_{t\in L}A_s(t)P_s(t)^{n-1}\\
&+n\sum_{t,u\in L}K_s(t,u)Q_s(t,u)^{n-1}\\
&+n(n-1)\sum_{t,u\in L}E_s(t,u)E_s(u,t)Q_s(t,u)^{n-2}.
\end{aligned}
\tag{1}
\]
The last sum is omitted when \(n=1\). All sums are finite and explicit in \(h,n,s\).

**Sharp rare-short-distance law.** Choose a complete ordered-pair type uniformly among all \(\sum_{s=1}^{2h}T_s(n)\) types. For each fixed \(h\ge2\),
\[
\Pr(d(x,y)<h)\sim\frac{1}{h+1}\left(1-\frac{2}{(h+1)^2}\right)^n\quad(n\to\infty).
\tag{2}
\]
Conditional on \(d(x,y)\ge h\), the \(h+1\) distances \(h,h+1,\ldots,2h\) are asymptotically equiprobable. More precisely, for every \(h\le s\le2h\),
\[
T_s(n)=(h+1)^{2n}+2nc_s[h(h+1)]^{n-1}+O_h(n^2h^{2n-2}),
\tag{3}
\]
where \(c_h=c_{2h}=h\) and \(c_s=h+1\) for \(h<s<2h\). Thus every interior upper distance has a strictly larger count than either endpoint for all sufficiently large \(n\).

**Finite-size endpoint reversal.** The order of the two endpoint channels reverses as the old equilateral base grows:
\[
T_h(1)-T_{2h}(1)=\frac{h(h-1)}2>0,
\qquad
T_h(n)-T_{2h}(n)<0\quad(n\ge h+1).
\tag{4}
\]
No uniqueness of the intermediate crossover is asserted in general. At diameter four (\(h=2\)), the exact formulas are
\[
\begin{aligned}
T_1(n)&=7^n+2n5^{n-1}+n4^{n-1},\\
T_2(n)&=9^n+4n6^{n-1}+n4^{n-1}+n(n-1)4^{n-2},\\
T_3(n)&=9^n+6n6^{n-1}+n(n-1)4^{n-1},\\
T_4(n)&=9^n+4n6^{n-1}+n(n-1)4^{n-1};
\end{aligned}
\tag{5}
\]
terms multiplied by \(n(n-1)\) are omitted at \(n=1\). In particular, \(T_2(n)-T_4(n)=n4^{n-2}(7-3n)\): the endpoint order changes precisely between \(n=2\) and \(n=3\).

## Assumptions and scope

The language has a binary relation for each integer distance in \(\{1,\ldots,2h\}\), and equality. Every finite metric with these distances embeds in the countable homogeneous universal metric space. Homogeneity identifies complete types over a finite pointwise-named base with isometry classes of finite labelled metric extensions fixing that base, so distinct distance tables contribute distinct types. Both new points are different from all named points and from each other; all distances in the tables are strictly positive. The case \(n=0\) is not included in formula (1), although trivially each mutual distance yields one type.

All asymptotic assertions fix \(h\) before \(n\to\infty\). Probabilities are on the finite **set of logical types**, not on an invariant spatial probability measure on the countable metric space.

## Proof

**1. Exceptional-coordinate classification.** If \(v=(d(x,a_i))_{i=1}^n\) describes one new point over the diameter-equilateral base, the only nontrivial triangle requirements are \(v_i+v_j\ge2h\); the difference inequalities are automatic because every entry lies between \(1\) and \(2h\). Hence at most one entry of \(v\) can lie below \(h\). If it has value \(t\in L\) at position \(i\), then each other entry must be in \(\{2h-t,\ldots,2h\}\). If no entry is below \(h\), every entry independently lies in \(J\). This classifies all admissible nonalgebraic one-point types.

**2. Exact pair decomposition.** A pair of such vectors \(v,w\) together with \(d(x,y)=s\) is realizable exactly when \(K_s(v_i,w_i)=1\) for every named point \(i\). Partition pairs by the low-coordinate locations of \(v,w\): neither has a low entry, exactly one has a low entry (two ordered choices), both have a low entry at the same position, or both have low entries at distinct positions. Their respective contributions are the four terms of (1). The first is \(B_s^n\). In the one-low case, the exceptional position has \(A_s(t)\) choices and each ordinary position has \(P_s(t)\); in the same-position case the exceptional pair contributes \(K_s(t,u)\) and each ordinary position contributes \(Q_s(t,u)\); in the distinct-position case the two exceptional positions give \(E_s(t,u)E_s(u,t)\) and remaining positions give \(Q_s(t,u)\). Multiplying by the ordered choices of positions proves (1) without overcounting. All resulting finite metrics embed, so there are no additional realizability restrictions.

**3. Lower-distance leading term.** For \(s<h\), since all entries in \(J\) sum to at least \(2h\),
\[
B_s=\#\{(a,b)\in J^2:|a-b|\le s\}=(h+1)(2s+1)-s(s+1).
\]
The sets counted by \(P_s(t)\) and \(Q_s(t,u)\) are strict subsets of the \(J^2\) band counted by \(B_s\), since they exclude the allowed pair \((h,h)\). Thus every exceptional-coordinate term has a strictly smaller exponential base than \(B_s\). For each fixed \(h\), \(T_s(n)=B_s^n(1+O_h(n^2\theta_{h,s}^n))\) for some \(\theta_{h,s}<1\). Since \(B_s\) is strictly increasing for \(1\le s<h\), the lower-distance sum is asymptotic to \(B_{h-1}^n=((h+1)^2-2)^n\).

**4. Upper-distance two layers.** For \(h\le s\le2h\), all pairs from \(J^2\) satisfy the triangle inequalities, as do all pairs whose entries range over \(\{2h-t,\ldots,2h\}\times J\) or over two such high subsets. Consequently \(B_s=(h+1)^2\), \(P_s(t)=(t+1)(h+1)\), and \(Q_s(t,u)=(t+1)(u+1)\). The largest one-low base occurs uniquely at \(t=h-1\), with value \(h(h+1)\), and its coefficient is \(A_s(h-1)=h\) at \(s=h,2h\) and \(h+1\) at intermediate \(s\). All other one-low bases are at most \((h-1)(h+1)=h^2-1\), while all two-low bases are at most \(h^2\). Formula (3) follows, with a uniform error bound over the finitely many \(s\). Summing the \(h+1\) upper channels and applying Step 3 proves (2) and asymptotic conditional equiprobability. The difference of the leading second-layer coefficients proves eventual strict interior advantage.

**5. Endpoint reversal.** For \(s=h\) and \(s=2h\), the one-low coefficients coincide for every \(t\in L\), namely \(A_h(t)=A_{2h}(t)=t+1\); the no-low terms coincide as well. In the two-low same-position term, \(K_h(t,u)=\mathbf1_{t+u\ge h}\) and \(K_{2h}(t,u)=0\). In the two-low distinct-position term, the two endpoint counts per exceptional coordinate are respectively \(q=\max(0,t+u-h+1)\) and \(v+1\), where \(v=\min(t,u)\). Put \(p=(t+1)(u+1)\) and \(b=(v+1)^2-q^2>0\). Their exact difference is
\[
T_h(n)-T_{2h}(n)=n\sum_{t,u\in L}\mathbf1_{t+u\ge h}p^{n-1}
-n(n-1)\sum_{t,u\in L}b p^{n-2},
\tag{6}
\]
with the second sum absent when \(n=1\). At \(n=1\), the number of pairs \((t,u)\in L^2\) with \(t+u\ge h\) is \(h(h-1)/2\). For every such pair, writing \(w=\max(t,u)\le h-1\) gives \(q\le v\), and hence
\[
b\ge2v+1>v+1\ge\frac{(v+1)(w+1)}h=\frac ph.
\]
If \(t+u<h\), the first contribution vanishes and the second is strictly negative. Therefore each summand in (6) is strictly negative when \(n-1\ge h\), proving (4). Substituting \(h=2\) in (1) yields (5) and the exact single crossover.

## Verification

The included `CHECKER.py` uses two independent implementations: direct enumeration of ordered distance vectors with all triangle inequalities, and the analytic zero/one/two-low-coordinate decomposition. It checks all distance channels for \((h,n)\) up to \((2,4)\), \((3,3)\), \((4,3)\), and \((5,2)\): 78 complete direct comparisons. It independently compares the endpoint difference formula to the upper-channel formula for 66 parameter pairs, tests the endpoint sign in the proved region, and checks diameter-four closed forms through \(n=9\). The saved output is in `CHECKER_OUTPUT.txt`; its last line is `ALL_METRIC_TYPE_CHECKS_PASS`.

These finite checks are corroborative only. The all-parameter proof is the exceptional-coordinate partition and the inequalities above, not extrapolation from computation. Reproduce with `python3 CHECKER.py` from the same directory. Python standard library only.

## Relationship to prior work

Sauer's 2010 work develops finite-distance Urysohn spaces and the Katětov one-point-extension criterion. The criterion is used here as background; its indivisibility theorem and orbit structure do not give an exact ordered-pair spectrum over growing equilateral bases. Mubayi and Terry's February 2015 paper establishes that nearly all *globally labelled finite metric spaces* with even diameter use only distances in the upper half, and proves an associated zero-one law. The present type-space distribution fixes a diameter-equilateral old base and counts extensions by just two new points; neither its exact decay constant nor its reversal law follows from the global random-metric result. Related calculations for the three-distance case and one-point graph-metric type polynomials concern distinct alphabets or arities and do not establish the all-even-diameter formula.

## Limitations

This result is restricted to even maximum distance \(2h\), integer distances, diameter-equilateral pointwise-named bases, and ordered pairs of distinct new points. Odd maximum distances, arbitrary old metric bases, higher tuple arities, and joint growth of \(h,n\) are not treated. The endpoint reversal theorem guarantees a sign change, not a unique crossover for general \(h\). Historical priority under other terminology is not exhaustively established. No independent mathematical audit has been carried out.

## References

- Norbert Sauer, *Partitions of metric spaces with finite distance sets*, arXiv:1010.4212, publicly posted 20 October 2010, Sections 1–2. https://arxiv.org/abs/1010.4212
- Dhruv Mubayi and Caroline Terry, *Discrete metric spaces: structure, enumeration, and 0-1 laws*, arXiv:1502.01212, first posted 4 February 2015, especially Sections 1–3 and 6. https://arxiv.org/abs/1502.01212
