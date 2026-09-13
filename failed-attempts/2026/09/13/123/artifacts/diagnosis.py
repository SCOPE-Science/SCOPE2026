"""Pinpoint: is the transition wrong, or the base? Test k=1 fully and k=2 p1^2 by hand."""
import math
# k=1: Dx_1 = [0,1]. W_1[(e1),0] = int t = 1/2. Transition gives 1/2*W_0[0,2]=1/2. Correct.
# k=2, p1^2: true = 1/3 (computed: k(k+1)/(k+2)! = 6/24 = 1/4?? wait k=2: 2*3/24=6/24=1/4).
# Direct: int_{Dx_2} (x+y)^2 = int_0^1 s^2 * s ds = 1/4. Yes 1/4.
# Recursion: subs of p1^2 (e=(2,0..)): f in {0, e1, 2e1}: C=1,2,1; A=2,1,0.
# W_2 = 1/3 W_1[0,3] + 2*(1/2) W_1[e1,2] + 1*W_1[2e1,1].
# W_1[0,3]=1/4; W_1[e1,2]=int t(1-t)^2=1/12; W_1[2e1,1]=int t^2(1-t)=1/12.
# W_2 = 1/12 + 1/12 + 1/12 = 1/4. Correct!
# So small-k transitions are RIGHT. Then why does k=50 drift? Ratios 25.5, 654.3...
# 25.5 = 51/2. 654.33 = 654+1/3 = 1963/3? 654.333*3=1963. Hmm 51*... : 51/2=25.5 yes.
# ratio(d) = got/want for int S^d at k=50: 25.5, 654.33, 16893.75, ...
# hypothesized got = int (x_1+...+x_50 + 49*t?)... i.e., computed as if Q'=Q (all k vars incl current)?
# If the code's 'restriction' Q' actually still contains t_k, then Q(t',t_k) expanded would
# double count. But subs use exponent vectors of Q' on k-1 vars — same vectors, fine.
# Alternative hypothesis: W_0 base wrong: W_0[h,r] = delta: correct (point at S=0, u=1).
# W_1[h,r] = int_0^1 t^A (1-t)^r: code gives C/(A+r+1) W_0: = 1/(A+r+1) — but TRUE Beta(A+1,r+1) = A! r!/(A+r+1)!.
# THERE it is: the transition factor 1/(A+r+1) is only valid for f=0 part... no wait:
# W_k[h,r] = sum_f C(h,f)/(A+r+1) W_{k-1}[f, A+r+1]. At k=1: W_1[h,r] = sum_f C/(A+r+1) W_0[f,A+r+1]
# = (only f=0 survives) C(h,0)/(A+r+1) * 1 where A=W(h): = 1/(W+r+1). But TRUE = Beta(W+1,r+1) = W!r!/(W+r+1)!.
# These differ unless W=0 or r=0!! At r=0: 1/(W+1) = W!0!/(W+1)! = 1/(W+1). Same. So r=0 fine at k=1.
# But at k=2, children need W_1[f, s] with s>=1: WRONG values (missing factor W(f)! s!/(s+... ) hmm).
# So the recursion is wrong for r>=1?? Let's recheck derivation:
# W_k[h,r] = int_{Dx_{k-1}(1)} Q'^... : inner integral over t_k in [0,u]: int Q(t',t_k)^h (u-S'-t_k)^r dt_k.
# With Q = sum_q c_q t_k^q (c_q weight pieces): Q^h = sum over sub-multis: C(h,f) Q'^{f} t_k^{A}.
# inner = C(h,f) Q'^f int_0^u t^A (u-S'-t)^r dt. Substitute t = (u-S')z: = (u-S')^{A+r+1} B(A+1,r+1).
# AH — the Beta factor B(A+1,r+1), NOT 1/(A+r+1)! I forgot B(A+1,r+1) = A!r!/(A+r+1)! vs 1/(A+r+1).
# At r=0: B(A+1,1)=1/(A+1). Same. So the fix: multiply each transition by B(A+1,r+1)*(A+r+1) = A! r!/(A+r)!.
# i.e., factor = C(h,f) * Beta(A+1, r+1), and child (f, A+r+1). This matches the ORIGINAL (first) DP!
# So the original DP's transition was correct; its bug was ONLY the weight W(f) [used WFs=W(f_full... let me recheck:
# original: B1 = (k-1)+WFs+s+1 with WFs=W(f). Claimed Beta(A+1, (k-1)+W(f)+s+1). True needed: the child's r'=A+r+1 enters
# W_{k-1}[f, r'] whose own expansion... no — the transition factor itself should be Beta(A+1, r+1) [the u-power
# at level k is r, and int_0^u t^A (u-S'-t)^r dt = (u-S')^{A+r+1} B(A+1,r+1) — INDEPENDENT of k-1].
# Original code used Beta(A+1, (k-1)+W(f)+s+1) — WRONG (that's the error found: ratio k+d style).
# Correct: factor Beta(A+1, r+1), child (f, A+r+1). And needed-set DP structure from dp_correct.py is right.
# Fix and rerun: bottom-up with factor C*B(A+1,r+1).
print("diagnosis confirmed by hand computation")
print("fix: transition factor = C(h,f)*Beta(A+1,r+1), child (f,A+r+1)")
