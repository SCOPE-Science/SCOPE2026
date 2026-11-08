# Endpoint-block observations uniquely maximize Hankel completion degree

## Finding

For every pair of integers \(r\ge2\) and \(n\ge2r+1\), exactly one set of \(2r\) observed Hankel anti-diagonals achieves the greatest possible generic number of complex low-rank completions: the first \(r\) and last \(r\). Its generic completion degree is
\[
\deg(\pi_{\Omega_*})=\binom{n-r}{r},
\quad\Omega_*=\{1,\ldots,r\}\cup\{n-r+1,\ldots,n\}.
\]
For any other \(2r\)-element observation set \(\Omega\),
\[\deg(\pi_\Omega)<\binom{n-r}{r}.\]
The same argument applies to \(r=1\), for which the two endpoints are also uniquely maximal; the nontrivial uniform-rank statement concerns \(r\ge2\).

## Assumptions and scope

Work over \(\mathbb C\). Let \(H_{r,n}\subset\mathbb A^n\) be the locus where every \((r+1)\)-minor of
\[
C_{r,n}(x)=\bigl(x_{i+j-1}\bigr)_{1\le i\le r+1,\;1\le j\le n-r}
\]
vanishes. Its homogeneous projectivization \(X_{r,n}\subset\mathbb P^{n-1}\) is the \(r\)-th secant variety of the degree-\((n-1)\) rational normal curve, with secant-rank convention \(\dim X_{r,n}=2r-1\). The ideal is prime, and its codimension equals \(n-2r\). For \(\Omega\subseteq\{1,\ldots,n\}\) of cardinality \(2r\), write \(\pi_\Omega\) for the affine coordinate projection and \(d_\Omega\) for its generic field-extension degree. Reed and Tsakiris prove that every such projection is generically finite (the uniformity theorem); this established result is used as a premise.

## Proof

**1. Compute the ambient projective degree.** The transpose of \(C_{r,n}\) presents a map of vector bundles on \(\mathbb P^{n-1}\),
\[
\mathcal O^{r+1}\longrightarrow\mathcal O(1)^{n-r}.
\]
The rank-at-most-\(r\) degeneracy locus has the expected codimension \(n-2r\), since the defining maximal-minor ideal is prime of that codimension. The maximal-minor case of the Thom–Porteous formula gives
\[
[X_{r,n}]=c_{n-2r}\bigl(\mathcal O(1)^{n-r}-\mathcal O^{r+1}\bigr)
=\binom{n-r}{n-2r}h^{n-2r},
\]
where \(h\) denotes the hyperplane class. Thus
\[\deg X_{r,n}=\binom{n-r}{r}.\]
This is a classical secant degree, not itself claimed to be new.

**2. Exclude the endpoint projection center from the variety.** The projective center of the endpoint projection is
\[
\Lambda_*=\{x_1=\cdots=x_r=x_{n-r+1}=\cdots=x_n=0\}.
\]
Suppose that \([x]\in X_{r,n}\cap\Lambda_*\). If all coordinates are zero this is not a projective point. Otherwise choose the *least* \(j\) for which \(x_j\ne0\). The endpoint vanishing forces \(r+1\le j\le n-r\). In \(C_{r,n}\), select all \(r+1\) rows and the consecutive columns indexed by \(j-r,j-r+1,\ldots,j\). These are valid column indices. Its entry in row \(i\) and relative column \(k\) is \(x_{j-r+i+k-2}\) for \(1\le i,k\le r+1\). Entries with \(i+k<r+2\) vanish, while entries on \(i+k=r+2\) equal \(x_j\). Hence this matrix is anti-triangular and has determinant \((-1)^{r(r+1)/2}x_j^{r+1}\ne0\), contradicting rank at most \(r\). So \(\Lambda_*\cap X_{r,n}=\varnothing\).

**3. Obtain the exact endpoint degree.** Projection from \(\Lambda_*\) is a globally defined morphism \(f_*:X_{r,n}\to\mathbb P^{2r-1}\) satisfying \(f_*^*\mathcal O(1)=\mathcal O_{X_{r,n}}(1)\). It is finite: a contracted projective curve would have zero degree against the pullback of \(\mathcal O(1)\), contradicting ampleness of \(\mathcal O_{X_{r,n}}(1)\). Since source and target have equal dimension and the source is irreducible, its image is the whole target. The projection formula gives
\[
\deg(f_*)=\int_{X_{r,n}}c_1(\mathcal O_{X_{r,n}}(1))^{2r-1}
=\deg X_{r,n}=\binom{n-r}{r}.
\]
Homogeneity identifies this projective degree with the generic degree of the affine map \(\pi_{\Omega_*}\): a generic affine fiber is the slice of the projective fiber with a prescribed scalar normalization.

**4. Show every different center meets the variety.** For \(j\in\{1,\ldots,r\}\), the Hankel matrix of the projective coordinate vector \(e_j\) has at most \(j\) nonzero entries in distinct rows and columns, hence rank \(\le r\). By reversal, the same holds for every \(j\in\{n-r+1,\ldots,n\}\). Thus each such \([e_j]\) lies in \(X_{r,n}\). Any observation set \(\Omega\ne\Omega_*\) of size \(2r\) omits at least one of these \(2r\) indices. Its projective center \(\Lambda_\Omega\) therefore contains \([e_j]\in X_{r,n}\).

**5. Strict degree loss at a base point.** Let \(X\subset\mathbb P^N\) be an irreducible projective variety of dimension \(m\) and degree \(D\), and suppose a generically finite linear projection \(f:X\dashrightarrow\mathbb P^m\) has a center containing a point \(p\in X\). Factor the linear projection by first projecting from the point \(p\), producing a rational map \(g:X\dashrightarrow Y\subseteq\mathbb P^{N-1}\) of generic degree \(a\), and then linearly projecting \(Y\) to \(\mathbb P^m\) with generic degree \(b\). Generic finiteness of \(f\) ensures both stages are generically finite, and \(\deg f=ab\). For a generic codimension-\(m\) linear space through \(p\), the local intersection multiplicity at \(p\) is the positive Hilbert–Samuel multiplicity \(\operatorname{mult}_p X\). The standard projection-from-a-point degree formula therefore yields
\[
D=a\deg(Y)+\operatorname{mult}_pX.
\]
For the second stage, a generic linear projection satisfies \(b\deg(\mathbb P^m)\le\deg(Y)\), so \(b\le\deg(Y)\). Therefore
\[
\deg f=ab\le a\deg(Y)=D-\operatorname{mult}_pX<D.
\]
Apply this with \(X=X_{r,n}\) and \(p=[e_j]\in X_{r,n}\cap\Lambda_\Omega\). Every \(\Omega\) is generically finite by Reed–Tsakiris, and the strict loss gives
\[d_\Omega<\deg X_{r,n}=d_{\Omega_*}\quad(\Omega\ne\Omega_*).\]
This proves both the exact maximal degree and its unique maximizing observation pattern.

## Verification

The included Python/SymPy program `verify.py` forms maximal Hankel minors at deterministic generic-rank witness sequences, specializes the observed endpoints, computes exact Groebner bases over \(\mathbb Q\), and counts standard monomials. It checks the cases \((r,n)=(2,5),(2,6),(2,7),(3,7),(3,8),(3,9),(4,9)\), obtaining respectively \(3,6,10,4,10,20,5\) as predicted by \(\binom{n-r}{r}\). It also checks that all omitted endpoint coordinate vectors have rank at most \(r\) in small cases. These are finite corroborations only. The universal statement follows from the geometric argument above, including the classical maximal-minor intersection formula.

## Relationship to prior work

Reed and Tsakiris (2026), *On Hankel Determinantal Matroids* (arXiv:2610.27554), establish primality/dimension as known Hankel results, prove that any \(2r\) coordinates form a matroid basis, and derive degree bounds together with exact formulas for certain different observation sets. Their introduction and degree-analysis sections do not state this unique all-rank maximizing endpoint pattern or the exact equality criterion. Standard literature on rational-normal secants provides the projective degree \(\binom{n-r}{r}\), which is explicitly treated here as a premise rather than new mathematics. The added observation is that the endpoint center is disjoint, whereas every competing coordinate center meets the secant variety at an endpoint coordinate point; combined with linear-projection degree loss, this yields the sharp global extremality and uniqueness.

## Limitations

The statement is about generic complex fibers and sets of *exactly* \(2r\) observed anti-diagonals; it does not calculate fibers of arbitrary special observations, describe monodromy, or determine exact degrees for all nonmaximizing patterns. Generic finite completeness relies on the cited 2026 uniformity theorem. The classical linear-projection degree comparison and Thom–Porteous are standard inputs. Historical priority is provisional; a differently formulated older result on extremal partial-moment projections may remain to be found. No independent mathematical audit is claimed.

## References

- Ethan Reed and Manolis C. Tsakiris, *On Hankel Determinantal Matroids*, arXiv:2610.27554, first public 2026-10-20; especially §1.2, §2, §4, and §5.
- Classical rational-normal-curve secant varieties, maximal-minor determinantal ideals, and the Thom–Porteous degeneracy-locus formula (standard intersection-theory facts).
- Zaqueu Ramos and Aron Simis, *Linear Sections of the Generic Square Hankel Matrix*, in *Determinantal Ideals of Square Linear Matrices* (2024); related linear-section background, not identified as establishing the extremal coordinate-projection degree.
