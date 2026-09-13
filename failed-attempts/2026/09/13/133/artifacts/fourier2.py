import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import eu, es, B, Binv
# Determine fund. frequency vectors: Delta(x) uses modes m in {(+/-1,0),(0,+/-1)} pulled back: phase freq at level k is w_k = (B^k)^T m... but as function of x the frequency is w_k (non-integer!) since B^k x mod 1 composed with trig: exp(2pi i m.B^k x) = exp(2pi i w_k.x), w_k=(B^k)^T m, |w_k| grows like lam^k. So Delta is an almost-periodic sum, NOT a degree-1 trig polynomial. Interval B&B must handle high frequencies.
# Better rigorous route: DIRECT interval evaluation of the defining finite sum + tail bound, box by box.
# Cost estimate: 160k boxes x 12 pairs x 2N+1=29 evals... feasible in numpy batches.
# Tail bound: forward tail k>K: |S_k| <= 2*Mdr*|b|*mu^k (Mdr=max|dr|~0.314). Backward tail j>K': <= 2*Mdr*|a|*mu^j.
# With N=12: mu^12 ~ 3.2e-6? mu^12 = 0.382^12 ≈ e^{12 ln0.382}=e^{-11.55}≈9.6e-6. tail ≈ 2*0.314*0.05*9.6e-6/0.618 ≈ 4.9e-7. Fine vs target |Delta|>= c0 ab = 1e-3*7.5e-4=7.5e-7?? c0*|a||b| with a=b=0.015: 1e-3*2.25e-4=2.25e-7. Tail comparable — need N=16: mu^16≈3.3e-7, tail ~1.7e-8. OK.
# Interval sin/cos over boxes: widths blow up for high-k terms (frequency lam^k*boxsize). For box size h, term k width ~ 2pi|w_k| h * amplitude... at k=12, |w|~ lam^12 ~ 3e5?? width astronomic -> interval eval useless for deep terms on coarse boxes. Need adaptive: split boxes until widths OK: requires h << 1/|w_K| ~ 3e-6?? 300M boxes. INFEASIBLE directly.
# Alternative: exploit cancellation INSIDE each S_k: S_k = [r(B^k xu)-r(B^k xus)] - [r(B^k x)-r(B^k xs)]: each bracket is a stable-direction difference, evaluable via MEAN VALUE: r(p)-r(q) = dr(xi).(p-q) with p-q = B^k(b es) EXACT (no wrap issue in torus lift? B^k(x+bes)-B^k(x) = mu^k b es exactly in R^2 lift; r is 1-periodic so difference well-defined).
# So S_k(x) = [dr(xi1(x)) - dr(xi2(x))].(mu^k b es) where xi1 in segment [B^k xu, B^k xus], xi2 in [B^k x, B^k xs]. Width of dr over those segments: segments have length |b|mu^k (tiny) but LOCATION uncertainty from box h amplified by lam^k. Still high-frequency for large k.
# Hmm. Deeper alternative: write Delta/ab = K0(x) + E, K0 = leading mixed-derivative-like term? Since K(x) ~ O(1) with |K| up to 6 but min over x of max-menu |K| ... the earlier K-minimization suggested K can vanish at isolated points (K~0 at one point) — but that's the LEADING coefficient at scale->0; at FIXED scale r0=0.05 the higher-order terms (a,b up to 0.05, lam^k a up to O(1)) contribute O(1) oscillations that SAVE the bound (the function oscillates at scale 1/a in x). I.e., the proof must use finite-scale oscillations, not Taylor.
# Practical rigorous alternative: COMPUTER-ASSISTED proof via validated evaluation of Delta on a FINE grid + validated modulus of continuity W(d) (Holder) to extend grid to all x.
# W(d) computed above: W(1e-4) ~ 0.011?? That's >> signal 2.25e-7. USELESS: Holder modulus too weak because lam^k amplification.
# Hmm!! Wait, that modulus estimate is way too pessimistic? Check empirically: how much does Delta(x;0.015,0.015) vary when x moves by d=1e-4?
from fastdelta import Delta_grid
rng=np.random.default_rng(0)
X=rng.random((2000,2)); d=1e-4
D1=Delta_grid(X,0.015,0.015,N=14); D2=Delta_grid((X+d)%1.0,0.015,0.015,N=14)
print("empirical max|dDelta| for shift 1e-4:", np.abs(D1-D2).max(), "mean", np.abs(D1-D2).mean())
print("signal scale c0*ab =",1e-3*0.015*0.015)
