# Independent mathematical audit

## correctness

PASS

A length-n binary window modulo global complement is bijective to its n-1 adjacent XOR differences. The nonconstant two-block partitions correspond exactly to all nonzero (n-1)-difference windows, counted L=2^(n-1)-1. Such a cyclic punctured de Bruijn word has 2^(n-2) ones, even for n>=3, so admits precisely two complementary cyclic antiderivatives. Its Euler tour in binary (n-1)-overlap digraph omits only the all-zero self-loop, which is inserted uniquely at zero vertex, creating a bijection with ordinary de Bruijn cycles of order m=n-1. The 2-outregular overlap graph on N=2^(m-1) vertices has A^(m-1)=J, so directed matrix-tree and BEST give 2^(N-1)/N cycles, i.e. 2^(2^(n-2)-n+1). Rotation/complement act freely as argued. Independent complete circular-word enumeration n3..5 finds indexed 6,28,480 and orbit counts 1,2,16.

## originality

PASS

PASS best-of-knowledge. Higgins–Kelley–Sieben–Godbole 2015 Section3/Theorem12 establishes existence and liftability of all Eulerian tours for two-block partitions, but does not state the exact total or adjacent-difference bijection to de Bruijn cycles. The enumeration of ordinary de Bruijn cycles itself is classical (OEIS A016031); this is openly excluded from novel content. Resultary and primary searches found no earlier explicit equivalence for exactly globally binary set-partition universal cycles, with nontrivial complement and rotation quotient. Historical unindexed correspondence remains risk.

## value

PASS

PASS. The count of globally binary universal cycles for all two-block set partitions is a natural exact combinatorial invariant not supplied by prior existence/lifting proofs. The explicit punctured de Bruijn/Euler-tour bijection explains the unexpectedly classical sequence, establishes exact orbit counts for every n and is useful for classification and generation; despite using standard BEST numbers it is not mere renaming without the missing-loop/integration argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
