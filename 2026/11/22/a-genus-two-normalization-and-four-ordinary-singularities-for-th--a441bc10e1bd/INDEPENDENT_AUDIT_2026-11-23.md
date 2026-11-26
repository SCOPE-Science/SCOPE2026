# Independent mathematical audit

## correctness

PASS

The configuration and generic rank agree with Malara §§6.1–6.2. An independent exact computation (python -B /workspace/reviews/octic_check.py; SymPy) used 43 affine Taylor-jet rows, not the submitted homogeneous derivative matrix. Rank 42 at both (2:5:1) and (-59:-21:35) puts both witnesses on the maximal-rank locus; all relevant 43-by-43 minors vanish identically by the generic rank statement. The supplied octic passes the jet constraints, with multiplicities 3,3,3,5 and all four recorded tangent discriminants reproduced. Lex Gröbner elimination of (f,f_x,f_y) gave x^3(x-2)^6, an alternative to the submitted pairwise resultant calculation. Fiber gcds y^2 and (y-5)^4 give exactly the two affine points; the infinity factorization matches and its two simple roots are smooth. One blow-up at each ordinary point gives a smooth strict transform. Over the rank-constant disjoint-section open, the universal corrected divisors are relative effective Cartier divisors (a nonzero section on each smooth integral surface fiber), hence flat; fiber smoothness is open by properness, and exact ordinary multiplicities are an open jet condition. The nonempty integrality open and this open meet in the irreducible projective bundle, and its projection contains a base open with dense member opens. One also need not take the separate absolute factorization on trust: the certified (2:5:1) witness is reduced by finiteness of its singular set, and a smallest irreducible component of degree d<=4 would meet the rest in d(8-d). Cross-intersections occur only at the marked ordinary points and contribute m_component(m_total-m_component). A line through Q meets at most one triple (Q is on no coordinate side), giving at most 4+2=6, and a line missing Q gives at most 4; both are less than 7. A smooth irreducible conic gives at most 3*2+4=10<12. For d=3 or 4 the universal bound 3*2+6=12 is less than 15 or 16. This also proves integrality of the smooth-resolution witness. The genus and square follow from 21-19=2 and 64-27-25=12; genus-two hyperellipticity is standard. The computation is a specialization certificate only, not a parameter census.

## originality

PASS

Best-of-knowledge pass for the generic singularity basket and exact normalization genus, not for the configuration, net dimension, or existence of integral members. The supplied explicit specialization and openness settle the missing geometric statement.

## value

PASS

This is the naturally singled-out nonreduced octic net of the initiating paper, with a known reducible subsystem. The exact full generic basket proves the sharp genus bound, showing that normalization of the extra integral direction is genus two rather than a smaller genus caused by hidden singularities. That is relevant to the geometry of the actual system; the square and hyperellipticity are consequences, not standalone novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
