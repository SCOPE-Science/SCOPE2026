# Independent mathematical audit

## correctness

PASS

On the bilateral binary shift the dual of the stated forward local rule is multiplication by P, not its reciprocal. The nonzero endpoints also give a two-sided inhomogeneous recurrence, proving surjectivity and giving nd free bits for the time-n kernel. For a fixed output the possible pin values form a coset of the pin projection of that kernel, so the obstruction dimension is the codimension of that projection, equivalently dim(span(z^a,z^b,z^c) intersect (P^n)). Monomial shifts are units, including for negative sites. An eligible pair has exponent gap q times an integer; removing its 2-power leaves a simple root by differentiation. An eligible triple must have three different residues. After removing its common Frobenius power the derivative cannot vanish: it is a monomial if just one reduced exponent is odd, and vanishing for two odd reduced exponents would force coincident residues modulo the odd order q. Thus the triple multiplicity is exactly H_-. In the equal-residue case the three eligible pairs form one dimension-two subspace, with two tied smaller multiplicities and one strictly larger one, giving the two drops as stated. For an obstruction of depth h, a pair costs span at least qh; a triple costs at least m(P)h. Primitivity writes 1+alpha as alpha^v with 2<=v<q, proving existence and m(P)<q; degree proves m(P)>=d. A minimal trinomial has multiplicity one (otherwise halve both exponents) and scaling its exponents by the largest dyadic h with m(P)h<=L gives the matching last obstruction at n=h. The n>=1 convention gives the first full time 1 when L<m(P). Independently enumerated the residues by repeated doubling and reduction for the two example polynomials: their nonzero cycles have lengths 7 and 31, and lexicographic search by (v,u) first hits (3,1) and (8,3). Inspected check_singer.py and VERIFICATION.md without executing the bundled script. The three implementation paths cover 207628 finite cases by their loop bounds, not arbitrary degrees or spans.

## originality

PASS

Best-of-knowledge pass for the stated degree-at-least-three classification and sharp m(P) cutoff. The Rule 150 analogue is substantial overlap in mechanism and shape but is a fixed degree-two rule outside this scope. The available comparisons do not supply the independent residue-line test, the varying least-trinomial-span invariant, and the associated sharp all-L conclusion for primitive polynomials of arbitrary degree. Duality and Frobenius multiplicity alone are not claimed as original.

## value

PASS

This completely classifies the first pin count at which a genuinely ternary dependence can occur in this natural infinite-volume recurrence family. It distinguishes immediate full reachability from one or two exact stages of obstruction, and gives both a sharp universal span bound and a realizing triple for every diameter. The cutoff uses an intrinsic invariant that demonstrably need not equal the degree, rather than recomputing a selected finite window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
