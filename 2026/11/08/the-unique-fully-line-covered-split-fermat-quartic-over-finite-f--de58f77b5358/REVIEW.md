# Scientific review: the unique fully line-covered split Fermat quartic

## Correctness

**PASS.** The line-incidence proof directly classifies all pairwise and multiple intersections: \(24\) points support four lines, \(192\) support two lines, and each of the \(48\) lines has \(q-9\) singly incident rational points. In characteristic different from two and three these incidence assertions are valid for every \(q\equiv1\pmod8\). Every \(\mathbb F_{17}\)-point is covered by an exact fourth-power pairing argument. Explicit off-line witnesses establish noncoverage over \(\mathbb F_{25}\), \(\mathbb F_{41}\), and \(\mathbb F_{49}\); the K3 Weil bound proves noncoverage over every larger admissible field. The only admissible prime powers below \(73\) are \(17,25,41,49\), once characteristic three is excluded. Two independent, exhaustive exact-arithmetic programs verify all stated small-field point counts and incidence spectra. The infinite statement is proved symbolically, not inferred from these tests.

## Originality

**PASS, conditional on unverified historical priority.** The \(48\) coordinate-pairing lines are classical, and no novelty is claimed for their existence. Degtyarev–Rams (arXiv:2301.04127, introduction and classification of configurations larger than \(48\)) concerns geometric K3 line configurations, not finite-field rational-point coverage. Schütt–Shioda–van Luijk (arXiv:0812.2377) concerns lines and Néron–Severi theory of Fermat surfaces. Voloch–Zieve (arXiv:1310.1772, Theorem 1.5) already describes the \(\mathbb F_{25}\) specialization and its off-line stratum: that overlap is acknowledged, and novelty is **not** attributed to the isolated \(q=25\) count. Salberger (doi:10.1112/plms.12508) studies a number-field height problem for surface points away from lines. No inspected source gives the exact forty-eight-line incidence spectrum and the global unique-covering theorem over all \(q\equiv1\pmod8\), excluding characteristic three. Residual risk: a classical Jacobi-sum or finite-geometric calculation may encode the theorem in a different form.

## Mathematical value

**PASS.** The line-complement incidence invariant of a smooth quartic K3 surface is geometrically natural. The theorem supplies a complete, not arbitrarily truncated, classification of fields in its structural split-line congruence class for which *all* rational points are accounted for by the visible algebraic curves. The unique \(\mathbb F_{17}\) extremum is explained by an intrinsic fourth-power combinatorial restriction; the bound and explicit witnesses exclude every other admissible field. This gives more than a routine restatement of known line existence or a one-field point count. The conclusion does not assert classification outside the congruence class, in characteristic three, or independent historical-priority certification.

## Closest literature and limitations

1. A. Degtyarev and S. Rams, *Lines on K3-quartics via triangular sets*, arXiv:2301.04127, first public January 10, 2023: geometric line configurations and motivation, not the arithmetic covering classification.
2. M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377: known coordinate-pairing lines and Fermat-surface geometry.
3. J. F. Voloch and M. E. Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772, Theorem 1.5: preexisting explicit \(\mathbb F_{25}\) Fermat-quartic rational-point classification.
4. P. Salberger, *Counting rational points on projective varieties*, doi:10.1112/plms.12508: rational-point complements in a different base-field and counting regime.

No statement is made for characteristic three or for \(q\not\equiv1\pmod8\). A complete general formula for \(N_0(q)\) using Jacobi sums is not provided; instead an exact expression in terms of \(\#X_q\), finite complete counts, and a uniform large-field bound are established.

Self-review: passed. Independent audit: not yet performed.
