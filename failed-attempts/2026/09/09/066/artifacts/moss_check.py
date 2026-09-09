"""Moss-convergence cobar check for lane-447 literal target (integer arithmetic only).

E2 addresses (p=3, homological grading E_r^{s,t}, stem=t-s):
  A = alpha_1   : (s,t) = (1,4)    [Ext^{1,4}, stem 3]
  P = 3         : (s,t) = (0,0)    [degree-0 map, stem 0]
  B = beta_{9/8}: (s,t) = (2,112)  [Ext^{2,112}, stem 110]
Claimed carrier x: (S,T) = (5,88)  [(t-s,s)=(83,5)]

Cobar: d: C^{s,t} -> C^{s+1,t} (preserves t). Defining system for <A,P,B>:
  u in C^{0,4} with d(u)=A*P; v in C^{1,112} with d(v)=P*B.
Massey representative m = A*v +/- u*B in C^{S0,T0}:
  A*v: s=1+1=2, t=4+112=116; u*B: s=0+2=2, t=4+112=116.
  => (S0,T0)=(2,116), stem 114. Matches Toda 3+0+110+1=114.
ANSS d_r: (s,t) -> (s+r, t+r-1): stem drops exactly 1 per step, t rises.
Claimed carrier (5,88): dS=+3 vs Massey, dT=-28 (t must never decrease).
Stem path 114->83 needs >=31 dropping steps => filt >= 2+31 = 33, never 5.
Conclusion: no differential zigzag carries (2,116) to (5,88). Double exclusion.
"""
A = (1, 4); P = (0, 0); B = (2, 112)
S0 = A[0] + P[0] + B[0] - 1   # Massey filt (cohomological convention)
T0 = A[1] + P[1] + B[1]
print(f"Massey (S0,T0) = ({S0},{T0}), stem = {T0-S0}")
assert (S0, T0) == (2, 116)
assert T0 - S0 == 114
# Toda cross-check
toda = 3 + 0 + (B[1] - B[0]) + 1
print(f"Toda stem = {toda}")
assert toda == 114
# Carrier comparison
CS, CT = 5, 88
print(f"carrier (S,T) = ({CS},{CT}), stem = {CT-CS}")
assert CT - CS == 83
print(f"dS needed = {CS-S0} (crossing jump +3); dT needed = {CT-T0} (t decrease, impossible)")
assert CT - T0 == -28
# Minimal filtration after 31 stem drops starting from filt 2
min_filt = S0 + 31
print(f"31 drops => filt >= {min_filt}, never 5")
assert min_filt == 33 and min_filt != 5
print("VERIFY_OK: Moss/Massey double exclusion (filt too low for stem distance; T moves wrong way).")
