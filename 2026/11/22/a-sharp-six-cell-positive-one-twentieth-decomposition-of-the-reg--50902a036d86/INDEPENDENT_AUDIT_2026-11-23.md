# Independent mathematical audit

## correctness

PASS

The affine coordinate change is invertible, preserves normalized areas, and puts all 45 chord and side segments in Q(√5)². Exact intersection and split-edge deduplication is essential at multiple crossings; the cyclic half-edge traversal counts bounded faces rather than cycles from unsplit diagonals. The separately written and run reproduction /workspace/branches/82cc46dd-df40-4e84-a28e-93484fc1d518/independent_decagon_check.py gives (V,E,F)=(171,390,221), with one outer face, and agrees with all twelve exact normalized areas and multiplicities. Independently, using area (a+b√5)/200, the target pair is (10,0) and the integer functional 4a+9b has per-class values (6,2,5,1,4,2,1,8,4,0,4,8). Fewer than five cannot sum to 40; five would require only classes 7 and 11 and their radical coefficient would be 80j−40, never zero. Unpruned exact pair enumeration at size six (12,376 multisets) gave just (4,8,11,11,11,11) and (7,8,10,11,11,11); the source's 6,186 retained prefixes through size five also recompute correctly. These patterns have sufficient distinct cells and give 20²·C(20,4)=1,938,000 and 10·20·30·C(20,3)=6,840,000 subsets, a total of 8,778,000. The subset count concerns minimal witnesses and does not assert connectedness or exclude larger witnesses. Source copies were read, not executed. Malformed TeX control characters in the displayed binomial-count line do not affect the unambiguous count or its independently reproduced derivation.

## originality

PASS

Neither the 220-cell census total nor the signed denominator 20 is new. The distinct supported finding is the positive decagon construction at 1/20, the minimum support and full minimal pattern/count classification. The independently verified twelve-area refinement was not located in the passages inspected; its individual priority is less certain than the scope distinction between signed and unsigned claims.

## value

PASS

A published exact signed-area question singles out 1/20 rather than an arbitrary target. A positive witness settles that case without cancellation, and the sharp support threshold, both possible signatures and exact subset count describe the attainable minimum, not merely one example or a recomputation of the known number of regions. The finite result does not settle the general positive-union question or connected realizability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
