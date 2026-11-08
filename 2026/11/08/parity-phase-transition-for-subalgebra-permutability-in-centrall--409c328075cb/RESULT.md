# Parity phase transition for subalgebra permutability in centrally stabilized affine Lie algebras

## Finding
Let \(q\) be any prime power and \(r\ge 3\). Write \(L_r(q)=\mathfrak{aff}_1(\mathbb F_q)\oplus\mathbb F_q^r\) for the Lie algebra with basis \(h,e,w_1,\dots,w_r\), sole nonzero basis bracket \([h,e]=e\), and central summand \(W=\langle w_1,\ldots,w_r\rangle\). Write \(\mathcal L_r\) for its finite set of Lie subalgebras. Two Lie subalgebras permute when their vector-space sum is a Lie subalgebra, equivalently \([A,B]\subseteq A+B\).

The numbers \(T_r(q)=|\mathcal L_r|\) and \(N_r(q)=|\{(A,B)\in\mathcal L_r^2:[A,B]\not\subseteq A+B\}|\) are determined exactly by Gaussian-binomial finite sums below. Consequently the subalgebra commutativity degree is
\[
\operatorname{sd}(L_r(q))=1-\frac{N_r(q)}{T_r(q)^2}.
\]
For each fixed \(r\ge3\), the following sharp parity law holds as \(q\) tends to infinity through prime powers:
\[
\boxed{\lim_{q\to\infty}\operatorname{sd}(L_r(q))=\begin{cases}0,&r\text{ odd},\\[1mm]1/4,&r\text{ even}.\end{cases}}
\]
In particular, central stabilization yields distinct limiting permutability probabilities in alternating Lie-algebra dimensions.

## Assumptions and scope
The base field is \(\mathbb F_q\) in arbitrary characteristic. The integer \(r\ge3\) is fixed for the asymptotic assertion and arbitrary for the exact formulas; no assumption of odd characteristic is needed. The Lie algebra has dimension \(r+2\), one-dimensional derived ideal \(\langle e\rangle\), and center \(W\) of dimension \(r\).

For integers \(a,b\), write \({a\brack b}_q\) for the Gaussian binomial, the number of \(b\)-dimensional subspaces of \(\mathbb F_q^a\), and define it as zero unless \(0\le b\le a\). Put \(G_d(q)=\sum_{j=0}^d {d\brack j}_q\). For indices \(0\le u,v\le r\) and \(\max(0,u+v-r)\le t\le\min(u,v)\), define
\[
W_{u,v,t}(q)={r\brack u}_q{u\brack t}_q{r-u\brack v-t}_q q^{(u-t)(v-t)}.
\]
All sums below are finite integer expressions. The subalgebra count is
\[
\boxed{T_r(q)=2G_{r+1}(q)-G_r(q)+q\sum_{u=0}^r {r\brack u}_q q^{r-u}.}
\]
The number of ordered nonpermuting subalgebra pairs is
\[
\boxed{N_r(q)=\sum_{u=0}^r\sum_{v=0}^r\sum_{t=\max(0,u+v-r)}^{\min(u,v)} W_{u,v,t}(q)\Big\{2(q^{u-t}-1)q^{r-v+1}+q(q-1)\big(q^{2r-u-v}-q^{r-t}\big)\Big\}.}
\]
For the first new central rank \(r=3\), these specialize to
\[
T_3(q)=(q+3)(q^4+2q^3+2q^2+q+2),
\]
\[
N_3(q)=q^2(q-1)(q+1)(q^2+q+1)(q^4+3q^3+8q^2+3q+1).
\]
The same finite-sum formulas also make sense at \(r=0,1,2\), but those smaller ranks are not claimed as new territory: they are included only as consistency checks and comparisons with earlier dimensional results.

## Proof
**1. Complete parametrization of Lie subalgebras.** Let \(I=\langle e\rangle\oplus W\), an abelian ideal. All linear subspaces of \(I\) are Lie subalgebras, giving \(G_{r+1}(q)\) objects. If a subalgebra \(A\) is not contained in \(I\) but contains \(e\), it is the full inverse image under \(L_r\to L_r/\langle e\rangle\) of a subspace whose image in \(L_r/I\) is nonzero. Since the quotient is abelian of dimension \(r+1\) and its \(W\)-subspace has dimension \(r\), this yields \(G_{r+1}(q)-G_r(q)\) objects.

Now let \(A\not\subseteq I\) and \(e\notin A\). Choose a vector \(h+ce+w\in A\) with \(c\in\mathbb F_q\) and \(w\in W\). For any \(e\)-coordinate-bearing vector \(u+f(u)e\in A\cap I\), the bracket with that chosen vector is \(-f(u)e\in A\). As \(e\notin A\), we must have \(f(u)=0\). Thus \(A\cap I=U\le W\), and every such subalgebra is uniquely
\[
C(U,c,\overline w)=\langle h+ce+w\rangle\oplus U,
\qquad U\le W,\ c\in\mathbb F_q,\ \overline w\in W/U.
\]
For \(\dim U=u\), there are \(q^{r-u+1}\) choices of \(c,\overline w\). Adding the three types proves the displayed formula for \(T_r(q)\).

The subalgebras in \(I\) that do not contain \(e\) can likewise be written uniquely as
\[
B(U,f)=\{u+f(u)e:u\in U\},\qquad U\le W,\quad f\in U^*.
\]
**2. Exhaustive nonpermuting pair classification.** Every subalgebra containing \(e\) permutes with all others, since all brackets lie in \(\langle e\rangle\). Two subalgebras of type \(B\) commute. Thus only \(B\)-\(C\) and \(C\)-\(C\) pairs can be nonpermuting.

Fix \(U,V\le W\), with \(\dim U=u\), \(\dim V=v\), \(\dim(U\cap V)=t\). The pair \(B(U,f)\), \(C(V,c,\overline w)\) has nonzero brackets precisely when \(f\ne0\). It then fails to permute precisely when \(e\notin B(U,f)+C(V,c,\overline w)\), which is equivalent to \(f\) vanishing on \(U\cap V\). There are exactly \(q^{u-t}-1\) such nonzero functionals, and \(q^{r-v+1}\) choices for the second subalgebra. Including both orders gives the first term in braces in \(N_r(q)\).

For two subalgebras \(C(U,c,\overline w)\) and \(C(V,d,\overline w')\), their only potentially nonzero bracket is \((d-c)e\). If \(c\ne d\), the pair fails to permute exactly when \(w-w'\notin U+V\). For fixed \(U,V\), there are \(q(q-1)\) ordered pairs \((c,d)\) of unequal scalars and \(q^{2r-u-v}-q^{r-t}\) ordered pairs of cosets \((\overline w,\overline w')\) with difference outside \(U+V\). Indeed, the total number of coset pairs is \(q^{2r-u-v}\), and the kernel of the difference map to \(W/(U+V)\) has order \(q^{r-t}\). This gives the second term in braces.

For fixed dimensions \((u,v,t)\), the number of ordered subspace pairs \((U,V)\) is \(W_{u,v,t}(q)\): first choose \(U\), then its intersection \(U\cap V\), then the image of \(V\) in \(W/U\), and finally a graph map to \(U/(U\cap V)\). Summing all possibilities proves the exact formula for \(N_r(q)\) and hence the exact commutativity-degree formula.

**3. Parity asymptotics.** For fixed integers \(r,u\), the Gaussian binomial has leading term \(q^{u(r-u)}\) with coefficient one. A type \(C\) subalgebra with \(\dim U=u\) contributes
\[
{r\brack u}_q q^{r-u+1}=q^{1+(u+1)(r-u)}(1+O(q^{-1})).
\]
The two other types together contribute one power of \(q\) less than the dominant type \(C\) count, and therefore have asymptotically zero proportion. The exponent \(1+(u+1)(r-u)\) is maximized uniquely at \(u=k\) when \(r=2k+1\), and equally at \(u=k-1,k\) when \(r=2k\); in the latter case the asymptotic masses are \(1/2\) each.

Two uniformly sampled dominant type \(C\) subalgebras with subspace dimensions \(u,v\) have independent uniformly distributed scalar parameters and coset parameters. If \(u+v<r\), then \(U+V\ne W\), and the probability of permutability is at most \(q^{-1}+q^{-1}\): either the scalar parameters agree (probability \(1/q\)), or unequal scalars require the coset difference to land in a proper subspace (probability at most \(1/q\)). For odd \(r=2k+1\), both dominant dimensions equal \(k\), hence the limit is zero. For even \(r=2k\), the only dominant dimension pair with \(u+v\ge r\) is \((k,k)\), of asymptotic mass \(1/4\). Two uniformly sampled \(k\)-subspaces of \(\mathbb F_q^{2k}\) are complementary with probability \(1-O(q^{-1})\). For complementary subspaces, \(U+V=W\), hence the associated type \(C\) subalgebras always permute. All other dominant pairs have permutability probability tending to zero. Thus the limit is \(1/4\). This completes both parity cases, with no restriction on the characteristic.

## Verification
The standalone script `artifacts/verify.py` enumerates every linear subspace in reduced row echelon form, directly tests Lie closure via row ranks, and directly tests the bracket-in-sum condition for each ordered pair of Lie subalgebras. It does not use the structural parametrization to generate its test objects. It verifies nine finite-field/dimension configurations: central dimensions \(r=0,1,2,3\), with \(q=2,3,4,5\) where computationally feasible (including a genuine \(\mathbb F_4\) implementation), examining 1339 ambient subspaces in total. All total-subalgebra counts and nonpermuting ordered-pair counts agree with the displayed finite sums, including for \(r=3,q=2\) the exact values \(T_3(2)=220\), \(N_3(2)=6636\).

The verified output is in `artifacts/verification_output.txt`, ending with `VERIFY_OK cases= 9 subspaces_examined= 1339`. Finite enumeration corroborates the symbolic formula only in these cases; the proof of the arbitrary-rank formulas and the asymptotic phase transition is the preceding algebraic argument.

## Relationship to prior work
Muhie, Otera and Russo introduced subalgebra commutativity degree and its permutability criterion, with explicit small-dimensional computations (arXiv:2609.19086v1, 2026-09-16). These definitions and results are prior work. Towers, Zuleta and Gutierrez's 2026 treatment of comaximal graphs develops related subalgebra-incidence invariants, but their comaximal adjacency is generation of the whole Lie algebra, not the Lie-closure of a vector-space sum, and the inspected primary text does not give the present family of formulas.

The previously reported three-dimensional plane-count formula covers the \(r=1\) member of this family, so that specialization is explicitly not a novelty claim. An earlier four-dimensional calculation for a *different*, diagonally acting solvable family (with eigenvalues \(1,1,\lambda\)) gives the same polynomials \(T_2(q)\) and \(N_2(q)\) for \(q>2\). That earlier numerical coincidence is acknowledged; the present claim focuses on every \(r\ge3\) and the rank-parity limit, which neither small-dimensional record implies. An earlier computation of a four-dimensional central stabilization of the Heisenberg algebra also has limiting degree \(1/4\), but concerns a nilpotent Lie algebra with derived ideal central, unlike the nonnilpotent family here. These comparisons concern mathematical statements, not merely similar titles.

## Limitations
The explicit formulas concern central stabilizations of the nonabelian two-dimensional affine Lie algebra, not arbitrary solvable Lie algebras, Heisenberg stabilizations or noncentral semidirect products. The limit fixes \(r\) and sends \(q\) to infinity; simultaneous growth regimes are not proved. Exhaustive computations cover only the stated small fields/dimensions. General older results on Lie subalgebra lattices could conceivably imply the formulas or limit through a less explicit equivalent description; no absolute historical-priority claim is made. Independent mathematical validation is not asserted.

## References
1. Seid Kassaw Muhie, Daniele Ettore Otera, Francesco G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (first public 2026-09-16), https://arxiv.org/abs/2609.19086.
2. David Towers, Yesneri Zuleta, Ismael Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1 (first public 2026-08-17), https://arxiv.org/abs/2608.16575.
3. *Plane counts control subalgebra commutativity in dimension three*, mathematical record (2026-09-18), https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c.
4. *Exact subalgebra commutativity degree after a one-dimensional central stabilization of the Heisenberg algebra*, mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-subalgebra-commutativity-degree-after-a-one-dimensional-ce--246d7542fd6a.
