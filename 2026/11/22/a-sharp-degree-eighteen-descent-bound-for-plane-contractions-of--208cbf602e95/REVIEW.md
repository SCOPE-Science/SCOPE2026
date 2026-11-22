# Scientific review of the plane-contraction descent spectrum

## Correctness (C): PASS
The geometric input is the standard classification of \(56\) exceptional curves on a degree-two del Pezzo surface. The explicit four-family integer model verifies their intersection form and enumerates all \(576\) unordered disjoint seven-curve sets. The generated seven reflections enumerate \(2{,}903{,}040\) elements of \(W(E_7)\), partitioned into \(60\) conjugacy classes; their exact sizes sum to the group order. Each class is represented on the full \(576\)-set permutation action, giving the reported minimum-cycle spectrum without interpolation. The complete certificate and a separate witness check were executed and reproduced successfully.

The identification of Frobenius-invariant contraction sets with ground-field contractions uses descent of pairwise disjoint exceptional curves and triviality of the Brauer group of finite fields. Loughran–Trepalin, Theorem 1.2, establishes sharp finite-field realizability for odd \(q\ge9\). The statement does not assert sharpness for the remaining odd fields.

## Originality (O): PASS, qualified
Classical geometry supplies \(56\) curves, their \(576\) unordered blowdown sets, the Geiser involution, and \(288\) heptads. Bergvall's papers on plane-quartic markings and degree-two del Pezzo Frobenius-type counts describe those foundations and count types of surfaces. Loughran–Trepalin proves which types are realized. The new evaluated invariant is **the complete shortest-orbit distribution of Frobenius on the \(576\) seven-curve contraction sets**, including the extremal orbit \(18^{32}\) that maps to \(9^{32}\) on heptads. Counting classes, class traces, or fixed points of the 288-point quotient alone does not determine which heptads lift to invariant plane contractions.

Closest primary sources: Loughran–Trepalin (arXiv:1811.06785, Theorem 1.2), Bergvall (arXiv:2211.12855, sections 2–4), and Bergvall (European Journal of Mathematics 2023, sections 1–2.3). Existing \(W(E_7)\) conjugacy tables contain the base group classification, but not the evaluated orbit-minimum table on this particular \(576\)-point action among the materials inspected. This comparison is not an assertion that all historical tables or publications are indexed. An older equivalent orbit calculation remains a residual priority risk.

## Mathematical value (V): PASS
The least extension degree allowing an actual morphism to the projective plane is a natural birational descent invariant, more restrictive than obtaining an Aronhold heptad or individual bitangents. The sharp universal degree \(18\) and a complete nine-value classification give exact bounded extensions for explicit blowdown searches. The arithmetic distinction \(9\) versus \(18\) reveals a nontrivial Geiser-sheet obstruction invisible in the 288-heptad quotient. The exact finite group calculation is not presented as a new group classification; its mathematical content is the evaluated descent invariant and its fieldwise realization.

## Limitations and risks
Only odd characteristic is asserted; explicit polynomial equations for extremal surfaces are not supplied; the small-field set \(q\in\{3,5,7\}\) is not exhaustively resolved. The 60-class census is a finite exhaustive computation whose source and outputs are included; independent external mathematical validation has not been done. Equivalent unindexed historical tables cannot be categorically excluded.

Self-review: passed. Independent audit: not yet performed.
