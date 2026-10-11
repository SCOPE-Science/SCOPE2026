#!/usr/bin/env python3
import math
import random

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def add_scaled(A0,A1,z0,z1):
    return [[z0*A0[i][j]+z1*A1[i][j] for j in range(2)] for i in range(2)]

def orthonormal_columns(m,rng):
    cols=[]
    for _ in range(2):
        v=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(m)]
        for u in cols:
            c=sum(u[k].conjugate()*v[k] for k in range(m))
            v=[v[k]-c*u[k] for k in range(m)]
        n=math.sqrt(sum(abs(z)**2 for z in v))
        cols.append([z/n for z in v])
    return cols

def random_channel(rng):
    cols=orthonormal_columns(4,rng)
    W=[[cols[j][i] for j in range(2)] for i in range(4)]
    return [W[0],W[1]],[W[2],W[3]]

def determinant_matrix(A0,A1):
    m00=det2(A0)
    m11=det2(A1)
    Ap=[[A0[i][j]+A1[i][j] for j in range(2)] for i in range(2)]
    m01=(det2(Ap)-m00-m11)/2
    return [[m00,m01],[m01,m11]]

def singular_values_2x2(M):
    h00=abs(M[0][0])**2+abs(M[1][0])**2
    h11=abs(M[0][1])**2+abs(M[1][1])**2
    h01=M[0][0].conjugate()*M[0][1]+M[1][0].conjugate()*M[1][1]
    tr=h00+h11
    disc=math.sqrt(max(0.0,(h00-h11)**2+4*abs(h01)**2))
    return math.sqrt(max(0.0,(tr+disc)/2)),math.sqrt(max(0.0,(tr-disc)/2))

def remix_pair(A0,A1,U):
    return [add_scaled(A0,A1,U[k][0],U[k][1]) for k in range(2)]

def random_unitary_2(rng):
    cols=orthonormal_columns(2,rng)
    return [[cols[j][i] for j in range(2)] for i in range(2)]

def determinant_sum(A0,A1,cols):
    x,y=cols
    return sum(abs(det2(add_scaled(A0,A1,x[k],y[k]))) for k in range(len(x)))

def tp_error(A0,A1):
    S=[[0j,0j],[0j,0j]]
    for A in (A0,A1):
        for i in range(2):
            for j in range(2):
                S[i][j]+=sum(A[k][i].conjugate()*A[k][j] for k in range(2))
    return max(abs(S[i][j]-(1 if i==j else 0)) for i in range(2) for j in range(2))

def main():
    for p in (0.0,0.1,0.35,0.5,0.9,0.99):
        A0=[[1.0,0.0],[0.0,math.sqrt(1-p)]]
        A1=[[0.0,math.sqrt(p)],[0.0,0.0]]
        s1,s2=singular_values_2x2(determinant_matrix(A0,A1))
        assert abs(s1-math.sqrt(1-p))<2e-12
        assert s2<2e-8

    for p in (0.1,0.25,0.5,0.7,0.9):
        A0=[[math.sqrt(p),0.0],[0.0,math.sqrt(p)]]
        A1=[[math.sqrt(1-p),0.0],[0.0,-math.sqrt(1-p)]]
        s1,s2=singular_values_2x2(determinant_matrix(A0,A1))
        hi=(1+s1+s2)/2
        lo=(1+s1-s2)/2
        assert abs(hi-1.0)<2e-12
        assert abs(lo-max(p,1-p))<2e-12
        # In this signed determinant basis, the real Hadamard attains the minimum.
        U=[[1/math.sqrt(2),1/math.sqrt(2)],[-1/math.sqrt(2),1/math.sqrt(2)]]
        B=remix_pair(A0,A1,U)
        f=0.5+0.5*sum(abs(det2(X)) for X in B)
        assert abs(f-lo)<2e-12

    rng=random.Random(424242)
    bound_checks=invariance_checks=tp_checks=0
    for _ in range(120):
        A0,A1=random_channel(rng)
        assert tp_error(A0,A1)<3e-12
        tp_checks+=1
        s1,s2=singular_values_2x2(determinant_matrix(A0,A1))
        U=random_unitary_2(rng)
        B0,B1=remix_pair(A0,A1,U)
        t1,t2=singular_values_2x2(determinant_matrix(B0,B1))
        assert abs(s1-t1)<3e-10 and abs(s2-t2)<3e-10
        invariance_checks+=1
        for m in (2,3,4,5,6):
            cols=orthonormal_columns(m,rng)
            ds=determinant_sum(A0,A1,cols)
            assert ds >= s1-s2-5e-10
            assert ds <= s1+s2+5e-10
            bound_checks+=1

    print("VERIFY_OK")
    print("random_rank2_channels =",tp_checks)
    print("takagi_invariance_checks =",invariance_checks)
    print("finite_representation_bound_checks =",bound_checks)
    print("amplitude_damping_invariance = OK")
    print("dephasing_extrema = OK")

if __name__=="__main__":
    main()
