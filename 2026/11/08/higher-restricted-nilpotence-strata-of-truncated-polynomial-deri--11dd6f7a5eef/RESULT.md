# Higher restricted-nilpotence strata of truncated polynomial derivations in characteristic two

## Finding
Let \(k\) be any field of characteristic two, \(m\geq1\) an integer, \(n\in\{2m,2m+1\}\), \(e\geq2\), and \(s=2^e\). Set \(A_n=k[x]/(x^n)\), and give its Lie algebra of ordinary derivations the restricted power \(D\mapsto D^2\), defined by composition. Put \(T=k[t]/(t^m)\). Under the linear coordinates below, the higher restricted-nilpotence locus \(\mathcal X_{m,s}=\{D:D^s=0\}\) has exact equation
\[
P Q^{s-1}=Q^s=0\quad\text{in }T.
\]
Write \(c=\lceil m/s\rceil\) and \(d=\lceil m/(s-1)\rceil\). The reduced geometric locus has precisely \(d-c+1\) geometrically irreducible components
\[
\mathcal X_h=\{(P,Q):P\in t^{\max(0,m-(s-1)h)}T,\;Q\in t^hT\},\quad c\leq h\leq d,
\]
each an affine linear space of dimension
\[
\delta_h=2m-h-\max(0,m-(s-1)h).
\]
The dimensions are nondecreasing in \(h\). Consequently the reduced locus is equidimensional precisely if \(d=c\), or \(d=c+1\) and \(m\equiv1\pmod{s-1}\). In particular, at \(m=8\), \(s=4\) the two components have unequal dimensions \(12\) and \(13\), meeting in dimension \(11\). This is a genuine geometric change from the square-zero layer.

Over \(k=\mathbb F_q\), for any \(0\leq r\leq m\), the exact number \(F_{m,s,q}(r)\) of derivations with \(D^s=0\) and \(\operatorname{rank}_kD\leq r\) is
\[
F_{m,s,q}(r)=q^r+(q-1)\sum_{h=\max(m-r,c)}^{m-1}q^{m-h-1+\min\{r,(s-1)h\}}.
\]
An empty sum is zero. Setting \(F_{m,s,q}(-1)=0\), the number of exact rank \(r\) is \(F_{m,s,q}(r)-F_{m,s,q}(r-1)\). Thus the complete rank distributions agree for \(A_{2m}\) and \(A_{2m+1}\), for every \(q\). Subtracting the analogous cumulative formulas at exponents \(2^{e-1}\) and \(2^e\) yields the exact rank counts of derivations of restricted nilpotence height **exactly** \(e\).

## Assumptions and scope
All fields have characteristic \(2\). Here the exponent \(s=2^e\) has \(e\geq2\); the case \(e=1\) is a previously studied square-zero boundary, included only in comparisons and computational checks. Ordinary derivations \(D\) satisfy the Leibniz identity and \(D^s\) denotes \(s\)-fold composition (a derivation when \(s\) is a power of the characteristic). No restriction to nilpotent coefficients is imposed beyond \(D^s=0\).

For even \(n=2m\), the arbitrary derivation is uniquely \(D=f(x)\partial_x\) with
\[
f(x)=P(x^2)+xQ(x^2),\qquad P,Q\in T.
\]
For odd \(n=2m+1\), the condition \(D(x^n)=0\) forces \(f(0)=0\) and the unique form is
\[
f(x)=x^2P(x^2)+xQ(x^2),\qquad P,Q\in T.
\]
The common coefficient spaces are affine \(2m\)-spaces. The valuation \(\nu(G)\) of \(G\in T\) is its least nonzero \(t\)-degree, with \(\nu(0)=m\). The phrase *reduced geometric locus* means the reduced closed variety over an algebraic closure of \(k\); no claim is made about nilpotents in its defining scheme.

## Proof
**1. Restricted power identity.** In characteristic two, \(D^2\) satisfies the Leibniz rule because the mixed term is multiplied by \(2\). Its action on \(x\) is \(D(f)=ff'\), so \(D^2=ff'\partial_x\). The ordinary derivative of \(f'\) is zero in characteristic two, i.e. \(f''=0\). For every \(j\geq1\), by induction using \(D^2\) and \((f')'=0\),
\[
D^{2^j}=f(f')^{2^j-1}\partial_x.
\]
Indeed, if \(g=f(f')^{2^j-1}\), then \(g'= (f')^{2^j}\) (the exponent is odd), and \(g g'=f(f')^{2^{j+1}-1}\). In either parity of \(n\), \(f'=Q(x^2)\). Decomposing the coefficient of \(f(f')^{s-1}\) into even and odd degrees gives exactly the two equations \(PQ^{s-1}=0\) and \(Q^s=0\) in \(T\). For odd \(n\), multiplying the even term by \(x^2\), and the odd term by \(x\), preserves the same length-\(m\) coefficient conditions. This proves necessity and sufficiency.

**2. Geometric components.** If \(Q=0\), every \(P\) is permitted. Otherwise write \(h=\nu(Q)<m\). In the truncated principal ideal ring \(T\), the equations are equivalent to
\[
h\geq c,\qquad\nu(P)\geq\max\{0,m-(s-1)h\}.
\]
For \(h\geq d\), the lower bound on \(P\) is zero, and the resulting pairs lie in \(\mathcal X_d\). For \(c\leq h<d\), the conditions imply membership in \(\mathcal X_h\). Conversely every point in any of these linear spaces obeys the equations. The set is therefore their union. The \(P\)-divisibility threshold strictly decreases until \(h=d\), whereas the \(Q\)-divisibility threshold strictly increases. Thus no \(\mathcal X_h\) contains another, and all are irreducible affine linear spaces, hence precisely the irreducible components of the reduced geometric locus. Their coordinate dimensions give \(\delta_h\).

For \(h<d\), \(\delta_h=m+(s-2)h\). Because \(s\geq4\), these dimensions strictly increase until the terminal index. Write \(m=(s-1)(d-1)+v\), where \(1\leq v\leq s-1\); then
\[
\delta_d-\delta_{d-1}=v-1\geq0.
\]
Consequently all components have equal dimension only in the stated one-component case, or the two-component case with \(v=1\), exactly \(m\equiv1\pmod{s-1}\). For \(m=8,s=4\), \(c=2,d=3\), so \(\mathcal X_2=\{P\in t^2T,Q\in t^2T\}\) and \(\mathcal X_3=\{P\in T,Q\in t^3T\}\), of dimensions \(12\) and \(13\); their intersection has dimension \(11\).

**3. Linear-map ranks.** On either algebra, all even monomials are killed by \(D\), while
\[
D(x^{2j+1})=x^{2j}f(x).
\]
The map from the \(m\)-dimensional span of odd monomials to the even-plus-odd target is therefore represented, up to harmless powers of \(x\), by the \(T\)-linear column \(P\oplus Q\). Its kernel consists of the \(a(t)\in T\) annihilating both \(P\) and \(Q\), which is the ideal \(t^{m-\min(\nu(P),\nu(Q))}T\) with dimension \(\min(\nu(P),\nu(Q))\). Thus
\[
\operatorname{rank}_k D=m-\min\{\nu(P),\nu(Q)\}.
\]
This also proves the even/odd rank-distribution equality.

**4. Finite-field counts.** Rank at most \(r\) requires \(\nu(P),\nu(Q)\geq m-r\). The case \(Q=0\) has \(q^r\) possibilities for \(P\). For a nonzero \(Q\) of exact valuation \(h\), there are \((q-1)q^{m-h-1}\) choices of \(Q\). Restricted nilpotence forces \(h\geq c\); the valuation conditions on \(P\) allow precisely \(q^{\min(r,(s-1)h)}\) elements. Summing over \(\max(m-r,c)\leq h\leq m-1\) proves the formula. The difference of adjacent cumulative counts gives exact ranks. Since \(D^{2^{e-1}}=0\) implies \(D^{2^e}=0\), subtracting the two counts isolates exactly height \(e\). There are no finite-experiment assumptions in any step.

## Verification
The standalone file `verify_derivation_height.py` independently builds the multiplication and original derivation matrices, computes their power matrices over \(\mathbb F_2\) and \(\mathbb F_4\), and computes ranks by Gaussian elimination. It exhaustively compares formulas for \(2\leq n\leq11\) over \(\mathbb F_2\) and \(2\leq n\leq6\) over \(\mathbb F_4\), at heights \(s=2,4,8,16\) (the \(s=2\) cases serve as baseline checks). It also exhaustively checks the proposed geometric component cover for \(1\leq m\leq8\) at \(s=4,8\), using all binary coordinate pairs. Every comparison passes; the captured exact output is `verify_derivation_height.log`.

For \(m=8,s=4\), the reduced finite-field locus has exactly \(q^{12}+q^{13}-q^{11}\) rational points (two linear components meeting in dimension eleven); this is \(10{,}240\) when \(q=2\). The computation is corroborative, not a proof over arbitrary fields.

## Relationship to prior work
Premet's *Regular derivations of truncated polynomial rings* (arXiv:1405.2426, first public 2014-05-10, primary MSC 17B50) studies restricted Cartan-type derivation algebras in characteristic \(p>2\), including invariant-theoretic and nilpotent-cone geometry. Its hypotheses and principal regularity/quotient results do not give the present characteristic-two higher-height component equations or finite-field rank counts. Feldvoss, Siciliano and Weigel (arXiv:1102.2629) study restricted derivations of nilpotent restricted Lie algebras, a different object. Preexisting classification of the \(D^2=0\) layer is not claimed anew: the contribution begins at heights \(2^e\) with \(e\geq2\) and includes the non-equidimensional geometry, all-height rank census, and sharp equidimensionality criterion. The literature check cannot rule out every unindexed general theorem on restricted-nilpotence fibres.

## Limitations
The geometry is the reduced set, not the scheme-theoretic multiplicity or its singularities. The formula uses one-variable truncated polynomial algebras in characteristic two, not multivariable Witt algebras or odd characteristics. It counts labeled derivations, not automorphism-conjugacy classes. Source coverage and historical priority remain provisional, and no independent audit has been performed.

## References
1. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426 (first public 2014-05-10), https://arxiv.org/html/1405.2426v3.
2. J. Feldvoss, S. Siciliano, T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629 (first public 2011-02-13), https://arxiv.org/abs/1102.2629.
3. C. Chen, *Nilpotent varieties of some finite dimensional restricted Lie algebras*, arXiv:1910.00954 (2019), https://arxiv.org/abs/1910.00954; context outside the present characteristic and algebra family.
