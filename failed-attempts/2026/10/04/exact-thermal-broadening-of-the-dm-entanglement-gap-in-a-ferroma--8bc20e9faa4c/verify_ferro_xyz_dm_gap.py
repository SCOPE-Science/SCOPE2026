#!/usr/bin/env python3
import math

def params(Jx,Jy,Jz):
    A=(Jx-Jy)/2.0
    P=-(Jx+Jy)/2.0
    Z=-Jz
    assert A>0 and P>0 and Z>0
    nuc=A+Z
    assert nuc>P
    Dc=math.sqrt(nuc*nuc-P*P)
    return A,P,Z,nuc,Dc

def edges(Jx,Jy,Jz,T):
    A,P,Z,nuc,Dc=params(Jx,Jy,Jz)
    q=math.exp(Z/T)*math.sinh(A/T)
    if q<=math.cosh(P/T):
        Dm=0.0
        um=None
    else:
        um=T*math.acosh(q)
        Dm=math.sqrt(max(0.0,um*um-P*P))
    up=T*math.asinh(math.exp(Z/T)*math.cosh(A/T))
    Dp=math.sqrt(up*up-P*P)
    return A,P,Z,nuc,Dc,Dm,Dp,um,up

def c_under(Jx,Jy,Jz,D,T):
    A,P,Z,nuc,Dc=params(Jx,Jy,Jz)
    nu=math.hypot(P,D)
    num=math.sinh(A/T)-math.exp(-Z/T)*math.cosh(nu/T)
    den=math.cosh(A/T)+math.exp(-Z/T)*math.cosh(nu/T)
    return max(num/den,0.0)

def c_over(Jx,Jy,Jz,D,T):
    A,P,Z,nuc,Dc=params(Jx,Jy,Jz)
    nu=math.hypot(P,D)
    num=math.sinh(nu/T)-math.exp(Z/T)*math.cosh(A/T)
    den=math.cosh(nu/T)+math.exp(Z/T)*math.cosh(A/T)
    return max(num/den,0.0)

def concurrence(Jx,Jy,Jz,D,T):
    A,P,Z,nuc,Dc=params(Jx,Jy,Jz)
    if abs(D-Dc)<1e-13:
        return 0.0
    return c_under(Jx,Jy,Jz,D,T) if D<Dc else c_over(Jx,Jy,Jz,D,T)

def main():
    edge_checks=0
    sign_checks=0
    for Jx,Jy,Jz in [(-1.0,-2.0,-3.0),(-0.5,-1.5,-2.0),(-1.2,-2.0,-2.8)]:
        for T in (0.18,0.3,0.55,1.0):
            A,P,Z,nuc,Dc,Dm,Dp,um,up=edges(Jx,Jy,Jz,T)
            assert Dp>Dc
            if Dm>0:
                assert Dm<Dc
                nu_m=math.hypot(P,Dm)
                lhs=math.cosh(nu_m/T)
                rhs=math.exp(Z/T)*math.sinh(A/T)
                assert abs(lhs-rhs)/rhs<2e-12
            nu_p=math.hypot(P,Dp)
            lhs=math.sinh(nu_p/T)
            rhs=math.exp(Z/T)*math.cosh(A/T)
            assert abs(lhs-rhs)/rhs<2e-12
            edge_checks+=1

            maxD=max(Dp*1.4,Dc+2.0)
            for k in range(101):
                D=maxD*k/100.0
                C=concurrence(Jx,Jy,Jz,D,T)
                predicted=(D<Dm-1e-10) or (D>Dp+1e-10)
                if min(abs(D-Dm),abs(D-Dp),abs(D-Dc))>1e-8:
                    assert (C>1e-13)==predicted,(Jx,Jy,Jz,T,D,C,Dm,Dp)
                    sign_checks+=1

    ratios=[]
    Jx,Jy,Jz=-1.0,-2.0,-3.0
    for T in (0.4,0.2,0.1,0.08):
        A,P,Z,nuc,Dc,Dm,Dp,um,up=edges(Jx,Jy,Jz,T)
        asym=(2*nuc/Dc)*T*math.exp(-2*A/T)
        ratios.append((Dp-Dm)/asym)
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    assert abs(ratios[-1]-1)<2e-7

    print("VERIFY_OK")
    print("edge_equation_checks =",edge_checks)
    print("concurrence_sign_checks =",sign_checks)
    print("low_T_width_ratio =",ratios[-1])
    A,P,Z,nuc,Dc,Dm,Dp,um,up=edges(-1.0,-2.0,-3.0,0.2)
    print("example_Dc =",Dc)
    print("example_Dminus =",Dm)
    print("example_Dplus =",Dp)

if __name__=="__main__":
    main()
