# Independent mathematical audit — 2026-10-01

## Non-Golod certificate for the facet-glued stacked-plus-octahedron 9-vertex 2-sphere G9

**Disposition:** failed.

The explicit named G9 product witness is sound, but the non-Golod conclusion is already covered by the published surface-triangulation characterization; additionally, the committed enumeration script does not certify the asserted all-18 same-C4 extension.

## Correctness

**UNRESOLVED** — The named G9 witness is correct: the listed facets make 06 and 17 missing while 01, 07, 16 and 67 are edges, so the induced subcomplex on {0,1,6,7} is a hollow 4-cycle; the displayed four coboundary equations for e01 are inconsistent, proving a nonzero Tor product. However the final claim also asserts the same C4 mechanism for all 18 facet gluings. The actual committed enumerate_check.py has the permutation-loop body dedented and therefore tests only one permutation per each of three stacked-facet orbits, i.e. three representatives. The claimed corrected 18-case rerun is not present in the audited tree, so that universal mechanism was not freshly certified.

## Originality

**FAIL** — The scientifically central conclusion that this triangulated 2-sphere is non-Golod is already a direct corollary of Iriye-Kishimoto's characterization of orientable surface triangulations: Golod if and only if neighborly. G9 has explicit missing edges, hence is not neighborly and therefore not Golod.

## Scientific value

**FAIL** — The named non-Golod conclusion and the facet-sum variants fall inside a known structural classification. The explicit missing-edge product is a routine certificate for a covered case, while the claimed 18-case extension is not fully certified in the tree; this does not supply an independently motivated new gap.

## Sources checked

- Iriye and Kishimoto, Golodness and polyhedral products for two-dimensional simplicial complexes, Forum Math. 30 (2018), 527-532.
- Iriye and Kishimoto, Golod and tight 3-manifolds, theorem recalling the surface result: a closed connected orientable surface triangulation is Golod iff neighborly.
- Resultary search for Golod 2-sphere, hollow 4-cycle, missing-edge Tor product, and the named G9.
- Audited package RESULT.md, artifacts/verify.py and artifacts/enumerate_check.py.

## Residual risks

- The universal 18-case mechanism remains unverified from actual committed code; the record is rejected independently on originality and value grounds.
