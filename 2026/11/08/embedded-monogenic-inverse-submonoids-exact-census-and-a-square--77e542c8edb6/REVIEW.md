# Scientific review: embedded monogenic inverse submonoids

## Correctness — PASS

The exact identity partitions generators of the symmetric inverse monoid into non-group-type maps and partial permutations. The decisive lemma is verified in the proof: a word in a partial bijection and its inverse has a fixed integer translation on each chain, so any generator of the same inverse submonoid must have displacement \(\pm1\); omission of a chain edge prevents regenerating that edge. Group-type generators are counted by cyclic subgroups, not by a naive two-to-one division. The cycle-index denominator \(\varphi(\ell_\lambda)\) is essential. Acyclic partial injections have the labeled directed-path generating function \(\exp(z/(1-z))\). The stated saddle estimate supplies the constants and the \(n^{-1/2}\) ratio, with explicit central expansion and tail decay. All quantifiers and the empty-set case are addressed.

The separately implemented finite enumerator in `verify.py` reconstructed every inverse closure for \(1\le n\le6\), and compared direct numbers, generator counts, and nilpotent-generated closures to the exact formulas. This supports but does not replace the unrestricted proof. The asymptotic conclusion uses the proved coefficient estimate, not finite extrapolation.

## Originality — PASS relative to examined evidence

Elliott--Levine--Mitchell (arXiv:2303.12387, full nine-page preprint inspected) count *isomorphism types* of monogenic inverse submonoids, identifying types through chain length and permutation order; they do not count the distinct embedded subsets or their generator multiplicities. Laradji--Umar (2022, full 14-page article inspected) count partial injections by image size, fixed points and image extrema, not by generated inverse submonoid. The earlier nilpotent-element papers by Laradji--Umar and Ganyushkin--Mazorchuk are treated as existing coverage of the raw acyclic-element number; the new claim is an embedded-submonoid census and asymptotic. Searches for actual/embedded/labeled monogenic inverse submonoids, generator rigidity, and the asymptotic Laguerre law did not reveal a stronger covering theorem. A failed search does not prove global novelty, and the 2004 papers were not available in full text; priority is provisional.

## Mathematical value — PASS

Counting distinct embedded substructures is a different, intrinsic enumerative problem from counting abstract isomorphism types. The theorem determines a natural full-sequence invariant of the symmetric inverse monoid, including a nontrivial cyclic-subgroup correction, and identifies a sharp structural asymptotic: almost every monogenic inverse submonoid has two generators, while the nilpotent-generated fraction is asymptotic to \(n^{-1/2}\). The exact support-by-cycle partition term permits computations for arbitrary degree and separates group-type behavior from typical chain behavior. It is not a relabeled special case of the published type count. Further work might refine the census by orbit, order, or generator rank; none of that is asserted here.

## Closest literature and limitations

Primary comparison: Elliott, Levine, Mitchell (2023), DOI:10.1080/00927872.2023.2214821; full arXiv preprint inspected. Related full article: Laradji, Umar (2022), DOI:10.12958/adm1793. Relevant earlier nilpotent-element literature: Laradji, Umar (2004), DOI:10.1081/AGB-120038637, and Ganyushkin, Mazorchuk (2004), DOI:10.1007/s00026-004-0213-7; abstracts examined, full text not secured. Only actual inverse submonoids containing the ambient identity are counted. The asymptotic has no uniformity parameter beyond degree. External independent review and comprehensive publication-priority validation remain undone.

Self-review: passed. Independent audit: not yet performed.
