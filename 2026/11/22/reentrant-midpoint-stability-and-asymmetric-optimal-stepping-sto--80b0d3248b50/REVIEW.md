# Scientific review: Reentrant midpoint stability and asymmetric optimal stepping-stone placement for two dispersal scales

## Correctness — PASS

The one- and two-species functions are explicitly normalized in `RESULT.md`. A symmetric squared-coordinate reduction proves the exact derivative; exact polynomial root isolation gives three sharp midpoint-stability reversals and four open phases. At length \(L=14\), Descartes' rule, integer-bracketed roots and a strict exact rational comparison prove that the locally preferred central site is beaten by precisely two reflected global sites. `CHECK.py` passed 1,169 supplementary assertions. No finite enumeration is used to claim a continuum proof.

## Originality — PASS on inspected material

The main prior coverage risk is Hodgson et al. (2012), who explicitly optimize stepping-stone positions for population range-shift speed; their objective, kernel and population dynamics differ from the present two-stage multi-species survival objective. Gracanin and Mikac (2023) study multi-species corridor suitability; Saura, Bodin and Fortin (2013) study stepping-stone routes and range expansion; Melià et al. (2016) use multi-species connectivity aggregation. Nearest published mathematical records concern Perron spectra under exponential transport and habitat-area allocation rather than this objective. Actual query comparisons and source inspections are recorded in `AUDIT.json`. A more general prior theorem not located in the searches remains possible; no exhaustive novelty certification is asserted.

## Value — PASS

Simultaneous connectivity planning for differently mobile species naturally uses a multi-species tradeoff. The difference between **local** midpoint stability and **global** passage success is a substantial design warning, while three reversals as the separation changes are an exact structural phase classification. A one-species comparison proves this effect cannot occur for just one dispersal scale. No unmeasured ecological benefit, all-distance global phase diagram, or independent validation is claimed.

## Sources and scientific limitations

- Gracanin and Mikac (2023), https://doi.org/10.1007/s10980-023-01628-8, first public 2023-03-15; motivating multi-species corridor study.
- Hodgson et al. (2012), https://doi.org/10.1371/journal.pone.0047141; closest single-species stepping-stone positioning study, different population-dynamic objective.
- Saura, Bodin and Fortin (2013), https://doi.org/10.1111/1365-2664.12179; network dispersal and range expansion, not equivalent two-stage kernel.
- Melià et al. (2016), https://doi.org/10.1038/srep23705; multi-species geometric aggregation of connectivity metrics.

The fixed log-logistic tail and weights are deliberately stylized; the model ignores patch area, costs, alternative routes, environmental forcing and actual metapopulation viability. Public article access and historical novelty checks remain incomplete outside the inspected materials.

Self-review: passed. Independent audit: not yet performed.
