# Two-eigenspace subalgebra permutability and a three-phase finite-field limit

## Finding

Let \(q\) be any prime power, let \(a,b\geq2\) be integers, and let \(L_{a,b}(q)\) be the Lie algebra over \(\mathbb F_q\) with vector-space decomposition \(\mathbb F_q h\oplus E\oplus F\), \(\dim E=a\), \(\dim F=b\), and sole nonzero brackets \([h,e]=e\) for \(e\in E\). Thus \(F\) is central and \(E\oplus F\) is an abelian ideal. Two Lie subalgebras \(A,B\) *permute* when \([A,B]\subseteq A+B\), or equivalently when their vector-space sum is a Lie subalgebra.

**Exact census theorem.** For every \(a,b\ge2\) and \(q\), the number \(T_{a,b}(q)\) of Lie subalgebras and the number \(P_{a,b}(q)\) of ordered permuting pairs are given by the finite Gaussian-binomial formulas in the next section. Consequently \(\operatorname{sd}(L_{a,b}(q))=P_{a,b}(q)/T_{a,b}(q)^2\), including in characteristic two.

**Sharp limit theorem.** With \(a,b\) fixed, as \(q\) grows through prime powers,
\[
\boxed{\lim_{q\to\infty}\operatorname{sd}(L_{a,b}(q))=\begin{cases}
\frac25,&a=b=2,\\
\frac7{16},&\{a,b\}=\{2,3\},\\
1,&\text{all other }a,b\ge2.
\end{cases}}
\]
The two exceptional values are distinct from the already known rank-one central-stabilization limits. For the first case \(a=b=2\), the complete finite-field formulas simplify to
\[
\begin{aligned}
T_{2,2}(q)&=5q^4+7q^3+9q^2+5q+6,\\
T_{2,2}(q)^2-P_{2,2}(q)&=q^2(q-1)(q+1)(15q^4+24q^3+18q^2+6q+1).
\end{aligned}
\]
The full theorem is an infinite two-parameter census, not an extrapolation from these polynomials.

## Assumptions and scope

All subspaces and subalgebras are over \(\mathbb F_q\), and all ordered pairs include repetitions, the zero subalgebra and the whole algebra. The theorem requires \(a,b\ge2\). Lower-rank comparisons are prior-work checks, not newly claimed cases.

For integers \(d\ge0\), let \(\mathrm G_q(d,j)\) be the Gaussian binomial coefficient, equal to zero unless \(0\le j\le d\), and let
\[
H_n(q)=\sum_{j=0}^{n}\mathrm G_q(n,j),\qquad n=a+b.
\]
Set
\[
B_{a,b}(q)=\sum_{p=0}^a\sum_{z=0}^b
\mathrm G_q(a,p)\mathrm G_q(b,z)q^{n-p-z}.
\]
For \(w,d\ge0\), set
\[
R_q(w,d)=\sum_{j=0}^w\mathrm G_q(w,j)q^{d(w-j)}.
\]
Define the mixed-pair subtotal
\[
M_{a,b}(q)=\sum_{p=0}^a\sum_{z=0}^b
\mathrm G_q(a,p)\mathrm G_q(b,z)q^{n-p-z}
\sum_{i=0}^{a-p}\sum_{j=0}^{b-z}
\mathrm G_q(a-p,i)\mathrm G_q(b-z,j)R_q(p+z,i+j).
\]
For the exterior--exterior subtotal use the Gaussian subspace-intersection count
\[
C_q(d;u,v,t)=\mathrm G_q(d,u)\mathrm G_q(u,t)
\mathrm G_q(d-u,v-t)q^{(u-t)(v-t)}.
\]
For \(0\le p,p'\le a\), \(0\le z,z'\le b\), and intersection dimensions
\[
\max(0,p+p'-a)\le t\le\min(p,p'),\qquad
\max(0,z+z'-b)\le s\le\min(z,z'),
\]
put \(k_E=p+p'-t\), \(k_F=z+z'-s\), and \(k=k_E+k_F\). Then
\[
\begin{aligned}
Q_{a,b}(q)= {}&\sum_{p,p'=0}^{a}\sum_{z,z'=0}^{b}\sum_{t,s\ \mathrm{admissible}}
 C_q(a;p,p',t)C_q(b;z,z',s)\\
&\quad\cdot q^{n-(p+z)-(p'+z')+k}
\bigl(q^{a-k_E}+q^{b-k_F}-1\bigr).
\end{aligned}
\]
Here the innermost summation runs over the two intersection ranges displayed immediately above it; the exponent of \(q\) is nonnegative. The exact counts are
\[
\boxed{T_{a,b}(q)=H_n(q)+B_{a,b}(q),\qquad
P_{a,b}(q)=H_n(q)^2+2M_{a,b}(q)+Q_{a,b}(q).}
\]
These are explicit finite sums of nonnegative integer counts, not implicit enumeration over subalgebras.

## Proof

**1. Subalgebra classification.** Put \(V=E\oplus F\), and let \(D:V\to V\) be identity on \(E\) and zero on \(F\). Every vector subspace of the abelian ideal \(V\) is a Lie subalgebra; their number is \(H_n(q)\). Any subalgebra \(A\not\subseteq V\) has the unique description
\[
A=\mathbb F_q(h+v)\oplus W,\qquad v\in V/W,
\]
where \(W=A\cap V\) is \(D\)-invariant: closure is equivalent to \(DW\subseteq W\). Since \(D\) has distinct eigenvalues zero and one, \(D\)-invariant subspaces are precisely \(W=P\oplus Z\) with \(P\le E\), \(Z\le F\). For dimensions \(\dim P=p\), \(\dim Z=z\), there are \(\mathrm G_q(a,p)\mathrm G_q(b,z)q^{n-p-z}\) exterior subalgebras. This proves \(T=H_n+B\).

**2. Inside--inside pairs.** Every pair of subspaces of \(V\) permutes because \(V\) is abelian. This contributes \(H_n(q)^2\).

**3. Mixed pairs.** Fix \(U\le V\) and \(A=\mathbb F_q(h+v)\oplus W\) with \(W\) invariant. Then \(U+A\) is a Lie subalgebra exactly when \(D(U+W)\subseteq U+W\); the coset \(v+W\) is irrelevant. For fixed \(W=P\oplus Z\) as above, every invariant super-subspace of \(W\) has form \(P'\oplus Z'\), with dimensions \(p+i\) and \(z+j\), and there are \(\mathrm G_q(a-p,i)\mathrm G_q(b-z,j)\) of them. If an invariant super-subspace \(Y\supseteq W\) has quotient dimension \(d=i+j\), the number of subspaces \(U\le Y\) satisfying \(U+W=Y\) is \(R_q(w,d)\), where \(w=\dim W\): choose \(K=U\cap W\) with dimension \(h\), then take the graph of an arbitrary linear map \(Y/W\to W/K\). Summation gives \(M_{a,b}(q)\) mixed pairs in each orientation.

**4. Exterior--exterior pairs.** Let \(A=\mathbb F_q(h+v)\oplus W\) and \(B=\mathbb F_q(h+u)\oplus W'\). Their vector-space sum is
\[
A+B=\mathbb F_q(h+v)\oplus\bigl(W+W'+\mathbb F_q(u-v)\bigr).
\]
It is bracket-closed exactly when the line generated by the image of \(u-v\) in \(V/(W+W')\) is \(D\)-invariant (including the zero image). The quotient splits into eigenspaces of dimensions \(a-k_E\) and \(b-k_F\). A vector in this quotient spans an invariant line or is zero precisely when it lies in one of the two eigenspaces, giving exactly \(q^{a-k_E}+q^{b-k_F}-1\) allowed quotient vectors.

For fixed \(W,W'\) the map from ordered cosets \((v+W,u+W')\) to the image of \(u-v\) in \(V/(W+W')\) is surjective, and every fiber has \(q^{n-w-w'+k}\) elements. Finally, \(C_q(a;p,p',t)C_q(b;z,z',s)\) counts the ordered choices of the two invariant subspaces with those intersection dimensions. Summing gives \(Q_{a,b}(q)\). The exact census follows.

**5. Dominant degrees and the limit.** Gaussian binomials have leading coefficient one and degree \(j(d-j)\). The largest degree of the inside-subalgebra count is \(\lfloor n^2/4\rfloor\). The largest degree of the exterior-subalgebra count is
\[
n+\left\lfloor\frac{(a-1)^2}{4}\right\rfloor+
\left\lfloor\frac{(b-1)^2}{4}\right\rfloor,
\]
because \(\max_{0\le p\le a}p(a-p-1)=\lfloor(a-1)^2/4\rfloor\), and likewise for \(b\). For \(a,b\ge2\) the inside degree is strictly larger except at \((2,2)\), \((2,3)\) and \((3,2)\), where they tie. This follows directly from the displayed degree formula: increasing either multiplicity from those boundary values makes the difference positive and nondecreasing. Whenever the inside count dominates, two independent uniformly sampled subalgebras lie inside the abelian ideal with probability tending to one, and so their permutability probability tends to one.

For \((a,b)=(2,2)\), the dominant inside objects are two-dimensional subspaces, one leading unit in the count, and the dominant exterior objects have eigenspace dimensions \((p,z)\in\{0,1\}^2\), four leading units. For generic pairs of these types, exactly one inside--inside type pair, two oriented mixed pairs (the exterior type \((1,1)\)), and seven exterior--exterior type pairs (those for which the two chosen eigenspace components together span at least one full eigenspace) permute. Other pairs contribute strictly lower powers of \(q\). Hence the leading coefficient of \(P\) is \(1+2+7=10\), while that of \(T\) is five, yielding \(10/25=2/5\).

For \((a,b)=(2,3)\), the dominant inside subspaces have dimensions two or three, one leading unit of each type; the exterior objects have eigenspace dimensions \((p,z)=(0,1)\) or \((1,1)\), likewise one leading unit each. All four inside--inside type pairs permute. Of the mixed type pairs, only a generic dimension-three inside subspace with exterior type \((1,1)\) spans \(V\), contributing two oriented type pairs. Of the exterior--exterior types, only the \((1,1)\)-\((1,1)\) pair generically spans all of \(E\), leaving a quotient inside \(F\), so it permutes, contributing one type pair. All others have lower order. Thus \(P\) has leading coefficient seven and \(T\) coefficient four, giving \(7/16\).

Swapping \(E\) and \(F\) preserves the subalgebra lattice and permutability relation: the operators \(D\) and \(I-D\) induce identical relations because the difference of the two brackets on vectors \(x,y\) lies in \(\langle x,y\rangle\). Therefore the \((3,2)\) case also gives \(7/16\). This completes the limit classification over all prime powers.

## Verification

The standalone Python 3 program `artifacts/verify.py` counts every linear subspace of small ambient vector spaces in reduced row-echelon form, directly tests closure under the Lie bracket, and for every ordered pair of subalgebras directly checks bracket containment in their vector-space sum. These test objects are not generated by the formulas. For each stated case it independently evaluates the Gaussian finite sums and asserts exact agreement. Its five cases include \((a,b,q,\lambda)=(2,2,2,0)\) and \((2,2,3,0)\), giving \((T,P)=(188,29140)\) and \((696,337248)\), as well as three lower-dimensional boundary checks. Here \(\lambda\) is the second diagonal eigenvalue used by the checker; the formulas depend only on its being distinct from the first eigenvalue one.

The program produces `TWO_EIGEN_LIE_VERIFY_OK 5`, as preserved in `artifacts/verification_output.txt`. Exact enumeration at small dimensions does not prove the infinite identities or their asymptotics; those follow from the preceding argument.

## Relationship to prior work

Muhie, Otera and Russo (arXiv:2609.19086v1, first posted September 16, 2026) introduced subalgebra commutativity degree and proved results for Heisenberg, scalar-action and other selected Lie algebras, but not the present higher-rank central stabilizations. The complete three-dimensional case and its projective-eigenline classification were established in the mathematical record *Plane counts control subalgebra commutativity in dimension three* (September 18, 2026). Therefore the rank-one and total-dimension-three cases are not claimed here.

The record *Parity phase transition for subalgebra permutability in centrally stabilized affine Lie algebras* (November 8, 2026) already gives exact sums and a \(0\)-versus-\(1/4\) limit for the central stabilizations of the **two-dimensional** affine algebra, meaning the noncentral eigenspace has dimension one. Its full proof also notes an earlier four-dimensional diagonal-action calculation. These cases are excluded by the assumptions \(a,b\ge2\). Scalar-shift invariance of Lie-subalgebra permutability is also already explicit in *Exact subalgebra permutability and a rank threshold for Jordan-chain Lie algebras* (October 25, 2026); the proof here does not claim that observation as new. The latter result treats a single Jordan block, not two scalar eigenspaces of dimensions at least two.

The present two-parameter theorem supplies the higher-rank fixed-field pair census and isolates the new limits \(2/5\) and \(7/16\) before the full-probability range. Earlier work on elementwise commuting probability is not a theorem about permuting subalgebras. Relevant primary mathematical texts and published records were compared by their actual hypotheses and implications, but unindexed literature remains a priority risk.

## Limitations

The theorem treats scalar actions with two distinct eigenspaces, both of dimension at least two; it does not cover arbitrary nonsplit or nonsemisimple adjoint actions. The limit holds with \(a,b\) fixed as \(q\to\infty\), not with simultaneous growth in the dimensions. The finite checker works over prime fields in the listed cases; validity over all prime powers rests on the field-independent proof. No independent mathematical audit is asserted. The exact new-source historical priority cannot be absolutely certified from indexed searches alone.

## References

1. S. K. Muhie, D. E. Otera and F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, first public September 16, 2026. https://arxiv.org/abs/2609.19086
2. *Parity phase transition for subalgebra permutability in centrally stabilized affine Lie algebras*, published mathematical record, November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-phase-transition-for-subalgebra-permutability-in-centrall--409c328075cb
3. *Exact subalgebra permutability and a rank threshold for Jordan-chain Lie algebras*, published mathematical record, October 25, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-subalgebra-permutability-and-a-rank-threshold-for-jordan-c--2ca07ad52f23
4. *Plane counts control subalgebra commutativity in dimension three*, published mathematical record, September 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c
