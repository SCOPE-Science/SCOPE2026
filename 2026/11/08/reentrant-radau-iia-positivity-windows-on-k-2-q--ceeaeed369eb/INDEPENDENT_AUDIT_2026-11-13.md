# Independent mathematical audit

## correctness

PASS

Spectral projectors for L(K_2,q) at 0,q,2,q+2 yield two diagonal entry classes d_A,d_B and positive off-diagonals by monotone g(z)=(z+6)/(z²+4z+6). Independent SymPy factored each diagonal rational numerator exactly as supplied A_q,B_q and independently recomputed Sylvester resultant -46656 q^4(q-2)^4(q+2)^10 F(q) with F=3q^6-64q^5-708q^4-2388q³-2375q²-1776q-576. Exact Sturm counts show no positive quartic root for integer 2<=q<=9; Descartes and explicit negative rational test values imply exactly two roots per quartic for real q>=10. F has unique positive zero q*=30.086536..., so order of negative intervals changes once between q=30 and 31; signs at q=10 and 31 fix root order globally. Numerically corroborated q=10,30,31,50 (q=10 boundaries approximately .5613097,1.0971926,3.0537513,5.7791663). Three safe bands for 10<=q<=30, two for q>=31, unconditional q<=9. No claims about internal-stage positivity; infinite all-q theorem follows from sign/resultant argument, not finite matrices.

## originality

PASS

Best-of-knowledge independent source and logical implication comparison supports an exact new statement after explicit credit for known techniques and partial cases. Historical priority is not certified and residual access risks are retained.

## value

PASS

A natural full step-size topology classification for a standard L-stable implicit method on complete-bipartite graph heat flow, identifying a merger of two forbidden bands with sharp integer threshold 30/31. This adds substantive information beyond generic small-step positivity, unconditional cutoff at graph order eleven and eventual large-step recovery; permits exact selection of safe nonmonotone timesteps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
