# Independent mathematical audit

## correctness

PASS

The published four-extrema observational invariant and row endpoint multiplicities are used as established prerequisites. Fix first row a0=1,b0=n-1 and last a_{n-1}=0,b_{n-1}=n-2; intermediate rows choose a∈{0,1},b∈{n-2,n-1}. Every resulting relation has constant four profiles. The boundary rows yield 2^(n-3) subsets each; each middle row has sum 2^(n-3)+2^(n-2)+2^(n-4)+2^(n-3)=9·2^(n-4). Thus one single fiber has 9^(n-2)2^(n²-4n+2) members for every n≥4, a strict improvement over earlier 2^(n(n-2)) factor 9^(n-2)/4^(n-1). At n=5, the exact 16^5 endpoint-vector census groups all profiles, weights by 2^max(b-a-1,0), totals 2^25 relations and computes a unique maximal fiber 93,312. I independently wrote and ran a distinct C++ integer enumeration for n=3,4,5 obtaining (279,512,8,5),(7171,65536,324,1),(235152,33554432,93312,1). This exhaustive n=5 calculation is finite and not a proof of optimality for n≥6. The corrected claim and full self-contained proof are in supplied replacement RESULT.md; no novelty claimed for known profiles, sparsification, injectivity or class counts.

## originality

PASS

Original package overclaimed originality of the four-profile equivalence theorem, edge sparsification, threshold and n=5 class count: all prepublished in October 18/25 and November 2 exact full theorems. Corrected final claim removes those novelty assertions. Its all-n exponentially improved explicit large-fiber lower bound and unique five-world maximum remain genuine best-of-knowledge new refinements.

## value

PASS

Worst-case observational ambiguity is a natural exact representational invariant. The explicit general bound improves prior best guaranteed fiber size by an exponentially diverging multiplicative factor, and the five-world exact unique maximum is the next natural complete finite case after prior n≤4 tables. The corrected note is independently useful although M_n remains open for n≥6.

The dated certificate retains the supplied scientific assessment, sources and limitations.
