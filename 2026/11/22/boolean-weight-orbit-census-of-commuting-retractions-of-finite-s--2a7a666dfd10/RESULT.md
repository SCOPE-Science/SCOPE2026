# Boolean-weight orbit census of commuting retractions of finite symmetric jet algebras

## Finding
Let \(k\) be an arbitrary field, \(n\ge2\), \(d\ge3\), and \(t\ge2\). Let \(A=k[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^{d+1}\), with coefficient-field-fixing unital algebra endomorphisms. Consider an **ordered** \(t\)-tuple \((E_1,\ldots,E_t)\) of pairwise commuting retractions: \(E_i^2=E_i\) and \(E_iE_j=E_jE_i\), with products here denoting composition.

Put \(\Omega=\{0,1\}^t\). Every tuple is conjugate under \(\operatorname{Aut}_k(A)\) to the simultaneous degreewise extension of tangent-space projections associated with a decomposition \(k^n=\bigoplus_{\epsilon\in\Omega}V_\epsilon\). Its orbit is uniquely determined by the weak composition \((n_\epsilon)_{\epsilon\in\Omega}\), \(n_\epsilon=\dim V_\epsilon\), \(\sum n_\epsilon=n\). Thus there are exactly \(\binom{n+2^t-1}{2^t-1}\) conjugacy classes over every field, without any gradedness assumption.

Over any finite field \(k=\mathbb F_q\), define
\[
H_{n,d}=\sum_{j=2}^d\binom{n+j-1}{j}=\binom{n+d}{d}-n-1.
\]
For each \(\eta\in\Omega\), let \(M_\eta(\mathbf n)\) be the number of monomials of total degree \(2\) through \(d\), in \(n\) variables colored by \(\epsilon\in\Omega\) with multiplicities \(n_\epsilon\), whose coordinatewise bitwise-AND of the colors of all variables occurring in the monomial is exactly \(\eta\). Explicitly,
\[
M_\eta(\mathbf n)=\sum_{j=2}^d\ \sum_{\substack{a_\epsilon\ge0,\ \sum_\epsilon a_\epsilon=j\\\bigwedge_{a_\epsilon>0}\epsilon=\eta}}\ \prod_{\epsilon\in\Omega}\binom{n_\epsilon+a_\epsilon-1}{a_\epsilon},
\]
where a factor with \(n_\epsilon=a_\epsilon=0\) is defined as \(1\), and with \(n_\epsilon=0<a_\epsilon\) as \(0\). The count of **actual labeled algebra-map tuples** in the conjugacy class indexed by \(\mathbf n\) is
\[
\boxed{C_{\mathbf n}(q)=\frac{|\mathrm{GL}_n(q)|}{\prod_{\epsilon\in\Omega}|\mathrm{GL}_{n_\epsilon}(q)|}\;q^{\,nH_{n,d}-\sum_{\epsilon\in\Omega}n_\epsilon M_\epsilon(\mathbf n)}.}
\]
The number of all tuples is \(\sum_{\sum n_\epsilon=n}C_{\mathbf n}(q)\). For every nonempty index set \(I\subseteq\{1,\ldots,t\}\), set \(r_I=\sum_{\epsilon:\epsilon_i=1\ \forall i\in I}n_\epsilon\). The complete joint **linear-image-rank** generating polynomial of all products is
\[
\boxed{\sum_{\sum n_\epsilon=n}C_{\mathbf n}(q)\prod_{\varnothing\ne I\subseteq[t]}Z_I^{\binom{r_I+d}{d}}.}
\]
Here the exponent includes the unit and all monomials in the retained variables.

For the first nonlinear two-generator case \(n=t=2\), every \(d\ge3\) and every prime power \(q\) have the exact formula
\[
\boxed{N_{2,d,2}(q)=4+q(q+1)\bigl(5q^{H_{2,d}}+q^{H_{2,d}+\binom d2}\bigr).}
\]
Among the six ways to assign distinct Boolean colors to the two generators, the incomparable-color pair \(01,10\) has a nonlinear orbit exactly \(q^{\binom d2}\) times as large as each of the other five: the extra exponent counts mixed commutative monomials of degrees \(2\) through \(d\). For \(d=3\), \(q=2\), there are exactly \(9988\) ordered commuting pairs, with \(770\) individual retractions.

## Assumptions and scope
A retraction is a unital, coefficient-field-fixing algebra endomorphism idempotent under composition. The maximal ideal \(\mathfrak m=(x_1,\ldots,x_n)\) is nilpotent and preserved by every such endomorphism, and \(V=\mathfrak m/\mathfrak m^2\) is its cotangent space. The field may have arbitrary positive or zero characteristic, and need not be algebraically closed. The count and rank-polynomial formulas require a finite field of order \(q\). All tuples are ordered, including repetitions; all automorphisms and retractions may have nonlinear generator images. A bitwise AND of one color is that color.

## Proof
**1. Simultaneous decomposition and lifting.** Each endomorphism induces an idempotent linear map \(P_i\) on \(V\); the \(P_i\) commute. Because \(X(X-1)\) is separable over every field, \(V=\bigoplus_{\epsilon\in\Omega}V_\epsilon\) with \(P_i|_{V_\epsilon}=\epsilon_i I\). As linear endomorphisms of the whole algebra, define \(Q_\epsilon=\prod_{i:\epsilon_i=1}E_i\prod_{i:\epsilon_i=0}(I-E_i)\). These are mutually orthogonal commuting projections on the underlying vector space, even though \(I-E_i\) is generally not multiplicative. They satisfy \(E_iQ_\epsilon=\epsilon_iQ_\epsilon\) and induce the corresponding tangent-space projectors. For a cotangent basis representative \(v\in\mathfrak m\) of color \(\epsilon\), replace \(v\) by \(Q_\epsilon(v)\in\mathfrak m\); its class modulo \(\mathfrak m^2\) is unchanged. Assigning these replacements to the \(n\) polynomial generators uniquely defines an algebra endomorphism \(g\). It has invertible tangent map, hence is an automorphism: the induced maps on \(\mathfrak m^j/\mathfrak m^{j+1}\cong\operatorname{Sym}^j V\) are invertible, and the finite nilpotent filtration implies invertibility. By construction, \(E_ig=g\widetilde P_i\) on every generator, hence on the entire algebra, where \(\widetilde P_i\) is the homogeneous extension of \(P_i\). This gives simultaneous conjugacy \(E_i=g\widetilde P_i g^{-1}\). Conversely every collection of tangent Boolean-weight projections extends to commuting algebra retractions.

**2. Orbit classification.** Conjugation by algebra automorphisms descends to simultaneous \(\mathrm{GL}(V)\) conjugation of the \(P_i\), preserving each common weight-space dimension. Two decompositions with the same multiplicities are conjugate by an invertible linear change of generators, itself an automorphism of the full homogeneous truncation. Thus the dimensions give a complete invariant. Their nonnegative weak compositions are counted by \(\binom{n+2^t-1}{2^t-1}\).

**3. Automorphism group.** A substitution of arbitrary \(n\) elements of \(\mathfrak m\) extends uniquely to an algebra endomorphism because every product of \(d+1\) such images vanishes. It is an automorphism iff its tangent linear matrix is invertible, by the filtration argument. The vector space of terms of degrees \(2,\ldots,d\) has dimension \(H_{n,d}\). Therefore \(\lvert\operatorname{Aut}(A)\rvert=|\mathrm{GL}_n(q)|q^{nH_{n,d}}\).

**4. Stabilizer.** Fix a homogeneous representative. A commuting algebra automorphism must preserve each tangent-space color \(V_\epsilon\), so its degree-one matrix lies in \(\prod_\epsilon\mathrm{GL}_{n_\epsilon}(q)\). Its higher-degree image of every generator of color \(\epsilon\) must consist only of monomials of precisely the same Boolean-AND color, since the source generator and each monomial must have identical eigenvalues for every \(\widetilde P_i\). For each such generator this is a vector space of dimension \(M_\epsilon(\mathbf n)\). Every choice preserves all original defining relations and yields an automorphism because the prescribed tangent matrix is invertible. The stabilizer order is exactly \(\prod_\epsilon|\mathrm{GL}_{n_\epsilon}(q)|q^{\sum_\epsilon n_\epsilon M_\epsilon}\). Orbit–stabilizer proves \(C_{\mathbf n}(q)\).

**5. Ranks and the two-generator resonance.** The product \(E_I\) is conjugate to the homogeneous retraction onto the symmetric-jet algebra in \(r_I\) retained generators. Its linear image rank is the number of monomials of degrees \(0,\ldots,d\) in those generators, namely \(\binom{r_I+d}{d}\); the formula remains valid for \(r_I=0\). For \(n=t=2\), the four decompositions concentrating both generators in one color yield singleton orbits. For each of the six choices of two distinct one-dimensional colors, \(|\mathrm{GL}_2(q)|/(q-1)^2=q(q+1)\). In a comparable pair, the monomials involving either generator have no extra non-matching weight, and the orbit exponent is \(H_{2,d}\). For the incomparable pair \(01,10\), each mixed monomial \(x^ay^b\) with \(a,b>0\) has the third color \(00\), not either generator color, producing exactly \(\sum_{j=2}^d(j-1)=\binom d2\) additional free coefficients. This proves the specialized formula and the exact orbit-size ratio.

## Verification
The standalone `commuting_verify.py` uses exact binary polynomial multiplication in the basis of the ten monomials of total degree at most three in two variables. It enumerates all \(2^{18}=262144\) endomorphism generator assignments of \(\mathbb F_2[x,y]/(x,y)^4\), tests composition idempotency by composing the original substitutions on the two generators, and finds \(770\) retractions (tangent ranks \(0,1,2\) have counts \(1,768,1\)). It then tests all \(770^2=592900\) ordered pairs for actual commutation of substitutions and finds exactly \(9988\), agreeing with the formula, independently of the orbit derivation. The program also prints the full joint tangent-rank histogram and confirms it sums to \(9988\). Run `python3 commuting_verify.py` to reproduce `ALL_COMMUTING_JET_RETRACTIONS_VERIFIED`. Finite enumeration is a check, not the proof of the all-field result.

## Relationship to prior work
Chakraborty–Dasgupta–Dutta–Gupta (2019, arXiv:1910.11023) examine polynomial-ring retracts, including the behavior of a single retraction under quotient descent; they do not enumerate all ordered commuting retraction families in finite symmetric jets. Gupta–Nagamine (2023, arXiv:2301.12681) address Laurent polynomial-ring retracts over domains, again not this nilpotent commutative algebra and not commuting tuples.

Published results in the published-finding corpus mathematical collection cover both the exact **single-map** retraction counts for all truncated symmetric powers and the cubically truncated commutative case, and these individual-map results are prior work here. Another published theorem, *Simultaneous linearization and an exact census of commuting retractions of truncated free associative algebras* (2026), treats **nonunital noncommutative** free algebras with ordered tensor words, with a related Boolean-weight orbit method. That theorem does not imply the present orbit counts by direct specialization: a commutative maximal-ideal-power quotient has symmetric monomials, a different automorphism and stabilizer group, and noncommutative lifts need not respect the quotient. The explicit commutative mixed-monomial exponent and all-arity joint-rank enumerator are the distinct claims here. The general Boolean eigenspace decomposition and conjugacy mechanism are not claimed as newly invented techniques.

## Limitations
The theorem concerns unital commutative polynomial truncations by the **full** power of the maximal ideal; it does not address coordinatewise truncations, arbitrary Artinian local rings, unrelated algebra identities, or noncommuting idempotents. The original formal-retraction literature and a nearby noncommutative theorem may already imply portions of the strategy; the particular symmetric-monomial enumeration has not been found in inspected sources, but absence from searches is not proof of absolute novelty. No independent validation or publication-priority certification is claimed.

## References
1. S. Chakraborty, N. Dasgupta, A. K. Dutta, and N. Gupta, *Some results on retracts of polynomial rings*, arXiv:1910.11023v1, first public 2019-10-24, https://arxiv.org/abs/1910.11023.
2. N. Gupta and T. Nagamine, *Retracts of Laurent polynomial rings*, arXiv:2301.12681v1, first public 2023-01-30, https://arxiv.org/abs/2301.12681.
3. *Simultaneous linearization and an exact census of commuting retractions of truncated free associative algebras*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-simultaneous-linearization-and-an-exact-census-of-commuting-retr--5df169bbe08e/RESULT.md.
4. *Retracts and idempotent endomorphisms of cube-zero truncated symmetric algebras*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-retracts-and-idempotent-endomorphisms-of-cube-zero-truncated-sym--d0314edd48d9/RESULT.md.
