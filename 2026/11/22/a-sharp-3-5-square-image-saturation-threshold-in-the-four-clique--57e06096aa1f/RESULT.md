# The exact square-image deficit of the four-clique evolution algebra over F₍₂₇₎

## Finding

For the unweighted four-clique evolution algebra over \(F=\mathbb F_{27}\), take the natural basis with \(e_ie_j=0\) for \(i\ne j\) and \(e_i^2=\sum_{j\ne i}e_j\). The span \(E^2\) of pairwise products is the coordinate-sum-zero hyperplane. Exactly **1,248 of its 19,683 ordered targets are not individual squares**, so the square image has size **18,435**. Every target with a repeated coordinate is a square. The missing targets are the 24 orderings of each of exactly **52** four-element supports with coordinate sum zero.

## Reduction and finite proof

Put \(s_i=x_i^2\) and \(T=\sum_i s_i\). Then \((x^2)_i=T-s_i\). The matrix of the linear map from \(s\) to \(x^2\) is \(J_4-I_4\); in characteristic three its kernel is the line of constant vectors and its image is the coordinate-sum-zero hyperplane. Since its columns are the \(e_i^2\), its image is exactly \(E^2\). For a target \(y\) in this hyperplane, all solutions for \(s\) are \(s_i=t-y_i\), \(t\in F\). In fact these coordinates sum to \(4t=t\). Let \(L=\{-u^2:u\in F\}\), including zero. The target is an individual square exactly when its support is contained in some \(t+L\).

The attached `check_deficit_27.py` realizes \(F\) as \(\mathbb F_3[X]/(X^3-X+1)\). The cubic has no roots in \(\mathbb F_3\) since \(x^3=x\) there. For each of \(d=3,4\), enumerate every \(d\)-subset \(A\) of the complete set \(L\) and all 27 of its translates. The union is exactly the family of \(d\)-supports contained in a translate of \(L\): membership in either direction is equivalent to taking \(A=S-t\). The resulting cardinalities are \(2925=\binom{27}{3}\) and \(16146=\binom{27}{4}-1404\), respectively. Thus all supports of size at most three work by extension to a triple, and exactly 1,404 unordered four-supports fail before normalization.

Translating every member of a four-support by \(b\) changes its coordinate sum by \(4b=b\). Hence every translation orbit of four-supports has size 27 and exactly one member with sum zero; being covered by a translate of \(L\) is constant on each orbit. There are therefore exactly \(1404/27=52\) missing normalized supports and \(24\cdot52=1248\) missing ordered targets. Subtracting from \(27^3\) gives 18,435. The finite certificate uses exact field arithmetic and exhaustive sets; it makes no extrapolation.

## Prior work and scope

Elduque and Labra, *Evolution algebras and graphs* (arXiv:1312.4685), provide the graph-algebra construction and linear background. *Finite-field square-zero geometry of complete multipartite evolution algebras* (record 555bc289f00b) covers the already known zero-target fiber \(8q-7\) at resonance; it does not enumerate the support of nonzero square targets.

In Paley-tournament language the statistic is the number of four-point supports not contained in any **closed** translate of the signed square set. The related *The Paley-27 tournament: nonpure VC shattering and a center-exclusion gap* (record 04160d23af3c) establishes that all triples are shattered and gives counts of quartets realizing **every** pattern. Its convention has zero as a negative response. Failing full shattering can be caused by any missing pattern and does not count failure of the single all-positive pattern with zero allowed. Likewise *A sharp rank-five genericity threshold for finite Paley tournaments* (record 981ee7b69845) gives an existence property, not this deficit. The compiled Paley data at <https://aeb.win.tue.nl/graphs/Paley.html> and the related exact Paley-81 quartet orbit record (c53aa05fd9d3) provide overlap with higher-order saturation or obstruction questions. Neither a field-size threshold nor priority for those higher-order statements is claimed here.

The result measures the first support size at which the single closed-translate condition fails in this field, and gives the exact size of that failure class. It does not classify all fiber multiplicities, and is limited to the specified algebra and field. Priority is a best-of-knowledge comparison, not an exhaustive literature certification.
