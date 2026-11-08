# A smooth toral-derivation fourfold for the characteristic-two biquadratic algebra

## Finding
For a field \(k\) of characteristic \(2\), put \(A=k[x,y]/(x^2,y^2)\), \(z=xy\), and \(\mathcal T=\{D\in\operatorname{Der}_k(A):D^2=D\}\), with the natural polynomial scheme structure in eight derivation coordinates. Then \(\mathcal T\) is smooth and has exactly two connected components: an isolated reduced point and a smooth geometrically irreducible fourfold. Conjugation by the full algebra-automorphism group has exactly four orbits represented by
\[
0,\qquad x\partial_x,\qquad x\partial_x+y\partial_y,\qquad (1+x)\partial_x.
\]
Every nonzero such derivation has linear rank \(2\) on \(A\). For every \(q=2^e\), the respective orbit cardinalities are \(1\), \(q^2(q+1)\), \(q^2\), \(q^2(q^2-1)\), and
\[
\#\mathcal T(\mathbb F_q)=1+q^2+q^3+q^4.
\]
The dense orbit has nonzero constant coefficients in the images of at least one generator: it consists of derivations that do not preserve the unique maximal ideal \((x,y)\).

## Assumptions and scope
All assertions hold for every field \(k\) of characteristic exactly \(2\); the point count assumes \(k=\mathbb F_q\), \(q\) a power of two. Derivations are ordinary, not super-derivations. A point of \(\mathcal T\) is given by \(D=f\partial_x+g\partial_y\), where \(f,g\in A\) are arbitrary; the defining equations are the eight coefficients of \(D^2(x)-D(x)\) and \(D^2(y)-D(y)\). A geometric component means a component after extension to an algebraic closure. Rank refers to the \(k\)-linear operator on \(A\), not merely its linear part on the maximal ideal.

## Proof
**Parameterization.** Every derivation is uniquely \(f\partial_x+g\partial_y\): in characteristic two the derivatives of the defining square relations vanish. Write
\[
f=a+b x+c y+d z,\quad g=e+h x+i y+j z,\qquad z=xy.
\]
The action on the fourth basis vector is \(D(z)=e x+a y+(b+i)z\). The map \(D^2\) is a derivation in characteristic two, since its failure to satisfy Leibniz is \(2D(u)D(v)=0\). Thus \(D^2=D\) is equivalent to the two generator equations \(D(f)=f\) and \(D(g)=g\).

**Zero constant vector.** If \(a=e=0\), the linear part \(P=\begin{psmallmatrix}b&h\\c&i\end{psmallmatrix}\) is an idempotent on \(\langle x,y\rangle\), and the quadratic-coefficient row \(Q=(d,j)\) obeys
\[
P^2=P,\qquad QP+(\operatorname{tr}P)Q=Q.
\]
For rank \(P=0\), only \(D=0\) occurs. For rank \(P=1\), the trace is \(1\) and \(Q\) vanishes on \(\operatorname{im}P\), giving a one-dimensional space of possibilities. For rank \(P=2\), \(P=I\) and \(Q\) is arbitrary. The number of rank-one projectors on a two-space over \(\mathbb F_q\) is \(q(q+1)\), so these three strata have sizes \(1\), \(q^2(q+1)\), and \(q^2\).

**Nonzero constant vector.** An automorphism induced by a linear coordinate change sends any \((a,e)\ne(0,0)\) to \((1,0)\). Solving the eight equations in that normalization gives exactly
\[
D(x)=1+x+c y+c i z,\qquad D(y)=i y+(i+i^2)z,
\]
with freely chosen \(c,i\in k\). Hence the nonzero-constant stratum is locally an affine-two-space bundle over \(\mathbb A^2\setminus\{0}\}\); it is smooth, geometrically irreducible, and four-dimensional. It has \(q^2(q^2-1)\) points over \(\mathbb F_q\). The automorphism \(\phi(x)=x+c z\), \(\phi(y)=y+i z\) intertwines the displayed \(D\) with \(D_*= (1+x)\partial_x\), proving transitivity over \(k\).

**Other conjugacy classes.** Every automorphism of \(A\) is given by an invertible linear change of the generators followed by an arbitrary pair of quadratic corrections. Rank-one idempotents \(P\) are conjugate under \(\operatorname{GL}_2(k)\); in coordinates where \(P=\operatorname{diag}(1,0)\), the allowed \(Q\) is removable by the shear \(y\mapsto y+vz\). For \(P=I\), any \(Q\) is removable by quadratic shears. Therefore there are precisely the four stated orbits. Their representatives have linear-operator ranks \(0,2,2,2\). These ranks are constant on each orbit.

**Geometry and smoothness.** The nonzero-constant locus is an open geometrically irreducible fourfold. The families \(D_s=(s+x)\partial_x\) and \(E_s=(s+x)\partial_x+y\partial_y\) are idempotent for all \(s\), belong to this open locus when \(s\ne0\), and specialize to the two zero-constant nonzero representatives at \(s=0\). Conjugation shows that the closure of the open locus contains every nonzero idempotent derivation; hence the nonzero locus is a geometrically irreducible fourfold.

For the scheme-theoretic assertion, linearization at \(D\) of \(D^2-D\) is \(H\mapsto DH+HD-H\) on the eight-dimensional derivation space. At \(D=0\) it has zero-dimensional kernel. At each of the three nonzero representatives, its kernel has dimension \(4\): each corresponding operator \(D\) splits \(A\) into two-dimensional zero- and one-eigenspaces, and the induced adjoint action on \(A\partial_x\oplus A\partial_y\) has a four-dimensional one-eigenspace. Thus the Zariski tangent dimension equals the geometric local dimension at every point. The idempotent-derivation scheme is smooth, the zero point is reduced and isolated, and the nonzero component is smooth and geometrically irreducible.

## Verification
The standalone pure-Python program `verify.py` performs actual arithmetic in \(\mathbb F_2\) and \(\mathbb F_4\). It exhausts all \(q^8\) derivation coefficient vectors, evaluates \(D^2=D\) using the full four-dimensional action, classifies strata, verifies every nonzero operator has rank two, and checks the Jacobian kernel dimension at all four orbit representatives in characteristic two. It returns the counts \(29\) and \(337\) and the marker `ALL_TORAL_DERIVATION_CHECKS_PASS`. The computational tests are finite examples; the classification and all-characteristic-two scheme assertions are proved above independently of enumeration. The Jacobian checks are also justified symbolically in the proof.

## Relationship to prior work
The Jacobson–Witt algebra framework treats derivations of truncated polynomial algebras, and classical work classifies maximal tori. Bin Shu, *Conjugacy of Borel subalgebras of restricted Lie algebras and the associated solvable algebraic groups (I)* (arXiv:1404.1149), describes this framework and focuses its principal simple-algebra results on \(p>3\), not the full characteristic-two toral-element scheme. Karin Erdmann, *Ext-finite modules for weakly symmetric algebras with radical cube zero* (arXiv:1511.01418), discusses four-dimensional quantum-exterior-type algebras but not their idempotent derivation loci. Hao Chang, *Toral stabilizers of restricted Lie algebras* (arXiv:1608.02258), investigates maximal-torus structures and assumes \(p>3\) for its generalized Witt calculation. None of the inspected statements gives the four affine orbit strata, smoothness, or the stated finite-field polynomial for \(\mathcal T\). Classical maximal-torus classification is acknowledged as relevant background and creates a residual possibility of a stronger pre-existing implication.

## Limitations
Only the ordinary derivation algebra of this two-generator, exponent-two truncated commutative algebra is classified. No result is asserted for \(p>2\), for more generators, or for different truncation exponents. The theorem describes idempotent derivations, not arbitrary semisimple or nilpotent derivations or a classification of all maximal tori. Historical priority has not been independently established.

## References
1. Bin Shu, *Conjugacy of Borel subalgebras of restricted Lie algebras and the associated solvable algebraic groups (I)*, arXiv:1404.1149, first posted 2014-04-04.
2. Karin Erdmann, *Ext-finite modules for weakly symmetric algebras with radical cube zero*, arXiv:1511.01418, first posted 2015-11-04.
3. Hao Chang, *Toral stabilizers of restricted Lie algebras*, arXiv:1608.02258, first posted 2016-08-07.
