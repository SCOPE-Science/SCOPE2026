# Independent mathematical audit

## correctness

PASS

Before the block the uncontrolled live state probabilities are e^(−αs) and p_I(s), with p_I'=αe^(−αs)−rp_I. Write A_L=1−e^(−γL), K_L=∫_0^L e^(−αu−γ(L−u))du and M_L=∫_0^L e^(−αu)(1−e^(−γ(L−u)))du. Compared with no intervention, the only change to the eventual conditional chance β/r occurs on live paths which recover during the block; its exact decrease is (β/r)(A_L p_I+αe^(−αs)M_L). Integration by parts gives αM_L+γK_L=A_L. The derivative has the sign of m_L−Φ_d(s): Φ_d strictly increases from zero to either infinity or r/d>1, and m_L∈(0,1), so exactly one positive crossing is the global optimum including s=0 and arbitrarily late starts. Inversion gives the displayed logarithm, or m_L/r when d=0. For a single uniform U∈(0,1), the quantile log(1+U(e^(γL)−1))/γ of the m_L weighting is strictly increasing in L with limits 0 and infinity; its negative exponential proves strict decrease of m_L and its limits 1 and 0. The inverse at 1 is the uncontrolled p_I peak. The integral convention also handles α=γ. In the exact example, A_L=1/2, m_L=1/2 and e^(−s*)=5/6 give risks 307/648 and 1/2; their difference is 17/648. The supplied arithmetic and RK4 program was inspected, not executed. This is an abstract prevention theorem for one target, not a population or field-policy claim.

## originality

PASS

The distinct claim is the fully quantified exact optimum, strict duration monotonicity, and both endpoint laws for this one-transition preventive control of a competing-risk chain. The closest fixed-length quarantine theorem concerns nonlinear population SIR with partial contact reduction and even permits immediate optimal deployment. The closest catalogue timing analogue uses an arrival-window success probability instead of a controlled irreversible hazard and has opposite duration monotonicity. The distinction is established from actual statements, not from search omissions; earlier equivalents under abstract scheduling or reliability terminology remain possible.

## value

PASS

This is a fully quantified preventive scheduling benchmark with an unexpected qualitative distinction: even without population feedback, one should strictly delay a finite perfect block, and a longer block should start earlier. The exact optimizer and both limits isolate the effect of the initially latent state and recovery continuing during protection. It is a useful mathematical check for richer models, not evidence of clinical or policy efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
