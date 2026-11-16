# Review: one-frequency Walsh-basis substitution

## Correctness — PASS
The exact Walsh coefficient for an odd Hamming-weight frequency is reconstructed by the Krawtchouk partial-sum and duality identities, including all signs and binomial normalizations. Every even nonzero Walsh coefficient vanishes by antipodal pairing; no odd coefficient does. A single replacement row is resolved into its removed-basis coefficient and its orthogonal complement, giving a complete rank-two Gram spectrum and strict invertibility. The ratio of successive binomial expressions proves all exact extremizers; Stirling establishes the distinct polynomial and exponential scales. The standalone checker independently tests finite instances, without treating them as an infinite proof.

## Originality — PASS relative to inspected evidence
The closest finite spectral-set results of Ferguson and Iosevich concern orthogonality, tiling, and Fourier support, without a sharp single-frequency replacement stability law. Hamming-ball Slepian studies and a fully inspected quadratic majority-halfcube result treat low-band compression, not the complete even-parity Fourier basis with one odd-frequency swap. The matrix rank-two step and Krawtchouk duality are acknowledged as standard, and the claimed distinct contribution is the natural canonical spectral-set substitution problem plus full parametric, worst/best stability classification. An equivalent older specialization of majority-function Fourier coefficients to rank-one Hadamard perturbations remains a genuine priority risk.

## Mathematical value — PASS
An orthogonal character basis is a natural spectral reconstruction design; a one-frequency error is its smallest possible discrete design perturbation. The exact all-dimension theorem identifies which errors preserve polynomial conditioning and which produce exponentially poor conditioning, even though every substitution still yields invertibility. This distinction informs stability of Fourier interpolation on a natural half-density Boolean spectral set and is not a merely arbitrary finite example.

## Limitations and checked literature
The result is specific to a halfcube of odd dimension and a single frequency replacement. The 2026 finite Fuglede papers establish existence questions, not conditioning. Low-degree Walsh concentration does not imply this full-band basis statement. General matrix row-replacement identities and classical Krawtchouk duality are prior mathematical tools, not claimed independently. Priority may change if an older combined statement exists.

Self-review: passed. Independent audit: not yet performed.
