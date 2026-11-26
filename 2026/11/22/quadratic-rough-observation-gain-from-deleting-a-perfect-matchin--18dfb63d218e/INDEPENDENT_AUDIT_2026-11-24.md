# Independent mathematical audit

## correctness

PASS

For each input the lower approximation is the complement of the upper approximation of the complementary input. With F=[n], nonfull upper values are the empty value, 2n singleton/co-singleton pairs, 2(2^n−n−2) one-full values, and n(n−1) distinct-index co-singleton/co-singleton values. Every one has a full-complement representative. The only inputs with both coverages nonfull are ({i},F\{i}) and their shore swaps, all with distinct images. The full/full value exists by selecting the same singleton index on both shores. Thus there are 1+2(2^(n+1)+n²−n−3)+2n images. The one-full values whose nonfull coverage is (F,F\{i}) or its swap have 1+sum_{k=2}^{n−2} binom(n−1,k)=2^(n−1)−n preimages; both orderings give 4n distinguished fibers. All others save the central fiber are singleton, and subtraction from 4^n gives the claimed c_n. For K_{n,n}, a proper nonempty subset of a single shore yields one-full coverage, with full complementary coverage; the empty subset and full/full value finish the count. The n=1 crown has two isolated vertices, and n=2 has two disjoint edges. Independent exhaustive neighborhood enumeration at n=3,4 returned crown/biclique counts 45/27 and 91/59, and the full crown fiber histograms 44 singletons plus one size 20, and 74 singletons plus 16 of size 4 and one size 118. These are examples, not the proof.

## originality

PASS

The biclique baseline is prior. The surviving claim is the exact increase and complete inverse-fiber census for the crown under the same reflexive tolerance. The inspected statements do not cover that claim on the evidence available.

## value

PASS

Deleting a canonical sparse matching from a symmetric graph gives an exact quadratic net gain rather than merely a qualitative change. The inverse-fiber classification identifies exactly where the remaining indistinguishability sits, including the boundary n=3; the baseline or the image size alone does not give this distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
