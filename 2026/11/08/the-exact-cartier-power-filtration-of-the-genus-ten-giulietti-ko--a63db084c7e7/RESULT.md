# The exact Cartier power filtration of the genus-ten Giulietti–Korchmáros curve in characteristic two

## Finding
Over an algebraically closed field \(k\) of characteristic \(2\), the genus-ten Giulietti–Korchmáros curve \(X\) has Cartier power ranks \(\operatorname{rank}(\mathcal C^j)=(10,6,3,0)\) for \(j=0,1,2,3\), and all further ranks are zero. Thus its exact nilpotent Cartier block lengths are \((3,3,3,1)\); in particular \(\operatorname{rank}(\mathcal C^2)=3\).

## Assumptions and scope
Let \(X\) be the smooth projective model over \(k\) of \(y^3=x^2+x\) and \(z^3=y^4+y\). Set \(H=x^2+x+1\) and \(F=x(x+1)H^3\). Since \(y^4+y=y(y^3+1)=yH\), one has \(z^3=yH\), hence \(y=z^3/H\) and \(z^9=F\). The extension \(k(x,z)/k(x)\) is tame Kummer of degree nine: \(F\) has simple zeros at \(x=0,1\), zeros of order three at the two roots of \(H\), and a pole of order eight at infinity. Its tame Riemann–Hurwitz different contribution is \(8+8+6+6+8=36\), giving \(2g-2=-18+36=18\) and \(g=10\). The curve is smooth by taking its projective normalization, without asserting the displayed affine model is smooth at every finite point.

## Proof
Define \(\omega_{i,a}=x^aH^{\lfloor i/3\rfloor}z^{-i}dx\), with the ten index pairs
\[
(2,0),(4,0),(5,0),(5,1),(6,0),(7,0),(7,1),(8,0),(8,1),(8,2).
\]
All ten forms are holomorphic. At the single point above \(x=0\) or \(x=1\), tame local orders are \(\operatorname{ord}(z)=1\), \(\operatorname{ord}(dx)=8\), giving order at least \(8-i\). At each point above either root of \(H\), the ramification index is three and \(\operatorname{ord}(z)=1\), \(\operatorname{ord}(H)=3\), \(\operatorname{ord}(dx)=2\); the resulting order is \(3\lfloor i/3\rfloor+2-i\ge0\). At infinity the valuations are \(\operatorname{ord}(x)=-9\), \(\operatorname{ord}(H)=-18\), \(\operatorname{ord}(z)=-8\), \(\operatorname{ord}(dx)=-10\). The listed pairs are exactly those satisfying \(9a+18\lfloor i/3\rfloor+10\le8i\). The forms are linearly independent: different \(i\) have distinct Kummer characters under \(z\mapsto\zeta z\), while the polynomials for equal \(i\) have different degrees. Since \(g=10\), they are a basis of \(H^0(X,\Omega_X^1)\).

For \(1\le i\le8\), let \(f_i=\lfloor i/3\rfloor\). Because \(z^9=F\), the form \(\omega_{i,a}\) can be written \(G(x)z^{-2s}dx\), where if \(i\) is even set \(s=i/2\) and \(G=x^aH^{f_i}\), and if \(i\) is odd set \(s=(i+9)/2\) and \(G=x^aH^{f_i}F\). For every \(G\in\mathbb F_2[x]\), its ordinary derivative \(G'\) is a square, and the local Cartier identity in the separating parameter \(x\) yields
\[
\mathcal C(\omega_{i,a})=z^{-s}\sqrt{G'(x)}\,dx.
\]
This follows by writing \(G=U(x)^2+xV(x)^2\), so \(G'=V^2\), and using \(\mathcal C((U^2+xV^2)dx)=Vdx\), together with \(\mathcal C(h^2\eta)=h\mathcal C(\eta)\). The square roots are uniquely determined in \(\mathbb F_2[x]\).

In the order of the ten index pairs above, the exact images of the basis are
\[
0,\ \omega_{2,0},\ \omega_{7,0},\ \omega_{7,1},\ 0,\ \omega_{8,0},\ \omega_{8,2},\ 0,\ \omega_{4,0},\ 0.
\]
Each nonzero image has coefficient one; these identities are also verified by the standalone exact polynomial checker. Six distinct basis elements occur as first images, so \(\operatorname{rank}(\mathcal C)=6\). Applying Cartier again yields precisely three distinct nonzero second images, \(\omega_{8,0},\omega_{8,2},\omega_{2,0}\), and all three have zero Cartier image. Therefore \(\operatorname{rank}(\mathcal C^2)=3\) and \(\mathcal C^3=0\). The rank differences imply three nilpotent blocks of length three and one of length one, as asserted. As the matrix is defined over \(\mathbb F_2\), its semilinear iteration is calculated by ordinary matrix powers.

## Verification
Run \(\texttt{python3 artifacts/verify_cartier.py}\) with Python standard library. The script recomputes \(F\), the ten basis pairs, each derivative square root, all ten exact Cartier images, and the three matrix ranks over \(\mathbb F_2\); its recorded output is in \(\texttt{artifacts/verify_output.txt}\). The proof above establishes the all-field statement; the checker is exact but is not a separate independent scientific audit.

## Relationship to prior work
Almeida Filho–Tafazolian–Vieira (2026), Proposition 6.1, determines the \(a\)-number of this curve as \(4\), hence the first Cartier rank as \(6\). Their GK computation does not give its second Cartier rank. Earlier general maximal-curve results constrain Cartier nilpotence but do not give the exact intermediate rank. Elkin's rank formula for cyclic covers computes a single Cartier rank; the exact iterated rank requires the incidence of successive image subspaces, which is explicitly calculated here. Searches of accessible sources found no statement equivalent to the exact sequence \((10,6,3,0)\); this is not a proof of publication priority. The initial GK construction and literature on Weierstrass semigroups define the geometric setting.

## Limitations
The result is only for the minimal case \(q=2,n=3\), not the full Giulietti–Korchmáros or Garcia–Güneri–Stichtenoth families. It does not determine the complete Ekedahl–Oort type, all arithmetic Newton data, or a classification of Jacobian group schemes. Published general statements might yield the result through a not-yet-identified specialization; independent review and exhaustive historical priority verification have not been performed.

## References
Almeida Filho, Tafazolian and Vieira, *\(a\)-numbers of covers in characteristic two: semigroups and Riemann–Roch spaces*, arXiv:2610.22755 (first submitted 2026-10-15), Proposition 6.1 and Sections 2.5, 6, 10.5.

Giulietti and Korchmáros, *A new family of maximal curves over a finite field*, Math. Ann. 343 (2009), 229–245.

Elkin, *The rank of the Cartier operator on cyclic covers of the projective line*, J. Algebra 327 (2011), 1–12.

Beelen and Montanucci, *Weierstrass semigroups on the Giulietti–Korchmáros curve*, Finite Fields Appl. 52 (2018), 10–29.
