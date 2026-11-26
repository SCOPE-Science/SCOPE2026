# Independent mathematical audit

## correctness

PASS

Leibniz determines D from f=D(t), and f descends precisely when nt^{n−1}f vanishes: automatic at even n and exactly f∈(t) for odd n. At odd n one differentiates polynomial representatives and multiplies by f; the bare derivative alone need not descend. Since squaring a derivation in characteristic two gives a derivation, D² is zero iff ff′=0. With x=t² and R=k[x]/(x^s), write f=E+tH at even n and f=xE+tH at odd n, with the two parities disjoint and each summand represented by R. Then f′=H, and the even and odd coefficient blocks of ff′ vanish independently exactly for EH=0 and H²=0 in R. To check the rank independently, restrict D to the odd input block tR (it kills the even block). On odd inputs the output coefficient pair is (Eu,Hu) for u∈R, in the appropriate two parity summands. If v=min(v_x(E),v_x(H)), the kernel in R is x^{s−v}R, hence the rank is s−v in both dimensions. The zero pair agrees with v=s. For v≥ceil(s/2) there are q^{2(s−v)}−q^{2(s−v−1)} pairs at that minimum valuation. For v below that cutoff, H cannot attain v and must lie in x^{s−v}R, giving (q−1)q^{s−v−1}·q^v pairs. Independently, H=0 gives q^s solutions, and each nonzero valuation j of H with ceil(s/2)≤j≤s−1 gives (q−1)q^{s−j−1} choices of H and q^j choices of E. This checks the total, including s=1. The independent matrix replay checked all admissible D(t), testing the square on each basis column and performing field elimination for ranks: q=2, n=2,…,8 and q=4, n=2,…,6. It matched every claimed histogram, including both n=6 and n=7 over F₂. The proof establishes the full parameters and the explicit parity correspondence.

## originality

FAIL

Verified full coverage in distinct indexed text. Resultary 0ca161a05327 states the identical rank polynomial for both truncation lengths and proves a stronger isomorphism theorem for the reduced rank loci. Independently, 1bb3999bc902 gives the very same coefficient-pair correspondence, the parity isomorphism preserving rank, and the total count. The original claim's theorem content, not merely a few parameters, is covered; these are not the frozen record returned under an alias. The indexed paths show later calendar dates than the assignment path, but do not establish historical priority or provenance. This is a present-coverage decision, not a claim that the frozen work historically followed the covering record. The narrower even-only comparator does not by itself settle the odd case. No distinct surviving central claim warrants repair.

## value

FAIL

The rank law and parity symmetry are natural, potentially useful invariants. But as a contribution here they duplicate explicit rank-locus counts and the coefficient identification already present in the distinct indexed results. The low/high-rank formula and total are either stated or mechanical point counts in those results, and the finite replay is corroboration, not an independent new invariant. There is no additional mathematical result under the frozen scope that can be salvaged by narrowing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
