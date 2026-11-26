# Independent mathematical audit

## correctness

PASS

On a path with nonzero signed edge weights x,y, center mass alternates p,1-p,p. Equal edge signs make the center the unique extreme score; its upper or lower tail forces p=1/2. For opposite signs the two leaves are distinct extremes, and from times 1 to 2 both leaf masses scale from p to 1-p, so the upper and lower tails again force equality (their transition factors are strictly positive). This gives F(|x|+|y|,x+y)=F(|x|,x)+F(|y|,y) for arbitrary nonzero real weights. Each boundary-ray function is positive additive, hence increasing and determined by its values on the positive rationals. The opposite-sign equation extends the two slopes to the full interior as F(d,s)=cd+bs, with |b|<c. On the signed unit triangle with scores (0,2,0), the top-score mass satisfies p_next=(1-p)/2; successive inequalities then force p_0=1/3, hence b=0. This supplies necessity without any regularity assumption. Undirected conductances give detailed balance for F=cd, proving sufficiency for all times; two-vertex score laws are identical because both scores equal the single signed edge weight. In the finite score range, lower-tail probabilities at a unique minimum are complements of upper tails at the next attainable score, so the direction of each lower-tail inequality is justified. Independent rational witness replay: python3 /workspace/branches/independent_checks.py 2. The frozen checker was read, not run; the universal proof is analytical.

## originality

PASS

The closest primary result classifies time-zero-to-later domination, explicitly disavows consecutive-time monotonicity, and admits score tilts that fail that property on the exact three-vertex model. The signed-path functional equation and the triangle obstruction establish a distinct sharp necessity; stationary sufficiency is standard.

## value

PASS

The sharp cutoff and arbitrary-positive-rule necessity answer a natural strengthening of an existing universal sampling theorem. The contrast is structural: signed paths reduce all local rules to a two-parameter linear family, and a single triangle eliminates the remaining nonstationary direction. The result is stronger than giving an isolated decreasing-tilt counterexample and identifies the unique rule without continuity or a large test graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
