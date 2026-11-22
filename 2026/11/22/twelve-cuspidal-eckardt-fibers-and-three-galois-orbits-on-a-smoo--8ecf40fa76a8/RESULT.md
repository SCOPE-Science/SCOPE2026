# Twelve cuspidal Eckardt fibers and three Galois orbits on a smooth cubic fourfold

## Finding

Let \(Y\subset\mathbb P^5_{\mathbb Q}\) be the smooth cubic fourfold
\[
Y:\quad x_0^3+x_1^3+x_2^3+x_3^3+x_0z_0^2+x_1z_0z_1+x_2z_1^2=0.
\]
Its Eckardt hyperplane pencil consists of cubic threefolds
\[
T_{[u:v]}:\quad \sum_{j=0}^3x_j^3+w^2(u^2x_0+uvx_1+v^2x_2)=0
\quad\text{in }\mathbb P^4.
\]
Put
\[
D_+(u,v)=u^6+u^3v^3+v^6,\qquad
D_-(u,v)=u^6-3u^3v^3+v^6,\qquad D=D_+D_-.
\]
Over \(\mathbb C\), the family has exactly **twelve singular members**, at the distinct zeros of \(D\) on \(\mathbb P^1\). Each singular threefold has **exactly two isolated hypersurface singularities of type \(A_2\)** (each Milnor number \(2\)); all other members are smooth. The two points in each singular member are interchanged by the involution \(w\mapsto-w\).

The corresponding plane section of the fixed Fermat cubic surface is a plane cubic with exactly one ordinary cusp \(A_2\). As a Cartier divisor on the parameter line, the discriminant of this family is, up to a nonzero constant,
\[
\boxed{\operatorname{Disc}(T_{[u:v]})\doteq D(u,v)^4.}
\]
In particular, its total degree is \(48\), and every reduced bad parameter has discriminant multiplicity \(4\).

Over \(\mathbb Q\), the twelve bad parameters have **two Galois orbits of degree six**, defined by \(D_+=0\) and \(D_-=0\). The 24 geometric singular points of the fibers, viewed in the total space with their parameters, have Galois orbit sizes **\(6,6,12\)**. The two singular points over a root of \(D_+\) are individually rational over its parameter field, whereas those over a root of \(D_-\) are exchanged by adjoining \(\sqrt{-3}\).

## Assumptions and scope

The geometric claims are over \(\mathbb C\), or any algebraically closed characteristic-zero field with the corresponding algebraic singularity interpretations. The arithmetic claim is over \(\mathbb Q\). The symbol \(\doteq\) denotes equality up to a nonzero scalar, so no discriminant normalization is asserted. The pencil and fourfold are the **explicit equation** above, not a generic rank-three family.

## Proof

**1. The ambient fourfold is smooth.** This is the example in Li Bassi, Equation (2.5). Directly, its derivatives with respect to \(x_j\) force \(x_3=0\). If either \(z_0\) or \(z_1\) vanishes, the remaining derivatives preclude a projective critical point. Otherwise normalize \(z_0=1,z_1=t\). The derivatives in \(z_0,z_1\) give \(x_1=-2x_0/t\) and \(x_2=x_0/t^2\); those in \(x_0,x_1,x_2\) then require simultaneously \(t^3=4\) and \(t^6=1\), impossible in characteristic zero.

**2. Complete parameter and singular-point classification.** In the affine parameter chart \([u:v]=[1:t]\), the gradient of the cubic threefold shows that a singular point has \(w\ne0\). After setting \(w=1\), Euler's identity reduces the full singular-point system to
\[
x_3=0,\quad 3x_0^2=-1,\quad 3x_1^2=-t,\quad 3x_2^2=-t^2,
\quad x_0+tx_1+t^2x_2=0.
\]
There are no solutions for \(t=0\). The endpoint \([0:1]\) is likewise smooth by the symmetric gradient check. For \(t\ne0\), necessarily \(x_0x_2\ne0\); write \(x_2=\delta tx_0\) with \(\delta\in\{1,-1\}\). Then
\[
\frac{x_1}{x_0}=-\frac{1+\delta t^3}{t},\qquad
0=t^6+(2\delta-1)t^3+1.
\]
Thus \(\delta=1\) gives \(D_+(1,t)=0\) and \(\delta=-1\) gives \(D_-(1,t)=0\). Conversely, each such root provides precisely the two solutions
\[
\boxed{[x_0:x_1:x_2:x_3:w]
=[\epsilon a:-\epsilon a(1+\delta t^3)/t:\epsilon a\delta t:0:1],
\quad a^2=-1/3,\quad\epsilon=\pm1.}
\]
The two sextics are coprime because their difference is \(4t^3\); each is squarefree, as seen by differentiating. They have no zero at \(0\) or \(\infty\), so there are twelve distinct bad parameters and precisely two critical points each.

**3. Exact analytic types and the fixed-surface cusps.** In \(w=1\) coordinates, the Hessian at either critical point in the \((x_0,x_1,x_2)\) variables is \(\operatorname{diag}(6x_0,6x_1,6x_2)\), of rank three. The remaining variable occurs as \(x_3^3\) without mixed terms. The analytic splitting lemma gives a germ equivalent to
\[
q_3(y_0,y_1,y_2)+y_3^3=0,
\]
where \(q_3\) is nondegenerate. This is the isolated threefold \(A_2\) singularity, of Milnor number \(2\). Changing the sign of all the \(x_j\) exchanges the two points in the normalized \(w=1\) chart, corresponding projectively to the involution \(w\mapsto-w\).

For the fixed cubic surface \(S:\sum x_j^3=0\), the plane \(x_0+tx_1+t^2x_2=0\) cuts, in the chart \(x_2=1\), the plane cubic
\[
(-tr-t^2)^3+r^3+z^3+1=0.
\]
Its binary-cubic discriminant in \(r\) is exactly
\[
-27(t^6+t^3+1)(t^6-3t^3+1)=-27D(1,t).
\]
At each zero the cubic in \(r\) has exactly one double, not triple, root: for its coefficients \(ar^3+br^2+cr+d\), \(b^2-3ac=9t^5\ne0\). The local plane equation therefore has type \(r'^2+z^3=0\), a unique ordinary cusp. Away from these parameters the plane sections are smooth.

**4. The scheme-theoretic discriminant.** The parameter derivative of the threefold's defining equation at one of the two singular points is
\[
\frac{\partial T_t}{\partial t}=x_1+2tx_2
=\frac{\epsilon a}{t}(\delta t^3-1).
\]
It is nonzero at every bad parameter: \(\delta t^3=1\) is incompatible with either sextic. Hence, in a local analytic splitting of each \(A_2\) point, the one-parameter deformation has nonzero first-order constant term. The discriminant of a cubic local equation \(z^3+A(s)z+B(s)\), with \(B'(0)\ne0\), vanishes to exact order two. The two distinct \(A_2\) singular points contribute multiplicities \(2+2=4\). The twelve parameters exhaust the bad locus, proving the divisor \(4(D=0)\). The independent classical dual-degree identity \(\deg(Y^\vee)=3(3-1)^4=48\) agrees with \(12\cdot4=48\).

**5. Arithmetic orbits.** Both sextics reduce modulo two to \(t^6+t^3+1=\Phi_9(t)\), irreducible over \(\mathbb F_2\) because the multiplicative order of \(2\) modulo \(9\) is \(6\). Thus each sextic is irreducible over \(\mathbb Q\). The first is precisely \(\Phi_9\), so the corresponding degree-six parameter field contains \(\sqrt{-3}\), and the two displayed singular points are individually rational over that field, yielding two degree-six point orbits. The second sextic has a positive real root (since \(t^3=(3+\sqrt5)/2\)); its degree-six parameter field admits a real embedding and therefore excludes \(\sqrt{-3}\). Each singular point then has field of definition of degree twelve, giving the remaining single orbit of twelve points.

## Verification

Run the accompanying standalone `verify.py` with SymPy. It checks the elimination ideal's monic parameter polynomial, independently computes the binary-cubic discriminant, checks coprimality and squarefreeness of the two sextics, certifies irreducibility modulo two, and verifies the critical-point coordinate identities and nonvanishing of the transverse derivatives. These exact finite polynomial computations support the cited algebraic reductions; the local analytic and Galois arguments above establish the geometric and arithmetic conclusions.

## Relationship to prior work

Li Bassi's 2026 paper provides the smooth fourfold equation, the Eckardt pencil and the smoothness criterion in terms of plane sections of the fixed cubic surface (Lemma 2.1, Equation (2.5)). It does not state the twelve bad parameters, the paired \(A_2\) classification, the fourth-power discriminant or the arithmetic orbit partition. Marquand's earlier classification of cubic fourfold involutions provides the surrounding symmetry framework, not this exact explicit singular-fiber calculation. The dual-degree and simple singularity facts used in the proof are classical, not claimed as new.

## Limitations

The result treats one distinguished explicit smooth fourfold, not a generic cubic fourfold with a symplectic involution. It gives no stable reductions, Hodge-theoretic monodromy or extension of the Prym family through the singular members. Historical computations of isomorphic pencils may be unindexed, so absolute priority is not certified. No independent mathematical validation has been performed.

## References

- Lucas Li Bassi, *Cubic fourfolds with a symplectic involution from finite Prym data*, arXiv:2611.14747v1 (first public 2026-11-10), especially Lemma 2.1 and Equation (2.5). https://arxiv.org/html/2611.14747v1
- Lisa Marquand, *Cubic fourfolds with an involution*, Trans. Amer. Math. Soc. 376 (2023), 1373--1406. https://doi.org/10.1090/tran/8811
- Alexandru Dimca and Giovanna Ilardi, *On the duals of smooth projective complex hypersurfaces*, arXiv:2301.06952. https://arxiv.org/abs/2301.06952
