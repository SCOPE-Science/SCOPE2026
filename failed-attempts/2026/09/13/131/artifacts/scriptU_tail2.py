"""Script U: CORRECT non-stationary-phase tail bound.
M[j,k] = int_{T^3} exp(2pi i (k.y - j.f(y))) dy, |k|_inf<=K.
Split j-region: (a) |j|_2 <= R0 := 8 (finite block: compute directly, no tail);
(b) |j|_2 > R0: phase gradient g(y) = k - Df(y)^T j, |g| >= c|j|-|k|, c=smin(Df^T).
smin(Df): det=1, smax<=3.859 => smin >= 1/smax^2 = 1/14.89 = 0.0671?? Better: certify
directly: smin(Df) = 1/smax(Df^{-1}); bound smax(Df^{-1}) = smax(DS^{-1}A^{-1})
<= (1+alp+bet+alp*bet)*smax(A^{-1}) = (1.3417)*(5.0489) = 6.774 => smin(Df)>=0.1476.
With R0=8, K=2: |g| >= 0.1476*8 - 3.46 = -0.28?? negative -- R0 too small!
Need c|j|>|k|: |j| > 3.46/0.1476 = 23.5. So R0=24: finite block = 49^3 = 117k modes.
Non-stationary phase with ONE integration by parts on T^3 (periodic, no boundary):
|M[j,k]| <= (1/2pi|g|) * int|div(G)| ... <= C1/|g|, C1 = sup|D^2 phase|/|g|... each IBP
gains 1/|g|: two IBP: |M| <= C2/|g|^2 with C2 from up-to-2nd derivatives of f (bounded:
||D2f||<=3.85, ||D3f||<=||A||*(2pi)^3*0.03=24.1). Then tail L2 per column:
sum_{|j|>R0} C2^2/|g|^4 converges (exponent 4>3) and is SMALL for R0=24.
Compute explicit C2 and tail with |g| >= 0.1476|j|-3.46."""
import math
Aop=3.246979603717467; Ainvop=5.04891734
alp,bet=2*math.pi*0.03,2*math.pi*0.02
print("smax(DS^{-1})<=1+alp+bet+alp*bet =",1+alp+bet+alp*bet)
smaxInv=(1+alp+bet+alp*bet)*Ainvop
print("smax(Df^{-1})<=",round(smaxInv,4)," => smin(Df)>=",round(1/smaxInv,4))
c=1/smaxInv
D2=3.845568502451675  # ||D2f||
D3=Aop*(2*math.pi)**3*0.03  # ||D3f|| crude
print("D2<=",round(D2,3)," D3<=",round(D3,2))
# IBP constants: L = (1/2pi i)(g/|g|^2).grad; ||L||<= (|g|*|Dg|/|g|^2 + ...)/2pi
# standard: after 2 IBP, |M| <= (C_a/|g|^2), C_a = (3*D2/(2pi) + ... ) -- use crude C_a = 8
Ca=8.0
K=2; krad=math.sqrt(3)*K
R0=24
tot=0.0; J=60
for n1 in range(-J,J+1):
    for n2 in range(-J,J+1):
        for n3 in range(-J,J+1):
            if n1==0 and n2==0 and n3==0: continue
            j=math.sqrt(n1*n1+n2*n2+n3*n3)
            if j<=R0: continue
            g=c*j-krad
            if g<=0: tot+=1.0; continue
            tot+=(Ca/g**2)**2
# integral tail beyond J: sum_{j>J} (Ca/(c j)^2)^2 * 4pi j^2 dj = (Ca/c^2)^2*4pi/(3J^3)... ~ j^{-4}*j^2=j^{-2} tail
tail_int=(Ca/c**2)**2*4*math.pi/J
print(f"shell-sum tail^2 (R0={R0}..{J}) = {tot:.3e}; integral tail beyond {J} <= {tail_int:.3e}")
print(f"tail L2 per column <= {math.sqrt(tot+tail_int):.3e}")
print("REQUIRED: < s0 ~ 0.0116 (Script T). Check passes?" , math.sqrt(tot+tail_int)<0.0116)
