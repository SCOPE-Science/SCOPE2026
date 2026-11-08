# Canonically coincident two-sided ideal lattices of modular dihedral and quaternion group algebras

## Finding
Let \(k\) be **any field of characteristic two**, and let \(m=2^h\) with \(h\ge2\). Consider the dihedral group and generalized quaternion group of common order \(2m\), presented as
\[
 D_{2m}=\langle r,t\mid r^m=1,\ t^2=1,\ trt^{-1}=r^{-1}\rangle,
 \qquad Q_{2m}=\langle r,v\mid r^m=1,\ v^2=r^{m/2},\ vrv^{-1}=r^{-1}\rangle.
\]
Identify their group algebras as *vector spaces* through the coefficient-preserving linear map
\[
 \Phi:\ k[D_{2m}]\longrightarrow k[Q_{2m}],\qquad
 \sum_{i=0}^{m-1}(a_i r^i+b_i r^it)\longmapsto
 \sum_{i=0}^{m-1}(a_i r^i+b_i r^iv).
\]
**Theorem.** For every \(k\)-subspace \(I\subseteq k[D_{2m}]\), the subspace \(I\) is a two-sided ideal if and only if \(\Phi(I)\) is a two-sided ideal of \(k[Q_{2m}]\). Consequently \(\Phi\) induces an inclusion-preserving, intersection- and sum-preserving bijection of complete two-sided ideal lattices, and is simultaneously a Hamming isometry of corresponding two-sided group codes. Every corresponding ideal pair has identical vector-space dimension, full Hamming weight enumerator, minimum distance and support hierarchy (when finite-field code terminology applies). The assertion is **not** that \(\Phi\) is an algebra homomorphism or that the left-ideal lattices coincide.

For the smallest case over \(\mathbb F_2\), both group algebras have exactly fifteen two-sided ideals. Their common dimension enumerator is
\[
 Z(T)=1+T+3T^2+T^3+3T^4+T^5+3T^6+T^7+T^8.
\]
In contrast, their left-ideal dimension enumerators are respectively
\[
 L_D(T)=1+T+3T^2+5T^3+11T^4+5T^5+3T^6+T^7+T^8,
\]
\[
 L_Q(T)=1+T+3T^2+T^3+3T^4+T^5+3T^6+T^7+T^8.
\]
These finite counts illustrate, but are not needed for, the general lattice theorem.

## Assumptions and scope
The field \(k\) may be finite or infinite, but must have characteristic two. The common rotation subgroup has order \(m=2^h\ge4\), so the dihedral and generalized quaternion presentations both define groups of order \(2m\). We classify two-sided ideals *as coefficient subspaces under the indicated linear identification*. No corresponding statement is asserted for left ideals, other characteristics, or non-power-of-two orders.

## Proof
Put \(R=k[r]/(r^m-1)\), let \(\bar a\) denote the involution \(r\mapsto r^{-1}\) on \(R\), and set \(z=r^{m/2}\), so \(z^2=1\). Both group algebras have the common underlying space \(R\oplus Rw\). Define \(A_e\) for \(e\in\{0,1\}\) by \(wa=\bar a w\), \(w^2=z^e\), where \(A_0=k[D_{2m}]\) and \(A_1=k[Q_{2m}]\). With elements written as \((a,b)=a+bw\), left and right rotation operators are independent of \(e\):
\[
 L_r(a,b)=(ra,rb),\qquad R_r(a,b)=(ar,br^{-1}).
\]
The reflection-type generators act as
\[
 L_w^{(e)}(a,b)=(z^e\bar b,\bar a),\qquad
 R_w^{(e)}(a,b)=(z^e b,a).
\]
Fix \(e\in\{0,1\}\) and a two-sided ideal \(I\) of \(A_e\). Because \(k\) has characteristic two, applying the sum of left and right rotation operators to any \((a,b)\in I\) gives
\[
 (L_r+R_r)(a,b)=(0,(r+r^{-1})b)\in I.
\]
The identity \(r+r^{-1}=r^{-1}(r+1)^2\) holds in \(R\). As \(m=2^h\), the Frobenius identity gives \(1+z=(r+1)^{m/2}\). Since \(m/2\ge2\), one has the *exact divisibility identity*
\[
 (1+z)=(r+r^{-1})\,r(r+1)^{m/2-2}.
\]
Multiplication by the second factor, an element of \(R\), preserves \(I\), so \((0,(1+z)b)\in I\). Multiplying this element on the left and right by \(w\) in \(A_e\) yields respectively
\[
 ((1+z)\bar b,0)\in I,\qquad ((1+z)b,0)\in I,
\]
because \(z^e(1+z)=1+z\) and \(\overline{1+z}=1+z\).

Now the differences between the reflection-type actions in \(A_0\) and \(A_1\) on any \((a,b)\in I\) are exactly
\[
 (L_w^{(1)}+L_w^{(0)})(a,b)=((1+z)\bar b,0),\qquad
 (R_w^{(1)}+R_w^{(0)})(a,b)=((1+z)b,0).
\]
Both lie in \(I\). Thus stability under both left and right generators \(r,w\) in \(A_e\) implies stability under both left and right generators in \(A_{1-e}\), hence under the entire algebra \(A_{1-e}\). This implication is symmetric in \(e\), proving equality of two-sided ideal collections under \(\Phi\).

Since \(\Phi\) is the identity on coefficient vectors relative to the displayed group bases, it preserves Hamming supports, all codeword weights and every linear subspace. Its ideal-lattice correspondence therefore preserves sums, intersections, dimensions and the asserted code invariants. No enumeration or computational assumption is involved in this argument.

## Verification
The self-contained `checker.py` directly constructs the two group multiplication tables and independently tests left and right closure of all \(29{,}212\) binary subspaces of the seven-dimensional augmentation ideal when \(m=4\). It finds exactly the same fourteen proper two-sided ideal subspaces for \(\mathbb F_2[D_8]\) and \(\mathbb F_2[Q_8]\), plus each whole algebra. The exhaustive search covers all proper ideals because the group algebra of a finite \(2\)-group over \(\mathbb F_2\) is local, with its seven-dimensional augmentation ideal as its unique maximal ideal. It also reproduces both left-ideal dimension enumerators displayed above. For group orders sixteen and thirty-two it directly compares a deterministic set of two-sided principal ideal spans under both group products. These finite tests are corroboration, **not a proof of the assertion for every field and group size**. The all-field theorem follows from the explicit divisibility and generator-action identities above. Execute `python3 checker.py` with a standard Python 3 interpreter; `checker_output.txt` contains the expected successful output.

## Relationship to prior work
Modular group algebras of dihedral and dicyclic groups were studied by Jeyakumar (1970), and the dimension of group-ring ideals and group codes by Elia–Gorla (arXiv:1403.7920, first public preprint 2014-03-31). Marks (2002) studied reversible and symmetric rings and provides relevant established properties of the binary quaternion group ring. Cao–Cao–Fu–Gao (arXiv:1902.07533, 2019) give a broad classification of binary left dihedral codes, so the dihedral left-code counts are **not claimed to be independently new**. Creedon–Hughes–Szabo (2021) compare modular dihedral and generalized quaternion group rings and prove several common ring-theoretic properties; they also establish nonisomorphism in the modular setting. The narrow claim assessed here is an explicit coefficient-preserving identity of **all two-sided ideal subspace lattices** for every characteristic-two field and every power-of-two order, and the resulting exact equivalence of two-sided group codes. The full text of the 2021 comparison was not accessible for a definitive all-sections priority check, and earlier structural work may imply the statement without using this wording.

## Limitations
The theorem does not identify the two multiplication laws, left or right ideal lattices, module categories, or Jacobson radical filtrations as algebras. It makes no claim in odd characteristic. The finite cardinalities require \(k=\mathbb F_2\) and \(m=4\), while the ideal-lattice equivalence itself requires only characteristic two and \(m=2^h\ge4\). The priority assessment is qualified because a directly relevant 2021 comparison and a 1970 predecessor were not available in complete text for inspection. No independent mathematical audit or exhaustive historical priority certification is claimed.

## References
- A. V. Jeyakumar, *Group Algebras of Dihedral and Dicyclic Groups Over Modular Fields*, Journal of the London Mathematical Society (1970), DOI `10.1112/jlms/s2-2.2.297`.
- M. Elia and E. Gorla, *Computing the dimension of ideals in group algebras, with an application to coding theory*, arXiv:1403.7920v1 (2014), https://arxiv.org/abs/1403.7920.
- G. Marks, *Reversible and symmetric rings*, J. Pure Appl. Algebra 174 (2002), 311–318, DOI `10.1016/S0022-4049(02)00070-1`.
- Y. Cao, Y. Cao, F.-W. Fu and J. Gao, *Self-dual binary codes constructed by left ideals of the dihedral group algebra*, arXiv:1902.07533v1 (2019), https://arxiv.org/abs/1902.07533.
- L. Creedon, K. Hughes and S. Szabo, *A comparison of group algebras of dihedral and quaternion groups*, Applicable Algebra in Engineering, Communication and Computing 32 (2021), 245–264, DOI `10.1007/s00200-020-00485-1`.
