# Cut-partition rank law for idempotent derivations of three-layer incidence algebras

## Finding
Let \(q=2^e\), \(e\ge1\), and let \(P_n\), \(n\ge1\), be the finite poset with three antichain levels, each of size \(n\), in which every element of an earlier level precedes every element of a later level. Let \(A_n=I(P_n,\mathbb F_q)\). Write \(E_{n,r}(q)\) for the number of distinct \(\mathbb F_q\)-linear algebra derivations \(D:A_n\to A_n\) with \(D^2=D\) and \(\operatorname{rank}D=r\).

The **complete operator-rank polynomial** is
\[
\boxed{\sum_{r\ge0} E_{n,r}(q)z^r=\frac12\sum_{a,b,c=0}^{n}\binom na\binom nb\binom nc\,(qz)^{R_n(a,b,c)}},
\]
where
\[
R_n(a,b,c)=a(n-b)+(n-a)b+a(n-c)+(n-a)c+b(n-c)+(n-b)c.
\]
The factor \(1/2\) is an ordinary integer division after summation, not a scalar in \(\mathbb F_q\). The polynomial has only even exponents, and its constant coefficient is \(1\).

The largest attainable operator rank is exactly \(2n^2\). The multiplicity at this rank is
\[
\boxed{E_{n,2n^2}(q)=3(2^n-1)q^{2n^2}}.
\]
Equivalently, the maximizers are parametrized by three vertex color classes: two levels must be monochromatic in opposite binary colors, and the third level may be colored arbitrarily; global color complementation represents the same derivation. If \(D_n\) is uniform among the idempotent derivations of \(A_n\), then for each fixed \(q\),
\[
\boxed{\Pr(\operatorname{rank}D_n=2n^2)=1-O_q(\rho_q^n)}
\]
for some \(0<\rho_q<1\). In particular, the complete rank polynomial has a frustrated, exponentially degenerate maximum stratum, yet the uniform distribution on concrete derivations is exponentially concentrated on that stratum. This is an exact finite-field statement and an asymptotic theorem, not a finite-computation extrapolation.

## Assumptions and scope
A derivation means a \(\mathbb F_q\)-linear map obeying \(D(xy)=D(x)y+xD(y)\) for every \(x,y\in A_n\). The rank is taken on the full \(\mathbb F_q\)-vector space \(A_n\), of dimension \(3n+3n^2\). Distinct maps are counted, rather than conjugacy classes or isomorphism types of gradings. The incidence algebra has basis \(e_{uv}\) indexed by \(u\le v\), with \(e_{uv}e_{vw}=e_{uw}\) and all other products of basis elements zero. The conclusion is for finite fields of characteristic two and all integer \(n\ge1\); the concentration assertion keeps \(q\) fixed.

## Proof
**1. Every derivation is inner.** Let \(D\) be a derivation and \(e_v=e_{vv}\). The orthogonal-idempotent identities imply that \(h=\sum_vD(e_v)e_v\) satisfies \([h,e_v]=D(e_v)\), where \([h,a]=ha-ah\). Thus \(D-\operatorname{ad}_h\) kills each \(e_v\) and consequently sends \(e_{uv}\) to \(\lambda_{uv}e_{uv}\). The Leibniz identity on \(e_{uv}e_{vw}\) gives \(\lambda_{uw}=\lambda_{uv}+\lambda_{vw}\) on all three-term chains. These scalars are a potential difference. For example, choose a bottom vertex \(x_0\) and a top vertex \(z_0\), and put \(t_x=\lambda_{xz_0}\) for bottom \(x\), \(t_y=\lambda_{yz_0}\) for middle \(y\), and \(t_z=\lambda_{x_0z_0}-\lambda_{x_0z}\) for top \(z\). The chain equations imply \(\lambda_{uv}=t_u-t_v\) on each comparable strict pair. Hence the remaining derivation equals \(\operatorname{ad}_{\sum_vt_ve_v}\), proving \(\operatorname{Der}(A_n)=\operatorname{IDer}(A_n)\).

**2. Idempotent operators come from idempotent generators.** Connectedness of the comparability graph implies \(Z(A_n)=\mathbb F_q I\): commuting with all vertex idempotents forces a central element to be diagonal, and commuting with every \(e_{uv}\) forces equal diagonal entries on comparable vertices. In characteristic two, \((\operatorname{ad}_X)^2=\operatorname{ad}_{X^2}\). Therefore \((\operatorname{ad}_X)^2=\operatorname{ad}_X\) exactly when \(X^2+X=\gamma I\). Choose one diagonal entry \(s=X_{vv}\); then \(s^2+s=\gamma\), so \(Y=X+sI\) obeys \(Y^2=Y\) and induces the same derivation. Conversely every idempotent \(Y\) yields an idempotent derivation. Two idempotent generators induce the same derivation precisely when they differ by \(cI\) with \(c^2+c=0\), hence by \(0\) or \(I\). Each idempotent derivation therefore has exactly two idempotent generators.

**3. Diagonal-pattern fibers.** Fix a binary diagonal coloring \(\epsilon:P_n\to\{0,1\}\), and write \(E=\sum_v\epsilon(v)e_v\). Any idempotent \(Y\) with this diagonal is conjugate to \(E\) by a unit of \(1+J\), where \(J\) is the strictly upper-poset radical: \(W=YE+(I-Y)(I-E)\) obeys \(WE=YW\) and satisfies \(W\equiv I\pmod J\), hence is invertible. The group \(1+J\) has \(q^{3n^2}\) elements. Its stabilizer at \(E\) has one arbitrary coefficient for every comparable strict pair whose endpoints have equal colors, since \(UE=EU\) is equivalent to \(U_{uv}(\epsilon(u)-\epsilon(v))=0\). Hence the conjugacy orbit, which is the entire fixed-diagonal fiber, has size \(q^{r(\epsilon)}\), with \(r(\epsilon)\) the number of strict comparable pairs with differently colored endpoints. Also \(\operatorname{ad}_E(e_{uv})=(\epsilon(u)-\epsilon(v))e_{uv}\), giving \(\operatorname{rank}\operatorname{ad}_E=r(\epsilon)\). Conjugation does not change operator rank.

**4. Exact rank polynomial.** For \(a,b,c\) vertices colored \(1\) in the respective levels, the number of patterns is \(\binom na\binom nb\binom nc\), and \(r(\epsilon)=R_n(a,b,c)\). Each contributes \(q^{R_n(a,b,c)}\) idempotents. Divide by the exact two-to-one passage from idempotent generators to derivation maps, proving the formula. Every vertex of the undirected comparability graph has degree \(2n\), so each cut has even size. Cut size zero forces a constant coloring because this graph is connected, hence the zero derivation is unique.

**5. Maximum and its exact multiplicity.** Set \(s_1=2a-n\), \(s_2=2b-n\), \(s_3=2c-n\). Then
\[
R_n(a,b,c)=\tfrac12(3n^2-s_1s_2-s_1s_3-s_2s_3).
\]
On \([-n,n]^3\), the multilinear expression is at most \(2n^2\), with equality exactly when some two coordinates \(s_i,s_j\) are opposite endpoints \(n,-n\). This can be checked by minimizing the affine function of one coordinate and factoring the resulting endpoint expressions; equality requires two opposed endpoint coordinates, while the third is free. There are \(6\cdot2^n\) choices of an ordered pair of pure opposite levels and an arbitrary third coloring. Exactly six fully monochromatic-level configurations with two levels one color and the third the opposite are counted twice, and no others are duplicated. Hence the number of maximizing binary colorings is \(6(2^n-1)\). Every such pattern has an orbit of \(q^{2n^2}\) idempotents; division by two gives \(3(2^n-1)q^{2n^2}\) derivations.

**6. Exponential maximal-rank concentration.** Normalize the total number of idempotent generators by \(q^{2n^2}\). Their maximizing colorings contribute exactly \(6(2^n-1)\). We bound the remaining normalized weight by \(o(2^n)\) exponentially. Fix \(\eta=1/100\). On the compact part of \([0,1]^3\) outside every neighborhood where some color frequency is at least \(1-\eta\) and another at most \(\eta\), continuity and the equality characterization in Step 5 give \(R_n\le(2-\delta)n^2\) for some \(\delta=\delta(\eta)>0\). Its entire contribution is at most \(2^{3n}q^{-\delta n^2}\).

Inside such a neighborhood, choose the nearly all-one level and the nearly all-zero level. Write their numbers of wrong-color vertices as \(a,b\le\eta n\), and let \(k\) be the number of ones in the remaining level. The deficit is \(2[a(n-k)+bk-ab]\). Summing over \(k\) with binomial multiplicities gives exactly
\[
q^{2ab}(q^{-2a}+q^{-2b})^n.
\]
For \(a+b>0\) with one of \(a,b\) zero, this is at most \((1+q^{-2})^n\). When both are positive, it is at most \((2q^{-2(1-\eta)})^n\). The number of possible choices of the two small wrong-color sets is at most \(2^{2H_2(\eta)n}\), where \(H_2(t)=-t\log_2t-(1-t)\log_2(1-t)\). There are only six choices of ordered pure-color levels. Since for all \(q\ge2\)
\[
2^{2H_2(\eta)}\max\{1+q^{-2},\,2q^{-2(1-\eta)}\}<2,
\]
the nonmaximizing weight in these neighborhoods is bounded by \(C\kappa^n\) for some \(\kappa<2\), and the far part is smaller still for large \(n\). Dividing by the ground-state contribution \(6(2^n-1)\) proves the stated \(O_q(\rho_q^n)\) bound for some \(\rho_q<1\).

## Verification
The standalone `verify.py` uses Python's standard library. It independently enumerates every element of the incidence algebra for \(n=1,2\) over \(\mathbb F_2\), tests idempotency by explicit algebra multiplication, constructs the inner derivation matrices, and computes operator ranks by binary elimination. It also exhaustively repeats \(n=1\) over \(\mathbb F_4\) with polynomial-field multiplication, and separately enumerates all \((a,b,c)\) through \(n=10\) to check the maximum-cut characterization and multiplicity. The executed output is `BINARY_EXHAUSTIVE_OK 1 6 {0: 1, 2: 12}`, `BINARY_EXHAUSTIVE_OK 2 18 {0: 1, 4: 96, 6: 1024, 8: 2304}`, `GF4_EXHAUSTIVE_OK {0: 1, 2: 48}`, `MAX_CUT_ENUMERATION_OK through n=10`, and `VERIFY_OK`. The proof of all parameter values and asymptotic rates is in Steps 1–6, not in these finite checks.

## Relationship to prior work
The inner-plus-additive description of derivations of incidence algebras, and its cohomological obstruction, are established; see Fornaroli–Khrypchenko (2023), especially Theorem 2.8 and Corollary 3.9, and Krylov–Tuganbaev (2023/2024). The conjugation of incidence-algebra idempotents to diagonal form is also previously known, explicitly as Lemma 7 in Santulo–Souza–Yasumura (2019). That paper classifies group gradings of incidence algebras up to graded isomorphism, including gradings by an abelian group. Dos Santos–Yasumura (2024) extends this program with complete realizability and isomorphism conditions (Theorems 6.1–6.2); its inspected statements again do not enumerate individual operators by rank. In characteristic two, idempotent derivations correspond to \(\mathbb Z/2\mathbb Z\)-gradings, so this is a substantial structural predecessor. The present count is for **distinct embedded linear derivation operators**, refined by rank, with a finite-field orbit factor for every vertex coloring; it is not a count of grading isomorphism classes. The complete \(q\)-weighted rank polynomial, maximum-rank multiplicity \(3(2^n-1)q^{2n^2}\), and concentration law were not located in those inspected texts. The polynomial is also the (integer-valued) two-state antiferromagnetic cut partition function of the complete tripartite comparability graph, divided by two. The maximum-cut combinatorics are elementary and are not claimed as a new graph-theoretic classification on their own.

## Limitations
The result is restricted to the three-antichain-level complete poset and characteristic-two finite fields, and counts linear derivations rather than arbitrary additive maps. The maximum-rank asymptotic fixes \(q\). The general relation between \(\mathbb Z/2\mathbb Z\)-gradings and idempotent derivations is prior mathematics; the claimed contribution is the concrete rank refinement and its quantitative enumeration. No independence or exhaustive priority search is claimed. Earlier gradings classifications and inaccessible literature may contain an implication of part of the census; publication priority therefore remains provisional.

## References
1. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439, first posted 2023-07-17, https://arxiv.org/abs/2307.08439 (sections 2–3).
2. P. Krylov and A. Tuganbaev, *Incidence Rings: Automorphisms and Derivations*, arXiv:2305.02984, first posted 2023-05-04, https://arxiv.org/abs/2305.02984; subsequent journal version *Derivations of Incidence Algebras* (2024).
3. E. A. Santulo Jr., J. P. Souza and F. Y. Yasumura, *Group gradings on finite dimensional incidence algebras*, arXiv:1905.08391, first posted 2019-05-21, https://arxiv.org/html/1905.08391v2 (Lemma 7; Theorems 1 and 34).
4. M. R. Jones, *Group gradings of incidence algebras*, University of Connecticut doctoral dissertation (2003), https://digitalcommons.lib.uconn.edu/dissertations/AAI3118955/ (abstract consulted; full dissertation not inspected).
5. H. S. Dos Santos and F. Y. Yasumura, *Group gradings on finite-dimensional incidence algebras. II*, arXiv:2406.19329, first posted 2024-06-27, https://arxiv.org/abs/2406.19329 (Theorems 2.1, 6.1–6.2).
