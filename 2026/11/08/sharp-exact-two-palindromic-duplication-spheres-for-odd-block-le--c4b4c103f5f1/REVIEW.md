# Independent mathematical audit

## correctness

PASS

The H=(n-k+1)(n+1) histories contain disjoint pairs (a,b+k),(b,a) for disjoint original starts a<b. Counting those pairs by shifting b by k-1 gives the stated binomial subtraction and a universal upper bound even when more collisions occur. On a distinct-letter source no insertion can precede the first occurrence of a copied symbol, so the originals and occupied gaps are recovered from the output. For two gaps, fixing the execution order fixes the insertion endpoints and hence both operations. If their original endpoints differ by d<k, the first d symbols of the right-gap reversed block agree across orders but the next symbol is x_a versus x_(a-k+1); if d>=k the operations commute. Within one gap, t=0 gives RR without an equal adjacent pair inside the gap; for t>0 the first such pair is at positions t,t+1, determining the second insertion. This proves there are no further collisions for k>=2. Checked the empty-disjoint-pair boundary and the k=1 exclusion. The separate Python replay `python3 /workspace/audit_evidence/reproduce.py 3` passed 25 exact distinct-letter cases including lengths near 2k and odd k up to 21; the original checker was inspected, not executed.

## originality

PASS

The universal subtraction, numerical formula in the even case, and disjoint commutation are prior. The supported increment is sharpness and the exact collision fibers for odd equal lengths in ordinary palindromic duplication over q>=n. The strongest same-date records change the duplication operation or exclude equal lengths; neither was discarded because of its date, and neither establishes the claimed case.

## value

PASS

The theorem closes the odd-parity gap for an unbounded and natural large-alphabet regime. The structural statement is useful beyond the count: it identifies exactly which two-step error histories remain ambiguous even when every original symbol has a distinct identity, including the overlapping and inserted-copy cases that the commuting bound alone leaves open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
