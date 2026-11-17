# Two inequivalent dyadic reductions of the Klein twelve-line configuration

## Finding

Let \(R=\mathbb Z[a]/(a^2+a+2)\), the ring of integers of \(\mathbb Q(\sqrt{-7})\), and consider the twelve-line subarrangement \(\mathcal K'\) of the Klein twenty-one-line arrangement singled out by Gévay and Pokora [1, Proposition 2.1]. Let \(F\) be the product of its twelve specified linear forms, and let \(\mathcal D=V(F)\subset\mathbb P^2_R\) be the associated effective Cartier divisor.

**Theorem.** The family \(\mathcal D\to\operatorname{Spec}R\) is flat of relative degree twelve. At every geometric point of odd residue characteristic its fiber is a reduced arrangement of twelve distinct lines, with exactly twelve ordinary triple points, thirty ordinary double points and no other singularities. The complete locus of combinatorial bad reduction consists of the two primes of \(R\) over two:

\[
\begin{aligned}
\mathfrak p_0=(2,a):&\quad F\bmod\mathfrak p_0=(X+Y)^4(X+Z)^4(Y+Z)^4,\\
\mathfrak p_1=(2,a-1):&\quad F\bmod\mathfrak p_1=(X+Y+Z)^{12}.
\end{aligned}
\]

The first reduced support is a union of three **concurrent** lines; the second is a single line. In particular, the two dyadic fibers are not isomorphic as reduced curves and are not isomorphic as embedded nonreduced divisors. Every geometric fiber has arithmetic genus fifty-five; the reduced dyadic supports have arithmetic genera one and zero, respectively.

The good-reduction assertion includes the ramified prime of characteristic seven: the characteristic-seven phenomena of the full twenty-one-line configuration do not introduce extra incidences among these twelve chosen lines.

## Assumptions and scope

All base changes in this statement refer to the explicit integral model of \(\mathcal K'\) over \(R\). Other projectively equivalent models can have different integral presentations, so the theorem does not claim model-independent minimality of the bad-reduction locus. Geometric fibers mean fibers over algebraic closures of residue fields. The term *ordinary* refers to transverse intersections of distinct smooth line branches. No statement is made about singularities of the total three-dimensional space above the dyadic fibers or about modular reflection-group actions.

The twelve defining forms, in the ordering inherited from [1], are

\[
\begin{aligned}
& aX+Y-Z,\quad aX-Y+Z,\quad X+aY-Z,\quad aX-Y-Z,\\
&-X+Y+aZ,\quad aX+Y+Z,\quad -X+aY+Z,\quad -X-Y+aZ,\\
&-X+aY-Z,\quad X+aY+Z,\quad X-Y+aZ,\quad X+Y+aZ.
\end{aligned}
\]

Thus \(F\) is their product without any scalar denominators. The source identifiers for the motivating geometry are arXiv:2211.15309 (first submitted 2022-11-28), arXiv:1609.08648 (earlier full Klein arrangement), and DOI:10.3390/axioms13050321 (later finite-characteristic context).

## Proof

**1. The integral base and flatness.** The polynomial \(a^2+a+2\) has discriminant \(-7\). Since this is the fundamental discriminant of \(\mathbb Q(\sqrt{-7})\), \(R\) is its ring of integers and is a Dedekind domain. Every displayed linear factor has at least one coefficient \(1\) or \(-1\). Therefore its reduction modulo any prime of \(R\) is nonzero, and so is the product \(F\). In each localization of \(R\) at a nonzero prime, \(F\) defines a relative effective Cartier divisor in the smooth flat family \(\mathbb P^2_R\); the quotient is torsion-free over the local discrete valuation ring and hence flat. The generic fiber is likewise a Cartier divisor of degree twelve. This establishes flatness over \(R\), including at its generic point.

**2. Exact characteristic-independent determinant certificate.** Represent \(u+va\in R\) by its integer pair \((u,v)\). The relation \(a^2=-a-2\) makes multiplication and determinant evaluation exact. The quadratic norm is

\[
N(u+va)=(u+va)(u+v(-1-a))=u^2-uv+2v^2.
\]

For the \(\binom{12}{3}=220\) unordered triples of line coefficient vectors, an exhaustive integer-arithmetic determinant census gives the following norm counts:

\[
\begin{array}{c|rrrrr}
N(\det)&0&8&16&32&64\\\hline
\text{number of triples}&12&56&84&64&4.
\end{array}
\]

Moreover, each of the twelve zero-determinant triples uses three distinct lines; each line occurs in exactly three such triples; and no unordered pair of lines occurs in two zero-determinant triples. Each of the sixty-six unordered pairs lies in some triple with nonzero determinant. These assertions are exact finite calculations, independently reconstructible by the attached standalone program `verify_modular.py`; no sampling, floating point or unbounded conjectural extrapolation is involved.

Every nonzero determinant has norm a power of two. Hence it becomes a unit in \(R[1/2]\) and never vanishes after passage to a residue field of odd characteristic. Pairwise line distinctness and all zero/nonzero triple-concurrence relations therefore persist at every odd prime. Twelve triple-concurrence classes account for thirty-six of the sixty-six line pairs, leaving thirty pairs meeting at distinct ordinary double points. Since a fourfold concurrence would force some pair to belong to two zero triples, there is none. A pairwise intersection section is defined over \(R[1/2]\) by the cross product of two coefficient vectors; the unit determinant with a third vector makes that cross product unimodular. Consequently the forty-two intersection sections are disjoint there, proving the asserted uniform geometric incidence.

**3. The two dyadic special fibers.** Modulo two,

\[
a^2+a+2\equiv a(a+1).
\]

Thus the two distinct primes above two have residues \(a=0\) and \(a=1\) in \(\mathbb F_2\). Substituting these values into all twelve integral factors yields, respectively, precisely four copies each of \(X+Y\), \(X+Z\), and \(Y+Z\); or twelve copies of \(X+Y+Z\). These are the factorization identities in the theorem. At the first prime the three distinct supporting lines pass through \([1:1:1]\), and at the second the reduced support is smooth. Since distinct residual components have coalesced, both primes are bad; Step 2 rules out every other prime.

**4. Arithmetic genus.** Every fiber is a degree-twelve Cartier divisor in a projective plane, so the standard exact sequence with \(\mathcal O_{\mathbb P^2}(-12)\) gives

\[
p_a(\mathcal D_s)=\frac{(12-1)(12-2)}2=55.
\]

For the reduced supports in characteristic two the degrees are three and one, giving genera one and zero. If \(\mathcal N_s\) is the kernel of \(\mathcal O_{\mathcal D_s}\to\mathcal O_{(\mathcal D_s)_{\mathrm{red}}}\), the Euler characteristics of these nilpotent kernels are, respectively, \(-54\) and \(-55\). This quantifies how the fixed genus of the flat family is carried by nonreduced structure at the two dyadic primes.

## Verification

Run `python3 verify_modular.py` from the directory containing that standalone program. It checks all 220 integral triple determinants and their exact norms; the incidence relations among all 66 pairs; both mod-two factor multisets; and directly reconstructs the 12 triple and 30 double points over suitable finite fields of characteristics \(3,5,7,11,13,17,19\). All tests operate on integers or explicit prime-field/quadratic-field arithmetic, and the program terminates with `VERIFY_KLEIN12_MODULAR_OK` when every assertion holds. The proof of uniformity is the exact norm argument, not the finite-field spot checks.

## Relationship to prior work

Gévay and Pokora [1, Section 2.1, Proposition 2.1] gave the chosen twelve-line subarrangement and established its complex incidence basket of twelve triple and thirty double points. The theorem above is **not** a new complex incidence calculation; it determines the exact good-reduction locus for this fixed integral model and classifies both distinct scheme-theoretic dyadic fibers. Bauer and collaborators [2, Sections 2 and 9] analyze the full twenty-one-line Klein configuration and its characteristic-seven specialization, not the two dyadic degenerations of this twelve-line subarrangement. Innamorati [3] studies characteristic-seven Klein and characteristic-two Ceva finite configurations, rather than these twelve-line dyadic fibers. No prior inspected source was found to state the two dyadic factorizations together with the all-odd-prime determinant-unit certificate. An equivalent calculation under another integral normalization remains possible.

## Limitations

The result is tied to the specific integral equations supplied by [1], rather than to all possible models of the abstract configuration. It does not provide a simultaneous desingularization, prove any property of the reflection group in characteristic two, or settle arithmetic invariants of the full twenty-one-line divisor. The novelty comparison covers the cited literature and the available mathematical records, not every unpublished calculation. An independent mathematical audit has not been performed.

## References

[1] G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309, first version 2022-11-28, Section 2.1 and Proposition 2.1. https://arxiv.org/abs/2211.15309

[2] T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu, and T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648, first version 2016-09-27, Sections 2 and 9. https://arxiv.org/abs/1609.08648

[3] S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024), 321, DOI:10.3390/axioms13050321 (2024-05-11). https://doi.org/10.3390/axioms13050321
