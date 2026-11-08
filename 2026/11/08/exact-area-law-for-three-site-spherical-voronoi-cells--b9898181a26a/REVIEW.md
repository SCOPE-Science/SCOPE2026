# Scientific review of the three-site spherical Voronoi area law

## Correctness — PASS

The claim is for exactly three independent Haar-uniform sites on the unit two-sphere and the ordinary (unnormalized) area of the labelled site's Voronoi region. The core reduction is exact: its two bisector inequalities define a spherical lune of area \(2(\pi-\gamma)\), where \(\gamma\) is the angle between the bisector normals. From uniform site height, each independent bisector normal has the surface-area density \((e\cdot b)_+/\pi\). A two-dimensional Gaussian polar integral gives the exact positive-part kernel \([\sin\gamma+(\pi-\gamma)\cos\gamma]/(6\pi)\). Angular-density reweighting then yields the CDF; its normalization, derivatives, moments, and endpoint Taylor orders are explicitly checked. The path from the primitive site-sampling law to the cell-area CDF contains no numerical inference and covers the full interval, including boundary values.

The standalone checker passed numerical integration, derivative identities, deterministic exact-CDF checkpoints, 500,000 direct site configurations, and separate 125,000-point lune-area checks. Finite numerical checks corroborate but are not proof. All computations in the proof are analytic and self-contained.

## Originality — PASS (historical priority provisional)

The exact problem is a randomly labelled spherical Voronoi cell with **three** independent area-uniform generating sites. Kabluchko–Thäle's full accessible article (arXiv:1911.07221, especially Sections 2–4) develops the same spherical Voronoi framework and its random halfspace representation but computes cell *face vectors*, not its area distribution. Devroye–Györfi–Lugosi–Walk (arXiv:1512.04267v1) proves a **large-number-of-sites** Euclidean typical-cell measure limit, so neither its dimension nor its limit implies this fixed-three-site spherical CDF. Cho–Saul (2009), Section 2 and Eq. (6), explicitly gives the positive-part cosine kernel used here. That kernel is not novel; the spherical Voronoi representation and its conversion into a full cell-area law and sharp area tails are the proposed mathematical contribution.

The nearest accessible indexed research records concerning Voronoi cells deal with hyperbolic Poisson limits or Euclidean lattice-cell clearance, not this three-site sphere law. Earlier broad spherical tessellation works by Miles (1971) and Arbeiter–Zähle (1994) are especially material historical risks: accessible citation records identify them, but their full texts could not be substantively checked. The searchable JSTOR record for Miles did not expose article content, and an authorized institutional request was unavailable. These gaps are recorded and not treated as proof of novelty. No independent priority certification is asserted.

## Mathematical value — PASS

The random surface area of a typical spherical Voronoi region is a natural geometric size invariant, but exact full laws for individual cells are rare. The smallest genuinely nontrivial random tessellation on the two-sphere has a complete elementary area distribution, a nontrivial exact variance \(4\pi^2/9-10/3\), an exact one-quarter-sphere lower-tail probability \(1/6\), and sharply different small-area and nearly-hemisphere exponents, five and two. This supplies both a benchmark for spherical-tessellation simulation and a transparent analytic link from random great-circle intersections to probabilistic geometry. The statement is a whole natural distribution law rather than an arbitrary fixed-n sample or unmotivated numerical parameter.

## Limits and closest literature

The result does not concern size-biased cells, four or more sites, higher-dimensional spherical cells, joint cell areas, or arbitrary site distributions. The positive-part kernel formula and the halfspace representation are known, and historical source coverage remains incomplete, particularly Miles (1971) and Arbeiter–Zähle (1994). A related later treatment is Kabluchko–Thäle (2019), but its proved f-vector result does not subsume the stated area law. This is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
