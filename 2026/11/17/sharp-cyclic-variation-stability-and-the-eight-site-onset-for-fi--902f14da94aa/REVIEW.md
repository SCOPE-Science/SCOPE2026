# Self-review

## Correctness — PASS

The map is continuous piecewise linear on rank chambers. All chamber matrices preserve constants, and a layer-cake/coarea argument reduces the seminorm to indicators. For neighboring five-point windows, both middle-three selections include the central two of their four shared sites; this bounds the jump response of each chamber by \(1/3\) per affected output edge, with only five affected edges per input edge. The resulting all-dimensional bound is \(5/3\). The complete strict-rank and binary-cut enumeration for five through nine sites uses exact integers and exhausts every chamber/cut pair; the five listed sharpness witnesses and an insertion construction attain the bound at every size from ten onward. The checker is supplied as full standalone source and was executed on the packaged file.

## Originality — PASS (qualified)

Bovik–Huang–Munson's original order-statistic-filter work, Longbotham–Bovik's OS/FIR comparison, and Veldhuizen's full accessible online chapter establish the filter family and rank-wise linearity, not the claimed exact two-input variation coefficients. Published results about cyclic running medians concern the single middle rank, whereas this operator averages three ranks; neither the stated threshold at eight nor the eventual factor \(5/3\) follows by specializing the median conclusions. Targeted searches for the five-point symmetric trimmed mean, its aliases and the exact ratios found no known covering statement. Some older original papers were available in abstracts/metadata only, so historical priority is not independently settled.

## Mathematical value — PASS

The result completely classifies when a classical robust trimmed-mean filter is variation-nonexpansive on cyclic signals, determines the smallest length permitting strict growth, and provides sharp worst-case constants and explicit adversarial inputs for every length. The ability of a local robust smoother to amplify variation of differences is not settled by its denoising role. The shared-middle-ranks lemma explains the universal coefficient and supplies a potentially reusable local sensitivity argument. The exact finite-size transition is a natural stability invariant, not an arbitrary parameter slice.

## Closest literature, evidence and limitations

The original 1982 ICASSP order-statistic family was identified by DOI and conference proceedings; its accessible abstract discusses noise MSE, not two-input variation. The 1983 journal expansion and 1989 structural paper were also located, but complete authorized text was not retrieved. Veldhuizen's online chapter, read at its actual address, presents the trimmed-mean filter and chamber linearity, without cyclic sharp BV coefficients. The scope is equal-weight symmetric five-site trimming and one pass only. Results for median windows, other weights, and statistical risk are not claimed.

Self-review: passed. Independent audit: not yet performed.
