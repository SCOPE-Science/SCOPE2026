# Ternary symmetry defect and complete tuple-orbit profiles of balanced Johnson graphs

## Finding

**Theorem.** Fix an integer \(k\ge 2\). Let \(\Omega_k\) be the set of all \(k\)-subsets of \([2k]\), let \(H_k\cong S_{2k}\) act by permuting ground elements, and let \(G_k=\operatorname{Aut}(J(2k,k))\) act on the graph's vertices. Write \(c(A)=[2k]\setminus A\). The known full-automorphism theorem gives \(G_k=H_k\times\langle c\rangle\).

(1) The closure of \(H_k\) on ordered pairs of vertices is \(G_k\), whereas its closure on ordered triples is exactly \(H_k\). This is a sharp arity-two/arity-three distinction for every \(k\ge2\).

(2) For each integer \(r\ge1\), define
\[
A_r(k)=[z^{2k}x_1^k\cdots x_r^k]\prod_{\epsilon\in\{0,1\}^r}\left(1-z\prod_{i=1}^{r}x_i^{\epsilon_i}\right)^{-1},\qquad
B_r(k)=\binom{k+2^{r-1}-1}{2^{r-1}-1}.
\]
The number of \(G_k\)-orbits of **all ordered \(r\)-tuples** of vertices, repetitions allowed, is exactly \((A_r(k)+B_r(k))/2\). For pairwise-distinct ordered \(r\)-tuples, let \(s(r,m)\) be the signed Stirling numbers of the first kind. The numbers of \(H_k\)-orbits, \(G_k\)-orbits, and \(H_k\)-orbits fixed by \(c\), respectively, are
\[
I_r(k)=\sum_{m=1}^r s(r,m)A_m(k),\quad
J_r(k)=\frac12\sum_{m=1}^r s(r,m)(A_m(k)+B_m(k)),\quad
F_r(k)=\sum_{m=1}^r s(r,m)B_m(k).
\]
These hold even when \(r>|\Omega_k|\), when the distinct-tuple counts are zero.

(3) A complete local **ternary orbit classification** is available. For ordered pairwise-distinct \((A,B,C)\), set \(p=|A\cap B|\), \(q=|A\cap C|\), \(u=|B\cap C|\), and \(t=|A\cap B\cap C|\). The feasible parameters are \(0\le p,q,u\le k-1\) and
\[
L=\max(0,p+q-k,p+u-k,q+u-k)\le t\le
U=\min(p,q,u,p+q+u-k).
\]
The \(H_k\)-orbit is determined by \((p,q,u,t)\). The \(G_k\)-orbit is determined by \((p,q,u,\min(t,p+q+u-k-t))\): complement acts by the reflection \(t\mapsto p+q+u-k-t\). Thus a feasible fixed pairwise-intersection profile with \(N=U-L+1\) possibilities splits into exactly \(\lceil N/2\rceil\) \(G_k\)-orbits.

For all \(k\ge2\), the number \(I_3(k)\) of \(H_k\)-orbits of ordered distinct triples is
\[
I_3(k)=\begin{cases}
\dfrac{k(k^3+8k^2+26k-32)}{24},& k\text{ even},\\[2mm]
\dfrac{(k-1)(k^3+9k^2+35k+3)}{24},& k\text{ odd}.
\end{cases}
\]
Exactly \(F_3(k)=k(k-1)(k+7)/6\) of these \(H_k\)-orbits are fixed by complement, so the number \(J_3(k)\) of full graph-automorphism orbits is
\[
J_3(k)=\begin{cases}
\dfrac{k(k^3+12k^2+50k-60)}{48},& k\text{ even},\\[2mm]
\dfrac{(k-1)(k^3+13k^2+63k+3)}{48},& k\text{ odd}.
\end{cases}
\]
The first three nontrivial examples are \((k,I_3,F_3,J_3)=(2,5,3,4),(3,18,10,14),(4,44,22,33)\).

(4) For each **fixed** \(r\ge3\), as \(k\to\infty\),
\[
I_r(k)=\Theta_r(k^{2^r-r-1}),\qquad
\frac{F_r(k)}{I_r(k)}=\Theta_r(k^{-(2^{r-1}-r)}).
\]
In particular \(F_3(k)/I_3(k)=4/k+O(k^{-2})\). Here the fraction is among **orbit types**, not among uniformly sampled labelled tuples. Thus asymptotically almost every \(H_k\)-orbit of injective ordered \(r\)-tuples is paired with a different \(H_k\)-orbit by the extra graph automorphism.

## Assumptions and scope

The vertices of \(J(2k,k)\) are the \(k\)-subsets of \([2k]\); two vertices are adjacent when they intersect in \(k-1\) elements. Coordinates of an ordered tuple are distinguished and **not** permuted. The permutation group \(H_k\) acts by simultaneous relabelling of the underlying \(2k\) points. The graph automorphism group \(G_k\) is the larger group when the underlying set has size exactly twice the subset size. The full-automorphism description, including the \(k=2\) octahedral case, is previously known, not a new result here.

For a permutation group \(H\) on \(\Omega\), its \(r\)-closure is the set of permutations of \(\Omega\) preserving **each** \(H\)-orbit on \(\Omega^r\), setwise. The coefficient notation extracts the stated monomial. Define \(s(0,0)=1\), \(s(r,0)=0\) for \(r>0\), and \(s(r,m)=s(r-1,m-1)-(r-1)s(r-1,m)\) for integers \(r\ge1\).

## Proof

**1. Full graph automorphisms and the sharp arity.** Ganesan's theorem, confirming a result of Jones, gives \(G_k=H_k\times\langle c\rangle\). On ordered pairs of \(k\)-subsets, \(H_k\)-orbits are classified by their intersection size. The graph's edges are exactly the pairs of intersection size \(k-1\). Hence any permutation preserving all \(H_k\)-pair orbits belongs to \(G_k\); conversely all of \(G_k\) preserves intersection sizes because graph distance is \(k-|A\cap B|\). Therefore \(H_k^{(2)}=G_k\).

The complement \(c\) does not preserve all \(H_k\)-triple orbits: choose a \((k-2)\)-subset \(D\) and four distinct points \(a,b,d,e\) outside \(D\), and consider \(D\cup\{a,b\},D\cup\{a,d\},D\cup\{a,e\}\). The three-way intersection has \(k-1\) points, whereas the three-way intersection of their complements has \(k-2\) points. No ground permutation can identify the two triples. Since any \(3\)-closure is contained in the \(2\)-closure and \(H_k\) has index two there, its \(3\)-closure must be \(H_k\). The four chosen points exist even for \(k=2\).

**2. Venn-pattern orbits and complement.** Given an ordered tuple \((A_1,\ldots,A_r)\), for each \(\epsilon\in\{0,1\}^r\) let \(a_\epsilon\) count ground points lying in \(A_i\) exactly when \(\epsilon_i=1\). Two tuples are in one \(H_k\)-orbit if and only if all these \(2^r\) counts agree: a ground permutation maps each corresponding Venn cell bijectively. Such count vectors are precisely the nonnegative integer solutions to
\[
\sum_{\epsilon}a_\epsilon=2k,\qquad
\sum_{\epsilon:\epsilon_i=1}a_\epsilon=k\quad(1\le i\le r),
\]
whose generating coefficient is \(A_r(k)\). Complement maps the vector to \((a_{\bar\epsilon})_\epsilon\), where \(\bar\epsilon\) flips each bit. A vector is fixed exactly when \(a_\epsilon=a_{\bar\epsilon}\) in all \(2^{r-1}\) complementary pairs. Writing their common entries as \(b_1,\ldots,b_{2^{r-1}}\), the constraints reduce to \(b_i\ge0\) and \(\sum b_i=k\). The stars-and-bars count is \(B_r(k)\). Burnside's lemma for the two-element action on the set of \(H_k\)-orbits proves \((A_r+B_r)/2\).

**3. Remove repeated tuple coordinates.** Let \(U_r\) be the set of \(H_k\)-orbits on all ordered \(r\)-tuples and \(V_r\subseteq U_r\) those with pairwise-distinct coordinates. The decomposition by equality partitions gives \(|U_r|=\sum_{m=1}^r\left\{{r\atop m}\right\}|V_m|\), where the braces are Stirling numbers of the second kind. Equality partitions are invariant under complement, so the same decomposition holds for the *numbers of complement-fixed orbit types*. Signed Stirling inversion gives \(I_r\) and \(F_r\) as stated; another Burnside averaging gives \(J_r=(I_r+F_r)/2\).

**4. Three-coordinate cells and exact polynomials.** For distinct \((A,B,C)\), the eight Venn-cell counts, in patterns \(111,110,101,011,100,010,001,000\), are respectively
\[
t,\;p-t,\;q-t,\;u-t,\;k-p-q+t,\;k-p-u+t,\;k-q-u+t,\;p+q+u-k-t.
\]
Their nonnegativity is exactly \(L\le t\le U\). Complement replaces the \(111\)-entry by the \(000\)-entry, giving the claimed reflection. The interval is reflection-invariant, so \(L+U=p+q+u-k\) whenever feasible. For each triple \((p,q,u)\), reflection on a consecutive integer interval of length \(N\) has exactly \(\lceil N/2\rceil\) orbits.

For a separate closed-form count of \(I_3\), fix distinct \(A,B\) with \(v=|A\cap B|\in\{0,\ldots,k-1\}\). The stabilizer of \((A,B)\) has four cells of sizes \(v,k-v,k-v,v\). The orbit of the third \(k\)-subset is specified by the number of its elements in each cell. Removing the two coincident choices \(C=A\) and \(C=B\) yields
\[
I_3(k)=\sum_{v=0}^{k-1}[x^k](1+x+\cdots+x^v)^2(1+x+\cdots+x^{k-v})^2-2k.
\]
With \(\binom{m}{j}_+=0\) for \(m<j\), the inner coefficient is
\[
\binom{k+3}{3}-2\binom{k-v+2}{3}-2\binom{v+2}{3}+\binom{k-2v+1}{3}_++\binom{2v-k+1}{3}_+.
\]
Hockey-stick summation gives
\[
I_3(k)=k\binom{k+3}{3}-2\binom{k+3}{4}-2\binom{k+2}{4}+E_k-2k,
\]
where for \(k=2m\), \(E_k=2\sum_{j=1}^{m}\binom{2j+1}{3}-\binom{2m+1}{3}\), and for \(k=2m+1\), \(E_k=2\sum_{j=1}^{m+1}\binom{2j}{3}-\binom{2m+2}{3}\). Summing these cubic binomial expressions gives the two displayed closed forms for \(I_3\). Independently, Stirling inversion of \(B_1=1\), \(B_2=k+1\), and \(B_3=\binom{k+3}{3}\) gives \(F_3=B_3-3B_2+2B_1=k(k-1)(k+7)/6\). Thus \(J_3=(I_3+F_3)/2\), proving its displayed forms.

**5. Fixed-arity asymptotics.** For fixed \(r\), after dividing the count vector by \(k\), the feasible vectors form a rational polytope in \(\mathbb R^{2^r}\) with \(r+1\) independent linear equations. The point with every coordinate equal to \(2^{1-r}\) lies in its relative interior; hence the dimension is \(d_r=2^r-r-1\). Its lattice-point count \(A_r(k)\) is an Ehrhart quasipolynomial with positive leading coefficient and degree \(d_r\), so \(A_r(k)=\Theta_r(k^{d_r})\). For fixed \(r\ge3\), all the terms with \(m<r\) in \(I_r\) have strictly smaller degree, yielding \(I_r(k)=\Theta_r(k^{d_r})\). Likewise \(B_r(k)\) is a polynomial of degree \(2^{r-1}-1\), and the lower \(B_m\) terms cannot cancel its leading term, so \(F_r(k)=\Theta_r(k^{2^{r-1}-1})\). The exponent difference is \(2^{r-1}-r>0\). Substituting the explicit ternary formulas gives \(4/k+O(k^{-2})\) at \(r=3\).

## Verification

The self-contained file `checker.py` uses exact integer arithmetic. Execute it with `python checker.py` in Python 3. It independently enumerates all ordered pairwise-distinct tuple signatures and their complement orbits at \((k,r)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4)\); compares them against signed-Stirling profile formulas; compares three distinct derivations of \(I_3\) for every \(2\le k\le25\); and verifies directly that the automorphism group of \(J(4,2)\) has 48 members and four orbits of ordered distinct triples. It prints `ALL_CHECKS_OK` when every check passes. This is a finite consistency test, not an infinite proof; the symbolic arguments above supply the arbitrary-parameter statements.

## Relationship to prior work

Benediktsson, Macpherson and Adler's recent work (arXiv:2610.40054v1, first public 2026-10-29) motivates the finite-model-theoretic importance of Johnson graphs and studies their growing-parameter first-order limit theory. Its main results concern completeness, axiomatization, stability and monadic dependence; they are not the finite tuple-orbit census developed here.

Jones's earlier classification of automorphisms of merged Johnson graphs and Ganesan's complete elementary proof of \(\operatorname{Aut}(J(2k,k))=S_{2k}\times C_2\) supply the full-group premise. The pairwise orbitals of the Johnson association scheme, indexed by intersection size, are also classical. None of those group or pair-orbit statements alone evaluates the full higher-arity Venn-counting coefficient, its complement-fixed strata, the ternary conditional fiber classification, or the asymptotic proportion of unmerged injective orbit types. The elementary closure consequence is included for context and is not presented separately as a new group classification. Ordinary Burnside averaging, Stirling inversion and Ehrhart theory are standard tools, not new general techniques.

## Limitations

The result counts **group orbit types** of actual finite graph-vertex tuples; it does not assert that every such orbit is definable by a formula of bounded graph-logic quantifier rank. The main new contribution is the **combined sharp quantitative profile and complete ternary refinement**, not the previously established automorphism group or the general Burnside/Ehrhart machinery. Some earlier material on higher-order orbit counts of Johnson association schemes might encode an equivalent result under other terminology; historical priority has not been independently certified. The 2005 Jones paper was not accessible in its entirety, although a complete later group-theorem proof and the relevant publicly displayed group/orbital statements were inspected. All asymptotic statements hold for fixed \(r\) and \(k\to\infty\), and refer to uniformly weighted orbit types, not uniformly sampled vertex tuples. Independent mathematical audit has not been performed.

## References

1. Bjarki Geir Benediktsson, Dugald Macpherson and Isolde Adler, *Model Theory of Johnson Graphs*, arXiv:2610.40054v1 (first publicly submitted 2026-10-29), https://arxiv.org/abs/2610.40054.
2. Ashwin Ganesan, *On the automorphism group of a Johnson graph*, arXiv:1412.5055 (2014), especially Theorem 1, https://arxiv.org/abs/1412.5055.
3. G. A. Jones, *Automorphisms and regular embeddings of merged Johnson graphs*, European Journal of Combinatorics **26** (2005), 417–435, DOI:10.1016/j.ejc.2004.01.012.
4. Coen del Valle and Colva M. Roney-Dougal, *The base size of the symmetric group acting on subsets*, Algebraic Combinatorics **7** (2024), 959–967, DOI:10.5802/alco.370 (different group-action invariant).
