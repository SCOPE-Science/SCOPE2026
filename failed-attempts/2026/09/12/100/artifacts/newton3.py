"""Newton polish A,B jointly; test period-2 hypothesis: P(P(A)) vs A."""
import numpy as np
exec(open('output/artifacts/refine1.py').read().split('A=np.array')[0])
A=np.array([-0.86788293,3.29968203]);B=np.array([0.86781168,3.29895488])
def newt(x0,nit=15):
    x=np.array(x0,float)
    for it in range(nit):
        y,t,DP,sc=pmap(x)
        d=np.array([((y[0]-x[0]+np.pi)%(2*np.pi))-np.pi,y[1]-x[1]])
        print(f"  it{it} x=({x[0]:.7f},{x[1]:.7f}) |d|={np.linalg.norm(d):.3e} T={t:.5f}")
        if np.linalg.norm(d)<1e-12: break
        x=x+np.linalg.solve(DP-np.eye(2),-d); x[0]=((x[0]+np.pi)%(2*np.pi))-np.pi
    return x
print("polish A:"); A2=newt(A)
print("polish B:"); B2=newt(B)
print("A*=",A2,"B*=",B2)
# image of A* under P should be near B* if same orbit hits section twice per period?
yA,tA,_,_=pmap(A2); yB,tB,_,_=pmap(B2)
print("P(A*)=",yA," T=",tA, " dist to B*:",np.linalg.norm([((yA[0]-B2[0]+np.pi)%(2*np.pi))-np.pi,yA[1]-B2[1]]))
print("P(B*)=",yB," T=",tB, " dist to A*:",np.linalg.norm([((yB[0]-A2[0]+np.pi)%(2*np.pi))-np.pi,yB[1]-A2[1]]))
# eig at polished points
for nm,x in [("A*",A2),("B*",B2)]:
    y,t,DP,sc=pmap(x)
    print(nm,"DP eig abs:",np.abs(np.linalg.eigvals(DP)),"det:",np.linalg.det(DP),"T:",t)
