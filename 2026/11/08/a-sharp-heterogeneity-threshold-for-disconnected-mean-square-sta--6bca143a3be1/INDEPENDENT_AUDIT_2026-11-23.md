# Independent mathematical audit

## correctness

PASS

Re-audited corrected RESULT.md. The two conditional moment masses evolve by P^T diag(A,B); the positive initial mass has positive projection on a nonnegative left Perron eigenvector, so even zero multipliers do not invalidate necessity. The second eigenvalue is nonpositive, so sign det(I-M) measures strict stability. The factor h is positive; all terms of G(-t) are nonnegative with strictly positive constant, excluding any nonpositive root. The first discriminant then gives respectively three positive roots or one, and at zero its real root factorization gives a puncture for d<s or a collapsed upper window for s<d; a triple root leaves one interval. The original 'separated' phrasing was ambiguous because two open components need not enclose an interval of positive length. The repair states both notions and gives a concrete puncture with z=(1-q)h=5/4 double, 3/2 simple, q=(97+5 sqrt(745))/512, lambda=-(1+q)/(5/16+3q). The nested discriminant has negative sign below q_* and a single simple real lambda-zero, so positive endpoint values exclude all interior zeros. At q_* nonnegativity allows only the one interior even-multiplicity lambda-zero, where G has a triple root. Above q_* up to 1/2, simple lambda-roots cannot cross the endpoints (whose values stay positive); the rational alternating signs at q=49/100 certify an interior negative P and pin the two roots throughout. q=1/2 has an explicit negative evaluation, and for q>1/2 continuity from lambda=-1 gives an interior negative value. This proves necessity and sufficiency for existence including the case where the gap can be just a point. Exact bounded replay: python3 /workspace/repairs/2/check_boundary.py passed the nested discriminant, endpoint identities, cusp and puncture factorizations, earlier-slice determinant identity and all four rational witness checks (149481/200000, -147/6250, 83961/200000, -3501/3125). No packaged script was executed.

## originality

PASS

Only for the corrected claim. Earlier Resultary f(1,6) record 2e4ff5de9e1e fully covers the qualitative existence of reentrant windows and the exact persistence classification at ratio six. That was a substantive omission from the original comparison (and qualitative novelty in its scientific assessment is not supported). The repair explicitly credits the antecedent and delimits the worthwhile new content to the all-contrast cusp, joint anti-persistent phase diagram and general multiple-root distinction. The earlier theorem does not supply these as a parameter substitution or immediate corollary. Best of knowledge, not an exhaustive priority guarantee.

## value

PASS

Re-audited the narrowed result: the all-contrast threshold tells which centered quadratic pairs can ever exhibit strict stable-unstable-stable steps under the allowed chains, rather than merely re-demonstrating that some pair can. In particular it detects a range below the deterministic-alternation contrast threshold, and separates an isolated marginal failure from loss over a positive-length range at the boundary. The exact algebraic frontier is a useful check for stability theory and parameter scans; numerical witnesses and the second-moment kernel are supporting evidence rather than the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
