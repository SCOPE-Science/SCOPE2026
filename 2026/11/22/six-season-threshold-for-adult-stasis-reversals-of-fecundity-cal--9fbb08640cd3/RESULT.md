# Six-season threshold for adult-stasis reversals of fecundity-calendar growth rankings

## Finding
For the positive, two-stage, time-periodic population projection model
\[
 A(f)=\begin{pmatrix}0&f\\s&t\end{pmatrix},\qquad f>0,\quad 0<s<1,\quad 0<t<1,
\]
let a *calendar* of length \(n\) be a permutation of a fixed multiset of \(n\) fecundities, and let its per-season asymptotic growth factor be \(\rho(A(f_n)\cdots A(f_1))^{1/n}\).

**Sharp minimality theorem.** For every \(n\le5\), for any two calendars with the same fecundity multiset, the sign of their growth-factor difference is independent of both common maturation survival \(s\) and common adult retention \(t\), as long as both remain strictly positive. At \(n=6\) this rigidity fails, even with six distinct positive fecundities and both survivals in \((0,1)\). Specifically, for
\[
 \mathcal C=(1,2,3,4,5,6),\qquad \mathcal D=(1,2,4,3,5,6),
\]
the traces of their period products differ by exactly
\[
 T_{\mathcal C}-T_{\mathcal D}=s^2(7s-3t^2).
\]
Consequently, the first calendar has strictly higher growth for \(t<\sqrt{7s/3}\), ties at equality, and strictly lower growth for \(t>\sqrt{7s/3}\), whenever the indicated retention values are admissible. Choosing \(s=1/4\) gives the interior switch \(t_*=\sqrt{7/12}\), with trace gaps \(1/16\) at \(t=1/2\) and \(-17/400\) at \(t=9/10\).

## Assumptions and scope
The model has juvenile and adult stages. Every season uses the same fixed juvenile-to-adult survival \(s\) and fixed adult retention \(t\); only the per-adult fertility \(f_i\) changes. Reproduction produces juveniles from adults; all juveniles mature or leave the juvenile class within one season. The period repeats indefinitely. A comparison holds the *entire multiset* of fertility coefficients fixed and alters only its temporal permutation. The result compares linear low-density Floquet growth factors, not finite-time population counts or nonlinear carrying-capacity equilibria. All stated strict inequalities require \(s,t\in(0,1)\) and positive fecundities; degenerate zero-survival limits are excluded.

## Proof
**1. A cyclic independent-set identity.** For every integer \(n\ge2\), write \(P= A(f_n)\cdots A(f_1)\) and \(T=\operatorname{tr}P\). Expanding the trace by closed stage histories, a transition from an adult to a juvenile in season \(i\) contributes \(f_i\), and must be immediately followed by juvenile-to-adult maturation contributing \(s\). Two such adult-to-juvenile transitions cannot occur in cyclically consecutive seasons. All remaining transitions retain an adult and contribute \(t\). Conversely, each subset \(S\) of seasons without cyclically adjacent members produces exactly one compatible closed stage history. Therefore
\[
 T=\sum_{\substack{S\subseteq\{1,\ldots,n\}\\ S\cap(S+1\pmod n)=\varnothing}}
 s^{|S|}t^{n-2|S|}\prod_{i\in S}f_i.
\]
Here the empty product is one and \(S+1\pmod n\) denotes cyclic successor indices. This proof includes the two-season case, where the nonempty allowed subsets are the two singletons. The determinant is separately
\[
 \det P=(-s)^n\prod_{i=1}^n f_i,
\]
so it does not depend on calendar order.

**2. Trace ordering equals growth ordering.** A product of two matrices \(A(f)\) with positive \(f,s,t\) is strictly positive; hence so is \(P\) for \(n\ge2\). Its Perron eigenvalue is
\[
 \rho(P)=\frac{T+\sqrt{T^2-4\det P}}{2},
\]
with real, distinct eigenvalues (for positive \(2\times2\) matrices the discriminant is strictly positive). At a fixed determinant this expression is strictly increasing in \(T>0\), because its derivative is \(\tfrac12(1+T/\sqrt{T^2-4\det P})>0\). Since permutations have identical determinant, their Perron and per-season growth-factor orderings are exactly the trace orderings.

**3. Rigidity for at most five seasons.** The largest cyclically independent subset has size \(\lfloor n/2\rfloor\). For \(n=2,3\), the independent-set identity contains only terms of size zero and one, so all calendars tie. For \(n=4,5\), it contains terms of sizes zero, one and two. The size-zero contribution \(t^n\) and size-one contribution \(s t^{n-2}\sum_i f_i\) are independent of permutation. Therefore the trace difference between any two calendars takes the form
\[
 \Delta T=s^2t^{n-4}\Delta B,
\]
where \(\Delta B\) is the difference between their sums of \(f_i f_j\) over nonadjacent pairs of the cycle, and depends only on the two calendars. Since \(s^2t^{n-4}>0\), varying either survival cannot change its sign. This proves the stated universal rigidity for every \(n\le5\).

**4. The first reversal, at six seasons.** The size-three independent sets of a six-cycle are exactly the odd positions and the even positions. Thus
\[
 T=t^6+s t^4\sum_i f_i+s^2t^2
 \sum_{\substack{1\le i<j\le6\\i,j\text{ nonadjacent}}}f_i f_j
 +s^3(f_1f_3f_5+f_2f_4f_6).
\]
For an arbitrary calendar \((a,b,c,d,e,f)\) and its neighbor-swap calendar \((a,b,d,c,e,f)\), the cyclic-pair and triple terms give the exact factorization
\[
 \Delta T=s^2(c-d)\bigl[s(ae-bf)-t^2(b-e)\bigr].
\]
Substituting \((a,b,c,d,e,f)=(1,2,3,4,5,6)\) yields \(\Delta T=s^2(7s-3t^2)\). For \(s=1/4\), \(t_*=\sqrt{7/12}\) lies strictly between zero and one. The sign of \(\Delta T\) is positive below \(t_*\), zero there, and negative above it. Step 2 converts this trace reversal into the claimed reversal in growth factors. Combining with Step 3 proves six is minimal. \(\square\)

## Verification
The standalone Python 3 file `checker.py` uses exact rational matrix arithmetic to compare the cyclic independent-set expansion with direct products for **every permutation of \((1,\ldots,n)\), \(2\le n\le6\)** at four distinct survival pairs. It also exhaustively compares the sign of every unordered calendar-pair difference for \(n\le5\), checks the six-season neighbor-swap identity, verifies the two displayed rational trace differences, and checks exact persistence-threshold witness signs using \(\det(I-P)\). Its executed result was `PASS: 14432 exact-arithmetic diagnostic assertions.` The unrestricted claims follow from the preceding proof, not from finite enumeration. Run with `python3 checker.py` from the directory containing this document.

## Relationship to prior work
Gourley's 1977 analysis of periodic population models and Caswell–Trevisan's 1994 periodic-matrix sensitivity framework establish the broader demographic setting. Ackleh and Chiquet analyze continuous versus seasonal juvenile–adult reproduction and predominantly period-two cases; Cushing and Ackleh give periodic growth/reproduction theory and period-two Leslie formulas. These pre-existing approaches motivate the same kind of stage projection but, in the inspected accessible materials, do not state the sharp **fixed-fecundity-multiset, survival-driven first reversal at six seasons** proved above. General cyclic independent-set expansions and two-by-two characteristic-polynomial algebra are not independently claimed as novel methods. Related recent studies of four-season stage-specific interventions allow different vital rates to vary between seasons; their stronger scheduling effects in different models do not imply the present minimality under *fixed* survivals.

## Limitations
The mathematical theorem applies only to the specified two-stage projection with season-invariant maturation and retention, exact periodic forcing, and strictly positive fertility. It does not claim optimality among all calendars, infer a nonlinear stable cycle, cover uncertain vital rates, or establish that these precise fecundity profiles occur in any species. The historical-priority comparison to Gourley (1977) remains limited because only an abstract, not the full paper, could be accessed. The result has not been independently audited.

## References
- R. S. Gourley and C. E. Lawrence, *Stable population analysis in periodic environments*, Theoretical Population Biology 11 (1977), 49–59. DOI: https://doi.org/10.1016/0040-5809(77)90006-5. Publication evidence resolves to February 1977, not a verified exact first-public day.
- H. Caswell and M. C. Trevisan, *Sensitivity analysis of periodic matrix models*, Ecology 75 (1994), 1299–1303. DOI: https://doi.org/10.2307/1937455.
- A. S. Ackleh and R. A. Chiquet, *The global dynamics of a discrete juvenile–adult model with continuous and seasonal reproduction*, Journal of Biological Dynamics 3 (2009), 101–115. DOI: https://doi.org/10.1080/17513750802379010. The publisher identifies an online date of 2010-12-04; bibliographic date metadata disagree.
- J. M. Cushing and A. S. Ackleh, *A net reproductive number for periodic matrix models*, Journal of Biological Dynamics 6 (2012), 166–188. DOI: https://doi.org/10.1080/17513758.2010.544410. Published online 2011-02-18.
