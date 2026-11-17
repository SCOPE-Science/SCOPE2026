#!/usr/bin/env python3
"""Independent numerical quadratic-programming check of one-negative ASM projections."""
import numpy as np
from scipy.optimize import minimize
from verify_one_defect import canonical, full_certificate, partial_asm_enum, partial_one_defect_certificate

def run():
    cases=0
    maximum=0.0
    for n in range(3,10):
        AA,X=full_certificate(n)
        target=np.array(AA,dtype=float)
        exact=np.array(X,dtype=float)
        matrix=[]
        for i in range(n):
            row=np.zeros((n,n));row[i,:]=1;matrix.append(row.ravel())
        for j in range(n-1):
            col=np.zeros((n,n));col[:,j]=1;matrix.append(col.ravel())
        E=np.stack(matrix)
        b=np.ones(2*n-1)
        objective=lambda z: .5*np.sum((z.reshape(n,n)-target)**2)
        grad=lambda z: z-target.ravel()
        z0=np.full(n*n,1/n)
        res=minimize(objective,z0,jac=grad,bounds=[(0,None)]*(n*n),constraints=[{'type':'eq','fun':lambda z:E@z-b,'jac':lambda z:E}],method='SLSQP',options={'ftol':1e-12,'maxiter':2500})
        assert res.success, (n,res.message)
        err=np.max(np.abs(res.x.reshape(n,n)-exact))
        maximum=max(maximum,err)
        assert err<3e-5,(n,err)
        assert abs(np.sum((res.x.reshape(n,n)-target)**2)-(2+2/(n+5)))<1e-7
        cases+=1
    partial_cases=0
    seen=set()
    for m,n in ((2,3),(3,3),(3,4),(4,4)):
        for A in partial_asm_enum(m,n):
            if sum(z==-1 for row in A for z in row)!=1: continue
            a,b=partial_one_defect_certificate(A)
            key=(m,n,a,b)
            if key in seen: continue
            seen.add(key)
            target=np.array(A,dtype=float)
            E=[]
            for i in range(m):
                row=np.zeros((m,n));row[i,:]=1;E.append(row.ravel())
            for j in range(n):
                col=np.zeros((m,n));col[:,j]=1;E.append(col.ravel())
            E=np.stack(E)
            obj=lambda z: .5*np.sum((z.reshape(m,n)-target)**2)
            grad=lambda z: z-target.ravel()
            res=minimize(obj,np.zeros(m*n),jac=grad,bounds=[(0,None)]*(m*n),constraints=[{'type':'ineq','fun':lambda z:np.ones(m+n)-E@z,'jac':lambda z:-E}],method='SLSQP',options={'ftol':1e-12,'maxiter':2500})
            assert res.success,(key,res.message)
            assert abs(np.sum((res.x.reshape(m,n)-target)**2)-(a+b)/2)<1e-7,key
            partial_cases+=1
    print(f'ONE_DEFECT_INDEPENDENT_QP_PASS full_orders={cases} partial_cases={partial_cases} max_coordinate_error={maximum:.3g}')
if __name__=='__main__':run()
