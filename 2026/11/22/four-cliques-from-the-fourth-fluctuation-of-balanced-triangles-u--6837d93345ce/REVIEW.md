# Independent mathematical audit

## correctness

PASS

Write Y_T for the product of the signs on triangle T, S=sum_T Y_T, and B=(t+S)/2. Independent fair signs make a product expectation one precisely for an even edge multiset and zero otherwise. Triangle characters are centered signs; distinct characters have zero product expectation and hence, for fair binary marginals, are independent. This gives E[B]=t/2 and Var(B)=t/4. In E[S^4] the repeated-index cases contribute t+6*C(t,2): an odd-multiplicity pair of distinct triangle indices leaves a nonempty symmetric difference and vanishes. Four distinct triangles with even edge counts must share each of the three edges of a first triangle abc with a separate one of the remaining triangles, as two distinct triangles share at most one edge. Writing them abx,bcy,caz, the parity of ax and bx forces x=z and x=y, giving exactly all faces of one K4. The converse is immediate and each K4 contributes 24 ordered terms. Thus E[S^4]=3t^2-2t+24q, and centering and scaling the cumulant gives (24q-2t)/16. Solving with the variance yields the stated recovery, including t=0. As a separate normalization check, K4 gives probabilities 1/8, 6/8, 1/8 for B=0,2,4 (the face signs are uniform with product +1), whereas four independent triangles give Binomial(4,1/2); their respective cumulants are 1 and -1/2 at equal variance. I inspected signed_triangle_checker.py and the recorded 1103-graph run; that finite small-graph evidence is separate from the universal parity proof reconstructed here.

## originality

PASS

The constituent parity/Walsh and weight-enumerator identities are standard; the supported addition is the exact identification of the fourth fluctuation of balanced-triangle counts with four-clique counts for every fixed support, including its tetrahedral mechanism. A distinct same-day result obtains a tetrahedral motif recovery for cyclic orientations, not this sign statistic. The access and equivalence risks below limit the historical conclusion.

## value

PASS

The scalar law of a randomized triangle observable does not record vertex identities, and its variance cannot distinguish a tetrahedron from four disjoint triangles. Identifying the exact first relevant fourth-order configuration and recovering an independent graph invariant from the law is a useful, natural motif-identification statement; it is not merely computing the moment of a sum of independent signs. No sampling accuracy or speed advantage is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
