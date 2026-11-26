# The characteristic-five Bring fiber is a six-line cone with the exceptional \(S_5\)-action

## Finding
Let \(\mathcal B\subset\mathbf P^4_{\mathbf Z}\) be the homogeneous power-sum model
\[
\sum_{i=1}^{5}x_i=\sum_{i=1}^{5}x_i^2=\sum_{i=1}^{5}x_i^3=0.
\]
Its scheme-theoretic fiber \(B=\mathcal B\times_{\mathbf Z}\mathbf F_5\) is the reduced union of **exactly six distinct lines defined over** \(\mathbf F_5\), all concurrent at \(v=[1:1:1:1:1]\). It is singular precisely at \(v\), where it has six branches, multiplicity \(6\) and normalization discrepancy \(\delta_v=9\). Its normalization is six disjoint copies of \(\mathbf P^1\), and its arithmetic genus is \(4\). For every \(q=5^m\) with \(m\ge1\),
\[
\# B(\mathbf F_q)=6q+1.
\]
The coordinate-permuting \(S_5\) acts faithfully on the six components, and under their identification with \(\mathbf P^1(\mathbf F_5)\) this action is the exceptional isomorphism \(S_5\cong\operatorname{PGL}_2(\mathbf F_5)\); in particular it is sharply three-transitive.

## Assumptions and scope
All scheme-theoretic statements are over \(\mathbf F_5\) and remain true after extending the ground field to an algebraic closure. The specified model is the literal integral closure of the three displayed homogeneous equations, **not** a claim about stable reduction or about a regular/stable model of the smooth characteristic-zero curve. Its special fiber is a complete intersection of type \((2,3)\) in the hyperplane \(\sum_i x_i=0\cong\mathbf P^3\). A statement about geometric branches uses the normalization of the reduced special fiber.

## Proof
**1. An exact change of coordinates.** Work modulo \(5\) and write
\[
(x_1,x_2,x_3,x_4,x_5)=(a+t,b+t,c+t,t,-a-b-c+t).
\]
This is an invertible linear coordinate system on the hyperplane \(\sum_i x_i=0\), because the coefficient of \(t\) in the sum is \(5\), which vanishes. Put \(s=a+b+c\) and
\[
Q=a^2+b^2+c^2+s^2,\qquad T=a^3+b^3+c^3-s^3=-3(a+b)(a+c)(b+c).
\]
The other power sums become precisely \(Q\) and \(T+3tQ\). Therefore the homogeneous ideal defining \(B\subset\mathbf P^3\) is \((Q,T)\), with both generators independent of \(t\). Hence \(B\) is the projective cone with vertex \([a:b:c:t]=[0:0:0:1]\) over \(Z=V(Q,T)\subset\mathbf P^2_{[a:b:c]}\). The vertex maps back to \(v=[1:1:1:1:1]\).

**2. Six reduced rational directions.** The Gram matrix of \(Q\), with diagonal \(2\) and off-diagonal \(1\), has eigenvalues \(4,1,1\) modulo \(5\). Thus \(Q=0\) is a nonsingular conic. The cubic \(T=0\) consists of the three distinct lines \(a+b=0\), \(a+c=0\), and \(b+c=0\). Direct substitution, or intersecting each with the smooth conic, produces six distinct points:
\[
Z=\{[1:2:3],[1:2:4],[1:3:2],[1:3:4],[1:4:2],[1:4:3]\}.
\]
They are all rational over \(\mathbf F_5\). By Bézout, the degree of \(Z\) is \(2\cdot3=6\), so these six distinct rational points exhaust the intersection scheme and each has length one. Consequently \(B\) is exactly the union of their six reduced cone lines, without embedded components or additional geometric components. Any pair of the six distinct cone lines meets only at \(v\).

**3. Singularity and arithmetic.** Every point other than \(v\) lies on exactly one component, which is a smooth line. The vertex is the unique singular point. Its tangent cone is the same homogeneous complete-intersection union of six lines, so its Hilbert–Samuel multiplicity is \(6\), and its normalization separates the six branches. For a complete-intersection curve of bidegree \((2,3)\) in \(\mathbf P^3\), the adjunction formula gives
\[
p_a(B)=1+\frac{2\cdot3\,(2+3-4)}2=4.
\]
The normalization is a disjoint union of six genus-zero curves. The exact normalization sequence and Euler characteristics give
\[
\delta_v=p_a(B)-\sum_{j=1}^6 g_j+6-1=4+6-1=9.
\]
For \(\mathbf F_q\), each line has \(q+1\) points and the common vertex is counted six times, so the total is \(6(q+1)-5=6q+1\).

**4. Exceptional permutation action.** The subgroup permuting the five original coordinates is \(S_5\); it preserves all three power sums and the unique vertex. For every \([a:b:c]\in Z\), the associated direction in the original coordinates is \([a:b:c:0:-a-b-c]\); its five entries are the five distinct elements of \(\mathbf F_5\). Thus the lines are the projective directions obtained from the five-tuple \((0,1,2,3,4)\) by permutations. Two permutations yield the same direction in the quotient by the vertex precisely when their vectors differ by a nonzero scalar and a diagonal translation, i.e. by the affine group \(\operatorname{AGL}_1(\mathbf F_5)\) of order \(20\). The orbit therefore has \(120/20=6\) points, as already constructed. The kernel of the permutation action is a normal subgroup of \(S_5\) lying inside an order-\(20\) stabilizer, hence trivial: neither nontrivial normal subgroup \(A_5\) nor \(S_5\) can be in this stabilizer. The six directions are all six \(\mathbf F_5\)-rational points of the smooth conic \(Q\). Its projective automorphism group is \(\operatorname{PGL}_2(\mathbf F_5)\) of order \(120\); the induced faithful group homomorphism is therefore an isomorphism. Since \(\operatorname{PGL}_2(\mathbf F_5)\) is sharply three-transitive on \(\mathbf P^1(\mathbf F_5)\), the same holds for the components.

## Verification
The supplied standalone `verify.py` uses only the Python standard library. It enumerates the six projective directions over \(\mathbf F_5\), verifies local transversality, tests the coordinate-change polynomial identities at every \(625\) affine four-tuple over \(\mathbf F_5\), checks the \(120\) distinct permutation actions and all \(120\) ordered images of a fixed triple, computes the complete rational-point counts over \(\mathbf F_5\) and \(\mathbf F_{25}\), and checks the complete-intersection Hilbert polynomial. The completed run printed `VERIFY_OK`. Those finite checks supplement the proof above and do not, on their own, establish the all-extension formula or geometric reducedness.

## Relationship to prior work
Korchmáros, Lia and Timpanella [1] study precisely these symmetric power-sum complete intersections, including the genus-four specialization, but impose \(p\ge7\) and \(m\le p-1\) in positive characteristic; therefore their smoothness and irreducibility results do not apply when five coordinates are reduced in characteristic five. Braden and Disney-Hogg [2] provide the classical power-sum Bring model and investigate its characteristic-zero geometry and automorphisms, explicitly setting aside extensions to positive characteristic. The six-line special fiber, its singularity invariant and its exceptional component action are not consequences of those stated theorems. This comparison does not establish uniqueness against all earlier classical or unindexed work.

## Limitations
This is the naive scheme-theoretic special fiber of a specific integral projective model. The theorem neither computes stable reduction of Bring's smooth generic fiber nor claims that arbitrary integral models have the same reduction. The count enumerates rational points of the **singular special fiber**, not points of a smooth reduction or a desingularization. No independent mathematical audit has been performed.

## References
[1] G. Korchmáros, S. Lia and M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886, first version 20 December 2021, https://arxiv.org/abs/2112.10886.

[2] H. W. Braden and L. Disney-Hogg, *Bring's curve: Old and New*, arXiv:2208.13692, first version 29 August 2022, https://arxiv.org/abs/2208.13692; *European Journal of Mathematics* 10 (2024), article 3, https://doi.org/10.1007/s40879-023-00706-0.
