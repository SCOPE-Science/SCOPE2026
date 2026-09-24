# Independent audit — Mahler spectrum of the 16 reflexive polygons

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/037`  
**Audited directory tree:** `807d2be7b573a4e45bf1222717f5533e0b122b82` (unchanged when checked at repository head `c40ff4843745efb8c2c7275f5cacbda243c36a25`)  
**Review type:** separate AI independent audit.

## Claim audited

The record enumerates the Euclidean Mahler products `area(P) area(P°)` over the 16 two-dimensional reflexive lattice polygons, claiming the spectrum {27/4, 8, 35/4, 9} with multiplicities 2/6/4/4. It further identifies exactly three centrally symmetric classes, two parallelograms of product 8 and one hexagon of product 9, and calls the resulting symmetric non-parallelogram gap 1 a new finite-family stability gap.

## Correctness — PASS

I independently recomputed the geometry from the published 16 representatives. Convex hulls, exact rational shoelace areas, primitive facet equations, and polar vertices reproduce every table entry. All polar vertices are integral. The products are 27/4 for rows 1–2, 8 for rows 3–8, 35/4 for rows 9–12, and 9 for rows 13–16. Boundary counts satisfy the 12-point relation. Exact set comparison gives exactly three centrally symmetric polygons: the two parallelograms with product 8 and the six-vertex polygon with product 9. Thus the numerical spectrum and gap statement are correct.

## Originality — FAIL

The spectrum is a routine consequence of a published classification presentation. Grassi, Gugiatti, Lutz and Petracci, **“Reflexive polygons and rational elliptic surfaces,”** *Rend. Circ. Mat. Palermo* 72 (2023), DOI `10.1007/s12215-023-00922-3`, §3.5, explicitly states that there are exactly 16 reflexive polygons, orders them as `P3,...,P9` by normalized volume, and gives the polar pairings:
`P3 <-> P9`, three `P4i <-> P8i`, two `P5i <-> P7i`, and four `P6` classes self-dual up to GL(2,Z). The same section states `Vol(P)+Vol(P°)=12`.

In dimension two, their normalized lattice volume is twice Euclidean area. Therefore their published data immediately yields the record's whole Mahler spectrum:
`(3*9)/4 = 27/4` (2 classes), `(4*8)/4 = 8` (6), `(5*7)/4 = 35/4` (4), and `(6*6)/4 = 9` (4). No new enumeration is needed to obtain the headline spectrum.

## Scientific value — FAIL

A bounded repair was considered around the centrally symmetric subfamily. Within a classified set of only 16 polygons, checking which three representatives satisfy `P=-P` and noting that the two parallelograms have product 8 while the remaining symmetric hexagon has 9 is correct. But once the published volume/duality classification is accounted for, this “gap 1” is a tiny finite-case observation rather than a new stability theorem, method, or reusable structural result. It does not meet the campaign value threshold.

## Disposition

**FAILED.** Correctness passes, but originality and value fail. Preserve the original package in the failed-attempt archive together with this audit.

## Search/access notes

The decisive 2023 article is open access; §3.5 was inspected directly. Searches also covered “16 reflexive polygons Mahler volume”, “reflexive polygon polar volume 12”, “centrally symmetric reflexive polygons”, and the record's cited 12-point literature. No inaccessible source was used in the failure determination.
