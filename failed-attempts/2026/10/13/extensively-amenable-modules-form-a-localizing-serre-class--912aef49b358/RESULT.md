# Extensively amenable modules form a localizing Serre class
## Finding
Let \(\mathscr A\) be a cocommutative Hopf algebra over a field \(k\). In the sense introduced by Bartholdi, the class of extensively amenable left \(\mathscr A\)-modules is closed under arbitrary direct sums and under directed unions of \(\mathscr A\)-submodules. Combining these two permanence properties with Bartholdi's theorem for short exact sequences shows that the extensively amenable modules form a localizing Serre subcategory of \(\mathscr A\text{-Mod}\).

Consequently every left \(\mathscr A\)-module \(M\) has a unique largest extensively amenable submodule
\[
T_{\mathrm{EA}}(M)=\sum_{N\le M,\;N\;\mathrm{extensively\ amenable}}N.
\]
This assignment is functorial: every \(\mathscr A\)-linear map \(f:M\to M'\) satisfies \(f(T_{\mathrm{EA}}(M))\subseteq T_{\mathrm{EA}}(M')\). Moreover \(M/T_{\mathrm{EA}}(M)\) contains no nonzero extensively amenable submodule. Thus extensive amenability determines a hereditary torsion radical on the module category.

## Assumptions and scope
The base ring is a field \(k\), and \(\mathscr A\) is a cocommutative Hopf algebra over \(k\). Extensive amenability is Bartholdi's symmetric-algebra definition: \(M\) is extensively amenable when \(\operatorname{Sym}(M)\) is an amenable module for the smash product \(\operatorname{Sym}(M)\#\mathscr A\). The claim concerns ordinary left modules and does not assert an analogue for noncocommutative Hopf algebras or for module categories over a non-field base.

The term “localizing Serre subcategory” is used in the standard module-category sense: a Serre class closed under arbitrary coproducts. The stronger directed-union statement is proved directly and is used to establish arbitrary direct sums from finite ones.

## Proof
First prove closure under directed unions. Let \(M=\bigcup_{i\in I}M_i\), where the \(M_i\) form a directed family of extensively amenable \(\mathscr A\)-submodules. To test extensive amenability of \(M\), fix a finite-dimensional subspace \(S\subseteq\operatorname{Sym}(M)\#\mathscr A\) and a positive tolerance \(\varepsilon\). Every vector of \(S\) is a finite linear combination of smash-product tensors whose polynomial coefficients involve only finitely many vectors of \(M\). Directedness therefore gives one index \(i\) such that all these vectors lie in \(M_i\). Because symmetric algebras preserve injections of vector spaces over a field, we may identify \(\operatorname{Sym}(M_i)\) with a subalgebra of \(\operatorname{Sym}(M)\), and then
\[
S\subseteq\operatorname{Sym}(M_i)\#\mathscr A.
\]
Extensive amenability of \(M_i\) supplies a nonzero finite-dimensional Følner subspace \(F\subseteq\operatorname{Sym}(M_i)\) for this same \(S\) and tolerance. The action of \(S\) on \(F\) computed inside \(\operatorname{Sym}(M_i)\) is identical to the action after inclusion in \(\operatorname{Sym}(M)\). Hence the same Følner inequality holds in \(M\). Since \(S\) and \(\varepsilon\) were arbitrary, \(M\) is extensively amenable.

Now let \(M=\bigoplus_{j\in J}M_j\). If every \(M_j\) is extensively amenable, then every finite partial sum is extensively amenable by repeated application of Bartholdi's short-exact-sequence theorem to split exact sequences
\[
0\longrightarrow U\longrightarrow U\oplus V\longrightarrow V\longrightarrow0.
\]
The whole direct sum is the directed union of its finite partial sums, so it is extensively amenable by the preceding paragraph. Conversely, if the whole direct sum is extensively amenable, then for each \(j\) the split exact sequence with kernel \(M_j\) and quotient \(\bigoplus_{i\ne j}M_i\) and Bartholdi's theorem imply that \(M_j\) is extensively amenable. Thus an arbitrary direct sum is extensively amenable exactly when all its summands are.

Bartholdi proves that for every exact sequence \(0\to L\to N\to Q\to0\), the middle module is extensively amenable if and only if both ends are. Hence the class is closed under submodules, quotients, and extensions. Together with arbitrary direct sums this is precisely a localizing Serre class in \(\mathscr A\text{-Mod}\).

Finally, define \(T_{\mathrm{EA}}(M)\) as the sum of all extensively amenable submodules of \(M\). The external direct sum of those submodules is extensively amenable by the direct-sum result, and its canonical map onto their sum has extensively amenable image because the class is quotient-closed. Thus \(T_{\mathrm{EA}}(M)\) is itself extensively amenable and is visibly the unique largest such submodule. For an \(\mathscr A\)-linear map \(f:M\to M'\), the image \(f(T_{\mathrm{EA}}(M))\) is a quotient of an extensively amenable module, hence lies in \(T_{\mathrm{EA}}(M')\), proving functoriality. If a nonzero extensively amenable submodule \(L/T_{\mathrm{EA}}(M)\) existed in the quotient, its preimage \(L\) would be an extension of two extensively amenable modules and therefore extensively amenable, contradicting maximality unless \(L=T_{\mathrm{EA}}(M)\).

## Verification
The proof uses only two nontrivial inputs from the source: the definition of extensive amenability through the symmetric-algebra smash product and the two-of-three theorem for short exact sequences. The directed-union step was checked at the level of the defining Følner test: a finite-dimensional test subspace uses finitely many polynomial variables, so it is already supported in one stage of a directed union. No finite experiment or compactness surrogate is used.

The direct-sum step was checked in both directions. The construction of \(T_{\mathrm{EA}}(M)\) avoids assuming that an arbitrary sum of submodules is a directed union of a prescribed chain: it passes through the external direct sum and quotient closure. The torsion-free quotient assertion is then a direct extension argument.

## Relationship to prior work
Bartholdi, “On extensive amenability of algebras,” arXiv:2610.00364v1, introduces extensive amenability for modules over cocommutative Hopf algebras and proves preservation and reflection by short exact sequences. The paper also proves several other permanence statements, but the inspected text does not state closure under arbitrary module direct sums, the localizing-Serre conclusion, or the maximal extensively amenable submodule and torsion radical constructed here.

Juschenko, Matte Bon, Monod, and de la Salle, “Extensive amenability and an application to interval exchanges,” Ergodic Theory and Dynamical Systems 38 (2018), 195–219, DOI 10.1017/etds.2016.32, develops the older notion for group actions. That theory has a direct-union permanence principle for actions. Via Bartholdi's permutation-module comparison this covers special permutation modules, but it does not imply the claim for arbitrary modules over a cocommutative Hopf algebra, nor the localizing Serre and torsion-radical conclusions.

The MSC2020 database identifies 16T05 as “Hopf algebras and their applications,” matching the primary mathematical object of the result.

## Limitations
The proof does not show closure under arbitrary inverse limits, products, or non-injective filtered colimits. It does not identify the torsion radical by a simpler elementwise criterion, and it does not determine when \(T_{\mathrm{EA}}(M)=M\) beyond consequences already available from the source. The originality check is literature-based rather than an exhaustive theorem-index search; a general categorical treatment of this newly introduced module notion could independently contain the same consequence.

## References
1. Laurent Bartholdi, “On extensive amenability of algebras,” arXiv:2610.00364v1, first submitted 2026-09-30.
2. Kate Juschenko, Nicolás Matte Bon, Nicolas Monod, and Mikael de la Salle, “Extensive amenability and an application to interval exchanges,” Ergodic Theory and Dynamical Systems 38 (2018), 195–219, DOI 10.1017/etds.2016.32.
3. Mathematics Subject Classification 2020, code 16T05, “Hopf algebras and their applications.”
