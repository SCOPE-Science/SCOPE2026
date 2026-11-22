# A sharp relative-error threshold for a common-determinant dependence split

## Finding

Let \(A,B,C\) be finite nonempty named sets, with \(|B|=r\ge 2\) and \(|C|=s\ge 2\). For every team \(T\subseteq A\times B\times C\), consider the lax splitting formula
\[
\Phi_p\ :=\ =_p(x,y)\ \lor\ =_0(x,z),\qquad 0\le p\le1.
\]
The approximate atom \(=_p(x,y)\) means that at most a fraction \(p\) of the assignments of its *own* team may be deleted to make \(y\) functionally dependent on \(x\). In a lax split the two covering subteams may overlap.

**Sharp threshold and equality classification.** Put
\[
p_{r,s}=\frac{(r-1)(s-1)}{rs-r+1}.
\]
Every team satisfies \(\Phi_{p_{r,s}}\), and no smaller universal parameter works. More precisely, for nonempty \(T\), the least \(p\in[0,1]\) for which \(T\models\Phi_p\) equals \(p_{r,s}\) if and only if every nonempty \(x\)-fiber of \(T\) is the entire Cartesian rectangle \(B\times C\). All other nonempty teams have a strictly smaller least parameter.

**Exact finite-team criterion.** For each \(a\in A\), \(u\in B\), and \(v\in C\), write
\[
M_{a,u,v}=\mathbf1_{\{(a,u,v)\in T\}},\quad
R_{a,u}=\sum_{v\in C}M_{a,u,v},\quad
C_{a,v}=\sum_{u\in B}M_{a,u,v}.
\]
Then for every real \(p\in[0,1]\), including the endpoints,
\[
\boxed{\quad
T\models\Phi_p\quad\Longleftrightarrow\quad
\sum_{a\in A}\max_{u\in B,\,v\in C}
\bigl(R_{a,u}+(1-p)(C_{a,v}-M_{a,u,v})\bigr)
\ge (1-p)|T|.\quad}
\]
For rational \(p\), the criterion gives an exact polynomial-time decision algorithm using \(O(|T|+|A|rs)\) arithmetic operations on numbers of polynomial bit length. It also yields the exact least rational parameter by searching the \(O(|T|^2)\) possible ratios with numerator and positive denominator at most \(|T|\), with zero treated separately.

## Assumptions and scope

The team consists of **sets of distinct assignments** to precisely the three variables \(x,y,z\), with values in the indicated named alphabets. There are no additional hidden coordinates or duplicate tuples. An empty team satisfies the formula for every parameter. The notation \(=_0(x,z)\) is ordinary exact functional dependence. For a subteam \(U\), \(U\models =_p(x,y)\) means that some \(D\subseteq U\) obeys \(|D|\le p|U|\) and \(U\setminus D\models =(x,y)\). A lax split is \(T=T_1\cup T_2\) with no disjointness requirement. The theorem allows arbitrary \(|A|\ge1\). The degenerate cases \(r=1\) or \(s=1\) have universal threshold zero, but no uniqueness assertion is made for them.

## Proof

**1. A normal form for arbitrary overlapping witnesses.** Fix a nonempty team and choose for each occupied \(x\)-fiber a pair of values \((u_a,v_a)\in B\times C\). Let \(E\) contain the assignments \((a,y,z)\) with \(y\ne u_a\) and \(z\ne v_a\), and let \(H\) contain those with \(y\ne u_a\) and \(z=v_a\). Write \(e=|E|\), \(b=|H|\), and \(N=|T|\). Construct
\[
T_1^*=\{(a,y,z)\in T:y=u_a\text{ or }z\ne v_a\},\qquad
T_2^*=\{(a,y,z)\in T:z=v_a\}.
\]
These subteams cover \(T\), with \(T_2^*\models =(x,z)\); deleting exactly \(E\) from \(T_1^*\) makes \(y\) a function of \(x\). Thus \(e\le p(N-b)\) is sufficient for this displayed split with its specified deletion certificate; necessity for some choice of pairs is proved next.

Conversely, suppose \(T=T_1\cup T_2\), \(T_2\models =(x,z)\), and deleting \(D\subseteq T_1\) leaves \(T_1\setminus D\models =(x,y)\). Choose \(v_a\) from the second dependence and \(u_a\) from the repaired first dependence, assigning arbitrary values on fibers where one side is empty. Then \(E\subseteq D\). Every assignment in \(T_1\cap H\) must belong to \(D\), while \(T_1\subseteq T_1^*\cup(T_1\cap H)\). Writing \(h=|T_1\cap H|\) gives \(|D|\ge e+h\), \(|T_1|\le (N-b)+h\). Since \(e\le N-b\), the inequalities \(|D|\le p|T_1|\) imply \(e\le p(N-b)\) for \(0\le p\le1\): indeed \(e+h\le |D|\le p[(N-b)+h]\), so \(e\le p(N-b)-(1-p)h\le p(N-b)\). This proves the normal form even when the original split overlaps or either side is empty.

**2. The exact criterion.** On each fiber, the number of doubly excluded assignments is
\[
e_a=N_a-R_{a,u_a}-C_{a,v_a}+M_{a,u_a,v_a},
\]
and the number placed solely on the exact side is \(b_a=C_{a,v_a}-M_{a,u_a,v_a}\). The condition \(\sum_a e_a\le p(N-\sum_a b_a)\) rearranges to
\[
\sum_a\bigl(R_{a,u_a}+(1-p)(C_{a,v_a}-M_{a,u_a,v_a})\bigr)\ge(1-p)N.
\]
Choice of values is independent across fibers, so taking the maximum separately in every fiber proves the boxed equivalence. If the first side is empty, its deletion budget is zero and the inequalities are still well-defined. For the least parameter, any canonical pair choice has rational threshold \(e/(N-b)\) when \(N-b>0\); when both vanish it has threshold zero. Numerators and denominators do not exceed \(N\), yielding the claimed finite rational candidate set.

**3. Universal sharp bound.** Set \(c=1-p_{r,s}=s/(rs-r+1)\). In a fixed fiber of size \(N_a\), average the score
\[
Q_a(u,v)=R_{a,u}+c(C_{a,v}-M_{a,u,v})
\]
over all \(rs\) pairs. Each assignment contributes \(1/r\) to the mean of the first term and \(c(r-1)/(rs)\) to the second, hence
\[
\frac1{rs}\sum_{u,v}Q_a(u,v)
=N_a\left(\frac1r+\frac{c(r-1)}{rs}\right)=cN_a.
\]
Therefore \(\max_{u,v}Q_a(u,v)\ge cN_a\) on each fiber, and the criterion establishes \(T\models\Phi_{p_{r,s}}\).

If a fiber is the full rectangle, every pair gives \(e_a=(r-1)(s-1)\) and \(N_a-b_a=rs-r+1\). Thus every full nonempty fiber has exact threshold \(p_{r,s}\), as does any union of such fibers, and the universal constant cannot be reduced.

**4. Classification of equality.** Suppose the least parameter of nonempty \(T\) equals \(p_{r,s}\). Then the criterion at \(p_{r,s}\) is an equality, since any strict score surplus would persist after decreasing \(p\) slightly. As each fiber's maximum is at least its average \(cN_a\), every nonempty fiber has all its \(Q_a(u,v)\) equal. Fix such a fiber, abbreviate its incidence matrix by \(M_{uv}\), and compare two columns \(v,v'\). The constancy of \(Q_a\), for every row \(u\), implies
\[
C_v-C_{v'}=M_{uv}-M_{uv'}.
\]
Summing over rows yields \((r-1)(C_v-C_{v'})=0\). Because \(r\ge2\), all column sums agree and each row has identical entries across columns. Let \(t_u\in\{0,1\}\) be this row entry, and let \(h\) be the number of full rows. Then
\[
Q_a(u,v)=ch+(s-c)t_u.
\]
Since \(s-c>0\), equality of all scores forces all \(t_u\) to be equal. The fiber is nonempty, so every \(t_u=1\), and it is the full \(B\times C\). Conversely full occupied fibers attain the constant by step 3. This completes the proof.

## Verification

The accompanying standard-library program `verify.py` independently enumerates all overlapping lax splits and exact deletion budgets, then compares the resulting least parameter with the separate fiber-cross formula. It checks every subteam on \(1\times2\times2\), \(1\times2\times3\), \(1\times3\times3\), and \(2\times2\times2\), altogether 848 teams including the empty cases, and also checks eight rational decision thresholds for each team. The same cases exhaustively verify the stated extremizers. Successful output ends with `SEMANTIC_AND_EXTREMAL_CHECKS_OK 848`. These finite checks are independent stress tests, not a substitute for the all-size proof above.

## Relationship to prior work

Fröhlich, Häggblom, Å. Hirvonen, and M. Hirvonen (2026) formalize relative-error dependence and prove NP-completeness for a two-atom mixed disjunction with distinct determinants. Their model-checking result does not provide the present sharp, alphabet-dependent universal threshold or the all-team same-determinant max formula. Fröhlich, Kolaitis, and Meier (2025/2026), Theorem 21, prove four-coherence for the exact split \(=(x,y)\lor =(x,z)\), corresponding to the zero-error boundary of the present setting; that result does not entail the positive-error threshold. A related published size enumerator for the exact split counts satisfying teams, a different statistic from the smallest relative error needed for each team and its unique worst-case geometry. The proof here uses the full semantics of relative, not absolute, error and of overlapping lax disjunction.

## Limitations

The result is for finite sets of distinct triples, one approximate and one exact atom, a shared single determinant, and bounded named \(y,z\) alphabets. It does not give a trichotomy for arbitrary approximate dependence formulas, nor an error threshold when both atoms are approximate or have different determinants. The exact value of the threshold is asymmetric in the two alphabet sizes because the approximate and exact disjuncts are different. Historical priority is assessed against the literature inspected but is not independently certified.

## References

1. N. Fröhlich, M. Häggblom, Å. Hirvonen, and M. Hirvonen, *Approximate Functional Dependencies—Implication Problem Revisited*, arXiv:2608.16570, first posted 2026-08-17. https://arxiv.org/abs/2608.16570
2. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, first posted 2025-08-22, also CSL 2026. https://arxiv.org/html/2508.16146v1
3. *Exact size enumerator for a two-dependence-atom disjunction*, published research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-size-enumerator-for-a-two-dependence-atom-disjunction--e22bc6a91416
