# Scientific evaluation

## Correctness

**PASS within the stated unit-edge homogeneous independent-extinction model.** The incoming-edge generating polynomial obeys a branch product recursion, yielding the exact cross-grouping identity. Its third-order zero at the moment-generating evaluation point gives equality of mean and variance for every extinction probability, and its nonzero third derivative gives strict separation. The finite minimality claim is supported by complete canonical enumeration of all shapes with 2 through 16 leaves, ending with 10,905 shapes, and independent edge-covariance integer-polynomial signatures. The executable package checks the first collision class, performs direct exhaustive survivor-set enumeration for the witness at a rational extinction probability, and recomputes the third raw moment polynomial independently. Code exhaustion is limited to the explicitly stated finite range.

## Originality

**PASS at current literature coverage, with historical priority provisional.** Faller, Pardi and Steel (arXiv:0708.0425, §§1–4) supply independent-extinction phylogenetic-diversity definitions, moments and distribution recursion; they do not state this first failure of joint moment identification across all parameter values or the unique 16-leaf collision. Nipperess and Matsen (2013) treat fixed-size rarefaction rather than independent extinction. The established 9-leaf mean-response ambiguity does not cover the 16-leaf mean-and-variance obstruction, since variance separates the earlier pair. Identical mathematical ingredients in broader generating-function literature may allow alternate derivations, so independent literature review remains a residual risk.

## Value

**PASS.** Exact first and second moments are a standard compact description of projected biodiversity loss, especially when normal approximations are used. The theorem locates the first *structural* limitation of these summaries under a very controlled natural model, separates the full tail law by an explicit polynomial, and gives a general swap identity valid for all equal-size input subtrees. The first-exception uniqueness adds a natural complete finite classification rather than an arbitrary numerical slice. Absolute probability gaps for this witness are small, and no empirical impact is claimed.

## Sources and scientific limits

Relevant primary literature: B. Faller, F. Pardi and M. Steel (2007/2008), arXiv:0708.0425 / DOI:10.1016/j.jtbi.2007.11.034; D. A. Nipperess and F. A. Matsen (2013), DOI:10.1111/2041-210X.12042. The statement is restricted to unit-edge unordered rooted full-binary shapes, whole-parameter equality, and homogeneous independent extinction; none of its finite classification is extended without an explicit proof. Source access and historical-priority limitations are described in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
