# Independent mathematical audit

## correctness

PASS

Grounding retains diagonal 2+mu and splits the matrix into paths on g_i-1 vertices. A closed step word of span R has (ell-R)_+ translations into an ell-vertex path, so every trace of an even adjacency power is discretely convex in ell. At ell>=1 the word going ell steps each way witnesses strictness at order 2ell; its coefficient is positive both in the heat expansion and in the absolutely convergent inverse-power expansion (path adjacency norm strictly below 2). Strict gap transfers give exactly the stated multisets. Counting gap words with an anchor gives N binom(k,r)/k, and the unique long gap has N possible starting vertices unless k=N, when there is only the empty follower problem. The degenerate cases k=1 and k=N-1 agree. Independently, det(T_{g-1})=sinh(g theta)/sinh(theta) by the tridiagonal recurrence; its mu-log-derivative is the claimed inverse trace, with limit (g^2-1)/6. A fresh bounded check used integer path-walk recurrences (80 second differences, up to length 18) and 75 (N,k) groups of labeled masks, N<=12. Replay: /workspace/branches/spectral_design_replays.js, cycleCheck. The supplied check.py was inspected, not run; its floating-point assertions are supplementary. Neither exact integer finite checks nor the uploaded evidence constitute a formal proof certificate.

## originality

FAIL

A distinct same-day record explicitly covers the principal heat and inverse-moment classification under identical assumptions, with the same walk-span convexity proof and the labeled count. Its positive-weight heat-integral formulation also shows that the change to an inverse-power binomial proof does not change the claim. Same-day cataloguing establishes overlapping coverage, not relative chronology. The mass-dependent elementary inverse-trace evaluation is not a surviving independently valuable contribution.

## value

FAIL

Simultaneous exact extremizers would be a meaningful classification on their own, but that classification and its structural walk lemma are already present in the matching record. The remainder is an alternate positive expansion, a routine exact evaluation of the Dirichlet inverse trace, and the immediate placement count for the explicitly known long arc. No independently worthwhile narrower claim remains here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
