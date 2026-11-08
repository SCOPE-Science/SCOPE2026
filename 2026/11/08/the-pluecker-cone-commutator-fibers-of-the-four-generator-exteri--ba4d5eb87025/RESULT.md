# The Plücker-cone commutator fibers of the four-generator exterior algebra

## Finding
Let \(q\) be any odd prime power, \(k=\mathbb F_q\), \(V=k^4\), and \(E=\bigwedge_k V\). Fix an ordered basis \(e_1,e_2,e_3,e_4\) and let \(\omega=e_1\wedge e_2\wedge e_3\wedge e_4\). For \(a,b\in E\) use the **ordinary associative-algebra commutator** \([a,b]=ab-ba\), not the graded supercommutator.

Write each \(\gamma\in\bigwedge^2V\) uniquely as \(\sum_{1\le i<j\le4}g_{ij}e_i\wedge e_j\), and set
\[
P(\gamma)=g_{12}g_{34}-g_{13}g_{24}+g_{14}g_{23}.
\]
Then **the set of individual commutator values** is exactly
\[
\{[a,b]:a,b\in E\}=\{\gamma+t\omega: \gamma\in\bigwedge^2V,\ P(\gamma)=0,\ t\in k\}.
\]
More precisely, let \(F(\gamma,t)=|\{(a,b)\in E^2:[a,b]=\gamma+t\omega\}|\). Then
\[
F(\gamma,t)=q^{16}\begin{cases}
q^8+(q^4-1)(q+1)q^7,&\gamma=0,\ t=0,\\
(q^4-1)(q+1)q^7,&\gamma=0,\ t\ne0,\\
q^8(q^2-1),&\gamma\ne0,\ P(\gamma)=0,\\
0,&P(\gamma)\ne0.
\end{cases}
\]
These cases are exhaustive. In particular the image has exactly
\[
q\big[1+(q-1)(q^2+1)(q^2+q+1)\big]
\]
elements. Two independent uniform random elements of \(E\) commute with exact probability
\[
\Pr([a,b]=0)=q^{-4}+q^{-5}-q^{-9}.
\]
The additive span of all commutators equals \(\bigwedge^2 V\oplus\bigwedge^4V\). Exactly two commutator summands are necessary and sufficient to express an arbitrary element of that seven-dimensional subspace.

## Assumptions and scope
The algebra is the full sixteen-dimensional unital exterior algebra on four odd generators over a finite field of **odd** characteristic. Multiplication is the exterior product. The main count is of **ordered** pairs \((a,b)\), with no quotient by automorphisms, conjugacy, scalar rescaling, or change of basis. The output is graded, so degree-two and degree-four components are specified individually. Because \(2\) is invertible, the Pfaffian condition \(P(\gamma)=0\) is equivalent to \(\gamma\) being decomposable (or zero). The intrinsic value set is basis-independent; the Pfaffian formula is its fixed-coordinate description. The square-zero cone and the full exterior algebra in characteristic two are not covered.

## Proof
**1. Reduction to the odd subspace.** Decompose each input into its even and odd parts,
\[
a=a_{\mathrm{ev}}+u+\alpha,\qquad b=b_{\mathrm{ev}}+v+\beta,
\]
with \(u,v\in V\), \(\alpha,\beta\in\bigwedge^3V\), and \(a_{\mathrm{ev}},b_{\mathrm{ev}}\in\bigwedge^{\mathrm{even}}V\). Every even element commutes with all elements by graded commutativity, whereas two odd elements anticommute. Degree truncation in four generators therefore gives the exact identity
\[
[a,b]=2\big(u\wedge v+u\wedge\beta+\alpha\wedge v\big).
\]
The even components have eight free coordinates for each input; they contribute the multiplicative factor \(q^{16}\) to every fiber. In particular all outputs lie in \(\bigwedge^2V\oplus k\omega\).

**2. Decomposable two-form values and their counts.** The degree-two output is \(2u\wedge v\), hence a simple bivector. Conversely, every simple bivector is \(2u\wedge v\) for some ordered \((u,v)\), because \(2\) is invertible. For \(V\) of dimension four, the single Plücker relation \(P(\gamma)=0\) characterizes simple bivectors: equivalently, the rank of the alternating coefficient matrix is at most two. A nonzero simple bivector determines one two-plane in \(V\). The number of such two-planes is the Gaussian binomial coefficient
\[
{4\brack2}_q=(q^2+1)(q^2+q+1),
\]
and each has \(q-1\) nonzero volume elements. Hence the number of nonzero simple bivectors is \((q-1)(q^2+1)(q^2+q+1)\). For any *fixed* nonzero simple \(\gamma\), the pairs \((u,v)\) with \(2u\wedge v=\gamma\) are the ordered bases of that plane with prescribed determinant, namely \(|\operatorname{SL}_2(k)|=q(q^2-1)\) pairs.

**3. The top-degree linear functional.** For fixed \((u,v)\), the map
\[
T_{u,v}:\bigwedge^3V\oplus\bigwedge^3V\longrightarrow k\omega,
\qquad (\alpha,\beta)\longmapsto 2(u\wedge\beta+\alpha\wedge v)
\]
is \(k\)-linear. It is zero exactly when \(u=v=0\), because wedge pairing between \(V\) and \(\bigwedge^3 V\) is nondegenerate. If at least one of \(u,v\) is nonzero, it is surjective and every prescribed output \(t\omega\) has exactly \(q^7\) preimages. At \((u,v)=(0,0)\) the top output must be zero and the fiber has \(q^8\) points.

**4. Nonzero and zero two-form fibers.** Fix \(\gamma\ne0\) with \(P(\gamma)=0\). All corresponding \((u,v)\) are nonzero and there are \(q(q^2-1)\) of them. Each has exactly \(q^7\) choices of \((\alpha,\beta)\) for any prescribed \(t\), so the odd-input fiber has \(q^8(q^2-1)\) points. If \(\gamma=0\), the vectors \(u,v\) are dependent. There are \(q^4\) choices with \(u=0\), and \((q^4-1)q\) with \(u\ne0\) and \(v\) in its one-dimensional span. Of these, precisely one pair has \(u=v=0\); the other \((q^4-1)(q+1)\) pairs have surjective top functional. Thus the odd-input fiber has \((q^4-1)(q+1)q^7\) points for \(t\ne0\), with \(q^8\) extra points for \(t=0\). Multiplication by \(q^{16}\) gives all four displayed cases. This also shows that every allowable \(t\) actually occurs.

**5. Consequences and the sharp sum length.** Counting the image combines the number of admissible nonzero degree-two values with the single zero value, multiplied by the \(q\) free top scalars. For the commuting probability, divide \(F(0,0)\) by \(|E|^2=q^{32}\):
\[
\frac{q^{16}[q^8+(q^4-1)(q+1)q^7]}{q^{32}}
=q^{-4}+q^{-5}-q^{-9}.
\]
The simple bivectors linearly span \(\bigwedge^2V\), and a pure top-degree value occurs by taking \(u\ne0\), \(v=0\) with a suitable \(\beta\). Thus the additive span equals \(\bigwedge^2V\oplus k\omega\). Every two-form in dimension four has alternating rank zero, two, or four; any rank-four two-form is the sum of two nonzero simple bivectors, and a rank-four form is not itself simple. For any prescribed top coefficient, adjust the first nonzero simple summand using Step 3. Therefore two commutators always suffice for the span, and the rank-four case shows two are sometimes necessary.

## Verification
Two standalone programs accompany this account. `verify.cpp` exhausts the \(3^{16}=43{,}046{,}721\) ordered pairs of odd components over \(\mathbb F_3\), computes all seven output coordinates, and compares **every** fiber against the four-case formula. Its test excludes none of the codomain values. `verify.py` independently enumerates wedge images of all ordered pairs of vectors in \(\mathbb F_3^4\) and \(\mathbb F_5^4\), then uses 10,000 reproducible randomized full sixteen-coordinate exterior-algebra multiplications in each field to compare the original commutator with the displayed coordinate reduction. Run `python3 verify.py`, and compile/run `verify.cpp` using `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. Both have completed with `VERIFY_OK` from this package. These finite tests are corroboration; Steps 1–5, not their finite scope, prove the theorem for every odd prime power.

## Relationship to prior work
Gardella and Thiel (2023, revised 2024) study when rings are generated by commutators and when products of commutators have bounded Waring-type representations; their theorems are not finite-field fiber enumerations of a particular Grassmann algebra. Brešar (2020) studies the linear span and Waring problems for general polynomial images, prominently matrix-algebra settings. The classical Plücker relation and alternating rank decomposition predate this account; neither is claimed as independently new. Kleiner (2002) gives related structural results on rank-two multivectors but not counts of the ordinary associative-algebra commutator fibers. Demir and Nazemian (2025/2026) classify automorphism-stable linear subspaces and subalgebras of Grassmann algebras, including the **algebra generated** by commutators; that differs from the nonlinear set of individual commutator values and especially from their ordered-pair fibers. The distinctive claim assessed here is the complete uniform \(q\)-dependent fiber law, including the exceptional central-axis fibers and its sharp commuting probability. No statement about first publication priority is asserted beyond the inspected sources.

## Limitations
The exact identity requires odd characteristic and four generators; characteristic two makes the ordinary exterior algebra commutative. No extension to other exterior ranks, general coefficient rings, or nonassociative supercommutators is claimed. The direct computations cover only prime fields of orders three and five; the proof covers all odd finite fields. Broader or differently named literature may contain an equivalent enumeration.

## References
1. E. Gardella and H. Thiel, *Rings and C*-algebras generated by commutators*, arXiv:2301.05958, first posted January 14, 2023, https://arxiv.org/abs/2301.05958 .
2. M. Brešar, *Commutators and images of noncommutative polynomials*, arXiv:2001.10392, 2020, https://arxiv.org/abs/2001.10392 .
3. M. K. Demir and Z. Nazemian, *Aut-stable subspaces of Grassmann algebras*, arXiv:2508.16945, first posted August 23, 2025, https://arxiv.org/abs/2508.16945 .
4. G. B. Kleiner, *Multivectors of rank 2 over fields and commutative rings*, 2002 (classical rank-two multivector literature).
