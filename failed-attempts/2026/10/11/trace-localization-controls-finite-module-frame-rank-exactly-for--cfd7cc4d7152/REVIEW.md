# Independent mathematical audit

## correctness

FAIL

The algebraic statements derived from the EXPLICIT surrogate definition m_B=min{m:Σ_i w_i* w_i=I_B} are true: trace energy averaging gives sqrt(τ(1)/m_B)≤||iota||≤sqrt τ(1), and on M_{r,s}, ||iota||²=c min(r,s), m_B=ceil(s/r). However the result repeatedly identifies this number as the least length of a finite Parseval RIGHT MODULE FRAME and claims it obstructs standard right module-frame rank. In the established Hilbert C*-module definition (Frank–Larson arXiv:math/0010189, Def.2 and reconstruction formula Thm.4.1), a finite right Parseval frame must satisfy x=Σ_i w_i〈w_i,x〉_B for EVERY x, equivalently Σ_i w_i w_i*=I_r on Z=M_{r,s}, not Σ_i w_i* w_i=I_s. Concrete decisive counterexample r=1,s=2: Z=M_{1,2}, w=(1,0). Then for every row X, w(w*X)=X, so {w} is a one-vector right Parseval frame; the claim says minimum ceil(2/1)=2. For trace τ=Tr_2, ||iota||=1, so the asserted purported right-frame lower bound would say sqrt(2/1)≤1, false. The paper’s private definition instead measures a B-normalizing family/dual left frame; it does not justify the stated interpretation as right-frame rank. No complete repaired claim/files were supplied. Thus the final claimed right-frame theorem is false although its differently named B-normalizing inequalities survive algebraically.

## originality

FAIL

The asserted right-Parseval-frame conclusion cannot be original as a true theorem because it is false by the explicit 1×2 counterexample; the real right-frame reconstruction and counts are already supplied by classical frame theory (Frank–Larson, 2001/2002). The separate B-normalization energy inequality is a one-line pigeonhole consequence of positivity and a known finite B-normalization identity; rank bounds for matrices likewise follow directly from elementary partial isometries. Available Resultary/literature search did not identify a novel result overcoming the stated mismatch. A potentially distinct B-normalization invariant could be investigated but is not this claimed right-frame statement.

## value

FAIL

The claimed motivation is an obstruction to short Parseval RIGHT MODULE frames, but its numeric bound does not constrain them; for M_{1,2} it gives the wrong minimum and a false inequality for actual frame length. Recasting the correct but easy surrogate count Σw_i*w_i=I_s as an ad hoc B-normalization invariant would require independent invariant motivation beyond the ordinary module-rank problem; the surviving trace-pigeonhole and basic matrix-rank arithmetic alone do not substantiate the claimed new mathematical gap. Correct code/proof of the surrogate condition cannot rescue the false right-frame claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
