# The characteristic-five Cayley Hessian has fourteen rational nodes and maximal quadratic-extension reduction

## Finding
Let \(e_i\) be the elementary symmetric polynomial of degree \(i\) in \(x_0,x_1,x_2,x_3\). Over \(\mathbb F_5\), consider the Cayley cubic \(F=e_3=0\) and its Hessian quartic
\[
H:\quad h=e_1e_3-4e_4=0\quad\subset\mathbb P^3_{\mathbb F_5}.
\]
The quartic has exactly **fourteen geometric ordinary double points, all defined over \(\mathbb F_5\)**. They form three orbits under coordinate permutations: the four vertices \([1:0:0:0]\); six points \([1:-1:0:0]\); and four points \([1:1:1:-1]\). No further geometric singularity exists.

Let \(Y\to H\) denote the minimal resolution. Then \(Y\) is a K3 surface and
\[
\#Y(\mathbb F_5)=126,\qquad \#Y(\mathbb F_{25})=1176=1+25^2+22\cdot25.
\]
Its complete zeta function is
\[
Z(Y/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^{21}(1+5T)}.
\]
Writing \(q=5^m\), for every integer \(m\ge1\) we have
\[
\#Y(\mathbb F_q)=q^2+1+q(21+(-1)^m),\qquad
\#H(\mathbb F_q)=q^2+1+q(7+(-1)^m).
\]
Thus \(Y\) has geometric Picard rank \(22\) (supersingular), and the Frobenius-fixed Picard rank over \(\mathbb F_5\) is \(21\).

## Assumptions and scope
The field is exactly \(\mathbb F_5\), with its finite extensions and algebraic closure. The Hessian means the determinant of the full \(4\times4\) second-derivative matrix of the displayed integral Cayley cubic; the determinant equals \(-4(e_1e_3-4e_4)\) over \(\mathbb Z\), so reduction modulo \(5\) defines the nonzero quartic \(h\). The zeta function of the *singular* quartic \(H\) is obtained by deleting one \(\mathbb F_q\)-point and adding \(q+1\) points for each of the fourteen split exceptional conics:
\[
Z(H/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^7(1+5T)}.
\]
This statement does not assert the complete Artin invariant or classify all projective models of the resolution.

## Proof
**1. Hessian equation.** With \(F=e_3\), direct expansion of its second-derivative determinant gives the integral identity \(\det(\partial_i\partial_jF)=-4(e_1e_3-4e_4)\). Since \(-4\) is a unit in characteristic \(5\), the asserted equation is exactly the Hessian zero locus.

**2. Geometric singularities.** The projective Jacobian equations are \(\partial_i h=0\) for \(0\le i\le3\). Euler's identity \(\sum x_i\partial_i h=4h\) shows that the equation \(h=0\) is automatic. Cover \(\mathbb P^3\) by the four disjoint standard normalizations \(x_0=1\), then \(x_0=0,x_1=1\), then \(x_0=x_1=0,x_2=1\), and finally \([0:0:0:1]\). On each chart use all four restricted homogeneous derivatives. Over \(\mathbb F_5\) their reduced lexicographic Gröbner bases are, in the first chart with variables \(b=x_1,c=x_2,d=x_3\),
\[
\begin{aligned}
b^2+b-c^2+cd^2+cd-c,&\\
bc-c^2+cd^2-c+d^2+d,&\\
bd+cd^2,&\\
c^3-c,&\\
c^2d+c^2-cd^2+c-d^2-d,&\\
d^3-d.&
\end{aligned}
\]
The next charts have reduced bases \(\{c^2+c,cd,d^2+d\}\), \(\{d^2+d\}\), and \(\{0\}\), respectively. Exact division by the basis gives zero remainders for every polynomial \(z^5-z\) in the free chart variables. Thus **every geometric singular point is \(\mathbb F_5\)-rational**: the Jacobian ideal's coordinate quotient is forced onto the finite-field locus in each chart. Exhaustive evaluation of these finitely many rational candidates yields exactly \(8+3+2+1=14\) points, the three stated symmetric orbits. The affine quadratic Hessian determinants are nonzero modulo \(5\) at one representative from each of these three orbits; by permutation symmetry they are nonzero at all fourteen points. Every singular point is therefore an ordinary double point. A projective quartic with only finitely many singularities is geometrically integral (different positive-degree components would meet along a curve and force nonisolated singularities); the hypersurface is Cohen–Macaulay and regular in codimension one, hence normal.

**3. Resolution and finite-field counts.** The minimal resolution of a normal quartic with only ordinary double points has trivial canonical class and vanishing first structure-sheaf cohomology; it is a K3 surface. Because each singularity is an \(\mathbb F_5\)-rational ordinary double point with nonsingular tangent cone, its exceptional curve is a smooth rational conic, and in this example the conic is split: the symmetric representatives have isotropic tangent quadrics over \(\mathbb F_5\), by the standard finite-field theorem that every smooth projective plane conic has a rational point. Hence replacing each node contributes exactly \(q\) points over every \(\mathbb F_q\). Exhaustive evaluation of \(h\) on the canonical representatives of \(\mathbb P^3(\mathbb F_5)\) and \(\mathbb P^3(\mathbb F_{25})\), using \(\mathbb F_{25}=\mathbb F_5[t]/(t^2+3)\), gives respectively \(56\) and \(826\) points. Accordingly \(\#Y(\mathbb F_5)=56+14\cdot5=126\) and \(\#Y(\mathbb F_{25})=826+14\cdot25=1176\).

**4. Frobenius and all extensions.** The Weil conjectures for K3 surfaces give \(22\) degree-two Frobenius eigenvalues \(\alpha_i\), each of complex absolute value \(5\). Point counting gives \(\sum_i\alpha_i=126-(1+5^2)=100\) and \(\sum_i\alpha_i^2=1176-(1+25^2)=550=22\cdot25\). Equality in the triangle inequality implies \(\alpha_i^2=25\) for every \(i\). Consequently \(\alpha_i\in\{+5,-5\}\), with exactly \(21\) positive and one negative eigenvalue. The Grothendieck–Lefschetz trace formula gives the asserted counts and Euler-product rational function. Since every eigenvalue is \(5\) times a root of unity, the K3 Tate theorem in odd characteristic gives geometric Picard number \(22\) and Picard number \(21\) over \(\mathbb F_5\).

## Verification
Run `python verify.py` using Python 3 and SymPy. The script verifies the integral Hessian identity, all four chart Gröbner reductions and rational singular support, nonsingularity of the three local tangent quadrics, and exhaustive \(\mathbb F_5\) and \(\mathbb F_{25}\) point counts. The recorded output is `verification_output.txt`, ending in `VERIFY_OK`. The Frobenius conclusion is a proof from those verified point counts and the K3 Weil bounds, not an extrapolation from samples.

## Relationship to prior work
Dardanelli and van Geemen (2004), Section 3.1–3.2, analyze the classical Cayley cubic Hessian K3 and its rank-20 transcendental lattice \(\langle2\rangle\oplus\langle6\rangle\). In characteristic zero the Cayley Hessian has fourteen nodes. This result uses that classical surface but proves the precise geometric special fiber and arithmetic Frobenius over \(\mathbb F_5\). Shimada's work (2012) describes degree-two projective models of the characteristic-five supersingular K3 of Artin invariant one; it does not supply this four-degree Hessian equation or these \(\mathbb F_5\)-point counts in the material examined. More general CM and modularity theorems may yield another route to some Frobenius properties, and no claim of independent historical priority is implied.

## Limitations
The result does not compute the Artin invariant or the full automorphism group. It does not certify novelty against every unpublished calculation or every consequence of general CM modularity. The fifteen-node characteristic-three specialization of a different symmetric Hessian model must not be substituted for this fourteen-node characteristic-five surface. All arithmetic point counts refer to the explicitly given \(\mathbb F_5\)-model and are not invariant under arbitrary twists.

## References
1. E. Dardanelli and B. van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322v1, 18 September 2004, §3, https://arxiv.org/abs/math/0409322.
2. I. Shimada, *Projective models of the supersingular K3 surface with Artin invariant 1 in characteristic 5*, arXiv:1201.4533v1, 22 January 2012, https://arxiv.org/abs/1201.4533.
3. B. Hunt, *The Geometry of Some Special Arithmetic Quotients*, Springer, 1996, pp. 115–122 (classical background).
