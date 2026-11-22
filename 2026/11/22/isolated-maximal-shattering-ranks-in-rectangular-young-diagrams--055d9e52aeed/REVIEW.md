# Scientific review

## Correctness — PASS

The assertion is about all integers \(m\ge3\) and areas \(0\le k\le2m(m-1)\), including boundaries. The finite-poset rank-ideal trace criterion is reconstructed using the all-positive/all-negative patterns and interpolation within intervals of lower ideals. For an antichain of size \(m-1\), only its omitted row can contain cells incomparable to every queried point, and at most \(m-1\) columns qualify. The trace criterion forces all \(m-1\) to be incomparable, uniquely determining the antichain and the permissible area. A full-row antichain of size \(m\) is excluded. Direct trace checks and separate geometric closure computations, implemented in `verify.py`, corroborate the proof at small parameters.

## Originality — PASS, qualified

Primary text comparisons distinguish this top-dimensional support-rigidity theorem from rank enumeration and unimodality of rectangular partitions (Melczer–Panova–Pemantle 2018; Early 2019) and from general shattering-extremal set-family constructions (Kusch–Mészáros 2017). The closest available square-board rank-constrained bound addresses a different aspect ratio and does not imply the exact isolated progression or unique top support at each permitted area. A general ideal-shattering criterion is treated as background rather than original. Searches for alternative descriptions, including down-set rank sections, interval obstructions and fixed-area Young diagrams, did not reveal a covering theorem. Historical priority beyond inspected sources is not guaranteed.

## Value — PASS

Rank-unimodality of diagram counts does not control the Boolean geometry of cells identifiable from fixed-area diagrams. The theorem reveals an exact and infinitely persistent gap phenomenon: as area changes by one, the existence of a maximal shattered support repeatedly turns off, then on \(m-2\) cells later. The unique top support and arithmetic progression make the boundary structurally transparent and furnish precise extremal examples for rank-restricted distributive-lattice concept classes.

## Limitations

The exact lower-dimensional shattering polynomial and exact dimensions off the exceptional ranks are not claimed. Computations are finite checks, not an all-order certificate by themselves. Unindexed equivalent formulations remain possible.

Self-review: passed. Independent audit: not yet performed.
