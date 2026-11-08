# Complete finite-field commutator fibers and width in the five-generator exterior algebra

## Finding
Let \(q\) be an odd prime power, let \(V\) be a five-dimensional vector space over \(k=\mathbb F_q\), and let \(E=\bigwedge_k V\) be the unital associative exterior algebra, with ordinary commutator \([X,Y]=XY-YX\). Every commutator lies in \(\bigwedge^2 V\oplus\bigwedge^4 V\). For \(a\in\bigwedge^2V\) and \(b\in\bigwedge^4V\), put
\[
F_q(a,b)=\#\{(X,Y)\in E^2:[X,Y]=2(a+b)\}.
\]
A bivector is **simple** (or decomposable) if it is a wedge \(u\wedge v\) of two vectors. Then the complete fiber distribution is
\[
\boxed{F_q(a,b)=\begin{cases}
q^{50}\big((q^5-1)(q+1)+q^4\big),&a=0,\ b=0,\\
q^{50}(q^4-1)(q+1),&a=0,\ b\ne0,\\
q^{50}(q^2-1),&a\ne0\text{ simple},\ b\text{ arbitrary},\\
0,&a\text{ not simple}.
\end{cases}}
\]
Nonzero targets outside the positive-degree even subspace also have empty fibers. Among targets in \(\bigwedge^2 V\oplus\bigwedge^4V\), the number represented by a single commutator is exactly
\[
q^5\left(1+\frac{(q^5-1)(q^4-1)}{q^2-1}\right).
\]
The derived additive subspace is the full \(\bigwedge^2V\oplus\bigwedge^4V\), and its **commutator width is exactly two**: every element is a sum of at most two ordinary commutators, and some elements require two.

## Assumptions and scope
The field is \(\mathbb F_q\) with \(q\) any odd prime power; no primality assumption is made on \(q\). The vector space has dimension exactly five and \(E\) has dimension \(32\). The commutator is the *ordinary associative* commutator, not the graded supercommutator. Counts are of ordered labeled pairs, not automorphism orbits. The factor \(2\) in the target is invertible and merely normalizes the formulas. The only assumptions needed are exterior multiplication and the elementary ranks of maps induced by wedge product.

## Proof
**1. Reduction to a bilinear map.** In the \(\mathbb Z/2\mathbb Z\) grading, even elements commute with everything, while odd elements anticommute. An arbitrary odd element of \(E\) has a unique expression \(u+s+\tau\), where \(u\in V\), \(s\in\bigwedge^3V\), and \(\tau\in\bigwedge^5V\). Since the last summand annihilates all positive-degree elements, for two odd elements \(u+s+\tau\) and \(v+t+\sigma\),
\[
[X,Y]=2\bigl(u\wedge v+(u\wedge t+s\wedge v)\bigr).
\]
The degree-two output is \(u\wedge v\), and the degree-four output is \(u\wedge t+s\wedge v\). The even parts of the two inputs supply \(q^{32}\) freely chosen coordinates, and their degree-five parts supply a further \(q^2\). Thus every reduced fiber count on \(V^2\times(\bigwedge^3V)^2\) must be multiplied by \(q^{34}\).

**2. Nonzero simple degree-two target.** If \(a=u\wedge v\ne0\), the plane \(P=\langle u,v\rangle\) is uniquely determined by \(a\), and the number of ordered pairs \((u,v)\) realizing this fixed wedge is \(|\operatorname{SL}_2(k)|=q(q^2-1)\). For every independent \(u,v\), the linear map
\[
L_{u,v}:\bigl(\bigwedge^3V\bigr)^2\longrightarrow\bigwedge^4V,
\qquad(s,t)\longmapsto u\wedge t+s\wedge v
\]
is surjective. Indeed, complete \(u,v\) to a basis: every four-element subset of a five-element basis meets the two-element set indexing \(u,v\), and its basis wedge is in the image. The domain has dimension \(20\) and the codomain dimension \(5\), so each degree-four target has \(q^{15}\) preimages. The reduced fiber is \(q(q^2-1)q^{15}=q^{16}(q^2-1)\), yielding the third case after multiplication by \(q^{34}\).

**3. Zero degree-two target.** The equation \(u\wedge v=0\) means the two vectors span a space of dimension at most one. When both vanish, every pair \((s,t)\) gives degree-four output zero, giving \(q^{20}\) solutions if \(b=0\), and none otherwise. For a fixed one-dimensional subspace \(\ell\subset V\), the number of ordered pairs \((u,v)\in\ell^2\) spanning \(\ell\) is \(q^2-1\). For each such pair, the image of \(L_{u,v}\) equals \(\ell\wedge\bigwedge^3V\), of dimension \(\binom43=4\); each target in this image has \(q^{16}\) preimages.

For \(b=0\), all \((q^5-1)/(q-1)\) lines are allowed, so the reduced zero fiber is
\[
q^{20}+\frac{q^5-1}{q-1}(q^2-1)q^{16}
=q^{20}+(q^5-1)(q+1)q^{16}.
\]
For nonzero \(b\in\bigwedge^4V\), the linear map \(V\to\bigwedge^5V\) given by \(w\mapsto w\wedge b\) has a four-dimensional kernel \(H_b\). A nonzero four-form in a five-space is decomposable, and \(b\in\ell\wedge\bigwedge^3V\) exactly when \(\ell\subset H_b\). Exactly \((q^4-1)/(q-1)\) lines lie in \(H_b\); hence the reduced fiber is \((q^4-1)(q+1)q^{16}\). Multiplication by \(q^{34}\) proves the first two cases.

**4. Non-simple target and full mass.** Every degree-two output is \(u\wedge v\), so a nonsimple \(a\) has no witnesses. There are \(\binom52_q\) two-dimensional subspaces of \(V\), and each contributes \(q-1\) nonzero simple bivectors. Thus the number of nonzero simple targets is
\[
D_q=(q-1)\binom52_q=\frac{(q^5-1)(q^4-1)}{q^2-1}.
\]
The four strata have target multiplicities \(1\), \(q^5-1\), \(q^5D_q\), and the remainder. Their weighted sum equals \(q^{64}=|E|^2\), as can also be checked after dividing by \(q^{34}\):
\[
\bigl[q^{20}+(q^5-1)(q+1)q^{16}\bigr]
+(q^5-1)(q^4-1)(q+1)q^{16}
+q^5D_q q^{16}(q^2-1)=q^{30}.
\]
This verifies the normalization and that all pairs have been accounted for.

**5. Sharp commutator width.** Each nonzero four-form is divisible by some nonzero vector, hence has a one-commutator representation with degree-two output zero; similarly any simple degree-two form has one-commutator representations with every degree-four output. By alternating normal form, any bivector in a five-space is a sum of at most two simple bivectors. Assign the entire prescribed four-form to the first nonzero simple summand and zero to the second; this expresses every element of \(\bigwedge^2V\oplus\bigwedge^4V\) as a sum of at most two commutators. The degree-two form \(e_1\wedge e_2+e_3\wedge e_4\) is nonsimple (its square is twice a nonzero degree-four form), so cannot be a single commutator. Thus the width is exactly two.

## Verification
The standalone file `check.py` constructs the literal \(32\)-by-\(32\) exterior multiplication on basis masks and checks its commutator against the degree-two/degree-four reduction on \(155\) reproducibly sampled ordered pairs each over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). It separately forms the twenty wedge-map columns and checks their ranks in \(101\) samples in each of those fields. For \(\mathbb F_3\), it exhaustively enumerates all \(3^{10}=59049\) pairs of degree-one inputs for seven selected degree-two/degree-four targets and counts compatible degree-three input pairs via finite-field linear-system ranks. The results match all three nonempty cases and the nonsimple zero case. Polynomial mass identities are evaluated at four field-size test values. Run `python3 check.py` and compare with `check_output.txt`. The infinite family is proved above, not inferred from these finite tests.

## Relationship to prior work
The underlying supercommutativity, relation between commuting odd elements and zero wedge products, and the role of decomposable bivectors are classical. Domokos and Zubor, *Commutative subalgebras of the Grassmann algebra* (first made public March 12, 2014), study maximal commutative subalgebra dimensions and explicitly discuss the Plücker description of decomposable degree-two elements (their Example 8.6). Their result establishes crucial context but does not state the present target-by-target finite-field commutator-fiber counts or the sharp width-two assertion. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra* (first made public March 12, 2007), develops the same algebra's automorphism structure, not this bilinear count. The new calculation is a finite-field counting refinement; it does not claim the exterior-product identities or Plücker equations as new. A general result about fibers of exterior multiplication could subsume it; no exhaustive priority guarantee is made.

## Limitations
Only the ordinary commutator map in the five-generator exterior algebra over odd finite fields is classified. Characteristic two has identically zero ordinary commutators and is excluded from the formulas. Higher generator numbers introduce additional wedge degrees and are not covered. The proof counts labeled pairs, not automorphism orbits, and does not determine distributions of individual centralizer dimensions beyond the commuting-fiber total. The source comparison is limited to identified accessible literature; independent review and comprehensive priority certification have not occurred.

## References
1. V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352v1, March 12, 2007, https://arxiv.org/abs/math/0703352.
2. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916v1, March 12, 2014, https://arxiv.org/abs/1403.2916.
