# Independent mathematical audit

## correctness

PASS

For a unit eigenvector u of PQP on ran P with eigenvalue t^2 in (0,1), adjoining (Qu-t^2u)/(t sqrt(1-t^2)) gives the stated generic block. The common and orthogonal parts contribute zero. Each generic block has spectrum 1±t for P+Q, deficit phi_p(t), and energy 2t^2(1-t^2); a noncommuting pair's global quotient is an energy-weighted mean of block quotients. With x=t^2 and f_p=phi_p(sqrt(x))/x, the quotient is f_p(x)/(2(1-x)), with f_p(1)=0. In the locally twice-differentiable binomial series, all even binomial coefficients from degree four onwards are positive for 3<p<4; the degree-four term is linear in x and the higher coefficients are negative for 4<p<5. The subtracted x^((p-2)/2) term supplies strict convexity below four and strict concavity above. Anchored secants therefore decrease in t below four and increase above. Direct endpoint computations give f_p(0+)=p(p-1) and -f_p'(1)=p(2^(p-1)-2)/2, yielding the stated best constants via generic blocks tending to t=0 and t=1. In particular the ratios at p=3 and p=5 are 3/(1+t) and 10+15t^2/(1+t); the quartic ratio is constant 6. Continuity gives every intermediate value, strictness holds off quartic for noncommuting pairs, and commuting pairs give equality at zero. The direction is with respect to cosine, not angle. Replay: frozen RESULT.md Steps 1–3; VERIFICATION.md and verify_projection_p_bounds.py were inspected, not executed; their finite diagnostics are not needed to prove the continuum claim.

## originality

PASS

Best of current knowledge, the distinct result is the pair of optimal nonquartic coefficients and strict angular interpolation across 3≤p≤5. The complementary trace deficit, its sign, principal-angle blocks, and the exact quartic projection identity are prior material; the record credits this overlap.

## value

PASS

The sharp positive two-sided comparison quantifies when the complementary deficit measures noncommutation, uniformly in rank. Which limiting principal angles govern either constant reverses across four; this geometry and the complete interval of block ratios are not conveyed by nonnegativity or by the known isolated quartic identity. The claim concerns finite-rank projections on the stated exponent interval, not general positive matrices outside the credited quartic case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
