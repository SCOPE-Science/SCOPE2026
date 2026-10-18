# Separable images of free homogeneous automorphism groups inherit dense local finiteness

## Finding
Let \(G\) be a Polish group with ample generics and suppose that \(G\) contains a dense locally finite subgroup \(L\). For every abstract group homomorphism
\[
\varphi:G\longrightarrow H
\]
into a separable Hausdorff topological group \(H\), one has
\[
\overline{\varphi(G)}=\overline{\varphi(L)}.
\]
In particular, the closure of every separable homomorphic image of \(G\) contains a dense locally finite subgroup. If \(H\) is torsion-free, then \(\varphi\) is trivial.

Siniora and Solecki prove that, for every countable free homogeneous structure \(M\) over a finite relational language, \(\operatorname{Aut}(M)\) both contains a dense locally finite subgroup and has ample generics. Therefore every abstract homomorphism
\[
\operatorname{Aut}(M)\longrightarrow H
\]
into a separable Hausdorff torsion-free topological group is trivial. This includes every countable torsion-free group equipped with the discrete topology.

## Assumptions and scope
The topology on \(G\) is Polish. "Ample generics" is used in the standard Kechris--Rosendal sense. The target \(H\) is assumed separable and Hausdorff, but the homomorphism \(\varphi\) is not assumed continuous a priori. "Locally finite" means that every finitely generated subgroup of \(L\) is finite.

The application concerns free homogeneous structures in finite relational languages, exactly the setting of Siniora--Solecki's theorem. The conclusion does not address nonseparable target groups, and it does not assert that all separable images are themselves locally finite; only the closure of the image is forced to contain a dense locally finite subgroup.

## Proof
Kechris and Rosendal prove that every homomorphism from a Polish group with ample generics into a separable topological group is automatically continuous. Hence \(\varphi\) is continuous.

Because \(L\) is dense in \(G\), continuity gives
\[
\varphi(G)=\varphi(\overline L)\subseteq\overline{\varphi(L)}.
\]
The reverse inclusion after taking closures is immediate from \(\varphi(L)\subseteq\varphi(G)\). Thus
\[
\overline{\varphi(G)}=\overline{\varphi(L)}.
\]
The image of a locally finite group under a homomorphism is locally finite, so \(\varphi(L)\) is a dense locally finite subgroup of \(\overline{\varphi(G)}\).

Now suppose \(H\) is torsion-free. Every element of \(L\) has finite order, so every element of \(\varphi(L)\) has finite order. Torsion-freeness therefore gives \(\varphi(L)=\{1\}\). The closure identity yields \(\overline{\varphi(G)}=\{1\}\); since \(H\) is Hausdorff, \(\varphi(G)=\{1\}\), proving triviality.

Finally, Siniora--Solecki supply both hypotheses for \(G=\operatorname{Aut}(M)\) whenever \(M\) is a free homogeneous structure over a finite relational language, so the application follows.

## Verification
The argument was checked premise-by-premise against the source statements. Siniora--Solecki explicitly state both required properties for automorphism groups of free homogeneous structures: a dense locally finite subgroup and ample generics. Kechris--Rosendal explicitly state automatic continuity for arbitrary homomorphisms from Polish groups with ample generics into separable groups.

The remaining deductions are elementary and do not require computation: continuous images of dense sets are dense in the image closure; homomorphic images of locally finite groups are locally finite; and a torsion-free group has no nonidentity finite-order elements.

No computational experiment is used as evidence for the theorem.

## Relationship to prior work
Siniora--Solecki place dense local finiteness and ample generics side by side as consequences of coherent extension phenomena, but the checked statements do not formulate the resulting restriction on arbitrary separable homomorphic images. Kechris--Rosendal provide the automatic-continuity mechanism but do not combine it with dense local finiteness.

Sági later gives equivalent conditions for the existence of dense locally finite subgroups in automorphism groups of homogeneous structures; that work broadens the structural context for one hypothesis but does not state the separable-image consequence above.

There is an important nearby stronger theorem in a narrower setting: Macpherson--Tent prove simplicity for transitive free homogeneous structures whose automorphism group is not the full symmetric group. That theorem can force stronger quotient rigidity in those transitive cases. It does not cover all free homogeneous structures: their paper explicitly notes nontransitive free homogeneous examples with nonsimple automorphism groups. The present statement instead applies uniformly to every free homogeneous structure in a finite relational language and, more generally, to every Polish group having the two stated topological/algebraic properties.

## Limitations
The proof is short once the two known ingredients are juxtaposed, so an uncatalogued folklore occurrence is a substantial originality risk. The theorem gives no obstruction to homomorphisms into nonseparable torsion-free groups. For general separable targets with torsion, it only forces a dense locally finite subgroup inside the image closure and does not classify that closure. The application also depends on the finite-relational-language hypothesis used by Siniora--Solecki.

## References
Daoud Siniora and Sławomir Solecki, “Coherent extension of partial automorphisms, free amalgamation and automorphism groups,” arXiv:1705.01888, first submitted 4 May 2017; *Journal of Symbolic Logic* 85 (2020), 199–223, DOI 10.1017/jsl.2019.32. The abstract and Corollary 1.9 state that automorphism groups of free homogeneous structures over finite relational languages contain dense locally finite subgroups and have ample generics.

Alexander S. Kechris and Christian Rosendal, “Turbulence, amalgamation, and generic automorphisms of homogeneous structures,” arXiv:math/0409567; *Proceedings of the London Mathematical Society* 94 (2007), 302–350, DOI 10.1112/plms/pdl007. Theorem 6.24 gives automatic continuity of homomorphisms from Polish groups with ample generics into targets of uniform Souslin number at most the continuum, in particular separable groups.

Dugald Macpherson and Katrin Tent, “Simplicity of some automorphism groups,” *Journal of Algebra* 342 (2011), 40–52, DOI 10.1016/j.jalgebra.2011.05.021. Theorem 1.1 gives simplicity in the transitive free-homogeneous nonsymmetric case and records why transitivity cannot be omitted.

Gábor Sági, “On dense, locally finite subgroups of the automorphism group of certain homogeneous structures,” *Mathematical Logic Quarterly* 70 (2024), DOI 10.1002/malq.202200060. The paper characterizes dense locally finite subgroups via a semi-coherent extension property.
