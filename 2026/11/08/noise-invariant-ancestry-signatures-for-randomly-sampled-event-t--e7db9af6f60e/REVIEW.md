# Scientific review

## Correctness

**PASS.** The central identity follows by conditioning independent observation channels on the latent path indicators, after which strict laminarity and positive mass at all nodes give a nonzero signed covariance formula. The graph theorem follows from the rooted-forest ancestor closure and an explicit recursive universal-vertex construction; equal closed neighborhoods are shown to coincide exactly with unary runs. The empirical guarantee uses bounded Bernoulli Hoeffding estimates and a union bound. The locally rerun standard-library checker tested every labelled tree on two through six vertices with every root (8,476 rooted instances), verified 81,711 exact pairwise covariance signs, and reconstructed every labelled unary-contracted forest from the positive-covariance graph. Finite checks are diagnostics, not an infinite proof.

## Originality

**PASS, subject to historical-priority uncertainty.** The motivating event-accumulation paper proves a different graph theorem: a noiseless conditional-independence *line graph*, and explains that observation noise destroys its screening. The present theorem establishes a complete *unconditional covariance-sign graph* classification and exact identifiable quotient in the presence of unknown, event-specific, asymmetric independent measurement channels. Classical trivially perfect graph characterizations and binary-channel covariance attenuation are credited, not claimed separately. The earlier oncogenetic-tree literature includes noisy recovery procedures but uses simultaneous edge-event accumulation, with materially different dependence between separate branches. The original 2002 paper was not read in full after lawful open-access searches and unsuccessful institutional retrieval; fuller priority comparison remains warranted. Searches do not prove novelty.

## Mathematical value

**PASS.** This is a natural full structural classification and identifiability boundary for recovering hierarchy from cross-sectional event data despite unknown heterogeneous measurement errors. It identifies a precise recoverable branching skeleton when the noiseless conditional-independence graph becomes unreliable, supplies a falsifiable graph-class diagnostic, and gives a sufficient finite-sample recovery bound. The finding is not merely a numerical table or a restatement of a known graph equivalence: the sign-robust noisy observation theorem and statistical interpretation are the substantive focus.

## Closest literature and limitations

Labouriau (2026), arXiv:2610.40127v1, supplies the single-path tree model and the distinct Markov graph; Wolk (1962) and Golumbic (1978, 2022) supply classical trivially perfect graph theory; Olde Loohuis et al. (2014) and Szabo–Boucher (2002) cover noisy oncogenetic tree inference under different generative assumptions. The result assumes strict positivity at all nodes and independent positively informative coordinate channels. Only covariance-sign information is classified, so full distribution compatibility, noise rates, and the order within unary chains are not determined. The sample bound is sufficient rather than proved optimal. Definitive novelty requires further human literature review, particularly the inaccessible original 2002 article and related measurement-error research.

Self-review: passed. Independent audit: not yet performed.
