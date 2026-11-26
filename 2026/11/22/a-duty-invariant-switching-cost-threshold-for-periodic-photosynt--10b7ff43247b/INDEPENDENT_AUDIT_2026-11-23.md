# Independent mathematical audit

## correctness

PASS

Let a=u/(u+d), E=exp(-pT), F=exp(-qT). Composing the two affine flows gives multiplier EF strictly between zero and one; the periodic light-start excess over a is (1-a)(1-F)/(1-EF). Its integrated illuminated contribution is that excess times (1-E)/(u+d), giving the stated J_c after dividing by T and charging c once per cycle. For an independent concavity check put R=g_p+g_q, g_s=coth(sT/2), so Phi=2/R. For each s>0, g_s'<0 and g_s g_s''-2(g_s')^2=2(s/2)^2 csch^2(sT/2)>0. Weighted Cauchy–Schwarz gives RR''>2R sum((g_s')²/g_s)>=2(R')², hence Phi'>0 and Phi''<0. The analytic expansion R=2(1/p+1/q)/T+(p+q)T/6+O(T³) gives Phi=pq T/(p+q)-p²q² T³/[12(p+q)]+O(T⁵). Consequently H=Phi-T Phi' starts at zero with cubic coefficient p²q²/[6(p+q)], and H tends to one at infinity because Phi tends to one and T Phi' decays exponentially. Since H'=-T Phi''>0 and J_c'=(c-KH)/T², c=0 and c>=K give the claimed strictly monotone unattained boundary suprema, including the equality c=K. For 0<c<K the derivative switches sign once and gives the unique finite optimum. Substitution gives the strictly positive improvement K Phi'(T_c), monotonicity follows by inversion, and the cubic coefficient gives the reported small-cost law. The fast zero-cost limit fa+Kpq/(p+q) simplifies to the fraction in the statement. The result requires two phases of positive share and a positive dark repair rate; no interchange with a boundary limit in f or v is claimed. Inspected checker.py as text. Its finite diagnostics are not needed for the analytic proof.

## originality

PASS

Best-of-knowledge pass for the exact fixed-per-cycle-cost optimum and its sharp qualitative and small-cost regimes. An important closer antecedent omitted in the frozen bibliography is Fierro Ulloa–Lu–Bernard (2023), whose scalar Han reduction already gives the same periodic integration and exponential interpolation factor in an equal-repair special case. The uncharged light/dark average and the affine matching method are not credited as stand-alone novelty. The inspected work does not solve the charged period problem; its gross-rate formula does not establish the uniqueness and onset law for the charged objective.

## value

PASS

This idealized model isolates a meaningful decision: whether paying a setup charge at each switch makes rapid cycling too costly and whether any best finite period remains. The threshold equals the total excess light-phase output available after complete dark repair in the long-cycle limit, which explains its invariance with fixed positive duty and dark repair. The uniqueness, endpoint behavior and singular cube-root onset give a precise benchmark for charged two-phase models. The cost is stipulated rather than physically estimated, so no claimed empirical, energetic or general control prescription is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
