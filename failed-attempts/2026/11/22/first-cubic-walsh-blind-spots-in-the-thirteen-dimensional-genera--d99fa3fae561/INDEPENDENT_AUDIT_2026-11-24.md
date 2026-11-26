# Independent mathematical audit

## correctness

PASS

Counting convolution on the full binary group has one eigenvalue per Walsh character, with no scaling. For forbidden run length r, splitting at zeros into runs shorter than r gives the generating series R/(1-zR), where R=sum_{j=0}^{r-1}(uz)^j and u marks ones. At u=1 modulo 2, counts are odd exactly for n congruent to 0 or r modulo r+1; then all Walsh coefficients are odd. At u=-1 the same series gives an exact zero of the full-support Walsh coefficient in every other residue. For r=3 the independent integer replay, with indicator/butterfly and prefix-state checks agreeing on all 16,382 coefficients through n=13, confirms minimum zero degrees 1,1,2,2,2,2,3 at the singular orders 1,2,5,6,9,10,13. It confirms 3,136 allowed words, nullity 1,296, rank 6,896 and the complete stated degree histogram at n=13. The absolute minima in degrees one and two are 274 and 2. The cubic zero supports are exactly (1,7,9), (1,9,11), (3,5,13), (5,7,13). The minimum zero degree is undefined at the nonsingular orders.

## originality

FAIL

The main finite census is a mechanical extraction from stronger earlier same-family coefficient coverage, not a demonstrated new cancellation theorem. The November 16 run-factor record gives an explicit signed superset sum for every Walsh coefficient in exactly this normalization and boundary convention. Its accompanying verification actually constructs all the full spectrum arrays for k=3,n=1..15, including the entire assigned domain, and already summarizes zero counts for selected members. The exact n=13 histogram and support list are not claimed to have been printed there. The covered operation is evaluating or filtering the already supplied spectra, independent of exact wording.

## value

FAIL

Low-degree visibility despite noninvertibility is a natural question. In this submission, however, the exact numerical threshold and support list are routine summaries of already covered full spectra, with no new structural explanation of that threshold or cancellation pattern. A reproducible summary is useful as a check but does not add a distinct exact invariant beyond routine extraction under the scientific standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
