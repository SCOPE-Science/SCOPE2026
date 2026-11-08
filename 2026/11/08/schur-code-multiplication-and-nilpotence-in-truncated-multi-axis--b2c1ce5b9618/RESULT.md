# Schur-code multiplication and nilpotence in truncated multi-axis ideal monoids

## Finding

For any field \(k\), any number of branches \(r\ge2\), and any integer cutoffs \(n_1,\ldots,n_r\ge2\), let
\[
R=k[x_1,\ldots,x_r]/(x_ix_j\ (i\ne j),\ x_i^{n_i}\ (1\le i\le r)).
\]
Every proper ideal can be represented uniquely by branch thresholds and a full-coordinate-support linear code, as recalled below. The **new result** is a closed, associative formula for the *entire multiplicative monoid of ideals*: the product is addition of thresholds, capped at the branch lengths, accompanied by the Schur (coordinatewise) product of the corresponding codes. Thus not just the ideals but the multiplication of any two of them is explicit, over every field. A further consequence is that zero products and the exact nilpotency index of every nonzero proper ideal are determined exclusively by its thresholds, even though the products themselves retain nontrivial coding data.

Write \(\mathfrak m=\bigoplus_{i=1}^r(x_i)\), and for a proper ideal \(I\) let \(a_i(I)\) be the least positive degree present in the coordinate projection of \(I\) onto \((x_i)\), with \(a_i(I)=n_i\) if this projection is zero. Set \(T(I)=\{i:a_i(I)<n_i\}\), and form the **leading code** \(L_I\le k^{T(I)}\) by taking the coefficients of \(x_i^{a_i(I)}\) in the projections of elements of \(I\). Each coordinate projection of \(L_I\) is nonzero. The ideal \(I\) is the full inverse image of \(L_I\) under the map
\[
\bigoplus_{i\in T(I)}(x_i^{a_i(I)})\longrightarrow\bigoplus_{i\in T(I)}(x_i^{a_i(I)})/(x_i^{a_i(I)+1})\cong k^{T(I)}.
\]
Indeed, it contains every higher tail \((x_i^{a_i(I)+1})\). Conversely, any thresholds \(a_i\in[1,n_i]\) and a code \(L\le k^{\{i:a_i<n_i\}}\) with nonzero projection on each coordinate specify exactly one proper ideal \(I(a,L)\). This convenient representation is a reformulation of an existing ideal classification, not itself a novelty claim.

For two proper ideals \(I=I(a,L)\) and \(J=I(b,M)\), define
\[
c_i=\min\{n_i,a_i+b_i\},\qquad U=\{i:c_i<n_i\},
\]
where the degree cutoffs \(a_i=n_i\), \(b_i=n_i\) denote zero projections. Restrict each code to the surviving coordinates \(U\), and let the **Schur product code** be
\[
(L|_U)\star(M|_U)=\operatorname{span}_k\{(u_iv_i)_{i\in U}:u\in L,\ v\in M\}\le k^U.
\]
Then the full ideal-product law is
\[
\boxed{I(a,L)\,I(b,M)=I\big(c,(L|_U)\star(M|_U)\big).}
\]
When \(U\) is empty the right side denotes the zero ideal. Each resulting coordinate is nonzero, so this is already a valid full-support code, even if its Schur product introduces coordinate axes. Adjoin the unit ideal \(R\) as the multiplicative identity.

In particular,
\[
IJ=0\ \Longleftrightarrow\ a_i(I)+a_i(J)\ge n_i\quad\text{for all }i,
\]
and for any nonzero proper ideal \(I\), its exact nilpotency index is
\[
\boxed{\nu(I)=\min\{t\ge1:I^t=0\}=\max_{i:a_i(I)<n_i}\left\lceil\frac{n_i}{a_i(I)}\right\rceil.}
\]
The full higher products are determined by coordinatewise Schur powers of the restricted leading code, with the threshold vector capped at \(\mathbf n\). No finite-field hypothesis is needed.

## Assumptions and scope

The algebra is commutative, finite-dimensional, split, and local, with pairwise-annihilating radical branches. All statements use labeled branches and arbitrary fields. Ideals are ordinary two-sided ideals, automatically so because the ring is commutative. When a branch vanishes, its corresponding coordinate is deleted before the Schur product. The zero ideal has all thresholds \(a_i=n_i\); its nilpotency index is conventionally one, and the displayed maximum is used only for nonzero proper ideals. The unit ideal is handled separately. The leading code is not required to have minimum distance two: coordinate axes are allowed. This is necessary because multiplying two mixed ideals may introduce pure branch generators.

## Proof

**Branch-leading representation.** Every proper ideal \(I\) is contained in \(\mathfrak m\). Its projection \(P_i\) onto \((x_i)\) is invariant under multiplication by \(x_i\), so \(P_i=(x_i^{a_i})\) for a unique \(a_i\in[1,n_i]\). If \(a_i<n_i\), some \(v\in I\) has nonzero coefficient of \(x_i^{a_i}\); multiplying \(v\) by \(x_i\) gives \(x_i^{a_i+1}h(x_i)\), where \(h(x_i)\) has nonzero constant coefficient and is a unit in \(k[x_i]/(x_i^{n_i})\). Multiplying by its inverse inside \(R\) gives \(x_i^{a_i+1}\in I\), and hence all of the tail \((x_i^{a_i+1})\subseteq I\). This also holds when \(a_i=n_i-1\), with zero higher tail. Therefore \(I\) contains the direct sum of all those higher tails. The quotient of \(I\) by them maps injectively to the direct sum of one-dimensional leading quotients; its image \(L_I\) has full coordinate support by the definition of \(a_i\). Conversely, lifting any full-support subspace and adjoining the higher tails gives an ideal, because multiplication by every generator sends every lift into the higher tails. This proves existence and uniqueness of the representation.

**The product.** For every \(u\in I\) and \(v\in J\), the \(i\)-th branch projection of \(uv\) is the product of the two \(i\)-th projections: all mixed-branch products vanish. Its least possible degree is \(a_i+b_i\); thus the projection is zero if \(a_i+b_i\ge n_i\). If \(a_i+b_i<n_i\), both leading coordinate functionals on \(I,J\) are nonzero; choose \(u,v\) with nonzero \(i\)-th leading coefficients. Their product has nonzero coefficient in degree \(a_i+b_i\). It follows that \(a_i(IJ)=c_i\) exactly, and by the preceding tail argument \(IJ\) contains every \((x_i^{c_i+1})\) for surviving \(i\).

Modulo these higher tails, the product \(uv\) has the \(i\)-th leading coefficient equal to the product of the leading coefficients of \(u\) and \(v\). Hence the leading code of \(IJ\) is the linear span of coordinatewise products \(L_I|_U\star L_J|_U\). Every generating coordinatewise product occurs by taking lifts in \(I,J\), and every product of lifts contributes to this span, so there are no missing or spurious vectors. The unique inverse-image representation gives the boxed law. Associativity also follows from ideal multiplication, or from associativity of coordinatewise multiplication and capping of positive degree sums.

**Zero criterion and nilpotency.** The leading code of the product has nonzero projection onto every surviving coordinate because both input projections are nonzero and the field has no zero divisors. Therefore the product is zero precisely when no coordinate survives. Iterating yields \(a_i(I^t)=\min(n_i,t a_i(I))\) for every \(t\ge1\). The least \(t\) for which all branches vanish is the displayed maximum of ceilings. This also proves that the nilpotency index depends on thresholds only, not on the leading code.

## Verification

The included dependency-free script `verify.py` enumerates every RREF subspace of the radical and tests generator-invariance directly over \(\mathbb F_2\) and \(\mathbb F_3\). For each pair of resulting ideals it calculates the *true* span of all basis-vector products using the defining ring multiplication, independently constructs the predicted span from leading codes and capped thresholds, and compares them by exact finite-field Gaussian elimination. It also checks the zero-product criterion. Across five tested algebras, the script checks exactly \(256+6241+4489+2500+576=14062\) ordered ideal products; all pass. The five tests span radical dimensions three through six, and include nontrivial higher truncations. The general proof is symbolic and does not rely on exhaustive finite examples.

For illustration, take three branches of cutoff at least four and the code generated by \((1,1,0)\) and \((0,1,1)\) over any field. The Schur square contains their coordinatewise product \((0,1,0)\) and the two squares, hence all three coordinate axes: the square of the associated mixed ideal has **fully separated leading branches**. In contrast, for a repetition code the Schur powers remain repetition codes; the code component is therefore mathematically necessary and cannot be discarded in general.

## Relationship to prior work

A previous ideal-spectrum classification for the same truncated multi-axis rings already gives the full ideal-dimension distribution and an alternate parametrization by axis-avoiding codes. Neither this prior classification nor its numerical count is asserted as a new result here. The assessed extension is the complete **ideal multiplication monoid**, its Schur-code realization, and the sharp nilpotency-index law. Behboodi–Shojaee's 2012 study of cyclic decompositions of local-ring ideals (arXiv:1201.6076) contains the two-branch truncated ring as Example 4.2 but no formula for products of arbitrary nonmonomial ideals. Randriambololona's November 29, 2013 preprint (arXiv:1312.0022) developed the Schur product and powers of linear codes; that operation and its general properties are duly credited. Its code-theoretic statements do not by themselves identify the multiplicative ideal monoid of these rings with truncated and restricted Schur codes.

## Limitations

The theorem does not classify multiplicative ideal monoids of arbitrary local rings, nonzero cross-branch products, automorphism orbits, or ideals of noncommutative algebras. The representation part is a known equivalence; novelty is limited to multiplication and its consequences. More general unlocated module-theoretic product laws might imply this application, so independent historical-priority verification remains unresolved. Exhaustive tests are finite and do not prove the all-field theorem. No independent mathematical audit has been conducted.

## References

- M. Behboodi and S. H. Shojaee, *Commutative Local Rings whose Ideals are Direct Sums of Cyclic Modules*, arXiv:1201.6076 (first submitted 2012-01-29), https://arxiv.org/abs/1201.6076.
- H. Randriambololona, *On products and powers of linear codes under componentwise multiplication*, arXiv:1312.0022 (first submitted 2013-11-29), https://arxiv.org/abs/1312.0022.
