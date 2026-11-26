# Independent mathematical audit

## correctness

PASS

For S>0, Parseval gives mean one for u=|F|²/S and coefficient Cauchy–Schwarz gives 0<=u<=k. Applying orthogonality again to |F|² gives E u²=1+sum_{d≠1}|R_d|²/S². Summing the difference-fiber Cauchy deficits counts each ordered off-diagonal pair once, yielding C4=1+λ(1−1/k) and the claimed exact amplitude/fiber decomposition. With s=p/2 and f(t)=t^s, the tangent remainder divided by (t−a)² is the integral of (1−r)f''(a+r(t−a)) over r in [0,1]. For s>2 this integral is strictly increasing in t on [0,k], including at 0 because 0<a<k; its value at k is A_s. This gives the quadratic majorant with contact exactly at a,k, and s=2 is exact everywhere. The proposed two-level law has mean one and second moment C4 by k(k−1)=λ(v−1), proving the normalized moment constant. A character-phase vector attains it since its squared character sum is k² at the peak and k−λ elsewhere. For s>2, contact and mean force exactly one peak, and Cauchy–Schwarz at the peak forces the character-phase vector. Distinct peaks produce distinct projective rays; no rigidity at s=2 is implied. For s=3 the quadratic remainder is (t−a)²(k−t), with quadratic coefficient k+2a, so the sixth deficit has exactly the three stated nonnegative terms. Zero coefficients contribute trivial equality. Replaying C6=(k³+(v−1)a³)/v with a=2/3,3/4,3/5 yields 37/9,85/16,289/25 for the three cited cyclic sets. VERIFICATION.md and checker.py were inspected and the script not executed; the arithmetic examples do not prove the general law.

## originality

FAIL

Demonstrable prior implication, not merely a plausible overlap: the known sharp difference-set fourth-moment bound combined with the 1998 bounded-interval upper 3-convex extremum theorem yields the entire sharp p>4 bound with this very two-atom law. Character-phase attainment and rigidity follow from the known character profile, the strict two-node quadratic contact, and Cauchy–Schwarz. The sixth-deficit identity adds the universal cubic residual to the already published fourth-deficit identity by direct expansion; it does not leave a distinct new theorem of the asserted scope. The assessment credits mathematical coverage, not dating of same-day examples.

## value

FAIL

Sharp synthesis norms are natural, and the calculations are useful as an exposition of a classical moment extremum. As a new finding, however, the exact all-p law is mechanically supplied by that extremum and the prior fourth moment, and peak rigidity is immediate from its equality profile. The only proposed extra sixth-order structure is the expansion of one cubic polynomial added to the known fourth deficit. No further quantitative stability conclusion, new inequality, or independently useful nonmechanical remainder is proved. No repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
