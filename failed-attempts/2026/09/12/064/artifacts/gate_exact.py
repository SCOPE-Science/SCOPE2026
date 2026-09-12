# lane-1212 EXACT proof script (integer arithmetic only): gate + invariants + root number + Heegner obstruction
a1,a2,a3,a4,a6 = 1,1,1,-10,-10
def Frhs(x): return x**3+a2*x**2+a4*x+a6
def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def N_aff(p):
    n=0
    for x in range(p):
        B=(a1*x+a3)%p; C=(-Frhs(x))%p
        for y in range(p):
            if (y*y+B*y+C)%p==0: n+=1
    return n
def ap_good(p):
    return -sum(legendre((a1*x+a3)**2+4*Frhs(x),p) for x in range(p))
def sing(p):
    pts=[]
    for x in range(p):
        for y in range(p):
            F=(y*y+a1*x*y+a3*y-x**3-a2*x**2-a4*x-a6)%p
            dx=(a1*y-3*x*x-2*a2*x-a4)%p
            dy=(2*y+a1*x+a3)%p
            if F==0 and dx==0 and dy==0: pts.append((x,y))
    return pts
def kron(D,p):
    a=D%p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
print("== brute force affine counts ==", {p:N_aff(p) for p in [2,3,5,13]})
print("== ap ==", {p:ap_good(p) for p in [2,7,11,13,17,19,23,29,31]})
print("== a13 brute cross-check ==", 13+1-(N_aff(13)+1))
print("== splitting ==", {p:(kron(-23,p),'split' if kron(-23,p)==1 else 'inert') for p in [3,5,13]})
print("== ord13 ==", ap_good(13)%13 != 0, "a13mod13=", ap_good(13)%13)
print("== Frob2 disc mod13 ==", (1-8)%13, "QRmod13:", sorted((t*t)%13 for t in range(13)))
print("== sing ==", {p:sing(p) for p in [3,5]})
b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4; D=-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
print("c4=",c4,"Delta=",D,"=3^4*5^4?",3**4*5**4==D,"c4 mod3,mod5:",c4%3,c4%5)
for p,x0 in [(3,2),(5,3)]:
    disc=(1-4*((-3*x0-a2)%p))%p
    print(f"p={p} cone-disc={disc} QR={(disc in set((t*t)%p for t in range(p)))}")
print("7935 check:",15*23**2)
print("explicit QR witnesses: (-23 mod 3)=%d=1^2; (-23 mod13)=%d=4^2? %s; (-23 mod5)=%d nonQR in {0,1,4}" % (-23%3,-23%13,(4*4)%13==(-23%13),-23%5))
